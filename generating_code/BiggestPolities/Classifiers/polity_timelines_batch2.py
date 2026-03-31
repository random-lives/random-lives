"""
Complete polity timelines for: Democratic Republic of the Congo, Sudan,
South Sudan, Cameroon, Madagascar.

Format: list of (start_year, end_year_exclusive, polity_name) tuples.
Negative years = BCE. Gaps between entries = indeterminate.

Special polity names:
- NO_KNOWN_POLITIES: before any centralized polity with 100K+ people
- NOT_RELEVANT: polities existed but all had <100M lifetime births
  (lifetime births = avg_population × 0.04 × years_of_existence)
"""

TIMELINES = {}

# =============================================================================
# DEMOCRATIC REPUBLIC OF THE CONGO
# =============================================================================

TIMELINES['Democratic Republic of the Congo'] = [
    (-200000, 1400, 'NO_KNOWN_POLITIES'),
    # Kongo Kingdom emerges c. 1390-1400 as first centralized polity with >100K people.

    (1400, 1885, 'NOT_RELEVANT'),
    # Kongo Kingdom (c.1390-1914): peak ~500K, avg ~300K, 500 years → 6M births.
    # Luba Empire (c.1585-1889): peak ~1M, avg ~500K, 300 years → 6M births.
    # Lunda Empire (c.1665-1887): peak ~1M, avg ~500K, 220 years → 4.4M births.
    # No external polity with >100M lifetime births controlled any part of DRC territory.
    # Portugal had diplomatic contact with Kongo but did not control interior territory.

    (1885, 1908, 'Congo Free State'),
    # Leopold II's personal colony. Controlled essentially all of modern DRC's territory.

    (1908, 1960, 'Belgian Congo'),
    # Belgian state colony. Full territorial control of modern DRC.

    # GAP 1960-1965: Congo Crisis. The Republic of the Congo (later DRC) declared
    # independence June 30, 1960, but Katanga seceded July 11, 1960 (~10% of population)
    # and South Kasai seceded August 1960. Katanga secession ended January 1963,
    # but instability continued through 1965 Mobutu coup.
    # Polity with >100M births: DRC itself (avg ~50M × 0.04 × 66 years = 132M over 1960-2026).

    (1965, 1971, 'Democratic Republic of the Congo'),
    # Mobutu consolidated power by late 1965. Country reunified and stable.

    (1971, 1997, 'Zaire'),
    # Mobutu renamed the country to Zaire in 1971. Single-party state with full control.

    # GAP 1997-2003: First Congo War ended May 1997 (Kabila overthrew Mobutu), but the
    # Second Congo War (August 1998 - July 2003) saw the country effectively partitioned.
    # RCD rebels (backed by Rwanda/Uganda) controlled much of eastern DRC (>10% of population).
    # Polity with >100M births: DRC itself (see calculation above).

    (2003, 2026, 'Democratic Republic of the Congo'),
    # Transitional government 2003, elections 2006. Country nominally reunified.
    # Eastern instability continues but central government controls >99% of population.
]

# =============================================================================
# SUDAN
# =============================================================================

