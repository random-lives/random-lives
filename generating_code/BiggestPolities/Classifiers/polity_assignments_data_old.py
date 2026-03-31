"""
Polity assignment data: maps (modern_country, year) → polity_name.

Design principles:
- Only assign when 99%+ of the modern country's population was under that polity.
- Use a SPLITTING view: distinguish regimes (e.g. French Third Republic vs Second Empire).
- Gaps = "indeterminate" (multiple polities, civil war, contested).
- Negative years = BCE. end_year is EXCLUSIVE.
- Colonial territories get their own names (e.g. 'British India', not 'United Kingdom').

Four possible return values from assign_polity():
- A polity name string
- 'indeterminate' — known polities existed but can't cleanly assign
- 'no_known_polities' — predates any reliably known polities in the region
- 'not_relevant' — polities existed but all were too small to plausibly be top-100
"""

# NOT_RELEVANT entries are inline in ASSIGNMENT as ('NOT_RELEVANT') polity name.




# The main assignment table.
# Each entry: (start_year, end_year_exclusive, polity_name)
ASSIGNMENT = {}

# =============================================================================
# EAST ASIA
# =============================================================================

ASSIGNMENT['China'] = [
    (-200000, -1600, 'NO_KNOWN_POLITIES'),
    # Pre-Qing Chinese dynasties (Han, Tang, Ming, etc.) controlled "China proper"
    # but NOT Manchuria, Inner Mongolia, Xinjiang, or Tibet — regions that together
    # had 3-8% of the population within modern China's borders. Fails 99% rule.
    # These dynasties need the sampling approach instead.
    (1279, 1368, 'Yuan Dynasty'),  # Mongols controlled ALL of modern China + much more
    (1759, 1912, 'Qing Dynasty'),  # Qing controlled China proper from 1644, but Tibet ~1720,
    # Xinjiang 1759. Taiwan is a separate entry. Start from 1759 when all of modern China
    # (excluding Taiwan/HK which have separate entries) was under Qing control.
    # ROC (1912-1949): warlords, Japanese occupation. Skip.
    (1951, 2026, "People's Republic of China"),  # Tibet incorporated 1950-51
]

ASSIGNMENT['Taiwan'] = [
    (-200000, 1624, 'NO_KNOWN_POLITIES'),
    (1683, 1895, 'Qing Dynasty'),
    (1895, 1945, 'Empire of Japan'),
    (1945, 2026, 'Republic of China'),
]

ASSIGNMENT['Hong Kong'] = [
    (-200000, -221, 'NO_KNOWN_POLITIES'),
    (1650, 1842, 'Qing Dynasty'),
    (1898, 1941, 'British Hong Kong'),  # Full territory (HK Island 1842, Kowloon 1860, New Territories 1898)
    # 1941-1945: Japanese occupation
    (1945, 1997, 'British Hong Kong'),
    (1997, 2026, "People's Republic of China"),
]

ASSIGNMENT['Mongolia'] = [
    (-200000, -209, 'NO_KNOWN_POLITIES'),
    (1206, 1368, 'Mongol Empire'),
    (1691, 1911, 'Qing Dynasty'),
    (1911, 1919, 'Bogd Khanate of Mongolia'),
    (1924, 1992, "Mongolian People's Republic"),  # MPR proclaimed 1924 after Bogd Khan's death
    (1992, 2026, 'Mongolia'),
]

ASSIGNMENT['Japan'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    (710, 794, 'Nara Period'),
    (794, 1185, 'Heian Period'),
    (1185, 1333, 'Kamakura Shogunate'),
    (1392, 1467, 'Muromachi Shogunate'),
    # Sengoku period 1467-1590: fragmented
    (1590, 1600, 'Toyotomi Regime'),
    (1603, 1868, 'Tokugawa Shogunate'),
    (1868, 1945, 'Empire of Japan'),
    (1945, 2026, 'Japan'),  # Okinawa under US until 1972 but <1% of pop; sovereignty restored 1952
]

ASSIGNMENT['South Korea'] = [
    (-200000, -57, 'NO_KNOWN_POLITIES'),
    (668, 935, 'Unified Silla'),
    (936, 1392, 'Goryeo Dynasty'),
    (1392, 1897, 'Joseon Dynasty'),
    (1897, 1910, 'Korean Empire'),
    (1910, 1945, 'Empire of Japan'),
    (1948, 2026, 'Republic of Korea'),
]

ASSIGNMENT['North Korea'] = [
    (-200000, -37, 'NO_KNOWN_POLITIES'),
    (936, 1392, 'Goryeo Dynasty'),
    (1392, 1897, 'Joseon Dynasty'),
    (1897, 1910, 'Korean Empire'),
    (1910, 1945, 'Empire of Japan'),
    (1948, 2026, "Democratic People's Republic of Korea"),
]

# =============================================================================
# SOUTH ASIA
# =============================================================================

ASSIGNMENT['India'] = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    # Maurya: didn't control far south (5-10% of population). Skip.
    (1858, 1947, 'British India'),
    (1947, 2026, 'Republic of India'),
]

ASSIGNMENT['Pakistan'] = [
    (-200000, -2000, 'NO_KNOWN_POLITIES'),
    (-2000, -550, 'NOT_RELEVANT'),
    (1858, 1947, 'British India'),
    (1947, 2026, 'Pakistan'),
]

ASSIGNMENT['Bangladesh'] = [
    (-200000, -350, 'NO_KNOWN_POLITIES'),
    (1576, 1717, 'Mughal Empire'),
    (1717, 1757, 'Nawabi of Bengal'),
    (1757, 1858, 'East India Company'),
    (1858, 1947, 'British India'),
    (1947, 1971, 'Pakistan'),
    (1971, 2026, 'Bangladesh'),
]

ASSIGNMENT['Sri Lanka'] = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (-200, 985, 'NOT_RELEVANT'),
    (1070, 1815, 'NOT_RELEVANT'),
    (1815, 1948, 'British Ceylon'),
    (1948, 2026, 'Sri Lanka'),
]

ASSIGNMENT['Nepal'] = [
    (-200000, -250, 'NO_KNOWN_POLITIES'),
    (1816, 2008, 'Kingdom of Nepal'),
    (2008, 2026, 'Federal Democratic Republic of Nepal'),
]

ASSIGNMENT['Myanmar'] = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (-500, 1287, 'NOT_RELEVANT'),
    # Gap 1287-1555: Yuan Dynasty (>100M) conquered Upper Burma; Ming Dynasty (>100M) intervened in Shan states.
    (1555, 1599, 'Toungoo Empire'),
    (1599, 1752, 'NOT_RELEVANT'),
    (1752, 1824, 'Konbaung Dynasty'),
    # Gap 1824-1886: British Empire (>100M) took Arakan/Tenasserim (1826), Lower Burma (1852).
    (1886, 1942, 'British Empire'),
    # Gap 1942-1945: Empire of Japan (>100M) vs British Empire (>100M).
    (1945, 1948, 'British Empire'),
    (1948, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Afghanistan'] = [
    (-200000, -2000, 'NO_KNOWN_POLITIES'),
    (-2000, -550, 'NOT_RELEVANT'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -312, 'NOT_RELEVANT'),
    (-312, -305, 'Seleucid Empire'),
    # Gap -305 to 1186: Maurya/Seleucid/Parthian/Kushan/Sasanian/Umayyad/Abbasid each >100M,
    # divided Afghanistan between eastern and western powers.
    (1186, 1220, 'NOT_RELEVANT'),
    # Gap 1220-1370: Mongol Empire (>100M), split between Chagatai Khanate and Ilkhanate.
    (1370, 1405, 'Timurid Empire'),
    # Gap 1405-1507: Timurid successor branches (>100M overall).
    (1507, 1510, 'NOT_RELEVANT'),
    # Gap 1510-1747: Safavid Empire (borderline ~100M) in west; Mughal Empire (>100M) in east.
    (1747, 1896, 'NOT_RELEVANT'),
    (1896, 1973, 'Kingdom of Afghanistan'),
    (1973, 1978, 'Republic of Afghanistan'),
    # Gap 1978-1989: Soviet Union (>100M) invaded/occupied.
    (1989, 2001, 'NOT_RELEVANT'),
    # Gap 2001-2021: United States (>100M) military presence.
    (2021, 2026, 'Islamic Emirate of Afghanistan'),
]

# =============================================================================
# SOUTHEAST ASIA
# =============================================================================

ASSIGNMENT['Indonesia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (600, 1600, 'NOT_RELEVANT'),
    (1914, 1942, 'Dutch East Indies'),
    (1949, 2026, 'Republic of Indonesia'),
]

ASSIGNMENT['Philippines'] = [
    (-200000, 1565, 'NO_KNOWN_POLITIES'),
    (1913, 1941, 'American Philippines'),
    (1946, 2026, 'Republic of the Philippines'),
]

ASSIGNMENT['Vietnam'] = [
    (-200000, -257, 'NO_KNOWN_POLITIES'),
    (1802, 1858, 'Nguyen Dynasty'),
    (1885, 1941, 'French Indochina'),
    (1976, 2026, 'Socialist Republic of Vietnam'),
]

ASSIGNMENT['Thailand'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    (1200, 1909, 'NOT_RELEVANT'),
    (1909, 1932, 'Kingdom of Siam'),
    (1932, 2026, 'Kingdom of Thailand'),
]

ASSIGNMENT['Malaysia'] = [
    (-200000, 200, 'NO_KNOWN_POLITIES'),
    (200, 1511, 'NOT_RELEVANT'),
    # Gap 1511-1914: Portuguese (>100M from 1511), Dutch (>100M from 1641), British (>100M from 1786)
    # each controlled parts (Malacca, Straits Settlements) but not 99%.
    (1914, 1942, 'British Empire'),
    # Gap 1942-1945: Empire of Japan (>100M) vs British Empire (>100M).
    (1945, 1957, 'British Empire'),
    # Gap 1957-1963: Federation of Malaya independent; British Empire (>100M) still held Sabah/Sarawak.
    (1963, 2026, 'Malaysia'),
]

ASSIGNMENT['Cambodia'] = [
    (-200000, 550, 'NO_KNOWN_POLITIES'),
    (802, 1220, 'Khmer Empire'),
    (1863, 1941, 'French Cambodia'),
    (1953, 1970, 'Kingdom of Cambodia'),
    (1975, 1979, 'Democratic Kampuchea'),
    (1998, 2026, 'Kingdom of Cambodia'),
]

