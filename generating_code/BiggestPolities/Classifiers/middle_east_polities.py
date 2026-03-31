"""
Complete polity timelines for Turkey, Iran, Iraq, Syria, and Lebanon.

Rules:
- NO_KNOWN_POLITIES: before first polity with >=100K people under centralized control
- NOT_RELEVANT: all polities had <100M lifetime births (avg_pop * 0.04 * years)
- Named polity: single polity controlled >=99% of modern country's population
- Gap (missing years): polities with >100M births existed but none controlled 99%
- End years are exclusive. Negative years are BCE.

Every gap is justified in comments with at least one polity exceeding 100M lifetime births.
"""

# =============================================================================
# TURKEY
# =============================================================================

TURKEY = [
    (-200000, -2000, 'NO_KNOWN_POLITIES'),
    # Hittite Old Kingdom emerges ~1650 BCE with >100K centralized population.
    # Using -2000 to account for earlier Hatti polities in central Anatolia.

    (-2000, -550, 'NOT_RELEVANT'),
    # Hittite Empire (~1650-1178 BCE): ~2-3M, 472 years -> ~38-57M births.
    # Phrygia (~1200-700 BCE): ~1-2M, 500 years -> ~20-40M births.
    # Lydia (~680-546 BCE): ~1-2M, 134 years -> ~5-11M births.
    # Urartu (~860-590 BCE): ~1M, 270 years -> ~11M births.
    # None reach 100M.

    (-550, -334, 'Achaemenid Empire'),
    # Cyrus conquered Lydia (546 BCE); all of Anatolia under Achaemenid satraps.
    # Empire total ~17-35M, 220 years -> 150-308M births. 99%+ of Anatolia.

    # GAP: -334 to 17 CE
    # After Alexander's conquest, Anatolia fragmented among successor kingdoms.
    # Seleucid Empire (>100M births: ~10-15M avg, 249 years -> ~100-150M) held
    # eastern Anatolia until ~188 BCE (Treaty of Apamea). Pergamon, Pontus,
    # Bithynia, Cappadocia, Galatia were independent — collectively well over 1%
    # of Anatolian population. Roman Republic/Empire (>100M births) annexed western
    # kingdoms from -133 onward but Cappadocia (~3-5% of Anatolian pop) remained
    # a client kingdom until 17 CE. No single polity controlled 99%.

    (17, 395, 'Roman Empire'),
    # Cappadocia annexed 17 CE. Only tiny Commagene remained (annexed 72 CE, <1%
    # of Anatolian population). 99%+ under direct Roman control.

    (395, 611, 'Byzantine Empire'),
    # Eastern Roman Empire held all of Anatolia after the 395 division.

    # GAP: 611 to 628
    # Sassanid Empire (>100M births: ~12M avg, 427 years -> ~205M births) occupied
    # large portions of Anatolia during the Byzantine-Sassanid War of 602-628,
    # including regions reaching Chalcedon opposite Constantinople. Significant
    # share (>1%) of Anatolian population under Sassanid control.

    (628, 1071, 'Byzantine Empire'),
    # Heraclius recovered Anatolia from Sassanids. Byzantine control remained
    # intact despite Arab frontier raids (640s-960s). Arab-held frontier zones
    # in SE Anatolia contained <1% of total Anatolian population. Ends at
    # Battle of Manzikert (1071).

    # GAP: 1071 to 1517
    # After Manzikert, Seljuk Sultanate of Rum took central/eastern Anatolia;
    # Byzantine Empire (>100M births: ~12M avg for 1000+ years) held western
    # Anatolia. Neither controlled 99%. Mongol Ilkhanate (part of Mongol Empire,
    # >100M births) dominated eastern Anatolia after 1243. Ottoman beylik grew
    # from ~1299; fragmented by Timur (1402); reunified ~1420s-1460s. Trebizond
    # fell 1461, Karamanids subdued by 1487, Dulkadir annexed 1515.

    (1517, 1922, 'Ottoman Empire'),
    # By 1517, Ottomans controlled 99%+ of Anatolia (Dulkadir annexed 1515,
    # Mamluk Sultanate conquered 1517). ~20-35M avg empire population,
    # 623 years -> easily >100M births.

    # GAP: 1922 to 1923
    # Transition period: Ottoman Empire dissolved, Turkish War of Independence,
    # Lausanne Treaty. Republic of Turkey (>100M births: ~20-80M avg, 103 years)
    # was the successor state being established during this gap.

    (1923, 2026, 'Republic of Turkey'),
    # Founded October 29, 1923.
]

