"""
Polity timelines for Egypt, Saudi Arabia, Yemen, Jordan, Israel.

Each entry: (start_year, end_year_exclusive, polity_name)
- Negative years = BCE
- NO_KNOWN_POLITIES: pre-polity era
- NOT_RELEVANT: all polities in territory had <100M lifetime births
- Named polity: single polity controlled 99%+ of modern country's population
- Gaps (missing periods): polities with >100M births present but none controlled 99%

Lifetime births formula: avg_population × 0.04 × years_of_existence
For colonial empires, total population across ALL territories.

For every gap, justification is provided in comments naming the >100M polity.
"""

TIMELINES = {}

# =============================================================================
# EGYPT
# =============================================================================
TIMELINES['Egypt'] = [
    (-200000, -3100, 'NO_KNOWN_POLITIES'),
    (-3100, -525, 'NOT_RELEVANT'),
    # All pharaonic polities <100M births. Largest: New Kingdom ~76M.
    (-525, -404, 'Achaemenid Empire'),     # 308M births; controlled all Egypt
    (-404, -343, 'NOT_RELEVANT'),           # Independent 28th-30th dynasties; ~10M births
    (-343, -332, 'Achaemenid Empire'),
    (-332, -30, 'NOT_RELEVANT'),
    # Macedonian Empire 16M, Ptolemaic Kingdom 77M. No other >100M polity in Egypt.
    (-30, 395, 'Roman Empire'),             # 1,012M births; controlled all Egypt
    (395, 619, 'Byzantine Empire'),         # 508M births; controlled all Egypt
    (619, 629, 'Sassanid Empire'),          # 342M births; conquered Egypt from Byzantines
    (629, 641, 'Byzantine Empire'),         # Reconquered Egypt from Sassanids
    (641, 661, 'NOT_RELEVANT'),
    # Rashidun Caliphate controlled 99% but only 29M births. No other polity present.
    (661, 750, 'Umayyad Caliphate'),       # 142M births; controlled all Egypt
    (750, 868, 'Abbasid Caliphate'),       # 711M births; controlled all Egypt
    (868, 905, 'NOT_RELEVANT'),
    # Tulunid dynasty: 9M births. Abbasids existed but did not control Egypt.
    (905, 935, 'Abbasid Caliphate'),       # Reconquered Egypt
    (935, 969, 'NOT_RELEVANT'),
    # Ikhshidid dynasty: 7M births. Abbasids/Fatimids existed but neither controlled Egypt.
    (969, 1171, 'Fatimid Caliphate'),      # 126M births; controlled all Egypt
    (1171, 1250, 'NOT_RELEVANT'),
    # Ayyubid Sultanate: 36M births. Controlled 99% but <100M. No other >100M polity.
    (1250, 1517, 'Mamluk Sultanate'),      # 107M births; controlled all Egypt
    (1517, 1798, 'Ottoman Empire'),        # 623M births; controlled all Egypt
    # GAP 1798-1914: Ottoman Empire (623M births) maintained nominal sovereignty.
    # 1798-1801: French occupation while Ottoman Empire claimed sovereignty.
    # 1801-1805: Power struggle (Ottoman, Mamluk, British involvement).
    # 1805-1882: Muhammad Ali dynasty effectively independent but Ottoman suzerainty formal.
    # 1882-1914: British military occupation of nominally Ottoman Egypt.
    # No single polity cleanly controlled 99% throughout.
    (1914, 1922, 'British Empire'),        # Protectorate; Ottoman claim ended Dec 1914
    (1922, 1953, 'Kingdom of Egypt'),      # 21M births but controlled 99%+
    # British Canal Zone had <1% of Egypt's population.
    # Under decision tree: British Empire (>100M) controlled <1%, so step 2 passes →
    # step 3: KoE controlled 99% → named. But KoE itself has <100M births.
    # Treating as NOT_RELEVANT since total births in territory under any >100M polity
    # are negligible. Actually, naming it since it controlled 99% and the >100M
    # polity (British) controlled such a trivial share. Keeping it named for clarity.
    (1953, 2026, 'Republic of Egypt'),     # 146M births; controlled 99%+
]