ASSIGNMENT['Laos'] = [
    (-200000, 1354, 'NO_KNOWN_POLITIES'),
    (1354, 1707, 'Lan Xang'),
    (1707, 1893, 'NOT_RELEVANT'),
    (1893, 1941, 'French Third Republic'),
    # Gap 1941-1946: Empire of Japan (>100M) occupied French Indochina.
    (1946, 1953, 'French Fourth Republic'),
    (1953, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Singapore'] = [
    (-200000, 1299, 'NO_KNOWN_POLITIES'),
    (1299, 1819, 'NOT_RELEVANT'),
    (1819, 1942, 'British Empire'),
    (1942, 1945, 'Empire of Japan'),
    (1945, 1963, 'British Empire'),
    (1963, 1965, 'NOT_RELEVANT'),
    (1965, 2026, 'Republic of Singapore'),
]

# =============================================================================
# RUSSIA / USSR / POST-SOVIET
# =============================================================================

ASSIGNMENT['Russia'] = [
    (-200000, 862, 'NO_KNOWN_POLITIES'),
    (1547, 1721, 'Tsardom of Russia'),  # N. Caucasus unconquered but <1% of pop
    (1721, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Russian Federation'),
]

ASSIGNMENT['Ukraine'] = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (-500, 880, 'NOT_RELEVANT'),
    (1945, 1991, 'Soviet Union'),
    (1991, 2014, 'Ukraine'),
]

ASSIGNMENT['Belarus'] = [
    (-200000, 862, 'NO_KNOWN_POLITIES'),
    (1350, 1569, 'Grand Duchy of Lithuania'),
    (1569, 1795, 'Polish-Lithuanian Commonwealth'),
    (1795, 1917, 'Russian Empire'),
    (1945, 1991, 'Soviet Union'),
    (1991, 2026, 'Belarus'),
]

ASSIGNMENT['Kazakhstan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    # -550 to 1220: Saka confederations, Kangju, Turkic Khaganate, Kimek, Kipchak —
    # all nomadic states well under 100M lifetime births. Tang Dynasty (>100M) had a
    # garrison at Talas but this was a single outpost, not meaningful territorial control.
    (-550, 1220, 'NOT_RELEVANT'),
    # Mongol conquest of Central Asia 1219-1221; entire Kazakh steppe under Mongol control.
    (1220, 1260, 'Mongol Empire'),
    # 1260-1731: Golden Horde (~63M births), Chagatai Khanate (~40M), White Horde,
    # Kazakh Khanate (~50M births) — all under 100M. Timurid Empire (borderline ~110M)
    # controlled only the far southern fringe (Transoxiana), not Kazakh steppe proper.
    (1260, 1731, 'NOT_RELEVANT'),
    # 1731-1876: Russian Empire (>100M) gained suzerainty over Junior Zhuz (1731),
    # Middle Zhuz (1740s), Senior Zhuz (1840s-60s). Qing Dynasty (>100M) controlled
    # eastern Kazakhstan (Semirechye/Zhetysu) ~1758-1864 via conquest of Dzungars.
    # Neither controlled 99%+ until Russia completed annexation ~1876.
    # GAP JUSTIFICATION: Russian Empire (>100M) and Qing Dynasty (>100M) each
    # controlled parts of Kazakhstan.
    (1876, 1917, 'Russian Empire'),
    # 1917-1922: Russian Civil War; Bolsheviks gradually establish control.
    # GAP JUSTIFICATION: Russian state (>100M) existed but authority contested.
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Kazakhstan'),
]

ASSIGNMENT['Uzbekistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    # -550 to -530: Local Sogdian/Bactrian polities, all small. No >100M polity present.
    (-550, -530, 'NOT_RELEVANT'),
    # Cyrus and Darius conquered Transoxiana/Sogdiana by ~530-520 BCE.
    (-530, -330, 'Achaemenid Empire'),
    # Alexander conquered the region; Seleucids inherited it. >100M births.
    (-330, -250, 'Seleucid Empire'),
    # Greco-Bactrian Kingdom broke away ~250 BCE, controlled all of modern Uzbekistan.
    (-250, -150, 'Greco-Bactrian Kingdom'),
    # -150 to 50: Yuezhi/Saka migrations, transitional nomadic period. No >100M polity
    # controlled Uzbek territory.
    (-150, 50, 'NOT_RELEVANT'),
    # Kushan Empire controlled Bactria/Sogdiana and northern India (~50-230 CE).
    (50, 230, 'Kushan Empire'),
    # 230-650: Kushano-Sasanians, Kidarites, Hephthalites, Western Turkic Khaganate.
    # Sasanian Empire (>100M births) controlled southern Uzbekistan (Tokharistan)
    # intermittently while northern Uzbekistan was under Hephthalites then Turks.
    # GAP JUSTIFICATION: Sasanian Empire (>100M) controlled southern parts.
    # 650-710: Arab conquest in progress. Umayyad Caliphate (>100M) expanding into
    # Transoxiana while Turkic/Sogdian rulers held parts.
    # GAP JUSTIFICATION: Umayyad Caliphate (>100M) controlled some while local rulers
    # held others during gradual conquest.
    # Qutayba ibn Muslim completed conquest of Transoxiana by ~710-715.
    (710, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    # Samanid Empire ~819-999, effectively autonomous from ~900, controlled Transoxiana.
    # ~4-5M people, ~100 yrs independent = ~18M births. Under 100M but controlled 99%+.
    (900, 999, 'Samanid Empire'),
    # 999-1220: Karakhanids, then Kara-Khitan, then Khwarezmian Empire controlled
    # Transoxiana. Karakhanids ~17M births, Kara-Khitan ~11M, Khwarezmians ~4M — all
    # under 100M. Seljuk Empire was to the south/west and did not control Transoxiana.
    (999, 1220, 'NOT_RELEVANT'),
    # Mongol conquest of Transoxiana 1219-1221.
    (1220, 1260, 'Mongol Empire'),
    # 1260-1370: Chagatai Khanate. ~5M × ~110 yrs = 22M births. Under 100M.
    (1260, 1370, 'NOT_RELEVANT'),
    # Timur's empire centered on Samarkand. Controlled 99%+ of Uzbekistan.
    (1370, 1507, 'Timurid Empire'),
    # 1507-1868: Shaybanid then Janid/Astrakhanid Khanate of Bukhara, Khanate of Khiva,
    # Khanate of Kokand — multiple small khanates, none >100M. Safavid Empire (borderline
    # ~84M births) to the south did not control Uzbek territory. No >100M polity present.
    (1507, 1868, 'NOT_RELEVANT'),
    # 1868-1876: Russia conquered Bukhara (1868 protectorate), Khiva (1873 protectorate),
    # Kokand (1876 annexed). Russian Empire (>100M) controlled some directly while
    # protectorates retained partial autonomy. Full control by 1876.
    # GAP JUSTIFICATION: Russian Empire (>100M) controlled annexed territory while
    # Bukhara/Khiva protectorates had partial autonomy.
    (1876, 1917, 'Russian Empire'),
    # 1917-1922: Civil war, Basmachi resistance.
    # GAP JUSTIFICATION: Russian state (>100M) existed but authority contested.
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Uzbekistan'),
]

ASSIGNMENT['Kyrgyzstan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (1876, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Kyrgyzstan'),
]

ASSIGNMENT['Tajikistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-530, -330, 'Achaemenid Empire'),
    (1929, 1991, 'Soviet Union'),
    (1991, 2026, 'Tajikistan'),
]

ASSIGNMENT['Turkmenistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-530, -330, 'Achaemenid Empire'),
    (1884, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Turkmenistan'),
]

ASSIGNMENT['Georgia'] = [
    (-200000, -600, 'NO_KNOWN_POLITIES'),
    # -600 to -550: Early Colchian kingdom and Kingdom of Iberia forming. Small local
    # polities, no >100M polity present.
    (-600, -550, 'NOT_RELEVANT'),
    # -550 to -330: Achaemenid Empire (>100M) controlled eastern Georgia (Iberia as
    # satrapy/vassal) but western Georgia (Colchis) remained independent.
    # GAP JUSTIFICATION: Achaemenid Empire (>100M) controlled eastern Georgia.
    # -330 to -65: Hellenistic period. Local kingdoms (Iberia, Colchis). Seleucid Empire
    # (>100M) had nominal influence over parts of the southern Caucasus.
    # GAP JUSTIFICATION: Seleucid Empire (>100M) had influence over parts.
    # -65 to 654: Roman/Byzantine Empire (>100M) controlled western Georgia (Colchis/
    # Lazica), while Parthian Empire then Sasanian Empire (both >100M) controlled
    # eastern Georgia (Iberia/Kartli). Territory consistently split between two empires.
    # GAP JUSTIFICATION: Roman/Byzantine Empire and Parthian/Sasanian Empire (all >100M)
    # each controlled roughly half of modern Georgia.
    # 654-1008: Arab caliphates (>100M) controlled Tbilisi and central Georgia (Emirate
    # of Tbilisi), while western Georgian principalities (Abkhazia, Lazica) were under
    # Byzantine (>100M) influence. Georgian principalities gradually unified.
    # GAP JUSTIFICATION: Umayyad/Abbasid Caliphate (>100M) and Byzantine Empire (>100M)
    # each controlled parts of Georgia.
    # Unified Kingdom of Georgia under Bagrat III from 1008.
    (1008, 1236, 'Kingdom of Georgia'),
    # 1236-1260: Mongol Empire conquered Georgia. >100M births. Controlled 99%+.
    (1236, 1260, 'Mongol Empire'),
    # 1260-1335: Ilkhanate. ~79 yrs × ~15M = ~47M births. Under 100M but controlled 99%+
    # of Georgia as a vassal state.
    (1260, 1335, 'Ilkhanate'),
    # 1335-1386: Post-Ilkhanate fragmentation. Georgian kingdoms under various small
    # Turkic successor states. All under 100M births.
    (1335, 1386, 'NOT_RELEVANT'),
    # 1386-1405: Timurid Empire invaded Georgia repeatedly (1386, 1394, 1399-1403).
    # Timurids borderline >100M births (~20M × 0.04 × 137 = ~110M).
    # GAP JUSTIFICATION: Timurid Empire (borderline >100M) controlled/devastated Georgia.
    # 1405-1510: Georgian kingdoms (Kartli, Kakheti, Imereti split ~1490). Small local
    # polities. No >100M polity controlled Georgian territory.
    (1405, 1510, 'NOT_RELEVANT'),
    # 1510-1878: Ottoman Empire (>100M) controlled western Georgia (Adjara, Samtskhe,
    # parts of Imereti). Safavid Empire then successor Persian states controlled eastern
    # Georgia (Kartli, Kakheti). Russian Empire (>100M from 1721) entered from 1783
    # (Treaty of Georgievsk) and progressively annexed: eastern Georgia 1801, Imereti 1810,
    # Guria/Mingrelia by 1867, Adjara from Ottomans 1878. No single polity controlled 99%+
    # until 1878.
    # GAP JUSTIFICATION: Ottoman Empire (>100M) controlled western Georgian territories
    # throughout; Russian Empire (>100M) controlled eastern parts from 1801.
    (1878, 1917, 'Russian Empire'),
    # 1917-1918: Revolution. Transcaucasian Democratic Federative Republic (brief).
    # 1918-1921: Democratic Republic of Georgia. ~2.5M people. Under 100M births.
    (1918, 1921, 'NOT_RELEVANT'),
    (1922, 1991, 'Soviet Union'),
    # Post-1993: Abkhazia and South Ossetia (combined ~8% of population in claimed
    # territory) are de facto outside Georgian control, backed by Russia (>100M).
    # GAP JUSTIFICATION: Russian Federation (>100M) controls breakaway regions with
    # >1% of population within Georgia's internationally recognized borders.
    (1991, 1993, 'Georgia'),
]

ASSIGNMENT['Armenia'] = [
    (-200000, -860, 'NO_KNOWN_POLITIES'),
    # Kingdom of Urartu: major centralized state controlling all of modern Armenia + more.
    # ~270 yrs, ~1-2M people = ~15M births. Under 100M but controlled 99%+.
    (-860, -590, 'Kingdom of Urartu'),
    # -590 to -550: Median Empire briefly, transitional. Media under 100M births.
    # No >100M polity present.
    (-590, -550, 'NOT_RELEVANT'),
    # Achaemenid Empire: Armenia was a satrapy. >100M births. Controlled 99%+.
    (-550, -330, 'Achaemenid Empire'),
    # -330 to -190: Macedonian conquest, then Orontid dynasty under Seleucid suzerainty.
    # Seleucid Empire (>100M) was the nominal sovereign, though Orontids had autonomy.
    # GAP JUSTIFICATION: Seleucid Empire (>100M) was sovereign over Armenia through
    # Orontid vassal dynasty, but degree of control varied.
    # Artaxiad dynasty broke away ~190 BCE.
    (-190, -1, 'Kingdom of Armenia'),
    # 1 to 63: Roman-Parthian contest over Armenia. Kings installed/deposed by both sides.
    # Both Roman Empire (>100M) and Parthian Empire (>100M) controlled Armenia at times.
    # GAP JUSTIFICATION: Roman Empire and Parthian Empire (both >100M) competed for
    # control; neither held 99%+ consistently.
    # 63 CE: Arsacid dynasty established by compromise between Rome and Parthia.
    # 387: Armenia partitioned — eastern Armenia (= modern Armenia) became a Sasanian
    # vassal, western Armenia went to Rome. The Arsacid dynasty continued in the east
    # until 428 as Sasanian clients.
    (63, 428, 'Kingdom of Armenia'),
    # 428: Sasanians abolished the Armenian Arsacid monarchy. Eastern Armenia directly
    # ruled as a Sasanian marzbanate until the Arab conquest.
    # Sasanian Empire (>100M) controlled 99%+ of modern Armenia's territory.
    (428, 654, 'Sasanian Empire'),
    (654, 750, 'Umayyad Caliphate'),
    (750, 885, 'Abbasid Caliphate'),
    # 885-1045: Bagratid Kingdom of Armenia + other Armenian principalities (Syunik,
    # Vaspurakan). Modern Armenia is small enough that the Bagratids controlled most of it,
    # but Syunik principality covered modern Armenia's south. Multiple small Armenian
    # polities, none >100M. No >100M external polity present.
    (885, 1045, 'NOT_RELEVANT'),
    # 1045-1064: Byzantine Empire (>100M) conquered Bagratid Armenia. Controlled 99%+.
    (1045, 1064, 'Byzantine Empire'),
    # 1064-1236: Seljuk Empire conquered Armenia (Battle of Manzikert 1071 nearby).
    # Seljuks borderline >100M (~157 yrs × ~18M = ~113M). Post-Seljuk: Zakarid princes
    # ruled under Georgian suzerainty in northern Armenia, while Seljuk successor states
    # (Eldiguzids, etc.) held southern parts. Kingdom of Georgia (>100M? No, ~25M births)
    # had suzerainty over parts via Zakarids.
    # GAP JUSTIFICATION: Seljuk Empire (borderline >100M) controlled Armenian territory
    # after 1064; later Seljuk successor states competed with Georgian-backed Zakarids.
    # 1236-1260: Mongol Empire conquered the region. >100M births. Controlled 99%+.
    (1236, 1260, 'Mongol Empire'),
    # 1260-1335: Ilkhanate. Under 100M births but controlled 99%+ of modern Armenia.
    (1260, 1335, 'Ilkhanate'),
    # 1335-1501: Post-Ilkhanate. Jalairids, Qara Qoyunlu, Aq Qoyunlu controlled Armenia
    # successively. All under 100M births. Timurid invasion 1386-1403 (borderline >100M).
    # GAP JUSTIFICATION for 1386-1405: Timurid Empire (borderline >100M) devastated Armenia.
    (1335, 1386, 'NOT_RELEVANT'),
    (1405, 1501, 'NOT_RELEVANT'),
    # 1501-1722: Safavid Empire controlled eastern Armenia (= modern Armenia).
    # Safavids: ~235 yrs × ~9M = ~84M births — under 100M but controlled 99%+ of modern
    # Armenia. Ottoman Empire (>100M) controlled western Armenia (modern eastern Turkey)
    # but NOT modern Armenia's territory, which fell in the Persian sphere.
    (1501, 1722, 'Safavid Empire'),
    # 1722-1735: Safavid collapse. Ottoman Empire (>100M) briefly occupied eastern Armenia
    # (1723-1735). Then Nader Shah reconquered it.
    # GAP JUSTIFICATION: Ottoman Empire (>100M) controlled Armenian territory during this
    # period of Persian collapse.
    # 1735-1828: Afsharid dynasty, then Qajar Iran. Khanate of Erivan under Persian
    # suzerainty. Qajars: ~136 yrs × ~10M = ~54M births. Under 100M. No >100M polity
    # controlled modern Armenia until Russian conquest.
    (1735, 1828, 'NOT_RELEVANT'),
    # Treaty of Turkmenchay (1828): Russia gained the Erivan and Nakhchivan khanates.
    # Modern Armenia corresponds to the Erivan khanate area.
    (1828, 1917, 'Russian Empire'),
    # 1917-1918: Revolution. Transcaucasian period.
    # 1918-1920: First Republic of Armenia. Small, under 100M.
    # 1920-1922: Soviet conquest, Armenian SSR established.
    # All polities in this period under 100M births except Russian state (>100M) but it
    # didn't control 99%+ of Armenia during the civil war/independence period.
    # GAP JUSTIFICATION: Russian state / RSFSR (>100M) contested control during 1917-1922.
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Armenia'),
]

ASSIGNMENT['Azerbaijan'] = [
    (-200000, -850, 'NO_KNOWN_POLITIES'),
    # -850 to -550: Kingdom of Mannae, Median influence. Small local polities.
    # No >100M polity present.
    (-850, -550, 'NOT_RELEVANT'),
    # Achaemenid Empire: Azerbaijan was part of Media Atropatene satrapy. >100M. 99%+.
    (-550, -330, 'Achaemenid Empire'),
    # -330 to -150: Post-Alexander. Atropatene (southern Azerbaijan) semi-independent,
    # Caucasian Albania (northern Azerbaijan) emerging. Seleucid Empire (>100M) had
    # nominal authority over Atropatene but not Albania.
    # GAP JUSTIFICATION: Seleucid Empire (>100M) controlled southern Azerbaijan
    # (Atropatene) while Caucasian Albania in the north was independent.
    # -150 to 224: Parthian Empire dominated both Atropatene and Albania as vassal states.
    # Parthian Empire (>100M) was the sovereign power. Controlled 99%+.
    (-150, 224, 'Parthian Empire'),
    # Sasanian Empire conquered the Parthians. Controlled both Atropatene/Azerbaijan
    # and Albania. >100M births. 99%+.
    (224, 654, 'Sasanian Empire'),
    (654, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    # ~900-1050: Local dynasties (Shirvanshahs in north, Sajids then Rawadids in south,
    # Sallarids). All small, under 100M. No >100M external polity controlled Azerbaijan.
    (900, 1050, 'NOT_RELEVANT'),
    # 1050-1236: Seljuk Empire (borderline >100M, ~113M births) controlled Azerbaijan.
    # Then Eldiguzid atabegate (Seljuk vassals/successors). Khwarezmian Empire briefly.
    # Shirvanshahs in north maintained some autonomy.
    # GAP JUSTIFICATION: Seljuk Empire (borderline >100M) controlled most of Azerbaijan;
    # Shirvanshahs retained autonomy in the north.
    # 1236-1260: Mongol Empire conquered the region. >100M births. 99%+.
    (1236, 1260, 'Mongol Empire'),
    (1260, 1335, 'Ilkhanate'),
    # 1335-1386: Jalairids, then Qara Qoyunlu expanding. Shirvanshahs independent in
    # north. All under 100M births.
    (1335, 1386, 'NOT_RELEVANT'),
    # 1386-1405: Timurid Empire (borderline >100M) conquered Azerbaijan.
    # GAP JUSTIFICATION: Timurid Empire (borderline >100M) controlled Azerbaijan.
    # 1405-1501: Qara Qoyunlu (~19M births), then Aq Qoyunlu (~39M births), plus
    # independent Shirvanshahs. All under 100M.
    (1405, 1501, 'NOT_RELEVANT'),
    # Safavid Empire originated in Ardabil, Azerbaijan. Controlled all of modern
    # Azerbaijan including Shirvan. Safavids: ~235 yrs × ~9M = ~84M births.
    # Under 100M but controlled 99%+.
    (1501, 1722, 'Safavid Empire'),
    # 1722-1735: Safavid collapse. Ottoman Empire (>100M) invaded western/southern
    # Azerbaijan. Russian Empire (>100M) took northern Caspian coast (Baku, Derbent).
    # GAP JUSTIFICATION: Ottoman Empire (>100M) and Russian Empire (>100M) each
    # controlled parts during Safavid collapse.
    # 1735-1747: Nader Shah (Afsharid dynasty) reconquered Azerbaijan. Controlled 99%+.
    (1735, 1747, 'Afsharid Empire'),
    # 1747-1806: Azerbaijan fragmented into independent khanates (Baku, Shirvan, Shaki,
    # Karabakh, etc.). No >100M polity controlled any part.
    (1747, 1806, 'NOT_RELEVANT'),
    # 1806-1828: Russian Empire (>100M) progressively conquered Azerbaijani khanates.
    # Treaty of Gulistan (1813): northern khanates. Treaty of Turkmenchay (1828): rest.
    # Qajar Persia (~54M births) controlled southern khanates until ceded to Russia.
    # GAP JUSTIFICATION: Russian Empire (>100M) controlled northern khanates while
    # Qajar Persia held the rest.
    (1828, 1917, 'Russian Empire'),
    # 1917-1918: Revolution. 1918-1920: Azerbaijan Democratic Republic.
    # 1920-1922: Soviet conquest.
    # GAP JUSTIFICATION: Russian state (>100M) contested control during civil war period.
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Azerbaijan'),
]

ASSIGNMENT['Estonia'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    (1629, 1710, 'Swedish Empire'),
    (1710, 1917, 'Russian Empire'),
    (1918, 1940, 'Estonia'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Estonia'),
]

ASSIGNMENT['Latvia'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    (1795, 1917, 'Russian Empire'),
    (1918, 1940, 'Latvia'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Latvia'),
]

ASSIGNMENT['Lithuania'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    (1253, 1569, 'Grand Duchy of Lithuania'),
    (1569, 1795, 'Polish-Lithuanian Commonwealth'),
    (1795, 1917, 'Russian Empire'),
    (1918, 1940, 'Lithuania'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Lithuania'),
]

ASSIGNMENT['Moldova'] = [
    (-200000, 1350, 'NO_KNOWN_POLITIES'),
    (1812, 1856, 'Russian Empire'),
    (1878, 1917, 'Russian Empire'),
    (1918, 1940, 'Romania'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Moldova'),
]

# =============================================================================
# WESTERN EUROPE
# =============================================================================

ASSIGNMENT['France'] = [
    (-200000, -120, 'NO_KNOWN_POLITIES'),
    (-50, 418, 'Roman Empire'),
    (1491, 1792, 'Kingdom of France'),  # Brittany in personal union from 1491 (~5-8% of pop before that)
    (1792, 1804, 'French First Republic'),
    (1804, 1814, 'First French Empire'),
    (1815, 1830, 'Bourbon Restoration'),
    (1830, 1848, 'July Monarchy'),
    (1848, 1852, 'French Second Republic'),
    (1852, 1870, 'Second French Empire'),
    # 1871-1918: Alsace-Lorraine German (~4% of population). Fails 99%.
    (1918, 1940, 'French Third Republic'),
    # 1940-1944: Vichy/occupation. Gap.
    (1946, 1958, 'French Fourth Republic'),
    (1958, 2026, 'French Fifth Republic'),
]

ASSIGNMENT['Spain'] = [
    (-200000, -220, 'NO_KNOWN_POLITIES'),
    (-19, 410, 'Roman Empire'),
    # 585-711: Visigothic Kingdom — but Basques never fully subjugated (1-3% of pop). Borderline, excluded.
    (1516, 1700, 'Habsburg Spain'),
    # 1701-1714: War of Spanish Succession. Gap.
    (1714, 1808, 'Bourbon Spain'),
    # 1808-1814: Peninsular War. Gap.
    (1814, 1868, 'Bourbon Spain'),
    (1874, 1931, 'Bourbon Restoration Spain'),
    (1931, 1936, 'Spanish Second Republic'),
    # 1936-1939: Civil War. Gap.
    (1939, 1975, 'Francoist Spain'),
    (1975, 2026, 'Kingdom of Spain'),
]

ASSIGNMENT['Portugal'] = [
    (-200000, -220, 'NO_KNOWN_POLITIES'),
    (-138, 410, 'Roman Empire'),
    (585, 711, 'Visigothic Kingdom'),
    (1249, 1580, 'Kingdom of Portugal'),
    (1580, 1640, 'Iberian Union'),
    (1640, 1910, 'Kingdom of Portugal'),
    (1910, 1926, 'Portuguese First Republic'),
    (1926, 1933, 'Ditadura Nacional'),
    (1933, 1974, 'Estado Novo'),
    (1974, 2026, 'Portuguese Third Republic'),
]

ASSIGNMENT['United Kingdom'] = [
    (-200000, 43, 'NO_KNOWN_POLITIES'),
    # 1707: Act of Union merges England + Scotland. Northern Ireland was
    # technically part of Kingdom of Ireland (separate polity), but NI's
    # population was <2% of GB's — passes 99% rule.
    (1707, 1801, 'Kingdom of Great Britain'),
    (1801, 1922, 'United Kingdom of Great Britain and Ireland'),
    (1922, 2026, 'United Kingdom of Great Britain and Northern Ireland'),
]

ASSIGNMENT['Ireland'] = [
    (-200000, 1170, 'NO_KNOWN_POLITIES'),
    (1607, 1801, 'Kingdom of Ireland'),
    (1801, 1922, 'United Kingdom of Great Britain and Ireland'),
    (1922, 1937, 'Irish Free State'),
    (1937, 1949, 'Ireland (Eire)'),
    (1949, 2026, 'Republic of Ireland'),
]

ASSIGNMENT['Italy'] = [
    (-200000, -900, 'NO_KNOWN_POLITIES'),
    (-15, 476, 'Roman Empire'),
    (493, 535, 'Ostrogothic Kingdom'),
    (554, 568, 'Byzantine Empire'),
    # 568-1870: fragmented (Lombards, city-states, Papal States, etc.)
    (1870, 1943, 'Kingdom of Italy'),
    (1945, 1946, 'Kingdom of Italy'),
    (1946, 2026, 'Italian Republic'),
]

ASSIGNMENT['Germany'] = [
    (-200000, 0, 'NO_KNOWN_POLITIES'),
    (962, 1806, 'Holy Roman Empire'),
    # 1806-1871: German Confederation, then North German Confederation. Fragmented. Gap.
    (1871, 1918, 'German Empire'),
    (1918, 1933, 'Weimar Republic'),
    (1933, 1945, 'Nazi Germany'),
    # 1945-1990: divided (BRD + DDR). Gap.
    (1990, 2026, 'Federal Republic of Germany'),
]

ASSIGNMENT['Austria'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-15, 476, 'Roman Empire'),
    (788, 843, 'Carolingian Empire'),
    (962, 1804, 'Holy Roman Empire'),  # Austrian Empire takes over from 1804
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1934, 'First Austrian Republic'),
    (1934, 1938, 'Federal State of Austria'),
    (1938, 1945, 'Nazi Germany'),
    (1945, 2026, 'Second Austrian Republic'),
]

ASSIGNMENT['Switzerland'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-15, 401, 'Roman Empire'),
    (1032, 1499, 'Holy Roman Empire'),  # Joined 1032 (Kingdom of Burgundy); de facto left 1499 (Swabian War)
    (1798, 1803, 'Helvetic Republic'),
    (1815, 2026, 'Swiss Confederation'),
]

ASSIGNMENT['Netherlands'] = [
    (-200000, -57, 'NO_KNOWN_POLITIES'),
    (962, 1581, 'Holy Roman Empire'),  # Dutch Republic declared independence 1581
    (1810, 1813, 'First French Empire'),
    (1815, 1830, 'United Kingdom of the Netherlands'),
    (1839, 1940, 'Kingdom of the Netherlands'),
    (1945, 2026, 'Kingdom of the Netherlands'),
]

ASSIGNMENT['Belgium'] = [
    (-200000, -57, 'NO_KNOWN_POLITIES'),
    (962, 1556, 'Holy Roman Empire'),  # Then Spanish Netherlands (but Liège was separate — fails 99%)
    (1795, 1815, 'French Republic / First French Empire'),
    (1815, 1830, 'United Kingdom of the Netherlands'),
    (1830, 1940, 'Kingdom of Belgium'),
    (1944, 2026, 'Kingdom of Belgium'),
]

ASSIGNMENT['Sweden'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    (1658, 2026, 'Kingdom of Sweden'),
]

ASSIGNMENT['Denmark'] = [
    (-200000, 700, 'NO_KNOWN_POLITIES'),
    (960, 2026, 'Kingdom of Denmark'),
    # Schleswig-Holstein lost 1864 = modern Germany.
    # German occupation 1940-45: Danish government continued in place; sovereignty not transferred.
]

ASSIGNMENT['Norway'] = [
    (-200000, 872, 'NO_KNOWN_POLITIES'),
    (1537, 1814, 'Denmark-Norway'),
    (1814, 1905, 'United Kingdoms of Sweden and Norway'),
    (1905, 2026, 'Kingdom of Norway'),
]

ASSIGNMENT['Finland'] = [
    (-200000, 1150, 'NO_KNOWN_POLITIES'),
    (1595, 1809, 'Kingdom of Sweden'),
    (1809, 1917, 'Russian Empire'),
    (1917, 2026, 'Republic of Finland'),
]

ASSIGNMENT['Iceland'] = [
    (-200000, 870, 'NO_KNOWN_POLITIES'),
    (930, 1262, 'Icelandic Commonwealth'),
    (1262, 1380, 'Kingdom of Norway'),
    (1380, 1814, 'Denmark-Norway'),
    (1814, 1918, 'Kingdom of Denmark'),
    (1918, 1944, 'Kingdom of Iceland'),
    (1944, 2026, 'Republic of Iceland'),
]

# =============================================================================
# EASTERN EUROPE / BALKANS
# =============================================================================

ASSIGNMENT['Poland'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    (500, 960, 'NOT_RELEVANT'),
    (1945, 1952, 'Provisional Government of Poland'),
    (1952, 1989, "Polish People's Republic"),
    (1989, 2026, 'Republic of Poland'),
]

ASSIGNMENT['Hungary'] = [
    (-200000, 895, 'NO_KNOWN_POLITIES'),
    (1000, 1541, 'Kingdom of Hungary'),
    (1699, 1867, 'Habsburg Monarchy'),
    (1867, 1918, 'Austria-Hungary'),
    (1920, 1944, 'Kingdom of Hungary'),
    (1946, 1989, "Hungarian People's Republic"),
    (1989, 2026, 'Republic of Hungary'),
]

ASSIGNMENT['Romania'] = [
    (-200000, -82, 'NO_KNOWN_POLITIES'),
    (1920, 1940, 'Kingdom of Romania'),
    (1947, 1989, 'Socialist Republic of Romania'),
    (1989, 2026, 'Romania'),
]

ASSIGNMENT['Bulgaria'] = [
    (-200000, -340, 'NO_KNOWN_POLITIES'),
    (46, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),  # Slavic settlements disrupted control from 580s
    (1018, 1185, 'Byzantine Empire'),
    (1396, 1878, 'Ottoman Empire'),
    (1940, 1944, 'Kingdom of Bulgaria'),
    (1946, 1990, "People's Republic of Bulgaria"),
    (1990, 2026, 'Republic of Bulgaria'),
]

ASSIGNMENT['Czechia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (1004, 1335, 'Holy Roman Empire'),  # Bohemia incorporated into HRE; Crown of Bohemia from 1335
    (1335, 1526, 'Kingdom of Bohemia'),
    (1526, 1804, 'Habsburg Monarchy'),
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1938, 'Czechoslovakia'),
    (1945, 1993, 'Czechoslovakia'),
    (1993, 2026, 'Czech Republic'),
]

ASSIGNMENT['Slovakia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (1000, 1526, 'Kingdom of Hungary'),
    (1526, 1804, 'Habsburg Monarchy'),
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1938, 'Czechoslovakia'),
    (1945, 1993, 'Czechoslovakia'),
    (1993, 2026, 'Slovak Republic'),
]

ASSIGNMENT['Serbia'] = [
    (-200000, -100, 'NO_KNOWN_POLITIES'),
    (46, 395, 'Roman Empire'),
    (1541, 1699, 'Ottoman Empire'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 1999, 'Federal Republic of Yugoslavia'),
    # 1999+: Kosovo under UN administration (~20% of Serbia's population). Gap.
]

ASSIGNMENT['Croatia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (1815, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),  # Istria issue <1%
    # 1991-1998: Croatian War, Serb Krajina controlled 5-12% of population. Gap.
    (1998, 2026, 'Republic of Croatia'),
]

ASSIGNMENT['Bosnia and Herzegovina'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (1482, 1878, 'Ottoman Empire'),
    (1878, 1918, 'Austria-Hungary'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    # 1992-1995: Bosnian War, country fragmented. Gap.
    (1995, 2026, 'Bosnia and Herzegovina'),
]

ASSIGNMENT['Greece'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-67, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),
    # 580-800: Slavic invasions disrupted Byzantine control of mainland Greece
    (800, 1204, 'Byzantine Empire'),  # Reasserted control by ~800
    # 1204-1669: Fragmented (Venetian islands, Crusader states, Ottoman mainland)
    # 1669-1821: Most of modern Greece was Ottoman (including Crete from 1669),
    # but Ionian Islands were Venetian (to 1797), then French/British, joined Greece 1864.
    # Ionian Islands population was ~2-3% of total — fails 99%.
    # Dodecanese was Italian until 1947 — additional ~1%.
    # Only clean from 1947.
    (1947, 1967, 'Kingdom of Greece'),
    (1967, 1974, 'Greek military junta'),
    (1974, 2026, 'Hellenic Republic'),
]

ASSIGNMENT['Albania'] = [
    (-200000, -250, 'NO_KNOWN_POLITIES'),
    (-168, 395, 'Roman Empire'),
    # 395-1501: Slavic settlements, Bulgarian control of interior. Indeterminate.
    (1501, 1912, 'Ottoman Empire'),
    (1912, 1939, 'Albania'),
    (1946, 1992, "People's Socialist Republic of Albania"),
    (1992, 2026, 'Republic of Albania'),
]

ASSIGNMENT['North Macedonia'] = [
    (-200000, -340, 'NO_KNOWN_POLITIES'),
    (-148, 395, 'Roman Empire'),
    (395, 600, 'Byzantine Empire'),
    (850, 1018, 'First Bulgarian Empire'),
    (1018, 1185, 'Byzantine Empire'),
    (1395, 1912, 'Ottoman Empire'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),
    (1991, 2026, 'Republic of North Macedonia'),
]

ASSIGNMENT['Slovenia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (962, 1804, 'Holy Roman Empire'),  # Then Austrian Empire
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),
    (1991, 2026, 'Republic of Slovenia'),
]

ASSIGNMENT['Montenegro'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 2006, 'Federal Republic of Yugoslavia'),
    (2006, 2026, 'Montenegro'),
]