# =============================================================================
# IRAN
# =============================================================================

IRAN = [
    (-200000, -2700, 'NO_KNOWN_POLITIES'),
    # Proto-Elamite/Elamite civilization reached 100K+ centralized pop by ~2700 BCE.

    (-2700, -550, 'NOT_RELEVANT'),
    # Elamite kingdoms (~2700-539 BCE): peak ~1-2M, ~500 years -> ~20-40M births.
    # Median Empire (~678-550 BCE): ~2-4M, 128 years -> ~10-20M births.
    # None approach 100M.

    (-550, -330, 'Achaemenid Empire'),
    # Founded by Cyrus the Great. Controlled all of Iran and far beyond.
    # ~17-35M total pop, 220 years -> 150-308M births. 99%+ of Iran.

    (-330, -311, 'Macedonian Empire'),
    # Alexander conquered the entire Achaemenid Empire, inheriting its population
    # base (>100M births counting inherited territories). After his death (323 BCE),
    # the eastern satrapies were contested; Seleucus gained control by ~311 BCE.

    (-311, -247, 'Seleucid Empire'),
    # Seleucus controlled Iran from ~311 BCE (recapture of Babylon). Eastern fringe
    # ceded to Mauryas (~305 BCE) but that territory is in modern Afghanistan/
    # Pakistan, not Iran. 99%+ of modern Iran under Seleucid satraps.

    # GAP: -247 to -141
    # Parthian Empire growing in northeastern Iran (Arsaces I revolted 247 BCE)
    # while Seleucid Empire (>100M births: ~10-15M avg, 249 years -> ~100-150M)
    # still controlled western/central Iran. Neither held 99% of modern Iran.

    (-141, 224, 'Parthian Empire'),
    # Mithridates I captured Seleucia-on-Tigris in 141 BCE, completing Parthian
    # control of Iran. ~8-10M avg, 365 years -> ~117-146M births. 99%+.

    (224, 651, 'Sassanid Empire'),
    # Ardashir I overthrew last Parthian king. Controlled all of Iran.
    # ~10-15M avg, 427 years -> ~171-257M births.

    (651, 661, 'Rashidun Caliphate'),
    # Arab conquest of Iran completed ~651 (death of Yazdegerd III).

    (661, 750, 'Umayyad Caliphate'),
    # Controlled all of Iran. ~30-40M total empire pop, 89 years -> ~107-142M births.

    (750, 821, 'Abbasid Caliphate'),
    # Abbasid revolution began in Khorasan. Controlled all of Iran directly until
    # Tahirid appointment in 821.

    # GAP: 821 to 1231
    # Semi-independent dynasties: Tahirids (821-873), Saffarids (861-1003),
    # Samanids (819-999), Buyids (934-1062), Ghaznavids (977-1186),
    # Seljuk Empire (1037-1194), Khwarazmian Empire (1077-1231).
    # Abbasid Caliphate (>100M births: ~20-25M avg, 508 years -> ~406-508M)
    # remained nominal overlord but lacked real control. Seljuk Empire
    # (borderline >100M births: ~15-20M avg, 157 years -> ~94-126M) controlled
    # most of Iran at peak but not 99% continuously (Ghaznavids held east).
    # No single polity controlled 99%.

    (1231, 1335, 'Mongol Empire'),
    # Mongol conquest of Khwarazmian Empire completed by ~1231. Iran under
    # Mongol Ilkhanate. Mongol Empire total population >100M.

    (1335, 1501, 'NOT_RELEVANT'),
    # Post-Ilkhanate fragmentation: Jalairids (~1335-1432), Muzaffarids (1314-1393),
    # Timurid Empire (1370-1507), Qara Qoyunlu (1374-1468), Aq Qoyunlu (1378-1508).
    # Timurid Empire is largest: ~10-15M avg, 137 years -> ~55-82M births. Under 100M.

    (1501, 1722, 'Safavid Empire'),
    # Ismail I conquered Iran, establishing Twelver Shia Islam. ~6-10M avg,
    # 221 years -> ~53-88M births. Controlled 99%+ of Iran by ~1510.

    # GAP: 1722 to 1736
    # Afghan Hotaki dynasty invaded and captured Isfahan (1722). Remnant Safavids
    # and Afshar forces (under Nader) contested the north/east. Ottoman Empire
    # (>100M births: ~20-35M avg, 623 years -> easily >500M) seized western
    # Iranian provinces (1723-1727). No single polity controlled 99%.

    (1736, 1747, 'Afsharid dynasty'),
    # Nader Shah reunified Iran, expelled Afghans and Ottomans. 99%+ control.

    (1747, 1796, 'NOT_RELEVANT'),
    # Post-Nader Shah fragmentation: Zand dynasty (~5-6M, 47 years -> ~9-11M),
    # Afsharid remnants in Khorasan, Durrani Empire in eastern fringes.
    # All polities <100M lifetime births.

    (1796, 1925, 'Qajar dynasty'),
    # Agha Mohammad Khan reunified Iran. 99%+ control. Lost some peripheral
    # territories (Herat, Caucasus) but core modern Iran intact.

    (1925, 1979, 'Pahlavi dynasty'),
    # Reza Shah deposed last Qajar. Brief Anglo-Soviet occupation (1941-1946)
    # but Iranian sovereignty maintained.

    (1979, 2026, 'Islamic Republic of Iran'),
]

