"""
Complete polity timelines for Russia, Ukraine, Belarus, Romania, Hungary.

Each entry is (start_year, end_year, polity_name) where end_year is exclusive.
Negative years are BCE.

Special values:
- NO_KNOWN_POLITIES: No centralized polity with 100K+ people existed in this territory
- NOT_RELEVANT: Polities existed but all had <100M lifetime births
  (lifetime births = avg_population * 0.04 * years_of_existence)
- Named polity: Single polity controlled 99%+ of population in modern borders
- Gaps between entries: Indeterminate — polities with >100M lifetime births existed
  in the territory but none controlled 99%+ of the population
"""

# =============================================================================
# RUSSIA
# =============================================================================
#
# NO_KNOWN_POLITIES ends ~500 BCE: Bosporan Kingdom (founded ~480 BCE on the
#   Taman Peninsula, modern Krasnodar Krai) is the first centralized state with
#   100K+ people in modern Russia's territory.
#
# NOT_RELEVANT (-500 to -63): Bosporan Kingdom and other Black Sea Greek colonies.
#   Bosporan Kingdom: ~200K avg pop × 0.04 × 420 years = 3.4M births. Under threshold.
#   All other polities in Russian territory also well under 100M births.
#
# GAP (-63 to 1828): Large empires (>100M lifetime births) controlled parts of
#   modern Russia throughout this period, but none controlled 99%+:
#   - Roman Empire (63 BCE onward): Bosporan Kingdom as client state (Taman Peninsula)
#   - Byzantine Empire (4th–7th c.): inherited Roman positions on Black Sea coast
#   - Mongol Empire (1236–1368): controlled most of Russia
#   - Ming Dynasty (1409–1435): Nurgan Regional Military Commission in Russian Far East
#   - Ottoman Empire (1475–1696): controlled Azov (modern Rostov Oblast)
#   - Qing Dynasty (1644–1858): controlled Amur region (modern Russian Far East)
#   The Tsardom of Russia / Russian Empire was expanding throughout, but didn't reach
#   99% of the population in modern borders until the Caucasus was incorporated.
#   By 1828 (Treaty of Turkmenchay), Russia controlled Georgia, Armenia, Azerbaijan;
#   remaining Caucasus holdouts (Circassians, Chechnya) were <1% of Russia's ~50M pop.
#
# NOT_RELEVANT (1917–1922): Russian Civil War. RSFSR, White armies, Far Eastern
#   Republic — all newly formed entities with <100M lifetime births each.
#   RSFSR: ~100M pop × 0.04 × 5 years = 20M births. Under threshold.

RUSSIA = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (-500, -63, 'NOT_RELEVANT'),
    # Gap: Roman Empire, Byzantine Empire, Mongol Empire, Ming, Ottoman, Qing
    # all had >100M births and controlled parts of Russia. None controlled 99%+.
    (1828, 1917, 'Russian Empire'),
    (1917, 1922, 'NOT_RELEVANT'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Russian Federation'),
]


# =============================================================================
# UKRAINE
# =============================================================================
#
# NO_KNOWN_POLITIES ends ~600 BCE: Greek colonies (Olbia ~647 BCE, Bosporan
#   Kingdom ~480 BCE) and Scythian kingdoms in Ukrainian territory.
#
# NOT_RELEVANT (-600 to -63): Scythian kingdoms, Greek colonies — all under
#   100M lifetime births. Largest was Scythian kingdom: ~1M × 0.04 × 400 = 16M.
#
# GAP (-63 to 1939): Large empires controlled parts of Ukraine throughout:
#   - Roman Empire (63 BCE–4th c.): Crimean client states (Bosporan Kingdom)
#   - Byzantine Empire (4th–13th c.): Crimean outposts (Cherson)
#   - Mongol Empire (1240–1368): conquered all of Ukraine
#   - Ottoman Empire (1475–1774): controlled southern Ukraine, Crimea as vassal
#   - Polish-Lithuanian Commonwealth (1569–1795): controlled central/western Ukraine
#     (borderline ~100M births; erring on side of gap)
#   - Russian Empire (1654 onward, most from 1793): eastern/central Ukraine
#   - Habsburg Empire (1772–1918): controlled Galicia (western Ukraine)
#   Ukraine was consistently divided between multiple powers. Russian Empire had
#   most of it from 1793, but Austria/Austria-Hungary held Galicia (~20% of pop)
#   until 1918, and the interwar period saw division between Soviet Ukraine and
#   Poland (which held western Ukraine 1921–1939).
#
# GAP (1941–1944): WWII. Nazi Germany occupied essentially all of Ukraine.
#   Soviet Union (>100M births) still existed and was fighting to retake territory.
#   Third Reich: ~150M avg pop under control × 0.04 × 12 years = 72M (borderline;
#   erring on side of gap).