ASSIGNMENT['Cyprus'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    (1960, 1974, 'Republic of Cyprus'),
    # 1974-present: indeterminate (de facto partition)
]

# =============================================================================
# MIDDLE EAST
# =============================================================================

ASSIGNMENT['Turkey'] = [
    (-200000, -2000, 'NO_KNOWN_POLITIES'),
    (72, 395, 'Roman Empire'),
    (395, 611, 'Byzantine Empire'),
    (628, 640, 'Byzantine Empire'),
    (965, 1071, 'Byzantine Empire'),
    (1522, 1923, 'Ottoman Empire'),
    (1923, 2026, 'Republic of Turkey'),
]

ASSIGNMENT['Iran'] = [
    (-200000, -2700, 'NO_KNOWN_POLITIES'),
    (-520, -330, 'Achaemenid Empire'),
    (-330, -323, 'Macedonian Empire'),
    (-312, -247, 'Seleucid Empire'),
    (224, 651, 'Sassanid Empire'),
    (651, 750, 'Umayyad Caliphate'),
    (750, 820, 'Abbasid Caliphate'),
    (1256, 1335, 'Mongol Ilkhanate'),
    (1335, 1393, 'NOT_RELEVANT'),
    (1393, 1405, 'Timurid Empire'),
    (1405, 1510, 'NOT_RELEVANT'),
    (1510, 1722, 'Safavid Empire'),
    (1736, 1747, 'Afsharid dynasty'),
    (1796, 1925, 'Qajar dynasty'),
    (1925, 1979, 'Pahlavi dynasty'),
    (1979, 2026, 'Islamic Republic of Iran'),
]