# =============================================================================
# IRAQ
# =============================================================================

IRAQ = [
    (-200000, -3000, 'NO_KNOWN_POLITIES'),
    # Sumerian city-states (Uruk, Ur) reached 100K+ centralized pop by ~3000 BCE
    # during the Early Dynastic period.

    (-3000, -550, 'NOT_RELEVANT'),
    # Akkadian Empire (~2334-2154 BCE): ~1-2M, 180 years -> ~7-14M births.
    # Ur III (~2112-2004 BCE): ~1-2M, 108 years -> ~4-9M births.
    # Old Babylonian (~1894-1595 BCE): ~1-2M, 299 years -> ~12-24M births.
    # Kassite Babylonia (~1595-1155 BCE): ~1-2M, 440 years -> ~18-35M births.
    # Neo-Assyrian Empire (~911-609 BCE): ~4-5M, 302 years -> ~48-60M births.
    # Neo-Babylonian Empire (~626-539 BCE): ~3-4M, 87 years -> ~10-14M births.
    # None reach 100M.

    (-550, -330, 'Achaemenid Empire'),
    # Cyrus conquered Babylon (539 BCE). Controlled all of Mesopotamia. >100M births.

    (-330, -311, 'Macedonian Empire'),
    # Alexander conquered the Achaemenid Empire. Babylon was his intended capital.
    # After his death (323 BCE), Wars of the Diadochi; Seleucus took Babylon ~311.

    (-311, -141, 'Seleucid Empire'),
    # Seleucus I built Seleucia-on-Tigris as capital. 99%+ of Iraq under Seleucid
    # control until Parthian conquest.

    (-141, 224, 'Parthian Empire'),
    # Mithridates I captured Seleucia-on-Tigris. Controlled all of Iraq.
    # Brief Roman incursion (Trajan 116-117 CE) but no lasting control.

    (224, 637, 'Sassanid Empire'),
    # Ardashir I defeated last Parthian king. Ctesiphon (in modern Iraq) was
    # the Sassanid capital. 99%+ control.

    (637, 661, 'Rashidun Caliphate'),
    # Battle of Qadisiyyah (636-637). Kufa and Basra founded.

    (661, 750, 'Umayyad Caliphate'),

    (750, 946, 'Abbasid Caliphate'),
    # Baghdad founded as capital (762). Iraq was the caliphate's heartland.
    # Direct control until Buyid takeover of Baghdad in 945-946.

    (946, 1055, 'Buyid Confederacy'),
    # Buyids captured Baghdad. Abbasid caliph remained as figurehead.
    # Buyid Iraq branch controlled 99%+ of Iraq.

    # GAP: 1055 to 1258
    # Seljuk Empire (borderline >100M births: ~15-20M avg, 157 years -> ~94-126M)
    # took Baghdad from Buyids in 1055 but fragmented after ~1118. Zengids/atabegs
    # controlled northern Iraq while the Abbasid Caliphate (>100M births: ~20-25M
    # avg, 508 years -> ~406-508M) recovered real power in central/southern Iraq
    # (especially under Caliph al-Nasir, ~1180-1225). No single polity controlled
    # 99% of modern Iraq.

    (1258, 1335, 'Mongol Empire'),
    # Hulagu sacked Baghdad (1258), ending the Abbasid Caliphate. Iraq under
    # Mongol Ilkhanate. Mongol Empire total population >100M.

    (1335, 1534, 'NOT_RELEVANT'),
    # Jalairid Sultanate (~1335-1432), Timurid invasions (1393, 1401),
    # Qara Qoyunlu (1374-1468), Aq Qoyunlu (1378-1508), Safavids (1508-1534).
    # Timurid Empire is largest: ~10-15M avg, 137 years -> ~55-82M births.
    # Safavid Empire: ~6-10M avg, 221 years -> ~53-88M births.
    # All polities <100M lifetime births.

    (1534, 1623, 'Ottoman Empire'),
    # Suleiman the Magnificent conquered Baghdad (1534). 99%+ control.

    # GAP: 1623 to 1638
    # Safavid Empire recaptured Baghdad (1623). Ottoman Empire (>100M births)
    # and Safavids contested Iraq. Neither controlled 99%.

    (1638, 1920, 'Ottoman Empire'),
    # Murad IV recaptured Baghdad (1638). Three vilayets: Mosul, Baghdad, Basra.

    (1920, 1932, 'British Mandate of Mesopotamia'),

    (1932, 1958, 'Kingdom of Iraq'),

    (1958, 2026, 'Republic of Iraq'),
    # Various republican governments. US-led occupation (2003-2011) but Iraqi
    # government maintained sovereignty. ISIS held territory 2014-2017 but
    # government retained control of major population centers (>99%).
]

