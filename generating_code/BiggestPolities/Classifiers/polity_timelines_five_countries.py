"""
Complete polity timelines for Italy, Spain, Portugal, Greece, and Switzerland.

Rules:
- NO_KNOWN_POLITIES: earliest period until first polity with >=100K people under centralized control.
- NOT_RELEVANT: polities existed but ALL had <100M lifetime births (avg_pop * 0.04 * years).
- Named polity: single polity controlled >=99% of modern country's population.
- Gaps: polities with >100M lifetime births existed but none controlled 99%+ of pop.
  Each gap has explicit justification naming a >100M-birth polity.
- End years are exclusive. Negative years are BCE.

For colonial empires, lifetime births include ALL territories under the empire's control.
"""

# =============================================================================
# ITALY
# =============================================================================
#
# Key lifetime-births calculations for polities touching Italian territory:
#   Roman Republic (509-27 BC): avg ~15M × 0.04 × 482 = 289M. >100M.
#   Roman Empire (27 BC-476 AD): avg ~50M × 0.04 × 503 = 1,006M. >100M.
#   Ostrogothic Kingdom (493-553): avg ~5M × 0.04 × 60 = 12M. <100M.
#   Byzantine Empire (395-1453): avg ~10M × 0.04 × 1058 = 423M. >100M.
#   Lombard Kingdom (568-774): avg ~3M × 0.04 × 206 = 25M. <100M.
#   Carolingian Empire (751-888): avg ~10M × 0.04 × 137 = 55M. <100M.
#     BUT the broader Frankish Kingdom (481-843) was ~10M × 0.04 × 362 = 145M. >100M.
#     However Carolingian Empire proper (from 800) was only 44 years to 843. Marginal.
#   Holy Roman Empire (962-1806): avg ~10M × 0.04 × 844 = 338M. >100M.
#     Northern Italy was nominally part of HRE as "Kingdom of Italy" but effective
#     control was lost by ~1200. Still, HRE >100M births overall.
#   Kingdom of Naples / Sicily: ~3M × 0.04 × 600 = 72M. <100M.
#   Papal States (756-1870): ~2M × 0.04 × 1114 = 89M. <100M.
#   Republic of Venice (697-1797): ~2M × 0.04 × 1100 = 88M. <100M.
#   Kingdom of France: ~12M × 0.04 × 805 = 386M. >100M. Controlled parts of Italy.
#   Habsburg Spain/Austria: >100M. Controlled parts of Italy.
#   Kingdom of Italy (1861-1946): Italy itself avg ~30M × 0.04 × 85 = 102M. Just >100M.
#
# Timeline:
#   -200000 to -900: NO_KNOWN_POLITIES
#     First major centralized polity in Italian territory: Etruscan city-states and
#     Greek colonies emerged ~8th century BC but these were city-states, not centralized
#     polities of 100K+. Rome reached 100K+ population under centralized control by
#     roughly the 5th-4th century BC. Using -900 as conservative start.
#
#   -900 to -264: GAP — Roman Republic existed and eventually exceeds 100M lifetime
#     births overall, but it did not control 99% of Italian peninsula population.
#     Greek colonies in the south (Magna Graecia), Etruscan cities in central Italy,
#     Celtic/Gallic peoples in the Po Valley, Samnites, etc. Rome only unified the
#     peninsula by ~264 BC after the Samnite Wars and conquest of Magna Graecia.
#     Justification: Roman Republic (>100M lifetime births total) controlled part of Italy.
#
#   -264 to -27: Roman Republic — after the First Punic War, Rome controlled essentially
#     all of the Italian peninsula. Cisalpine Gaul (Po Valley) was incorporated as a
#     province by ~191 BC but culturally integrated. By 264 BC, 99%+ of peninsula pop
#     was under Roman control.
#
#   -27 to 476: Roman Empire — continuation of Roman control, now under imperial system.
#     The Western Roman Empire formally ended in 476.
#
#   476 to 493: GAP — Odoacer's Kingdom controlled Italy but was very short-lived.
#     Odoacer's kingdom: ~5M × 0.04 × 17 = 3.4M births. <100M.
#     However, the Eastern Roman/Byzantine Empire (>100M lifetime births) still claimed
#     sovereignty over Italy during this period and controlled parts (Sicily, south).
#     Justification: Byzantine Empire (>100M lifetime births) controlled southern Italy.
#
#   493 to 553: GAP — Ostrogothic Kingdom controlled most of Italy but the Byzantine
#     Empire still held parts of southern Italy and Sicily at various points. The
#     Ostrogothic Kingdom itself had <100M lifetime births (12M), but the Byzantine
#     Empire (>100M) also controlled territory. Not a clean 99% assignment because
#     Byzantine reconquest began in 535 and was ongoing.
#     Actually, from 493-535, Ostrogoths controlled essentially all of Italy.
#     But Ostrogothic Kingdom total births = 12M < 100M.
#     Byzantine Empire controlled parts from 535 onward.
#     For 493-535: Only the Ostrogothic Kingdom controlled Italy, and it had <100M births.
#     No other >100M polity controlled any part. So this should be NOT_RELEVANT.
#     For 535-553: Gothic War. Byzantine Empire (>100M) actively reconquering = gap.
#
#   553 to 568: Byzantine Empire controlled all of Italy after Gothic War ended.
#
#   568 to 1861: GAP — Extremely fragmented. Lombards controlled north/center,
#     Byzantines held south, Papal States in center, then Carolingians, then city-states,
#     then various foreign powers (Normans, Angevins, Aragonese, Spanish, Austrian, French).
#     At virtually every point, multiple significant polities controlled different regions.
#     Justification: Byzantine Empire (>100M), Holy Roman Empire (>100M), Kingdom of France
#     (>100M), Habsburg Spain (>100M), and others all controlled portions of Italian
#     territory throughout this long period.
#
#   1861 to 1943: Kingdom of Italy — unified Italy (Venice added 1866, Rome 1870).
#     Using 1861 is slightly generous since Venice (Veneto ~8% of pop) wasn't added
#     until 1866 and Rome/Lazio (~5%) until 1870. But the task says 99%, and
#     Piedmont-Sardinia effectively controlled the rest. Actually, missing Venetia
#     (8%) and Rome (5%) means only ~87% in 1861. Must wait until 1870.
#     1870: Kingdom of Italy controlled all of modern Italy's territory.
#     1943: Kingdom collapsed; German occupation of north, Allied south.
#
#   1943 to 1946: GAP — Italy split between German-occupied Italian Social Republic
#     (north) and Kingdom of Italy/Allied-occupied south. Nazi Germany (>100M lifetime
#     births) controlled northern Italy.
#     Justification: Nazi Germany (>100M lifetime births) controlled northern Italy.
#
#   1946 to 2026: Italian Republic.

