"""
Complete polity timelines for Nigeria, Ethiopia, Morocco, Algeria, Tunisia.

Each entry is (start_year, end_year, polity_name) where end_year is exclusive.
Negative years are BCE.

Special polity names:
- NO_KNOWN_POLITIES: Before first centralized polity with ≥100,000 people
- NOT_RELEVANT: All polities in this period had <100M lifetime births
  (lifetime births = avg_population × 0.04 × years_of_existence)
- Gaps between entries mean "indeterminate" — polities existed with >100M lifetime
  births, but no single one controlled ≥99% of the modern country's population.
"""

# =============================================================================
# NIGERIA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~500 CE. The Nok culture (900 BCE - 200 CE) shows
#   advanced material culture but no evidence of centralized political control
#   over 100k people. Kanem emerges ~700 CE as first clearly centralized state
#   in this region, but Yoruba urbanization (Ile-Ife) may push this to ~500 CE.
#
# 500-1861: Gap. Multiple polities existed controlling parts of Nigeria, and
#   Kanem-Bornu (avg ~2-3M people over ~1200 years ≈ 96-144M births) plausibly
#   exceeds 100M lifetime births. Also the Oyo Empire at its peak had several
#   million subjects. But no single polity controlled 99% of modern Nigeria.
#   Gap justification: Kanem-Bornu Empire controlled northeastern Nigeria
#   for over 1000 years with millions of subjects, likely exceeding 100M births.
#
# 1861-1914: Gap. British control expanding (Lagos Colony 1861, Oil Rivers
#   Protectorate 1884, etc.) but not yet unified. The British Empire easily
#   exceeds 100M lifetime births.
#   Gap justification: British Empire controlled parts of Nigeria but hadn't
#   unified the territory. British Empire vastly exceeds 100M lifetime births.
#
# 1914-1960: Colony and Protectorate of Nigeria (unified British colonial rule).
#   Britain controlled >99% of modern Nigeria's territory and population.
#
# 1960-1963: Federation of Nigeria (independent, constitutional monarchy with
#   Queen Elizabeth II as head of state).
#
# 1963-present: Federal Republic of Nigeria.

NIGERIA = [
    (-200000, 500, "NO_KNOWN_POLITIES"),
    # 500-1914: Gap.
    # Justification: Kanem-Bornu Empire (~700-1900 CE) controlled NE Nigeria with
    # avg ~2.5M people over ~1200 years ≈ 120M lifetime births, exceeding threshold.
    # Oyo Empire (~1400-1836) controlled SW Nigeria. Sokoto Caliphate (1804-1903)
    # controlled the north. No single polity controlled 99% of modern Nigeria.
    (1914, 1960, "Colony and Protectorate of Nigeria"),
    (1960, 1963, "Federation of Nigeria"),
    (1963, 2026, "Federal Republic of Nigeria"),
]

# =============================================================================
# ETHIOPIA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~900 BCE with the Kingdom of D'mt, the earliest
#   centralized polity in the Ethiopian highlands with likely >100k people.
#
# -900 to 1890: Gap. Multiple polities controlled parts of modern Ethiopia.
#   The Aksumite Empire (~100-940 CE, avg ~3M people over ~840 years ≈ 101M
#   births) exceeds the threshold. Later the Ethiopian Empire (Solomonic dynasty
#   from 1270) controlled the highlands but not the lowland peripheries (Afar,
#   Somali, Oromo territories in the south/east). Menelik II's conquests
#   (1880s-1890s) incorporated southern Ethiopia.
#   Gap justification: Aksumite Empire controlled northern Ethiopia/Eritrea for
#   ~840 years with ~3M average population, yielding ~101M lifetime births.
#   Ethiopian Empire (Solomonic dynasty) controlled highlands but not southern/
#   eastern lowlands until Menelik II's conquests.
#
# 1890-1936: Ethiopian Empire (under Menelik II and successors). After the
#   conquests of the 1880s-90s and the Battle of Adwa (1896), Ethiopia controlled
#   essentially all of its modern territory. Eritrea was Italian (not part of
#   modern Ethiopia's borders anyway).
#
# 1936-1941: Gap. Italian East Africa occupied Ethiopia. Italy/Italian Empire
#   easily exceeds 100M lifetime births. But Italian control was incomplete —
#   Ethiopian resistance persisted in many areas, so arguably neither Italy nor
#   Ethiopia controlled 99%. I'll leave this as a gap.
#   Gap justification: Italian Empire occupied Ethiopia (Italian East Africa)
#   but faced significant resistance. Italian Empire vastly exceeds 100M births.
#
# 1941-1974: Ethiopian Empire (restored under Haile Selassie). Eritrea was
#   federated with Ethiopia in 1952 and annexed in 1962, but Eritrea is not
#   part of modern Ethiopia, so this doesn't affect the 99% criterion for
#   modern Ethiopia's borders.
#
# 1974-1987: Provisional Military Government of Socialist Ethiopia (Derg).
#
# 1987-1991: People's Democratic Republic of Ethiopia.
#
# 1991-present: Federal Democratic Republic of Ethiopia (transitional government
#   1991-1995, then FDRE constitution).

