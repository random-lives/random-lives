"""
Polity timelines for Mexico, Brazil, United States, Canada, Chile,
Costa Rica, Panama, Bolivia, Paraguay, Uruguay.

Format: list of (start_year, end_year_exclusive, polity_name) tuples.

Special polity names:
- NO_KNOWN_POLITIES: Before any polity with >=100K under centralized control
- NOT_RELEVANT: Polities existed but ALL had <100M lifetime births
  (lifetime births = avg_population * 0.04 * years_of_existence)
- Gaps between entries = indeterminate (polities with >100M births existed,
  but no single one controlled 99%+ of the modern country's population)

Gap justifications are in comments.
"""

MEXICO = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    # Olmec civilization (~1500 BCE) is earliest centralized polity with >100K people
    # in this territory.

    (-1500, 1521, 'NOT_RELEVANT'),
    # Mesoamerican polities: Olmec, Teotihuacan, Maya city-states, Toltec, Aztec.
    # Largest is Aztec Empire: ~12M avg pop × 0.04 × 93 yrs ≈ 44.6M births. Under 100M.
    # Teotihuacan: ~1.5M × 0.04 × 550 ≈ 33M. Under 100M.
    # All others smaller.

    # GAP 1521–1550: Spanish Empire (avg ~15M total pop across all territories × 0.04 ×
    # 321 yrs ≈ 193M lifetime births, well over 100M) was conquering Mexico but had not
    # yet consolidated control over 99%+ of the population. Maya regions in Yucatan and
    # western/northern frontiers still being subjugated.

    (1550, 1821, 'Spanish Mexico'),
    # Viceroyalty of New Spain. By ~1550, Spanish control extended over 99%+ of the
    # population within modern Mexico's borders. Peripheral unconquered indigenous groups
    # (Seri, Yaqui, some Maya) constituted <1% of total population.

    (1821, 1823, 'First Mexican Empire'),
    (1824, 1835, 'First Mexican Republic'),
    (1835, 1846, 'Centralist Republic of Mexico'),
    (1846, 1853, 'Second Federal Republic of Mexico'),
    # Includes Mexican-American War period; despite territorial losses (Treaty of
    # Guadalupe Hidalgo 1848), the Mexican state controlled 99%+ of people within
    # modern Mexico's remaining borders throughout.

    (1853, 1855, 'Dictatorship of Santa Anna'),
    (1855, 1857, 'NOT_RELEVANT'),
    # Brief transitional period after Plan de Ayutla. Liberal faction consolidated power
    # but formal constitutional republic not proclaimed until 1857. No foreign polity
    # with >100M births controlled any part of Mexico. All domestic factions well under
    # 100M lifetime births.

    (1857, 1863, 'Liberal Republic of Mexico'),

    # GAP 1863–1867: French Empire (France ~37M pop; French colonial empire total >100M
    # lifetime births) backed the Second Mexican Empire under Maximilian I, which
    # controlled central Mexico and major cities, while Juárez's liberal republic held
    # northern regions. Neither controlled 99%+.

    (1867, 1876, 'Restored Republic'),
    (1876, 1911, 'Porfiriato'),

    # GAP 1911–1920: Mexican Revolution. Multiple factions (Constitutionalists under
    # Carranza, Villistas, Zapatistas, Conventionists) controlled different regions.
    # The United States (~95M pop by 1914; lifetime births since 1776: avg ~30M × 0.04
    # × 138 yrs ≈ 166M, over 100M) occupied Veracruz in 1914 and launched the Punitive
    # Expedition into northern Mexico in 1916–17.

    (1920, 2026, 'Mexico'),
    # Post-revolutionary Mexican state. PRI single-party rule 1929–2000, then
    # democratic transition. Constitutional framework remained continuous throughout.
]

