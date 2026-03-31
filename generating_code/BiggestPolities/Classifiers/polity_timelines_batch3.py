"""
Complete polity timelines for: Zimbabwe, Central African Republic, Malawi, Zambia,
Liberia, Mozambique, Angola, Namibia, Sierra Leone, Eritrea, Libya,
Dominican Republic, Haiti, Jamaica, Congo (Republic of the Congo),
Papua New Guinea, Australia, New Zealand, Luxembourg, Cyprus, Palestine,
Kuwait, UAE, Qatar, Bahrain, Oman, Kyrgyzstan, Tajikistan, Turkmenistan,
Moldova, North Korea, South Korea.

Each entry: (start_year, end_year_exclusive, polity_name)
Negative years = BCE.

Special polity names:
- NO_KNOWN_POLITIES: before first polity with 100k+ centralized population
- NOT_RELEVANT: polities existed but ALL had <100M lifetime births
  (lifetime births = avg_population × 0.04 × years_of_existence)
- Gaps between entries = indeterminate (polities existed with >100M lifetime
  births, but no single one controlled 99%+ of the population)

For every gap, a justification comment explains which >100M polity was present.
"""

TIMELINES = {}

# =============================================================================
# ZIMBABWE
# =============================================================================
# Gap 1963-1965 justification: UK (>100M lifetime births) retained sovereignty
# after Federation dissolved, before Rhodesia's UDI in November 1965.

TIMELINES['Zimbabwe'] = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    (1000, 1895, 'NOT_RELEVANT'),  # Great Zimbabwe, Mutapa, Rozvi — all <100M
    (1895, 1923, 'British South Africa Company (Rhodesia)'),
    (1923, 1953, 'Southern Rhodesia'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    # Gap 1963-1965: UK (>100M lifetime births) sovereign during transition.
    (1965, 1979, 'Rhodesia'),
    (1980, 2026, 'Zimbabwe'),
]

# =============================================================================
# CENTRAL AFRICAN REPUBLIC
# =============================================================================
# Gap 2013-2026 justification: Government controls ~1/3 of territory after
# Seleka crisis. France (>100M lifetime births) intervened militarily
# (Operation Sangaris 2013-2016; ongoing presence).

TIMELINES['Central African Republic'] = [
    (-200000, 1800, 'NO_KNOWN_POLITIES'),
    (1800, 1910, 'NOT_RELEVANT'),  # Zande kingdoms, Dar al-Kuti — all <100M
    (1910, 1960, 'French Equatorial Africa'),
    (1960, 1976, 'Central African Republic'),
    (1976, 1979, 'Central African Empire'),
    (1979, 2013, 'Central African Republic'),
    # Gap 2013-2026: Seleka/anti-balaka crisis. France (>100M) intervened.
    # No single polity controls 99%.
]

# =============================================================================
# MALAWI
# =============================================================================
# Gap 1963-1964 justification: UK (>100M lifetime births) sovereign during
# transition from Federation dissolution (Dec 1963) to independence (Jul 1964).

TIMELINES['Malawi'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1500, 1891, 'NOT_RELEVANT'),  # Maravi Confederacy, Ngoni, Yao — all <100M
    (1891, 1953, 'British Central Africa / Nyasaland'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    # Gap 1963-1964: UK (>100M) sovereign during transition.
    (1964, 2026, 'Malawi'),
]

# =============================================================================
# ZAMBIA
# =============================================================================
# Gap 1890-1924 justification: British Empire (>100M lifetime births) sovereign
# via BSAC charter. Barotseland and direct BSAC areas had separate arrangements.
#
# Gap 1963-1964 justification: UK (>100M) sovereign during transition.

