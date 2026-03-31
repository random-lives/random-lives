"""LLM-based polity classification for indeterminate sampled people.

Provides batched classification of people whose birth location/year can't be
deterministically assigned to a polity. Uses GPT with per-country canonical
name lists for naming consistency.
"""

import json
import re
import random
from collections import Counter
from llm_utils import get_client, CostTracker, llm_call, extract_json
from polity_assignments_data import (
    ASSIGNMENT, CHINA_CORE_DYNASTIES, CHINA_ADDITIONAL,
    INDIA_SUBREGION, UK_SUBREGION_ASSIGNMENTS,
)

# ── Canonical polity names ─────────────────────────────────────────────────

_EXCLUDE = {'NO_KNOWN_POLITIES', 'NOT_RELEVANT', 'not_relevant'}

# Common polities the LLM will encounter in indeterminate periods.
# Add entries here when a polity keeps appearing under inconsistent names.
EXTRA_CANONICAL_POLITIES = {
    'China': {
        'Southern Song Dynasty', 'Liao Dynasty',
        'Republic of China (Beijing)', 'Western Xia Dynasty',
        'Northern Yuan Dynasty', 'Western Zhou Dynasty', 'Eastern Zhou Dynasty',
        'State of Qi', 'State of Chu', 'State of Qin', 'State of Wei',
        'State of Han', 'State of Yan', 'State of Jin', 'State of Wu', 'State of Yue',
        'Liang Dynasty', 'Northern Wei Dynasty',
        'Golden Horde', 'Chagatai Khanate',
        'Reorganized National Government of the Republic of China',
    },
    'India': {
        'Nawabdom of Bengal', 'Nawabdom of Awadh',
        'Golconda Sultanate', 'Maratha Kingdom',
        'Sena Dynasty', 'Satavahana Dynasty',
        'Kakatiya Dynasty', 'Ahom Kingdom',
        'Kingdom of Mysore', 'Hyderabad State',
        'Pandya Dynasty', 'Hoysala Empire', 'Bahmani Sultanate',
        'Bijapur Sultanate', 'Nagvanshi Dynasty', 'Chandela Dynasty',
        'Eastern Ganga Dynasty', 'Seuna (Yadava) Dynasty',
        'Paramara Dynasty', 'Sur Empire', 'Sikh Empire',
        'Kingdom of Mewar', 'Kingdom of Amber', 'Kingdom of Marwar',
        'Kingdom of Kutch', 'Kingdom of Singhbhum', 'Chero Kingdom',
        'Garha Kingdom', 'Gwalior State', 'Rewa State',
        'Kingdom of Venad', 'Kingdom of Manipur', 'Kingdom of Tripura',
        'Western Chalukya Empire', 'Vakataka Dynasty', 'Maitraka Dynasty',
        'Shunga Empire', 'Samma Dynasty', 'Kingdom of Kashmir',
    },
    'Bangladesh': {
        'East India Company', 'Mughal Empire',
        'Pala Empire', 'Sena Dynasty',
        'Bengal Sultanate', 'Nawabdom of Bengal',
    },
    'Russia': {
        'Russian Empire', 'Tsardom of Russia',
        'Golden Horde', 'Novgorod Republic',
        'Khazar Khaganate',
    },
    'France': {
        'French Third Republic', 'Kingdom of France',
        'Duchy of Brittany', 'Duchy of Burgundy', 'Duchy of Normandy',
        'Duchy of Aquitaine', 'County of Toulouse', 'County of Flanders',
        'County of Champagne', 'Frankish Kingdom',
    },
    'Germany': {
        'German Democratic Republic', 'Federal Republic of Germany',
        'Kingdom of Prussia', 'German Empire',
    },
    'Turkey': {
        'Seljuk Empire', 'Byzantine Empire',
        'Seljuk Sultanate of Rûm',
    },
    'Iran': {
        'Sassanid Empire', 'Seljuk Empire', 'Buyid Dynasty', 'Safavid Empire',
        'Saffarid Dynasty', 'Ghaznavid Empire', 'Ghurid Empire',
    },
    'Pakistan': {
        'Durrani Empire', 'Sikh Empire', 'Ghaznavid Empire',
        'Samma Dynasty',
    },
    'Egypt': {
        'Old Kingdom of Egypt', 'Middle Kingdom of Egypt', 'New Kingdom of Egypt',
        'Ptolemaic Kingdom',
    },
    'Sudan': {
        'New Kingdom of Egypt', 'Middle Kingdom of Egypt',
        'Kingdom of Kush',
    },
    'Italy': {
        'Kingdom of Naples', 'Kingdom of Sicily', 'Papal States',
        'Republic of Venice', 'Republic of Genoa', 'Duchy of Milan',
    },
    'Poland': {
        'Kingdom of Poland', 'Polish–Lithuanian Commonwealth',
    },
    'Ukraine': {
        'Polish–Lithuanian Commonwealth', 'Crimean Khanate',
    },
    'Korea, Republic of': {'Joseon Dynasty'},
    'Korea, Dem. People\'s Rep. of': {'Joseon Dynasty'},
    'Ethiopia': {
        'Ethiopian Empire', 'Kingdom of Aksum',
    },
    'Morocco': {
        'Marinid Sultanate', 'Saadi Sultanate',
        'French Protectorate in Morocco',
    },
    'Afghanistan': {
        'Ghaznavid Empire', 'Ghurid Empire',
        'Hephthalite Empire',
    },
    'Sri Lanka': {
        'Anuradhapura Kingdom',
    },
    'Cambodia': {
        'Khmer Empire',
    },
    'Iraq': {
        'Abbasid Caliphate',
    },
    'Mexico': {
        'Spanish Mexico',
    },
    'Nigeria': {
        'Kanem–Bornu Empire', 'Songhai Empire',
    },
}