ASSIGNMENT['Iraq'] = [
    (-200000, -2334, 'NO_KNOWN_POLITIES'),
    (-539, -330, 'Achaemenid Empire'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'Parthian Empire'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 945, 'Abbasid Caliphate'),
    (945, 1055, 'Buyid dynasty'),
    (1258, 1335, 'Mongol Ilkhanate'),
    (1638, 1920, 'Ottoman Empire'),
    (1920, 1932, 'British Mandate of Mesopotamia'),
    (1932, 1958, 'Kingdom of Iraq'),
    (1958, 2026, 'Republic of Iraq'),
]

ASSIGNMENT['Egypt'] = [
    (-200000, -3100, 'NO_KNOWN_POLITIES'),
    (-3100, -2181, 'Old Kingdom Egypt'),
    (-2055, -1650, 'Middle Kingdom Egypt'),
    (-1550, -1077, 'New Kingdom Egypt'),
    (-664, -525, 'Late Period Egypt'),
    (-525, -404, 'Achaemenid Empire'),
    (-404, -343, 'Late Period Egypt'),
    (-343, -332, 'Achaemenid Empire'),
    (-332, -305, 'Macedonian Empire'),
    (-305, -30, 'Ptolemaic Kingdom'),
    (-30, 395, 'Roman Empire'),
    (395, 641, 'Byzantine Empire'),
    (641, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 868, 'Abbasid Caliphate'),
    (868, 905, 'Tulunid dynasty'),
    (905, 935, 'Abbasid Caliphate'),
    (935, 969, 'Ikhshidid dynasty'),
    (969, 1171, 'Fatimid Caliphate'),
    (1171, 1250, 'Ayyubid Sultanate'),
    (1250, 1517, 'Mamluk Sultanate'),
    (1517, 1805, 'Ottoman Empire'),
    (1805, 1882, 'Egypt (Muhammad Ali dynasty)'),
    (1882, 1922, 'British-occupied Egypt'),
    (1922, 1953, 'Kingdom of Egypt'),
    (1953, 2026, 'Republic of Egypt'),
]