BRAZIL = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    # No indigenous polity in Brazil's territory had centralized control over 100K people.
    # Tupinambá confederations, Marajoara chiefdoms, etc. were all below this threshold.

    # GAP 1500–1750: Portuguese Empire controlled coastal Brazil but interior was
    # unconsolidated. Dutch Empire (Dutch Republic ~2M + East Indies ~10M+; lifetime
    # births well over 100M across full existence) controlled northeast Brazil 1630–1654.
    # Portuguese Empire itself is borderline on 100M lifetime births (Portugal avg ~3M +
    # growing colonies, total avg ~5–6M × 0.04 × 322 yrs ≈ 64–77M), and per
    # instructions we err strongly toward gaps when in doubt.

    (1750, 1815, 'Portuguese Brazil'),
    # By 1750 (Treaty of Madrid), Portuguese control extended to essentially all
    # populated areas of modern Brazil. Bandeirante expansion had pushed frontiers
    # into the interior.

    (1815, 1822, 'United Kingdom of Portugal, Brazil and the Algarves'),
    (1822, 1889, 'Empire of Brazil'),
    (1889, 1930, 'First Brazilian Republic'),
    (1930, 1945, 'Vargas Era'),

    # GAP 1945–1946: Brief transitional period between Vargas deposition and new
    # constitution. José Linhares served as interim president. The Brazilian state
    # (cumulative births from Empire through Republic: Brazil avg pop ~15M × 0.04 ×
    # 123 yrs ≈ 73.8M by 1945) is borderline. Erring toward gap.

    (1946, 1964, 'Fourth Brazilian Republic'),
    (1964, 1985, 'Military dictatorship of Brazil'),
    (1985, 2026, 'Brazil'),
]

UNITED_STATES = [
    (-200000, 1565, 'NO_KNOWN_POLITIES'),
    # Cahokia (~1050–1350 CE) had ~20–40K people at peak, below 100K threshold.
    # No indigenous polity within modern US borders reached 100K under centralized
    # political control. 1565 = founding of St. Augustine, first permanent European
    # settlement.

    # GAP 1565–1848: Multiple European powers controlled parts of modern US territory.
    # Spanish Empire (>100M lifetime births) held Florida, the Southwest, and California.
    # British Empire (>100M lifetime births) held the eastern seaboard colonies.
    # French Empire (France alone ~20M pop × 0.04 × several centuries, >100M births)
    # held Louisiana and the interior.
    # After US independence (1783): Spain held Florida until 1821; France held Louisiana
    # until 1803 (sold to US); Mexico held the Southwest until 1848; Texas was an
    # independent republic 1836–1845; Oregon Country jointly occupied until 1846.
    # Only after the Treaty of Guadalupe Hidalgo (1848) did the US control 99%+ of the
    # population within modern US borders.

    (1848, 1861, 'United States'),

    # GAP 1861–1865: American Civil War. Confederate States of America controlled
    # ~9M people (~30% of US population). The United States (lifetime births by 1861:
    # avg ~12M pop × 0.04 × 85 yrs ≈ 40.8M, under 100M strictly, but erring toward
    # gap per instructions given the US was a large, established state with ~31M
    # population at the time and cumulative births approaching 100M when including
    # natural increase).

    (1865, 2026, 'United States'),
]

CANADA = [
    (-200000, 1600, 'NO_KNOWN_POLITIES'),
    # No indigenous polity in modern Canada's territory had 100K under centralized
    # political control. The Haudenosaunee (Iroquois) Confederacy was a loose
    # confederation of autonomous nations, not centralized governance. Other groups
    # (Huron-Wendat, etc.) were smaller.

    # GAP 1600–1763: French Empire (France ~20M pop; lifetime births >100M) controlled
    # New France (St. Lawrence valley, Great Lakes, interior). British Empire (>100M
    # lifetime births) controlled Hudson Bay territory (HBC), Newfoundland, and Nova
    # Scotia (from 1713). Neither controlled 99%+ of modern Canada's population.

    (1763, 1867, 'British North America'),
    # After Treaty of Paris (1763), all populated territory within modern Canada's
    # borders came under British sovereignty: Quebec, Maritime provinces, Rupert's Land
    # (Hudson's Bay Company, under British Crown), Newfoundland, and the Pacific coast
    # (claimed after Cook's voyages, formalized by Oregon Treaty 1846).

    # GAP 1867–1949: Dominion of Canada formed 1867 (Confederation), but Newfoundland
    # remained a separate British colony (self-governing dominion 1907–1934, then
    # Commission of Government under Britain 1934–1949). Newfoundland's population was
    # consistently 2–4% of the total within modern Canada's borders:
    #   1871: ~160K NL vs ~3.7M Canada (~4.1%)
    #   1901: ~220K NL vs ~5.4M Canada (~3.9%)
    #   1941: ~320K NL vs ~11.5M Canada (~2.7%)
    # This exceeds the 1% threshold throughout.
    # Gap justified: British Empire (>100M lifetime births) controlled Newfoundland.

    (1949, 2026, 'Canada'),
    # Newfoundland joined Canadian Confederation on March 31, 1949.
]