# =============================================================================
# SAUDI ARABIA
# =============================================================================
TIMELINES['Saudi Arabia'] = [
    (-200000, -550, 'NO_KNOWN_POLITIES'),
    # GAP -550 to -330: Achaemenid Empire (308M births) controlled eastern Arabian coast.
    # Interior (Najd) remained tribal. No single polity controlled 99%.
    (-330, 106, 'NOT_RELEVANT'),
    # After Achaemenid collapse: Seleucid/Ptolemaic presence in Arabia minimal.
    # Nabataean Kingdom in northwest, tribal polities elsewhere. All <100M births.
    # Parthian Empire had negligible Arabian presence.
    # GAP 106-632: Roman Empire (1,012M births) annexed Nabataean territory in
    # northwest Arabia (106 CE). Byzantine Empire (508M births) inherited it.
    # Sassanid Empire (342M births) controlled/influenced eastern coast.
    # Interior always remained tribal. No single polity controlled 99%.
    (632, 661, 'NOT_RELEVANT'),
    # Rashidun Caliphate unified Arabia after Ridda Wars. 29M births. Only polity.
    (661, 750, 'Umayyad Caliphate'),       # 142M births; controlled all Arabia
    (750, 900, 'Abbasid Caliphate'),       # 711M births; controlled Arabia initially
    (900, 969, 'NOT_RELEVANT'),
    # Abbasid control of Arabia collapsed. Qarmatians in east, local rulers in Hejaz.
    # Abbasids did not effectively control any Saudi territory. All polities <100M.
    # GAP 969-1073: Fatimid Caliphate (126M births) exercised suzerainty over
    # Sharifs of Mecca (Hejaz). Eastern/central Arabia independent. No 99% control.
    (1073, 1250, 'NOT_RELEVANT'),
    # Fatimid influence over Hejaz waned. Ayyubids briefly present. All <100M.
    # Abbasid Caliphate existed but did not control Saudi territory.
    # GAP 1250-1517: Mamluk Sultanate (107M births) controlled the Hejaz.
    # Central/eastern Arabia remained independent. No single polity controlled 99%.
    # GAP 1517-1925: Ottoman Empire (623M births) controlled Hejaz and intermittently
    # eastern coast. Central Arabia (Najd) under First/Second Saudi States, Rashidi
    # Emirate, etc. No single polity controlled 99%.
    (1925, 2026, 'NOT_RELEVANT'),
    # 1925-1932: Ibn Saud unified Arabia. 1932+: Kingdom of Saudi Arabia.
    # KSA: ~45M births. Only polity in territory. All <100M.
]

# =============================================================================
# YEMEN
# =============================================================================
TIMELINES['Yemen'] = [
    (-200000, -1000, 'NO_KNOWN_POLITIES'),
    (-1000, 570, 'NOT_RELEVANT'),
    # South Arabian kingdoms (Sabaean, Himyarite, etc.): all <100M births.
    # Himyarite Kingdom: ~51M. Roman expedition of 25 BCE failed; no Roman control.
    # Aksumite occupation (525-570): <100M. No external >100M polity controlled Yemen.
    (570, 630, 'Sassanid Empire'),         # 342M births; conquered Yemen from Aksumites
    (630, 661, 'NOT_RELEVANT'),
    # Rashidun Caliphate: 29M births. Controlled 99% but <100M. Only polity.
    (661, 750, 'Umayyad Caliphate'),       # 142M births; controlled all Yemen
    (750, 820, 'Abbasid Caliphate'),       # 711M births; controlled Yemen initially
    (820, 1040, 'NOT_RELEVANT'),
    # Local Yemeni dynasties (Ziyadid, Yu'firid, etc.). Abbasid Caliphate existed but
    # did not control Yemen. All polities in Yemen <100M.
    # GAP 1040-1098: Fatimid Caliphate (126M births) controlled parts of Yemen via
    # Sulayhid vassal dynasty. Other parts under independent rulers (Najahids, etc.).
    # No single polity controlled 99%.
    (1098, 1538, 'NOT_RELEVANT'),
    # After Sulayhid collapse, local dynasties (Hamdanids, Rasulids 1229-1454, Tahirids).
    # All <100M births. No external >100M polity controlled Yemeni territory.
    # GAP 1538-1636: Ottoman Empire (623M births) conquered coastal Yemen and parts of
    # highlands. Zaydi imams controlled significant highland territory (>1% of pop).
    # Neither Ottoman nor Zaydi controlled 99%.
    (1636, 1849, 'NOT_RELEVANT'),
    # Qasimid/Zaydi Imamate controlled most of Yemen. ~21M births. Only polity. <100M.
    # GAP 1849-1918: Ottoman Empire (623M births) reconquered northern Yemen (Yemen
    # Vilayet). British Empire (>100M births) controlled Aden and southern coast.
    # Neither controlled 99% — territory split between two >100M empires.
    # GAP 1918-1967: British Empire (>100M births) controlled southern Yemen (Aden
    # Colony/Protectorate). Northern Yemen was independent (Mutawakkilite Kingdom,
    # then YAR from 1962) with <100M births. British presence in south means
    # not all polities <100M, so NOT_RELEVANT doesn't apply.
    (1967, 2026, 'NOT_RELEVANT'),
    # After British withdrawal from Aden (1967): North Yemen (YAR) and South Yemen
    # (PDRY) — both <100M. Unified as Republic of Yemen 1990. Civil war from 2014.
    # No polity with >100M births controlled any Yemeni territory after 1967.
]