ASSIGNMENT['Saudi Arabia'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (632, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 860, 'Abbasid Caliphate'),  # Lost effective control of Arabia by ~860s
    (1932, 2026, 'Kingdom of Saudi Arabia'),
]

ASSIGNMENT['Syria'] = [
    (-200000, -2334, 'NO_KNOWN_POLITIES'),
    (-200, -140, 'Seleucid Empire'),  # Fragmented after ~140 BC
    (-64, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    (1300, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1946, 'French Mandate of Syria'),
    (1946, 2011, 'Syrian Republic'),  # Civil war from 2011; government lost most territory
]

ASSIGNMENT['Lebanon'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    (-200, -140, 'Seleucid Empire'),  # Fragmented after ~140 BC
    (-64, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    (1300, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1943, 'French Mandate of Lebanon'),
    (1943, 1975, 'Republic of Lebanon'),
    # 1975-1990: indeterminate (civil war)
    (1990, 2026, 'Republic of Lebanon'),
]

ASSIGNMENT['Jordan'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (106, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (1300, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1921, 1946, 'Emirate of Transjordan'),
    (1946, 2026, 'Hashemite Kingdom of Jordan'),
]

ASSIGNMENT['Israel'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (-539, -333, 'Achaemenid Empire'),
    (-301, -200, 'Ptolemaic Kingdom'),
    (-200, -167, 'Seleucid Empire'),
    (-63, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    (1291, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1948, 'British Mandate of Palestine'),
    (1948, 2026, 'State of Israel'),
]

ASSIGNMENT['Palestine'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (1994, 2007, 'Palestinian National Authority'),
    # 2007-present: indeterminate (Gaza / West Bank split + Israeli overriding control)
]

ASSIGNMENT['Yemen'] = [
    (-200000, -1000, 'NO_KNOWN_POLITIES'),
    (-1000, 570, 'NOT_RELEVANT'),
    (570, 630, 'Sassanid Empire'),
    (630, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (1990, 2014, 'Republic of Yemen'),
]

ASSIGNMENT['Oman'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (1650, 1749, "Ya'aruba dynasty"),
    (1749, 1920, 'Al Said dynasty'),
    (1959, 2026, 'Sultanate of Oman'),
]

ASSIGNMENT['Kuwait'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (1899, 1961, 'British protectorate of Kuwait'),
    (1961, 2026, 'State of Kuwait'),
]

ASSIGNMENT['UAE'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (1971, 2026, 'United Arab Emirates'),
]

ASSIGNMENT['Bahrain'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (1602, 1783, 'Safavid / Afsharid Iran'),
    (1783, 1861, 'Al Khalifa Bahrain'),
    (1861, 1971, 'British protectorate of Bahrain'),
    (1971, 2026, 'Kingdom of Bahrain'),
]

ASSIGNMENT['Qatar'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (1916, 1971, 'British protectorate of Qatar'),
    (1971, 2026, 'State of Qatar'),
]

# =============================================================================
# AFRICA
# =============================================================================

ASSIGNMENT['Nigeria'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    (500, 1903, 'NOT_RELEVANT'),
    (1903, 1914, 'British Nigeria'),
    (1914, 1960, 'British Nigeria'),
    (1960, 1967, 'Nigeria'),
    (1970, 2026, 'Nigeria'),
]

ASSIGNMENT['Ethiopia'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, 1270, 'NOT_RELEVANT'),
    (1900, 1936, 'Ethiopian Empire'),
    (1941, 2020, 'Ethiopia'),
    (2022, 2026, 'Ethiopia'),
]

ASSIGNMENT['Democratic Republic of Congo'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1400, 1885, 'NOT_RELEVANT'),
    (1885, 1908, 'Congo Free State'),
    (1908, 1960, 'Belgian Congo'),
    (1965, 1971, 'Democratic Republic of the Congo'),
    (1971, 1997, 'Zaire'),
    (2003, 2026, 'Democratic Republic of the Congo'),
]

ASSIGNMENT['South Africa'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1910, 1961, 'Union of South Africa'),
    (1961, 2026, 'South Africa'),
]

ASSIGNMENT['Tanzania'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    (500, 1891, 'NOT_RELEVANT'),
    (1891, 1919, 'German East Africa'),
    (1919, 1961, 'British Tanganyika'),
    (1961, 1964, 'Tanganyika'),
    (1964, 2026, 'Tanzania'),
]

ASSIGNMENT['Kenya'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    (500, 1895, 'NOT_RELEVANT'),
    (1895, 1920, 'British East Africa'),
    (1920, 1963, 'Kenya Colony'),
    (1963, 2026, 'Kenya'),
]

ASSIGNMENT['Uganda'] = [
    (-200000, 1300, 'NO_KNOWN_POLITIES'),
    (1900, 1962, 'British Uganda'),
    (1962, 2026, 'Uganda'),
]

ASSIGNMENT['Algeria'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, -200, 'NOT_RELEVANT'),
    (1848, 1962, 'French Algeria'),
    (1962, 2026, 'Algeria'),
]

ASSIGNMENT['Morocco'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    # 1912-1956: removed — French zone / Spanish zone / Tangier International Zone
    # don't fit a single-polity 99% assignment
    (1956, 2026, 'Morocco'),
]

ASSIGNMENT['Tunisia'] = [
    (-200000, -814, 'NO_KNOWN_POLITIES'),
    (1956, 2026, 'Tunisia'),
]

ASSIGNMENT['Sudan'] = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    (1821, 1885, 'Turkiyya (Egyptian Sudan)'),
    (1885, 1898, 'Mahdist State'),
    (1899, 1956, 'Anglo-Egyptian Sudan'),
    # 1956-1972: indeterminate (First Sudanese Civil War)
    (1972, 1983, 'Sudan'),
    # 1983-2011: indeterminate (Second Sudanese Civil War)
    (2011, 2023, 'Sudan'),
    # 2023-present: indeterminate (Sudanese civil war)
]

ASSIGNMENT['South Sudan'] = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    (-1500, 1821, 'NOT_RELEVANT'),
    (1899, 1956, 'Anglo-Egyptian Sudan'),
    (1956, 2011, 'Sudan'),
    (2011, 2026, 'South Sudan'),
]

ASSIGNMENT['Ghana'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    (1200, 1902, 'NOT_RELEVANT'),
    (1902, 1957, 'British Gold Coast'),
    (1957, 2026, 'Ghana'),
]

ASSIGNMENT['Angola'] = [
    (-200000, 1300, 'NO_KNOWN_POLITIES'),
    (1400, 1575, 'NOT_RELEVANT'),
    (1920, 1975, 'Portuguese Angola'),
    (2002, 2026, 'Angola'),
]

ASSIGNMENT['Mozambique'] = [
    (-200000, 900, 'NO_KNOWN_POLITIES'),
    (1920, 1975, 'Portuguese Mozambique'),
    (1975, 1977, 'Mozambique'),
    # 1977-1992: indeterminate (Mozambican Civil War)
    (1992, 2026, 'Mozambique'),
]

ASSIGNMENT['Madagascar'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    (1897, 1960, 'French Madagascar'),
    (1960, 2026, 'Madagascar'),
]

# =============================================================================
# AMERICAS
# =============================================================================

ASSIGNMENT['United States'] = [
    (-200000, 1565, 'NO_KNOWN_POLITIES'),
    (1848, 1861, 'United States'),
    # 1861-1865: Civil War. Confederacy held ~30% of population. Gap.
    (1865, 2026, 'United States'),
]