ETHIOPIA = [
    (-200000, -900, "NO_KNOWN_POLITIES"),
    # -900 to 1890: Gap.
    # Justification: Aksumite Empire (~100-940 CE) with avg ~3M people over ~840
    # years ≈ 101M lifetime births. Ethiopian Empire existed but didn't control
    # southern/eastern regions until Menelik II's conquests in the 1880s-90s.
    (1890, 1936, "Ethiopian Empire"),
    # 1936-1941: Gap.
    # Justification: Italian Empire occupied Ethiopia (Italian East Africa) but
    # faced resistance. Italian Empire vastly exceeds 100M lifetime births.
    (1941, 1974, "Ethiopian Empire"),
    (1974, 1987, "Provisional Military Government of Socialist Ethiopia"),
    (1987, 1991, "People's Democratic Republic of Ethiopia"),
    (1991, 2026, "Federal Democratic Republic of Ethiopia"),
]

# =============================================================================
# MOROCCO
# =============================================================================
# NO_KNOWN_POLITIES: ends ~-400. Carthaginian settlements on the coast existed
#   earlier, but the first centralized governance of inland Morocco with >100k
#   people under centralized control comes with the Kingdom of Mauretania
#   (~3rd century BCE). Phoenician trading posts (from ~800 BCE) were small
#   coastal enclaves, not centralized control of territory.
#
# -400 to -33: NOT_RELEVANT. Kingdom of Mauretania existed but was relatively
#   small. Population maybe 1-2M, lasted ~370 years. 1.5M × 0.04 × 370 = 22M
#   births — well under threshold. No other polity controlling Moroccan
#   territory exceeded the threshold either.
#
# -33 to 429: Gap. Roman Empire controlled Mauretania Tingitana (northern
#   Morocco) from 40 CE, but Roman influence began with client kingdom from
#   33 BCE. The Roman Empire easily exceeds 100M lifetime births. But Rome
#   only controlled the northern portion of modern Morocco — the interior and
#   south were controlled by independent Berber tribes. So no single polity
#   controlled 99%.
#   Gap justification: Roman Empire controlled northern Morocco (Mauretania
#   Tingitana) and vastly exceeds 100M lifetime births, but didn't control
#   the interior/south.
#
# 429-788: NOT_RELEVANT. Vandal Kingdom (429-534) controlled parts of NW Africa
#   but Morocco was peripheral. Vandals: ~2M people × 0.04 × 105 years = 8.4M.
#   Byzantine Empire reconquered parts but had minimal presence in Morocco proper
#   (mostly Ceuta). Wait — the Byzantine Empire itself vastly exceeds 100M births
#   and controlled Ceuta/Tangier area. So this can't be NOT_RELEVANT if Byzantium
#   controlled even part of Morocco. Let me reconsider.
#   Actually, Byzantine control of Morocco was limited to Ceuta and perhaps
#   Tangier — tiny coastal outposts, well under 1% of Morocco's population.
#   The vast majority of Morocco was under independent Berber control.
#   The Umayyad conquest reached Morocco by 680s. Umayyad Caliphate: ~30M people
#   × 0.04 × ~90 years (661-750) = 108M. So from the 680s, the Umayyads
#   controlled Morocco and exceed the threshold. Let me split this.
#
# 429-682: NOT_RELEVANT. After Rome, Morocco was under various Berber polities.
#   Vandals controlled the coast briefly. Byzantine control was limited to Ceuta.
#   No polity controlling significant Moroccan territory exceeded 100M births.
#   The Vandal Kingdom (~8.4M births) and independent Berber polities were all
#   well under threshold.
#
# 682-788: Gap. Umayyad Caliphate conquered Morocco (~682-710 CE). Umayyads
#   (~30M avg pop × 0.04 × 89 years = 107M births) exceed threshold. But
#   Berber revolts (740s) fragmented control. Abbasid takeover (750) didn't
#   effectively control Morocco.
#   Gap justification: Umayyad Caliphate conquered Morocco and exceeds 100M
#   lifetime births, but control was contested (Great Berber Revolt 740-743).
#
# 788-974: Idrisid dynasty. Founded by Idris I, controlled most of Morocco.
#   But did they control 99%? The Idrisids fragmented into sub-kingdoms by the
#   mid-800s. Their peak control of all Morocco was relatively brief.
#   Population: ~2-3M, lasted ~186 years. 2.5M × 0.04 × 186 = 18.6M births.
#   Under threshold. But were there other polities in Morocco exceeding 100M?
#   The Umayyad Caliphate of Córdoba intervened in northern Morocco. Córdoba
#   had ~10M people over ~275 years (756-1031) = 110M births. They controlled
#   parts of northern Morocco. So this is a gap, not NOT_RELEVANT.
#   Wait, Córdoba: ~5-10M average over 275 years. Let's say 7M × 0.04 × 275 = 77M.
#   Hmm, borderline. Actually at its peak Al-Andalus had ~7-10M. Average over
#   the whole period maybe 6M. 6M × 0.04 × 275 = 66M. Under threshold.
#   The Fatimid Caliphate controlled Morocco briefly before moving to Egypt.
#   Fatimids: originated in modern Tunisia/Algeria, conquered Morocco ~920s.
#   Then moved to Egypt 969. Fatimid period in NW Africa: ~909-973.
#   Total Fatimid empire: ~15-20M at peak × 0.04 × ~270 years = 162-216M.
#   They exceed the threshold. And they controlled parts of Morocco.
#   So from ~920 onwards, the Fatimids (who exceed threshold) controlled parts
#   of Morocco, making it a gap rather than NOT_RELEVANT.
#
# Let me reconsider the 788-1060 period more carefully:
# 788-~920: Idrisids controlled most of Morocco. Fatimids hadn't reached Morocco
#   yet. Umayyads of Córdoba: borderline on threshold. Let me check — if I'm
#   supposed to err on the side of gaps, I should leave this as a gap given
#   uncertainty about Córdoba. Actually the instructions say to err on the side
#   of leaving a gap. So I'll make 788-1070 a gap.
#
# 1040-1147: Almoravid Empire. Controlled Morocco AND much of Iberia and West
#   Africa. ~15M people × 0.04 × 107 = 64M births. Under threshold. But they
#   controlled 99% of Morocco. Since under threshold → NOT_RELEVANT? No, wait.
#   NOT_RELEVANT means ALL polities had <100M births. The Almoravids themselves
#   had <100M. Were there other polities in Morocco? No, Almoravids controlled
#   all of it. So this would be a named entry (they controlled 99%) but we list
#   them by name. Wait, the question is just about listing entries. If a single
#   polity controlled 99%, I name them, regardless of their birth count.
#   The threshold only matters for NOT_RELEVANT.
#
# OK let me simplify my approach for Morocco:
#
# 1070-1147: Almoravid Empire controlled essentially all of Morocco.
# 1147-1269: Almohad Caliphate controlled essentially all of Morocco.
# 1269-1465: Marinid dynasty controlled most of Morocco.
# 1472-1554: Wattasid dynasty — but controlled only Fez region, not all Morocco.
# 1549-1659: Saadian dynasty controlled most of Morocco.
# 1631/1666-1912: Alaouite dynasty.
#
# Many of these transitions involved overlap and fragmentation. Let me be more
# careful about 99% control.
#
# 1912-1956: French Protectorate of Morocco + Spanish protectorate in the north
#   and south. France didn't control 99% — Spain controlled the Rif and
#   southern strip (~10% of territory, ~5-10% of population). So this is a gap.
#   Gap justification: French colonial empire (vastly exceeds 100M births)
#   controlled most of Morocco, but Spanish protectorate controlled the north
#   (Rif) and Ifni/southern strip.
#
# 1956-present: Kingdom of Morocco.