def get_canonical_polities(country):
    """Return sorted list of canonical polity names for a country."""
    polities = set()

    if country in ASSIGNMENT:
        for start, end, polity in ASSIGNMENT[country]:
            if polity not in _EXCLUDE:
                polities.add(polity)

    if country == 'China':
        for start, end, polity in CHINA_CORE_DYNASTIES:
            polities.add(polity)
        for entries in CHINA_ADDITIONAL.values():
            for start, end, polity in entries:
                polities.add(polity)

    if country == 'India':
        for entries in INDIA_SUBREGION.values():
            for start, end, polity in entries:
                polities.add(polity)

    if country == 'United Kingdom':
        for entries in UK_SUBREGION_ASSIGNMENTS.values():
            for start, end, polity in entries:
                if polity not in _EXCLUDE:
                    polities.add(polity)

    if country in EXTRA_CANONICAL_POLITIES:
        polities |= EXTRA_CANONICAL_POLITIES[country]

    return sorted(polities)


# ── Name normalization ─────────────────────────────────────────────────────

_TITLE_WORDS = re.compile(
    r'\b(dynasty|empire|kingdom|sultanate|republic|caliphate|'
    r'khanate|principality|duchy|county)\b', re.IGNORECASE
)

def normalize_polity_name(name):
    """Capitalize polity-type words (dynasty → Dynasty, etc.)."""
    if name == 'NO_POLITY':
        return name
    return _TITLE_WORDS.sub(lambda m: m.group().capitalize(), name)


# ── Post-classification alias merging ─────────────────────────────────────
# Maps variant names → single canonical name. Applied after normalize_polity_name.
# Add entries here when the same polity appears under multiple names.