TIMELINES['Zambia'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    (1600, 1890, 'NOT_RELEVANT'),  # Lozi, Bemba, Lunda kingdoms — all <100M
    # Gap 1890-1924: British Empire (>100M) sovereign via BSAC charter.
    # Barotseland retained separate protectorate status.
    (1924, 1953, 'Northern Rhodesia'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    # Gap 1963-1964: UK (>100M) sovereign during transition.
    (1964, 2026, 'Zambia'),
]

# =============================================================================
# LIBERIA
# =============================================================================
# Gap 1989-2003 justification: Civil wars. Nigeria (>100M lifetime births:
# ~80M avg × 0.04 × 66 years = ~211M) deployed ECOMOG troops and controlled
# parts of Monrovia and surrounding territory.

TIMELINES['Liberia'] = [
    (-200000, 1822, 'NO_KNOWN_POLITIES'),
    (1822, 1926, 'NOT_RELEVANT'),  # Settler state + independent interior; all polities <100M
    (1926, 1980, 'Republic of Liberia'),
    (1980, 1989, 'Liberia (Doe)'),
    # Gap 1989-2003: Civil wars. Nigeria (>100M) deployed ECOMOG troops
    # controlling parts of the territory.
    (2003, 2026, 'Republic of Liberia'),
]

# =============================================================================
# MOZAMBIQUE
# =============================================================================
# Gap 900-1920: Portuguese Empire (>100M lifetime births across all territories:
# ~10M avg across metropole + colonies × 0.04 × 400+ years > 100M) controlled
# coastal areas from ~1500s but not interior until 20th century pacification.

TIMELINES['Mozambique'] = [
    (-200000, 900, 'NO_KNOWN_POLITIES'),
    # Gap 900-1920: Portuguese Empire (>100M) controlled coastal settlements
    # from ~1500s. Interior under African polities (Mutapa, Gaza, Maravi).
    # No single polity at 99%.
    (1920, 1975, 'Portuguese Mozambique'),
    (1975, 1977, 'Mozambique'),
    (1977, 1992, 'NOT_RELEVANT'),  # Civil war; no polity with >100M controlled territory
    (1992, 2026, 'Mozambique'),
]

# =============================================================================
# ANGOLA
# =============================================================================
# Gap 1575-1920: Portuguese Empire (>100M lifetime births) controlled coastal
# areas (Luanda, Benguela). Interior kingdoms (Kongo, Matamba, Lunda, Ovimbundu)
# remained independent or semi-independent.

TIMELINES['Angola'] = [
    (-200000, 1300, 'NO_KNOWN_POLITIES'),
    (1300, 1575, 'NOT_RELEVANT'),  # Kingdom of Kongo, Ndongo — all <100M
    # Gap 1575-1920: Portuguese Empire (>100M) controlled coastal areas.
    # Interior kingdoms remained independent.
    (1920, 1975, 'Portuguese Angola'),
    (1975, 2002, 'NOT_RELEVANT'),  # Civil war; no polity with >100M controlled territory
    (2002, 2026, 'Angola'),
]

# =============================================================================
# NAMIBIA
# =============================================================================
# Gap 1915-1920: British Empire (>100M lifetime births) via South Africa
# occupied the territory after defeating Germany. League of Nations mandate
# not yet formalized.

TIMELINES['Namibia'] = [
    (-200000, 1800, 'NO_KNOWN_POLITIES'),
    (1800, 1884, 'NOT_RELEVANT'),  # Herero, Nama, Ovambo polities — all <100M
    (1884, 1915, 'German South West Africa'),
    # Gap 1915-1920: British Empire (>100M) via South Africa occupied territory.
    (1920, 1990, 'South West Africa'),
    (1990, 2026, 'Republic of Namibia'),
]

# =============================================================================
# SIERRA LEONE
# =============================================================================
# Gap 1991-2002: Civil war. RUF controlled eastern diamond regions. Nigeria
# (>100M lifetime births: ~80M avg × 0.04 × 66 years = ~211M) deployed
# ECOMOG troops and controlled parts of the territory.

TIMELINES['Sierra Leone'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1400, 1896, 'NOT_RELEVANT'),  # Temne, Mende chieftaincies — all <100M
    (1896, 1961, 'British Sierra Leone'),
    (1961, 1991, 'Sierra Leone'),
    # Gap 1991-2002: Civil war. Nigeria (>100M) deployed ECOMOG troops.
    (2002, 2026, 'Sierra Leone'),
]