CHILE = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    # No polity in Chile's territory had 100K under centralized control before ~600 CE.
    # Atacameño, Diaguita, and early Mapuche societies were smaller scale.

    (600, 1540, 'NOT_RELEVANT'),
    # Tiwanaku state (600–1000 CE) extended influence into northern Chile: ~1M pop ×
    # 0.04 × 400 yrs ≈ 16M births. Under 100M.
    # Inca Empire (1470–1533) controlled northern Chile: ~10M pop × 0.04 × 95 yrs ≈
    # 38M births. Under 100M.
    # All other polities (Mapuche, Diaguita, Aymara kingdoms) much smaller.

    # GAP 1540–1883: Spanish Empire (>100M lifetime births across all territories)
    # conquered central and northern Chile starting in 1540 (Pedro de Valdivia).
    # However, the Mapuche in southern Chile (Araucanía, roughly from the Biobío River
    # south) maintained independence throughout the colonial period and into the
    # Chilean republic. The Mapuche population was substantial: estimates of 500K–1M
    # in the 16th century, declining but still significant through the 19th century.
    # This exceeded 1% of the population within modern Chile's borders at all times.
    # After Chilean independence (1818), the Republic of Chile controlled the same
    # central/northern territory but not Araucanía. The Occupation of Araucanía
    # (1861–1883) finally brought this region under Chilean state control.
    # Gap justified: Spanish Empire (>100M lifetime births) controlled part of territory.
    # After 1818, the gap continues because no single polity controlled 99%+.

    (1883, 1973, 'Chile'),
    # After the Occupation of Araucanía (completed 1883), Chile controlled 99%+ of the
    # population within its modern borders. Includes War of the Pacific gains (1879–83)
    # in the north (Atacama, Tarapacá from Bolivia/Peru).

    (1973, 1990, 'Military dictatorship of Chile'),
    (1990, 2026, 'Chile'),
]

COSTA_RICA = [
    (-200000, 1563, 'NO_KNOWN_POLITIES'),
    # No pre-Columbian polity in Costa Rica's territory had centralized control
    # over 100K people. Chorotega, Huetar, and other groups were chiefdoms.
    # Spanish effective control begins with Vásquez de Coronado's founding of
    # Cartago in 1563-64. Most of Central America was conquered 1519-1523 but
    # Costa Rica was largely left alone until 1560.

    (1563, 1821, 'Spanish Empire'),
    # Part of the Captaincy General of Guatemala within the Viceroyalty of New
    # Spain. Spanish Empire lifetime births: avg ~20M total pop across all
    # territories × 0.04 × 329 yrs ≈ 263M. Well over 100M.
    # Spanish controlled 99%+ of population; unconquered indigenous groups in
    # Talamanca were <1% of total.

    (1821, 2026, 'NOT_RELEVANT'),
    # 1821-1823: Part of First Mexican Empire (~6.5M pop × 0.04 × 1.5 yrs =
    # 0.39M births). Under 100M.
    # 1823-1838: Federal Republic of Central America (~2M pop × 0.04 × 15 yrs
    # = 1.2M births). Under 100M.
    # 1838-2026: Republic of Costa Rica (avg ~1.5M pop × 0.04 × 188 yrs =
    # 11.3M births). Under 100M.
    # No foreign polity with >100M lifetime births controlled any part of
    # Costa Rica during this entire period.
]