ITALY = [
    (-200000, -900, 'NO_KNOWN_POLITIES'),
    # GAP -900 to -264: Roman Republic (>100M births) controlled central Italy but
    # not 99% — Magna Graecia, Etruscans, Samnites, Gauls held other regions.
    (-264, -27, 'Roman Republic'),
    (-27, 476, 'Roman Empire'),
    # GAP 476-493: Byzantine Empire (>100M births) claimed/held parts of Italy.
    (493, 535, 'NOT_RELEVANT'),  # Ostrogothic Kingdom: 5M × 0.04 × 42 = 8.4M < 100M. No >100M polity held Italian territory.
    # GAP 535-553: Gothic War; Byzantine Empire (>100M births) reconquering Italy.
    (553, 568, 'Byzantine Empire'),
    # GAP 568-1870: Fragmented — Lombards, Byzantines, Papal States, HRE, city-states,
    # foreign crowns. Byzantine Empire (>100M), Holy Roman Empire (>100M),
    # Kingdom of France (>100M), Habsburg Spain (>100M) all controlled parts.
    (1870, 1943, 'Kingdom of Italy'),
    # GAP 1943-1946: Split between Nazi Germany (>100M) in the north and
    # Kingdom of Italy in the south.
    (1946, 2026, 'Italian Republic'),
]