# =============================================================================
# ERITREA
# =============================================================================
# Gap 1557-1890: Ottoman Empire (>100M lifetime births) controlled the coast
# (Massawa, Dahlak). Ethiopian polities controlled the highlands.
#
# Gap 1941-1952: UK (>100M lifetime births) administered under British
# military administration.
#
# Gap 1991-1993: Ethiopia (>100M lifetime births historically: Ethiopian
# Empire ~5M avg × 0.04 × 700 years = ~140M) was nominal sovereign; EPLF
# controlled de facto after defeating Ethiopian forces.

TIMELINES['Eritrea'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, 1557, 'NOT_RELEVANT'),  # D'mt, Aksum, successor states — all <100M
    # Gap 1557-1890: Ottoman Empire (>100M) on coast; Ethiopian polities
    # in highlands. No single polity at 99%.
    (1890, 1941, 'Italian Eritrea'),
    # Gap 1941-1952: UK (>100M) administered territory.
    (1952, 1962, 'Eritrea (federated with Ethiopia)'),
    (1962, 1991, 'Ethiopia'),
    # Gap 1991-1993: Ethiopia (>100M historically) nominal sovereign;
    # EPLF controlled de facto.
    (1993, 2026, 'State of Eritrea'),
]

# =============================================================================
# LIBYA
# =============================================================================
# Gap 455-534: Vandal Kingdom in Tripolitania; Byzantine Empire (>100M
# lifetime births) still held Cyrenaica.
#
# Gap 800-1551: Aghlabids, Fatimids, Hafsids, various. Fatimid Caliphate
# (>100M: ~20M avg × 0.04 × 260 years = ~208M) controlled Libya 909-~1050.
#
# Gap 1943-1951: UK (>100M) and France (>100M) administered different regions.
#
# Gap 2011-2026: Civil war. Two rival governments. Turkey (>100M: Republic
# of Turkey ~40M avg × 0.04 × 103 years = ~165M) has military presence
# supporting Tripoli-based government.

TIMELINES['Libya'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, -96, 'NOT_RELEVANT'),  # Phoenician/Greek colonies, Carthage — all <100M
    (-96, 395, 'Roman Empire'),
    (395, 455, 'Byzantine Empire'),
    # Gap 455-534: Vandals in Tripolitania; Byzantine Empire (>100M) in Cyrenaica.
    (534, 643, 'Byzantine Empire'),
    (643, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 800, 'Abbasid Caliphate'),
    # Gap 800-1551: Aghlabids, Fatimids, Hafsids, various. Fatimid Caliphate
    # (>100M) controlled Libya 909-~1050.
    (1551, 1711, 'Ottoman Empire'),
    (1711, 1835, 'Karamanli dynasty'),
    (1835, 1911, 'Ottoman Empire'),
    (1912, 1943, 'Italian Libya'),
    # Gap 1943-1951: UK (>100M) and France (>100M) administered different zones.
    (1951, 1969, 'Kingdom of Libya'),
    (1969, 2011, 'Libyan Arab Jamahiriya'),
    # Gap 2011-2026: Civil war. Turkey (>100M) has military presence.
]

# =============================================================================
# DOMINICAN REPUBLIC
# =============================================================================
# Gap 1795-1809: France (>100M lifetime births) received territory via Treaty
# of Basel. Haitian forces then occupied.
#
# Gap 1961-1966: Post-Trujillo instability. US (>100M lifetime births)
# intervened militarily in 1965.

TIMELINES['Dominican Republic'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1492, 1502, 'NOT_RELEVANT'),  # Post-contact; tiny population in transition
    (1502, 1795, 'Spanish Santo Domingo'),
    # Gap 1795-1809: France (>100M) received territory; Haitian occupation followed.
    (1809, 1821, 'Spanish Santo Domingo'),
    (1822, 1844, 'Republic of Haiti'),
    (1844, 1861, 'Dominican Republic'),
    (1861, 1865, 'Spanish Santo Domingo'),
    (1865, 1916, 'Dominican Republic'),
    (1916, 1924, 'US occupation of Dominican Republic'),
    (1924, 1930, 'Dominican Republic'),
    (1930, 1961, 'Dominican Republic (Trujillo)'),
    # Gap 1961-1966: Post-Trujillo instability. US (>100M) intervened 1965.
    (1966, 2026, 'Dominican Republic'),
]