MOROCCO = [
    (-200000, -400, "NO_KNOWN_POLITIES"),
    (-400, -33, "NOT_RELEVANT"),
    # -33 to 429: Gap.
    # Justification: Roman Empire controlled Mauretania Tingitana (northern
    # Morocco) and vastly exceeds 100M lifetime births, but did not control
    # the interior and southern regions of modern Morocco.
    (429, 682, "NOT_RELEVANT"),
    # 682-1070: Gap.
    # Justification: Umayyad Caliphate (~682-750) conquered Morocco and exceeds
    # 100M lifetime births. Fatimid Caliphate (~920s-973) also exceeds threshold
    # and controlled parts of Morocco. No single polity controlled 99%.
    (1070, 1147, "Almoravid Empire"),
    (1147, 1269, "Almohad Caliphate"),
    # 1269-1631: Gap.
    # Justification: Marinid dynasty controlled most of Morocco (1269-1465) but
    # after their decline, Wattasids controlled only the Fez region while
    # Portuguese held coastal cities (Ceuta, Tangier, etc.) and Saadians
    # controlled the south. The Ottoman Empire (which exceeds 100M births)
    # was active in the region. Portuguese Empire also borderline.
    # Erring on side of gap due to Ottoman and Portuguese involvement.
    (1631, 1912, "Alaouite dynasty"),
    # 1912-1956: Gap.
    # Justification: French colonial empire controlled most of Morocco as a
    # protectorate (vastly exceeds 100M births), but Spain controlled the
    # northern Rif region and southern strip as a separate protectorate
    # (~5-10% of population).
    (1956, 2026, "Kingdom of Morocco"),
]