# =============================================================================
# SPAIN
# =============================================================================
#
# Key lifetime-births calculations:
#   Roman Republic/Empire: >100M (see Italy).
#   Visigothic Kingdom (418-711): avg ~3M × 0.04 × 293 = 35M. <100M.
#   Umayyad Caliphate (661-750): avg ~30M × 0.04 × 89 = 107M. >100M.
#     Controlled most of Iberia 711-750.
#   Abbasid Caliphate (750-756): briefly claimed Iberia. >100M overall but only 6 years.
#   Umayyad Emirate/Caliphate of Cordoba (756-1031): avg ~5M × 0.04 × 275 = 55M. <100M.
#   Almoravid Empire (1040-1147): avg ~5M × 0.04 × 107 = 21M. <100M.
#   Almohad Caliphate (1121-1269): avg ~5M × 0.04 × 148 = 30M. <100M.
#   Crown of Castile (1230-1516): avg ~5M × 0.04 × 286 = 57M. <100M.
#   Crown of Aragon (1137-1516): avg ~3M × 0.04 × 379 = 45M. <100M.
#   Habsburg Spain (1516-1700): Empire total avg ~20M × 0.04 × 184 = 147M. >100M.
#   Bourbon Spain: Spain proper avg ~10M × 0.04 × ~100 = 40M per century.
#     But with empire: avg ~15M × 0.04 × 94 (1714-1808) = 56M. <100M for any
#     single continuous Bourbon period. Total Bourbon period (1714-1808, 1814-1868,
#     1874-1931) is not continuous. But "Bourbon Spain" as a polity from 1700-1808
#     with colonies: avg ~20M × 0.04 × 108 = 86M. Close but <100M.
#     Actually the Spanish Empire maintained extensive colonies. Let me reconsider.
#     Spanish colonial empire 1700: Spain (~8M) + New Spain (~6M) + Peru (~3M) +
#     Philippines (~1.5M) + others = ~20M total. 20M × 0.04 × 108 = 86M.
#     Still <100M for the 1714-1808 Bourbon period.
#     Wait, I should count Bourbon Spain as one continuous polity 1700-1808 (~108y):
#     ~20M × 0.04 × 108 = 86M. <100M.
#     Hmm but combined with restoration: 1700-1931 minus gaps = ~200 years.
#     As a single "Bourbon Spain" polity: 20M × 0.04 × 200 = 160M. >100M.
#     The regime changed but the polity is continuous. Using splitting view,
#     each individual period is <100M but the underlying state is continuous.
#     For the task's purposes, I'll use the splitting view as requested.
#     However, the task says to calculate births for the polity, not the regime.
#     "Bourbon Spain" 1714-1868 is arguably one polity = 20M × 0.04 × 154 = 123M. >100M.
#
# Timeline:
#   -200000 to -1100: NO_KNOWN_POLITIES
#     Phoenician/Greek colonies appeared ~1100 BC but were small trading posts.
#     Tartessos may have been centralized ~900-500 BC. Using -1100 conservatively
#     for Phoenician Gadir (~1100 BC) which was a significant settlement.
#     Actually, Tartessos and Phoenician colonies were relatively small.
#     First 100K+ centralized polity: Carthage controlled SE Iberia from ~237 BC
#     (Barcid conquest). But that's late. Celtic-Iberian tribes had some larger
#     settlements. Conservative: -500 for Carthaginian expansion into Iberia
#     or large Iberian tribal confederations.
#     Actually the task says "at least 100,000 people under centralized political control
#     existed in this territory." Carthage's Iberian territory from 237 BC had 100K+.
#     Before that, Iberian and Celtic tribes were tribal, not centralized states.
#     Let me use -237 for Carthaginian Iberia, or -220 (Second Punic War) as the
#     existing file does. I'll keep -220 as a reasonable estimate.
#
#   -220 to -19: GAP — Roman Republic (>100M births) controlled much of Iberia from
#     ~206 BC onward but the Cantabrian Wars (29-19 BC) were needed to subdue the
#     northwest. Until 19 BC, maybe ~5-10% of Iberian peninsula population was
#     outside Roman control in the northwest. This is borderline for the 99% rule.
#     Actually, Cantabria and Asturias were sparsely populated — probably <2% of
#     Iberian population. Roman control of 99%+ may date to ~150 BC when most of
#     Iberia was pacified. Let me use -197 (creation of Hispania provinces) to -19 as
#     Roman Republic, or be conservative and use the gap.
#     The Lusitanian War ended ~139 BC, Numantine War ended 133 BC. By 133 BC
#     Rome controlled ~95%+ of Iberian population. The remaining Cantabri/Asturiani
#     were <2%. I'll assign Roman Republic from -133.
#
#   Actually, let me reconsider. The existing file has -19 to 410 as Roman Empire,
#   with gap before. The Roman Republic vs Empire distinction matters. By -133 BC
#   Rome had practical control of 99%+ of Iberia. Republic ended -27 BC.
#
#   -19 to 410: Roman Empire (includes the final Cantabrian conquest).
#     Actually, -27 to 410 for Roman Empire (Augustus onwards).
#     -133 to -27 for Roman Republic.
#
#   410 to 585: GAP — Vandals, Suevi, Alans, and Visigoths divided Iberia.
#     The Visigothic Kingdom itself had <100M births, but the broader late Roman /
#     early medieval context... Actually, no >100M polity controlled any part of Spain
#     410-585. The Western Roman Empire collapsed. The Visigothic, Suevi, and Vandal
#     kingdoms were all <100M. This should be NOT_RELEVANT.
#     Wait — the Visigoths were initially foederati of Rome, but after 476 there's
#     no Roman Empire in the west. The Eastern Roman/Byzantine Empire didn't control
#     Spain (except briefly in the SE, 552-624). Byzantine Empire >100M.
#     552-624: Byzantines held Spania (SE coast). So 552-624 has a >100M polity
#     present = gap. 410-552: NOT_RELEVANT (all polities <100M).
#
#   585 to 711: Visigothic Kingdom controlled all of Iberia (Suevi conquered 585).
#     Visigothic Kingdom total: ~3M × 0.04 × 293 = 35M. <100M.
#     Byzantine Spania was conquered by Visigoths by 624.
#     After 624, no >100M polity in Iberian territory. NOT_RELEVANT.
#     Actually 585-624: Byzantines still in SE. Visigothic Kingdom + Byzantine Empire
#     both present. Byzantine Empire >100M. = gap (Visigoths don't have 99%).
#     624-711: Only Visigothic Kingdom. <100M. NOT_RELEVANT.
#
#   711-750: Umayyad Caliphate (>100M births) conquered most of Iberia.
#     Small Christian holdouts in Asturias. Asturias had <1% of Iberian pop? Probably yes.
#     But Umayyad Caliphate didn't control 99% — Asturias was independent from 722.
#     Asturias population: ~50K-100K out of ~5M = ~1-2%. Borderline.
#     Given uncertainty, leave as gap.
#
#   711 to 1516: GAP — Multiple polities, Reconquista. Umayyad Caliphate (711-750, >100M),
#     then various Islamic and Christian states, none controlling 99%.
#     After 750: Umayyad Emirate of Cordoba (<100M), Christian kingdoms (<100M each).
#     750-1516: Are there ANY >100M polities controlling part of Spain?
#     Almoravids: <100M. Almohads: <100M. Castile: <100M alone.
#     Aragon: <100M. Actually by the late medieval period, was any polity >100M?
#     Crown of Castile + Crown of Aragon were separate until 1469/1516.
#     Neither alone exceeded 100M births. And no foreign >100M polity controlled
#     any part of Spain 750-1516.
#     750-1516 should be NOT_RELEVANT.
#
#   Actually wait — let me reconsider. The Umayyad Caliphate 711-750 controlled
#   most of Spain. 750: Abbasid revolution, but Umayyads kept Iberia.
#   The Abbasid Caliphate (>100M) briefly claimed Iberia but never effectively
#   controlled it. So after 750, no >100M polity in Spain. NOT_RELEVANT.
#
#   1516-1700: Habsburg Spain. The Spanish Empire as a whole >100M births.
#     Controls 99%+ of modern Spain. ✓
#
#   1700-1714: War of Spanish Succession. France (>100M) backed Philip V,
#     Austria/HRE (>100M) backed Archduke Charles. Both >100M polities involved.
#     = gap.
#
#   1714-1808: Bourbon Spain. Controls 99%+.
#   1808-1814: Peninsular War. Napoleon's First French Empire (>100M births) and
#     the Spanish government both claimed control. = gap.
#   1814-1868: Bourbon Spain restored.
#   1868-1874: Sexenio Democrático (revolution, Amadeo I, First Republic).
#     Spain itself in this period: avg ~16M × 0.04 × 6 = 3.8M. <100M.
#     No >100M foreign polity controlled any part. NOT_RELEVANT? No—this IS Spain,
#     just a different regime. The "polity" is Spain with regime changes.
#     Actually per the splitting view, the Provisional Government/First Republic
#     is a different regime from Bourbon Spain. Duration too short for 100M births.
#     But it's still Spain — a sovereign state. The issue is whether it exceeds 100M.
#     Spanish state 1868-1874 with colonies: ~20M × 0.04 × 6 = 4.8M. <100M.
#     But wait — the task says "polities existed but ALL of them had fewer than
#     100 million lifetime births." The polity IS Spain (just under different governance).
#     The lifetime births of "Spain" as a continuous entity 1516-2026 vastly exceed 100M.
#     The splitting view means we treat each regime separately: Spanish First Republic
#     (1873-1874) = ~16M × 0.04 × 1 = 0.6M. <100M.
#     Provisional Government (1868-1871) = ~16M × 0.04 × 3 = 1.9M. <100M.
#     Amadeo I (1871-1873) = ~16M × 0.04 × 2 = 1.3M. <100M.
#     These are all <100M. But is there any >100M polity controlling part of Spain?
#     Spain controlled itself. The entity "Bourbon Spain" had >100M total births
#     but no longer existed 1868-1874. This should be NOT_RELEVANT since all
#     polities controlling Spanish territory during 1868-1874 had <100M births.
#     Actually, hmm. The *prior* Bourbon regime and *subsequent* restoration are
#     different entries. The regimes during 1868-1874 each had <100M births, and
#     no external >100M polity controlled any part. NOT_RELEVANT.
#
#   1874-1931: Bourbon Restoration Spain. With colonies (until 1898): avg ~20M × 0.04 × 57 = 46M.
#     Without colonies (1898-1931): ~20M × 0.04 × 33 = 26M. Total = 72M. <100M.
#     Hmm, but the question is about the polity, not just the Spanish territory period.
#     Actually for the "splitting view," Bourbon Restoration is one regime from 1874-1931.
#     Spain proper: ~18M avg × 0.04 × 57 = 41M. Plus colonies: early period ~25M total,
#     later ~18M. Say avg ~21M × 0.04 × 57 = 48M. <100M.
#     No >100M external polity controlled Spanish territory. NOT_RELEVANT.
#
#   Wait, I'm overcomplicating this. The task says to use NOT_RELEVANT when ALL polities
#   controlling ANY PART of the territory had <100M lifetime births. For Spain 1868-1874
#   and 1874-1931, the only polity is Spain itself under various regimes. Each regime
#   individually has <100M births. But hmm, is "Spain" one polity across regime changes?
#   The task says "splitting view" — so each regime is separate.
#
#   Let me reconsider: the task wants me to distinguish regimes. But a regime that only
#   lasted 6 years can't possibly have 100M births. However, the instruction says
#   "err strongly on the side of leaving a gap." And the sovereign state of Spain
#   is continuously present — it's debatable whether "Bourbon Restoration Spain" and
#   "Spanish First Republic" are truly different polities vs. regime changes within one.
#   I think the safest interpretation: if the underlying sovereign state clearly exceeds
#   100M births across its history, individual regime periods should be gaps, not
#   NOT_RELEVANT. The "Spanish state" from 1516 onward is one continuous entity with
#   regime changes. Its total: ~15M avg × 0.04 × 510 = 306M. >100M.
#
#   OK but the task specifically says to use splitting view. Let me just be practical:
#   assign named polities where 99% control is clear, use gaps where >100M polities
#   are present, and NOT_RELEVANT only when truly no large polity exists.
#
#   For 1868-1874: Spain was a sovereign state; its prior and subsequent regimes each
#   had >100M births across their lifespans (debatable for Restoration). There's genuine
#   ambiguity. Per "err on the side of gaps," I'll leave as gap.
#
#   For 1936-1939: Civil War. Spain as a state still existed with >100M births over time.
#   = gap.

