"""
Polity assignment data for Western Balkans countries:
Croatia, Bosnia and Herzegovina, Albania, North Macedonia, Montenegro

Lifetime births threshold: 100M = avg_population × 0.04 × years_of_existence.

Key polity estimates (OVER = >100M lifetime births):
- Roman Republic/Empire: ~50M avg × 985yr ≈ 1,970M. OVER.
- Byzantine Empire: ~10M avg × 1058yr ≈ 423M. OVER.
- Ottoman Empire: ~15M avg × 623yr ≈ 374M. OVER.
- Habsburg Monarchy / Austrian Empire / Austria-Hungary: ~20M avg × 392yr ≈ 314M. OVER.
- Kingdom of Italy (1861-1946): ~35M avg × 85yr ≈ 119M. OVER.

Key polity estimates (UNDER = <100M lifetime births):
- First Bulgarian Empire: ~2M avg × 337yr ≈ 27M. UNDER.
- Second Bulgarian Empire: ~2M avg × 211yr ≈ 17M. UNDER.
- Kingdom of Hungary (1000-1526): ~3M avg × 526yr ≈ 63M. UNDER.
- Republic of Venice: ~1.5M avg × 1100yr ≈ 66M. UNDER.
- Kingdom of Yugoslavia (1918-1941): ~14M avg × 23yr ≈ 13M. UNDER.
- SFRY (1945-1992): ~19M avg × 47yr ≈ 36M. UNDER.
- FRY (1992-2006): ~10M avg × 14yr ≈ 5.6M. UNDER.
- Nazi Germany (1933-1945): ~70M avg × 12yr ≈ 34M. UNDER.
- Napoleonic French Empire (1804-1815): ~30M avg × 11yr ≈ 13M. UNDER.
- Medieval Serbian states: UNDER.
- Kingdom of Macedon: ~3M avg × 350yr ≈ 42M. UNDER.
"""

BALKAN_ASSIGNMENT = {}

# =============================================================================
# CROATIA
# =============================================================================

BALKAN_ASSIGNMENT['Croatia'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    # GAP -300 to 9: Roman Republic/Empire (>100M) gradually conquered
    # Dalmatian coast (229-168 BCE) but interior Pannonia not subdued until
    # suppression of the Great Illyrian Revolt in 9 AD. Multiple polities
    # coexisted; Rome never controlled 99%+ until 9 AD.
    (9, 395, 'Roman Empire'),
    (395, 476, 'Western Roman Empire'),
    (476, 535, 'NOT_RELEVANT'),
    # Odoacer then Ostrogothic Kingdom controlled all of this territory.
    # Both well under 100M. No polity >100M controlled any part.
    # GAP 535 to 600: Byzantine Empire (>100M) reconquered Dalmatia in
    # Justinian's Gothic War (535), but Lombards invaded Pannonia from 568
    # and Avars/Slavs overran the interior by ~600. Split control.
    (600, 812, 'NOT_RELEVANT'),
    # Slavic/Avar period. Byzantine Empire nominally claimed a few Dalmatian
    # coastal towns (Split, Zadar) but effective control was negligible —
    # those towns had <1% of the total population of modern Croatia's
    # territory. All substantive polities (Avar Khaganate, nascent Croatian
    # tribal units) were well under 100M.
    # GAP 812 to 1000: Byzantine Empire (>100M) retained suzerainty over
    # Dalmatian coastal cities (Split, Zadar, Trogir, islands) — these had
    # ~15-25K people vs ~400-600K total, i.e. ~3-5% of population.
    # Croatian Duchy/Kingdom controlled the interior.
    (1000, 1420, 'NOT_RELEVANT'),
    # Byzantine control of Dalmatian cities faded by ~1000. Croatian Kingdom
    # (925-1102) then Croatian-Hungarian personal union (1102+) controlled
    # nearly all territory. Venice held some coastal towns but was under 100M.
    # Kingdom of Hungary was under 100M. No polity >100M controlled any part.
    # GAP 1420 to 1527: Ottoman Empire (>100M) conquering Croatian borderlands
    # from ~1460s onward. Venice held Dalmatian coast from 1420. Kingdom of
    # Hungary held interior Croatia. No single polity at 99%.
    # GAP 1527 to 1699: Ottoman Empire (>100M) controlled large parts of
    # Slavonia (~30-50% of modern Croatia at the Ottoman peak ~1550-1600).
    # Habsburg Monarchy (>100M) held the rest. Venice held Dalmatian coast.
    # GAP 1699 to 1797: Treaty of Karlowitz (1699) returned Slavonia to
    # Habsburgs, but Venice still held Dalmatia (~15-20% of population).
    # Habsburg Monarchy (>100M) controlled ~80-85% but not 99%+.
    (1797, 1805, 'Habsburg Monarchy'),
    # After Venice fell to Napoleon (1797), Treaty of Campo Formio gave
    # Dalmatia to Austria. Habsburgs controlled 99%+ of modern Croatia.
    # GAP 1805 to 1815: Treaty of Pressburg (1805) gave Dalmatia to France.
    # Illyrian Provinces (1809-1813) included Dalmatia, Istria, parts of
    # Croatia — ~15-20% of modern Croatia's population. Habsburg Monarchy
    # (>100M) controlled the rest but not 99%+.
    (1815, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    # GAP 1918 to 1941: Kingdom of Italy (>100M) held Zadar, Istria
    # (including Pula, Rijeka area), and Dalmatian islands — all part of
    # modern Croatia today, ~5-8% of population. Rest under Kingdom of
    # Yugoslavia (<100M).
    # GAP 1941 to 1945: Kingdom of Italy (>100M) controlled the Dalmatian
    # coast and annexed parts of Croatia. NDH puppet state held the rest.
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),
    (1991, 1998, 'NOT_RELEVANT'),
    # Republic of Serbian Krajina controlled ~5-12% of Croatia's population
    # but no polity >100M controlled any part. FRY supported Krajina but
    # didn't exercise direct sovereignty. All polities <100M.
    (1998, 2026, 'Republic of Croatia'),
    # Full control after peaceful reintegration of Eastern Slavonia (1998).
]