# =============================================================================
# HAITI
# =============================================================================
# Gap 1791-1804: Haitian Revolution. France (>100M lifetime births) fought to
# retain the colony. Multiple factions (French, Spanish, British intervention).

TIMELINES['Haiti'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1492, 1697, 'NOT_RELEVANT'),  # Tiny post-Taino-collapse population; Spanish nominal control
    (1697, 1791, 'French Saint-Domingue'),
    # Gap 1791-1804: Revolution. France (>100M) fought to retain colony.
    (1804, 1806, 'Empire of Haiti'),
    (1806, 1820, 'NOT_RELEVANT'),  # Split: Kingdom in north, Republic in south; both <100M
    (1820, 1849, 'Republic of Haiti'),
    (1849, 1859, 'Second Empire of Haiti'),
    (1859, 1915, 'Republic of Haiti'),
    (1915, 1934, 'US occupation of Haiti'),
    (1934, 1957, 'Republic of Haiti'),
    (1957, 1986, 'Haiti (Duvalier)'),
    (1986, 2026, 'Republic of Haiti'),
]

# =============================================================================
# JAMAICA
# =============================================================================

TIMELINES['Jamaica'] = [
    (-200000, 1509, 'NO_KNOWN_POLITIES'),
    (1509, 1655, 'Spanish Jamaica'),
    (1655, 1962, 'British Jamaica'),
    (1962, 2026, 'Jamaica'),
]

# =============================================================================
# CONGO (REPUBLIC OF THE CONGO)
# =============================================================================
# Gap 1880-1910: France (>100M lifetime births) established protectorates via
# Brazza's treaties but hadn't consolidated colonial control over full territory.

TIMELINES['Congo'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1400, 1880, 'NOT_RELEVANT'),  # Loango, Teke, Kongo periphery — all <100M
    # Gap 1880-1910: France (>100M) establishing colonial control via treaties.
    (1910, 1960, 'French Equatorial Africa'),
    (1960, 1970, 'Republic of the Congo'),
    (1970, 1991, "People's Republic of the Congo"),
    (1991, 1997, 'Republic of the Congo'),
    (1997, 1999, 'NOT_RELEVANT'),  # Civil war; no polity >100M controlled territory
    (1999, 2026, 'Republic of the Congo'),
]

# =============================================================================
# PAPUA NEW GUINEA
# =============================================================================
# Gap 1884-1949: German Empire (>100M: ~60M avg × 0.04 × 47 years = ~113M)
# controlled northern half (German New Guinea). British Empire (>100M) controlled
# southern half (British Papua, then Australian Papua). After 1920 Australia
# administered both as legally separate territories until merger in 1949.

TIMELINES['Papua New Guinea'] = [
    (-200000, 1884, 'NO_KNOWN_POLITIES'),
    # Gap 1884-1949: German Empire (>100M) in north, British Empire (>100M)
    # in south. After 1920, Australia administered both as separate territories.
    (1949, 1975, 'Australian Papua New Guinea'),
    (1975, 2026, 'Papua New Guinea'),
]

# =============================================================================
# AUSTRALIA
# =============================================================================
# Gap 1788-1901: Six separate British colonies. British Empire (>100M lifetime
# births) sovereign over all, but through separate colonial administrations.
# No single colonial polity covered 99% of population.

TIMELINES['Australia'] = [
    (-200000, 1788, 'NO_KNOWN_POLITIES'),
    # Gap 1788-1901: British Empire (>100M) via six separate colonies.
    (1901, 2026, 'Australia'),
]

# =============================================================================
# NEW ZEALAND
# =============================================================================
# Gap 1840-1885: British Empire (>100M lifetime births) established colony but
# Maori strongholds (King Country, Te Urewera) held 3-7% of population.