UKRAINE = [
    (-200000, -600, 'NO_KNOWN_POLITIES'),
    (-600, -63, 'NOT_RELEVANT'),
    # Gap: Roman Empire, Mongol Empire, Ottoman Empire, Russian Empire, Habsburg Empire
    # all had >100M births in Ukrainian territory. None controlled 99%+.
    (1939, 1941, 'Soviet Union'),
    # Gap: WWII — Nazi Germany occupied Ukraine; Soviet Union (>100M births) fighting back
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Ukraine'),
]


# =============================================================================
# BELARUS
# =============================================================================
#
# NO_KNOWN_POLITIES ends ~1000 CE: Polotsk Principality (part of Kievan Rus
#   sphere) is the first centralized polity with 100K+ in Belarusian territory.
#   Before this: Baltic and Slavic tribal societies without centralized states.
#
# NOT_RELEVANT (1000–1240): Polotsk and other principalities, all under 100M
#   births. Largest: Kievan Rus system, ~5M × 0.04 × 300 = 60M total, but
#   individual principalities much smaller.
#
# GAP (1240–1320): Mongol Empire (>100M lifetime births) briefly controlled
#   parts of Belarus during the 1240s invasion. Grand Duchy of Lithuania was
#   expanding into Belarus but hadn't yet consolidated control over all of it.
#
# Grand Duchy of Lithuania (1320–1569): controlled all Belarusian lands.
#   GDL: ~4M avg × 0.04 × 350 = 56M births. Under 100M threshold, so named.
#
# Polish-Lithuanian Commonwealth (1569–1772): controlled all of Belarus.
#   Ends at First Partition when Russia took eastern Belarus.
#
# GAP (1772–1795): Russian Empire (>100M births) took eastern Belarus in the
#   First Partition (1772). PLC retained western Belarus. Neither controlled 99%.
#
# Russian Empire (1795–1915): After Third Partition, controlled all of Belarus.
#   Ends when Germany occupied western Belarus in WWI.
#
# GAP (1915–1921): WWI German occupation of western Belarus; Russian Civil War;
#   Polish-Soviet War. German Empire (>100M births) occupied western Belarus
#   1915–1918. Soviet Russia fought Poland for control 1919–1921.
#
# NOT_RELEVANT (1921–1939): Western Belarus under Second Polish Republic,
#   eastern Belarus as Byelorussian SSR within Soviet Union. Both the USSR
#   and Poland were relatively young states. By the mid-1930s the USSR crossed
#   the 100M-birth threshold, but erring conservatively: the division persisted
#   and the USSR (>100M births from ~1936) controlled only part of Belarus.
#   Actually, since the USSR did cross 100M births during this period and
#   controlled eastern Belarus, this should be a gap, not NOT_RELEVANT.
#   Revising to gap.
#
# GAP (1941–1944): Nazi Germany occupied all of Belarus. Soviet Union (>100M
#   births) was fighting to retake it.

BELARUS = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    (1000, 1240, 'NOT_RELEVANT'),
    # Gap: Mongol Empire (>100M births) reached Belarus; GDL consolidating
    (1320, 1569, 'Grand Duchy of Lithuania'),
    (1569, 1772, 'Polish-Lithuanian Commonwealth'),
    # Gap: Russian Empire (>100M births) took eastern Belarus; PLC held the west
    (1795, 1915, 'Russian Empire'),
    # Gap: German Empire (>100M births) occupied western Belarus in WWI;
    # then Russian Civil War and Polish-Soviet War
    # Gap continues 1921-1939: Soviet Union (>100M births from ~1936) held
    # eastern Belarus; Poland held western Belarus. Neither controlled 99%.
    (1939, 1941, 'Soviet Union'),
    # Gap: Nazi occupation; Soviet Union (>100M births) fighting to retake
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Belarus'),
]