TIMELINES['Sudan'] = [
    (-200000, -2500, 'NO_KNOWN_POLITIES'),
    # Kingdom of Kerma emerges c. 2500 BCE as first centralized polity in Nubian Sudan
    # with >100K people under centralized control.

    # GAP -2500 to -1500: Kingdom of Kerma controlled Upper Nubia (northern Sudan).
    # Did not control 99% of modern Sudan's territory (western and southern regions independent).
    # Polity with >100M births: Egypt (avg ~3M pop over 3000 years = 360M+ lifetime births)
    # controlled parts of Lower Nubia and conducted campaigns into Kerma territory.
    # Egyptian fortifications at Buhen and Semna are within modern Sudan's borders.

    # GAP -1500 to -1070: Egyptian New Kingdom directly controlled northern Sudan (Nubia)
    # as far south as the 4th/5th cataract. But southern and western Sudan remained outside
    # Egyptian control. Egypt (>100M births) controlled part but not 99%.

    # GAP -1070 to 350: Kingdom of Kush/Meroë controlled the Nile valley through Sudan
    # (capital Meroë near modern Shendi). Kush at peak had ~1-2M people but didn't
    # control western Sudan (Darfur, Kordofan). Egypt (>100M births) was sometimes
    # subject to Kush (25th Dynasty) and sometimes controlled lower Nubia.
    # Rome (>100M births) controlled Egypt and lower Nubia after 30 BCE.

    # GAP 350-1504: After fall of Meroë, Christian Nubian kingdoms emerged:
    # Makuria, Alodia, Nobatia. These controlled the Nile valley but not western Sudan.
    # After Islamic expansion, Funj Sultanate precursors and Darfur sultanate emerge.
    # Polity with >100M births: Umayyad/Abbasid Caliphate (peak ~35M, 300+ years = 420M+)
    # controlled Egypt and had influence/raids into northern Sudan. Ottoman Empire
    # (from 1517) controlled Egypt, with indirect influence on Sudanese border regions.

    # GAP 1504-1821: Funj Sultanate of Sennar controlled central/eastern Sudan.
    # Darfur Sultanate controlled western Sudan. Neither controlled 99% of territory.
    # Polity with >100M births: Ottoman Empire (peak ~35M, existed 600+ years = 840M+)
    # controlled Egypt and had nominal suzerainty over parts of northern Sudan.

    (1821, 1885, 'Turkiyya (Egyptian Sudan)'),
    # Muhammad Ali of Egypt (Ottoman vassal) conquered Sudan 1820-24. Egyptian-Ottoman
    # administration controlled virtually all of modern Sudan's territory by 1874
    # (including Darfur, annexed 1874). Single administration over 99%+ of population.

    (1885, 1898, 'Mahdist State'),
    # Mahdist revolution overthrew Turkiyya. The Mahdist State controlled virtually all
    # of modern Sudan from the fall of Khartoum (1885) until the Battle of Omdurman (1898).

    (1899, 1956, 'Anglo-Egyptian Sudan'),
    # Anglo-Egyptian Condominium after British reconquest. Single administration over all
    # of modern Sudan (pre-2011 borders, but this entry is for post-2011 northern Sudan;
    # the condominium controlled all of it).

    # GAP 1956-1972: First Sudanese Civil War. Sudan declared independence Jan 1, 1956.
    # Anya-Nya rebels in the south (in what is now South Sudan) fought for autonomy.
    # For modern Sudan's (post-2011) territory specifically, the Sudanese government
    # controlled 99%+ since the civil war was in the south. However, using pre-2011
    # borders (as this is the same state), significant territory was contested.
    # Polity with >100M births: difficult to identify one that clearly exceeds threshold.
    # Sudan itself: avg ~15M × 0.04 × 67 years ≈ 40M over 1956-2023. Under 100M.
    # However, erring on the side of gaps as instructed due to uncertainty in population
    # estimates and the existence of a substantial state.

    (1972, 1983, 'Sudan'),
    # Addis Ababa Agreement ended the First Civil War. Sudan controlled 99%+ of its
    # territory during this peace period.

    # GAP 1983-2011: Second Sudanese Civil War. SPLA/M controlled large portions of
    # southern Sudan (now South Sudan). For post-2011 Sudan borders, the government
    # controlled its territory, but the Sudanese state as a polity had contested control.
    # Polity with >100M births: same uncertainty as above; erring toward gap.

    (2011, 2023, 'Sudan'),
    # After South Sudan's independence, Sudan controlled 99%+ of its remaining territory.
    # Darfur conflict continued but government maintained overall control.

    # GAP 2023-2026: Sudanese civil war (RSF vs SAF). RSF controls large portions of
    # Darfur, Kordofan, and parts of Khartoum — well over 1% of population.
    # Polity with >100M births: erring toward gap as with prior periods.
]

# =============================================================================
# SOUTH SUDAN
# =============================================================================

TIMELINES['South Sudan'] = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    # Southern Sudan had no centralized polities with >100K people until relatively late.
    # Nilotic pastoralist and agricultural societies predominated. Using -1500 as a
    # conservative estimate aligned with when polities existed in the broader region,
    # though South Sudan's own territory likely had no >100K polities until much later.

    (-1500, 1821, 'NOT_RELEVANT'),
    # South Sudan's territory was inhabited by Nilotic peoples (Dinka, Nuer, Shilluk, etc.)
    # organized in segmentary/chieftain societies. The Shilluk Kingdom (c. 1490+) was
    # the most centralized, with perhaps 100-200K people.
    # Shilluk Kingdom: avg ~150K × 0.04 × 330 years = 2M births. Far under 100M.
    # Kingdom of Kush was centered in northern Sudan; its southern extent did not reach
    # deep into modern South Sudan's territory. Egypt and other Nile valley polities
    # similarly did not control South Sudanese territory during this period.
    # Funj Sultanate had limited reach into northern South Sudan but didn't control it.

    # GAP 1821-1899: The Turkiyya (Egyptian Sudan) expanded into South Sudan,
    # particularly for slave trading. Egyptian/Ottoman forces established posts at
    # Gondokoro, Fashoda, etc. But control was partial — vast areas of South Sudan
    # remained under local authority. The Mahdist State (1885-1898) also had partial
    # control.
    # Polity with >100M births: Ottoman Empire (through its Egyptian vassal state) —
    # the Turkiyya was an arm of Ottoman-Egyptian administration, and the Ottoman Empire
    # (avg ~25M × 0.04 × 600 years = 600M+) vastly exceeds 100M lifetime births.

    (1899, 1956, 'Anglo-Egyptian Sudan'),
    # British-Egyptian Condominium controlled all of South Sudan. Administered as
    # "Closed Districts" (Southern Policy) from 1920s, but under single condominium authority.

    (1956, 2011, 'Sudan'),
    # South Sudan was part of independent Sudan. Despite the First (1955-1972) and
    # Second (1983-2005) Civil Wars, the Sudanese government remained the sovereign
    # authority and maintained control of major towns and much of the territory.
    # Rebel movements (Anya-Nya, SPLA) controlled rural areas at various times but
    # did not establish a separate recognized state until 2011.
    # This is a simplification — one could argue for gaps during civil war peaks.

    (2011, 2026, 'South Sudan'),
    # Independence July 9, 2011. Despite the South Sudanese Civil War (2013-2020),
    # no rival faction established a separate state or controlled >1% of population
    # as an independent polity. Both sides claimed to be the government of South Sudan.
]