SPAIN = [
    (-200000, -220, 'NO_KNOWN_POLITIES'),
    # GAP -220 to -133: Roman Republic (>100M births total) was conquering Iberia
    # but didn't yet control 99%. Celtiberian resistance ongoing.
    (-133, -27, 'Roman Republic'),
    (-27, 410, 'Roman Empire'),
    (410, 552, 'NOT_RELEVANT'),
    # All polities in Iberia 410-552 were <100M births:
    # Visigoths (~35M), Suevi (~5M), Vandals (left for Africa 429).
    # No >100M polity controlled any part of Iberian territory.
    # GAP 552-624: Byzantine Empire (>100M births) controlled Spania (SE coast).
    # Visigothic Kingdom held the rest but isn't 99%.
    (624, 711, 'NOT_RELEVANT'),
    # Visigothic Kingdom alone: ~3M × 0.04 × 87 = 10M. <100M.
    # No other polity present. All <100M.
    # GAP 711-750: Umayyad Caliphate (>100M births) conquered most of Iberia,
    # but Kingdom of Asturias (~1-2% of pop) was independent from 722.
    (750, 1516, 'NOT_RELEVANT'),
    # After 750, Umayyad Caliphate lost Iberia. Emirate/Caliphate of Cordoba (<100M),
    # Christian kingdoms each <100M. No external >100M polity controlled any part.
    # Almoravids (<100M), Almohads (<100M), Castile (<100M), Aragon (<100M).
    (1516, 1700, 'Habsburg Spain'),
    # GAP 1700-1714: War of Spanish Succession. France (>100M) and
    # Habsburg Austria/HRE (>100M) both intervened militarily.
    (1714, 1808, 'Bourbon Spain'),
    # GAP 1808-1814: Peninsular War. First French Empire (>100M births) occupied Spain.
    (1814, 1868, 'Bourbon Spain'),
    # GAP 1868-1874: Revolutionary period. The Spanish state as a continuous entity
    # (>100M births across its history from 1516) existed under rapidly changing
    # regimes, but no single regime controlled 99% for a stable period.
    # "Bourbon Spain" (>100M births across 1714-1868) had just ended.
    (1874, 1931, 'Bourbon Restoration Spain'),
    (1931, 1936, 'Spanish Second Republic'),
    # GAP 1936-1939: Civil War. The Spanish Republic (>100M births if we count
    # the continuous Spanish state) and Nationalist faction both controlled territory.
    (1939, 1975, 'Francoist Spain'),
    (1975, 2026, 'Kingdom of Spain'),
]


# =============================================================================
# PORTUGAL
# =============================================================================
#
# Key lifetime-births calculations:
#   Roman Republic/Empire: >100M (see above).
#   Visigothic Kingdom: ~35M. <100M.
#   Suevi Kingdom (411-585): ~500K × 0.04 × 174 = 3.5M. <100M.
#   Umayyad Caliphate (661-750): >100M overall. Controlled Portugal 711-750.
#   Umayyad Emirate of Cordoba (756-929): ~5M × 0.04 × 173 = 35M. <100M.
#   Caliphate of Cordoba (929-1031): ~5M × 0.04 × 102 = 20M. <100M.
#   County of Portugal / Kingdom of Portugal (1139-1910):
#     Portugal alone: avg ~2M × 0.04 × 771 = 62M. <100M.
#     Portuguese Empire total: avg ~5M × 0.04 × 584 = 117M. >100M (from ~1415).
#     But in the early period (1139-1415), Portugal was just the kingdom itself: <100M.
#     1139-1415: ~1.5M × 0.04 × 276 = 17M. <100M.
#   Kingdom of Leon (910-1230): ~2M × 0.04 × 320 = 26M. <100M.
#   Kingdom of Castile: <100M (see Spain).
#   Iberian Union (1580-1640): This is Habsburg Spain, which is >100M.
#
# Portugal is tricky because the Kingdom of Portugal as a standalone entity (pre-empire)
# was <100M births. But the Portuguese Empire from ~1500s had colonies that push it over.
# When does the empire cross 100M? Portuguese Empire 1415-1999:
#   1415-1500: ~1.5M avg × 0.04 × 85 = 5M.
#   1500-1600: ~3M avg (Portugal ~1.5M + Brazil growing + African/Asian posts) × 0.04 × 100 = 12M.
#   1600-1700: ~4M avg × 0.04 × 100 = 16M.
#   1700-1800: ~5M avg × 0.04 × 100 = 20M.
#   1800-1822: ~8M avg × 0.04 × 22 = 7M. (Brazil ~4M + Portugal ~3M + others)
#   So by 1822 (Brazil independence): cumulative ~60M. Not yet 100M.
#   After 1822: Portugal ~3.5M + remaining colonies ~1M = ~4.5M avg.
#   4.5M × 0.04 × 177 (1822-1999) = 32M. Grand total ~92M. Still <100M.
#
# Hmm, let me recalculate more carefully.
# Kingdom of Portugal 1139-1580: avg ~1.5M × 0.04 × 441 = 26M.
# Iberian Union 1580-1640: Habsburg Spain >100M.
# Kingdom of Portugal 1640-1910:
#   Portugal proper: avg ~3M × 0.04 × 270 = 32M.
#   + Brazil (1640-1822): avg ~2M × 0.04 × 182 = 15M.
#   + African colonies + others: small.
#   Total ~50M. <100M.
# Portuguese First Republic 1910-1926: ~6M × 0.04 × 16 = 3.8M.
# Estado Novo 1933-1974: ~8M (with colonies) × 0.04 × 41 = 13M.
#
# So the Kingdom of Portugal (1640-1910) as a whole: ~50M. <100M.
# The Kingdom of Portugal (1139-1580): ~26M. <100M.
# Each Portuguese regime is <100M.
#
# But the continuous Portuguese state 1139-1910 (minus Iberian Union):
# 26M + 50M = 76M. Still <100M.
# Including everything 1139-2026 (minus 1580-1640):
# 76M + 3.8M + ~5M + 13M + ~10M = ~108M. Just over 100M across 850 years.
#
# This is very borderline. The "Kingdom of Portugal" from 1249-1580 alone: <100M.
# But the continuous Portuguese state across its whole existence: ~100M.
# Per "err on the side of gaps," I'll treat Portuguese regimes as gaps rather than
# NOT_RELEVANT for the later period when the cumulative state is large.
# For the early period (1139-1249, even 1249-1580), the state was clearly <100M.
#
# Actually, I think I'm overcomplicating this. For Portugal 1139-1580:
# The ONLY polity controlling Portuguese territory is the Kingdom of Portugal.
# Its lifetime births are ~26M. <100M. No external >100M polity controls any part.
# This should be NOT_RELEVANT for periods where Portugal is the only polity and <100M.
#
# Wait, but 1249 onward the Kingdom of Portugal controlled 99%+ of modern Portugal.
# Before 1249, the Reconquista was ongoing (Algarve conquered 1249).
#
# For the whole period where Kingdom of Portugal existed:
# The question is whether ANY polity controlling ANY PART had >100M births.
# 1249-1580: Only Kingdom of Portugal. <100M births. = should use Kingdom of Portugal
# as the polity name since it controls 99%, OR mark as NOT_RELEVANT.
# But the task says to use the polity name when it controls 99%+.
# So: (1249, 1580, 'Kingdom of Portugal') — even though it has <100M births.
# The 100M threshold is for NOT_RELEVANT, not for named polities!
# Named polities are used when one polity controls 99%+ regardless of size.
#
# Re-reading the rules: NOT_RELEVANT is for periods where polities existed but ALL
# had <100M births. Named polity is for when one controls 99%+. These are independent.
# A named polity can be assigned even if it has <100M births — the 100M threshold
# only determines NOT_RELEVANT vs gap for periods without a clear 99% controller.
#
# This simplifies things enormously!

