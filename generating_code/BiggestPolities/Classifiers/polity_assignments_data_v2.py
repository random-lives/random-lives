"""
Polity assignment data: maps (modern_country, year) -> polity_name.
Merged from Opus agent outputs. 4 return values:
- polity name: single polity controlled 99%+ of country population
- 'indeterminate': polities >100M births existed but none at 99%
- 'no_known_polities': predates known polities
- 'not_relevant': all polities <100M lifetime births
"""

ASSIGNMENT = {}

ASSIGNMENT['Afghanistan'] = [
    (-200000, -2000, 'NO_KNOWN_POLITIES'),
    (-2000, -550, 'NOT_RELEVANT'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -312, 'NOT_RELEVANT'),
    (-312, -305, 'Seleucid Empire'),
    (1186, 1220, 'NOT_RELEVANT'),
    (1370, 1405, 'Timurid Empire'),
    (1507, 1510, 'NOT_RELEVANT'),
    (1747, 1896, 'NOT_RELEVANT'),
    (1896, 1973, 'Kingdom of Afghanistan'),
    (1973, 1978, 'Republic of Afghanistan'),
    (1989, 2001, 'NOT_RELEVANT'),
    (2021, 2026, 'Islamic Emirate of Afghanistan'),
]

ASSIGNMENT['Albania'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -229, 'NOT_RELEVANT'),
    (-168, 395, 'Roman Empire'),
    (395, 600, 'Byzantine Empire'),
    (1018, 1204, 'Byzantine Empire'),
    (1204, 1385, 'NOT_RELEVANT'),
    (1501, 1912, 'Ottoman Empire'),
    (1912, 1914, 'Albania'),
    (1920, 1939, 'Albania'),
    (1939, 1943, 'Kingdom of Italy'),
    (1943, 1946, 'NOT_RELEVANT'),
    (1946, 1992, "People's Socialist Republic of Albania"),
    (1992, 2026, 'Republic of Albania'),
]

ASSIGNMENT['Algeria'] = [
    (-200000, -200, 'NO_KNOWN_POLITIES'),
    (-200, -146, 'NOT_RELEVANT'),
    (-46, 429, 'Roman Empire'),
    (429, 534, 'NOT_RELEVANT'),
    (1518, 1830, 'Regency of Algiers'),
    (1848, 1962, 'French Algeria'),
    (1962, 2026, "People's Democratic Republic of Algeria"),
]

ASSIGNMENT['Angola'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1400, 1575, 'NOT_RELEVANT'),
    (1920, 1975, 'Portuguese Angola'),
    (2002, 2026, 'Republic of Angola'),
]