# =============================================================================
# JORDAN
# =============================================================================
TIMELINES['Jordan'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (-1200, -740, 'NOT_RELEVANT'),
    # Ammon, Moab, Edom, Israelite kingdoms. All <100M births.
    # New Kingdom Egypt had retreated from the region by ~1150 BCE.
    # GAP -740 to -612: Neo-Assyrian Empire (~10M avg pop × 0.04 × 300 yrs = 120M
    # births) controlled Transjordan through tribute/vassalage. Local kingdoms
    # (Ammon, Moab) persisted as tributaries with some autonomy. Assyrian control
    # was real but exercised through vassal kings, not direct governance of 99%.
    (-612, -539, 'NOT_RELEVANT'),
    # Neo-Babylonian Empire: 26M births. Controlled Transjordan. <100M. Only polity.
    (-539, -332, 'Achaemenid Empire'),     # 308M births; controlled 99%
    (-332, -301, 'NOT_RELEVANT'),
    # Macedonian Empire (16M births) then Diadochi wars. All <100M.
    (-301, -200, 'NOT_RELEVANT'),
    # Ptolemaic Kingdom controlled Transjordan. 77M births. <100M. Only >100M polity
    # (Seleucids) didn't control this territory during this period.
    (-200, -167, 'Seleucid Empire'),       # 199M births; controlled 99%
    # GAP -167 to -63: Seleucid Empire (199M births) still existed and controlled parts.
    # Hasmonean Kingdom expanded into parts of Transjordan. Nabataeans controlled south.
    # No single polity controlled 99%.
    # GAP -63 to 106: Roman Empire (1,012M births) controlled northern Jordan directly
    # and through client kings. Nabataean Kingdom controlled southern Jordan (Petra area)
    # independently with significant population (>1%). No single polity controlled 99%.
    (106, 395, 'Roman Empire'),            # After Nabataean annexation; controlled 99%
    (395, 636, 'Byzantine Empire'),        # 508M births; controlled 99%
    (636, 661, 'NOT_RELEVANT'),
    # Rashidun Caliphate: 29M births. Controlled 99%. Only polity. <100M.
    (661, 750, 'Umayyad Caliphate'),       # 142M births; controlled 99%
    (750, 969, 'Abbasid Caliphate'),       # 711M births; controlled Jordan
    (969, 1099, 'Fatimid Caliphate'),      # 126M births; controlled Palestine/Jordan
    (1099, 1250, 'NOT_RELEVANT'),
    # Crusader and Ayyubid period. Kingdom of Jerusalem (Oultrejordain) and Ayyubids.
    # All <100M births. Fatimid Caliphate still existed until 1171 but lost control
    # of Jordan to Crusaders. After 1171, Ayyubids controlled most of Jordan but <100M.
    (1250, 1516, 'Mamluk Sultanate'),      # 107M births; controlled 99%
    (1516, 1918, 'Ottoman Empire'),        # 623M births; controlled 99%
    # GAP 1918-1921: British Empire (>100M births) occupied the territory after WWI.
    # Faisal's Arab Kingdom (based in Damascus) claimed it briefly (1918-1920).
    # No single polity had stable 99% control — transitional period.
    (1921, 1946, 'British Empire'),        # Emirate of Transjordan under British mandate
    (1946, 2026, 'NOT_RELEVANT'),
    # Hashemite Kingdom of Jordan: 13M births. Only polity. <100M.
]