# =============================================================================
# BOSNIA AND HERZEGOVINA
# =============================================================================

BALKAN_ASSIGNMENT['Bosnia and Herzegovina'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    # GAP -300 to 9: Roman Republic/Empire (>100M) gradually conquering.
    # Dalmatian coast from 168 BCE, but interior Bosnia (Daesitiates) not
    # subdued until Great Illyrian Revolt suppressed in 9 AD.
    (9, 395, 'Roman Empire'),
    (395, 476, 'Western Roman Empire'),
    (476, 535, 'NOT_RELEVANT'),
    # Ostrogothic Kingdom controlled territory. All polities <100M.
    # GAP 535 to 600: Byzantine Empire (>100M) reconquered this territory
    # in 535-537 but Avar/Slavic invasions disrupted control from ~580s.
    (600, 1463, 'NOT_RELEVANT'),
    # Slavic settlement, then medieval Banate/Kingdom of Bosnia (1154-1463).
    # Hungary claimed suzerainty intermittently but effective control was
    # limited. Serbia held parts of eastern Bosnia at times. All polities
    # (Hungary ~63M, Bosnia ~5M, Serbia ~20M, Bulgaria ~27M) were under
    # 100M. Byzantine Empire lost effective control by ~600.
    # GAP 1463 to 1482: Ottoman Empire (>100M) conquered most of Bosnia
    # (fall of the kingdom, 1463) but Herzegovina not fully subdued until
    # ~1482 (last Herzegovinian fortresses fell).
    (1482, 1878, 'Ottoman Empire'),
    (1878, 1918, 'Austria-Hungary'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    # GAP 1941 to 1945: Kingdom of Italy (>100M) exercised authority over
    # a formal occupation zone covering most of Herzegovina and parts of
    # central Bosnia (~30-40% of territory). NDH puppet state held the rest.
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 1995, 'NOT_RELEVANT'),
    # Bosnian War. Three warring factions. FR Yugoslavia and Croatia
    # supported factions but didn't exercise direct sovereignty. No polity
    # >100M controlled any part.
    (1995, 2026, 'Bosnia and Herzegovina'),
]


# =============================================================================
# ALBANIA
# =============================================================================

