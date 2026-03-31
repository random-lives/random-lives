"""
Complete polity control timelines for West/Central/East African countries:
Mali, Burkina Faso, Niger, Chad, Guinea, Senegal, Benin, Togo, Rwanda,
Burundi, Cote d'Ivoire, Somalia, Mauritania.

Rules:
- NO_KNOWN_POLITIES: earliest period until first polity with 100k+ under centralized control
- NOT_RELEVANT: polities existed but ALL had <100M lifetime births (avg_pop * 0.04 * years)
- Polity name: single polity controlled 99%+ of modern country's population
- Gap: polities with >100M lifetime births existed but none controlled 99%+
- End years exclusive. Negative years = BCE.

For every gap, justification is provided in comments.

Key lifetime-birth calculations for polities referenced:
- Mali Empire (~1235-1460, ~225 yrs, avg pop ~15M): 15M * 0.04 * 225 = 135M. EXCEEDS 100M.
- Songhai Empire (~1464-1591, ~127 yrs, avg pop ~8M): 8M * 0.04 * 127 = 40.6M. Under.
- Ghana Empire (~300-1200, ~900 yrs, avg pop ~2M): 2M * 0.04 * 900 = 72M. Under.
- Kanem-Bornu (~800-1900, ~1100 yrs, avg pop ~3M): 3M * 0.04 * 1100 = 132M. EXCEEDS 100M.
- Sokoto Caliphate (1804-1903, ~99 yrs, avg pop ~10M): 10M * 0.04 * 99 = 39.6M. Under.
- French Third Republic (1870-1940, 70 yrs, France ~38M avg): 38M * 0.04 * 70 = 106.4M. EXCEEDS 100M.
- French Fourth Republic (1946-1958, 12 yrs, France ~42M): 42M * 0.04 * 12 = 20.2M. Under.
- French State / Vichy (1940-1944, 4 yrs, ~40M): 40M * 0.04 * 4 = 6.4M. Under.
- Free France / GPRF (1940-1946, 6 yrs): under 100M.
- German Empire (1871-1918, 47 yrs, ~55M avg): 55M * 0.04 * 47 = 103.4M. EXCEEDS 100M.
- Kingdom of Italy (1861-1946, 85 yrs, ~35M avg): 35M * 0.04 * 85 = 119M. EXCEEDS 100M.
- Italian Republic (1946-present, 80 yrs, ~55M avg): 55M * 0.04 * 80 = 176M. EXCEEDS 100M.
- British Empire: clearly >100M lifetime births at any reasonable calculation.
- Belgian colonial empire / Kingdom of Belgium: under 100M lifetime births.
- Kingdom of Rwanda (pre-colonial, ~500 yrs, pop ~1.5M): under 100M.
- Kingdom of Burundi (pre-colonial, ~350 yrs, pop ~1M): under 100M.
- Post-independence African states (pop ~5-20M, ~65 yrs): all well under 100M.
- Almoravid Empire (~1040-1147, ~107 yrs, ~5M): under 100M.
- Oyo Empire (~1400-1835, ~435 yrs, ~3M): 52.2M. Under.
"""


# =============================================================================
# MALI
# =============================================================================

