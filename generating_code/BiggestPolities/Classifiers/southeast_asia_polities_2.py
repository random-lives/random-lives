"""
Polity timelines for Southeast Asian countries: Indonesia, Philippines, Vietnam,
Thailand, Cambodia.

Format: list of (start_year, end_year_exclusive, polity_name) tuples.
- Negative years = BCE.
- NO_KNOWN_POLITIES: earliest period before any centralized polity with >=100K people.
- NOT_RELEVANT: polities existed but ALL had <100M lifetime births
  (calculated as avg_population * 0.04 * years_of_existence).
- Named polity: single polity controlled >=99% of modern country's population.
- Gaps: polities existed with >100M lifetime births but none controlled 99%+.

For colonial empires, lifetime births include ALL territories under imperial control.
"""

POLITIES = {}

# =============================================================================
# INDONESIA
# =============================================================================
#
# Gap justifications:
#
# 1800–1830: Kingdom of the Netherlands (1815-2026; including Indonesia 1815-1949):
#   avg ~33M total (Netherlands + Indonesia + other colonies) x 134 yrs x 0.04
#   = 177M births. Exceeds 100M. Controlled Java and key coastal areas but not 99%
#   of Indonesia's population — interior Sumatra, Borneo, many outer islands remained
#   under independent sultans. Also during 1800-1815, French-controlled Netherlands
#   held Java (French Empire far exceeds 100M births), and British Empire controlled
#   Java 1811-1816 (far exceeds 100M births).
#
# 1945–1949: Kingdom of the Netherlands (>100M births) attempted to reassert control
#   after Japanese surrender. Republic of Indonesia (1945-2026, >100M lifetime births
#   over full existence) declared independence. Neither controlled 99%.
#
POLITIES['Indonesia'] = [
    (-200000, 400, 'NO_KNOWN_POLITIES'),
    # Austronesian peoples, hunter-gatherer and early agricultural societies.
    # No centralized polity with >=100K people. Kutai and Tarumanagara kingdoms
    # emerge ~4th century CE as earliest Indianized states with plausible
    # centralized populations approaching 100K.

    (400, 1800, 'NOT_RELEVANT'),
    # Many polities existed but none controlling Indonesian territory exceeded 100M
    # lifetime births:
    # - Srivijaya (~650-1025): ~1.5M avg x 375 yrs x 0.04 = 22.5M births.
    # - Majapahit (~1293-1527): ~5M avg x 234 yrs x 0.04 = 46.8M births.
    # - Mataram Sultanate (~1587-1755): ~5M avg x 168 yrs x 0.04 = 33.6M births.
    # - VOC/Dutch Republic (~1602-1799): ~5M total x 197 yrs x 0.04 = 39.4M births.
    # - Portuguese outposts (Maluku, Timor): Portugal + colonies ~5M x 300 x 0.04 = 60M.
    # All under 100M. No external power with >100M births controlled Indonesian territory.

    # GAP 1800–1830 (see justification above)

    (1830, 1942, 'Kingdom of the Netherlands'),
    # After the Java War (1825-1830), Dutch had firm control of Java (~65-70% of
    # Indonesia's population). Adding Maluku, coastal Sulawesi and Sumatra, Dutch
    # control covered ~90%+ by 1830. Remaining independent areas (interior Borneo,
    # parts of Sumatra, Papua) had very small populations. Aceh War (1873-1904)
    # was the last major resistance but Aceh's ~500K-1M was ~2-3% of Indonesia's
    # ~30-40M total. By the 1880s-1900s, 99% was clearly met. Administered as the
    # Dutch East Indies, a colony of the Kingdom of the Netherlands.

    (1942, 1945, 'Empire of Japan'),
    # Japanese forces conquered the Dutch East Indies early 1942. Controlled all
    # major population centers and >99% of Indonesia's population.

    # GAP 1945–1949 (see justification above)

    (1949, 2026, 'Republic of Indonesia'),
    # Sovereignty transferred December 27, 1949. Western New Guinea (transferred
    # 1963) and East Timor (occupied 1975-1999) each had <1% of Indonesia's
    # population. Republic controlled 99%+ throughout.
]