# =============================================================================
# ALGERIA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~-200. Numidia emerges as a centralized polity
#   in the 3rd century BCE. Massinissa unified eastern and western Numidia
#   in 202 BCE after the Second Punic War. Carthaginian coastal settlements
#   existed earlier but didn't constitute centralized control of Algerian
#   interior with >100k people.
#
# -200 to -46: NOT_RELEVANT? Kingdom of Numidia: ~2-3M people over ~156 years.
#   2.5M × 0.04 × 156 = 15.6M births. Under threshold. Carthage controlled
#   the coast before that but was destroyed in 146 BCE. Carthaginian Empire:
#   maybe ~4M people × 0.04 × 400 years = 64M. Under threshold.
#   Wait — did the Roman Republic already control parts of Algeria after
#   destroying Carthage in 146 BCE? Rome made Africa a province in 146 BCE
#   (roughly modern Tunisia), but Numidia remained independent until 46 BCE.
#   Roman Republic/Empire at this point: ~50-60M people, existence from ~500 BCE
#   as a major state... easily exceeds 100M births. Rome controlled the former
#   Carthaginian coast (eastern Algeria/Tunisia border area) from 146 BCE.
#   So from -146, Rome (exceeding threshold) controlled part of Algeria.
#   Before -146: only Numidia and Carthage, both under threshold.
#
# -200 to -146: NOT_RELEVANT. Numidia and Carthage both under 100M births.
#
# -146 to 429: Gap (mostly). Rome controlled parts from 146 BCE, all of Algeria
#   as provinces from 46 BCE (after Numidia annexed). But even after 46 BCE,
#   Rome controlled the coastal/agricultural Tell region but not the deep
#   Saharan south. However, virtually all the population was in the north.
#   From 46 BCE, Rome controlled territory containing >99% of Algeria's
#   population. So:
#
# -146 to -46: Gap. Rome controlled eastern coastal Algeria (former Carthaginian
#   territory), Numidia controlled the rest. Rome exceeds 100M births.
#   Gap justification: Roman Republic controlled eastern coastal Algeria after
#   destroying Carthage, while Kingdom of Numidia controlled the interior.
#   Roman Republic/Empire vastly exceeds 100M lifetime births.
#
# -46 to 429: Roman Empire. After Caesar annexed Numidia (46 BCE), Rome
#   controlled essentially all populated areas of modern Algeria.
#   (Africa Nova, Mauretania Caesariensis, etc.)
#
# 429-534: Vandal Kingdom conquered Roman North Africa. But did Vandals control
#   99% of Algeria? They controlled the coast and major cities. Interior Berber
#   tribes were semi-independent. Vandals: ~2-3M people × 0.04 × 105 = 8-12.6M
#   births. Under threshold. Were there any other polities >100M? Not really —
#   the rump Western Roman Empire was collapsing, Eastern Roman Empire hadn't
#   reconquered yet. So this is NOT_RELEVANT.
#   Wait — the Eastern Roman/Byzantine Empire existed during this entire period
#   and vastly exceeds 100M births. Did it control ANY part of Algeria? Not
#   directly during Vandal rule (429-534). Byzantium didn't control Algerian
#   territory until reconquest in 534. So for 429-534, the only polity
#   controlling Algerian territory was the Vandal Kingdom (<100M births) and
#   independent Berber groups. I think NOT_RELEVANT is correct.
#   Actually wait — I should be more careful. The instructions say "ANY polity
#   controlling ANY PART of this modern country's territory." The Vandal Kingdom
#   itself had <100M births, and independent Berber polities had <100M births.
#   No polity exceeding 100M controlled any part of Algeria during 429-534.
#   So NOT_RELEVANT.
#
# 534-682: Byzantine reconquest. Byzantine Empire controlled coastal Algeria
#   (Praetorian prefecture of Africa). Byzantines vastly exceed 100M births.
#   But interior was under Berber control. Byzantines probably controlled
#   >99% of the population (which was concentrated on the coast). Hmm, actually
#   the Berber kingdoms of the interior (like the Aurès region under the
#   Dihya/Kahina) were significant. Let me call this a gap to be safe.
#   Gap justification: Byzantine Empire controlled coastal Algeria and vastly
#   exceeds 100M births, but interior Berber kingdoms controlled significant
#   populated areas.
#
# Actually, the Berber kingdoms in the interior during Byzantine rule — were they
# >1% of population? The Aurès mountains and other interior regions had
# significant Berber populations, possibly >1%. I'll leave it as a gap.
#
# 682-1518: Gap. Umayyad conquest (~680s-710s), then various Islamic dynasties.
#   Algeria was divided between multiple polities: Rustamids (761-909) in
#   central Algeria, Aghlabids in the east, Fatimids (909-973), Zirids
#   (973-1148), Hammadids (1014-1152) in central Algeria, Almohads (1147-1269),
#   Zayyanids (1235-1556) in western Algeria, Hafsids (1229-1574) in eastern
#   Algeria. No single polity controlled 99% of Algeria.
#   Gap justification: Umayyad Caliphate (exceeds 100M births) conquered
#   Algeria. Later Abbasid Caliphate, Fatimid Caliphate, and Almohad Caliphate
#   all exceed 100M births and controlled parts of Algeria.
#
# 1518-1830: Regency of Algiers (Ottoman Algeria). The Ottoman Empire controlled
#   essentially all of populated Algeria through the Regency. The Saharan south
#   was nominal, but >99% of population was under Ottoman control.
#   Ottoman Empire vastly exceeds 100M births. The Regency of Algiers was
#   semi-autonomous but part of the Ottoman Empire.
#
# 1830-1848: Gap/French conquest. France was conquering Algeria gradually.
#   Not yet full control. Abd el-Kader's state controlled western interior.
#   French Empire exceeds 100M births.
#   Gap justification: French colonial empire (exceeds 100M births) was
#   conquering Algeria but hadn't achieved full control. Abd el-Kader controlled
#   western regions until 1847.
#
# 1848-1962: French Algeria. From 1848, Algeria was officially part of France
#   (départements). France controlled >99% of the territory and population.
#   I'll use "French Algeria" as the polity name since it was constitutionally
#   part of France, not a separate colony.
#
# 1962-present: People's Democratic Republic of Algeria.