MALI = [
    # Earliest humans to first centralized polity with 100k+.
    # The Ghana Empire (centered in modern SE Mauritania / W Mali) had centralized
    # control with 100k+ by roughly 300-400 CE. Parts of northern/western Mali
    # were under Ghana's sphere. The Niger River valley had Djenné-Djenno from
    # ~250 BCE but this was a non-hierarchical urban cluster, not a centralized polity.
    (-200000, 300, 'NO_KNOWN_POLITIES'),

    # 300-1235: Ghana Empire, various successor states, Sosso Kingdom.
    # Ghana Empire (~300-1200): under 100M (72M). Sosso Kingdom tiny.
    # All polities under 100M lifetime births.
    (300, 1235, 'NOT_RELEVANT'),

    # GAP: 1235-1460
    # Mali Empire (135M lifetime births, EXCEEDS 100M) controlled the key population
    # centers of modern Mali along the Niger River (Timbuktu, Djenné, Gao, Niani).
    # At peak (~1350), it likely controlled >99% of population in modern Mali's borders,
    # but the empire's control waxed and waned, and the eastern Saharan margins and
    # some southern forest-edge peoples were outside its control at various times.
    # Cannot confirm 99% for the full 225-year period.

    # 1460-1893: Post-Mali fragmentation. Songhai (40.6M, under 100M), Bambara
    # kingdoms, Masina, Toucouleur Empire. All under 100M.
    (1460, 1893, 'NOT_RELEVANT'),

    # French colonial period. France progressively conquered from 1880s.
    # By 1893, most of modern Mali under French control (fall of Toucouleur Empire).
    # French Third Republic (1870-1940): 106.4M lifetime births. EXCEEDS 100M.
    # Controlled 99%+ of modern Mali's population from ~1893.
    (1893, 1940, 'French Third Republic'),

    # 1940-1960: Vichy France, Free France, French Fourth Republic.
    # All distinct regimes with <100M lifetime births individually.
    # Only polity controlling Mali in each sub-period: French State (1940-42),
    # Free France/GPRF (1942-46), French Fourth Republic (1946-58),
    # Sudanese Republic in French Community (1958-60). All under 100M.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Mali from September 22, 1960.
    # Pop ~5M-22M, avg ~12M over 66 yrs. 12M * 0.04 * 66 = 31.7M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# BURKINA FASO
# =============================================================================

BURKINA_FASO = [
    # The Mossi kingdoms emerged around the 11th-15th century in the central plateau.
    # Before that, the region had village-level societies. Ghana Empire influence
    # barely reached this territory. First centralized polity with 100k+ is
    # likely the Mossi kingdoms (~1200s), or possibly earlier trade-state influence.
    # Conservatively using 500 CE for emergence of organized chiefdoms that might
    # approach 100k. More likely ~1000 CE when Mossi precursors formed.
    (-200000, 1000, 'NO_KNOWN_POLITIES'),

    # 1000-1235: Early Mossi and other kingdoms forming. All under 100M lifetime births.
    # No polity with >100M lifetime births controlled any part of Burkina Faso.
    (1000, 1235, 'NOT_RELEVANT'),

    # GAP: 1235-1460
    # Mali Empire (>100M lifetime births) controlled western portions of modern
    # Burkina Faso (around Bobo-Dioulasso, the Mandinka-influenced west), while
    # Mossi kingdoms controlled the central/eastern plateau independently.
    # Neither controlled 99% of the population.

    # 1460-1896: Post-Mali period.
    # Songhai controlled northern/western parts (under 100M). Mossi kingdoms
    # in center. Gwiriko Kingdom in southwest. All under 100M lifetime births.
    (1460, 1897, 'NOT_RELEVANT'),

    # French conquest: France conquered the Mossi kingdoms in 1896-1897.
    # French Third Republic (>100M LB) controlled 99%+ from ~1897.
    (1897, 1940, 'French Third Republic'),

    # 1940-1960: Vichy, Free France, Fourth Republic. All <100M LB as distinct regimes.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Upper Volta / Burkina Faso.
    # Pop ~4M-22M, avg ~10M over 66 yrs. 10M * 0.04 * 66 = 26.4M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# NIGER
# =============================================================================

NIGER = [
    # Hausa city-states emerging ~1000 CE in southern Niger. Kanem-Bornu influenced
    # the Lake Chad region from ~800 CE. Ghana Empire influence in far west.
    (-200000, 300, 'NO_KNOWN_POLITIES'),

    # 300-800: No polity with >100M lifetime births in Niger's territory.
    # Ghana Empire (under 100M) influence barely reached western Niger.
    (300, 800, 'NOT_RELEVANT'),

    # GAP: 800-1900
    # Kanem-Bornu (>100M lifetime births over its full 800-1900 existence) controlled
    # eastern Niger around Lake Chad. From 1235, Mali Empire (>100M lifetime births)
    # controlled western Niger including the Niger River bend and Agadez.
    # Hausa city-states and Tuareg Air Sultanate in between.
    # No single polity controlled 99% of modern Niger's population.
    # Polities with >100M LB present: Kanem-Bornu (east), Mali Empire (west, 1235-1460).

    # French conquest completed ~1900-1906. Military territory of Niger established 1900.
    (1900, 1940, 'French Third Republic'),

    # 1940-1960: Vichy, Free France, Fourth Republic. All <100M LB.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Niger. Pop ~3M-25M, avg ~10M over 66 yrs.
    # 10M * 0.04 * 66 = 26.4M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# CHAD
# =============================================================================

CHAD = [
    # Sao civilization near Lake Chad from ~500 CE, but these were chiefdoms likely
    # below 100k centralized. Kanem Empire from ~800 CE is the first polity
    # with 100k+ under centralized control in this territory.
    (-200000, 800, 'NO_KNOWN_POLITIES'),

    # GAP: 800-1913
    # Kanem-Bornu (>100M lifetime births over full 800-1900 existence) was centered
    # in what is now Chad around Lake Chad. However, it never controlled 99% of
    # modern Chad's territory/population:
    # - Southern Chad (Sara peoples) were independent
    # - Eastern Chad: Wadai Sultanate (~1600s-1909) was independent
    # - Northern Saharan regions (Tibesti, Borkou) had independent Toubou peoples
    # - Sultanate of Baguirmi was sometimes independent
    # Polity with >100M LB: Kanem-Bornu.

    # French conquest: France established control over most of Chad by 1913.
    # Battle of Kousséri (1900) defeated Rabih az-Zubayr. Wadai conquered 1909-1912.
    (1913, 1940, 'French Third Republic'),

    # Chad rallied to Free France in August 1940 under Governor Éboué.
    # Free France/GPRF, then Fourth Republic: all <100M LB as distinct regimes.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Chad. Pop ~3M-18M, avg ~8M over 66 yrs.
    # 8M * 0.04 * 66 = 21.1M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# GUINEA
# =============================================================================

GUINEA = [
    # The Susu and Mandinka peoples established kingdoms in this area.
    # Centralized polities with 100k+ emerged with the expansion of the Mali Empire
    # (~1235) or possibly earlier Mandinka chiefdoms. The Sosso Kingdom (~1180-1235)
    # was centered near the Guinea/Mali border but was brief and small.
    (-200000, 500, 'NO_KNOWN_POLITIES'),

    # 500-1235: Various chiefdoms and small kingdoms. Ghana Empire's influence
    # barely reached this far south. All polities under 100M lifetime births.
    (500, 1235, 'NOT_RELEVANT'),

    # GAP: 1235-1460
    # Mali Empire (>100M lifetime births) controlled much of modern Guinea,
    # particularly the Upper Guinea region (Mandinka heartland) and the Niger River
    # headwaters. The Fouta Djallon highlands and the coastal/forest regions
    # (Forest Guinea) were less firmly controlled or independent.
    # Polity with >100M LB: Mali Empire.

    # 1460-1893: Post-Mali fragmentation.
    # Songhai barely reached Guinea (under 100M anyway). Fouta Djallon Imamate
    # (~1727-1896): ~1M * 0.04 * 169 = 6.8M. Wassoulou Empire (~1878-1898):
    # ~3M * 0.04 * 20 = 2.4M. All under 100M lifetime births.
    (1460, 1893, 'NOT_RELEVANT'),

    # French conquest: France defeated Samori Ture and consolidated control by 1893-1898.
    # French Third Republic (>100M LB) controlled 99%+ from ~1893.
    (1893, 1940, 'French Third Republic'),

    # 1940-1958: Vichy, Free France, Fourth Republic. All <100M LB.
    (1940, 1958, 'NOT_RELEVANT'),

    # Guinea voted "No" in the 1958 referendum and became independent immediately
    # on October 2, 1958.
    # Republic of Guinea. Pop ~3M-14M, avg ~7M over 68 yrs.
    # 7M * 0.04 * 68 = 19.0M. Under 100M.
    (1958, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# SENEGAL
# =============================================================================

SENEGAL = [
    # Takrur kingdom from ~800s in the Senegal River valley was likely the first
    # centralized polity with 100k+ in this territory. Ghana Empire influence
    # reached eastern Senegal from ~300 CE but was not centered here.
    (-200000, 300, 'NO_KNOWN_POLITIES'),

    # 300-1235: Ghana Empire influence in eastern Senegal. Takrur kingdom (~800-1285)
    # in the Senegal River valley. All under 100M lifetime births.
    # Ghana Empire: 72M. Takrur: ~0.5M * 0.04 * 485 = 9.7M.
    (300, 1235, 'NOT_RELEVANT'),

    # GAP: 1235-1460
    # Mali Empire (>100M lifetime births) controlled much of Senegal, including
    # the former Takrur region and the upper Senegal River. The coastal Wolof
    # and Serer kingdoms had varying degrees of independence.
    # Polity with >100M LB: Mali Empire.

    # 1460-1895: Post-Mali fragmentation.
    # Jolof Empire (~1350-1549): ~1M * 0.04 * 200 = 8M. Various Wolof states
    # (Cayor, Baol, Waalo), Serer kingdoms, Fouta Toro. All under 100M.
    # French trading posts from 1659 (Saint-Louis) but no interior control.
    (1460, 1895, 'NOT_RELEVANT'),

    # French conquest: France consolidated control of interior by ~1890-1895.
    # Senegal was the oldest French colony in Africa.
    # French Third Republic (>100M LB) controlled 99%+ from ~1895.
    (1895, 1940, 'French Third Republic'),

    # 1940-1960: Vichy, Free France, Fourth Republic. All <100M LB.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Senegal (independent August 20, 1960 after Mali Federation dissolved).
    # Pop ~3M-17M, avg ~8M over 66 yrs. 8M * 0.04 * 66 = 21.1M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# BENIN (formerly Dahomey)
# =============================================================================

BENIN = [
    # The earliest centralized polities here include the kingdom of Allada (~1500s)
    # and the kingdom of Dahomey (from ~1600). The Oyo Empire (centered in modern
    # Nigeria) influenced/controlled parts of southern Benin. Northern Benin had
    # Bariba/Borgu kingdoms.
    (-200000, 1000, 'NO_KNOWN_POLITIES'),

    # 1000-1894: Various kingdoms.
    # Dahomey (~1600-1894): pop ~300k-500k at peak. Well under 100M lifetime births.
    # Oyo Empire (~1400-1835, ~435 yrs, ~3M avg): 52.2M. Under 100M.
    # Borgu/Bariba kingdoms in north. All under 100M.
    # No polity with >100M lifetime births controlled any part of Benin before
    # French conquest. The Mali Empire did not extend to Benin. Songhai barely
    # reached northern Benin and is under 100M anyway.
    (1000, 1894, 'NOT_RELEVANT'),

    # French conquest: France conquered Dahomey in 1892-1894 (Franco-Dahomean Wars).
    # Northern territories conquered by ~1897. French Third Republic (>100M LB).
    (1894, 1940, 'French Third Republic'),

    # 1940-1960: Vichy, Free France, Fourth Republic. All <100M LB.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Dahomey / People's Republic of Benin / Republic of Benin.
    # Pop ~2M-13M, avg ~6M over 66 yrs. 6M * 0.04 * 66 = 15.8M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# TOGO
# =============================================================================

TOGO = [
    # Centralized polities in this small territory emerged relatively late.
    # Dagomba Kingdom and other northern states may have reached 100k+.
    # Ewe peoples migrated into southern Togo from ~1600s. No clearly
    # centralized polity with 100k+ before perhaps the Dagomba influence
    # (15th-16th century).
    (-200000, 1500, 'NO_KNOWN_POLITIES'),

    # 1500-1884: Various small kingdoms and chiefdoms.
    # Dagomba, Ewe states. All well under 100M lifetime births.
    # No polity with >100M controlled any part of Togo.
    (1500, 1884, 'NOT_RELEVANT'),

    # German Togoland (1884-1914): German Empire (>100M lifetime births, 103.4M).
    # Germany controlled 99%+ of modern Togo's territory.
    (1884, 1914, 'German Empire'),

    # GAP: 1914-1920
    # WWI: British and French conquered German Togoland in August 1914.
    # Territory split into British (western strip) and French (eastern, larger portion)
    # zones. Modern Togo corresponds to French Togoland.
    # During 1914-1920 (before League of Nations mandate formalized), France
    # administered modern Togo's territory under military occupation.
    # French Third Republic (>100M LB) controlled 99%+ of modern Togo from 1914,
    # but the period 1914-1920 was transitional military occupation, not formal
    # colonial administration. Britain (>100M LB) had a small western strip that
    # is now part of Ghana, not Togo. So France controlled ~100% of modern Togo.
    # Assign to French Third Republic from 1914.

    # Actually, France occupied essentially all of what is now modern Togo from
    # August 1914. The western strip (British Togoland) became part of Gold Coast
    # (now Ghana). Modern Togo = French Togoland. France controlled 99%+.
    (1914, 1940, 'French Third Republic'),

    # 1940-1960: Vichy, Free France, Fourth Republic. All <100M LB.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Togo (independent April 27, 1960).
    # Pop ~1.5M-9M, avg ~4M over 66 yrs. 4M * 0.04 * 66 = 10.6M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# RWANDA
# =============================================================================

RWANDA = [
    # Kingdom of Rwanda emerged in the 15th century as a centralized state.
    # Before that, small chiefdoms in the Great Lakes region.
    (-200000, 1400, 'NO_KNOWN_POLITIES'),

    # 1400-1898: Kingdom of Rwanda and other small states.
    # Kingdom of Rwanda: ~1.5M avg * 0.04 * 500 = 30M. Under 100M.
    # No polity with >100M lifetime births controlled any part of Rwanda.
    (1400, 1898, 'NOT_RELEVANT'),

    # German East Africa: Germany established indirect rule through the Rwandan
    # king from ~1898 (first resident 1897-98). German Empire (>100M LB).
    (1898, 1916, 'German Empire'),

    # Belgian occupation from 1916 (WWI). League of Nations mandate from 1922.
    # Kingdom of Belgium / Belgian colonial empire: under 100M lifetime births.
    # Belgium avg ~8M * 0.04 * 196 yrs (1830-2026) = 62.7M. Under 100M.
    (1916, 1962, 'NOT_RELEVANT'),

    # Republic of Rwanda (independent July 1, 1962).
    # Pop ~3M-14M, avg ~7M over 64 yrs. 7M * 0.04 * 64 = 17.9M. Under 100M.
    (1962, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# BURUNDI
# =============================================================================

BURUNDI = [
    # Kingdom of Burundi emerged by the late 16th century.
    (-200000, 1550, 'NO_KNOWN_POLITIES'),

    # 1550-1899: Kingdom of Burundi.
    # Pop ~1M avg * 0.04 * 350 = 14M. Under 100M.
    # No polity with >100M lifetime births controlled any part of Burundi.
    (1550, 1899, 'NOT_RELEVANT'),

    # German East Africa: Germany established indirect control from ~1899.
    # German Empire (>100M LB).
    (1899, 1916, 'German Empire'),

    # Belgian occupation from 1916. Mandate/trusteeship until 1962.
    # Kingdom of Belgium: under 100M lifetime births.
    (1916, 1962, 'NOT_RELEVANT'),

    # Kingdom of Burundi briefly independent (July 1, 1962) as monarchy.
    # Became Republic of Burundi in 1966.
    # Pop ~3M-13M, avg ~6M over 64 yrs. 6M * 0.04 * 64 = 15.4M. Under 100M.
    (1962, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# COTE D'IVOIRE (Ivory Coast)
# =============================================================================

COTE_D_IVOIRE = [
    # The earliest centralized polities here include the Kong Empire (~1710-1898).
    # Earlier Mandinka trade settlements existed from Mali Empire era.
    # First centralized polity with 100k+ is uncertain — possibly not until
    # the Kong Empire or Baoulé kingdom in the 18th century.
    (-200000, 1000, 'NO_KNOWN_POLITIES'),

    # 1000-1235: Small chiefdoms and early Senufo/Mandinka settlements.
    # No polity with >100M lifetime births.
    (1000, 1235, 'NOT_RELEVANT'),

    # GAP: 1235-1460
    # Mali Empire (>100M lifetime births) controlled the northern parts of modern
    # Côte d'Ivoire (Mandinka traders established Kong and other settlements).
    # The southern forest regions were independent. Mali Empire controlled the
    # savanna north but not the forested south (>1% of population).
    # Polity with >100M LB: Mali Empire.

    # 1460-1898: Post-Mali period.
    # Kong Empire (~1710-1898): ~500k * 0.04 * 188 = 3.8M. Baoulé, Agni kingdoms.
    # Samori Ture's Wassoulou Empire briefly in north. All under 100M.
    (1460, 1898, 'NOT_RELEVANT'),

    # French conquest: Côte d'Ivoire colony proclaimed 1893, but northern conquest
    # completed ~1898 (fall of Kong to Samori, then French reconquest).
    # French Third Republic (>100M LB) controlled 99%+ from ~1898.
    (1898, 1940, 'French Third Republic'),

    # 1940-1960: Vichy, Free France, Fourth Republic. All <100M LB.
    (1940, 1960, 'NOT_RELEVANT'),

    # Republic of Côte d'Ivoire (independent August 7, 1960).
    # Pop ~3.5M-28M, avg ~12M over 66 yrs. 12M * 0.04 * 66 = 31.7M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# SOMALIA
# =============================================================================

SOMALIA = [
    # Ancient Somali city-states (Mogadishu, Zeila) traded with Arabia and India.
    # Centralized city-states with 100k+ emerged by ~800-1000 CE
    # (Sultanate of Mogadishu, etc.).
    (-200000, 800, 'NO_KNOWN_POLITIES'),

    # 800-1889: Various Somali sultanates and city-states.
    # Sultanate of Mogadishu (~10th-16th c.), Ajuran Sultanate (~13th-17th c.),
    # Adal Sultanate (~1415-1577), Geledi Sultanate (~1750-1910).
    # None had >100M lifetime births. All relatively small polities.
    # Ottoman Empire claimed nominal suzerainty over some coastal areas but had
    # no effective centralized control. Even including Ottoman claims, the Ottomans
    # never controlled 99% of Somali territory.
    # The Adal Sultanate at its peak: ~3M * 0.04 * 162 = 19.4M. Under 100M.
    # Ajuran: ~2M * 0.04 * 400 = 32M. Under 100M.
    # No polity with >100M lifetime births effectively controlled Somali territory.
    (800, 1889, 'NOT_RELEVANT'),

    # GAP: 1889-1941
    # Italy established protectorate over southern Somalia from 1889 (Italian Somaliland).
    # Britain established protectorate over northern Somalia from 1884 (British Somaliland).
    # Kingdom of Italy (>100M LB, 119M) controlled the south.
    # British Empire (>100M LB) controlled the north.
    # Neither controlled 99% of modern Somalia's territory/population.
    # Additionally, the Dervish State (1896-1920) controlled interior regions.

    # 1941-1950: British Military Administration controlled ALL of Somalia
    # (conquered Italian Somaliland in WWII, 1941). British Empire (>100M LB).
    (1941, 1950, 'British Empire'),

    # GAP: 1950-1960
    # UN Trust Territory of Somaliland under Italian administration in south.
    # British Somaliland protectorate in north.
    # Italian Republic (>100M LB, 176M) administered the south.
    # British Empire (>100M LB) controlled the north.
    # Neither controlled 99% of modern Somalia.

    # Somali Republic (united July 1, 1960).
    # Pop ~3M-18M, avg ~8M over 66 yrs. 8M * 0.04 * 66 = 21.1M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# MAURITANIA
# =============================================================================

MAURITANIA = [
    # The Tichitt Tradition (~2200-200 BCE) shows early hierarchical society
    # in southeastern Mauritania, but debatable if 100k+ centralized.
    # The Ghana Empire (~300-1200 CE) was centered in SE Mauritania / W Mali.
    (-200000, 300, 'NO_KNOWN_POLITIES'),

    # 300-1235: Ghana Empire centered partly in Mauritania. Almoravid movement
    # originated in Mauritania (~1040s).
    # Ghana Empire: 72M. Under 100M. Almoravids: 21.4M. Under 100M.
    (300, 1235, 'NOT_RELEVANT'),

    # GAP: 1235-1460
    # Mali Empire (>100M lifetime births) controlled southeastern Mauritania
    # (the Sahel zone, including Oualata/Walata and Tichitt areas — the most
    # populated part of Mauritania). But the vast Saharan regions of northern/
    # western Mauritania were under nomadic Berber/Tuareg/Hassaniya control.
    # Southern Sahel had most of the population but nomadic populations may
    # have exceeded 1% of total.
    # Polity with >100M LB: Mali Empire.

    # 1460-1905: Post-Mali fragmentation.
    # Hassaniya Arab/Berber emirates (Trarza, Brakna, Adrar, Tagant) from 1600s.
    # All small, well under 100M lifetime births individually.
    (1460, 1905, 'NOT_RELEVANT'),

    # French conquest: France established control progressively from 1903-1905.
    # Military pacification continued until 1934 (conquest of Adrar).
    # Most population was in the south, controlled from ~1905.
    # French Third Republic (>100M LB) controlled 99%+ from ~1905.
    (1905, 1940, 'French Third Republic'),

    # 1940-1960: Vichy, Free France, Fourth Republic. All <100M LB.
    (1940, 1960, 'NOT_RELEVANT'),

    # Islamic Republic of Mauritania (independent November 28, 1960).
    # Pop ~1M-5M, avg ~2.5M over 66 yrs. 2.5M * 0.04 * 66 = 6.6M. Under 100M.
    (1960, 2026, 'NOT_RELEVANT'),
]


# =============================================================================
# Collect all assignments
# =============================================================================

ASSIGNMENT = {
    'Mali': MALI,
    'Burkina Faso': BURKINA_FASO,
    'Niger': NIGER,
    'Chad': CHAD,
    'Guinea': GUINEA,
    'Senegal': SENEGAL,
    'Benin': BENIN,
    'Togo': TOGO,
    'Rwanda': RWANDA,
    'Burundi': BURUNDI,
    "Cote d'Ivoire": COTE_D_IVOIRE,
    'Somalia': SOMALIA,
    'Mauritania': MAURITANIA,
}