POLITY_ALIASES = {
    # Spelling variants
    'Sasanian Empire': 'Sassanid Empire',
    'Polish–Lithuanian Commonwealth': 'Polish-Lithuanian Commonwealth',
    "Kievan Rus'": "Kyivan Rus'",
    'Qajar Iran': 'Qajar dynasty',

    # Empire/Dynasty/Kingdom referring to same polity
    'Gurjara-Pratihara Dynasty': 'Gurjara-Pratihara Empire',
    'Gurjara-Pratihara Kingdom': 'Gurjara-Pratihara Empire',
    'Chola Dynasty': 'Chola Empire',
    'Chola Kingdom': 'Chola Empire',
    'Gahadavala Dynasty': 'Gahadavala Kingdom',
    'Pallava Kingdom': 'Pallava Dynasty',
    'Pandya Kingdom': 'Pandya Dynasty',
    'Kingdom of Kuru': 'Kuru Kingdom',
    'Kingdom of Kalinga': 'Kalinga Kingdom',
    'Kingdom of Funan': 'Funan Kingdom',
    'Great Seljuk Empire': 'Seljuk Empire',
    'Buyid Dynasty': 'Buyid Confederacy',
    'Western Ganga Kingdom': 'Western Ganga Dynasty',
    'Ganga Dynasty of Talakad': 'Western Ganga Dynasty',
    'Kingdom of Kamarupa': 'Kamarupa Kingdom',
    'Kamarupa Kingdom (Late Kamarupa)': 'Kamarupa Kingdom',
    'Kamarupa Kingdom (Pala Dynasty)': 'Kamarupa Kingdom',
    'Bastar Kingdom': 'Kingdom of Bastar',
    'Kingdom of Kalahandi': 'Kalahandi Kingdom',
    'Kalahandi State': 'Kalahandi Kingdom',
    'Tomara Dynasty': 'Tomara Dynasty of Delhi',
    'Katyuri Dynasty': 'Katyuri Kingdom',
    'Kingdom of Ladakh (Namgyal Dynasty)': 'Kingdom of Ladakh',

    # Verbose qualifiers → shorter canonical
    'Chaulukya Dynasty': 'Chaulukya (Solanki) Dynasty',
    'Chaulukya Dynasty (Solanki Kingdom of Gujarat)': 'Chaulukya (Solanki) Dynasty',
    'Kadamba Dynasty of Banavasi': 'Kadamba Dynasty',
    'Mahameghavahana Kingdom of Kalinga': 'Mahameghavahana Dynasty',
    'Eastern Chalukya Kingdom of Vengi': 'Eastern Chalukya Dynasty',
    'Eastern Chalukya Dynasty of Vengi': 'Eastern Chalukya Dynasty',
    'Eastern Chalukya Dynasty of Vengi (Chola-Chalukya)': 'Eastern Chalukya Dynasty',
    'Hindu Shahi Kingdom of Lahore': 'Hindu Shahi Kingdom',
    'Hindu Shahi Dynasty': 'Hindu Shahi Kingdom',
    'Chera Perumal Kingdom of Mahodayapuram': 'Chera Perumal Kingdom',
    'Chera Dynasty (Kingdom of Mahodayapuram)': 'Chera Perumal Kingdom',
    'Kalachuri (Chedi) Kingdom of Tripuri': 'Kalachuri Dynasty of Tripuri',
    'Kalachuri Kingdom of Tripuri': 'Kalachuri Dynasty of Tripuri',
    'Kalachuri Dynasty of Ratnapura': 'Kalachuri Kingdom of Ratnapura',
    'Kalachuri Kingdom of Ratanpur': 'Kalachuri Kingdom of Ratnapura',

    # Empire/Dynasty/Kingdom suffix variants (same polity, different label)
    'Maratha Kingdom': 'Maratha Empire',
    'Chera Kingdom': 'Chera Dynasty',
    'Khmer Kingdom': 'Khmer Empire',
    'Toungoo Dynasty': 'Toungoo Empire',
    'Almoravid Dynasty': 'Almoravid Empire',
    'Lan Xang Kingdom': 'Lan Xang',
    'Merovingian Kingdom of the Franks': 'Merovingian Frankish Kingdom',
    'Southern Han Dynasty': 'Southern Han',
    'Median Kingdom': 'Median Empire',
    'Mitanni': 'Mitanni Kingdom',
    'Balhae Kingdom': 'Balhae (Bohai) Kingdom',
    'Sikh Confederacy': 'Sikh Empire',
    'Early Chalukya Dynasty': 'Chalukya Dynasty of Badami',
    'Frankish Empire': 'Frankish Kingdom',

    # "Kingdom of X" vs "X Kingdom" (same polity, word order variant)
    'Kingdom of Garhwal': 'Garhwal Kingdom',
    'Gauda Kingdom': 'Kingdom of Gauda',
    'Kingdom of Matsya': 'Matsya Kingdom',
    'Kolathunadu Kingdom': 'Kingdom of Kolathunadu',
    'Kingdom of Bushahr': 'Bushahr Kingdom',
    'Kamata Kingdom': 'Kingdom of Kamata',
    'Kingdom of Kumaon': 'Kumaon Kingdom',
    'Kingdom of Madra': 'Madra Kingdom',
    'Kingdom of Gandhara': 'Gandhara Kingdom',
    'Sultanate of Darfur': 'Darfur Sultanate',

    # Capitalization / spelling inconsistencies in deterministic data
    'Afsharid dynasty': 'Afsharid Dynasty',
    'Afsharid Empire': 'Afsharid Dynasty',
    'Safavid / Afsharid Iran': 'Afsharid Dynasty',
}


def merge_polity_name(name):
    """Map variant polity names to their canonical form."""
    return POLITY_ALIASES.get(name, name)


# ── Broad groupings for "meta-polity" ranking ─────────────────────────────
# Maps individual polity names → broader entity. Only used for the optional
# grouped ranking view, not for the main per-polity ranking.