ALGERIA = [
    (-200000, -200, "NO_KNOWN_POLITIES"),
    (-200, -146, "NOT_RELEVANT"),
    # -146 to -46: Gap.
    # Justification: Roman Republic controlled eastern coastal Algeria (former
    # Carthaginian territory) and vastly exceeds 100M births. Kingdom of
    # Numidia controlled the rest.
    (-46, 429, "Roman Empire"),
    (429, 534, "NOT_RELEVANT"),
    # 534-682: Gap.
    # Justification: Byzantine Empire controlled coastal Algeria and vastly
    # exceeds 100M births, but interior Berber kingdoms controlled significant areas.
    # 682-1518: Gap.
    # Justification: Umayyad Caliphate, Abbasid Caliphate, Fatimid Caliphate,
    # and Almohad Caliphate all exceed 100M lifetime births and controlled
    # parts of Algeria at various times. No single polity controlled 99%.
    (1518, 1830, "Regency of Algiers"),
    # 1830-1848: Gap.
    # Justification: French colonial empire (vastly exceeds 100M births) was
    # conquering Algeria but hadn't achieved full control. Abd el-Kader's
    # resistance state controlled western interior regions.
    (1848, 1962, "French Algeria"),
    (1962, 2026, "People's Democratic Republic of Algeria"),
]