ASSIGNMENT['Argentina'] = [
    (-200000, 1536, 'NO_KNOWN_POLITIES'),
    (1816, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Armenia'] = [
    (-200000, -860, 'NO_KNOWN_POLITIES'),
    (-860, -590, 'Kingdom of Urartu'),
    (-590, -550, 'NOT_RELEVANT'),
    (-550, -330, 'Achaemenid Empire'),
    (-190, -1, 'Kingdom of Armenia'),
    (63, 428, 'Kingdom of Armenia'),
    (428, 654, 'Sasanian Empire'),
    (654, 750, 'Umayyad Caliphate'),
    (750, 885, 'Abbasid Caliphate'),
    (885, 1045, 'NOT_RELEVANT'),
    (1045, 1064, 'Byzantine Empire'),
    (1236, 1260, 'Mongol Empire'),
    (1260, 1335, 'Ilkhanate'),
    (1335, 1386, 'NOT_RELEVANT'),
    (1405, 1501, 'NOT_RELEVANT'),
    (1501, 1722, 'Safavid Empire'),
    (1735, 1828, 'NOT_RELEVANT'),
    (1828, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Armenia'),
]

ASSIGNMENT['Australia'] = [
    (-200000, 1788, 'NO_KNOWN_POLITIES'),
    (1901, 2026, 'Australia'),
]

ASSIGNMENT['Austria'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -15, 'NOT_RELEVANT'),
    (-15, 476, 'Roman Empire'),
    (796, 843, 'Frankish Empire'),
    (843, 962, 'NOT_RELEVANT'),
    (962, 1806, 'Holy Roman Empire'),
    (1806, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1938, 'NOT_RELEVANT'),
    (1938, 1945, 'NOT_RELEVANT'),
    (1945, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Azerbaijan'] = [
    (-200000, -850, 'NO_KNOWN_POLITIES'),
    (-850, -550, 'NOT_RELEVANT'),
    (-550, -330, 'Achaemenid Empire'),
    (-150, 224, 'Parthian Empire'),
    (224, 654, 'Sasanian Empire'),
    (654, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1050, 'NOT_RELEVANT'),
    (1236, 1260, 'Mongol Empire'),
    (1260, 1335, 'Ilkhanate'),
    (1335, 1386, 'NOT_RELEVANT'),
    (1405, 1501, 'NOT_RELEVANT'),
    (1501, 1722, 'Safavid Empire'),
    (1735, 1747, 'Afsharid Empire'),
    (1747, 1806, 'NOT_RELEVANT'),
    (1828, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Azerbaijan'),
]

ASSIGNMENT['Bahrain'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'Parthian Empire'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1521, 'NOT_RELEVANT'),
    (1602, 1783, 'Safavid / Afsharid Iran'),
    (1783, 1861, 'Al Khalifa Bahrain'),
    (1861, 1971, 'British protectorate of Bahrain'),
    (1971, 2026, 'Kingdom of Bahrain'),
]

ASSIGNMENT['Bangladesh'] = [
    (-200000, -600, 'NO_KNOWN_POLITIES'),
    (-600, -322, 'NOT_RELEVANT'),
    (1858, 1947, 'British Raj'),
    (1947, 1956, 'Dominion of Pakistan'),
    (1956, 1971, 'Islamic Republic of Pakistan'),
    (1971, 2026, "People's Republic of Bangladesh"),
]

ASSIGNMENT['Belarus'] = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    (1000, 1240, 'NOT_RELEVANT'),
    (1320, 1569, 'Grand Duchy of Lithuania'),
    (1569, 1772, 'Polish-Lithuanian Commonwealth'),
    (1795, 1915, 'Russian Empire'),
    (1939, 1941, 'Soviet Union'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Belarus'),
]

ASSIGNMENT['Belgium'] = [
    (-200000, -57, 'NO_KNOWN_POLITIES'),
    (-57, -27, 'Roman Republic'),
    (-27, 395, 'Roman Empire'),
    (395, 430, 'Western Roman Empire'),
    (430, 481, 'NOT_RELEVANT'),
    (481, 751, 'NOT_RELEVANT'),
    (751, 843, 'Carolingian Empire'),
    (843, 959, 'NOT_RELEVANT'),
    (959, 962, 'NOT_RELEVANT'),
    (1795, 1804, 'French First Republic'),
    (1804, 1815, 'First French Empire'),
    (1815, 1830, 'United Kingdom of the Netherlands'),
    (1830, 1940, 'Kingdom of Belgium'),
    (1944, 2026, 'Kingdom of Belgium'),
]

ASSIGNMENT['Benin'] = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    (1000, 1894, 'NOT_RELEVANT'),
    (1894, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Bolivia'] = [
    (-200000, 200, 'NO_KNOWN_POLITIES'),
    (200, 1538, 'NOT_RELEVANT'),
    (1538, 1825, 'Spanish Empire'),
    (1825, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Bosnia and Herzegovina'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (9, 395, 'Roman Empire'),
    (395, 476, 'Western Roman Empire'),
    (476, 535, 'NOT_RELEVANT'),
    (600, 1463, 'NOT_RELEVANT'),
    (1482, 1878, 'Ottoman Empire'),
    (1878, 1918, 'Austria-Hungary'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 1995, 'NOT_RELEVANT'),
    (1995, 2026, 'Bosnia and Herzegovina'),
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

ASSIGNMENT['Bulgaria'] = [
    (-200000, -480, 'NO_KNOWN_POLITIES'),
    (-480, -46, 'NOT_RELEVANT'),
    (-46, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),
    (681, 971, 'First Bulgarian Empire'),
    (1018, 1185, 'Byzantine Empire'),
    (1396, 1878, 'Ottoman Empire'),
    (1885, 1908, 'Principality of Bulgaria'),
    (1908, 1913, 'Kingdom of Bulgaria'),
    (1913, 1940, 'NOT_RELEVANT'),
    (1940, 1944, 'Kingdom of Bulgaria'),
    (1944, 1946, 'NOT_RELEVANT'),
    (1946, 1990, "People's Republic of Bulgaria"),
    (1990, 2026, 'Republic of Bulgaria'),
]

ASSIGNMENT['Burkina Faso'] = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    (1000, 1235, 'NOT_RELEVANT'),
    (1460, 1897, 'NOT_RELEVANT'),
    (1897, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Burundi'] = [
    (-200000, 1550, 'NO_KNOWN_POLITIES'),
    (1550, 1899, 'NOT_RELEVANT'),
    (1899, 1916, 'German Empire'),
    (1916, 1962, 'NOT_RELEVANT'),
    (1962, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Cambodia'] = [
    (-200000, 200, 'NO_KNOWN_POLITIES'),
    (200, 1870, 'NOT_RELEVANT'),
    (1870, 1940, 'French Third Republic'),
    (1945, 1979, 'NOT_RELEVANT'),
    (1989, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Cameroon'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1902, 1916, 'German Kamerun'),
    (1961, 2026, 'Republic of Cameroon'),
]

ASSIGNMENT['Canada'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    (1763, 1867, 'British North America'),
    (1949, 2026, 'Canada'),
]

ASSIGNMENT['Central African Republic'] = [
    (-200000, 1800, 'NO_KNOWN_POLITIES'),
    (1800, 1910, 'NOT_RELEVANT'),
    (1910, 1960, 'French Equatorial Africa'),
    (1960, 1976, 'Central African Republic'),
    (1976, 1979, 'Central African Empire'),
    (1979, 2013, 'Central African Republic'),
]

ASSIGNMENT['Chad'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    (1913, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Chile'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (600, 1540, 'NOT_RELEVANT'),
    (1883, 1973, 'Chile'),
    (1973, 1990, 'Military dictatorship of Chile'),
    (1990, 2026, 'Chile'),
]

ASSIGNMENT['China'] = [
    (-200000, -1600, 'NO_KNOWN_POLITIES'),
    (1279, 1368, 'Yuan Dynasty'),
    (1759, 1912, 'Qing Dynasty'),
    (1951, 2026, "People's Republic of China"),
]

ASSIGNMENT['Colombia'] = [
    (-200000, 1200, 'NO_KNOWN_POLITIES'),
    (1200, 1525, 'NOT_RELEVANT'),
    (1550, 1819, 'Spanish New Granada'),
    (1819, 1886, 'NOT_RELEVANT'),
    (1886, 2026, 'Republic of Colombia'),
]

ASSIGNMENT['Congo'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1400, 1880, 'NOT_RELEVANT'),
    (1910, 1960, 'French Equatorial Africa'),
    (1960, 1970, 'Republic of the Congo'),
    (1970, 1991, "People's Republic of the Congo"),
    (1991, 1997, 'Republic of the Congo'),
    (1997, 1999, 'NOT_RELEVANT'),
    (1999, 2026, 'Republic of the Congo'),
]

ASSIGNMENT['Costa Rica'] = [
    (-200000, 1563, 'NO_KNOWN_POLITIES'),
    (1563, 1821, 'Spanish Empire'),
    (1821, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT["Cote d'Ivoire"] = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    (1000, 1235, 'NOT_RELEVANT'),
    (1460, 1898, 'NOT_RELEVANT'),
    (1898, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Croatia'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (9, 395, 'Roman Empire'),
    (395, 476, 'Western Roman Empire'),
    (476, 535, 'NOT_RELEVANT'),
    (600, 812, 'NOT_RELEVANT'),
    (1000, 1420, 'NOT_RELEVANT'),
    (1797, 1805, 'Habsburg Monarchy'),
    (1815, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),
    (1991, 1998, 'NOT_RELEVANT'),
    (1998, 2026, 'Republic of Croatia'),
]

ASSIGNMENT['Cuba'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1515, 1898, 'Spanish Cuba'),
    (1898, 1902, 'US military occupation of Cuba'),
    (1902, 1959, 'Republic of Cuba'),
    (1959, 2026, 'Revolutionary Cuba'),
]

ASSIGNMENT['Cyprus'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    (-700, -545, 'NOT_RELEVANT'),
    (-545, -333, 'Achaemenid Empire'),
    (-333, -58, 'NOT_RELEVANT'),
    (-58, 395, 'Roman Empire'),
    (395, 649, 'Byzantine Empire'),
    (965, 1191, 'Byzantine Empire'),
    (1191, 1489, 'NOT_RELEVANT'),
    (1571, 1878, 'Ottoman Empire'),
    (1878, 1960, 'British Cyprus'),
    (1960, 1974, 'Republic of Cyprus'),
]

ASSIGNMENT['Czechia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (600, 805, 'NOT_RELEVANT'),
    (1029, 1806, 'Holy Roman Empire'),
    (1806, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1938, 'NOT_RELEVANT'),
    (1938, 1945, 'NOT_RELEVANT'),
    (1945, 1993, 'NOT_RELEVANT'),
    (1993, 2026, 'NOT_RELEVANT'),
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

ASSIGNMENT['Denmark'] = [
    (-200000, 700, 'NO_KNOWN_POLITIES'),
    (960, 2026, 'Kingdom of Denmark'),
]

ASSIGNMENT['Dominican Republic'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1492, 1502, 'NOT_RELEVANT'),
    (1502, 1795, 'Spanish Santo Domingo'),
    (1809, 1821, 'Spanish Santo Domingo'),
    (1822, 1844, 'Republic of Haiti'),
    (1844, 1861, 'Dominican Republic'),
    (1861, 1865, 'Spanish Santo Domingo'),
    (1865, 1916, 'Dominican Republic'),
    (1916, 1924, 'US occupation of Dominican Republic'),
    (1924, 1930, 'Dominican Republic'),
    (1930, 1961, 'Dominican Republic (Trujillo)'),
    (1966, 2026, 'Dominican Republic'),
]

ASSIGNMENT['Ecuador'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (600, 1534, 'NOT_RELEVANT'),
    (1534, 1822, 'Spanish Ecuador'),
    (1822, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Egypt'] = [
    (-200000, -3100, 'NO_KNOWN_POLITIES'),
    (-3100, -525, 'NOT_RELEVANT'),
    (-525, -404, 'Achaemenid Empire'),
    (-404, -343, 'NOT_RELEVANT'),
    (-343, -332, 'Achaemenid Empire'),
    (-332, -30, 'NOT_RELEVANT'),
    (-30, 395, 'Roman Empire'),
    (395, 619, 'Byzantine Empire'),
    (619, 629, 'Sassanid Empire'),
    (629, 641, 'Byzantine Empire'),
    (641, 661, 'NOT_RELEVANT'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 868, 'Abbasid Caliphate'),
    (868, 905, 'NOT_RELEVANT'),
    (905, 935, 'Abbasid Caliphate'),
    (935, 969, 'NOT_RELEVANT'),
    (969, 1171, 'Fatimid Caliphate'),
    (1171, 1250, 'NOT_RELEVANT'),
    (1250, 1517, 'Mamluk Sultanate'),
    (1517, 1798, 'Ottoman Empire'),
    (1914, 1922, 'British Empire'),
    (1922, 1953, 'Kingdom of Egypt'),
    (1953, 2026, 'Republic of Egypt'),
]

ASSIGNMENT['El Salvador'] = [
    (-200000, 250, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1841, 'Federal Republic of Central America'),
    (1841, 2026, 'El Salvador'),
]

ASSIGNMENT['Eritrea'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, 1557, 'NOT_RELEVANT'),
    (1890, 1941, 'Italian Eritrea'),
    (1952, 1962, 'Eritrea (federated with Ethiopia)'),
    (1962, 1991, 'Ethiopia'),
    (1993, 2026, 'State of Eritrea'),
]

ASSIGNMENT['Estonia'] = [
    (-200000, 1227, 'NO_KNOWN_POLITIES'),
    (1227, 1710, 'NOT_RELEVANT'),
    (1710, 1721, 'Tsardom of Russia'),
    (1721, 1917, 'Russian Empire'),
    (1920, 1940, 'NOT_RELEVANT'),
    (1940, 1941, 'Soviet Union'),
    (1941, 1944, 'Nazi Germany'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Ethiopia'] = [
    (-200000, -900, 'NO_KNOWN_POLITIES'),
    (1890, 1936, 'Ethiopian Empire'),
    (1941, 1974, 'Ethiopian Empire'),
    (1974, 1987, 'Provisional Military Government of Socialist Ethiopia'),
    (1987, 1991, "People's Democratic Republic of Ethiopia"),
    (1991, 2026, 'Federal Democratic Republic of Ethiopia'),
]

ASSIGNMENT['Finland'] = [
    (-200000, 1250, 'NO_KNOWN_POLITIES'),
    (1250, 1809, 'NOT_RELEVANT'),
    (1809, 1917, 'Russian Empire'),
    (1917, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['France'] = [
    (-200000, -121, 'NO_KNOWN_POLITIES'),
    (-50, -27, 'Roman Republic'),
    (-27, 395, 'Roman Empire'),
    (395, 418, 'Western Roman Empire'),
    (418, 486, 'NOT_RELEVANT'),
    (486, 534, 'NOT_RELEVANT'),
    (534, 561, 'NOT_RELEVANT'),
    (561, 751, 'NOT_RELEVANT'),
    (751, 843, 'Carolingian Empire'),
    (1491, 1792, 'Kingdom of France'),
    (1792, 1804, 'French First Republic'),
    (1804, 1815, 'First French Empire'),
    (1815, 1830, 'Bourbon Restoration'),
    (1830, 1848, 'July Monarchy'),
    (1848, 1852, 'French Second Republic'),
    (1852, 1870, 'Second French Empire'),
    (1870, 1871, 'French Third Republic'),
    (1918, 1940, 'French Third Republic'),
    (1944, 1946, 'Provisional Government of the French Republic'),
    (1946, 1958, 'French Fourth Republic'),
    (1958, 2026, 'French Fifth Republic'),
]

ASSIGNMENT['Georgia'] = [
    (-200000, -600, 'NO_KNOWN_POLITIES'),
    (-600, -550, 'NOT_RELEVANT'),
    (1008, 1236, 'Kingdom of Georgia'),
    (1236, 1260, 'Mongol Empire'),
    (1260, 1335, 'Ilkhanate'),
    (1335, 1386, 'NOT_RELEVANT'),
    (1405, 1510, 'NOT_RELEVANT'),
    (1878, 1917, 'Russian Empire'),
    (1918, 1921, 'NOT_RELEVANT'),
    (1922, 1991, 'Soviet Union'),
    (1991, 1993, 'Georgia'),
]

ASSIGNMENT['Germany'] = [
    (-200000, -12, 'NO_KNOWN_POLITIES'),
    (410, 750, 'NOT_RELEVANT'),
    (800, 843, 'Carolingian Empire'),
    (843, 962, 'NOT_RELEVANT'),
    (962, 1806, 'Holy Roman Empire'),
    (1871, 1918, 'German Empire'),
    (1918, 1933, 'Weimar Republic'),
    (1933, 1945, 'Nazi Germany'),
    (1990, 2026, 'Federal Republic of Germany'),
]

ASSIGNMENT['Ghana'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1902, 1957, 'Gold Coast'),
    (1957, 1960, 'Ghana'),
    (1960, 2026, 'Republic of Ghana'),
]

ASSIGNMENT['Greece'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, -512, 'NOT_RELEVANT'),
    (-479, -200, 'NOT_RELEVANT'),
    (-146, -27, 'Roman Republic'),
    (-27, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),
    (800, 1204, 'Byzantine Empire'),
    (1947, 1967, 'Kingdom of Greece'),
    (1967, 1974, 'Greek military junta'),
    (1974, 2026, 'Hellenic Republic'),
]

ASSIGNMENT['Guatemala'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1841, 'Federal Republic of Central America'),
    (1841, 2026, 'Guatemala'),
]

ASSIGNMENT['Guinea'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    (500, 1235, 'NOT_RELEVANT'),
    (1460, 1893, 'NOT_RELEVANT'),
    (1893, 1940, 'French Third Republic'),
    (1940, 1958, 'NOT_RELEVANT'),
    (1958, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Haiti'] = [
    (-200000, 1492, 'NO_KNOWN_POLITIES'),
    (1492, 1697, 'NOT_RELEVANT'),
    (1697, 1791, 'French Saint-Domingue'),
    (1804, 1806, 'Empire of Haiti'),
    (1806, 1820, 'NOT_RELEVANT'),
    (1820, 1849, 'Republic of Haiti'),
    (1849, 1859, 'Second Empire of Haiti'),
    (1859, 1915, 'Republic of Haiti'),
    (1915, 1934, 'US occupation of Haiti'),
    (1934, 1957, 'Republic of Haiti'),
    (1957, 1986, 'Haiti (Duvalier)'),
    (1986, 2026, 'Republic of Haiti'),
]

ASSIGNMENT['Honduras'] = [
    (-200000, 250, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1841, 'Federal Republic of Central America'),
    (1841, 2026, 'Honduras'),
]

ASSIGNMENT['Hong Kong'] = [
    (-200000, -214, 'NO_KNOWN_POLITIES'),
    (-214, -206, 'Qin Dynasty'),
    (-206, -111, 'NOT_RELEVANT'),
    (-111, 9, 'Western Han Dynasty'),
    (9, 23, 'Xin Dynasty'),
    (23, 220, 'Eastern Han Dynasty'),
    (220, 280, 'NOT_RELEVANT'),
    (280, 316, 'Western Jin Dynasty'),
    (316, 589, 'NOT_RELEVANT'),
    (589, 618, 'Sui Dynasty'),
    (618, 907, 'Tang Dynasty'),
    (907, 971, 'NOT_RELEVANT'),
    (971, 1127, 'Song Dynasty'),
    (1127, 1279, 'Southern Song Dynasty'),
    (1279, 1368, 'Yuan Dynasty'),
    (1368, 1644, 'Ming Dynasty'),
    (1644, 1842, 'Qing Dynasty'),
    (1898, 1941, 'British Hong Kong'),
    (1941, 1945, 'Empire of Japan'),
    (1945, 1997, 'British Hong Kong'),
    (1997, 2026, "People's Republic of China"),
]

ASSIGNMENT['Hungary'] = [
    (-200000, -100, 'NO_KNOWN_POLITIES'),
    (-100, -9, 'NOT_RELEVANT'),
    (433, 796, 'NOT_RELEVANT'),
    (895, 1000, 'NOT_RELEVANT'),
    (1000, 1526, 'Kingdom of Hungary'),
    (1699, 1804, 'Habsburg Empire'),
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1920, 'NOT_RELEVANT'),
    (1920, 1944, 'Kingdom of Hungary'),
    (1946, 1949, 'Second Hungarian Republic'),
    (1949, 1989, "Hungarian People's Republic"),
    (1989, 2026, 'Hungary'),
]

ASSIGNMENT['Iceland'] = [
    (-200000, 1262, 'NO_KNOWN_POLITIES'),
    (1262, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['India'] = [
    (-200000, -2600, 'NO_KNOWN_POLITIES'),
    (-2600, -322, 'NOT_RELEVANT'),
    (1858, 1947, 'British Raj'),
    (1947, 1950, 'Dominion of India'),
    (1950, 2026, 'Republic of India'),
]

ASSIGNMENT['Indonesia'] = [
    (-200000, 400, 'NO_KNOWN_POLITIES'),
    (400, 1800, 'NOT_RELEVANT'),
    (1830, 1942, 'Kingdom of the Netherlands'),
    (1942, 1945, 'Empire of Japan'),
    (1949, 2026, 'Republic of Indonesia'),
]

ASSIGNMENT['Iran'] = [
    (-200000, -2700, 'NO_KNOWN_POLITIES'),
    (-2700, -550, 'NOT_RELEVANT'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'Macedonian Empire'),
    (-311, -247, 'Seleucid Empire'),
    (-141, 224, 'Parthian Empire'),
    (224, 651, 'Sassanid Empire'),
    (651, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 821, 'Abbasid Caliphate'),
    (1231, 1335, 'Mongol Empire'),
    (1335, 1501, 'NOT_RELEVANT'),
    (1501, 1722, 'Safavid Empire'),
    (1736, 1747, 'Afsharid dynasty'),
    (1747, 1796, 'NOT_RELEVANT'),
    (1796, 1925, 'Qajar dynasty'),
    (1925, 1979, 'Pahlavi dynasty'),
    (1979, 2026, 'Islamic Republic of Iran'),
]

ASSIGNMENT['Iraq'] = [
    (-200000, -3000, 'NO_KNOWN_POLITIES'),
    (-3000, -550, 'NOT_RELEVANT'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'Macedonian Empire'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'Parthian Empire'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 946, 'Abbasid Caliphate'),
    (946, 1055, 'Buyid Confederacy'),
    (1258, 1335, 'Mongol Empire'),
    (1335, 1534, 'NOT_RELEVANT'),
    (1534, 1623, 'Ottoman Empire'),
    (1638, 1920, 'Ottoman Empire'),
    (1920, 1932, 'British Mandate of Mesopotamia'),
    (1932, 1958, 'Kingdom of Iraq'),
    (1958, 2026, 'Republic of Iraq'),
]

ASSIGNMENT['Ireland'] = [
    (-200000, 1170, 'NO_KNOWN_POLITIES'),
    (1607, 1801, 'Kingdom of Ireland'),
    (1801, 1922, 'United Kingdom of Great Britain and Ireland'),
    (1922, 1937, 'Irish Free State'),
    (1937, 1949, 'Ireland (Eire)'),
    (1949, 2026, 'Republic of Ireland'),
]

ASSIGNMENT['Israel'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (-1200, -740, 'NOT_RELEVANT'),
    (-612, -539, 'NOT_RELEVANT'),
    (-539, -332, 'Achaemenid Empire'),
    (-332, -301, 'NOT_RELEVANT'),
    (-301, -200, 'NOT_RELEVANT'),
    (-200, -167, 'Seleucid Empire'),
    (-63, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'NOT_RELEVANT'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    (878, 905, 'NOT_RELEVANT'),
    (905, 935, 'Abbasid Caliphate'),
    (935, 969, 'NOT_RELEVANT'),
    (969, 1073, 'Fatimid Caliphate'),
    (1153, 1250, 'NOT_RELEVANT'),
    (1291, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1948, 'British Empire'),
    (1948, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Italy'] = [
    (-200000, -900, 'NO_KNOWN_POLITIES'),
    (-264, -27, 'Roman Republic'),
    (-27, 476, 'Roman Empire'),
    (493, 535, 'NOT_RELEVANT'),
    (553, 568, 'Byzantine Empire'),
    (1870, 1943, 'Kingdom of Italy'),
    (1946, 2026, 'Italian Republic'),
]

ASSIGNMENT['Jamaica'] = [
    (-200000, 1509, 'NO_KNOWN_POLITIES'),
    (1509, 1655, 'Spanish Jamaica'),
    (1655, 1962, 'British Jamaica'),
    (1962, 2026, 'Jamaica'),
]

ASSIGNMENT['Japan'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    (300, 710, 'NOT_RELEVANT'),
    (710, 794, 'Nara Period'),
    (794, 1185, 'Heian Period'),
    (1185, 1333, 'Kamakura Shogunate'),
    (1333, 1336, 'Kenmu Restoration'),
    (1336, 1467, 'Muromachi Shogunate'),
    (1590, 1603, 'Toyotomi Regime'),
    (1603, 1868, 'Tokugawa Shogunate'),
    (1868, 1947, 'Empire of Japan'),
    (1947, 2026, 'Japan'),
]

ASSIGNMENT['Jordan'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (-1200, -740, 'NOT_RELEVANT'),
    (-612, -539, 'NOT_RELEVANT'),
    (-539, -332, 'Achaemenid Empire'),
    (-332, -301, 'NOT_RELEVANT'),
    (-301, -200, 'NOT_RELEVANT'),
    (-200, -167, 'Seleucid Empire'),
    (106, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'NOT_RELEVANT'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 969, 'Abbasid Caliphate'),
    (969, 1099, 'Fatimid Caliphate'),
    (1099, 1250, 'NOT_RELEVANT'),
    (1250, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1921, 1946, 'British Empire'),
    (1946, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Kazakhstan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, 1220, 'NOT_RELEVANT'),
    (1220, 1260, 'Mongol Empire'),
    (1260, 1731, 'NOT_RELEVANT'),
    (1876, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Kazakhstan'),
]

ASSIGNMENT['Kenya'] = [
    (-200000, 1895, 'NO_KNOWN_POLITIES'),
    (1920, 1963, 'Colony and Protectorate of Kenya'),
    (1963, 1964, 'Kenya'),
    (1964, 2026, 'Republic of Kenya'),
]

ASSIGNMENT['Kuwait'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'Parthian Empire'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (1534, 1899, 'Ottoman Empire'),
    (1899, 1961, 'British protectorate of Kuwait'),
    (1961, 1990, 'State of Kuwait'),
    (1990, 1991, 'NOT_RELEVANT'),
    (1991, 2026, 'State of Kuwait'),
]

ASSIGNMENT['Kyrgyzstan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, 640, 'NOT_RELEVANT'),
    (750, 1218, 'NOT_RELEVANT'),
    (1370, 1876, 'NOT_RELEVANT'),
    (1876, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Kyrgyzstan'),
]

ASSIGNMENT['Laos'] = [
    (-200000, 1354, 'NO_KNOWN_POLITIES'),
    (1354, 1707, 'Lan Xang'),
    (1707, 1893, 'NOT_RELEVANT'),
    (1893, 1941, 'French Third Republic'),
    (1946, 1953, 'French Fourth Republic'),
    (1953, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Latvia'] = [
    (-200000, 1227, 'NO_KNOWN_POLITIES'),
    (1227, 1710, 'NOT_RELEVANT'),
    (1795, 1917, 'Russian Empire'),
    (1920, 1940, 'NOT_RELEVANT'),
    (1940, 1941, 'Soviet Union'),
    (1941, 1944, 'Nazi Germany'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Lebanon'] = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    (-1500, -550, 'NOT_RELEVANT'),
    (-550, -334, 'Achaemenid Empire'),
    (-200, -64, 'Seleucid Empire'),
    (-64, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    (1300, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1943, 'French Mandate of Lebanon'),
    (1943, 1975, 'Republic of Lebanon'),
    (1975, 1990, 'NOT_RELEVANT'),
    (1990, 2026, 'Republic of Lebanon'),
]

ASSIGNMENT['Liberia'] = [
    (-200000, 1822, 'NO_KNOWN_POLITIES'),
    (1822, 1926, 'NOT_RELEVANT'),
    (1926, 1980, 'Republic of Liberia'),
    (1980, 1989, 'Liberia (Doe)'),
    (2003, 2026, 'Republic of Liberia'),
]

ASSIGNMENT['Libya'] = [
    (-200000, -800, 'NO_KNOWN_POLITIES'),
    (-800, -96, 'NOT_RELEVANT'),
    (-96, 395, 'Roman Empire'),
    (395, 455, 'Byzantine Empire'),
    (534, 643, 'Byzantine Empire'),
    (643, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 800, 'Abbasid Caliphate'),
    (1551, 1711, 'Ottoman Empire'),
    (1711, 1835, 'Karamanli dynasty'),
    (1835, 1911, 'Ottoman Empire'),
    (1912, 1943, 'Italian Libya'),
    (1951, 1969, 'Kingdom of Libya'),
    (1969, 2011, 'Libyan Arab Jamahiriya'),
]

ASSIGNMENT['Lithuania'] = [
    (-200000, 1236, 'NO_KNOWN_POLITIES'),
    (1236, 1795, 'NOT_RELEVANT'),
    (1795, 1917, 'Russian Empire'),
    (1920, 1940, 'NOT_RELEVANT'),
    (1940, 1941, 'Soviet Union'),
    (1941, 1944, 'Nazi Germany'),
    (1944, 1990, 'Soviet Union'),
    (1990, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Luxembourg'] = [
    (-200000, -50, 'NO_KNOWN_POLITIES'),
    (-50, 410, 'Roman Empire'),
    (962, 1795, 'Holy Roman Empire'),
    (1795, 1815, 'First French Empire'),
    (1815, 1839, 'United Kingdom of the Netherlands'),
    (1839, 1914, 'Grand Duchy of Luxembourg'),
    (1918, 1940, 'Grand Duchy of Luxembourg'),
    (1944, 2026, 'Grand Duchy of Luxembourg'),
]

ASSIGNMENT['Madagascar'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    (800, 1897, 'NOT_RELEVANT'),
    (1897, 1960, 'French Madagascar'),
    (1960, 2026, 'Madagascar'),
]

ASSIGNMENT['Malawi'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1500, 1891, 'NOT_RELEVANT'),
    (1891, 1953, 'British Central Africa / Nyasaland'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    (1964, 2026, 'Malawi'),
]

ASSIGNMENT['Malaysia'] = [
    (-200000, 200, 'NO_KNOWN_POLITIES'),
    (200, 1511, 'NOT_RELEVANT'),
    (1914, 1942, 'British Empire'),
    (1945, 1957, 'British Empire'),
    (1963, 2026, 'Malaysia'),
]

ASSIGNMENT['Mali'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    (300, 1235, 'NOT_RELEVANT'),
    (1460, 1893, 'NOT_RELEVANT'),
    (1893, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Mauritania'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    (300, 1235, 'NOT_RELEVANT'),
    (1460, 1905, 'NOT_RELEVANT'),
    (1905, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
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
    (1855, 1857, 'NOT_RELEVANT'),
    (1857, 1863, 'Liberal Republic of Mexico'),
    (1867, 1876, 'Restored Republic'),
    (1876, 1911, 'Porfiriato'),
    (1920, 2026, 'Mexico'),
]

ASSIGNMENT['Moldova'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    (-700, 106, 'NOT_RELEVANT'),
    (275, 1350, 'NOT_RELEVANT'),
    (1350, 1512, 'NOT_RELEVANT'),
    (1812, 1856, 'Russian Empire'),
    (1878, 1917, 'Russian Empire'),
    (1918, 1940, 'Romania'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Moldova'),
]

ASSIGNMENT['Mongolia'] = [
    (-200000, -209, 'NO_KNOWN_POLITIES'),
    (-209, 630, 'NOT_RELEVANT'),
    (682, 1206, 'NOT_RELEVANT'),
    (1206, 1368, 'Mongol Empire'),
    (1368, 1691, 'NOT_RELEVANT'),
    (1691, 1911, 'Qing Dynasty'),
    (1911, 1919, 'Bogd Khanate of Mongolia'),
    (1924, 1992, "Mongolian People's Republic"),
    (1992, 2026, 'Mongolia'),
]

ASSIGNMENT['Montenegro'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, -229, 'NOT_RELEVANT'),
    (-168, 395, 'Roman Empire'),
    (395, 600, 'Byzantine Empire'),
    (1186, 1217, 'Grand Principality of Serbia'),
    (1217, 1346, 'Kingdom of Serbia'),
    (1346, 1371, 'Serbian Empire'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1941, 1943, 'Kingdom of Italy'),
    (1943, 1945, 'NOT_RELEVANT'),
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 2006, 'Federal Republic of Yugoslavia'),
    (2006, 2026, 'Montenegro'),
]

ASSIGNMENT['Morocco'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -33, 'NOT_RELEVANT'),
    (429, 682, 'NOT_RELEVANT'),
    (1070, 1147, 'Almoravid Empire'),
    (1147, 1269, 'Almohad Caliphate'),
    (1631, 1912, 'Alaouite dynasty'),
    (1956, 2026, 'Kingdom of Morocco'),
]

ASSIGNMENT['Mozambique'] = [
    (-200000, 900, 'NO_KNOWN_POLITIES'),
    (1920, 1975, 'Portuguese Mozambique'),
    (1975, 1977, 'Mozambique'),
    (1977, 1992, 'NOT_RELEVANT'),
    (1992, 2026, 'Mozambique'),
]

ASSIGNMENT['Myanmar'] = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (-500, 1287, 'NOT_RELEVANT'),
    (1555, 1599, 'Toungoo Empire'),
    (1599, 1752, 'NOT_RELEVANT'),
    (1752, 1824, 'Konbaung Dynasty'),
    (1886, 1942, 'British Empire'),
    (1945, 1948, 'British Empire'),
    (1948, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Namibia'] = [
    (-200000, 1800, 'NO_KNOWN_POLITIES'),
    (1800, 1884, 'NOT_RELEVANT'),
    (1884, 1915, 'German South West Africa'),
    (1920, 1990, 'South West Africa'),
    (1990, 2026, 'Republic of Namibia'),
]

ASSIGNMENT['Nepal'] = [
    (-200000, -322, 'NO_KNOWN_POLITIES'),
    (-185, 320, 'NOT_RELEVANT'),
    (550, 1790, 'NOT_RELEVANT'),
    (1790, 2008, 'Kingdom of Nepal'),
    (2008, 2026, 'Federal Democratic Republic of Nepal'),
]

ASSIGNMENT['Netherlands'] = [
    (-200000, -12, 'NO_KNOWN_POLITIES'),
    (410, 734, 'NOT_RELEVANT'),
    (734, 843, 'Carolingian Empire'),
    (843, 925, 'NOT_RELEVANT'),
    (925, 962, 'NOT_RELEVANT'),
    (962, 1581, 'Holy Roman Empire'),
    (1648, 1795, 'NOT_RELEVANT'),
    (1810, 1813, 'First French Empire'),
    (1813, 1815, 'NOT_RELEVANT'),
    (1815, 1830, 'United Kingdom of the Netherlands'),
    (1830, 1839, 'NOT_RELEVANT'),
    (1839, 1940, 'Kingdom of the Netherlands'),
    (1945, 2026, 'Kingdom of the Netherlands'),
]

ASSIGNMENT['New Zealand'] = [
    (-200000, 1840, 'NO_KNOWN_POLITIES'),
    (1885, 2026, 'New Zealand'),
]

ASSIGNMENT['Nicaragua'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1540, 1821, 'Spanish Guatemala'),
    (1822, 1823, 'First Mexican Empire'),
    (1823, 1838, 'Federal Republic of Central America'),
    (1838, 2026, 'Nicaragua'),
]

ASSIGNMENT['Niger'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    (300, 800, 'NOT_RELEVANT'),
    (1900, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Nigeria'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    (1914, 1960, 'Colony and Protectorate of Nigeria'),
    (1960, 1963, 'Federation of Nigeria'),
    (1963, 2026, 'Federal Republic of Nigeria'),
]

ASSIGNMENT['North Korea'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, -108, 'NOT_RELEVANT'),
    (313, 668, 'NOT_RELEVANT'),
    (676, 936, 'NOT_RELEVANT'),
    (936, 1392, 'Goryeo Dynasty'),
    (1392, 1897, 'Joseon Dynasty'),
    (1897, 1910, 'Korean Empire'),
    (1910, 1945, 'Empire of Japan'),
    (1948, 2026, "Democratic People's Republic of Korea"),
]

ASSIGNMENT['North Macedonia'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -340, 'NOT_RELEVANT'),
    (-340, -168, 'Kingdom of Macedon'),
    (-168, 395, 'Roman Empire'),
    (395, 600, 'Byzantine Empire'),
    (850, 1018, 'First Bulgarian Empire'),
    (1018, 1185, 'Byzantine Empire'),
    (1282, 1346, 'Kingdom of Serbia'),
    (1346, 1371, 'Serbian Empire'),
    (1395, 1912, 'Ottoman Empire'),
    (1913, 1915, 'Kingdom of Serbia'),
    (1915, 1918, 'NOT_RELEVANT'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),
    (1991, 2026, 'Republic of North Macedonia'),
]

ASSIGNMENT['Norway'] = [
    (-200000, 872, 'NO_KNOWN_POLITIES'),
    (1537, 1814, 'Denmark-Norway'),
    (1814, 1905, 'United Kingdoms of Sweden and Norway'),
    (1905, 2026, 'Kingdom of Norway'),
]

ASSIGNMENT['Oman'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, 224, 'NOT_RELEVANT'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1507, 'NOT_RELEVANT'),
    (1650, 1749, "Ya'aruba dynasty"),
    (1749, 1856, 'Al Said dynasty'),
    (1959, 2026, 'Sultanate of Oman'),
]

ASSIGNMENT['Pakistan'] = [
    (-200000, -2600, 'NO_KNOWN_POLITIES'),
    (-2600, -520, 'NOT_RELEVANT'),
    (1858, 1947, 'British Raj'),
    (1947, 1956, 'Dominion of Pakistan'),
    (1956, 2026, 'Islamic Republic of Pakistan'),
]

ASSIGNMENT['Palestine'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (-1200, -539, 'NOT_RELEVANT'),
    (-539, -333, 'Achaemenid Empire'),
    (-333, -200, 'NOT_RELEVANT'),
    (-200, -167, 'Seleucid Empire'),
    (-167, -63, 'NOT_RELEVANT'),
    (-63, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    (1291, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1948, 'British Mandate of Palestine'),
    (1994, 2007, 'Palestinian National Authority'),
    (2007, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Panama'] = [
    (-200000, 1510, 'NO_KNOWN_POLITIES'),
    (1510, 1821, 'Spanish Empire'),
    (1821, 1886, 'NOT_RELEVANT'),
    (1886, 1903, 'Republic of Colombia'),
    (1903, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Papua New Guinea'] = [
    (-200000, 1884, 'NO_KNOWN_POLITIES'),
    (1949, 1975, 'Australian Papua New Guinea'),
    (1975, 2026, 'Papua New Guinea'),
]

ASSIGNMENT['Paraguay'] = [
    (-200000, 1537, 'NO_KNOWN_POLITIES'),
    (1537, 1811, 'Spanish Empire'),
    (1811, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Peru'] = [
    (-200000, -200, 'NO_KNOWN_POLITIES'),
    (-200, 1532, 'NOT_RELEVANT'),
    (1542, 1821, 'Spanish Peru'),
    (1824, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Philippines'] = [
    (-200000, 900, 'NO_KNOWN_POLITIES'),
    (900, 1565, 'NOT_RELEVANT'),
    (1902, 1942, 'United States of America'),
    (1945, 1946, 'United States of America'),
    (1946, 2026, 'Republic of the Philippines'),
]

ASSIGNMENT['Poland'] = [
    (-200000, 960, 'NO_KNOWN_POLITIES'),
    (960, 1181, 'NOT_RELEVANT'),
    (1945, 1952, 'Provisional Government of Poland'),
    (1952, 1989, "Polish People's Republic"),
    (1989, 2026, 'Republic of Poland'),
]

ASSIGNMENT['Portugal'] = [
    (-200000, -220, 'NO_KNOWN_POLITIES'),
    (-138, -27, 'Roman Republic'),
    (-27, 410, 'Roman Empire'),
    (410, 585, 'NOT_RELEVANT'),
    (585, 711, 'NOT_RELEVANT'),
    (711, 750, 'Umayyad Caliphate'),
    (750, 1139, 'NOT_RELEVANT'),
    (1139, 1249, 'NOT_RELEVANT'),
    (1249, 1580, 'Kingdom of Portugal'),
    (1580, 1640, 'Iberian Union'),
    (1640, 1910, 'Kingdom of Portugal'),
    (1910, 1926, 'Portuguese First Republic'),
    (1926, 1933, 'Ditadura Nacional'),
    (1933, 1974, 'Estado Novo'),
    (1974, 2026, 'Portuguese Third Republic'),
]

ASSIGNMENT['Qatar'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'NOT_RELEVANT'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1550, 'NOT_RELEVANT'),
    (1916, 1971, 'British protectorate of Qatar'),
    (1971, 2026, 'State of Qatar'),
]

ASSIGNMENT['Romania'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, -46, 'NOT_RELEVANT'),
    (681, 1018, 'NOT_RELEVANT'),
    (1185, 1396, 'NOT_RELEVANT'),
    (1918, 1940, 'Kingdom of Romania'),
    (1940, 1945, 'NOT_RELEVANT'),
    (1945, 1947, 'Kingdom of Romania'),
    (1947, 1965, "Romanian People's Republic"),
    (1965, 1989, 'Socialist Republic of Romania'),
    (1989, 2026, 'Romania'),
]

ASSIGNMENT['Russia'] = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (-500, -63, 'NOT_RELEVANT'),
    (1828, 1917, 'Russian Empire'),
    (1917, 1922, 'NOT_RELEVANT'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Russian Federation'),
]

ASSIGNMENT['Rwanda'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1400, 1898, 'NOT_RELEVANT'),
    (1898, 1916, 'German Empire'),
    (1916, 1962, 'NOT_RELEVANT'),
    (1962, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Saudi Arabia'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-330, 106, 'NOT_RELEVANT'),
    (632, 661, 'NOT_RELEVANT'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 969, 'NOT_RELEVANT'),
    (1073, 1250, 'NOT_RELEVANT'),
    (1925, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Senegal'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    (300, 1235, 'NOT_RELEVANT'),
    (1460, 1895, 'NOT_RELEVANT'),
    (1895, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Serbia'] = [
    (-200000, -200, 'NO_KNOWN_POLITIES'),
    (-200, -29, 'NOT_RELEVANT'),
    (-29, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),
    (1521, 1699, 'Ottoman Empire'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1941, 1945, 'NOT_RELEVANT'),
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 2003, 'Federal Republic of Yugoslavia'),
    (2003, 2006, 'State Union of Serbia and Montenegro'),
    (2006, 2026, 'Republic of Serbia'),
]

ASSIGNMENT['Sierra Leone'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    (1400, 1896, 'NOT_RELEVANT'),
    (1896, 1961, 'British Sierra Leone'),
    (1961, 1991, 'Sierra Leone'),
    (2002, 2026, 'Sierra Leone'),
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

ASSIGNMENT['Slovakia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (600, 1000, 'NOT_RELEVANT'),
    (1000, 1526, 'Kingdom of Hungary'),
    (1699, 1804, 'Habsburg Monarchy'),
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1938, 'NOT_RELEVANT'),
    (1938, 1945, 'NOT_RELEVANT'),
    (1945, 1993, 'NOT_RELEVANT'),
    (1993, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Slovenia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    (962, 1804, 'Holy Roman Empire'),
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    (1918, 1941, 'Kingdom of Yugoslavia'),
    (1945, 1991, 'Socialist Federal Republic of Yugoslavia'),
    (1991, 2026, 'Republic of Slovenia'),
]

ASSIGNMENT['Somalia'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    (800, 1889, 'NOT_RELEVANT'),
    (1941, 1950, 'British Empire'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['South Africa'] = [
    (-200000, 1750, 'NO_KNOWN_POLITIES'),
    (1750, 1806, 'NOT_RELEVANT'),
    (1910, 1961, 'Union of South Africa'),
    (1961, 1994, 'Republic of South Africa'),
    (1994, 2026, 'Republic of South Africa'),
]

ASSIGNMENT['South Korea'] = [
    (-200000, -300, 'NO_KNOWN_POLITIES'),
    (-300, 668, 'NOT_RELEVANT'),
    (668, 935, 'Unified Silla'),
    (936, 1392, 'Goryeo Dynasty'),
    (1392, 1897, 'Joseon Dynasty'),
    (1897, 1910, 'Korean Empire'),
    (1910, 1945, 'Empire of Japan'),
    (1948, 2026, 'Republic of Korea'),
]

ASSIGNMENT['South Sudan'] = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    (-1500, 1821, 'NOT_RELEVANT'),
    (1899, 1956, 'Anglo-Egyptian Sudan'),
    (1956, 2011, 'Sudan'),
    (2011, 2026, 'South Sudan'),
]

ASSIGNMENT['Spain'] = [
    (-200000, -220, 'NO_KNOWN_POLITIES'),
    (-133, -27, 'Roman Republic'),
    (-27, 410, 'Roman Empire'),
    (410, 552, 'NOT_RELEVANT'),
    (624, 711, 'NOT_RELEVANT'),
    (750, 1516, 'NOT_RELEVANT'),
    (1516, 1700, 'Habsburg Spain'),
    (1714, 1808, 'Bourbon Spain'),
    (1814, 1868, 'Bourbon Spain'),
    (1874, 1931, 'Bourbon Restoration Spain'),
    (1931, 1936, 'Spanish Second Republic'),
    (1939, 1975, 'Francoist Spain'),
    (1975, 2026, 'Kingdom of Spain'),
]

ASSIGNMENT['Sri Lanka'] = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (1070, 1796, 'NOT_RELEVANT'),
    (1817, 1948, 'British Ceylon'),
    (1948, 1972, 'Dominion of Ceylon'),
    (1972, 1978, 'Republic of Sri Lanka'),
    (1978, 2026, 'Democratic Socialist Republic of Sri Lanka'),
]

ASSIGNMENT['Sudan'] = [
    (-200000, -2500, 'NO_KNOWN_POLITIES'),
    (1821, 1885, 'Turkiyya (Egyptian Sudan)'),
    (1885, 1898, 'Mahdist State'),
    (1899, 1956, 'Anglo-Egyptian Sudan'),
    (1972, 1983, 'Sudan'),
    (2011, 2023, 'Sudan'),
]

ASSIGNMENT['Sweden'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    (1658, 2026, 'Kingdom of Sweden'),
]

ASSIGNMENT['Switzerland'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    (-400, -58, 'NOT_RELEVANT'),
    (-15, 401, 'Roman Empire'),
    (401, 536, 'NOT_RELEVANT'),
    (536, 751, 'Merovingian Frankish Kingdom'),
    (751, 843, 'Carolingian Empire'),
    (843, 962, 'NOT_RELEVANT'),
    (1032, 1499, 'Holy Roman Empire'),
    (1499, 1798, 'NOT_RELEVANT'),
    (1798, 1803, 'Helvetic Republic'),
    (1815, 2026, 'Swiss Confederation'),
]

ASSIGNMENT['Syria'] = [
    (-200000, -2500, 'NO_KNOWN_POLITIES'),
    (-2500, -550, 'NOT_RELEVANT'),
    (-550, -334, 'Achaemenid Empire'),
    (-200, -64, 'Seleucid Empire'),
    (-64, 395, 'Roman Empire'),
    (395, 636, 'Byzantine Empire'),
    (636, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 878, 'Abbasid Caliphate'),
    (1300, 1516, 'Mamluk Sultanate'),
    (1516, 1918, 'Ottoman Empire'),
    (1920, 1946, 'French Mandate of Syria'),
    (1946, 1958, 'Syrian Republic'),
    (1958, 1961, 'United Arab Republic'),
    (1961, 2011, 'Syrian Republic'),
]

ASSIGNMENT['Taiwan'] = [
    (-200000, 1624, 'NO_KNOWN_POLITIES'),
    (1662, 1683, 'NOT_RELEVANT'),
    (1683, 1895, 'Qing Dynasty'),
    (1895, 1945, 'Empire of Japan'),
    (1945, 2026, 'Republic of China'),
]

ASSIGNMENT['Tajikistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-250, 30, 'NOT_RELEVANT'),
    (750, 820, 'Abbasid Caliphate'),
    (820, 1220, 'NOT_RELEVANT'),
    (1370, 1929, 'NOT_RELEVANT'),
    (1929, 1991, 'Soviet Union'),
    (1991, 2026, 'Tajikistan'),
]

ASSIGNMENT['Tanzania'] = [
    (-200000, 1750, 'NO_KNOWN_POLITIES'),
    (1750, 1885, 'NOT_RELEVANT'),
    (1964, 2026, 'United Republic of Tanzania'),
]

ASSIGNMENT['Thailand'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    (500, 1932, 'NOT_RELEVANT'),
    (1932, 2026, 'Kingdom of Thailand'),
]

ASSIGNMENT['Togo'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    (1500, 1884, 'NOT_RELEVANT'),
    (1884, 1914, 'German Empire'),
    (1914, 1940, 'French Third Republic'),
    (1940, 1960, 'NOT_RELEVANT'),
    (1960, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Tunisia'] = [
    (-200000, -650, 'NO_KNOWN_POLITIES'),
    (-650, -146, 'Carthage'),
    (-146, 439, 'Roman Empire'),
    (439, 534, 'NOT_RELEVANT'),
    (534, 698, 'Byzantine Empire'),
    (698, 750, 'Umayyad Caliphate'),
    (750, 800, 'Abbasid Caliphate'),
    (800, 909, 'Aghlabid Emirate'),
    (909, 973, 'Fatimid Caliphate'),
    (1159, 1229, 'Almohad Caliphate'),
    (1229, 1534, 'Hafsid Caliphate'),
    (1574, 1881, 'Ottoman Empire'),
    (1881, 1956, 'French Protectorate of Tunisia'),
    (1956, 1957, 'Kingdom of Tunisia'),
    (1957, 2026, 'Republic of Tunisia'),
]

ASSIGNMENT['Turkey'] = [
    (-200000, -2000, 'NO_KNOWN_POLITIES'),
    (-2000, -550, 'NOT_RELEVANT'),
    (-550, -334, 'Achaemenid Empire'),
    (17, 395, 'Roman Empire'),
    (395, 611, 'Byzantine Empire'),
    (628, 1071, 'Byzantine Empire'),
    (1517, 1922, 'Ottoman Empire'),
    (1923, 2026, 'Republic of Turkey'),
]

ASSIGNMENT['Turkmenistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (750, 820, 'Abbasid Caliphate'),
    (1370, 1884, 'NOT_RELEVANT'),
    (1884, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Turkmenistan'),
]

ASSIGNMENT['UAE'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -330, 'Achaemenid Empire'),
    (-330, -311, 'NOT_RELEVANT'),
    (-311, -141, 'Seleucid Empire'),
    (-141, 224, 'NOT_RELEVANT'),
    (224, 637, 'Sassanid Empire'),
    (637, 661, 'Rashidun Caliphate'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 1507, 'NOT_RELEVANT'),
    (1650, 1820, 'NOT_RELEVANT'),
    (1971, 2026, 'United Arab Emirates'),
]

ASSIGNMENT['Uganda'] = [
    (-200000, 1300, 'NO_KNOWN_POLITIES'),
    (1900, 1962, 'British Uganda'),
    (1962, 2026, 'Uganda'),
]

ASSIGNMENT['Ukraine'] = [
    (-200000, -600, 'NO_KNOWN_POLITIES'),
    (-600, -63, 'NOT_RELEVANT'),
    (1939, 1941, 'Soviet Union'),
    (1944, 1991, 'Soviet Union'),
    (1991, 2026, 'Ukraine'),
]

ASSIGNMENT['United Kingdom'] = [
    (-200000, 43, 'NO_KNOWN_POLITIES'),
    (1707, 1801, 'Kingdom of Great Britain'),
    (1801, 1922, 'United Kingdom of Great Britain and Ireland'),
    (1922, 2026, 'United Kingdom of Great Britain and Northern Ireland'),
]

ASSIGNMENT['United States'] = [
    (-200000, 1565, 'NO_KNOWN_POLITIES'),
    (1848, 1861, 'United States'),
    (1865, 2026, 'United States'),
]

ASSIGNMENT['Uruguay'] = [
    (-200000, 1680, 'NO_KNOWN_POLITIES'),
    (1726, 1811, 'Spanish Empire'),
    (1822, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Uzbekistan'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    (-550, -530, 'NOT_RELEVANT'),
    (-530, -330, 'Achaemenid Empire'),
    (-330, -250, 'Seleucid Empire'),
    (-250, -150, 'Greco-Bactrian Kingdom'),
    (-150, 50, 'NOT_RELEVANT'),
    (50, 230, 'Kushan Empire'),
    (710, 750, 'Umayyad Caliphate'),
    (750, 900, 'Abbasid Caliphate'),
    (900, 999, 'Samanid Empire'),
    (999, 1220, 'NOT_RELEVANT'),
    (1220, 1260, 'Mongol Empire'),
    (1260, 1370, 'NOT_RELEVANT'),
    (1370, 1507, 'Timurid Empire'),
    (1507, 1868, 'NOT_RELEVANT'),
    (1876, 1917, 'Russian Empire'),
    (1922, 1991, 'Soviet Union'),
    (1991, 2026, 'Uzbekistan'),
]

ASSIGNMENT['Venezuela'] = [
    (-200000, 1521, 'NO_KNOWN_POLITIES'),
    (1600, 1810, 'Spanish Venezuela'),
    (1821, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Vietnam'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    (-700, -111, 'NOT_RELEVANT'),
    (938, 1407, 'NOT_RELEVANT'),
    (1427, 1858, 'NOT_RELEVANT'),
    (1887, 1940, 'French Third Republic'),
    (1954, 1976, 'NOT_RELEVANT'),
    (1976, 2026, 'Socialist Republic of Vietnam'),
]

ASSIGNMENT['Yemen'] = [
    (-200000, -1000, 'NO_KNOWN_POLITIES'),
    (-1000, 570, 'NOT_RELEVANT'),
    (570, 630, 'Sassanid Empire'),
    (630, 661, 'NOT_RELEVANT'),
    (661, 750, 'Umayyad Caliphate'),
    (750, 820, 'Abbasid Caliphate'),
    (820, 1040, 'NOT_RELEVANT'),
    (1098, 1538, 'NOT_RELEVANT'),
    (1636, 1849, 'NOT_RELEVANT'),
    (1967, 2026, 'NOT_RELEVANT'),
]

ASSIGNMENT['Zambia'] = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    (1600, 1890, 'NOT_RELEVANT'),
    (1924, 1953, 'Northern Rhodesia'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    (1964, 2026, 'Zambia'),
]

ASSIGNMENT['Zimbabwe'] = [
    (-200000, 1000, 'NO_KNOWN_POLITIES'),
    (1000, 1895, 'NOT_RELEVANT'),
    (1895, 1923, 'British South Africa Company (Rhodesia)'),
    (1923, 1953, 'Southern Rhodesia'),
    (1953, 1963, 'Federation of Rhodesia and Nyasaland'),
    (1965, 1979, 'Rhodesia'),
    (1980, 2026, 'Zimbabwe'),
]


def assign_polity(country, year, subregion=None):
    if country not in ASSIGNMENT:
        return 'unknown_country'
    entries = ASSIGNMENT[country]
    for start, end, polity in entries:
        if start <= year < end:
            if polity == 'NO_KNOWN_POLITIES':
                return 'no_known_polities'
            elif polity == 'NOT_RELEVANT':
                return 'not_relevant'
            else:
                return polity
    if entries and year < entries[0][0]:
        return 'no_known_polities'
    return 'indeterminate'