POLITY_GROUPS = {
    # ── Roman world ──
    'Roman Kingdom': 'Roman civilization',
    'Roman Republic': 'Roman civilization',
    'Roman Empire': 'Roman civilization',
    'Western Roman Empire': 'Roman civilization',
    'Byzantine Empire': 'Roman civilization',
    'Empire of Trebizond': 'Roman civilization',
    'Empire of Nicaea': 'Roman civilization',
    'Principality of Achaea': 'Roman civilization',
    'Kingdom of Athens': 'Roman civilization',

    # ── German Empire ──
    'German Empire': 'German Empire (broad)',
    'Weimar Republic': 'German Empire (broad)',
    'Nazi Germany': 'German Empire (broad)',
    'Federal Republic of Germany': 'German Empire (broad)',
    'German Democratic Republic': 'German Empire (broad)',
    'German Reich': 'German Empire (broad)',

    # ── Russian/Soviet ──
    'Tsardom of Russia': 'Russian Empire / USSR',
    'Russian Empire': 'Russian Empire / USSR',
    'Russian Soviet Federative Socialist Republic': 'Russian Empire / USSR',
    'Soviet Union': 'Russian Empire / USSR',
    'Russian Federation': 'Russian Empire / USSR',
    'Grand Principality of Moscow': 'Russian Empire / USSR',
    'Grand Duchy of Moscow': 'Russian Empire / USSR',
    'Grand Principality of Vladimir': 'Russian Empire / USSR',
    'Novgorod Republic': 'Russian Empire / USSR',
    'Principality of Chernigov': 'Russian Empire / USSR',
    'Principality of Tver': 'Russian Empire / USSR',
    'Principality of Ryazan': 'Russian Empire / USSR',
    'Don Cossack Host': 'Russian Empire / USSR',
    'Cossack Hetmanate': 'Russian Empire / USSR',

    # ── Mongol Empire ──
    'Mongol Empire': 'Mongol Empire (broad)',
    'Golden Horde': 'Mongol Empire (broad)',
    'Chagatai Khanate': 'Mongol Empire (broad)',
    'Ilkhanate': 'Mongol Empire (broad)',

    # ── Imperial China (main-line historiographical dynasties) ──
    'Qin Dynasty': 'Imperial China',
    'Western Han Dynasty': 'Imperial China',
    'Xin Dynasty': 'Imperial China',
    'Eastern Han Dynasty': 'Imperial China',
    'Western Jin Dynasty': 'Imperial China',
    'Sui Dynasty': 'Imperial China',
    'Tang Dynasty': 'Imperial China',
    'Northern Song Dynasty': 'Imperial China',
    'Southern Song Dynasty': 'Imperial China',
    'Song Dynasty': 'Imperial China',
    'Yuan Dynasty': 'Imperial China',
    'Ming Dynasty': 'Imperial China',
    'Qing Dynasty': 'Imperial China',

    # ── Japanese ──
    'Heian Period': 'Japan (all periods)',
    'Kamakura Shogunate': 'Japan (all periods)',
    'Kenmu Restoration': 'Japan (all periods)',
    'Muromachi Shogunate': 'Japan (all periods)',
    'Toyotomi Regime': 'Japan (all periods)',
    'Tokugawa Shogunate': 'Japan (all periods)',
    'Empire of Japan': 'Japan (all periods)',
    'Japan': 'Japan (all periods)',
    'Nara Period': 'Japan (all periods)',
    'Japanese Korea': 'Japan (all periods)',
    'Japanese Taiwan': 'Japan (all periods)',
    'Japanese East Indies': 'Japan (all periods)',
    'Japanese Hong Kong': 'Japan (all periods)',
    'Japanese Singapore': 'Japan (all periods)',
    'Manchukuo': 'Japan (all periods)',

    # ── United States ──
    'American Philippines': 'United States (broad)',
    'United States': 'United States (broad)',
    'US occupation of Haiti': 'United States (broad)',
    'US occupation of Dominican Republic': 'United States (broad)',
    'US military occupation of Cuba': 'United States (broad)',
    'United States Army Military Government in Korea': 'United States (broad)',

    # ── Ancient Egypt (pharaonic through Ptolemaic) ──
    'Old Kingdom of Egypt': 'Ancient Egypt',
    'Middle Kingdom of Egypt': 'Ancient Egypt',
    'New Kingdom of Egypt': 'Ancient Egypt',
    'Twenty-first Dynasty Egypt': 'Ancient Egypt',
    'Twenty-second Dynasty Egypt': 'Ancient Egypt',
    'Twenty-third Dynasty Egypt': 'Ancient Egypt',
    'Twenty-fifth Dynasty Egypt': 'Ancient Egypt',
    'Twenty-sixth Dynasty Egypt': 'Ancient Egypt',
    'Hyksos Kingdom of Avaris': 'Ancient Egypt',
    'Ptolemaic Kingdom': 'Ancient Egypt',


}


