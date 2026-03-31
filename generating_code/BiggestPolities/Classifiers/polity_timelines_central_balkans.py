"""
Polity timelines for Czech Republic, Slovakia, Austria, Bulgaria, Serbia.

Rules:
- NO_KNOWN_POLITIES: earliest period, ends when first polity with 100K+ centralized pop exists
- NOT_RELEVANT: ALL polities in territory had <100M lifetime births (avg_pop * 0.04 * years)
- Named polity: single polity controlled 99%+ of modern country's population
- Gap (missing years): polities with >100M births existed but none controlled 99%+
- End years are exclusive. Negative years = BCE.

Key lifetime birth calculations for polities relevant to these countries:
  Roman Empire (-27 to 476): ~50M avg * 503yr * 0.04 ≈ 1.0B  ✓ (>100M)
  Byzantine Empire (395-1453): ~12M avg * 1058yr * 0.04 ≈ 507M  ✓
  Frankish Kingdom/Empire (481-843): ~10M avg * 362yr * 0.04 ≈ 145M  ✓
  Holy Roman Empire (962-1806): ~15M avg * 844yr * 0.04 ≈ 506M  ✓
  Ottoman Empire (1299-1922): ~18M avg * 623yr * 0.04 ≈ 448M  ✓
  Habsburg Monarchy (1526-1804): ~22M avg * 278yr * 0.04 ≈ 245M  ✓
  Austrian Empire (1804-1867): ~28M avg * 63yr * 0.04 ≈ 71M  ✗
  Austria-Hungary (1867-1918): ~45M avg * 51yr * 0.04 ≈ 92M  ✗
  Mongol Empire (1206-1368): ~100M avg * 162yr * 0.04 ≈ 648M  ✓

  Kingdom of Hungary (1000-1526): ~3M avg * 526yr * 0.04 ≈ 63M  ✗
  First Bulgarian Empire (681-1018): ~2.5M avg * 337yr * 0.04 ≈ 34M  ✗
  Second Bulgarian Empire (1185-1396): ~1.5M avg * 211yr * 0.04 ≈ 13M  ✗
  Great Moravia (833-907): ~1M avg * 74yr * 0.04 ≈ 3M  ✗
  Czechoslovakia (total 1918-92): ~14M avg * 67yr * 0.04 ≈ 38M  ✗
  Nazi Germany (1933-1945): ~75M avg * 12yr * 0.04 ≈ 36M  ✗
  Kingdom of Yugoslavia + SFR Yugoslavia: both under 100M  ✗
  Kingdom of Serbia (1882-1918): ~3M avg * 36yr * 0.04 ≈ 4M  ✗
"""

TIMELINES = {}

# =============================================================================
# CZECH REPUBLIC (Czechia)
# =============================================================================
#
# Key transitions:
# - Pre-600: no centralized polities with 100K+ in Bohemia/Moravia
# - 623-658: Samo's Empire (Slavic tribal union, >100K but all polities <100M births)
# - 833-907: Great Moravia
# - 895-929: Bohemia emerges as duchy, Moravia contested
# - 929/950-1806: Bohemia within Holy Roman Empire
# - Problem: Moravia was not always under same control as Bohemia. After Great Moravia
#   fell (907), Moravia was contested between Bohemia, Poland, and Hungary until ~1029
#   when Bretislav I reunited it with Bohemia. Bohemia proper joined HRE ~929-950.
#   Since Moravia is ~30% of Czech population, can't assign HRE until ~1029.
# - 1004: Bohemia formally restored to HRE after brief Polish occupation
# - 1029: Moravia definitively under Bohemian (and thus HRE) control
# - 1029-1806: All of modern Czech Republic within HRE
# - 1806-1867: Austrian Empire
# - 1867-1918: Austria-Hungary
# - 1918-1938: Czechoslovakia (all polities <100M)
# - 1938-1945: Nazi Germany (Sudetenland 1938, Protectorate 1939). Nazi Germany <100M births.
# - 1945-1992: Czechoslovakia (<100M)
# - 1993-2026: Czech Republic