BALKAN_ASSIGNMENT['Albania'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -229, 'NOT_RELEVANT'),
    # Illyrian tribal kingdoms (Taulantii, Enchele) and Greek colonies
    # (Epidamnos, Apollonia). All polities <100M. Kingdom of Macedon nearby
    # but didn't permanently control all Albanian territory.
    # GAP -229 to -168: Roman Republic (>100M) established coastal
    # protectorates after First Illyrian War (229 BCE). Controlled Illyrian
    # coast but not all of interior Albania.
    (-168, 395, 'Roman Empire'),
    (395, 600, 'Byzantine Empire'),
    # Albania was core eastern Roman/Byzantine Balkan territory.
    # GAP 600 to 850: Byzantine Empire (>100M) held coastal Albania
    # (Dyrrachium was a major Byzantine fortress) but Slavic tribes
    # controlled much of the interior.
    # GAP 850 to 1018: Byzantine Empire (>100M) contested this territory
    # with the First Bulgarian Empire. Under Tsar Samuel (~976-1014),
    # Bulgaria controlled much of Albania's interior. Neither controlled 99%+.
    (1018, 1204, 'Byzantine Empire'),
    # After Basil II destroyed the Bulgarian Empire (1018), Byzantines
    # controlled all of Albania.
    (1204, 1385, 'NOT_RELEVANT'),
    # After Fourth Crusade (1204), Albania fragmented: Despotate of Epirus,
    # Angevin Kingdom of Albania, various Albanian lords. All polities <100M.
    # Byzantine Empire lost this territory in 1204 and the restored empire
    # never effectively reclaimed Albanian territory.
    # GAP 1385 to 1501: Ottoman Empire (>100M) gradually conquering.
    # Ioannina 1385, much of Albania 1430s, Skanderbeg resistance 1443-1468,
    # last Venetian/Albanian holdouts fell by ~1501.
    (1501, 1912, 'Ottoman Empire'),
    (1912, 1914, 'Albania'),
    # Declared independence Nov 1912, recognized 1913. Principality covered
    # essentially all of modern Albania.
    # GAP 1914 to 1920: Kingdom of Italy (>100M) occupied Vlorë and
    # surroundings. Greece occupied southern Albania (Northern Epirus).
    # Serbia/Montenegro occupied the north. WWI chaos fragmented the country.
    (1920, 1939, 'Albania'),
    # Various regimes (republic 1925, kingdom 1928) but same Albanian state.
    (1939, 1943, 'Kingdom of Italy'),
    # Italy formally annexed Albania in personal union (April 1939).
    # Italian forces controlled 99%+ of territory.
    (1943, 1946, 'NOT_RELEVANT'),
    # After Italian armistice (Sept 1943), German occupation. Nazi Germany
    # (<100M lifetime births) held the territory. Albanian partisans
    # liberated the country by Nov 1944. Transitional period to 1946.
    # No polity >100M controlled any part.
    (1946, 1992, "People's Socialist Republic of Albania"),
    # (Called People's Republic 1946-1976, then People's Socialist Republic
    # 1976-1992; same regime throughout.)
    (1992, 2026, 'Republic of Albania'),
]


# =============================================================================
# NORTH MACEDONIA
# =============================================================================

BALKAN_ASSIGNMENT['North Macedonia'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -340, 'NOT_RELEVANT'),
    # Paeonian kingdom and other tribal polities in this territory.
    # All polities <100M. Kingdom of Macedon hadn't yet conquered Paeonia.
    (-340, -168, 'Kingdom of Macedon'),
    # Philip II conquered Paeonia ~340 BCE. Antigonid dynasty continued
    # controlling this territory until Roman conquest.
    (-168, 395, 'Roman Empire'),
    (395, 600, 'Byzantine Empire'),
    # Core Byzantine Balkan territory (province of Macedonia).
    # GAP 600 to 850: Byzantine Empire (>100M) held some fortified positions
    # (Thessaloniki nearby, cities along Via Egnatia) but Slavic tribes
    # (Berziti, Sagudati, Drougoubitai) controlled much of the interior
    # of modern North Macedonia.
    (850, 1018, 'First Bulgarian Empire'),
    # Under Boris I, Simeon I, and especially Samuel (capital at Ohrid),
    # Bulgaria controlled nearly all of modern North Macedonia.
    (1018, 1185, 'Byzantine Empire'),
    # After Basil II's conquest of Bulgaria (1018).
    # GAP 1185 to 1282: Second Bulgarian Empire (revived 1185) and Byzantine
    # Empire (>100M) competed for this territory. Serbians expanding south.
    # No single polity controlled 99%+ of modern North Macedonia.
    (1282, 1346, 'Kingdom of Serbia'),
    # Stefan Milutin took Skopje in 1282; Serbia controlled all of modern
    # North Macedonia through the Nemanjić period.
    (1346, 1371, 'Serbian Empire'),
    # Stefan Dušan crowned emperor 1346. Controlled all of this territory.
    # GAP 1371 to 1395: Ottoman Empire (>100M) expanding. After Battle of
    # Maritsa (1371), Serbian Empire fragmented. Ottoman vassals held parts.
    # Ottomans took Skopje 1392. No single polity controlled 99%+.
    (1395, 1912, 'Ottoman Empire'),
    # All of modern North Macedonia under Ottoman control by ~1395.
    (1913, 1915, 'Kingdom of Serbia'),
    # Serbia conquered this territory in First Balkan War (1912-13). Treaty
    # of Bucharest (1913) confirmed Serbian sovereignty.
    (1915, 1918, 'NOT_RELEVANT'),
    # Bulgarian occupation during WWI. Kingdom of Bulgaria (<100M) controlled
    # nearly all territory. No polity >100M controlled any part.
    (1918, 1941, 'Kingdom of Yugoslavia'),
    # GAP 1941 to 1944: Kingdom of Italy (>100M) effectively controlled
    # western North Macedonia (~15-20% of population around Tetovo, Gostivar,
    # Debar, Struga) through its Albanian puppet state. Bulgaria occupied
    # the rest.
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),
    (1991, 2026, 'Republic of North Macedonia'),
    # (Called Republic of Macedonia until 2019 Prespa Agreement.)
]