def group_polity_name(name):
    """Map a polity to its broad group, or return the name unchanged."""
    return POLITY_GROUPS.get(name, name)


# ── Overlapping "super-groups" ────────────────────────────────────────────
# These allow a polity to belong to multiple groups (e.g., Yuan Dynasty is
# both Imperial China and Mongol Empire). Computed separately from the main
# non-overlapping POLITY_GROUPS ranking.

POLITY_OVERLAYS = {
    # ── British Empire ──
    # All polities under British Crown control. Polities with "British" in the
    # name count for their full range; dominions/successor states have end dates.
    'British Empire': {
        # Core
        ('Kingdom of England', None, None),
        ('Kingdom of Scotland', None, None),
        ('Kingdom of Ireland', None, None),
        ('Lordship of Ireland', None, None),
        ('United Kingdom of Great Britain and Ireland', None, None),
        ('United Kingdom', None, None),
        # India
        ('East India Company', None, None),
        ('British Raj', None, None),
        ('Dominion of India', None, None),
        ('Dominion of Pakistan', None, None),
        # Named British colonies/protectorates (always count)
        ('British Burma', None, None),
        ('British Ceylon', None, None),
        ('Dominion of Ceylon', None, None),
        ('British Egypt', None, None),
        ('British Malaya', None, None),
        ('British Singapore', None, None),
        ('British Hong Kong', None, None),
        ('British Uganda', None, None),
        ('British Jamaica', None, None),
        ('British Guiana', None, None),
        ('British Somaliland', None, None),
        ('British North America', None, None),
        ('Colony and Protectorate of Nigeria', None, None),
        ('Colony and Protectorate of Kenya', None, None),
        ('British Central Africa / Nyasaland', None, None),
        ('British Sierra Leone', None, None),
        ('Gold Coast', None, None),
        ('British Mandate of Mesopotamia', None, None),
        ('British Mandate of Palestine', None, None),
        ('British Mandate of Transjordan', None, None),
        ('British Cyprus', None, None),
        ('British protectorate of Bahrain', None, None),
        ('British protectorate of Kuwait', None, None),
        ('British protectorate of Qatar', None, None),
        ('British South Africa Company (Rhodesia)', None, None),
        ('Southern Rhodesia', None, None),
        ('Northern Rhodesia', None, None),
        ('Federation of Rhodesia and Nyasaland', None, None),
        ('British East Africa Protectorate', None, None),
        ('Anglo-Egyptian Sudan', None, None),
        ('Union of South Africa', None, None),
        ('Northern Nigeria Protectorate', None, None),
        ('Southern Nigeria Protectorate', None, None),
        ('Niger Coast Protectorate', None, None),
        ('Lagos Colony', None, None),
        ('Royal Niger Company', None, None),
        ('Australian Papua New Guinea', None, None),
        ('Crown Colony of Barbados', None, None),
        ('Colony of the Bahamas', None, None),
        ('Colony of Saint Vincent', None, None),
        ('Federated Malay States', None, None),
        ('Raj of Sarawak', None, None),
        ('Colony of New South Wales', None, None),
        ('Colony of Virginia', None, None),
        ('Province of Maryland', None, None),
        ('Delaware Colony', None, None),
        ('Antigua and Barbuda', None, 1981),
        # Dominions (independent name, still British until Statute of Westminster / later)
        ('Canada', None, 1931),
        ('Australia', None, 1942),   # adopted Statute of Westminster in 1942
        ('New Zealand', None, 1947), # adopted Statute of Westminster in 1947
        ('South African Republic', None, None),  # Boer state, but conquered by British
        ('Irish Free State', None, None),
        ('Rhodesia', None, None),
    },

    # ── French Empire ──
    'French Empire': {
        # Metropolitan France
        ('Kingdom of France', None, None),
        ('French First Republic', None, None),
        ('First French Empire', None, None),
        ('Bourbon Restoration', None, None),
        ('July Monarchy', None, None),
        ('French Second Republic', None, None),
        ('Second French Empire', None, None),
        ('French Third Republic', None, None),
        ('Provisional Government of the French Republic', None, None),
        ('French Fourth Republic', None, None),
        ('French Fifth Republic', None, None),
        # Colonies
        ('French West Africa', None, None),
        ('French Equatorial Africa', None, None),
        ('French Algeria', None, None),
        ('French Indochina', None, None),
        ('French Madagascar', None, None),
        ('French Protectorate of Tunisia', None, None),
        ('French Protectorate in Morocco', None, None),
        ('French Mandate of Syria', None, None),
        ('French Mandate of Lebanon', None, None),
        ('French Togoland', None, None),
        ('French Saint-Domingue', None, None),
        ('French Cochinchina', None, None),
        ('French Protectorate of Tonkin', None, None),
        ('French Second Colonial Empire', None, None),
        ('French India', None, None),
        ("French India (Établissements français dans l'Inde)", None, None),
        ('French Antilles', None, None),
        ('Martinique', None, None),
    },

    # ── Spanish Empire ──
    'Spanish Empire': {
        ('Crown of Castile', None, None),
        ('Kingdom of Castile', None, None),
        ('Crown of Aragon', None, None),
        ('Kingdom of Aragon', None, None),
        ('Kingdom of León', None, None),
        ('Kingdom of Navarre', None, None),
        ('Habsburg Spain', None, None),
        ('Bourbon Spain', None, None),
        ('Kingdom of Spain', None, None),
        ('Bourbon Restoration Spain', None, None),
        ('Spanish Second Republic', None, None),
        ('Francoist Spain', None, None),
        ('Iberian Union', None, None),
        ('Spanish Mexico', None, None),
        ('New Spain', None, None),
        ('Spanish Peru', None, None),
        ('Viceroyalty of Peru', None, None),
        ('Spanish New Granada', None, None),
        ('Spanish Guatemala', None, None),
        ('Spanish Venezuela', None, None),
        ('Spanish Ecuador', None, None),
        ('Spanish Cuba', None, None),
        ('Spanish Paraguay', None, None),
        ('Spanish Jamaica', None, None),
        ('Spanish Santo Domingo', None, None),
        ('Spanish Upper Peru', None, None),
        ('Spanish Río de la Plata', None, None),
        ('Río de la Plata (Spanish colonial administration)', None, None),
        ('Captaincy General of the Philippines', None, None),
        ('Captaincy General of Chile', None, None),
        ('Captaincy General of Puerto Rico', None, None),
        ('Commonwealth of Puerto Rico', None, None),
    },

    # ── Portuguese Empire ──
    'Portuguese Empire': {
        ('Kingdom of Portugal', None, None),
        ('Portuguese First Republic', None, None),
        ('Ditadura Nacional', None, None),
        ('Estado Novo', None, None),
        ('Portuguese Third Republic', None, None),
        ('United Kingdom of Portugal, Brazil and the Algarves', None, None),
        ('Portuguese Brazil', None, None),
        ('Portuguese Angola', None, None),
        ('Portuguese Mozambique', None, None),
        ('Portuguese Guinea', None, None),
        ('Portuguese Ceylon', None, None),
        ('Captaincy of Bahia', None, None),
        ('Captaincy of Pernambuco', None, None),
        ('Captaincy of Espírito Santo', None, None),
        ('Captaincy of Rio Grande', None, None),
    },

    # ── Dutch Empire ──
    'Dutch Empire': {
        ('Dutch Republic', None, None),
        ('Kingdom of the Netherlands', None, None),
        ('United Kingdom of the Netherlands', None, None),
        ('Sovereign Principality of the United Netherlands', None, None),
        ('Batavian Republic', None, None),
        ('Dutch East Indies', None, None),
        ('Dutch Ceylon', None, None),
        ('Dutch East India Company', None, None),
    },

    # Habsburg: every polity under Habsburg rule at the time.
    'Habsburg domains': {
        # Direct Habsburg rule (with year ranges)
        # Format: (polity_name, start_year, end_year)
        ('Habsburg Spain', None, None),
        ('Iberian Union', None, None),
        ('Habsburg Monarchy', None, None),
        ('Austrian Empire', None, None),
        ('Austria-Hungary', None, None),
        ('Spanish Netherlands', None, None),
        ('Austrian Netherlands', None, None),
        ('Kingdom of Lombardy–Venetia', None, None),
        ('Grand Principality of Transylvania', None, None),
        ('Kingdom of Hungary', 1526, 1918),
        ('Kingdom of Bohemia', 1526, 1918),
        ('Duchy of Milan', 1535, 1714),
        ('Kingdom of Naples', 1504, 1714),
        ('Kingdom of Sicily', 1516, 1714),
        ('Kingdom of Sardinia', 1708, 1720),
        # Habsburg Spain's colonies (1516-1700)
        ('Spanish Mexico', 1516, 1700),
        ('New Spain', 1516, 1700),
        ('Spanish Peru', 1516, 1700),
        ('Viceroyalty of Peru', 1516, 1700),
        ('Spanish New Granada', 1516, 1700),
        ('Spanish Guatemala', 1516, 1700),
        ('Spanish Venezuela', 1516, 1700),
        ('Spanish Ecuador', 1516, 1700),
        ('Spanish Cuba', 1516, 1700),
        ('Spanish Paraguay', 1516, 1700),
        ('Spanish Upper Peru', 1516, 1700),
        ('Spanish Río de la Plata', 1516, 1700),
        ('Captaincy General of the Philippines', 1516, 1700),
        ('Captaincy General of Chile', 1516, 1700),
        ('Spanish Jamaica', 1516, 1655),
        ('Spanish Santo Domingo', 1516, 1700),
    },

    # Caliphate: the mainline caliphal succession
    'Caliphate (mainline)': {
        ('Rashidun Caliphate', None, None),
        ('Umayyad Caliphate', None, None),
        ('Abbasid Caliphate', None, None),
    },

    # Mongol Empire: Genghisid khanates with direct dynastic continuity
    'Mongol Empire (Genghisid)': {
        ('Mongol Empire', None, None),
        ('Yuan Dynasty', None, None),
        ('Northern Yuan Dynasty', None, None),
        ('Golden Horde', None, None),
        ('Chagatai Khanate', None, None),
        ('Ilkhanate', None, None),
    },
}