# =============================================================================
# SYRIA
# =============================================================================

SYRIA = [
    (-200000, -2500, 'NO_KNOWN_POLITIES'),
    # Ebla (~2500 BCE) — first centralized polity with 100K+ in Syrian territory.

    (-2500, -550, 'NOT_RELEVANT'),
    # Ebla (~2500-2250 BCE): ~100-200K, 250 years -> ~1-2M births.
    # Yamhad (~1810-1517 BCE): ~200-500K, 293 years -> ~2-6M births.
    # Mittani (~1500-1270 BCE): ~1-2M, 230 years -> ~9-18M births.
    # Neo-Assyrian Empire: ~4-5M, 302 years -> ~48-60M births.
    # None reach 100M.

    (-550, -334, 'Achaemenid Empire'),
    # Controlled all of Syria as "Beyond the River" satrapy. >100M births.

    # GAP: -334 to -200
    # After Alexander's conquest, Syria was divided: Seleucid Empire (>100M births)
    # held northern/inland Syria; Ptolemaic Kingdom held southern Syria (Coele-Syria,
    # ~10-20% of modern Syria's population) from ~301 to ~200 BCE. Neither controlled
    # 99% of modern Syria's population.

    (-200, -64, 'Seleucid Empire'),
    # After the Fifth Syrian War (202-195 BCE), Seleucids controlled all of Syria.
    # Syria was the empire's core territory until Pompey's annexation (64 BCE).

    (-64, 395, 'Roman Empire'),
    # Province of Syria. Brief Palmyrene Empire (267-272 CE) too short to break this.

    (395, 636, 'Byzantine Empire'),
    # Sassanid occupation (611-628) was temporary; Byzantine sovereignty restored.

    (636, 661, 'Rashidun Caliphate'),
    # Battle of Yarmouk (636). Damascus fell to Arab armies.

    (661, 750, 'Umayyad Caliphate'),
    # Damascus was the Umayyad capital. Syria was the caliphate's heartland.

    (750, 878, 'Abbasid Caliphate'),
    # Capital moved to Baghdad but Syria under direct Abbasid control until
    # Tulunid conquest (878).

    # GAP: 878 to 1300
    # Fragmented among many powers: Tulunids (878-905), Ikhshidids (935-969),
    # Fatimid Caliphate (southern Syria from 969), Hamdanids (northern Syria
    # from 945), Byzantines (Antioch region from 969), Crusader states (from 1098),
    # Zengids, Ayyubids (from ~1174). Abbasid Caliphate (>100M births: ~20-25M avg,
    # 508 years -> ~406-508M) was nominal overlord. Mongol Empire (>100M births)
    # invaded 1260 (defeated at Ain Jalut). No single polity controlled 99%.

    (1300, 1516, 'Mamluk Sultanate'),
    # After defeating Mongols (1260) and expelling Crusaders (Acre 1291), Mamluks
    # controlled all of Syria by ~1300. 99%+ control.

    (1516, 1918, 'Ottoman Empire'),
    # Selim I defeated Mamluks at Marj Dabiq (1516). Four centuries of control.

    # GAP: 1918 to 1920
    # Post-WWI transition. Arab Kingdom of Syria (Faisal, 1918-1920) briefly
    # existed but was not recognized by all powers. France (French colonial empire,
    # >100M births: ~40-60M avg metropole + colonies, 400+ years of colonial
    # activity) had League of Nations mandate rights. British forces also present.

    (1920, 1946, 'French Mandate of Syria'),

    (1946, 1958, 'Syrian Republic'),

    (1958, 1961, 'United Arab Republic'),
    # Union with Egypt under Nasser. Syria was the "Northern Region."

    (1961, 2011, 'Syrian Republic'),
    # Ba'ath Party rule from 1963. Assad dynasty from 1970.

    # GAP: 2011 to 2026
    # Syrian Civil War. Government lost control of large territories to ISIS,
    # Kurdish SDF, and rebel factions. Republic of Turkey (>100M births: ~20-80M
    # avg, 103 years -> ~200M+) controlled zones in northern Syria via military
    # operations (Euphrates Shield, Olive Branch, Peace Spring). Russian Federation
    # (>100M births: ~145M, 34 years -> ~197M) had military bases and operational
    # control in western Syria. Assad fell late 2024; transitional government has
    # not consolidated 99% control (Kurdish NE Syria autonomous).
]