TIMELINES['New Zealand'] = [
    (-200000, 1840, 'NO_KNOWN_POLITIES'),
    # Gap 1840-1885: British Empire (>100M) controlled most but Maori
    # strongholds held 3-7% of population.
    (1885, 2026, 'New Zealand'),
]

# =============================================================================
# LUXEMBOURG
# =============================================================================
# Gap 410-962: Carolingian Empire (>100M lifetime births: ~15M avg × 0.04 ×
# 200 years = ~120M) then fragmentation into Lotharingia/East Francia.
#
# Gap 1914-1918: German Empire (>100M) occupied Luxembourg.
# Gap 1940-1944: Nazi Germany (>100M) occupied/annexed Luxembourg.

TIMELINES['Luxembourg'] = [
    (-200000, -50, 'NO_KNOWN_POLITIES'),
    (-50, 410, 'Roman Empire'),
    # Gap 410-962: Carolingian Empire (>100M) then fragmentation.
    (962, 1795, 'Holy Roman Empire'),
    (1795, 1815, 'First French Empire'),
    (1815, 1839, 'United Kingdom of the Netherlands'),
    (1839, 1914, 'Grand Duchy of Luxembourg'),
    # Gap 1914-1918: German Empire (>100M) occupied.
    (1918, 1940, 'Grand Duchy of Luxembourg'),
    # Gap 1940-1944: Nazi Germany (>100M) occupied/annexed.
    (1944, 2026, 'Grand Duchy of Luxembourg'),
]

# =============================================================================
# CYPRUS
# =============================================================================
# Gap 649-965: Arab-Byzantine condominium. Byzantine Empire (>100M) and
# Umayyad/Abbasid Caliphates (>100M) both claimed control.
#
# Gap 1489-1571: Venetian Republic (borderline >100M: ~2.5M avg × 0.04 ×
# 1100 years = ~110M) controlled Cyprus. Erring toward gap.
#
# Gap 1974-2026: Turkey (>100M: ~40M avg × 0.04 × 103 years = ~165M) controls
# northern ~37% via TRNC.

TIMELINES['Cyprus'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    (-700, -545, 'NOT_RELEVANT'),  # Cypriot city-kingdoms — all <100M
    (-545, -333, 'Achaemenid Empire'),
    (-333, -58, 'NOT_RELEVANT'),  # Ptolemaic Kingdom (<100M: ~5M × 0.04 × 275 = ~55M)
    (-58, 395, 'Roman Empire'),
    (395, 649, 'Byzantine Empire'),
    # Gap 649-965: Arab-Byzantine condominium. Both Byzantine Empire (>100M)
    # and Caliphates (>100M) claimed control.
    (965, 1191, 'Byzantine Empire'),
    (1191, 1489, 'NOT_RELEVANT'),  # Lusignan Kingdom — <100M
    # Gap 1489-1571: Venetian Republic (borderline >100M) controlled Cyprus.
    (1571, 1878, 'Ottoman Empire'),
    (1878, 1960, 'British Cyprus'),
    (1960, 1974, 'Republic of Cyprus'),
    # Gap 1974-2026: Turkey (>100M) controls northern portion via TRNC.
]

# =============================================================================
# PALESTINE
# =============================================================================
# Gap 878-1291: Tulunids, Fatimids, Crusaders, Ayyubids. Fatimid Caliphate
# (>100M: ~20M avg × 0.04 × 260 years = ~208M) controlled Palestine 969-1099.
#
# Gap 1948-1994: West Bank under Jordan; Gaza under Egypt. Republic of Egypt
# (>100M: ~40M avg × 0.04 × 73 years = ~117M) controlled Gaza.