PORTUGAL = [
    (-200000, -220, 'NO_KNOWN_POLITIES'),
    # GAP -220 to -138: Roman Republic (>100M births) was expanding into Iberia
    # but Lusitania (modern Portugal) not yet conquered.
    # Actually, Romans arrived in Portugal ~194 BC but Lusitanian War ended ~139 BC.
    # Before -194: only local tribes. Are there >100M polities present?
    # Carthage controlled parts of SE Iberia but not Portugal. Rome was >100M.
    # Rome controlled the eastern/southern coast by ~194 BC.
    # I'll say gap from -220 to -138 since Rome (>100M) was actively present/expanding.
    (-138, -27, 'Roman Republic'),  # Lusitania fully conquered by ~138 BC
    (-27, 410, 'Roman Empire'),
    (410, 585, 'NOT_RELEVANT'),
    # Suevi Kingdom controlled most of modern Portugal; Visigoths in south.
    # Suevi: ~3.5M births. Visigothic: ~35M. Both <100M.
    # No >100M polity controlled any part of Portuguese territory.
    (585, 711, 'NOT_RELEVANT'),
    # Visigothic Kingdom alone: <100M. No other polity present.
    # GAP 711-750: Umayyad Caliphate (>100M births) conquered Portugal.
    # But Christian resistance in far north (Asturias/Galicia) — not exactly in
    # modern Portugal's territory though. Umayyad control was near-total.
    # By 99% rule, Caliphate probably controlled 99%+ of modern Portugal's pop.
    # Actually, Asturias was outside Portugal. The Umayyad Caliphate controlled
    # essentially all of modern Portugal 711-750.
    (711, 750, 'Umayyad Caliphate'),
    (750, 1139, 'NOT_RELEVANT'),
    # After 750: Umayyad Emirate/Caliphate of Cordoba (<100M, ~55M),
    # then taifa states, Almoravids (<100M), Almohads (<100M).
    # Christian kingdoms (Leon, Castile) expanding south but each <100M.
    # No single >100M polity controlled any part.
    (1139, 1249, 'NOT_RELEVANT'),
    # County/Kingdom of Portugal existed but didn't yet control all of modern Portugal
    # (Algarve not yet conquered). Kingdom of Portugal: <100M.
    # No >100M polity controlled any part.
    # Actually, by 1139-1249, the Kingdom of Portugal controlled most of modern Portugal
    # except the Algarve. Should this be a named polity? The Algarve (southernmost region)
    # was held by Almohads/Moors until 1249. Its population was maybe 5-10% of total.
    # Fails 99% rule. So can't assign Kingdom of Portugal.
    # All polities <100M. NOT_RELEVANT.
    (1249, 1580, 'Kingdom of Portugal'),
    (1580, 1640, 'Iberian Union'),  # Habsburg Spain, >100M
    (1640, 1910, 'Kingdom of Portugal'),
    (1910, 1926, 'Portuguese First Republic'),
    (1926, 1933, 'Ditadura Nacional'),
    (1933, 1974, 'Estado Novo'),
    (1974, 2026, 'Portuguese Third Republic'),
]