# =============================================================================
# TUNISIA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~-814. Phoenician settlement of Carthage traditionally
#   dated to 814 BCE. But Carthage didn't become a major centralized polity
#   with >100k people until later (~6th century BCE). Earlier Phoenician
#   settlements (Utica ~1100 BCE) were small trading posts. I'll use -550
#   as the start of centralized polity control in Tunisia (Carthage becoming
#   a major city-state with clear hegemony over surrounding territory).
#   Actually, by 650-600 BCE Carthage was already a significant city. Let me
#   use -650.
#
# -650 to -146: Carthaginian period. Carthage was located IN modern Tunisia
#   and controlled essentially all of it. But did Carthage control 99% of
#   Tunisia's population? At its height, yes — Carthaginian hegemony over
#   the entire region. Population of Carthage alone ~500k, total controlled
#   area in Tunisia ~1-2M.
#   Carthaginian Empire total: ~4-5M people × 0.04 × ~500 years = 80-100M.
#   Borderline. But the question is whether Carthage controlled 99% of modern
#   Tunisia, which it did. I'll list it as a named polity.
#   Actually, for the naming — "Carthaginian Empire" or just "Carthage"?
#   I'll use "Carthage" for the city-state/empire.
#
# -146 to 439: Roman province. Africa Proconsularis. Rome controlled essentially
#   all of Tunisia. Tunisia was the heartland of Roman Africa.
#
# 439-534: Vandal Kingdom. Centered on Carthage/Tunisia. Vandals controlled
#   Tunisia. ~2-3M × 0.04 × 95 = 7.6-11.4M births. Under threshold.
#   Other polities controlling Tunisian territory? None with >100M births
#   during this exact period. Western Rome had fallen, Eastern Rome (Byzantium)
#   didn't control Tunisia yet. NOT_RELEVANT.
#   Wait — did the Byzantine Empire control any part of Tunisia during Vandal
#   rule? No, the Vandals controlled it all. NOT_RELEVANT is correct.
#
# 534-698: Byzantine rule. Reconquest by Belisarius in 534. Byzantine Empire
#   vastly exceeds 100M births. Controlled essentially all of Tunisia.
#   Arab raids begin in the 640s, but Tunisia remains Byzantine until the
#   fall of Carthage in 698.
#
# 698-800: Gap. Umayyad then Abbasid conquest. Umayyads exceed 100M births.
#   Tunisia was part of Ifriqiya province. Abbasid Caliphate: ~30-40M people
#   × 0.04 × ~200 years (750-~950) = 240-320M. Easily exceeds. From 698-800,
#   Tunisia was under Umayyad then Abbasid control. They controlled 99%.
#   Actually, from 698-750 it was Umayyad. The Umayyad Caliphate controlled
#   essentially all of Tunisia. From 750-800, Abbasid Caliphate controlled it.
#   But both of these are single-polity control. Let me list them.
#
# 698-750: Umayyad Caliphate. Controlled Tunisia as part of Ifriqiya.
# 750-800: Abbasid Caliphate. Controlled Tunisia.
# 800-909: Aghlabid dynasty (autonomous under Abbasids). Controlled Tunisia.
#   Aghlabids: ~2-3M × 0.04 × 109 = 8.7-13.1M. Under threshold. But the
#   Abbasid Caliphate still nominally controlled it. Were the Aghlabids
#   independent enough to be a separate polity? They were de facto autonomous.
#   If I consider them a separate polity, they're under threshold. But the
#   Abbasid Caliphate (which exceeds threshold) still claimed sovereignty.
#   I'll treat the Aghlabids as the effective polity. They controlled 99% of
#   Tunisia. Since they're under threshold and no other polity with >100M
#   births controlled Tunisian territory independently of them... hmm, but
#   the Abbasids technically still claimed sovereignty. The Abbasids exceed
#   100M births and arguably "controlled" Tunisia through the Aghlabids.
#   I'll leave the Aghlabid period as the Abbasid Caliphate since the Aghlabids
#   were technically governors.
#   Actually no — the Aghlabids were de facto independent. This is like asking
#   whether the Mamluks were part of the Abbasid Caliphate. I'll treat them as
#   separate. Since they're under threshold AND they controlled 99%, I should
#   check: is there any OTHER polity controlling Tunisian territory with >100M
#   births? The Abbasids didn't independently control Tunisian territory.
#   So NOT_RELEVANT? No — I should name the Aghlabids since they controlled 99%.
#   Hmm, but the instructions say to use a polity name when a single polity
#   controlled 99%. So I name them regardless of whether they exceed the
#   threshold. The threshold only matters for NOT_RELEVANT.
#
# 909-973: Fatimid Caliphate originated in Tunisia (Ifriqiya). Controlled all
#   of Tunisia. Later moved capital to Cairo (969) but kept control until
#   appointing Zirids as governors.
#
# 973-1148: Zirid dynasty. Controlled Tunisia as Fatimid vassals, then
#   independently after the Fatimid withdrawal. The Banu Hilal invasion (1057)
#   devastated the countryside. Zirids retained coastal cities but lost control
#   of interior. This is complex. The Fatimid Caliphate still existed and
#   arguably exceeded 100M births (~15-20M × 0.04 × 270 = 162-216M).
#   After the Hilal invasion, Zirid control fragmented. Norman Sicily took
#   some coastal cities. This becomes messy. Let me call 973-1159 a gap.
#   Gap justification: Fatimid Caliphate (exceeds 100M births) existed and
#   claimed sovereignty. Zirids controlled parts, Hilalian tribes controlled
#   interior, Normans took coastal cities. Fragmented control.
#
# 1159-1229: Almohad Caliphate controlled Tunisia (conquered from Normans/
#   fragmented local rulers). Almohads: ~15-20M × 0.04 × ~120 years = 72-96M.
#   Borderline. But the question is control: Almohads controlled 99% of Tunisia.
#   I'll name them.
#
# 1229-1574: Hafsid dynasty. Based in Tunis, controlled Tunisia. One of the
#   longest-lasting North African dynasties. ~1-3M × 0.04 × 345 = 14-41M.
#   Under threshold. But they controlled 99% of Tunisia, so I name them.
#   However, there were periods of fragmentation and foreign intervention
#   (Marinid occupation of Tunis 1347-1350, Spanish/Ottoman conflicts in
#   the 1500s). By the early 1500s, Spanish and Ottoman forces were fighting
#   over Tunisia. Hafsids lost effective control. Let me end Hafsid control
#   at 1534 when Hayreddin Barbarossa captured Tunis.
#   1534-1574: Contested between Spain and Ottoman Empire. Both exceed 100M
#   births. No single polity controlled 99%. Gap.
#
# 1574-1881: Ottoman Tunisia. Ottomans controlled Tunisia through beys/deys.
#   Husainid dynasty from 1705 was autonomous but under Ottoman sovereignty.
#   Ottoman Empire vastly exceeds threshold. Controlled 99% of Tunisia.
#
# 1881-1956: French Protectorate of Tunisia. France controlled essentially all
#   of Tunisia. French Empire vastly exceeds threshold.
#
# 1956-1957: Kingdom of Tunisia (brief monarchy after independence).
# 1957-2011: Tunisian Republic (under Bourguiba then Ben Ali).
# 2011-present: Republic of Tunisia (post-revolution, new constitution 2014).
#   Actually, the official name didn't change. It's been "Republic of Tunisia"
#   since 1957. Let me just use that.