def compute_overlay_total(overlay_members, people, records, merge_fn):
    """Compute total for a time-aware overlay group.

    overlay_members: set of (polity_name, start_year_or_None, end_year_or_None)
    people: list of Person objects
    records: list of dicts with 'polity', 'status', 'birth_year'

    Returns count of people matching any member (with year constraints).
    """
    count = 0
    for rec in records:
        if rec['status'] not in ('assigned',):
            continue
        polity = merge_fn(rec['polity'])
        year = rec['birth_year']
        for member_name, start, end in overlay_members:
            if polity == member_name:
                if (start is None or year >= start) and (end is None or year <= end):
                    count += 1
                    break
    return count


# ── Prompt construction ────────────────────────────────────────────────────

SYSTEM_PROMPT_BASE = """You are a historical geography expert. You will be given a list of people, \
each with a birth year, coordinates (lat/lon), modern country, and subnational region. For each \
person, identify the polity (state, empire, kingdom, dynasty, etc.) that directly administered \
their birth location at the time of their birth.

"Directly administered" means the polity that collected taxes, enforced laws, and appointed \
officials in that territory. Not a distant suzerain with nominal sovereignty, and not a \
sub-unit or province of a larger state.

For example:
- Medieval Brittany → Duchy of Brittany (not Kingdom of France, which had nominal suzerainty)
- A village in Mughal India → Mughal Empire (not the local subah, which was a subdivision)
- A city in Roman Egypt → Roman Empire (not the province of Aegyptus)

For European colonies, use the name of the colonial administration, not the metropolitan power.
For example: British Raj (not British Empire), Dutch East Indies (not Kingdom of the Netherlands).

Rules:
- Always give an answer, no matter how small or obscure the polity.
- Use the FULL formal name (e.g., "Mughal Empire" not "Mughals", "Tang Dynasty" not "Tang").
- Always capitalize: Dynasty, Empire, Kingdom, Sultanate, Republic, Caliphate, Khanate, \
Principality, Duchy, County.
- If genuinely uncertain between 2+ polities, pick the most likely one.
- If the area was genuinely stateless, return "NO_POLITY".

For each person, first give a brief justification, then return a JSON object.

Format:
1. [justification]
2. [justification]
...

```json
{"1": "Polity Name", "2": "Polity Name", ...}
```"""