TIMELINES['Palestine'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (-1200, -539, 'NOT_RELEVANT'),  # Philistine, Israelite kingdoms — all <100M
    (-539, -333, 'Achaemenid Empire'),
    (-333, -200, 'NOT_RELEVANT'),  # Ptolemaic (<100M), brief Seleucid
    (-200, -167, 'Seleucid Empire'),
    (-167, -63, 'NOT_RELEVANT'),  # Hasmonean Kingdom — <100M
    (-63, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    # Gap 878-1291: Fatimid Caliphate (>100M) controlled 969-1099.
    # Crusaders, Ayyubids competed. No single polity at 99%.
    (1291, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1948, 'British Mandate of Palestine'),
    # Gap 1948-1994: Egypt (>100M) controlled Gaza. Jordan controlled West Bank.
    (1994, 2007, 'Palestinian National Authority'),
    (2007, 2026, 'NOT_RELEVANT'),  # Gaza/West Bank split; no polity >100M controls territory
]

# =============================================================================
# KUWAIT
# =============================================================================
# Gap 900-1534: Qarmatians, local rulers. Mongol Empire/Ilkhanate (>100M
# lifetime births: Mongol Empire ~100M+ pop × 0.04 × 60 years unified = ~240M)
# controlled this territory ~1258-1335.

TIMELINES['Kuwait'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),  # Brief post-Alexander fragmentation
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'Parthian Empire'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    # Gap 900-1534: Mongol Empire/Ilkhanate (>100M) controlled ~1258-1335.
    (1534, 1899, 'Ottoman Empire'),
    (1899, 1961, 'British protectorate of Kuwait'),
    (1961, 1990, 'State of Kuwait'),
    (1990, 1991, 'NOT_RELEVANT'),  # Iraqi invasion; Iraq as polity <100M lifetime births
    (1991, 2026, 'State of Kuwait'),
]

# =============================================================================
# UAE
# =============================================================================
# Gap 1507-1650: Portuguese Empire (>100M lifetime births) controlled Gulf
# coast forts. Interior under local tribal rulers.
#
# Gap 1820-1971: British Empire (>100M) established Trucial States system.
# Seven separate sheikhdoms under British protection — not a single polity.

TIMELINES['UAE'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'NOT_RELEVANT'),  # Parthian influence uncertain on lower Gulf coast
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1507, 'NOT_RELEVANT'),  # Local polities — all <100M
    # Gap 1507-1650: Portuguese Empire (>100M) controlled coastal forts.
    (1650, 1820, 'NOT_RELEVANT'),  # Ya'aruba/local control — all <100M
    # Gap 1820-1971: British Empire (>100M) via Trucial States system.
    (1971, 2026, 'United Arab Emirates'),
]

# =============================================================================
# QATAR
# =============================================================================
# Gap 1550-1916: Ottoman Empire (>100M lifetime births) claimed suzerainty
# (garrison 1871-1913). Portuguese Empire (>100M) controlled Gulf earlier.
# British Empire (>100M) competed for influence from 1868.

TIMELINES['Qatar'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'NOT_RELEVANT'),  # Parthian influence uncertain for Qatar peninsula
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1550, 'NOT_RELEVANT'),  # Qarmatian/local polities — all <100M
    # Gap 1550-1916: Ottoman Empire (>100M) and Portuguese then British Empires
    # (both >100M) competed for influence.
    (1916, 1971, 'British protectorate of Qatar'),
    (1971, 2026, 'State of Qatar'),
]

# =============================================================================
# BAHRAIN
# =============================================================================
# Gap 1521-1602: Portuguese Empire (>100M lifetime births) controlled Bahrain.

TIMELINES['Bahrain'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'Parthian Empire'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1521, 'NOT_RELEVANT'),  # Qarmatians, Uyunids — all <100M
    # Gap 1521-1602: Portuguese Empire (>100M) controlled Bahrain.
    (1602, 1783, 'Safavid / Afsharid Iran'),
    (1783, 1861, 'Al Khalifa Bahrain'),
    (1861, 1971, 'British protectorate of Bahrain'),
    (1971, 2026, 'Kingdom of Bahrain'),
]

# =============================================================================
# OMAN
# =============================================================================
# Gap 1507-1650: Portuguese Empire (>100M lifetime births) controlled Muscat
# and coast. Interior imamate separate.
#
# Gap 1856-1959: British Empire (>100M lifetime births) protectorate over coast.
# Interior Imamate separate (Treaty of Sib 1920 formalized division).