# =============================================================================
# GREECE
# =============================================================================
#
# Key lifetime-births calculations:
#   Achaemenid Empire (550-330 BC): avg ~25M × 0.04 × 220 = 220M. >100M.
#     Briefly controlled parts of Greece (Thrace, Macedonia) and invaded mainland.
#     Actually, Achaemenid control of Greek territory was limited to Thrace and
#     Ionia (Asia Minor, not modern Greece). Brief occupation in 480-479 BC.
#     Thrace (northern Greece) was a Persian satrapy ~512-479 BC.
#   Macedonian Kingdom/Empire: Alexander's empire was brief. Antigonid Macedonia
#     (306-168 BC): ~3M × 0.04 × 138 = 17M. <100M.
#   Seleucid Empire: didn't control Greece proper (mostly Asia).
#   Roman Republic: >100M. Controlled Greece from 146 BC (destruction of Corinth).
#     Actually, Macedonia became a province in 148 BC. Southern Greece (Achaea) in 146 BC.
#   Roman Empire: >100M.
#   Byzantine Empire: >100M.
#   Latin Empire (1204-1261): ~1M × 0.04 × 57 = 2.3M. <100M.
#   Republic of Venice: <100M (see Italy).
#   Ottoman Empire: >100M.
#   Kingdom of Greece: ~4M avg × 0.04 × 115 (1832-1947) = 18M. <100M.
#
# Greece is complicated because of the Ionian Islands (Venetian until 1797, then
# British until 1864) and Dodecanese (Italian until 1947).
#
# Timeline:
#   -200000 to -800: NO_KNOWN_POLITIES
#     Mycenaean civilization collapsed ~1200 BC. Dark Ages ~1200-800 BC.
#     City-states emerged ~800 BC but none had 100K+ under centralized control
#     until later. Athens by ~500 BC had ~300K total (including slaves/metics).
#     Argos, Corinth, Sparta were significant by 700 BC.
#     Actually, Mycenaean palaces (1600-1200 BC) were centralized polities.
#     Did any have 100K+ under centralized control? The Mycenaean world was
#     divided into several palace centers (Mycenae, Pylos, Thebes, Tiryns).
#     Each controlled maybe 10-50K people. Collectively ~500K? But not one polity.
#     Minoan Crete (2000-1450 BC): Knossos controlled maybe 50-100K? Borderline.
#     I'll use -1600 for Mycenaean palace systems as a conservative estimate of
#     when centralized polities of 100K+ existed.
#     Actually, the task says "at least 100,000 people under centralized political
#     control existed in this territory." The Mycenaean palace-states may qualify.
#     But it's debatable whether any single palace controlled 100K.
#     I'll use -800 as in the existing file (Greek city-states emerging).
#     By -750 BC, some polities had 100K+ (Sparta controlled Laconia/Messenia).
#
#   -800 to -146: GAP — Multiple city-states, no single one controlled 99%.
#     Achaemenid Empire (>100M) briefly controlled Thrace/Macedonia ~512-479 BC.
#     Roman Republic (>100M) was expanding into Greece from ~200 BC.
#     Justification: Roman Republic (>100M births) controlled Macedonia from 168 BC
#     and was intervening in Greek affairs. Achaemenid Empire (>100M) earlier.
#     Actually, for -800 to -512: no >100M polity controlled any part of Greece.
#     City-states were all small. This should be NOT_RELEVANT for -800 to -512.
#     -512 to -479: Achaemenid Empire (>100M) controlled Thrace/parts of N. Greece.
#     -479 to -168: Macedonian kingdom + city-states. All <100M.
#       Delian League / Athenian Empire: ~2M × 0.04 × 73 = 5.8M. <100M.
#       NOT_RELEVANT for -479 to -168? No — wait.
#       Roman Republic (>100M total births over its existence) was growing but
#       didn't control any Greek territory until ~200 BC interventions.
#       -479 to -200: no >100M polity in Greek territory. NOT_RELEVANT.
#       -200 to -146: Roman Republic (>100M) actively intervening and controlling
#       parts (Macedonia from 168 BC). Gap.
#
#   -146 to -27: Roman Republic — controlled all of Greece.
#   -27 to 395: Roman Empire.
#   395 to 580: Byzantine Empire — initially controlled all of Greece.
#     But Slavic invasions began disrupting mainland Greece ~580.
#   580 to 800: GAP — Slavic tribes occupied much of mainland Greece, reducing
#     Byzantine control to coastal/island areas. Byzantine Empire (>100M) held
#     some territory but not 99%.
#     Justification: Byzantine Empire (>100M births) still controlled islands,
#     coastal cities, and Peloponnese fortresses.
#   800 to 1204: Byzantine Empire — reasserted control over mainland Greece.
#   1204 to 1460: GAP — Fourth Crusade shattered Byzantine control. Latin Empire,
#     Principality of Achaea, Duchy of Athens, Venetian territories, and gradually
#     Ottoman conquest. Multiple polities.
#     Justification: Byzantine Empire (>100M births) held some territories (Nicaea,
#     then reconquered Constantinople 1261, held parts of Greece).
#     Ottoman Empire (>100M) began conquering from ~1360s.
#     Republic of Venice (<100M) held islands.
#     Actually Venice is <100M. But Byzantine (>100M) and then Ottoman (>100M)
#     were present. Gap justified by Byzantine Empire and Ottoman Empire.
#   1460 to 1669: GAP — Ottoman Empire controlled mainland Greece and most islands.
#     But Crete was still Venetian (fell 1669). Ionian Islands also Venetian.
#     Crete was ~5-8% of "Greek" population. Fails 99%.
#     Venice itself is <100M. But Ottoman Empire is >100M and controls most.
#     Justification: Ottoman Empire (>100M) controlled ~90%+ of Greek territory.
#   1669 to 1821: Ottoman Empire controlled mainland + Crete.
#     But Ionian Islands were Venetian (until 1797), then French (1797-1799),
#     then Russo-Ottoman (1800-1807), then British (1809-1864).
#     Ionian Islands population: ~200K out of ~2.5M Greeks = ~8%. Fails 99%.
#     Hmm, but the task asks about "modern country's current borders."
#     Ionian Islands are part of modern Greece. So we need 99% of population
#     within modern Greece's borders. Ionian Islands = ~5-8%. Ottoman Empire
#     controlled ~92-95%. Can't assign Ottoman Empire.
#     Justification for gap: Ottoman Empire (>100M) controlled ~92-95%.
#
#   Actually, let me reconsider the Ionian Islands population proportion.
#   In 1800: Greek territory (within modern borders) population ~2.5M.
#   Ionian Islands: ~200K = 8%. That's too much for 99% rule.
#   In 1797 (end of Venetian control): Corfu, Cephalonia, Zakynthos, etc.
#   Total Ionian pop ~180K. Rest of modern Greece ~2.3M = 7%. Still too much.
#
#   After Crete fell (1669) but before Greek independence:
#   Ottoman controlled ~92% of modern Greece's population. Not 99%.
#   Gap with Ottoman Empire (>100M) as justification.
#
#   1821-1832: Greek War of Independence. Ottoman Empire (>100M) vs rebels.
#   1832-1864: Kingdom of Greece, but missing Ionian Islands (~5-8% of eventual pop),
#     Thessaly, Epirus, Crete, Dodecanese, etc. The Kingdom of Greece in 1832 had
#     maybe only 40-50% of modern Greece's territory/population. Not 99%.
#   1864: Ionian Islands joined. Now ~60-65% of modern territory.
#   1881: Thessaly joined. ~70-75%.
#   1913: Macedonia, Epirus, Crete joined. ~95%.
#   1920/1923: Western Thrace. ~98%.
#   1947: Dodecanese (from Italy). Now 99%+.
#
#   So Kingdom of Greece / Hellenic Republic only controlled 99%+ from 1947.
#   Before that: Ottoman Empire (>100M) held parts, then various polities.
#   Italian Kingdom held Dodecanese 1912-1947. Kingdom of Italy: >100M? Let me check.
#   Kingdom of Italy 1861-1946: avg ~35M × 0.04 × 85 = 119M. >100M.
#   So 1912-1947: Kingdom of Italy (>100M) held Dodecanese. Gap.
#   1913-1947: Only Dodecanese was outside Greece. Pop ~120K out of ~6-7M = ~1.7%.
#   Borderline for 99% rule. 98.3% is close but fails.
#   Hmm, this is really borderline. Actually Dodecanese had ~140K population.
#   Greek population within modern borders ~7M by 1947. 140K/7M = 2%.
#   Fails 99%.
#   But in 1913-1940: Dodecanese was ~1.7% (120K/7M). Still >1%.
#
#   I'll follow the existing file's approach: Greece only cleanly assignable from 1947.

GREECE = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, -512, 'NOT_RELEVANT'),
    # Greek city-states emerged but none had >100M lifetime births.
    # Athens: ~2M × 0.04 × 200 = 16M. Sparta: similar. All <100M.
    # No external >100M polity present in Greek territory.
    # GAP -512 to -479: Achaemenid Empire (>100M births) controlled Thrace and
    # parts of northern Greece (Macedonia submitted to Persia).
    (-479, -200, 'NOT_RELEVANT'),
    # After Persian withdrawal. Greek city-states, Macedonian Kingdom, Hellenistic
    # successor states — all <100M births individually.
    # Delian League: <100M. Antigonid Macedonia: <100M. No >100M polity present.
    # GAP -200 to -146: Roman Republic (>100M births) actively intervening in Greece,
    # controlling Macedonia from 168 BC.
    (-146, -27, 'Roman Republic'),
    (-27, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),
    # GAP 580-800: Slavic invasions; Byzantine Empire (>100M births) held islands
    # and some coastal areas but not 99% of mainland.
    (800, 1204, 'Byzantine Empire'),
    # GAP 1204-1947: Extremely fragmented. After Fourth Crusade: Latin Empire,
    # Venetian territories, Frankish principalities. Then Ottoman conquest.
    # After independence (1832): Kingdom of Greece gradually expanded but didn't
    # encompass 99% of modern Greece's population until Dodecanese transfer (1947).
    # Justification: Byzantine Empire (>100M) 1204-1453, Ottoman Empire (>100M)
    # 1354-1821, Kingdom of Italy (>100M) held Dodecanese 1912-1947.
    (1947, 1967, 'Kingdom of Greece'),
    (1967, 1974, 'Greek military junta'),
    (1974, 2026, 'Hellenic Republic'),
]