# =============================================================================
# PHILIPPINES
# =============================================================================
#
# Gap justifications:
#
# 1565–1898: Spanish Empire (~1492-1898): Spain ~8M avg + Americas ~20M avg +
#   other colonies ~5M = ~33M avg x 406 yrs x 0.04 = 536M births. Far exceeds 100M.
#   Controlled ~90-95% of Philippine population (Christianized lowlands of Luzon and
#   Visayas) but never fully subjugated the Muslim south (Sultanate of Sulu,
#   Sultanate of Maguindanao). Muslim population was ~5-10% in early colonial period,
#   declining to ~3-5% by late 19th century. Not 99%.
#
# 1898–1902: United States of America (far exceeds 100M births) took possession
#   from Spain (Treaty of Paris, 1898) but First Philippine Republic (Aguinaldo)
#   controlled significant territory during Philippine-American War (1899-1902).
#
# 1942–1945: Empire of Japan (1868-1947): ~70M avg x 79 yrs x 0.04 = 221M births.
#   Exceeds 100M. Occupied major cities and lowlands but Filipino guerrilla forces
#   controlled significant rural areas (~10-20% of population at various points).
#   US forces returned October 1944 and gradually liberated the islands.
#
POLITIES['Philippines'] = [
    (-200000, 900, 'NO_KNOWN_POLITIES'),
    # Austronesian peoples organized into barangays (small polities of hundreds to
    # thousands). No centralized polity with >=100K people. Tondo polity emerges
    # ~900 CE in Manila Bay area as the earliest entity approaching this threshold.

    (900, 1565, 'NOT_RELEVANT'),
    # Various barangays, rajahnates, and sultanates:
    # - Rajahnate of Cebu, Butuan, Tondo (~900-1571)
    # - Sultanate of Sulu (~1450-1899), Sultanate of Maguindanao (~1500-1888)
    # All small polities. No external power controlled Philippine territory:
    # - Majapahit claimed Sulu area but no real control.
    # - Ming Dynasty had trade relations but no territorial control.
    # No polity controlling any part of the Philippines exceeded 100M lifetime births.

    # GAP 1565–1898 (see justification above)

    # GAP 1898–1902 (see justification above)

    (1902, 1942, 'United States of America'),
    # Philippine-American War ended 1902. US established the Insular Government.
    # Moro resistance continued until ~1913 but US maintained effective military
    # control of 99%+ of population areas. Philippines became a Commonwealth in
    # 1935 (semi-autonomous) but sovereignty remained with the US.

    # GAP 1942–1945 (see justification above)

    (1945, 1946, 'United States of America'),
    # After liberation (Manila recaptured February 1945, Japanese surrender
    # August 1945), US resumed sovereignty until independence.

    (1946, 2026, 'Republic of the Philippines'),
    # Independence granted July 4, 1946. Controlled 99%+ of population. Moro
    # insurgency in Mindanao ongoing but Philippine government maintains sovereign
    # territorial control; Bangsamoro Autonomous Region (2019) operates within
    # Philippine sovereignty.
]