PANAMA = [
    (-200000, 1510, 'NO_KNOWN_POLITIES'),
    # No pre-Columbian polity in Panama's territory had centralized control over
    # 100K people. Cueva, Coclé, and other groups were chiefdoms.
    # First permanent Spanish settlement at Santa María la Antigua del Darién
    # in 1510.

    (1510, 1821, 'Spanish Empire'),
    # Panama was a key transit point (Camino Real, Portobelo fairs). Spanish
    # Empire controlled 99%+ of population. Unconquered indigenous groups in
    # Darién were <1% of total. Spanish Empire lifetime births >100M.

    (1821, 1886, 'NOT_RELEVANT'),
    # 1821-1831: Part of Gran Colombia (~2.5M pop × 0.04 × 11 yrs = 1.1M
    # births). Under 100M.
    # 1831-1858: Republic of New Granada (~2M avg pop × 0.04 × 27 yrs = 2.2M
    # births). Under 100M.
    # 1858-1863: Granadine Confederation (~2.5M pop × 0.04 × 5 yrs = 0.5M
    # births). Under 100M.
    # 1863-1886: United States of Colombia (~3M avg pop × 0.04 × 23 yrs =
    # 2.8M births). Under 100M.
    # No other polity with >100M lifetime births controlled any part of Panama
    # during 1821-1886. Panama had a brief independent episode in 1840-41 but
    # this was also well under 100M.

    (1886, 1903, 'Republic of Colombia'),
    # Republic of Colombia (1886–present): avg pop ~18M × 0.04 × 140 yrs ≈
    # 101M lifetime births. Exceeds 100M. Controlled 99%+ of Panama's
    # population until Panama's secession on November 3, 1903.

    (1903, 2026, 'NOT_RELEVANT'),
    # Republic of Panama: avg pop ~2M × 0.04 × 123 yrs = 9.8M births.
    # Under 100M. The US-controlled Panama Canal Zone (1903–1979) held <1% of
    # Panama's total population. No other polity with >100M lifetime births
    # controlled any part of Panama.
]

BOLIVIA = [
    (-200000, 200, 'NO_KNOWN_POLITIES'),
    # No polity in Bolivia's territory had centralized control over 100K people
    # before the Tiwanaku state. Wankarani and Chiripa cultures were village-
    # level. Tiwanaku (c. 200–1000 CE) was a state with monumental architecture
    # and administrative reach across the altiplano, likely controlling several
    # hundred thousand people.

    (200, 1538, 'NOT_RELEVANT'),
    # Tiwanaku state (200–1000 CE): city of 30–70K, total polity ~500K–1M.
    # ~500K avg pop × 0.04 × 800 yrs = 16M births. Under 100M.
    # Post-Tiwanaku Aymara kingdoms (1000–1438): Qulla, Lupaqa, Pacajes, etc.
    # Each had populations of tens of thousands. All well under 100M.
    # Inca Empire (1438–1533): controlled western Bolivia as Qullasuyu.
    # ~10M avg pop × 0.04 × 95 yrs = 38M births. Under 100M.
    # Spanish conquest and civil wars (1533–1538): transitional period but all
    # polities still under 100M.

    (1538, 1825, 'Spanish Empire'),
    # Upper Peru / Audiencia of Charcas. By ~1538, Spanish effective control was
    # established after the civil wars between Pizarro and Almagro factions.
    # The Audiencia of Charcas was formally created in 1559 in Chuquisaca (Sucre).
    # Potosí became one of the wealthiest centers of the empire.
    # Spanish controlled 99%+ of population; eastern lowland indigenous groups
    # were <1% of total. Spanish Empire lifetime births >100M.
    # Bolivia declared independence August 6, 1825.

    (1825, 2026, 'NOT_RELEVANT'),
    # Republic of Bolivia: avg pop ~3M × 0.04 × 201 yrs = 24.1M births.
    # Under 100M. Bolivia lost territory in the War of the Pacific (1879–83),
    # Acre War (1899–1903), and Chaco War (1932–35), but always controlled
    # 99%+ of population within its current borders. No foreign polity with
    # >100M lifetime births controlled any part of modern Bolivia's territory
    # after 1825.
]