# =============================================================================
# SWITZERLAND
# =============================================================================
#
# Key lifetime-births calculations:
#   Roman Empire: >100M.
#   Alamannic/Burgundian kingdoms (5th-6th c.): tiny. <100M.
#   Frankish Kingdom/Carolingian Empire: borderline.
#     Merovingian Frankish Kingdom (481-751): ~5M × 0.04 × 270 = 54M. <100M.
#     Carolingian Empire (751-888): ~10M × 0.04 × 137 = 55M. <100M.
#     Combined Frankish Kingdom (481-843): ~7M × 0.04 × 362 = 101M. Just >100M.
#     Hmm, marginal. The Frankish state from Clovis to Charlemagne's grandsons
#     is arguably one continuous polity with >100M births.
#   Holy Roman Empire: >100M.
#   Old Swiss Confederacy (1291-1798): avg ~500K-1M × 0.04 × 507 = 10-20M. <100M.
#   Helvetic Republic (1798-1803): ~1.7M × 0.04 × 5 = 0.3M. <100M.
#   Swiss Confederation (1815-2026): avg ~4M × 0.04 × 211 = 34M. <100M.
#   First French Empire (1804-1815): >100M (France ~30M + vassals/empire ~60M+).
#     Actually, First French Empire: ~44M (France) + ~40M (rest) = ~84M × 0.04 × 11 = 37M. <100M.
#     Hmm, that's short-lived. But the French Republic/Empire 1792-1815:
#     ~30M × 0.04 × 23 = 28M. <100M.
#     The broader "French state" (Kingdom + Republic + Empire): >100M total.
#     Napoleonic France specifically 1799-1815: ~40M × 0.04 × 16 = 26M. <100M.
#   Kingdom of France: >100M (see above). But did it control Swiss territory? No,
#     Switzerland was in the HRE and then independent.
#
# Switzerland's small population means most polities controlling it are <100M
# UNLESS they're part of a larger empire (Rome, HRE).
#
# Timeline:
#   -200000 to -400: NO_KNOWN_POLITIES
#     Celtic settlements (La Tene culture centered in Switzerland!). The Helvetii
#     tribe was significant but was a tribal confederation, not a centralized state
#     of 100K+ under political control? Actually the Helvetii were ~250K people
#     (Caesar's count ~263K for the migration of 58 BC). They had centralized
#     political leadership. ~400 BC is reasonable.
#     Actually, La Tene culture from ~450 BC. The Helvetii as a organized polity
#     with centralized control existed from roughly 400-58 BC.
#     But was it "centralized political control" or a tribal confederation?
#     The Helvetii had a central council and could organize a mass migration (58 BC).
#     I'd call it borderline. The existing file uses -400. Let me keep it.
#
#   -400 to -58: The Helvetii controlled Swiss Plateau but this is a tribal
#     confederation. NOT_RELEVANT (all polities <100M).
#     Actually, is there any >100M polity controlling Swiss territory -400 to -58?
#     No. Only the Helvetii and smaller Celtic tribes. NOT_RELEVANT.
#
#   Actually -400 to -15: NOT_RELEVANT until Roman conquest.
#     Romans conquered Swiss territory: Ticino ~200 BC (part of Cisalpine Gaul),
#     but most of Switzerland conquered 15 BC (Raetia/Helvetia).
#     Wait, Helvetii were made a Roman client state after 58 BC (Caesar's defeat
#     of their migration). But formal provincial incorporation was ~15 BC.
#     58-15 BC: Roman Republic/Empire (>100M) had suzerainty.
#     Hmm, from -58 onward Rome controlled the Helvetii. Let me use:
#     -400 to -58: NOT_RELEVANT (Celtic tribes, all <100M).
#     -58 to -15: Roman Republic influence/control. Gap? Rome (>100M) was present
#     but was it 99%? After 58 BC, the Helvetii were under Roman authority.
#     The Alpine regions (Raetia) were independent until 15 BC. Raetia's pop
#     within modern Swiss borders was maybe 5-10% of total. Fails 99%.
#     -15 BC: All of modern Switzerland under Roman control.
#
#   Let me simplify. The existing file has (-200000, -400, NO_KNOWN_POLITIES)
#   and (-15, 401, Roman Empire). I need to fill -400 to -15.
#
#   -400 to -58: NOT_RELEVANT. Helvetii + Raetian tribes. All <100M. No external
#     >100M polity present.
#   -58 to -15: GAP. Roman Republic (>100M) controlled Helvetii (Swiss Plateau)
#     but not Alpine Raetia (~5-10% of modern Swiss territory's pop).
#
#   -15 to 401: Roman Empire. All of modern Switzerland incorporated.
#     Rome withdrew from Swiss territory gradually in early 5th century.
#     The Rhine frontier fell ~401-406.
#
#   401 to 534: NOT_RELEVANT. Alamanni (north/east) and Burgundians (west).
#     Both tiny. <100M. No >100M polity present.
#
#   534 to 843: GAP? Frankish Kingdom conquered Burgundy (534) and Alamannia (536),
#     bringing all of Switzerland under Frankish control.
#     Frankish Kingdom (481-843): Is this >100M? ~7M avg × 0.04 × 362 = 101M.
#     Just barely >100M. But it controlled 99%+ of modern Switzerland from 536 to 843.
#     Actually, I should assign it: (536, 843, 'Frankish Kingdom').
#     But wait — should I split Merovingian vs Carolingian?
#     Merovingian: 481-751. Carolingian: 751-843 (then split).
#     Per splitting view: Merovingian Frankish Kingdom (481-751): ~5M × 0.04 × 270 = 54M. <100M.
#     Carolingian Empire (751-843): ~10M × 0.04 × 92 = 37M. <100M.
#     Neither regime individually exceeds 100M.
#     But both ARE the Frankish Kingdom — continuous state with regime change.
#     Hmm, this is like the Spain situation. The Merovingian-to-Carolingian transition
#     was a dynastic change within the Frankish state. Using splitting view, they're
#     different. Neither individually >100M.
#     But each controlled 99% of Swiss territory. So they should be named polities!
#     Remember: 100M threshold is for NOT_RELEVANT, not for named polities.
#     A small polity can still be assigned if it controls 99%.
#
#   (536, 751, 'Merovingian Frankish Kingdom'),
#   (751, 843, 'Carolingian Empire'),
#
#   843 to 888: Kingdom of Middle Francia / Lotharingia. Swiss territory was split
#     between Middle and East Francia at Treaty of Verdun (843).
#     Actually, most of Switzerland went to Middle Francia (Lothar I), then
#     Kingdom of Burgundy / Kingdom of Italy for different parts.
#     The Swiss Plateau (Alemannic Switzerland) went to East Francia (Louis the German).
#     Romandie (French-speaking west) went to Middle Francia.
#     This is fragmented. Neither kingdom controlled 99%.
#     Are either >100M? East Francia (843-962): ~6M × 0.04 × 119 = 29M. <100M.
#     Middle Francia (843-855): very brief. <100M.
#     Kingdom of Upper Burgundy (888-1032): ~500K × 0.04 × 144 = 3M. <100M.
#
#   843 to 1032: NOT_RELEVANT? Or gap?
#     Split between East Francia (later HRE) and Kingdom of Burgundy.
#     East Francia/HRE (>100M over its full span but HRE starts 962; East Francia
#     843-962: <100M on its own). Kingdom of Burgundy: <100M.
#     962 onward: HRE >100M. But Swiss territory was split between HRE (Alemannic parts)
#     and Kingdom of Burgundy (western parts) until 1032.
#     843-962: NOT_RELEVANT (all polities <100M).
#     962-1032: GAP — HRE (>100M) controlled eastern Swiss territory; Kingdom of
#     Burgundy (<100M) controlled western parts. HRE didn't have 99%.
#     Actually, in 1032 the Kingdom of Burgundy was absorbed into the HRE.
#     Justification: Holy Roman Empire (>100M) controlled Alemannic Switzerland.
#
#   1032 to 1499: Holy Roman Empire — all of Switzerland within HRE.
#     Swiss Confederacy was de facto independent but nominally within HRE until
#     the Peace of Basel (1499) / Treaty of Westphalia (1648). Using 1499 as the
#     existing file does.
#
#   1499 to 1798: Old Swiss Confederacy / Swiss Confederation.
#     ~1M avg × 0.04 × 299 = 12M. <100M.
#     It controlled 99%+ of modern Switzerland. But it's <100M.
#     Still should be a named polity since it controls 99%.
#     Wait — the Old Swiss Confederacy was a loose confederation of cantons.
#     Was it a "polity" with centralized control? It was more of an alliance.
#     There were also "associated territories" and "subject territories."
#     The existing file leaves 1499-1798 as a gap, with only (1798, 1803, 'Helvetic Republic').
#     Let me reconsider: the Old Swiss Confederacy was not a single polity with
#     centralized control. Each canton was sovereign. It was more like a military
#     alliance. So no single polity controlled 99%.
#     All cantons individually: tiny. <100M each.
#     But collectively Switzerland was independent.
#     No external >100M polity controlled any part.
#     = NOT_RELEVANT.
#
#   1798-1803: Helvetic Republic. Napoleon imposed centralized government.
#     ~1.7M × 0.04 × 5 = 0.3M. <100M.
#     But it was a client state of France. First French Republic (>100M across
#     the broader French state's history). Hmm — the Helvetic Republic itself
#     controlled 99% of Switzerland. Assign it as named polity.
#     Or is France (>100M) the relevant polity? The Helvetic Republic was technically
#     sovereign (a sister republic). Assign as Helvetic Republic.
#
#   1803-1815: Act of Mediation — Napoleon restructured Switzerland as a confederation.
#     Mediation-era Switzerland was a French satellite. Still nominally independent.
#     ~1.7M × 0.04 × 12 = 0.8M. <100M.
#     Napoleon's French Empire (>100M as the continuous French state) dominated but
#     didn't formally annex Switzerland (except Valais, Geneva, Neuchâtel were annexed
#     to France in 1810-1812). With those annexations, ~10-15% of Swiss pop was
#     directly under France. Fails 99% for both France and Mediation Switzerland.
#     First French Empire (>100M considering the continuous French state) controlled parts.
#     = GAP.
#     Justification: First French Empire (>100M considering the French state's total
#     history) annexed Valais, Geneva, and parts of Switzerland.
#     Hmm, is First French Empire really >100M? 1804-1814: ~44M × 0.04 × 10 = 18M. <100M.
#     But the French state continuously from 987-2026: clearly >100M.
#     Per splitting view, First French Empire alone is <100M.
#     Is the Kingdom of France (987-1792) >100M? ~12M × 0.04 × 805 = 386M. >100M.
#     But it ended in 1792. The First French Republic (1792-1804) and First French
#     Empire (1804-1815) are separate regimes.
#     French First Republic: ~28M × 0.04 × 12 = 13M. <100M.
#     First French Empire: ~44M × 0.04 × 10 = 18M. <100M.
#     So no >100M polity controlled parts of Switzerland 1803-1815.
#     = NOT_RELEVANT? But the French state as a continuous entity was clearly >100M.
#     Per "err on side of gaps" — I'll make it a gap.
#     Actually... the task says to use splitting view for polity names (distinguishing
#     regimes) but when calculating lifetime births for the NOT_RELEVANT threshold,
#     should I also split? The task says "polities existed but ALL of them had fewer
#     than 100 million lifetime births" and "Use a splitting view for polity names."
#     I think the splitting applies to the timeline entries but NOT necessarily to
#     the 100M birth calculation. The "polity" for birth calculation could be the
#     continuous French state.
#     This is genuinely ambiguous. Per "err strongly on the side of leaving a gap,"
#     I'll use a gap.
#
#   1815-2026: Swiss Confederation (Congress of Vienna restored Swiss independence
#     and neutrality). This is the modern Swiss state.