# =============================================================================
# VIETNAM
# =============================================================================
#
# Gap justifications:
#
# -111 to 938: Chinese imperial dynasties controlled northern Vietnam (Jiaozhi/Annam
#   commanderies). Southern/central Vietnam was under Champa (independent). No single
#   polity controlled 99% of modern Vietnam.
#   - Han Dynasty (202 BCE - 220 CE): ~55M avg x 422 yrs x 0.04 = 928M births.
#   - Tang Dynasty (618-907): ~60M avg x 289 yrs x 0.04 = 694M births.
#   Both far exceed 100M and controlled northern Vietnam.
#
# 1407–1427: Ming Dynasty (1368-1644): ~100M avg x 276 yrs x 0.04 = 1.1B births.
#   Conquered Dai Ngu (Vietnam) in 1407, establishing Jiaozhi province. Controlled
#   northern Vietnam but not Cham territories in the south.
#
# 1858–1887: French Empire progressively conquered Vietnam. Cochinchina seized
#   1858-1862, protectorates over Annam and Tonkin 1883-1884, French Indochina
#   established 1887. French Third Republic (1870-1940): ~60M avg x 70 yrs x 0.04
#   = 168M births. Exceeds 100M. Controlled growing portions of Vietnam but not
#   99% until full protectorate system in place.
#
# 1940–1954: Complex overlapping authorities.
#   - Empire of Japan (1868-1947): 221M births. Dominated Vietnam 1940-1945.
#   - After 1945: France (Fourth Republic) fought First Indochina War.
#     French colonial empire's cumulative scale makes the <100M judgment uncertain
#     for Fourth Republic alone (49M births), but French forces controlled significant
#     territory. Erring on side of gap rather than NOT_RELEVANT.
#
POLITIES['Vietnam'] = [
    (-200000, -700, 'NO_KNOWN_POLITIES'),
    # Dong Son culture and predecessors. No centralized polity with >=100K people.
    # Van Lang kingdom traditionally dated to ~700 BCE (semi-legendary but
    # represents earliest plausible centralized polity in Red River Delta).

    (-700, -111, 'NOT_RELEVANT'),
    # Van Lang (~700-257 BCE), Au Lac (~257-207 BCE), Nanyue (204-111 BCE).
    # - Van Lang/Au Lac: ~750K avg x ~600 yrs x 0.04 = 18M births.
    # - Nanyue: ~1.5M x 93 yrs x 0.04 = 5.6M births.
    # - Qin Dynasty (~214-206 BCE): only 15 yrs total existence, 12M births.
    # All under 100M. No polity controlling Vietnam exceeded 100M births.

    # GAP -111 to 938 (see justification above)

    (938, 1407, 'NOT_RELEVANT'),
    # Vietnamese independence (Battle of Bach Dang 938). Successive dynasties
    # controlled northern Vietnam, Champa controlled center/south:
    # - Ly Dynasty (1009-1225): ~4M avg x 216 yrs x 0.04 = 34.6M births.
    # - Tran Dynasty (1225-1400): ~5M avg x 175 yrs x 0.04 = 35M births.
    # - Champa: ~1M avg over ~1000 yrs x 0.04 = 40M births.
    # Song Dynasty did not control Vietnam. Mongol Yuan invaded thrice but failed
    # to hold territory. No polity controlling any part exceeded 100M births.

    # GAP 1407–1427 (see justification above)

    (1427, 1858, 'NOT_RELEVANT'),
    # Later Le Dynasty (1428-1789), Trinh-Nguyen split (~1600-1777), Tay Son
    # (1778-1802), Nguyen Dynasty (1802-1945). Vietnam gradually expanded south.
    # - Trinh lords (1545-1787): ~5M avg x 242 x 0.04 = 48.4M births.
    # - Nguyen lords (1558-1777): ~2.5M avg x 219 x 0.04 = 22M births.
    # - Nguyen Dynasty (1802-1945): ~12M avg x 143 x 0.04 = 68.6M births.
    # - Tay Son (1778-1802): ~7M x 24 x 0.04 = 6.7M births.
    # All under 100M. Qing invaded 1788-89 but was defeated; no sustained control.

    # GAP 1858–1887 (see justification above)

    (1887, 1940, 'French Third Republic'),
    # French Indochina established 1887. France controlled all of Vietnam through
    # Cochinchina (colony), Annam (protectorate), Tonkin (protectorate). 99%+ of
    # Vietnam's population under French control.

    # GAP 1940–1954 (see justification above)

    (1954, 1976, 'NOT_RELEVANT'),
    # Vietnam divided at 17th parallel (Geneva Accords 1954):
    # - Democratic Republic of Vietnam (North, 1945-1976): ~15M avg x 31 yrs
    #   x 0.04 = 18.6M births.
    # - Republic of Vietnam (South, 1955-1975): ~16M avg x 20 yrs x 0.04 = 12.8M.
    # Neither controlled 99% of modern Vietnam. US had military presence in the
    # South but did not exercise sovereignty (RVN was sovereign). China and USSR
    # supported the North but did not control its territory. No polity controlling
    # Vietnamese territory exceeded 100M lifetime births as sovereign authority.

    (1976, 2026, 'Socialist Republic of Vietnam'),
    # Reunification July 2, 1976, following North Vietnam's victory (fall of Saigon
    # April 30, 1975). SRV (1976-2026): ~70M avg x 50 yrs x 0.04 = 140M births.
    # Exceeds 100M. Controlled 99%+ of modern Vietnam.
]

# =============================================================================
# THAILAND
# =============================================================================
#
# Thailand is unique in Southeast Asia for never being colonized by a European power.
# No external power with >100M lifetime births ever controlled any part of modern
# Thailand's territory:
# - Mongol Empire did not reach Thailand.
# - Ming/Qing had tributary relations with Siam but no territorial control.
# - British Empire took Malay states from Siam (1909) but those are in modern Malaysia.
# - French Empire took territories (1893, 1907) but those are in modern Laos/Cambodia.
# - During WWII, Japan allied with Thailand but Thailand maintained sovereignty
#   (declared war on Allies; Japan stationed troops but Thai government continued).
#
# All domestic polities were also under 100M lifetime births until the constitutional
# era:
# - Dvaravati (~6th-11th c.): ~500K avg x 500 yrs x 0.04 = 10M births.
# - Khmer Empire (802-1431): ~2M avg x 629 yrs x 0.04 = 50.3M births.
# - Sukhothai (~1238-1438): ~1.5M avg x 200 yrs x 0.04 = 12M births.
# - Ayutthaya (1351-1767): ~3M avg x 416 yrs x 0.04 = 49.9M births.
# - Kingdom of Siam / absolute monarchy (1782-1932): ~8M avg x 150 yrs x 0.04 = 48M.
# All under 100M.
#
# Kingdom of Thailand / constitutional monarchy (1932-2026): ~40M avg x 94 yrs
#   x 0.04 = 150.4M births. First Thai polity to exceed 100M.
#
POLITIES['Thailand'] = [
    (-200000, 500, 'NO_KNOWN_POLITIES'),
    # Bronze Age cultures (Ban Chiang ~3600 BCE), iron age communities, early
    # agricultural societies. No centralized polity with >=100K people.
    # Dvaravati Mon kingdom begins to emerge ~6th century.

    (500, 1932, 'NOT_RELEVANT'),
    # Many polities existed but none controlling Thai territory exceeded 100M
    # lifetime births, and no external power with >100M births controlled any
    # part of modern Thailand's territory. See detailed calculations above.

    (1932, 2026, 'Kingdom of Thailand'),
    # Siamese revolution of June 24, 1932 transformed absolute monarchy into
    # constitutional monarchy. Country renamed from Siam to Thailand 1939.
    # Various constitutions and coups but continuous Chakri dynasty and Thai
    # sovereignty throughout. During WWII (1941-1945), Thailand was a Japanese
    # ally but maintained its own government and territorial sovereignty.
    # Controlled 99%+ of population within modern borders.
]