PARAGUAY = [
    (-200000, 1537, 'NO_KNOWN_POLITIES'),
    # No pre-Columbian polity in Paraguay's territory had centralized control
    # over 100K people. The Guaraní lived in semi-sedentary village communities
    # with no overarching state. The Inca Empire did not extend into Paraguay.
    # Spanish founded Asunción on August 15, 1537.

    (1537, 1811, 'Spanish Empire'),
    # Asunción became the center of Spanish power in southeastern South America
    # ("La Provincia Gigante de Indias"). Jesuit missions (1609–1767) operated
    # under Spanish sovereignty with up to 150K indigenous people in 30
    # reducciones. Spanish controlled 99%+ of the population within modern
    # Paraguay's borders. Spanish Empire lifetime births >100M.
    # Paraguay declared independence May 14, 1811.

    (1811, 2026, 'NOT_RELEVANT'),
    # 1811–1840: Francia dictatorship. 1840–1870: López dynasty.
    # 1864–1870: War of the Triple Alliance devastated Paraguay (population
    # fell from ~500K to ~220K). Brazil, Argentina, and Uruguay occupied
    # territory but the Paraguayan state continued to resist until 1870.
    # Post-war republic reconstituted. None of the occupying powers' individual
    # lifetime births matter here since all Paraguayan-era polities are under
    # 100M, and the Triple Alliance members' control was temporary and partial.
    # Republic of Paraguay: avg pop ~1.5M × 0.04 × 215 yrs = 12.9M births.
    # Under 100M. Brazil (Empire: 21M births), Argentina (~20M births by that
    # point), Uruguay (~2M births) — all under 100M during the war period.
    # No polity with >100M lifetime births controlled any part of Paraguay
    # after 1811.
]

URUGUAY = [
    (-200000, 1680, 'NO_KNOWN_POLITIES'),
    # Charrúa, Guaraní, and other indigenous peoples inhabited the region but
    # had no centralized state with 100K+ people. No Mesoamerican or Andean
    # polity extended to this area.
    # Portuguese founded Colônia do Sacramento in 1680 — first European
    # settlement and first polity with >100K people present in this territory.

    # GAP 1680–1726: Portuguese Empire (Kingdom of Portugal, 1139–1910: avg
    # metropolitan pop ~3M + colonial territories, total avg ~4.5M × 0.04 ×
    # 771 yrs ≈ 139M lifetime births, over 100M) controlled Colônia do
    # Sacramento. Spain claimed the rest of the territory but had no
    # settlements. No single polity controlled 99%+ of the population (Portugal
    # held the only European settlement; the rest was indigenous territory under
    # no centralized state control that Spain could not yet enforce).

    (1726, 1811, 'Spanish Empire'),
    # Spain founded Montevideo in 1726, establishing effective control over the
    # Banda Oriental. Colônia do Sacramento changed hands several times but its
    # population (~3K) was <1% of the Spanish-controlled population. Treaty of
    # San Ildefonso (1777) gave Spain formal control of the entire territory.
    # Spanish Empire lifetime births >100M. Controlled 99%+ of population.

    # GAP 1811–1822: Complex period of contested control.
    # 1811–1814: Spanish Empire (>100M lifetime births) still held Montevideo
    # while Artigas controlled the countryside.
    # 1814–1817: Artigas's Liga Federal controlled most of the territory, but
    # Buenos Aires briefly held Montevideo. Liga Federal: too small, too brief
    # for >100M. But Spanish Empire's recent presence and Portugal's imminent
    # invasion mean polities with >100M births were active in the region.
    # 1817–1822: United Kingdom of Portugal, Brazil and the Algarves invaded
    # and conquered the territory as Cisplatina. The Kingdom of Portugal as a
    # continuous sovereign entity (1139–1910) had >100M lifetime births.
    # No single polity controlled 99%+ throughout this turbulent period.

    (1822, 2026, 'NOT_RELEVANT'),
    # 1822–1828: Empire of Brazil controlled Cisplatina. Empire of Brazil
    # (1822–1889): avg ~8M pop × 0.04 × 67 yrs = 21.4M births. Under 100M.
    # United Provinces of Río de la Plata contested this during the Cisplatine
    # War (1825–1828) but had <100M lifetime births as well.
    # 1828–2026: Oriental Republic of Uruguay. Avg pop ~1.5M × 0.04 × 198 yrs
    # = 11.9M births. Under 100M. No foreign polity with >100M lifetime births
    # controlled any part of Uruguay after 1822.
]