# =============================================================================
# CAMEROON
# =============================================================================

TIMELINES['Cameroon'] = [
    (-200000, 1500, 'NO_KNOWN_POLITIES'),
    # Cameroon had Bantu-speaking agricultural societies and Sao culture near Lake Chad,
    # but no single centralized polity with >100K people under centralized control
    # covering Cameroonian territory is reliably attested before ~1500.

    # GAP 1500-1902: Multiple polities controlled portions of modern Cameroon:
    # - Bornu Empire controlled far north Cameroon (Lake Chad basin).
    #   Bornu: avg ~3M × 0.04 × 1000 years ≈ 120M lifetime births. Exceeds 100M.
    # - Adamawa Emirate (Fulani, from 1809) controlled northern Cameroon.
    # - Bamum Kingdom controlled western highlands.
    # - Duala city-states on the coast.
    # None controlled 99% of Cameroon's territory. The Bornu Empire (>100M) controlled
    # the far north, justifying this as a gap rather than NOT_RELEVANT.

    (1902, 1916, 'German Kamerun'),
    # Germany established Kamerun protectorate 1884, but effective control of the full
    # interior was only achieved by ~1902 after military campaigns. Controlled 99%+ of
    # modern Cameroon's territory (plus parts of modern Chad, CAR, Congo, Nigeria, Gabon).

    # GAP 1916-1961: After German defeat in WWI, Cameroon was split between France
    # (French Cameroun, ~80% of territory and population) and Britain (British Cameroons,
    # ~20%). Two separate colonial administrations — no single polity controlled 99%.
    # Polity with >100M births: France (avg ~40M × 0.04 × 1000+ years as a state = far
    # exceeds 100M) and British Empire (similar). Both clearly exceed 100M.
    # French Cameroun became independent Jan 1, 1960. British Southern Cameroons joined
    # the Republic of Cameroon via plebiscite on Oct 1, 1961. British Northern Cameroons
    # joined Nigeria. So 99% unification is from 1961.

    (1961, 2026, 'Republic of Cameroon'),
    # Federal Republic of Cameroon (1961-1972), United Republic of Cameroon (1972-1984),
    # Republic of Cameroon (1984-present). All the same continuous state.
    # Using a single name since these are just name changes, not regime changes.
    # Anglophone crisis (2017+) has not resulted in any separate state controlling >1%.
]

# =============================================================================
# MADAGASCAR
# =============================================================================

TIMELINES['Madagascar'] = [
    (-200000, 800, 'NO_KNOWN_POLITIES'),
    # Madagascar was uninhabited until Austronesian settlers arrived c. 500 CE
    # (with subsequent Bantu migration). First centralized polities emerge c. 800-1000 CE
    # (various Malagasy kingdoms). No polity with >100K people before ~800.

    (800, 1897, 'NOT_RELEVANT'),
    # Various Malagasy kingdoms: Merina (c. 1540-1897), Sakalava (c. 1600-1800s),
    # Betsimisaraka (c. 1710-1750s), and others.
    # Merina Kingdom at peak (c. 1810-1895): pop ~3M, avg ~2M over ~350 years:
    #   2M × 0.04 × 350 = 28M births. Under 100M.
    # Sakalava kingdoms: much smaller.
    # Merina Kingdom (1817-1885) controlled perhaps 80-90% of Madagascar's population
    # after Radama I's conquests, but some western/southern groups remained independent.
    # French protectorate declared 1885 but was largely nominal until 1895-1897 invasion.
    # France did NOT effectively control Malagasy territory until the military conquest
    # of 1895-1897 and abolition of the monarchy in 1897.
    # No polity with >100M lifetime births controlled any part of Madagascar before 1897.
    # (France's protectorate claim 1885-1897 was diplomatic, not territorial control.)

    (1897, 1960, 'French Madagascar'),
    # France conquered Madagascar 1895-1897, abolished the Merina monarchy, and
    # established full colonial control. Single colonial administration over 99%+.

    (1960, 2026, 'Madagascar'),
    # Independence June 26, 1960. Despite political crises (1972, 1991, 2002, 2009),
    # Madagascar has remained a single state. Various regime names:
    # Malagasy Republic (1960-1975), Democratic Republic of Madagascar (1975-1992),
    # Republic of Madagascar (1992-present). Continuous state throughout.
]