ASSIGNMENT['Mexico'] = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    (-1500, 1521, 'NOT_RELEVANT'),
    (1550, 1821, 'Spanish Mexico'),
    (1821, 1823, 'First Mexican Empire'),
    (1824, 1835, 'First Mexican Republic'),
    (1835, 1846, 'Centralist Republic of Mexico'),
    (1846, 1853, 'Second Federal Republic of Mexico'),
    (1853, 1855, 'Dictatorship of Santa Anna'),
    (1857, 1863, 'Liberal Republic of Mexico'),
    (1867, 1876, 'Restored Republic'),
    (1876, 1911, 'Porfiriato'),
    (1920, 1934, 'Postrevolutionary Mexico'),
    (1934, 2000, 'PRI Mexico'),
    (2000, 2026, 'Mexico'),
]

ASSIGNMENT['Brazil'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1750, 1815, 'Portuguese Brazil'),
    (1815, 1822, 'United Kingdom of Portugal, Brazil and the Algarves'),
    (1822, 1889, 'Empire of Brazil'),
    (1889, 1930, 'First Brazilian Republic'),
    (1930, 1945, 'Vargas Era'),
    (1946, 1964, 'Fourth Brazilian Republic'),
    (1964, 1985, 'Military dictatorship of Brazil'),
    (1985, 2026, 'Brazil'),
]

ASSIGNMENT['Canada'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    (1949, 2026, 'Canada'),
]

ASSIGNMENT['Colombia'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    # 1200-1525: NOT_RELEVANT. Muisca Confederation (~1M pop, ~325 yrs: ~13M births),
    # Tayrona, Zenú — all well under 100M lifetime births. Spanish Empire not yet present.
    (1200, 1525, 'NOT_RELEVANT'),
    # 1525-1550: Gap. Spanish Empire (>100M lifetime births across all territories) present
    # via Santa Marta (1525) and Cartagena (1533), but conquest of interior ongoing;
    # Muisca territories not yet under Spanish control. <99% population control.
    (1550, 1819, 'Spanish New Granada'),
    # 1819-1886: NOT_RELEVANT. Gran Colombia (1819-1830, ~3M pop, 11 yrs: ~1.3M births),
    # Republic of New Granada (1831-1858, ~2.5M avg pop, 27 yrs: ~2.7M births),
    # Granadine Confederation (1858-1863, ~2.7M avg pop, 5 yrs: ~0.5M births),
    # United States of Colombia (1863-1886, ~3M avg pop, 23 yrs: ~2.8M births) —
    # all under 100M lifetime births. No other polity controlled any part of the territory.
    (1819, 1886, 'NOT_RELEVANT'),
    (1886, 2026, 'Republic of Colombia'),
    # Republic of Colombia (1886-2026, 140 yrs): population grew from ~4M to ~52M.
    # Time-weighted lifetime births ~122M. Exceeds 100M threshold.
]

ASSIGNMENT['Argentina'] = [
    (-200000, 1536, 'NO_KNOWN_POLITIES'),
    # No polity with 100K+ centralized population in Argentine territory before Spanish arrival.
    # Inca briefly reached NW Argentina ~1470s but their presence was marginal and the Inca
    # Empire had <100M lifetime births (~38M) so would be NOT_RELEVANT regardless.
    # Diaguita, Guaraní, and others were decentralized chiefdoms below 100K threshold.
    #
    # 1536-1816: Gap. Spanish Empire (>100M lifetime births across all territories) controlled
    # major settlements (Santiago del Estero 1553, Mendoza 1561, Tucumán 1565, Córdoba 1573,
    # Buenos Aires refounded 1580) but unconquered Pampas/Patagonia indigenous peoples
    # (Mapuche, Tehuelche, etc.) held ~3-7% of the population. <99% control.
    #
    # 1816-2026: NOT_RELEVANT. All post-independence Argentine polities had <100M lifetime births:
    # - United Provinces / Argentine Confederation (1816-1862, ~1.5M avg pop, 46 yrs: ~2.8M births)
    # - Argentina (1862-1930, ~4M avg pop, 68 yrs: ~10.9M births)
    # - Infamous Decade (1930-1943, ~12M avg pop, 13 yrs: ~6.2M births)
    # - Peronist Argentina (1946-1955, ~16M avg pop, 9 yrs: ~5.8M births)
    # - Argentine Revolution (1966-1973, ~23M avg pop, 7 yrs: ~6.4M births)
    # - National Reorganization Process (1976-1983, ~28M avg pop, 7 yrs: ~7.8M births)
    # - Argentina (1983-2026, ~38M avg pop, 43 yrs: ~65M births)
    # No other polity with >100M births controlled any part of the territory after 1816.
    # Even treating Argentina as a continuous polity 1862-2026 (164 yrs, ~10M avg pop)
    # yields ~66M births when properly time-weighted. Under 100M.
    # Conquest of the Desert (1879-84) brought remaining indigenous territory under control.
    (1816, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Peru'] = [
    (-200000, -200, 'NO_KNOWN_POLITIES'),
    # First centralized polities reaching 100K people around 200 BCE (late Chavín successors,
    # early Moche/Nazca precursors in coastal valleys).
    #
    # -200 to 1532: NOT_RELEVANT. All pre-Columbian Peruvian polities had <100M lifetime births:
    # - Moche (~100-700 CE, ~0.5M avg pop, 600 yrs: ~12M births)
    # - Wari Empire (~600-1000 CE, ~1.5M avg pop, 400 yrs: ~24M births)
    # - Chimú (~900-1470, ~0.7M avg pop, 570 yrs: ~16M births)
    # - Inca Empire (~1438-1533, ~10M avg pop, 95 yrs: ~38M births)
    # Spanish Empire not yet present in Peru before 1532.
    (-200, 1532, 'NOT_RELEVANT'),
    # 1532-1542: Gap. Spanish Empire (>100M lifetime births across all territories) conquering
    # Peru — Cajamarca 1532, Cusco captured 1533, Lima founded 1535. But conquest still
    # incomplete; neo-Inca state at Vilcabamba; not yet 99% population control.
    (1542, 1821, 'Spanish Peru'),
    # Viceroyalty of Peru established 1542. Spain controlled 99%+ of Peru's population.
    # Vilcabamba neo-Inca state (1537-1572) held <1% of population.
    #
    # 1821-1824: Gap. Spanish Empire (>100M lifetime births) still controlled significant parts
    # of Peru — royalists held Cusco and southern highlands until Battle of Ayacucho (Dec 1824).
    #
    # 1824-2026: NOT_RELEVANT. All post-independence Peruvian polities had <100M lifetime births:
    # - Republic of Peru (1824-1836, ~1.5M avg pop, 12 yrs: ~0.7M births)
    # - Peru-Bolivia Confederation (1836-1839, ~1.8M avg pop Peru portion, 3 yrs: ~0.2M births)
    # - Republic of Peru (1839-1968, ~4M avg pop, 129 yrs: ~20.6M births)
    # - Revolutionary Government of the Armed Forces (1968-1980, ~14M avg pop, 12 yrs: ~6.7M births)
    # - Peru (1980-1992, ~20M avg pop, 12 yrs: ~9.6M births)
    # - Fujimori regime (1992-2000, ~25M avg pop, 8 yrs: ~8M births)
    # - Peru (2000-2026, ~30M avg pop, 26 yrs: ~31.2M births)
    # Total across all regimes ~77M. No single regime exceeds 100M.
    # No other polity with >100M births controlled any part of Peru after 1824.
    (1824, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Venezuela'] = [
    (-200000, 1521, 'NO_KNOWN_POLITIES'),
    # No centralized polity of 100K+ people in Venezuelan territory before Spanish arrival.
    # Indigenous peoples (Caribs, Arawaks, Timoto-Cuica) organized as chiefdoms, none
    # reaching 100K under centralized political control.
    #
    # 1521-1600: Gap. Spanish Empire (>100M lifetime births across all territories) present
    # from Cumaná (1521), Coro (1527), Klein-Venedig/Welser colony (1528-1546). But
    # conquest and settlement ongoing; large indigenous populations not yet under control.
    (1600, 1810, 'Spanish Venezuela'),
    # By ~1600, Spanish settlements controlled the coast and Andes foothills where 99%+
    # of Venezuela's population lived. Interior Llanos/Guayana were very sparsely populated.
    # Various Spanish provinces (Venezuela, Maracaibo, Cumaná, Guayana, etc.) were all
    # part of the single Spanish Empire polity, unified administratively as Captaincy General
    # in 1777 but under continuous Spanish sovereignty throughout.
    #
    # 1810-1821: Gap. Spanish Empire (>100M lifetime births) and independence forces both
    # controlled parts of Venezuela during the War of Independence (1810-1823).
    # Royalists held key areas while patriots controlled others.
    #
    # 1821-2026: NOT_RELEVANT. From 1821, no polity with >100M lifetime births controlled
    # any part of Venezuelan territory. All post-independence polities had <100M births:
    # - Gran Colombia (1819-1830, ~3M total pop, 11 yrs: ~1.3M births)
    # - Republic of Venezuela (1830-1948, ~3M avg pop, 118 yrs: ~14.2M births)
    # - Military government (1948-1958, ~6M avg pop, 10 yrs: ~2.4M births)
    # - Venezuela (1958-1999, ~16M avg pop, 41 yrs: ~26.2M births)
    # - Bolivarian Republic (1999-2026, ~28M avg pop, 27 yrs: ~30.2M births)
    # Total ~73M across all regimes.
    (1821, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Chile'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (600, 1470, 'NOT_RELEVANT'),
    (1883, 1973, 'Chile'),
    (1973, 1990, 'Military dictatorship of Chile'),
    (1990, 2026, 'Chile'),
]

ASSIGNMENT['Ecuador'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    # No centralized polity of 100K+ people in Ecuadorian territory before ~600 CE.
    # Valdivia, Machalilla, and other early cultures were small. The Cañari and other
    # highland groups began forming larger polities around this time.
    #
    # 600-1534: NOT_RELEVANT. All pre-Columbian Ecuadorian polities had <100M lifetime births:
    # - Cañari, Quitu-Cara, Puruhá kingdoms (~600-1470, <0.5M avg pop each, <100M births)
    # - Inca Empire in Ecuador (~1463-1533, ~10M avg pop total empire, 95 yrs: ~38M births)
    # Spanish Empire not yet present in Ecuador before 1534.
    (600, 1534, 'NOT_RELEVANT'),
    # 1534: Spanish conquest of Quito. By ~1534, Spain controlled the main population centers.
    # The Real Audiencia of Quito was established in 1563 as part of the Viceroyalty of Peru
    # (later transferred to Viceroyalty of New Granada in 1717/1739).
    # Spain controlled 99%+ of Ecuador's population from ~1534.
    (1534, 1822, 'Spanish Ecuador'),
    # Battle of Pichincha (May 1822) ended Spanish rule. Ecuador joined Gran Colombia.
    #
    # 1822-2026: NOT_RELEVANT. All post-independence Ecuadorian polities had <100M births:
    # - Gran Colombia (1822-1830, ~3M total pop, 11 yrs total: ~1.3M births)
    # - Republic of Ecuador (1830-1972, ~2.5M avg pop, 142 yrs: ~14.2M births)
    # - Military government (1972-1979, ~7M avg pop, 7 yrs: ~2M births)
    # - Ecuador (1979-2026, ~12M avg pop, 47 yrs: ~22.6M births)
    # Total across all regimes ~40M. No other polity with >100M births present.
    (1822, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Bolivia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (1470, 1533, 'Inca Empire'),
    (1542, 1825, 'Spanish Upper Peru'),
    (1825, 1964, 'Bolivia'),
    (1964, 1982, 'Military Bolivia'),
    (1982, 2026, 'Bolivia'),
]

ASSIGNMENT['Paraguay'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1542, 1811, 'Spanish Paraguay'),
    (1811, 1954, 'Paraguay'),
    (1954, 1989, 'Stroessner regime'),
    (1989, 2026, 'Paraguay'),
]

ASSIGNMENT['Uruguay'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1776, 1816, 'Spanish Rio de la Plata'),
    # 1816-1828: indeterminate
    (1828, 1973, 'Uruguay'),
    (1973, 1985, 'Civic-military dictatorship of Uruguay'),
    (1985, 2026, 'Uruguay'),
]

ASSIGNMENT['Cuba'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1515, 1898, 'Spanish Cuba'),
    (1898, 1902, 'US military occupation of Cuba'),
    (1902, 1959, 'Republic of Cuba'),
    (1959, 2026, 'Revolutionary Cuba'),
]

ASSIGNMENT['Guatemala'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1841, 'Federal Republic of Central America'),
    (1841, 2026, 'Guatemala'),
]