# =============================================================================
# ISRAEL (territory within modern borders, excluding West Bank/Gaza)
# =============================================================================
TIMELINES['Israel'] = [
    (-200000, -1200, 'NO_KNOWN_POLITIES'),
    (-1200, -740, 'NOT_RELEVANT'),
    # Israelite kingdoms, Philistine city-states. All <100M births.
    # GAP -740 to -612: Neo-Assyrian Empire (120M births) conquered Kingdom of Israel
    # (720 BCE) and dominated Judah as vassal. Philistia conquered. But Judah maintained
    # its own king with meaningful autonomy (>1% of population in semi-independent state).
    (-612, -539, 'NOT_RELEVANT'),
    # Neo-Babylonian Empire: 26M births. Conquered Judah 586 BCE. <100M. Only polity.
    (-539, -332, 'Achaemenid Empire'),     # 308M births; controlled 99% (Yehud province)
    (-332, -301, 'NOT_RELEVANT'),
    # Macedonian Empire 16M births. Diadochi wars. All <100M.
    (-301, -200, 'NOT_RELEVANT'),
    # Ptolemaic Kingdom controlled Palestine. 77M births. <100M.
    (-200, -167, 'Seleucid Empire'),       # 199M births; controlled 99%
    # GAP -167 to -63: Seleucid Empire (199M births) still existed and contested areas.
    # Hasmonean Kingdom gradually took control but Seleucids held coastal cities at times.
    # No single polity controlled 99%.
    (-63, 395, 'Roman Empire'),            # 1,012M births; controlled 99%
    # Client kings (Herod et al.) were firmly under Roman authority.
    (395, 636, 'Byzantine Empire'),        # 508M births; controlled 99%
    (636, 661, 'NOT_RELEVANT'),
    # Rashidun Caliphate: 29M births. Controlled 99%. Only polity. <100M.
    (661, 750, 'Umayyad Caliphate'),       # 142M births; controlled 99%
    (750, 878, 'Abbasid Caliphate'),       # 711M births; controlled Palestine
    (878, 905, 'NOT_RELEVANT'),
    # Tulunid dynasty controlled Palestine from Egypt. ~9M births. <100M.
    # Abbasids existed but didn't control Palestine.
    (905, 935, 'Abbasid Caliphate'),       # Reconquered Palestine
    (935, 969, 'NOT_RELEVANT'),
    # Ikhshidid dynasty controlled Palestine from Egypt. ~7M births. <100M.
    (969, 1073, 'Fatimid Caliphate'),      # 126M births; controlled 99% of Palestine
    # GAP 1073-1099: Seljuk Empire (155M births; ~20M pop × 0.04 × 194 yrs) conquered
    # Palestine from Fatimids (1073). Fatimid Caliphate (126M births) contested and
    # briefly reconquered parts. Local Turkmen warlords held individual cities.
    # No single polity controlled 99%.
    # GAP 1099-1153: Crusader Kingdom of Jerusalem (<100M births) held most of Palestine
    # but Fatimid Caliphate (126M births) held Ascalon until 1153, controlling a
    # coastal city with meaningful population share.
    (1153, 1250, 'NOT_RELEVANT'),
    # After Ascalon fell (1153): Crusaders held all territory. <100M.
    # 1187: Ayyubids conquered most of Palestine. <100M.
    # Crusader remnants at Acre. All polities <100M.
    # GAP 1250-1291: Mamluk Sultanate (107M births) controlled most of Palestine.
    # Crusader states held Acre and coastal strip with >1% of population.
    (1291, 1516, 'Mamluk Sultanate'),      # 107M births; controlled 99% after fall of Acre
    (1516, 1918, 'Ottoman Empire'),        # 623M births; controlled 99%
    # GAP 1918-1920: British Empire (>100M births) occupied Palestine (OETA South).
    # Transitional military administration, not yet mandated. Technically no single
    # polity had internationally recognized 99% control.
    (1920, 1948, 'British Empire'),        # British Mandate of Palestine; controlled 99%
    (1948, 2026, 'NOT_RELEVANT'),
    # State of Israel: 16M births. Only sovereign polity in this territory. <100M.
]