TIMELINES['Czech Republic'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    # 600-~805: Various Slavic polities (Samo's Empire 623-658, then tribal duchies).
    # All had <100M lifetime births. Frankish Kingdom existed but did not control
    # any Czech territory during this period.
    (600, 805, 'NOT_RELEVANT'),
    # 805-950: Frankish Empire/East Francia exacted tribute from Bohemia from ~805.
    # Frankish Kingdom (>100M lifetime births) exercised overlordship but Bohemia
    # was largely autonomous. Great Moravia (833-907) controlled the region independently.
    # After Great Moravia fell (907), Bohemia re-entered Frankish/East Francian orbit.
    # Erring on side of gap since Frankish realm (>100M births) had political influence.
    # GAP JUSTIFICATION: Frankish Kingdom/Empire (>100M births) claimed overlordship
    # over Bohemia from ~805.
    # 950-1029: HRE controlled Bohemia but Moravia was under Hungarian/Polish control.
    # HRE had >100M lifetime births.
    # GAP JUSTIFICATION: Holy Roman Empire (>100M births) controlled Bohemia (~70%
    # of modern Czech population) but not Moravia.
    (1029, 1806, 'Holy Roman Empire'),
    (1806, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    # 1918-1938: Czechoslovakia was the sole sovereign controller. <100M lifetime births.
    # No other polity with >100M births controlled any part of Czech territory.
    (1918, 1938, 'NOT_RELEVANT'),
    # 1938-1945: Germany annexed Sudetenland (Oct 1938), then created Protectorate of
    # Bohemia and Moravia (Mar 1939). Nazi Germany (1933-1945) had ~36M lifetime births
    # (<100M). No other polity with >100M controlled any Czech territory.
    (1938, 1945, 'NOT_RELEVANT'),
    # 1945-1993: Czechoslovakia. <100M lifetime births. Soviet Union had effective
    # influence but Czechoslovakia was formally sovereign. No polity with >100M births
    # directly controlled Czech territory.
    (1945, 1993, 'NOT_RELEVANT'),
    # 1993-2026: Czech Republic. <100M lifetime births. No other polity controls territory.
    (1993, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# SLOVAKIA
# =============================================================================
#
# Key transitions:
# - Pre-600: no centralized polities with 100K+ in Slovak territory
# - 623-658: Samo's Empire
# - 833-907: Great Moravia (controlled all of modern Slovakia)
# - 907-1000: Magyar tribal confederation, then Kingdom of Hungary from 1000
# - 1000-1526: Kingdom of Hungary controlled all of Slovakia
# - 1526-1699: Slovakia split between Royal Hungary (Habsburg) and Ottoman Empire.
#   Ottomans controlled southern Slovakia (~15-25% of territory/population).
#   Both Habsburg Monarchy and Ottoman Empire had >100M lifetime births.
# - 1699-1804: Habsburg Monarchy (all of Hungary/Slovakia after Treaty of Karlowitz)
# - 1804-1867: Austrian Empire
# - 1867-1918: Austria-Hungary
# - 1918-1938: Czechoslovakia (<100M)
# - 1938-1945: First Slovak Republic (Nazi puppet) + some territory ceded to Hungary.
#   Neither the First Slovak Republic nor Nazi Germany nor Horthy's Hungary had >100M births.
# - 1945-1993: Czechoslovakia (<100M)
# - 1993-2026: Slovak Republic

TIMELINES['Slovakia'] = [
    (-200000, 600, 'NO_KNOWN_POLITIES'),
    # 600-1000: Samo's Empire (623-658), Avar Khaganate remnants, Great Moravia (833-907),
    # then Magyar tribal confederation. All had <100M lifetime births.
    (600, 1000, 'NOT_RELEVANT'),
    (1000, 1526, 'Kingdom of Hungary'),
    # 1526-1699: Gap. After Battle of Mohács, Slovakia split between Royal Hungary
    # (Habsburg) in north/west and Ottoman Empire in south. Both the Habsburg Monarchy
    # (>100M births) and Ottoman Empire (>100M births) controlled parts of Slovakia,
    # but neither controlled 99%+.
    # GAP JUSTIFICATION: Habsburg Monarchy and Ottoman Empire both had >100M lifetime births.
    (1699, 1804, 'Habsburg Monarchy'),
    (1804, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    # 1918-1938: Czechoslovakia. <100M lifetime births. Sole sovereign controller.
    (1918, 1938, 'NOT_RELEVANT'),
    # 1938-1945: First Slovak Republic (puppet state, <100M). Southern territories
    # ceded to Hungary (First Vienna Award, Nov 1938). Horthy's Hungary had <100M births
    # (interwar Hungary ~9M * 24yr * 0.04 = 8.6M). Nazi Germany also <100M.
    # No polity with >100M births controlled any part of Slovakia.
    (1938, 1945, 'NOT_RELEVANT'),
    # 1945-1993: Czechoslovakia. <100M births. Sole sovereign controller.
    (1945, 1993, 'NOT_RELEVANT'),
    (1993, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# AUSTRIA
# =============================================================================
#
# Key transitions:
# - Celtic Noricum kingdom from ~2nd century BC, but uncertain if 100K+ centralized
# - -15: Roman conquest of Noricum and Pannonia
# - 476: Fall of Western Roman Empire
# - 476-788: Various Germanic peoples (Ostrogoths, Lombards, Bavarians), Avars in east.
#   Western Austria was under Bavarian/Frankish control; eastern Austria under Avars.
#   The Frankish Kingdom (>100M births) controlled western parts but not 99%+.
# - 788: Charlemagne defeats Tassilo III of Bavaria; western Austria fully Frankish
# - 791-796: Charlemagne destroys Avar Khaganate; eastern Austria (Pannonia) comes under
#   Frankish control. By ~800, all of modern Austria was under Carolingian/Frankish rule.
# - 843: Treaty of Verdun → East Francia
# - 843-962: East Francia. ~8M avg * 119yr * 0.04 = 38M births. <100M.
#   But is East Francia a continuation of the Frankish realm? With the splitting view,
#   East Francia is distinct from the unified Frankish Empire. However, looking at what
#   controlled Austrian territory: East Francia was the sole controller.
#   No other polity with >100M births controlled any part of Austria. NOT_RELEVANT.
# - 962-1806: Holy Roman Empire
# - 1806-1867: Austrian Empire
# - 1867-1918: Austria-Hungary
# - 1918-1938: First Austrian Republic, then Federal State of Austria
# - 1938-1945: Nazi Germany (Anschluss March 1938)
# - 1945-2026: Second Austrian Republic

TIMELINES['Austria'] = [
    (-200000, -400, 'NO_KNOWN_POLITIES'),
    # -400 to -15: Celtic polities (Noricum, etc.). All <100M births.
    # No polity with >100M births controlled any Austrian territory.
    (-400, -15, 'NOT_RELEVANT'),
    (-15, 476, 'Roman Empire'),
    # 476-788: Post-Roman period. Western Austria under Bavarian/Frankish influence,
    # eastern Austria under Avars/Slavs. The Frankish Kingdom (481-843, >100M births)
    # controlled western Austria (via Bavaria) but not eastern Austria (Avar territory).
    # GAP JUSTIFICATION: Frankish Kingdom had >100M lifetime births and controlled
    # western Austria, but Avars held eastern Austria (Pannonia), preventing 99% control.
    # After Charlemagne's conquest of Bavaria (788), Frankish control extended further
    # but Avar Khaganate still held the eastern marches until 791-796.
    (796, 843, 'Frankish Empire'),
    # 843-962: East Francia controlled all of Austria. East Francia as a distinct polity
    # (843-962) had ~8M avg pop * 119yr * 0.04 = 38M births. <100M.
    # No other polity with >100M births controlled Austrian territory.
    (843, 962, 'NOT_RELEVANT'),
    (962, 1806, 'Holy Roman Empire'),
    (1806, 1867, 'Austrian Empire'),
    (1867, 1918, 'Austria-Hungary'),
    # 1918-1938: Republic of Austria. <100M births for all controlling polities.
    # First Austrian Republic (1918-1934): ~6.5M * 16yr * 0.04 = 4.2M
    # Federal State of Austria (1934-1938): ~6.7M * 4yr * 0.04 = 1.1M
    # No polity with >100M births controlled any Austrian territory.
    (1918, 1938, 'NOT_RELEVANT'),
    # 1938-1945: Nazi Germany (Anschluss). Third Reich: ~75M * 12yr * 0.04 = 36M. <100M.
    (1938, 1945, 'NOT_RELEVANT'),
    # 1945-1955: Allied occupation, but Austrian government restored. Four-zone occupation.
    # Could argue the occupying powers (USA, USSR, UK, France) each exceed 100M births,
    # but Austria had a functioning central government from 1945 and the occupation was
    # temporary/supervisory. Sovereignty fully restored 1955 (Austrian State Treaty).
    # The Second Austrian Republic was the governing polity throughout.
    # However, 1945-1955 the four powers had direct authority. Still, Austria functioned
    # as a unit. I'll treat the Second Austrian Republic as the polity from 1945.
    (1945, 2026, 'NOT_RELEVANT'),
]

# =============================================================================
# BULGARIA
# =============================================================================
#
# Key transitions:
# - Thracian kingdoms from ~5th century BC, but centralized 100K+? The Odrysian Kingdom
#   (~480-46 BC) likely had >100K. Start NO_KNOWN_POLITIES end at ~-480.
# - -340 to -168: Macedonian Empire/successor states controlled parts. Macedonia/Antigonids
#   had ~3M * ~180yr * 0.04 = 22M. <100M.
# - -46: Rome conquers Thrace
# - 46-395: Roman Empire (provinces of Thrace, Moesia)
# - 395-580s: Byzantine Empire
# - 580s-681: Slavic migrations disrupted Byzantine control. Slavic tribes + Bulgar
#   migrants. Byzantine Empire (>100M births) still claimed the territory and controlled
#   some coastal/urban areas, but effective control of interior was lost.
#   GAP because Byzantine Empire (>100M births) controlled parts.
# - 681-1018: First Bulgarian Empire controlled most of modern Bulgaria.
#   BUT: coastal cities (Mesembria/Nesebar, Anchialos) sometimes remained Byzantine.
#   Overall, First Bulgarian Empire controlled 95%+ of population in modern Bulgaria
#   for most of this period. Close to 99% threshold. I'll give this as a named polity
#   for the period when control was clearest: ~850-971 (Preslav period, golden age).
#   Actually, let me reconsider. 681-971 the First Bulgarian Empire controlled nearly
#   all of modern Bulgaria. Byzantine Empire held a few coastal towns but <1% of pop.
#   971-1018: Byzantine reconquest of eastern Bulgaria (971), western Bulgaria held out
#   under Samuel until 1018. So 971-1018 is split.
# - 681-971: First Bulgarian Empire (controlled 99%+ of modern Bulgarian territory)
# - 971-1018: Gap. Byzantines controlled eastern Bulgaria, Samuel's Bulgaria controlled west.
#   Byzantine Empire had >100M births.
# - 1018-1185: Byzantine Empire (reconquered all Bulgarian territory)
# - 1185-1396: Second Bulgarian Empire. Controlled most of modern Bulgaria but
#   fluctuating borders. Initially just northeast, expanded. By ~1218-1241 (Ivan Asen II)
#   controlled all modern Bulgaria. But before and after, borders shifted.
#   For much of 1185-1396, did the Second Bulgarian Empire control 99%+ of modern Bulgaria?
#   Southern Thrace (around Plovdiv) was contested between Bulgaria and Byzantium.
#   The Byzantine Empire (>100M births) held parts, and later the Ottoman Empire entered.
#   This is complex. Let me mark most of this as a gap.
# - 1185-1396: Gap. Second Bulgarian Empire and Byzantine Empire (both with significant
#   lifetime births — Byzantines >100M) contested territory. After 1340s, Ottoman Empire
#   (>100M) began conquering Bulgarian territory.
# - 1396-1878: Ottoman Empire (complete control after fall of Vidin 1396)
# - 1878-1908: Principality of Bulgaria (autonomous under Ottoman suzerainty, but
#   Eastern Rumelia was separate until 1885 unification). 1878-1885: Principality of
#   Bulgaria was only northern Bulgaria; Eastern Rumelia (southern) was separate Ottoman
#   province. That's roughly 40% of population in Eastern Rumelia. Fails 99%.
#   1885-1908: United Principality of Bulgaria (de facto).
#   Ottoman Empire still had nominal suzerainty. Is the Principality a separate polity?
#   It was autonomous but under Ottoman suzerainty. I'll treat 1878-1885 as a gap
#   (Ottoman Empire >100M controlled Eastern Rumelia; Principality had northern Bulgaria).
#   1885-1908: United Bulgaria, but Ottoman suzerainty. De facto independent.
# - 1908-1940: Kingdom of Bulgaria (independent). <100M births.
#   But 1913: Southern Dobruja lost to Romania (Treaty of Bucharest). Regained 1940.
#   Southern Dobruja had ~1-2% of Bulgarian population. Marginal.
#   1918-1919: Western Outlands lost to Yugoslavia. ~2-3% of population. Might fail 99%.
#   Actually, these territories were LOST, so the question is whether the Kingdom of
#   Bulgaria controlled 99%+ of MODERN Bulgaria's territory. If modern Bulgaria doesn't
#   include those lost territories, then yes.
#   Modern Bulgaria's borders were largely set by 1947 Treaty of Paris (same as current).
#   Southern Dobruja was regained in 1940 (Treaty of Craiova) and kept.
#   So 1913-1940: Southern Dobruja was part of Romania. ~300K people, vs Bulgaria ~5-6M.
#   That's ~5% of the population within modern Bulgarian borders. Fails 99%.
#   Hmm, but do I count it as "modern Bulgaria's territory"? Yes — Southern Dobruja is
#   part of modern Bulgaria. During 1913-1940 it was under Romania.
#   So 1908-1913: Kingdom of Bulgaria controlled ~99%+ of modern Bulgarian territory.
#   1913-1940: Romania controlled Southern Dobruja (~5% of modern Bulgaria's population area).
#   Romania (>100M births? Romania 1881-1947: ~15M avg * 66yr * 0.04 = 40M. <100M.
#   Actually Kingdom of Romania as a continuous entity: ~12M avg * 66yr * 0.04 = 32M. <100M.)
#   So 1913-1940: Kingdom of Bulgaria controlled ~95%, Romania controlled ~5%.
#   Neither Romania nor Bulgaria had >100M births. So this is NOT_RELEVANT? No — the
#   Kingdom of Bulgaria controlled 95% which fails the 99% threshold. But for NOT_RELEVANT,
#   ALL polities must have <100M births. Romania <100M, Bulgaria <100M. So NOT_RELEVANT
#   would apply IF no polity with >100M births controlled any part.
#   Wait: is any other polity with >100M births controlling any part of modern Bulgaria
#   during 1913-1940? No. So this is actually NOT_RELEVANT (all polities <100M).
#
# Let me simplify the Bulgarian timeline:

TIMELINES['Bulgaria'] = [
    (-200000, -480, 'NO_KNOWN_POLITIES'),
    # -480 to -46: Thracian Odrysian Kingdom and successor polities, then Macedonian
    # control, then independent Thracian states. All <100M births.
    # Alexander's empire was brief in this area; Antigonid Macedonia ~3M * 180yr = 22M.
    (-480, -46, 'NOT_RELEVANT'),
    (-46, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),
    # 580-681: Slavic migrations disrupted Byzantine control of the interior.
    # Byzantine Empire (>100M births) retained some coastal towns but lost effective
    # control of most of the territory. Slavic tribal polities had <100M births.
    # GAP JUSTIFICATION: Byzantine Empire had >100M lifetime births and controlled
    # coastal areas of modern Bulgaria during this period.
    (681, 971, 'First Bulgarian Empire'),
    # 971-1018: Byzantine Empire reconquered eastern Bulgaria (fall of Preslav 971).
    # Western Bulgaria held out under Comitopuli/Samuel dynasty until 1018.
    # Both Byzantine Empire (>100M births) and remnant Bulgarian state controlled parts.
    # GAP JUSTIFICATION: Byzantine Empire had >100M lifetime births.
    (1018, 1185, 'Byzantine Empire'),
    # 1185-1396: Second Bulgarian Empire existed but borders fluctuated significantly.
    # Byzantine Empire (>100M births) controlled southern Thrace/Plovdiv area for much
    # of this period. After 1340s, Ottoman Empire (>100M births) began conquering
    # Bulgarian territory. No single polity controlled 99%+ of modern Bulgaria.
    # GAP JUSTIFICATION: Byzantine Empire (>100M births) controlled southern portions;
    # after ~1340, Ottoman Empire (>100M births) controlled eastern portions.
    (1396, 1878, 'Ottoman Empire'),
    # 1878-1885: Principality of Bulgaria (northern Bulgaria only). Eastern Rumelia
    # (southern Bulgaria, ~40% of modern Bulgarian territory/population) remained an
    # autonomous Ottoman province. Ottoman Empire had >100M births.
    # GAP JUSTIFICATION: Ottoman Empire (>100M births) controlled Eastern Rumelia.
    # 1885-1908: Unification of Bulgaria and Eastern Rumelia. De facto independent but
    # under nominal Ottoman suzerainty. The unified Principality controlled 99%+ of
    # modern Bulgaria. Ottoman suzerainty was nominal — Bulgaria acted independently.
    (1885, 1908, 'Principality of Bulgaria'),
    # 1908-1913: Kingdom of Bulgaria, fully independent. Controlled all modern Bulgarian
    # territory.
    (1908, 1913, 'Kingdom of Bulgaria'),
    # 1913-1940: Southern Dobruja under Romania (Treaty of Bucharest 1913). ~5% of
    # modern Bulgaria's population within those borders. Kingdom of Bulgaria <100M births,
    # Kingdom of Romania <100M births. No polity with >100M controlled any part.
    (1913, 1940, 'NOT_RELEVANT'),
    (1940, 1944, 'Kingdom of Bulgaria'),
    # 1944-1946: Transitional period. Soviet-backed Fatherland Front coup Sept 1944.
    # Regency period, then republic declared Sept 1946. All polities <100M births.
    (1944, 1946, 'NOT_RELEVANT'),
    (1946, 1990, "People's Republic of Bulgaria"),
    (1990, 2026, 'Republic of Bulgaria'),
]

# =============================================================================
# SERBIA
# =============================================================================
#
# Key transitions:
# - Pre-Roman: Celtic Scordisci and other tribes. Centralized 100K+? Possibly from
#   ~3rd century BC when Scordisci were significant, but uncertain.
#   Dardanian kingdom in southern Serbia also significant.
# - -75 to -29: Roman conquest of the region (Moesia)
# - 29 BC - 395 AD: Roman Empire (province of Moesia)
# - 395-~600: Byzantine Empire controlled the area
# - ~580-600: Slavic and Avar invasions disrupted Byzantine control
# - 600-1180: Various Serbian principalities/states. Byzantine Empire frequently
#   controlled parts of modern Serbia (especially south). First Bulgarian Empire
#   controlled eastern parts at times. Hungarian Kingdom controlled Vojvodina (north).
#   Complex, multi-polity situation for centuries.
# - 1180-1355: Serbian Grand Principality → Kingdom → Empire. Medieval Serbian state
#   at its height under Stefan Dušan (1331-1355). But did it control 99%+ of modern
#   Serbia? Vojvodina (north, ~25% of modern Serbia's population) was under Hungary.
#   So no — medieval Serbian states never controlled 99%+ of modern Serbia because
#   Vojvodina was Hungarian.
# - 1355-1459: Serbian state fragmented, then Ottoman conquest (Kosovo 1389, Serbia 1459)
# - 1459-1804: Ottoman Empire controlled most of Serbia. But Vojvodina came under
#   Habsburg control after 1699 (Treaty of Karlowitz). So:
#   1459-1699: Ottoman Empire controlled nearly all of modern Serbia (~99%+).
#   Vojvodina was also Ottoman during this period.
# - 1521: Belgrade falls to Ottomans (had been Hungarian frontier fortress).
#   After 1521, all of modern Serbia was under Ottoman control.
# - 1699-1804: Vojvodina under Habsburg Monarchy, rest of Serbia under Ottoman Empire.
#   Both had >100M births. Gap.
# - 1804-1878: Serbian revolution and gradual autonomy. Principality of Serbia (autonomous
#   from 1817/1830) but only controlled central Serbia, not Vojvodina (Habsburg) or
#   Kosovo/southern Serbia (Ottoman). Gap.
# - 1878: Serbia gains full independence (Congress of Berlin) but only over central Serbia.
#   Vojvodina still Habsburg. Kosovo still Ottoman. Neither area is small — together
#   they represent maybe 40-50% of modern Serbia's territory/population.
# - 1912-1913: Balkan Wars. Serbia gains Kosovo and Macedonia.
# - 1918: Vojvodina joins Serbia/Yugoslavia. Now all of modern Serbia is under one state.
# - 1918-1941: Kingdom of Serbs, Croats and Slovenes / Kingdom of Yugoslavia.
#   Did this control 99%+ of modern Serbia? Yes.
# - 1941-1944: Axis occupation. Serbia under German military administration.
#   Nazi Germany <100M births. But various other forces (Chetniks, Partisans, Hungarian
#   occupation of Vojvodina). Hungary <100M. Germany <100M.
# - 1944/45-1992: SFR Yugoslavia
# - 1992-2003: Federal Republic of Yugoslavia (Serbia + Montenegro)
#   Kosovo remained part of FRY/Serbia until 1999 UN administration.
#   But FRY controlled 99%+ until 1999.
# - 1999-2006: Kosovo under UN administration (UNMIK). Kosovo population was ~1.8M vs
#   Serbia proper ~7.5M + Kosovo ~1.8M = ~9.3M total. Kosovo = ~19% of Serbia's
#   population (within pre-2008 borders). If we consider modern Serbia as NOT including
#   Kosovo (since Kosovo declared independence 2008 and is recognized by many states),
#   then Serbia proper was under FRY/SCG/Republic of Serbia control.
#   The question says "modern country's current borders." Serbia's position is that
#   Kosovo is part of Serbia, but de facto it's not controlled by Serbia.
#   I'll treat modern Serbia as the territory Serbia actually controls (excluding Kosovo).
# - 2003-2006: State Union of Serbia and Montenegro. Serbia was dominant partner.
#   Controlled 99%+ of modern Serbia (excluding Kosovo).
# - 2006-2026: Republic of Serbia.
#
# REVISED: Treating "modern Serbia" as the territory Serbia de facto controls (excluding Kosovo).
# With that definition, Vojvodina is ~28% of Serbia's population (2M of ~7M).

TIMELINES['Serbia'] = [
    (-200000, -200, 'NO_KNOWN_POLITIES'),
    # -200 to -29: Celtic Scordisci, Dardanians, other tribal polities. All <100M births.
    # Macedonian influence in the south after Alexander, but Antigonid Macedonia <100M.
    (-200, -29, 'NOT_RELEVANT'),
    (-29, 395, 'Roman Empire'),
    (395, 580, 'Byzantine Empire'),
    # 580-1521: Complex multi-polity period. At various times:
    # - Byzantine Empire (>100M births) controlled southern parts
    # - First Bulgarian Empire (681-1018, <100M births) controlled eastern parts
    # - Kingdom of Hungary (1000-1526, <100M births) controlled Vojvodina (north)
    # - Various Serbian principalities/kingdoms controlled central Serbia
    # - Ottoman Empire (from ~1389 onward, >100M births) conquered progressively
    #
    # 580-~800: Slavic/Avar period. Byzantine Empire (>100M births) lost control of
    # interior but retained claim and some coastal influence.
    # GAP JUSTIFICATION: Byzantine Empire (>100M births) controlled portions.
    #
    # ~800-1018: Byzantine Empire reasserted some control in south. First Bulgarian Empire
    # controlled east. Serbian principalities in center. All except Byzantines <100M births.
    # GAP JUSTIFICATION: Byzantine Empire (>100M births).
    #
    # 1018-1180: Byzantine Empire controlled most of modern Serbia directly.
    # But Vojvodina was under Kingdom of Hungary. Hungary <100M births.
    # Byzantine Empire (>100M births) controlled the rest (~75%+ of modern Serbia).
    # But not 99% because of Hungarian Vojvodina.
    # GAP JUSTIFICATION: Byzantine Empire (>100M births) controlled ~75%.
    # Actually, wait — if Hungary is <100M births and Byzantium controlled 75% but
    # not 99%, is this a gap or NOT_RELEVANT? It's a gap because the Byzantine Empire
    # (>100M births) controlled a part but not 99%+.
    #
    # 1180-1459: Serbian medieval state, Hungarian Vojvodina, then Ottoman expansion.
    # Byzantine Empire weakened, but Ottoman Empire (from 1299, >100M births after
    # accumulating enough pop*years) entered the picture.
    # Ottoman Empire: by 1389 (Kosovo battle) it controlled significant Serbian territory.
    # Ottoman Empire's lifetime births by 1389: ~5M avg * 90yr * 0.04 = 18M. Still <100M.
    # By 1459 (fall of Serbia): ~8M avg * 160yr * 0.04 = 51M. Still <100M.
    # Ottoman Empire crosses 100M threshold around: 100M / (0.04 * avg_pop).
    # With avg 10M pop, need 250 years from 1299 = 1549. With avg 15M, need 167yr = 1466.
    # So Ottoman Empire is <100M births until roughly ~1460-1550.
    #
    # Hmm, this complicates things. Let me reconsider.
    # Actually, the Ottoman Empire's population grew significantly. By 1500 it had
    # ~12-15M people, by 1600 ~25-30M. The integral of population over time matters.
    # 1299-1400: avg ~4M, 101yr → 16M births
    # 1400-1500: avg ~8M, 100yr → 32M births
    # Running total by 1500: 48M
    # 1500-1550: avg ~12M, 50yr → 24M births
    # Running total by 1550: 72M
    # 1550-1600: avg ~20M, 50yr → 40M births
    # Running total by 1600: 112M ✓
    # So Ottoman Empire crosses 100M lifetime births around ~1580.
    #
    # But wait — the 100M births calculation should be for the polity's ENTIRE existence,
    # not just up to the year in question. The Ottoman Empire existed 1299-1922 and
    # clearly exceeded 100M total births. The question is whether the polity had >100M
    # lifetime births, period — not whether it had reached that threshold by a given year.
    # Re-reading the rules: "polities existed but ALL of them had fewer than 100 million
    # lifetime births. Calculate lifetime births as: average_population × 0.04 × years_of_existence."
    # So it's the TOTAL lifetime births of the polity across its entire existence.
    # Ottoman Empire total: ~18M avg * 623yr * 0.04 = 448M. Clearly >100M.
    # So even in 1350, the Ottoman Empire is a polity with >100M lifetime births (because
    # we calculate over its whole existence 1299-1922).
    # This means: any year the Ottoman Empire controlled any part of Serbian territory,
    # that period CANNOT be NOT_RELEVANT.
    #
    # OK, with that understanding:
    # 580-1521: Byzantine Empire (>100M births) controlled parts throughout.
    # From ~1389: Ottoman Empire (>100M births) also controlled parts.
    # Kingdom of Hungary (1000-1526, <100M births) controlled Vojvodina.
    # No single polity controlled 99%+ of modern Serbia at any point.
    # This entire period is a gap.

    # 1521-1699: After fall of Belgrade (1521), Ottoman Empire controlled ALL of modern
    # Serbia including Vojvodina. 99%+ control.
    (1521, 1699, 'Ottoman Empire'),
    # 1699-1817: Treaty of Karlowitz (1699): Vojvodina transferred to Habsburg Monarchy.
    # Rest of Serbia remained Ottoman. Both had >100M lifetime births.
    # Vojvodina = ~28% of modern Serbia's population. Fails 99%.
    # GAP JUSTIFICATION: Habsburg Monarchy (>100M births) controlled Vojvodina;
    # Ottoman Empire (>100M births) controlled central/southern Serbia.

    # 1817-1878: Principality of Serbia gained autonomy (recognized 1830) over central
    # Serbia only. Vojvodina still Habsburg/Austrian. Southern Serbia/Kosovo still Ottoman.
    # Same gap situation continues.

    # 1878-1918: Serbia independent but only central Serbia. Vojvodina under Austria-Hungary
    # (>100M births? A-H: ~45M * 51yr * 0.04 = 92M. Borderline, just under 100M.
    # But the broader Habsburg state from 1526-1918: clearly >100M.)
    # Actually, with splitting view: Austria-Hungary specifically (1867-1918) had 92M births.
    # Under 100M. But the instruction says to check if ANY polity exceeds 100M.
    # The Habsburg Monarchy (1526-1804) as a distinct polity had >100M. Austrian Empire
    # (1804-1867) had ~71M. Austria-Hungary (1867-1918) had ~92M.
    # With strict splitting: Austria-Hungary is its own polity with <100M births.
    # Hmm, but the Serbian lands that were under Austria-Hungary (Vojvodina) — was
    # Austria-Hungary the only polity controlling that part? Yes.
    # And the Kingdom of Serbia controlled the rest.
    # Kingdom of Serbia: ~3M * 36yr * 0.04 = 4.3M. <100M.
    # Austria-Hungary: ~92M. <100M.
    # So 1878-1918: ALL polities <100M? That would make it NOT_RELEVANT.
    # But wait — the Ottoman Empire (>100M births) still controlled Kosovo and
    # southern Serbia (Sandžak, etc.) which are part of modern Serbia's claimed territory.
    # If we define modern Serbia as excluding Kosovo (de facto), then the Ottoman-held
    # areas within modern Serbia (excluding Kosovo) would be just the Sandžak region,
    # which is small (<5% of population).
    # Hmm, this is getting complicated. Let me think about what "modern Serbia" means.
    # I'll use de facto Serbia (excluding Kosovo) as the reference territory.
    #
    # 1878-1912: Central Serbia = independent Kingdom of Serbia. Vojvodina = Austria-Hungary.
    # Sandžak = Ottoman Empire. Population shares of modern Serbia (excl Kosovo):
    # Central Serbia ~70%, Vojvodina ~28%, Sandžak ~2%.
    # Austria-Hungary (<100M with strict splitting) controlled Vojvodina.
    # Ottoman Empire (>100M) controlled Sandžak.
    # So Ottoman Empire (>100M) controlled SOME part → cannot be NOT_RELEVANT → gap.
    #
    # 1912-1913: Balkan Wars. Serbia conquers Sandžak and Kosovo.
    # 1913-1918: Serbia controls all of modern Serbia (excl Kosovo) except Vojvodina
    # (still Austria-Hungary). After Serbia gained Sandžak, the remaining non-Serbian
    # territory within modern Serbia (excl Kosovo) is just Vojvodina (~28% of pop).
    # Austria-Hungary controlled Vojvodina. A-H had <100M births (strictly).
    # Kingdom of Serbia had <100M births.
    # So 1913-1918: Is any polity with >100M controlling part of modern Serbia?
    # A-H had 92M — just under. No other large polity.
    # But I was told to err on the side of leaving gaps. A-H is very close to 100M.
    # The instruction says "err strongly on the side of leaving a gap."
    # 92M is close enough that I should leave a gap.
    # GAP JUSTIFICATION: Austria-Hungary controlled Vojvodina. While A-H's strict
    # lifetime births (~92M) are slightly under 100M, the instruction says to err
    # on the side of gaps, and this is a borderline case.

    # Actually, let me reconsider. The instruction says Austria-Hungary is its own
    # polity but it's a continuation of the Habsburg state. The Habsburg Monarchy
    # (1526-1804) + Austrian Empire (1804-1867) + Austria-Hungary (1867-1918) are all
    # the same dynasty/state with regime changes. With strict splitting, A-H is 92M.
    # The instruction to "err strongly on the side of leaving a gap" applies. 92M is
    # borderline. I'll leave 1699-1918 as a gap.

    (1918, 1941, 'Kingdom of Yugoslavia'),
    # 1941-1945: Axis occupation. Territory of Serbia under German military admin.
    # Vojvodina split between Hungary and Germany. Various resistance movements.
    # Nazi Germany <100M, Horthy's Hungary <100M.
    # No polity with >100M births controlled any part of modern Serbia.
    (1941, 1945, 'NOT_RELEVANT'),
    (1945, 1992, 'Socialist Federal Republic of Yugoslavia'),
    (1992, 2003, 'Federal Republic of Yugoslavia'),
    (2003, 2006, 'State Union of Serbia and Montenegro'),
    (2006, 2026, 'Republic of Serbia'),
]


# =============================================================================
# Gap justification summary
# =============================================================================
#
# Czech Republic:
#   805-1029: Frankish Kingdom/HRE (>100M births) controlled/claimed Bohemia but
#             not Moravia (under Great Moravia, then Hungary/Poland).
#
# Slovakia:
#   1526-1699: Habsburg Monarchy (>100M) and Ottoman Empire (>100M) split control.
#
# Austria:
#   476-796: Frankish Kingdom (>100M births) controlled western Austria; Avars held east.
#
# Bulgaria:
#   580-681: Byzantine Empire (>100M) retained coastal areas despite Slavic invasions.
#   971-1018: Byzantine Empire (>100M) controlled eastern Bulgaria; western Bulgaria independent.
#   1185-1396: Byzantine Empire (>100M) and later Ottoman Empire (>100M) contested territory.
#   1878-1885: Ottoman Empire (>100M) controlled Eastern Rumelia (~40% of modern Bulgaria).
#
# Serbia:
#   580-1521: Byzantine Empire (>100M) and later Ottoman Empire (>100M) controlled portions.
#             Kingdom of Hungary (<100M) controlled Vojvodina.
#   1699-1918: Habsburg Monarchy/Austrian Empire/A-H controlled Vojvodina (~28% of pop).
#              Ottoman Empire (>100M) controlled rest until Serbian independence.
#              After 1878, A-H (~92M, borderline) held Vojvodina; Ottoman Empire (>100M)
#              held Sandžak until 1912. Err on side of gap per instructions.


if __name__ == '__main__':
    for country, timeline in TIMELINES.items():
        print(f"\n{'='*60}")
        print(f"  {country}")
        print(f"{'='*60}")
        prev_end = None
        for start, end, polity in timeline:
            if prev_end is not None and start > prev_end:
                print(f"  [{prev_end:>7} to {start:>7}]  ** GAP (indeterminate) **")
            yr_s = f"{start} BC" if start < 0 else f"{start} AD" if start > 0 else "0"
            yr_e = f"{end} BC" if end < 0 else f"{end} AD" if end > 0 else "0"
            print(f"  ({start:>7}, {end:>7})  {polity}")
            prev_end = end
        if prev_end and prev_end < 2026:
            print(f"  [{prev_end:>7} to    2026]  ** GAP (indeterminate) **")