ASSIGNMENT['Honduras'] = [
    (-200000, 250, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1841, 'Federal Republic of Central America'),
    (1841, 2026, 'Honduras'),
]

ASSIGNMENT['El Salvador'] = [
    (-200000, 250, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1841, 'Federal Republic of Central America'),
    (1841, 2026, 'El Salvador'),
]

ASSIGNMENT['Nicaragua'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1838, 'Federal Republic of Central America'),
    (1838, 2026, 'Nicaragua'),
]

ASSIGNMENT['Costa Rica'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1838, 'Federal Republic of Central America'),
    (1838, 2026, 'Costa Rica'),
]

ASSIGNMENT['Panama'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish New Granada'),
    (1821, 1830, 'Gran Colombia'),
    (1831, 1858, 'Republic of New Granada'),
    (1858, 1863, 'Granadine Confederation'),
    (1863, 1886, 'United States of Colombia'),
    (1886, 1903, 'Republic of Colombia'),
    (1903, 1968, 'Panama'),
    (1968, 1989, 'Military Panama'),
    (1989, 2026, 'Panama'),
]

# =============================================================================
# OCEANIA
# =============================================================================

ASSIGNMENT['Australia'] = [
    (-200000, 1788, 'NO_KNOWN_POLITIES'),
    (1901, 2026, 'Australia'),
]

ASSIGNMENT['New Zealand'] = [
    (-200000, 1840, 'NO_KNOWN_POLITIES'),
    # Maori strongholds (King Country, Te Urewera) held 3-7% of population in 1870.
    (1885, 2026, 'New Zealand'),
]

ASSIGNMENT['Papua New Guinea'] = [
    (-200000, 1884, 'NO_KNOWN_POLITIES'),
    (1949, 1975, 'Australian Papua New Guinea'),
    (1975, 2026, 'Papua New Guinea'),
]

# =============================================================================
# AFRICA (ADDITIONS)
# =============================================================================

ASSIGNMENT['Benin'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    # Dahomey kingdom only controlled southern third; northern kingdoms (Bariba, etc.) were separate.
    # French conquest unified the territory.
    (1900, 1960, 'French Dahomey'),  # Part of French West Africa
    (1960, 1975, 'Republic of Dahomey'),
    (1975, 1990, "People's Republic of Benin"),
    (1990, 2026, 'Republic of Benin'),
]

ASSIGNMENT['Mali'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    (300, 750, 'NOT_RELEVANT'),
    (1600, 1893, 'NOT_RELEVANT'),
    (1893, 1960, 'French Sudan'),
    (1960, 1968, 'Republic of Mali'),
    (1968, 1991, 'Mali (Moussa Traore)'),
    (1991, 2012, 'Republic of Mali'),
    (2013, 2020, 'Republic of Mali'),
]

ASSIGNMENT['Burkina Faso'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    # Mossi kingdoms (Ouagadougou, Yatenga, etc.) controlled central plateau but not
    # western (Bobo, Lobi) or northern (Tuareg/Fulani) regions. No single pre-colonial polity.
    (1919, 1932, 'Upper Volta'),  # French colony
    # 1932-1947: dissolved into Cote d'Ivoire, Mali, Niger. Gap.
    (1947, 1960, 'Upper Volta'),  # Reconstituted
    (1960, 1966, 'Republic of Upper Volta'),
    (1966, 1983, 'Upper Volta'),
    (1983, 1987, 'Burkina Faso (Sankara)'),
    (1987, 2014, 'Burkina Faso (Compaore)'),
    (2014, 2022, 'Burkina Faso'),
    # 2022-present: indeterminate (military coup, jihadist insurgency controls ~40% of territory)
]

ASSIGNMENT['Cameroon'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    # No pre-colonial polity controlled all of modern Cameroon.
    (1902, 1916, 'German Kamerun'),  # Full interior control from ~1902
    # 1916-1961: split between French (80%) and British (20%) mandates. Gap.
    (1961, 2026, 'Republic of Cameroon'),  # Reunification (Southern Cameroons joined)
]

ASSIGNMENT['Niger'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    # Kanem-Bornu, Songhai, Hausa states partially covered modern Niger; none controlled all.
    (1922, 1960, 'French Niger'),  # Part of French West Africa
    (1960, 1974, 'Republic of Niger'),
    (1974, 1991, 'Niger (Kountche/Saibou)'),
    (1991, 1996, 'Republic of Niger'),
    (1996, 1999, 'Niger (Mainassara)'),
    (1999, 2010, 'Republic of Niger'),
    (2010, 2011, 'Niger (military junta)'),
    (2011, 2023, 'Republic of Niger'),
    # 2023-present: indeterminate (military coup)
]

ASSIGNMENT["Cote d'Ivoire"] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    # Kong Empire, Gyaaman, Baoule kingdoms — none covered the whole territory.
    (1915, 1960, "French Cote d'Ivoire"),  # Full pacification ~1915; part of French West Africa
    (1960, 1999, "Republic of Cote d'Ivoire"),
    # 1999-2002: indeterminate (coup)
    # 2002-2011: indeterminate (civil war, country split north/south)
    (2011, 2026, "Republic of Cote d'Ivoire"),
]

ASSIGNMENT['Somalia'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    # Somalia's clan-based system means no single polity ever controlled 99% of the territory
    # before European colonization. Colonial period: split between British Somaliland,
    # Italian Somaliland, and French Somaliland — no single polity.
    (1960, 1991, 'Somali Republic'),  # Including Siad Barre era (1969-1991)
    # 1991-present: indeterminate (state collapse, warlords, Somaliland de facto independent)
]

ASSIGNMENT['Chad'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    # Kanem-Bornu Empire controlled Lake Chad basin but not the south (Sara peoples)
    # or the Tibesti (Toubou). No pre-colonial polity covered all modern Chad.
    (1920, 1960, 'French Equatorial Africa'),  # Chad within AEF
    (1960, 1975, 'Republic of Chad'),
    # 1975-1982: indeterminate (civil war, Libyan intervention)
    (1982, 1990, 'Chad (Habre)'),
    (1990, 2021, 'Chad (Deby)'),
    (2021, 2026, 'Chad'),  # Transitional military government
]

ASSIGNMENT['Guinea'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    # Futa Jallon theocracy (1727-1896) controlled central highlands but not coast
    # (Susu) or forest region (Kissi, Toma). No single pre-colonial polity.
    (1898, 1958, 'French Guinea'),  # Part of French West Africa
    (1958, 1984, 'Guinea (Sekou Toure)'),
    (1984, 2008, 'Guinea (Lansana Conte)'),
    (2010, 2021, 'Republic of Guinea'),
    # 2021-present: indeterminate (military coup)
]

ASSIGNMENT['Libya'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    # Greek colonies only in Cyrenaica; Tripolitania was Phoenician/Carthaginian.
    # Unified under Rome.
    (-96, 395, 'Roman Empire'),  # Cyrenaica from 96 BC, Tripolitania effectively under Rome from ~146 BC
    (395, 455, 'Byzantine Empire'),
    # 455-534: Vandal Kingdom in Tripolitania, Byzantine still held Cyrenaica. Gap.
    (534, 643, 'Byzantine Empire'),
    (643, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 800, 'Abbasid Caliphate'),
    (1551, 1711, 'Ottoman Empire'),
    (1711, 1835, 'Karamanli dynasty'),  # Ottoman vassal, effectively independent
    (1835, 1911, 'Ottoman Empire'),
    (1912, 1943, 'Italian Libya'),
    # 1943-1951: British/French military administration
    (1951, 1969, 'Kingdom of Libya'),
    (1969, 2011, 'Libyan Arab Jamahiriya'),
    # 2011-present: indeterminate (civil war, two rival governments)
]

ASSIGNMENT['Rwanda'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    # Kingdom of Rwanda dominated essentially all of modern Rwanda's territory by ~1700.
    (1700, 1890, 'Kingdom of Rwanda'),
    (1890, 1916, 'German East Africa'),
    (1916, 1962, 'Belgian Rwanda'),  # League of Nations / UN mandate
    (1962, 1994, 'Republic of Rwanda'),
    # April-July 1994: genocide — government lost control. Brief gap.
    (1994, 2026, 'Republic of Rwanda'),
]

ASSIGNMENT['Senegal'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    # Jolof Empire (1350-1549) only covered western Wolof areas, not Casamance or east.
    (1895, 1960, 'French West Africa'),  # Senegal colony within AOF
    (1960, 2026, 'Republic of Senegal'),  # Casamance rebellion never controlled >1% of population
]

ASSIGNMENT['Togo'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    # No pre-colonial polity covered all of modern Togo.
    (1884, 1914, 'German Togoland'),
    # 1914-1960: split between French and British mandates. Gap.
    (1960, 2026, 'Republic of Togo'),  # French Togoland became independent; British part joined Ghana
]

ASSIGNMENT['Burundi'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    # Kingdom of Burundi's borders closely matched modern Burundi by ~1700.
    (1700, 1890, 'Kingdom of Burundi'),
    (1890, 1916, 'German East Africa'),
    (1916, 1962, 'Belgian Ruanda-Urundi'),
    (1962, 1966, 'Kingdom of Burundi'),
    (1966, 1993, 'Republic of Burundi'),
    # 1993-2005: indeterminate (civil war)
    (2005, 2026, 'Republic of Burundi'),
]

ASSIGNMENT['Zimbabwe'] = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    # Great Zimbabwe (11th-15th c) and Mutapa/Rozvi empires covered parts but not all.
    (1895, 1923, 'British South Africa Company (Rhodesia)'),
    (1923, 1953, 'Southern Rhodesia'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    (1965, 1979, 'Rhodesia'),  # UDI
    (1980, 2026, 'Zimbabwe'),
]

ASSIGNMENT['Central African Republic'] = [
    (-200000, 1800, 'NO_KNOWN_POLITIES'),
    # No pre-colonial state controlled this territory.
    (1910, 1960, 'French Equatorial Africa'),  # Oubangui-Chari colony
    (1960, 1976, 'Central African Republic'),
    (1976, 1979, 'Central African Empire'),
    (1979, 2013, 'Central African Republic'),
    # 2013-present: indeterminate (Seleka, anti-balaka; government controls ~1/3 of territory)
]