TIMELINES['Oman'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, 224, 'NOT_RELEVANT'),  # Hellenistic/Parthian influence minimal in Oman
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1507, 'NOT_RELEVANT'),  # Ibadi imamate, Nabhani dynasty — all <100M
    # Gap 1507-1650: Portuguese Empire (>100M) controlled Muscat and coast.
    (1650, 1749, "Ya'aruba dynasty"),
    (1749, 1856, 'Al Said dynasty'),
    # Gap 1856-1959: British Empire (>100M) protectorate over coast.
    # Interior Imamate separate.
    (1959, 2026, 'Sultanate of Oman'),
]

# =============================================================================
# KYRGYZSTAN
# =============================================================================
# Gap 640-750: Tang Dynasty (>100M lifetime births) controlled parts of Central
# Asia including Kyrgyz territory via Anxi Protectorate.
#
# Gap 1218-1370: Mongol Empire (>100M lifetime births) controlled this territory.
#
# Gap 1917-1922: Bolsheviks (Soviet Union, >100M) fighting for control during
# Russian Civil War.

TIMELINES['Kyrgyzstan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, 640, 'NOT_RELEVANT'),  # Saka, Wusun, Turkic khaganates — all <100M
    # Gap 640-750: Tang Dynasty (>100M) controlled via Anxi Protectorate.
    (750, 1218, 'NOT_RELEVANT'),  # Qarakhanids, Qara Khitai — all <100M
    # Gap 1218-1370: Mongol Empire (>100M) controlled this territory.
    (1370, 1876, 'NOT_RELEVANT'),  # Moghulistan, Kokand Khanate — all <100M
    (1876, 1917, 'Russian Empire'),
    # Gap 1917-1922: Bolsheviks (>100M) fighting for control.
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Kyrgyzstan'),
]

# =============================================================================
# TAJIKISTAN
# =============================================================================
# Gap -330 to -250: Seleucid Empire (>100M lifetime births) controlled Bactria.
#
# Gap 30-750: Multiple >100M polities at various times: Kushan Empire
# (borderline ~100M), Sassanid Empire (>100M), Tang Dynasty (>100M).
#
# Gap 1220-1370: Mongol Empire (>100M lifetime births) controlled this territory.
#
# Gap 1917-1929: Bolsheviks (Soviet Union, >100M) establishing control.
# Tajik SSR created 1929.

TIMELINES['Tajikistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    # Gap -330 to -250: Seleucid Empire (>100M) controlled Bactria.
    (-250, 30, 'NOT_RELEVANT'),  # Greco-Bactrian kingdom — <100M
    # Gap 30-750: Kushan (borderline >100M), Sassanid (>100M), Tang (>100M)
    # controlled at various times.
    (750, 820, 'Abbasid Caliphate'),
    (820, 1220, 'NOT_RELEVANT'),  # Samanids, Qarakhanids, Ghurids — all <100M
    # Gap 1220-1370: Mongol Empire (>100M) controlled this territory.
    (1370, 1929, 'NOT_RELEVANT'),  # Timurid, Shaybanid, Bukhara Khanate — all <100M
    (1929, 1991, 'Soviet Union'),
    (1991, 2026, 'Tajikistan'),
]

# =============================================================================
# TURKMENISTAN
# =============================================================================
# Gap -330 to 750: Seleucid (>100M), Parthian (>100M: ~10M avg × 0.04 × 370
# = ~148M), Sassanid (>100M), Umayyad (>100M) all controlled at various times.
#
# Gap 820-1370: Seljuk Empire (borderline >100M; Merv was their capital).
# Mongol Empire (>100M) controlled from 1220.
#
# Gap 1917-1922: Bolsheviks (>100M) fighting for control.