# =============================================================================
# MONTENEGRO
# =============================================================================

BALKAN_ASSIGNMENT['Montenegro'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, -229, 'NOT_RELEVANT'),
    # Illyrian tribal polities (Ardiaei, Docleati). All <100M.
    # GAP -229 to -168: Roman Republic (>100M) established coastal
    # protectorates after First Illyrian War (229 BCE) but didn't control
    # the mountainous interior.
    (-168, 395, 'Roman Empire'),
    # Province of Dalmatia, later Praevalitana.
    (395, 600, 'Byzantine Empire'),
    # Praevalitana was transferred to the Eastern Empire (Prefecture of
    # Illyricum moved to Constantinople in 395). Core Byzantine territory.
    # GAP 600 to 1186: Byzantine Empire (>100M) had intermittent control
    # and suzerainty over the Slavic principality of Duklja/Zeta. Effective
    # control fluctuated — Duklja was semi-independent with periods of
    # rebellion (Vojislav ~1040, Mihailo, Bodin). Byzantines never fully
    # lost their claim but also never consistently controlled 99%+.
    (1186, 1217, 'Grand Principality of Serbia'),
    # Stefan Nemanja annexed Zeta ~1186. Under Nemanjić dynasty.
    (1217, 1346, 'Kingdom of Serbia'),
    (1346, 1371, 'Serbian Empire'),
    # GAP 1371 to 1918: After Serbian Empire fragmented (1371), Montenegro
    # was ruled by the Balšić (1371-1421) then Crnojević (1451-1499) families.
    # Ottoman Empire (>100M) conquered lowlands/eastern parts from ~1390s.
    # Venice controlled the Bay of Kotor coast from 1420 to 1797.
    # Austria/Austria-Hungary (>100M) held Bay of Kotor from 1814 to 1918.
    # Montenegrin highland core maintained de facto autonomy/independence
    # (formally recognized at Congress of Berlin 1878).
    # Even after 1878, Austria-Hungary (>100M) retained Bay of Kotor
    # (~12-15% of modern Montenegro's population), so independent Montenegro
    # never controlled 99%+ of the modern state's territory.
    (1918, 1941, 'Kingdom of Yugoslavia'),
    # After WWI, both Montenegro proper and Bay of Kotor joined Yugoslavia.
    (1941, 1943, 'Kingdom of Italy'),
    # Italy occupied Montenegro directly (Italian Governorate of Montenegro).
    # Controlled 99%+ of territory at least initially despite partisan
    # resistance.
    (1943, 1945, 'NOT_RELEVANT'),
    # After Italian armistice (Sept 1943), German occupation. Germany (<100M)
    # held the territory until partisan liberation (1944). No polity >100M.
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 2006, 'Federal Republic of Yugoslavia'),
    # Renamed State Union of Serbia and Montenegro in 2003; same entity.
    (2006, 2026, 'Montenegro'),
]