ASSIGNMENT['Malawi'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    # Maravi Confederacy (16th-18th c) covered much of modern Malawi but was loose.
    (1891, 1953, 'British Central Africa / Nyasaland'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    (1964, 2026, 'Malawi'),
]

ASSIGNMENT['Zambia'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    # Lozi (Barotseland), Bemba, Lunda kingdoms — none controlled all of modern Zambia.
    (1924, 1953, 'Northern Rhodesia'),  # British colony (BSAC rule before 1924)
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    (1964, 2026, 'Zambia'),
]

ASSIGNMENT['Liberia'] = [
    (-200000, 1822, 'NO_KNOWN_POLITIES'),
    # Founded by ACS settlers; settler control of interior only complete by ~1920s.
    (1926, 1980, 'Republic of Liberia'),  # Effective control of interior from ~1920s
    (1980, 1989, 'Liberia (Doe)'),
    # 1989-2003: indeterminate (First and Second Liberian Civil Wars)
    (2003, 2026, 'Republic of Liberia'),
]

ASSIGNMENT['Mauritania'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    # Fragmented emirates (Trarza, Brakna, Adrar) — none covered all territory.
    (1920, 1960, 'French Mauritania'),  # Part of French West Africa
    (1960, 1978, 'Islamic Republic of Mauritania'),
    (1978, 1991, 'Mauritania (military rule)'),
    (1991, 2026, 'Islamic Republic of Mauritania'),
]

ASSIGNMENT['Congo'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    # Republic of the Congo (Brazzaville). Kongo Kingdom covered southern portion only.
    (1910, 1960, 'French Equatorial Africa'),  # Moyen-Congo colony
    (1960, 1970, 'Republic of the Congo'),
    (1970, 1991, "People's Republic of the Congo"),
    (1991, 1997, 'Republic of the Congo'),
    # 1997-1999: indeterminate (civil war)
    (1999, 2026, 'Republic of the Congo'),
]

ASSIGNMENT['Namibia'] = [
    (-200000, 1800, 'NO_KNOWN_POLITIES'),
    # No pre-colonial polity controlled all of modern Namibia (Herero, Nama, Ovambo separate).
    (1884, 1915, 'German South West Africa'),
    (1920, 1990, 'South West Africa'),  # South African mandate/administration
    (1990, 2026, 'Republic of Namibia'),
]

ASSIGNMENT['Sierra Leone'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    # No pre-colonial polity controlled all of modern Sierra Leone.
    (1896, 1961, 'British Sierra Leone'),  # Colony + Protectorate unified
    (1961, 1991, 'Sierra Leone'),
    # 1991-2002: indeterminate (civil war — RUF controlled large portions)
    (2002, 2026, 'Sierra Leone'),
]

ASSIGNMENT['Eritrea'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    # D'mt and Aksum were centered in northern Ethiopia/Eritrea but coast and lowlands
    # were often separate. No single pre-colonial polity covered all of modern Eritrea.
    (1890, 1941, 'Italian Eritrea'),
    (1941, 1952, 'British Eritrea'),
    (1952, 1962, 'Eritrea (federated with Ethiopia)'),
    (1962, 1991, 'Ethiopia'),  # Annexed; independence war ongoing but government held territory
    (1993, 2026, 'State of Eritrea'),
]

# =============================================================================
# AMERICAS (ADDITIONS)
# =============================================================================

ASSIGNMENT['Dominican Republic'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1502, 1795, 'Spanish Santo Domingo'),  # Effective Spanish settlement from ~1502
    # 1795-1809: French cession (Treaty of Basel), then reconquered by Spain
    (1809, 1821, 'Spanish Santo Domingo'),
    (1822, 1844, 'Republic of Haiti'),  # Haitian occupation of entire island
    (1844, 1861, 'Dominican Republic'),
    (1861, 1865, 'Spanish Santo Domingo'),  # Spanish re-annexation
    (1865, 1916, 'Dominican Republic'),
    (1916, 1924, 'US occupation of Dominican Republic'),
    (1924, 1930, 'Dominican Republic'),
    (1930, 1961, 'Dominican Republic (Trujillo)'),
    (1966, 2026, 'Dominican Republic'),  # 1961-1965: instability/US intervention. Gap.
]

ASSIGNMENT['Haiti'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1697, 1791, 'French Saint-Domingue'),
    # 1791-1804: Haitian Revolution — indeterminate
    (1804, 1806, 'Empire of Haiti'),
    # 1806-1820: indeterminate (split: Kingdom in north, Republic in south)
    (1820, 1844, 'Republic of Haiti'),  # Included Dominican Republic 1822-1844
    (1844, 1849, 'Republic of Haiti'),
    (1849, 1859, 'Second Empire of Haiti'),
    (1859, 1915, 'Republic of Haiti'),
    (1915, 1934, 'US occupation of Haiti'),
    (1934, 1957, 'Republic of Haiti'),
    (1957, 1986, 'Haiti (Duvalier)'),
    (1986, 2026, 'Republic of Haiti'),
]

ASSIGNMENT['Jamaica'] = [
    (-200000, 1509, 'NO_KNOWN_POLITIES'),
    (1509, 1655, 'Spanish Jamaica'),
    (1655, 1962, 'British Jamaica'),
    (1962, 2026, 'Jamaica'),
]

# =============================================================================
# EUROPE (ADDITIONS)
# =============================================================================

ASSIGNMENT['Luxembourg'] = [
    (-200000, -50, 'NO_KNOWN_POLITIES'),
    (-50, 410, 'Roman Empire'),
    (1815, 1839, 'United Kingdom of the Netherlands'),
    (1839, 1914, 'Grand Duchy of Luxembourg'),
    # 1914-1918: German occupation
    (1918, 1940, 'Grand Duchy of Luxembourg'),
    # 1940-1944: German occupation/annexation
    (1944, 2026, 'Grand Duchy of Luxembourg'),
]

# =============================================================================
# SUB-REGION ASSIGNMENTS
# =============================================================================
# For countries where the country-level assignment is "indeterminate", we can
# sometimes resolve it at the sub-region level. This is mainly useful for China,
# where "core China proper" provinces were under every major dynasty even though
# the dynasty didn't control ALL of modern China.

# Chinese provinces that were part of every unified dynasty (Qin through Ming)
# These provinces are in the Yellow River / Yangtze heartland.
CHINA_CORE = {
    'Henan', 'Shandong', 'Jiangsu', 'Anhui', 'Hubei', 'Hunan',
    'Jiangxi', 'Zhejiang', 'Fujian', 'Shaanxi', 'Shanxi', 'Sichuan',
    'Shanghai', 'Chongqing', 'Guangdong', 'Hainan',
}

# Provinces that were Southern Song (1127-1279) but not necessarily Northern Song
# (because Hebei/Beijing was under Liao/Jin)
CHINA_SOUTH = CHINA_CORE | {'Guizhou', 'Guangxi'}
# Note: Hebei, Beijing, Tianjin were Liao territory 907-1125, then Jin 1125-1234.
# Gansu was partly Tangut (Western Xia). Yunnan was independent (Nanzhao/Dali).
# Manchuria (Liaoning, Jilin, Heilongjiang) was outside Chinese control.

# Dynasty assignments for core provinces
# These only apply when the country-level assignment returns 'indeterminate'
CHINA_CORE_DYNASTIES = [
    (-221, -207, 'Qin Dynasty'),
    (-202, 9, 'Western Han Dynasty'),
    (25, 220, 'Eastern Han Dynasty'),
    # 220-280: Three Kingdoms — indeterminate even for core (Wei vs Shu vs Wu)
    (280, 304, 'Western Jin Dynasty'),
    # 304-589: fragmented (Sixteen Kingdoms, Northern/Southern Dynasties)
    (589, 618, 'Sui Dynasty'),
    (618, 755, 'Tang Dynasty'),
    # 755-960: fragmented (late Tang, Five Dynasties and Ten Kingdoms)
    (960, 1127, 'Northern Song Dynasty'),  # Core provinces only — Hebei was Liao
    (1127, 1279, 'Southern Song Dynasty'),  # South only — north was Jin then Mongol
    (1368, 1644, 'Ming Dynasty'),
    (1644, 1759, 'Qing Dynasty'),  # Fills gap before country-level Qing starts
    # 1912-1928: warlord era. 1928-1937: Nanjing government controlled core provinces.
    (1928, 1937, 'Republic of China (Nanjing)'),
]

# For the UK, simple sub-region logic
UK_SUBREGION_ASSIGNMENTS = {
    'England': [
        (927, 1649, 'Kingdom of England'),
        (1649, 1660, 'Commonwealth of England'),
        (1660, 1707, 'Kingdom of England'),
    ],
    'Scotland': [
        (843, 1707, 'Kingdom of Scotland'),
    ],
    'Wales': [
        # Wales conquered by England 1283, but previously independent princes
        (1283, 1707, 'Kingdom of England'),
    ],
}


# =============================================================================
# THE ASSIGNMENT FUNCTION
# =============================================================================

def assign_polity(country, year, subregion=None):
    """
    Given a modern country name, a year, and optionally a sub-region,
    return the polity name, 'indeterminate', 'no_known_polities', or 'not_relevant'.

    Returns:
        str: polity name if cleanly assigned
        'indeterminate': known polities existed but can't cleanly assign
        'no_known_polities': predates any reliably known polities
        'not_relevant': polities existed but all too small for top-100 ranking
    """
    # First try country-level assignment
    country_result = _assign_country(country, year)

    # If country-level is determinate (assigned, no_known_polities, or not_relevant), return it
    if country_result != 'indeterminate':
        return country_result

    # Try sub-region resolution
    if subregion is not None:
        sub_result = _assign_subregion(country, year, subregion)
        if sub_result is not None:
            return sub_result

    return country_result


def _assign_country(country, year):
    """Country-level assignment only.

    Each country's ASSIGNMENT list contains its full timeline:
    - 'NO_KNOWN_POLITIES': predates any known polities
    - 'NOT_RELEVANT': polities existed but all too small for top-100
    - Any other string: the polity name
    - Gaps between entries: 'indeterminate'
    """
    if country not in ASSIGNMENT:
        return 'indeterminate'

    for start, end, polity in ASSIGNMENT[country]:
        if start <= year < end:
            if polity == 'NO_KNOWN_POLITIES':
                return 'no_known_polities'
            if polity == 'NOT_RELEVANT':
                return 'not_relevant'
            return polity

    return 'indeterminate'


def _assign_subregion(country, year, subregion):
    """Try to resolve an indeterminate country-level assignment using sub-region data."""
    if country == 'China':
        # Check if this province is in core China proper
        if subregion in CHINA_CORE:
            for start, end, polity in CHINA_CORE_DYNASTIES:
                if start <= year < end:
                    return polity
        # Southern Song only applies to southern provinces
        if subregion in CHINA_SOUTH and 1127 <= year < 1279:
            return 'Southern Song Dynasty'
        # Manchukuo for Manchurian provinces
        if subregion in ('Liaoning', 'Jilin', 'Heilongjiang') and 1932 <= year < 1945:
            return 'Manchukuo'

    elif country == 'United Kingdom':
        if subregion in UK_SUBREGION_ASSIGNMENTS:
            for start, end, polity in UK_SUBREGION_ASSIGNMENTS[subregion]:
                if start <= year < end:
                    return polity

    return None