# =============================================================================
# CAMBODIA
# =============================================================================
#
# Gap justifications:
#
# 1940–1945: Empire of Japan (1868-1947): ~70M avg x 79 yrs x 0.04 = 221M births.
#   Exceeds 100M. Exercised dominant military power over French Indochina including
#   Cambodia 1941-1945.
#
# 1979–1989: Socialist Republic of Vietnam (1976-2026): ~70M avg x 50 yrs x 0.04
#   = 140M births. Exceeds 100M. Vietnam invaded Cambodia December 1978 and
#   installed the People's Republic of Kampuchea as a client state with ~150,000
#   Vietnamese troops. Khmer Rouge remnants controlled small border areas, making
#   99% threshold uncertain. Not naming SRV as controller because PRK was formally
#   sovereign and the situation is analogous to a puppet state.
#
POLITIES['Cambodia'] = [
    (-200000, 200, 'NO_KNOWN_POLITIES'),
    # Pre-state agricultural and fishing communities. Funan kingdom begins to
    # emerge ~1st-2nd century CE as earliest Indianized state with plausible
    # centralized population approaching 100K.

    (200, 1870, 'NOT_RELEVANT'),
    # Many polities existed but none controlling Cambodian territory exceeded
    # 100M lifetime births:
    # - Funan (~1st-6th c.): ~750K avg x 400 yrs x 0.04 = 12M births.
    # - Chenla (~6th-8th c.): ~750K avg x 200 yrs x 0.04 = 6M births.
    # - Khmer Empire (802-1431): ~2M avg x 629 yrs x 0.04 = 50.3M births.
    # - Post-Angkor Cambodia (1431-1863): ~1M avg. Well under 100M.
    # - Second French Empire (1852-1870): ~40M x 18 yrs x 0.04 = 28.8M births.
    #   Protectorate from 1863 but regime itself under 100M.
    # External powers:
    # - Ayutthaya (1351-1767): 49.9M births. Under 100M.
    # - Siam absolute monarchy (1782-1932): 48M births. Under 100M.
    # - Nguyen Dynasty (1802-1945): 68.6M births. Under 100M.
    # No polity controlling any part of Cambodia exceeded 100M lifetime births.

    (1870, 1940, 'French Third Republic'),
    # French Third Republic (1870-1940) continued the protectorate over Cambodia.
    # France controlled 99%+ through protectorate system — Cambodian king was
    # figurehead; France controlled administration, military, foreign affairs.
    # French Third Republic: ~60M avg x 70 yrs x 0.04 = 168M births. Exceeds 100M.

    # GAP 1940–1945 (see justification above)

    (1945, 1979, 'NOT_RELEVANT'),
    # French protectorate briefly resumed; Cambodia gained independence 1953.
    # - French Fourth Republic (1946-1958): ~102M x 12 x 0.04 = 49M births. Under 100M.
    # - Kingdom of Cambodia / Sihanouk (1953-1970): ~6M avg x 17 x 0.04 = 4.1M.
    # - Khmer Republic / Lon Nol (1970-1975): ~7M avg x 5 x 0.04 = 1.4M.
    # - Democratic Kampuchea / Khmer Rouge (1975-1979): ~7M avg x 4 x 0.04 = 1.1M.
    # US bombing campaign and Vietnamese presence in eastern Cambodia did not
    # constitute sovereign control. China backed Khmer Rouge but did not control
    # territory. No polity controlling any part exceeded 100M lifetime births.

    # GAP 1979–1989 (see justification above)

    (1989, 2026, 'NOT_RELEVANT'),
    # Vietnamese troops withdrew 1989. Successive Cambodian governments:
    # - State of Cambodia (1989-1993): ~8M x 4 x 0.04 = 1.3M births.
    # - Kingdom of Cambodia restored (1993-2026): ~13M avg x 33 x 0.04 = 17.2M.
    # No external power with >100M births controlled any part.
]