# =============================================================================
# LEBANON
# =============================================================================

LEBANON = [
    (-200000, -1500, 'NO_KNOWN_POLITIES'),
    # Phoenician city-states (Byblos, Sidon, Tyre) existed from ~3000 BCE but
    # individual city-states didn't reach 100K under centralized control of
    # Lebanese territory. Egyptian New Kingdom exercised suzerainty over the
    # Lebanese coast from ~1500 BCE with >100K under centralized governance.

    (-1500, -550, 'NOT_RELEVANT'),
    # Egyptian New Kingdom (~1500-1200 BCE): ~3-4M, 480 years -> ~58-77M births.
    # Independent Phoenician city-states (~1200-550 BCE): each <100K.
    # Neo-Assyrian control (~740-627 BCE): Assyria ~48-60M births.
    # Neo-Babylonian control (~605-539 BCE): ~10-14M births.
    # All polities <100M lifetime births.

    (-550, -334, 'Achaemenid Empire'),
    # Phoenician cities were key naval assets of the empire. 99%+ of Lebanese
    # territory under Persian control.

    # GAP: -334 to -200
    # After Alexander's conquest (>100M births), Lebanon was contested between
    # Ptolemaic Kingdom (held Sidon, Tyre, southern coast) and Seleucid Empire
    # (>100M births; held Bekaa Valley and northern regions). Neither controlled
    # 99% of modern Lebanon.

    (-200, -64, 'Seleucid Empire'),
    # After Fifth Syrian War, Seleucids controlled all of Lebanon. Local Ituraean
    # kingdom in Bekaa Valley had <1% of coastal population.

    (-64, 395, 'Roman Empire'),
    # Pompey annexed Syria including Lebanon. Berytus (Beirut) became a major
    # Roman colony and center of Roman law.

    (395, 636, 'Byzantine Empire'),

    (636, 661, 'Rashidun Caliphate'),

    (661, 750, 'Umayyad Caliphate'),

    (750, 878, 'Abbasid Caliphate'),

    # GAP: 878 to 1300
    # Same fragmentation as Syria: Tulunids, Fatimid Caliphate (from ~970s),
    # Crusader County of Tripoli (1109-1289, northern Lebanon), Crusader Kingdom
    # of Jerusalem (southern coast). Abbasid Caliphate (>100M births) was nominal
    # overlord in earlier period. Mongol Empire (>100M births) invaded 1260.
    # No single polity controlled 99%.

    (1300, 1516, 'Mamluk Sultanate'),
    # Crusaders expelled (Tripoli fell 1289). Mamluks controlled all of Lebanon.
    # Mount Lebanon had semi-autonomous Druze/Maronite communities but under
    # Mamluk suzerainty. 99%+ of population.

    (1516, 1918, 'Ottoman Empire'),
    # Mount Lebanon had special autonomy (Emirate, later Mutasarrifate from 1861)
    # but remained under Ottoman sovereignty. 99%+ under Ottoman political control.

    # GAP: 1918 to 1920
    # Post-WWI transition. Same situation as Syria: British/Arab forces, then
    # French mandate assigned. France (colonial empire, >100M births) was the
    # incoming power.

    (1920, 1943, 'French Mandate of Lebanon'),
    # Greater Lebanon created under French mandate.

    (1943, 1975, 'Republic of Lebanon'),
    # Independence (1943). National Pact established confessional power-sharing.

    (1975, 1990, 'NOT_RELEVANT'),
    # Lebanese Civil War. Multiple factions controlled different areas.
    # Syrian Republic (~10M avg, 65 years -> ~26M births): occupied much of Lebanon.
    # Israel (~5M avg, 78 years -> ~16M births): occupied southern Lebanon.
    # All polities involved had <100M lifetime births.

    (1990, 2026, 'Republic of Lebanon'),
    # Taif Agreement ended civil war. Syrian military presence until 2005 but
    # Lebanese government maintained sovereignty. 99%+ under Lebanese state.
]

# =============================================================================
# COMBINED OUTPUT
# =============================================================================

POLITY_TIMELINES = {
    'Turkey': TURKEY,
    'Iran': IRAN,
    'Iraq': IRAQ,
    'Syria': SYRIA,
    'Lebanon': LEBANON,
}

# Print summary
if __name__ == '__main__':
    for country, timeline in POLITY_TIMELINES.items():
        print(f"\n{'='*70}")
        print(f"  {country}")
        print(f"{'='*70}")
        prev_end = None
        for start, end, polity in timeline:
            if prev_end is not None and start > prev_end:
                gap_start = prev_end
                gap_end = start
                yr_s = f"{abs(gap_start)} BCE" if gap_start < 0 else f"{gap_start} CE"
                yr_e = f"{abs(gap_end)} BCE" if gap_end < 0 else f"{gap_end} CE"
                print(f"  {'*** GAP: ' + yr_s + ' to ' + yr_e + ' ***':>50s}")
            yr_s = f"{abs(start)} BCE" if start < 0 else f"{start} CE"
            yr_e = f"{abs(end)} BCE" if end < 0 else f"{end} CE"
            print(f"  {yr_s:>12s} - {yr_e:<12s}  {polity}")
            prev_end = end