# =============================================================================
# ROMANIA
# =============================================================================
#
# NO_KNOWN_POLITIES ends ~300 BCE: Dacian/Getic kingdoms (Dromichaetes ~300 BCE)
#   are the first centralized polities with 100K+ in Romanian territory.
#
# NOT_RELEVANT (-300 to -46): Dacian kingdoms, Greek colonies on Black Sea coast.
#   Dacian kingdom of Burebista (~82–44 BCE) was large but brief.
#   All under 100M lifetime births.
#
# GAP (-46 to 681): Roman Empire (>100M births) controlled Dobrudja from ~46 CE
#   (province of Moesia Inferior) and Transylvania/Wallachia from 106 CE (province
#   of Dacia). Rome withdrew from Dacia in 271 but retained Dobrudja. Byzantine
#   Empire continued control of Dobrudja until the Bulgarian conquest ~681.
#   Neither Rome nor Byzantium controlled 99% of modern Romania at any point
#   (eastern plains and Moldavia were outside Roman/Byzantine control).
#
# NOT_RELEVANT (681–1018): First Bulgarian Empire controlled Dobrudja.
#   Bulgaria: ~3M avg × 0.04 × 337 = 40M births. Under threshold.
#   Hungarian tribal state in Transylvania from ~900 CE: small, under threshold.
#
# GAP (1018–1185): Byzantine Empire (>100M births) reconquered Bulgaria and
#   controlled Dobrudja. Kingdom of Hungary controlled Transylvania. Neither
#   controlled 99% of modern Romania.
#
# NOT_RELEVANT (1185–1396): Second Bulgarian Empire in Dobrudja, Kingdom of Hungary
#   in Transylvania, emerging principalities of Wallachia (1310) and Moldavia (1346).
#   All under 100M lifetime births individually.
#   Kingdom of Hungary: ~3.5M × 0.04 × 526 = 74M. Under threshold.
#
# GAP (1396–1918): Ottoman Empire (>100M births) controlled Wallachia, Moldavia,
#   and Dobrudja as vassals or directly from the late 14th century. Habsburg Empire
#   / Austria-Hungary (>100M births) controlled Transylvania from 1699. Kingdom of
#   Romania (from 1859/1881) controlled Wallachia + Moldavia + Dobrudja (from 1878)
#   but NOT Transylvania, which remained Austro-Hungarian until 1918.
#
# Kingdom of Romania (1918–1940): After WWI, Romania gained Transylvania, Bukovina,
#   and Bessarabia. "Greater Romania" controlled all of modern Romania's territory.
#
# NOT_RELEVANT (1940–1945): Hungary took Northern Transylvania (Second Vienna Award,
#   1940). Romania retained the rest. Both Romania (~14M × 0.04 × 59 = 33M by 1940)
#   and Horthy's Hungary (~9M × 0.04 × 24 = 9M) were under 100M births.
#   No other polity directly controlled Romanian territory.
#
# Kingdom of Romania continues (1945–1947): Northern Transylvania returned.
#   King Michael reigned until forced abdication Dec 30, 1947.

ROMANIA = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, -46, 'NOT_RELEVANT'),
    # Gap: Roman Empire (>100M births) controlled Dobrudja and Dacia
    (681, 1018, 'NOT_RELEVANT'),
    # Gap: Byzantine Empire (>100M births) reconquered Dobrudja
    (1185, 1396, 'NOT_RELEVANT'),
    # Gap: Ottoman Empire + Habsburg Empire (both >100M births) divided Romania
    (1918, 1940, 'Kingdom of Romania'),
    (1940, 1945, 'NOT_RELEVANT'),
    (1945, 1947, 'Kingdom of Romania'),
    (1947, 1965, "Romanian People's Republic"),
    (1965, 1989, 'Socialist Republic of Romania'),
    (1989, 2026, 'Romania'),
]