def build_system_prompt(canonical_names=None):
    """Build system prompt, optionally appending canonical name list."""
    if not canonical_names:
        return SYSTEM_PROMPT_BASE
    names_str = ', '.join(canonical_names)
    return SYSTEM_PROMPT_BASE + f"""

IMPORTANT — Name consistency: The following polity names are already used in our database. \
When one of these is the correct answer, use the EXACT name shown:
  {names_str}

You may use other names for polities not in this list."""


# ── Classification ─────────────────────────────────────────────────────────

def latlon_from_rowcol(row, col):
    """Compute lat/lon from HYDE grid coordinates."""
    res = 0.0833
    lon = round(-180 + (col + 0.5) * res, 2)
    lat = round(90 - (row + 0.5) * res, 2)
    return lat, lon


def format_batch_prompt(batch):
    """Format batch of (index, country, subregion, year_str, lat, lon) into a prompt."""
    lines = ["People to classify:"]
    for idx, country, subregion, year_str, lat, lon in batch:
        lines.append(f"  {idx}. {year_str}, {lat}°N {lon}°E, {subregion}, {country}")
    return '\n'.join(lines)


def classify_batch(client, tracker, batch, canonical_names=None):
    """Classify a batch via LLM. Returns (dict of idx->polity, raw_text)."""
    messages = [
        {"role": "system", "content": build_system_prompt(canonical_names)},
        {"role": "user", "content": format_batch_prompt(batch)},
    ]
    raw = llm_call(client, messages, callbacks=[tracker] if tracker else [])
    result = extract_json(raw)
    if not result:
        print(f"  WARNING: Failed to parse JSON from response")
        return {}, raw
    result = {k: merge_polity_name(normalize_polity_name(v)) for k, v in result.items()}
    return result, raw