TIMELINES['Turkmenistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    # Gap -330 to 750: Seleucid (>100M), Parthian (>100M), Sassanid (>100M),
    # Umayyad (>100M) all controlled at various times.
    (750, 820, 'Abbasid Caliphate'),
    # Gap 820-1370: Seljuk Empire (borderline >100M; Merv was capital).
    # Mongol Empire (>100M) from 1220.
    (1370, 1884, 'NOT_RELEVANT'),  # Timurid, Turkmen tribal, Khiva — all <100M
    (1884, 1917, 'Russian Empire'),
    # Gap 1917-1922: Bolsheviks (>100M) fighting for control.
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Turkmenistan'),
]

# =============================================================================
# MOLDOVA
# =============================================================================
# Gap 106-275: Roman Empire (>100M lifetime births) controlled parts of modern
# Moldova (Trajan's Dacia extended into western Moldova).
#
# Gap 1512-1812: Ottoman Empire (>100M lifetime births) held suzerainty over
# Principality of Moldavia.
#
# Gap 1856-1878: Ottoman Empire (>100M) retained nominal suzerainty over the
# United Principalities that controlled this territory.
#
# Gap 1940-1944: Soviet Union (>100M) annexed Bessarabia 1940; Romania
# reoccupied 1941-1944 during WWII.

TIMELINES['Moldova'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    (-700, 106, 'NOT_RELEVANT'),  # Scythian, Dacian polities — all <100M
    # Gap 106-275: Roman Empire (>100M) controlled parts of western Moldova.
    (275, 1350, 'NOT_RELEVANT'),  # Migration era; successor polities all <100M
    (1350, 1512, 'NOT_RELEVANT'),  # Principality of Moldavia — <100M
    # Gap 1512-1812: Ottoman Empire (>100M) held suzerainty over Moldavia.
    (1812, 1856, 'Russian Empire'),
    # Gap 1856-1878: Ottoman Empire (>100M) nominal suzerain over territory.
    (1878, 1917, 'Russian Empire'),
    (1918, 1940, 'Romania'),
    # Gap 1940-1944: Soviet Union (>100M) annexed 1940; Romania reoccupied 1941-44.
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Moldova'),
]

# =============================================================================
# NORTH KOREA
# =============================================================================
# Gap -108 to 313: Han Dynasty (>100M lifetime births) established Lelang
# Commandery in Pyongyang area. Goguryeo controlled other portions.
#
# Gap 668-676: Tang Dynasty (>100M) controlled Pyongyang area after conquering
# Goguryeo (Protectorate General to Pacify the East).
#
# Gap 1945-1948: Soviet Union (>100M lifetime births) occupied northern Korea.

TIMELINES['North Korea'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, -108, 'NOT_RELEVANT'),  # Gojoseon/Wiman Joseon — <100M
    # Gap -108 to 313: Han Dynasty (>100M) established Lelang Commandery.
    (313, 668, 'NOT_RELEVANT'),  # Goguryeo — <100M
    # Gap 668-676: Tang Dynasty (>100M) controlled Pyongyang area.
    (676, 936, 'NOT_RELEVANT'),  # Silla/Balhae — both <100M
    (936, 1392, 'Goryeo Dynasty'),
    (1392, 1897, 'Joseon Dynasty'),
    (1897, 1910, 'Korean Empire'),
    (1910, 1945, 'Empire of Japan'),
    # Gap 1945-1948: Soviet Union (>100M) occupied northern Korea.
    (1948, 2026, "Democratic People's Republic of Korea"),
]

# =============================================================================
# SOUTH KOREA
# =============================================================================
# Gap 1945-1948: United States (>100M lifetime births) administered southern
# Korea via USAMGIK (US Army Military Government in Korea).

TIMELINES['South Korea'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, 668, 'NOT_RELEVANT'),  # Samhan, Three Kingdoms — all <100M
    (668, 935, 'Unified Silla'),
    (936, 1392, 'Goryeo Dynasty'),
    (1392, 1897, 'Joseon Dynasty'),
    (1897, 1910, 'Korean Empire'),
    (1910, 1945, 'Empire of Japan'),
    # Gap 1945-1948: United States (>100M) administered via USAMGIK.
    (1948, 2026, 'Republic of Korea'),
]