# =============================================================================
# HUNGARY
# =============================================================================
#
# NO_KNOWN_POLITIES ends ~100 BCE: Celtic tribal kingdoms (Scordisci, Boii,
#   Eravisci) and Dacian expansion under Burebista reached the Pannonian plain.
#   First centralized polities with 100K+ people in Hungarian territory.
#
# NOT_RELEVANT (-100 to -9): Celtic and Dacian kingdoms — all under 100M births.
#
# GAP (-9 to 433): Roman Empire (>100M births) controlled Pannonia (western Hungary,
#   west of the Danube) from 9 BCE. Eastern Hungary (Great Hungarian Plain) remained
#   under Sarmatian (Iazyges) control, outside Roman territory. Rome never controlled
#   99% of modern Hungary's population.
#
# NOT_RELEVANT (433–796): Hunnic Empire (~5M × 0.04 × 80 = 16M), Gepid Kingdom,
#   Lombard Kingdom, Avar Khaganate (~4M × 0.04 × 228 = 36M) — all under 100M births.
#
# GAP (796–895): Carolingian Empire controlled Pannonia after destroying the Avar
#   Khaganate. Carolingian Empire: ~20–25M avg × 0.04 × 120 years = 96–120M births.
#   Borderline; erring on side of gap. Bulgarian Empire had influence in eastern areas.
#
# NOT_RELEVANT (895–1000): Magyar tribal confederation settling the Carpathian Basin.
#   Grand Principality of Hungary: ~500K–1M × 0.04 × 105 = 2–4M births. Under threshold.
#   No other large polity controlled Hungarian territory.
#
# Kingdom of Hungary (1000–1526): Founded by Stephen I. Controlled all of modern
#   Hungary (and much more). ~3.5M avg × 0.04 × 526 = 74M births. Under 100M
#   threshold, so qualifies as named polity. Ends at Battle of Mohacs (1526).
#
# GAP (1526–1699): Ottoman Empire (>100M births) controlled central Hungary
#   (Buda Eyalet, including most of the Great Plain). Habsburg Empire (>100M births)
#   controlled Royal Hungary (western/northern strips). Principality of Transylvania
#   controlled eastern areas. No single polity controlled 99% of modern Hungary.
#
# Habsburg Empire (1699–1804): After Treaty of Karlowitz, Habsburgs controlled all
#   of Hungary. Renamed to Austrian Empire in 1804.
#
# Austrian Empire (1804–1867): Francis II proclaimed Austrian Empire. Controlled all
#   of Hungary until Compromise of 1867.
#
# Austria-Hungary (1867–1918): Dual monarchy. Hungary had internal autonomy but
#   the Austro-Hungarian state controlled 99%+ of modern Hungary's territory.
#
# NOT_RELEVANT (1918–1920): Post-WWI chaos — Hungarian Democratic Republic (Oct 1918),
#   Hungarian Soviet Republic (Mar–Aug 1919), Romanian occupation of Budapest (1919),
#   counter-revolutionary government. All under 100M lifetime births.
#
# Kingdom of Hungary (1920–1944): Horthy regency within Trianon borders (≈ modern
#   Hungary). Ends with Nazi German occupation (March 1944).
#
# GAP (1944–1946): Nazi Germany occupied Hungary (March 1944). Soviet Union (>100M
#   births) advanced through Hungary (Oct 1944 – April 1945). Territory divided
#   between occupying forces. Provisional government formed Dec 1944, but country
#   under Soviet military administration until republic proclaimed Feb 1946.

HUNGARY = [
    (-200000, -100, 'NO_KNOWN_POLITIES'),
    (-100, -9, 'NOT_RELEVANT'),
    # Gap: Roman Empire (>100M births) controlled western Hungary (Pannonia)
    (433, 796, 'NOT_RELEVANT'),
    # Gap: Carolingian Empire (borderline >100M births) controlled Pannonia
    (895, 1000, 'NOT_RELEVANT'),
    (1000, 1526, 'Kingdom of Hungary'),
    # Gap: Ottoman Empire + Habsburg Empire (both >100M births) divided Hungary
    (1699, 1804, 'Habsburg Empire'),
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1920, 'NOT_RELEVANT'),
    (1920, 1944, 'Kingdom of Hungary'),
    # Gap: Nazi Germany + Soviet Union (>100M births) in Hungarian territory
    (1946, 1949, 'Second Hungarian Republic'),
    (1949, 1989, "Hungarian People's Republic"),
    (1989, 2026, 'Hungary'),
]


# =============================================================================
# Combined output
# =============================================================================

POLITY_TIMELINES = {
    'Russia': RUSSIA,
    'Ukraine': UKRAINE,
    'Belarus': BELARUS,
    'Romania': ROMANIA,
    'Hungary': HUNGARY,
}

if __name__ == '__main__':
    for country, timeline in POLITY_TIMELINES.items():
        print(f"\n{'='*60}")
        print(f" {country}")
        print(f"{'='*60}")
        prev_end = None
        for start, end, name in timeline:
            if prev_end is not None and start > prev_end:
                print(f"  [{prev_end:>7} to {start:>7}]  *** GAP ***")
            print(f"  ({start:>7}, {end:>7}, '{name}')")
            prev_end = end