SWITZERLAND = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -58, 'NOT_RELEVANT'),
    # Helvetii and Raetian tribes. All <100M lifetime births.
    # No external >100M polity controlled any part of modern Swiss territory.
    # GAP -58 to -15: Roman Republic (>100M births) controlled Swiss Plateau
    # (Helvetii) after Caesar's campaign, but Alpine Raetia (~5-10% of modern
    # Swiss territory's pop) remained independent until Augustus's conquest in 15 BC.
    (-15, 401, 'Roman Empire'),
    (401, 536, 'NOT_RELEVANT'),
    # Alamanni and Burgundians settled Swiss territory. All <100M.
    # No >100M polity controlled any part.
    (536, 751, 'Merovingian Frankish Kingdom'),
    (751, 843, 'Carolingian Empire'),
    (843, 962, 'NOT_RELEVANT'),
    # Swiss territory split between East Francia and Kingdom of Burgundy.
    # East Francia (843-962): ~6M × 0.04 × 119 = 29M. <100M.
    # Kingdom of Upper Burgundy: <100M. No >100M polity present.
    # GAP 962-1032: Holy Roman Empire (>100M births) controlled Alemannic (eastern)
    # Switzerland, but Kingdom of Burgundy (<100M) still held western parts.
    # HRE didn't control 99%.
    (1032, 1499, 'Holy Roman Empire'),
    (1499, 1798, 'NOT_RELEVANT'),
    # Old Swiss Confederacy was a loose alliance of sovereign cantons, not a
    # centralized polity. Individual cantons each <100M births.
    # No external >100M polity controlled any part of Swiss territory.
    (1798, 1803, 'Helvetic Republic'),
    # GAP 1803-1815: Act of Mediation; French Empire (arguably >100M births as
    # the continuous French state) annexed parts of Switzerland (Valais, Geneva)
    # in 1810-1812, so neither France nor the Mediation Confederation controlled 99%.
    (1815, 2026, 'Swiss Confederation'),
]