TUNISIA = [
    (-200000, -650, "NO_KNOWN_POLITIES"),
    (-650, -146, "Carthage"),
    (-146, 439, "Roman Empire"),
    (439, 534, "NOT_RELEVANT"),
    (534, 698, "Byzantine Empire"),
    (698, 750, "Umayyad Caliphate"),
    (750, 800, "Abbasid Caliphate"),
    (800, 909, "Aghlabid Emirate"),
    (909, 973, "Fatimid Caliphate"),
    # 973-1159: Gap.
    # Justification: Fatimid Caliphate (exceeds 100M births with ~15-20M avg
    # population over ~270 years) still existed and claimed sovereignty over
    # Ifriqiya. Zirids governed as vassals then independently, but Banu Hilal
    # invasion fragmented the interior. Norman Sicily captured coastal cities.
    (1159, 1229, "Almohad Caliphate"),
    (1229, 1534, "Hafsid Caliphate"),
    # 1534-1574: Gap.
    # Justification: Spanish Empire (vastly exceeds 100M births) and Ottoman
    # Empire (vastly exceeds 100M births) both fought over Tunisia. Spain held
    # Tunis 1535-1569 as a protectorate, Ottomans captured it in 1534 and
    # definitively in 1574. No single polity controlled 99%.
    (1574, 1881, "Ottoman Empire"),
    (1881, 1956, "French Protectorate of Tunisia"),
    (1956, 1957, "Kingdom of Tunisia"),
    (1957, 2026, "Republic of Tunisia"),
]