def sample_and_batch(indet_people, n_sample, batch_size=50, seed=42):
    """Sample indeterminate people, sort by (country, year), batch them.

    Returns (batches, sample_records) where each batch has:
      batch, orig_indices, countries, canonical_names, summary
    """
    rng = random.Random(seed)
    sample = rng.sample(indet_people, min(n_sample, len(indet_people)))

    records = []
    for orig_idx, p in sample:
        country = p.location.country
        subregion = getattr(p.location, 'subregion', None) or '?'
        lat, lon = latlon_from_rowcol(p.row, p.col)
        records.append((orig_idx, country, subregion, p.birth_year, p.birth_year_str, lat, lon))

    records.sort(key=lambda r: (r[1], r[3]))

    batches = []
    for i in range(0, len(records), batch_size):
        chunk = records[i:i + batch_size]
        batch = []
        countries = set()
        for j, (_, country, subregion, _, year_str, lat, lon) in enumerate(chunk, 1):
            batch.append((j, country, subregion, year_str, lat, lon))
            countries.add(country)

        canonical = set()
        for c in countries:
            canonical.update(get_canonical_polities(c))

        batches.append({
            'batch': batch,
            'orig_indices': [r[0] for r in chunk],
            'countries': countries,
            'canonical_names': sorted(canonical),
            'summary': f"{chunk[0][1]} {chunk[0][4]} … {chunk[-1][1]} {chunk[-1][4]}",
        })

    return batches, records


def _classify_one_batch(args):
    """Worker for parallel classification. Takes (client, tracker, batch_info, batch_idx, n_batches)."""
    client, tracker, b, batch_idx, n_batches = args
    print(f"Batch {batch_idx+1}/{n_batches}: {b['summary']} ...", end=' ', flush=True)
    batch_result, raw = classify_batch(client, tracker, b['batch'],
                                       canonical_names=b['canonical_names'])
    # Map back to original indices
    mapped = {}
    for local_idx_str, polity in batch_result.items():
        local_idx = int(local_idx_str) - 1
        if 0 <= local_idx < len(b['orig_indices']):
            mapped[b['orig_indices'][local_idx]] = polity
    print(f"✓ ({len(batch_result)} classified)")
    return mapped, raw


def run_classification(unclassified_people, n_sample, model='gpt-5.2', batch_size=100,
                       seed=42, max_workers=10):
    """End-to-end: sample, batch, classify (optionally in parallel).

    Args:
        unclassified_people: list of (orig_index, person) tuples
        n_sample: how many to sample
        model: LLM model name
        batch_size: people per LLM call
        seed: random seed
        max_workers: number of parallel API calls (1 = sequential)

    Returns (results, records, raw_responses, tracker).
    """
    batches, records = sample_and_batch(unclassified_people, n_sample, batch_size, seed)
    client = get_client(model)
    tracker = CostTracker(model)
    n_batches = len(batches)

    results = {}
    raw_responses = []

    if max_workers <= 1:
        for i, b in enumerate(batches):
            mapped, raw = _classify_one_batch((client, tracker, b, i, n_batches))
            results.update(mapped)
            raw_responses.append(raw)
    else:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        args_list = [(client, tracker, b, i, n_batches) for i, b in enumerate(batches)]
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = {pool.submit(_classify_one_batch, a): a[3] for a in args_list}
            for future in as_completed(futures):
                mapped, raw = future.result()
                results.update(mapped)
                raw_responses.append(raw)

    tracker.print_summary()
    return results, records, raw_responses, tracker