# =============================================================================
# Summary / Validation
# =============================================================================
def validate_timeline(name, timeline):
    """Check that entries don't overlap and are in chronological order."""
    errors = []
    for i, (start, end, polity) in enumerate(timeline):
        if start >= end:
            errors.append(f"  Entry {i}: start ({start}) >= end ({end}): {polity}")
        if i > 0:
            prev_end = timeline[i-1][1]
            if start < prev_end:
                errors.append(
                    f"  Entry {i}: start ({start}) < previous end ({prev_end}): "
                    f"{polity} overlaps with {timeline[i-1][2]}"
                )
    if errors:
        print(f"{name}: ERRORS")
        for e in errors:
            print(e)
    else:
        # Check for gaps
        gaps = []
        for i in range(1, len(timeline)):
            prev_end = timeline[i-1][1]
            curr_start = timeline[i][0]
            if curr_start > prev_end:
                gaps.append(f"  Gap: {prev_end} to {curr_start}")
        print(f"{name}: OK ({len(timeline)} entries, {len(gaps)} gaps)")
        for g in gaps:
            print(g)


if __name__ == "__main__":
    for name, timeline in [
        ("Nigeria", NIGERIA),
        ("Ethiopia", ETHIOPIA),
        ("Morocco", MOROCCO),
        ("Algeria", ALGERIA),
        ("Tunisia", TUNISIA),
    ]:
        validate_timeline(name, timeline)
        print()
