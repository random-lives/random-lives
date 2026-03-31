"""
Complete polity control timelines for France, Germany, Poland, Belgium, Netherlands.

Rules:
- NO_KNOWN_POLITIES: earliest period until first polity with 100k+ under centralized control
- NOT_RELEVANT: polities existed but ALL had <100M lifetime births (avg_pop * 0.04 * years)
- Polity name: single polity controlled 99%+ of modern country's population
- Gap: polities with >100M lifetime births existed but none controlled 99%+
- End years exclusive. Negative years = BCE.

For every gap, justification is provided in comments.
"""

# =============================================================================
# FRANCE
# =============================================================================

FRANCE = [
    # Earliest humans to first centralized polity with 100k+ in this territory.
    # Gallic tribal kingdoms (Arverni, Aedui) had centralized structures by ~200 BCE
    # but the first unambiguous 100k+ centralized polity in this territory is the
    # Roman Republic's Provincia Narbonensis, established ~121 BCE.
    (-200000, -121, 'NO_KNOWN_POLITIES'),

    # GAP: -121 to -50
    # Roman Republic controlled Provincia (southern Gaul) but independent Gallic
    # tribes controlled the rest. Roman Republic clearly >100M lifetime births
    # (pop ~50M+ for centuries).

    # Caesar's conquest completed 50 BCE. Roman control of all Gaul.
    # Roman Republic to -27, then Principate/Empire.
    (-50, -27, 'Roman Republic'),
    (-27, 395, 'Roman Empire'),
    (395, 418, 'Western Roman Empire'),

    # GAP: 418-486
    # Visigoths controlled Aquitaine from 418, Burgundians held eastern regions,
    # rump Roman authority in north until 476/486. None of these individually
    # controlled 99%. But were any >100M lifetime births?
    # Western Roman Empire (395-476): ~20M avg pop * 0.04 * 81 years = 64.8M. Close but under.
    # Combined Roman Empire before 395: easily >100M. But that's before this gap.
    # The Visigoths, Burgundians, Franks during 418-486 each had <5M people * <100 years = well under.
    # However, the Western Roman Empire existed until 476 and arguably still controlled
    # parts of northern Gaul. Its TOTAL population across all territories was ~20M for 81 years = 64.8M.
    # This is under 100M. So NOT_RELEVANT is actually correct for 418-486.
    (418, 486, 'NOT_RELEVANT'),

    # GAP: 486-534
    # Clovis's Frankish Kingdom controlled most of northern/central France but
    # Burgundian Kingdom held the east, Visigoths held parts of the south until 507.
    # After Vouillé (507), Visigoths pushed to Septimania. Burgundy independent until 534.
    # Frankish Kingdom under Clovis: ~5M people, existed ~30 years as large state = 6M.
    # All polities in this territory <100M lifetime births.
    (486, 534, 'NOT_RELEVANT'),

    # GAP: 534-561
    # Frankish Kingdom nominally united under Chlothar I from 558, but divided among
    # sons of Clovis 511-558. The Frankish Kingdom as a whole (across all partitions)
    # controlled essentially all of modern France from 534 (Burgundy conquered).
    # But because it was divided among co-kings, no SINGLE polity had 99%.
    # Total Frankish Kingdom: ~7-8M, existed ~80 years by this point = ~25M. Under 100M.
    # Cumulative from 481: 7M * 0.04 * 80 = 22.4M. Under 100M.
    (534, 561, 'NOT_RELEVANT'),

    # 558-561: Chlothar I briefly reunited all Frankish lands
    # But only 3 years. The Frankish Kingdom is still under 100M cumulative.
    # Continue NOT_RELEVANT through the Merovingian divisions.

    # GAP: 561-751 (Merovingian divisions)
    # Repeatedly divided into Neustria, Austrasia, Burgundy. Brief reunifications
    # (613-629 Chlothar II, 629-639 Dagobert I) but mostly divided.
    # The Frankish realm as a totality: ~8M avg pop, from 481-751 = 270 years.
    # 8M * 0.04 * 270 = 86.4M. Getting close but still under 100M.
    # By ~700 CE the Frankish realm has existed long enough to approach 100M cumulative.
    # But the question is about individual polities during this gap period, not cumulative.
    # Each divided Frankish sub-kingdom had ~3-4M people, existed ~30-60 years per division.
    # Even the longest-lived single partition (Austrasia): ~4M * 0.04 * 200 = 32M. Under.
    # The concept of a single "Frankish Kingdom" is debatable when divided.
    # Under a strict reading, when divided they are separate kingdoms. All under 100M.
    (561, 751, 'NOT_RELEVANT'),

    # 751-843: Carolingian dynasty. Unified control of all modern France territory.
    # Pippin III reunified, Charlemagne expanded. Brittany was nominally tributary.
    # The Carolingian Empire easily controlled 99%+ of France's modern population.
    # But wait — Charlemagne's empire was much bigger than France. The polity is the
    # Carolingian Empire/Frankish Kingdom, which included France.
    (751, 843, 'Carolingian Empire'),

    # GAP: 843-1491
    # Treaty of Verdun (843) divided the empire. West Francia became the Kingdom of France,
    # but it didn't control all of modern France's territory:
    # - Lotharingia/Burgundy/Provence (eastern regions) went to Middle Francia
    # - Brittany was independent until 1491
    # - English-held territories (Aquitaine, Normandy at various times)
    # - Burgundy was semi-independent especially 1363-1477
    # The Kingdom of France is clearly >100M lifetime births: ~10-15M avg pop over 600+ years.
    # But it didn't control 99% of modern France's population at any point until 1491.

    # 1491: Brittany enters personal union with France (marriage of Anne of Brittany).
    # Before this, Brittany had ~5-8% of modern France's population — fails 99% rule.
    (1491, 1792, 'Kingdom of France'),
    (1792, 1804, 'French First Republic'),
    (1804, 1815, 'First French Empire'),
    (1815, 1830, 'Bourbon Restoration'),
    (1830, 1848, 'July Monarchy'),
    (1848, 1852, 'French Second Republic'),
    (1852, 1870, 'Second French Empire'),

    # GAP: 1870-1871
    # Franco-Prussian War, Paris Commune. French Third Republic proclaimed Sept 1870
    # but the transition was chaotic. Very brief — include in Third Republic.

    # 1871-1918: Alsace-Lorraine was annexed by Germany.
    # Alsace-Lorraine had ~1.5M people vs France's ~36M = ~4%. Fails 99%.
    # German Empire clearly >100M lifetime births. This is a gap, not NOT_RELEVANT.
    # GAP: 1871-1918. German Empire controlled Alsace-Lorraine (>100M lifetime births).

    (1870, 1871, 'French Third Republic'),

    # GAP: 1871-1918
    # German Empire held Alsace-Lorraine (~4% of modern France's population).
    # German Empire: ~55M avg pop * 0.04 * 47 years = 103.4M lifetime births. >100M.

    (1918, 1940, 'French Third Republic'),

    # GAP: 1940-1944
    # Northern France under German occupation, southern France under Vichy regime.
    # Nazi Germany clearly >100M lifetime births (80M * 0.04 * 12 = 38.4M for Nazi period alone,
    # plus continuity with German state). No single polity controlled 99%.

    (1944, 1946, 'Provisional Government of the French Republic'),
    (1946, 1958, 'French Fourth Republic'),
    (1958, 2026, 'French Fifth Republic'),
]

# =============================================================================
# GERMANY
# =============================================================================

GERMANY = [
    # Germanic tribal areas. No centralized polity with 100k+ until Roman conquest
    # of western regions or formation of larger tribal confederations.
    # The Roman Empire reached the Rhine by ~12 BCE but never controlled all of
    # modern Germany (only west of Rhine and brief forays east).
    # First polity with 100k+ under centralized control in German territory:
    # Roman provinces (Germania Inferior, Germania Superior) from ~12 BCE for western parts.
    # For eastern Germany, no centralized state until Carolingian conquest ~800 CE.
    # But the question is about ANY part of the territory.
    # Roman Empire controlled the Rhineland with 100k+ from ~12 BCE.
    (-200000, -12, 'NO_KNOWN_POLITIES'),

    # GAP: -12 to 410
    # Roman Empire controlled western Germany (provinces of Germania Inferior,
    # Germania Superior, Raetia) but Germanic tribes (Cherusci, Marcomanni,
    # Saxons, etc.) controlled the east. Roman Empire >100M lifetime births.

    # 410-750: Post-Roman period. Frankish kingdoms gradually expanded east.
    # Franks controlled Rhineland, Alamanni in southwest, Bavarians in southeast,
    # Saxons and Thuringians in center/north. The Frankish Kingdom reached ~100M
    # lifetime births around 750 CE (8-10M avg * 0.04 * ~270 years from 481).
    # Before that, no polity controlling any part of Germany had >100M.
    (410, 750, 'NOT_RELEVANT'),

    # GAP: 750-800
    # Carolingian/Frankish Kingdom (>100M lifetime births) controlled western and
    # southern Germany but Saxony (north/northeast) remained independent until
    # Charlemagne's Saxon Wars (772-804). Saxony had significant population.

    # 800-843: Charlemagne completed conquest of Saxony by 804.
    # Carolingian Empire controlled all of modern Germany.
    (800, 843, 'Carolingian Empire'),

    # GAP: 843-962
    # East Francia (Treaty of Verdun) controlled most of modern Germany.
    # But Lotharingia (including the Rhineland) was contested.
    # East Frankish Kingdom: ~5M people * 0.04 * 119 = 23.8M. Under 100M.
    # But East Francia is a successor to the Carolingian Empire which was >100M.
    # Hmm, the question is about individual polities during the gap.
    # East Francia: ~5M * 0.04 * 119 = 23.8M. Under 100M.
    # West Francia also controlled some of modern Germany's western territory.
    # West Francia: ~8M * 0.04 * 119 = 38M. Under 100M.
    # Actually, do we count Carolingian Empire's cumulative births? No — it ended in 843.
    # New polities (East Francia, West Francia) start fresh.
    # Both under 100M. So this should be NOT_RELEVANT.
    (843, 962, 'NOT_RELEVANT'),

    # 962-1806: Holy Roman Empire.
    # The HRE is specified as counting as a single polity.
    # It encompassed essentially all of modern Germany's territory throughout.
    # Some border areas (Schleswig) were Danish, but these were <1% of population
    # within modern Germany's borders.
    (962, 1806, 'Holy Roman Empire'),

    # GAP: 1806-1871
    # After HRE dissolution: Confederation of the Rhine (1806-1813), then German
    # Confederation (1815-1866), then North German Confederation (1866-1871).
    # These were loose confederations, not centralized states.
    # Individual member states (Prussia, Bavaria, Saxony, etc.) were separate polities.
    # Prussia: ~15-20M by mid-1800s * 0.04 * 65 = 39-52M. Under 100M.
    # But France controlled parts during Napoleonic period (1806-1813).
    # First French Empire: ~44M * 0.04 * 11 = 19.4M. Under 100M.
    # Actually, the question is about polities controlling ANY PART of this territory.
    # Prussia existed from 1525 and by 1806 had ~10M growing to ~25M by 1866.
    # Prussia: ~15M avg * 0.04 * 341 years (1525-1866) = 204.6M. >100M!
    # So this is a GAP, not NOT_RELEVANT. Prussia (>100M lifetime births) controlled
    # large parts of modern Germany but not 99% (Bavaria, Saxony, etc. were independent).

    (1871, 1918, 'German Empire'),
    (1918, 1933, 'Weimar Republic'),
    (1933, 1945, 'Nazi Germany'),

    # GAP: 1945-1990
    # Germany divided into BRD (West) and DDR (East).
    # Federal Republic of Germany (West): ~55-60M people.
    # German Democratic Republic (East): ~16-17M people.
    # Both clearly parts of larger blocs. Neither controlled 99% of modern Germany.
    # BRD: ~58M avg * 0.04 * 45 = 104.4M. >100M.
    # DDR: ~16.5M avg * 0.04 * 45 = 29.7M. Under 100M individually.
    # BRD >100M, so this is a gap.

    (1990, 2026, 'Federal Republic of Germany'),
]

# =============================================================================
# POLAND
# =============================================================================

POLAND = [
    # No centralized polity with 100k+ in Polish territory until the Piast dynasty.
    # Slavic tribes settled from ~500s CE. The first centralized Polish state is
    # under Mieszko I (~960s).
    (-200000, 960, 'NO_KNOWN_POLITIES'),

    # 960-1181: Piast dynasty controlled most of modern Poland's core territory
    # (Silesia, Greater Poland, Lesser Poland, Mazovia, parts of Pomerania).
    # The HRE (from 962) claimed nominal suzerainty at times but didn't directly
    # control territory within modern Poland's borders. HRE's direct presence in
    # modern Polish territory was minimal until the Duchy of Pomerania became an
    # imperial fief (1181) and Brandenburg expanded eastward.
    # Piast state: ~1-1.5M * 0.04 * 221 = ~13M. Under 100M.
    # HRE didn't control any significant part of modern Poland's territory. Under 100M
    # for any polity controlling territory here. NOT_RELEVANT.
    (960, 1181, 'NOT_RELEVANT'),

    # GAP: 1181-1945
    # From 1181, the HRE (>100M lifetime births) had formal authority over the Duchy
    # of Pomerania (including territory now in northwest Poland).
    #
    # 1181-1335: Fragmented Piast duchies in central Poland; HRE (>100M) controlled
    # western Pomerania through the Duchy of Pomerania. Teutonic Order arrived 1226,
    # controlled Prussia and Pomerelia (from 1308).
    #
    # 1335-1795: Kingdom of Poland / PLC controlled central and eastern parts of
    # modern Poland. HRE/Habsburg Monarchy (>100M) controlled Silesia (ceded to
    # Bohemian Crown 1335). Brandenburg-Prussia controlled Pomerania and East Prussia.
    #
    # 1795-1918: Poland fully partitioned. Russian Empire (>100M), Prussia/German
    # Empire (>100M), Habsburg/Austria-Hungary (>100M) each controlled parts.
    #
    # 1918-1939: Second Polish Republic controlled central/eastern parts of modern
    # Poland. Weimar Republic / Germany (>100M) controlled western territories
    # (Silesia, Pomerania, East Prussia) — ~25-30% of modern Poland's population.
    #
    # 1939-1945: Nazi Germany (>100M) and Soviet Union (>100M) occupied all of Poland.

    # 1945-1952: Post-war. Borders shifted dramatically westward to Oder-Neisse line.
    # Provisional government controlled essentially all of new Poland's territory.
    # Soviet Union exercised heavy influence but Poland was formally sovereign.
    (1945, 1952, 'Provisional Government of Poland'),
    (1952, 1989, "Polish People's Republic"),
    (1989, 2026, 'Republic of Poland'),
]

# =============================================================================
# BELGIUM
# =============================================================================

BELGIUM = [
    # Celtic/Germanic tribes. No centralized polity with 100k+ until Roman conquest.
    # Caesar conquered Gallia Belgica ~57 BCE.
    (-200000, -57, 'NO_KNOWN_POLITIES'),

    # GAP: -57 to 395
    # Roman Republic/Empire controlled all of Belgium's territory.
    (-57, -27, 'Roman Republic'),
    (-27, 395, 'Roman Empire'),
    (395, 430, 'Western Roman Empire'),

    # 430-481: Frankish settlement, Roman authority collapsed.
    # Franks, other Germanic tribes. All small polities <100M.
    # Western Roman Empire still nominally existed until 476 but didn't control Belgium.
    # WRE total: 20M * 0.04 * 81 = 64.8M. Under 100M.
    (430, 481, 'NOT_RELEVANT'),

    # 481-843: Frankish Kingdom / Carolingian Empire controlled all of Belgium.
    # Clovis's kingdom (481+) included all of modern Belgium.
    # But the Frankish Kingdom was frequently divided (Neustria/Austrasia).
    # Belgium was part of Austrasia in most divisions.
    # During divisions, Austrasia: ~3M * 0.04 * ~200 = 24M. Under 100M.
    # During unified periods the Frankish Kingdom as a whole would be larger.
    # The Frankish Kingdom/Carolingian Empire as a continuous entity from 481-843:
    # ~8-10M avg * 0.04 * 362 = 115-145M. >100M.
    # But if we consider divisions as separate polities, each partition is under 100M.
    # The Carolingian Empire (751-843) more clearly unified: ~15-20M * 0.04 * 92 = 55-74M.
    # The Merovingian Kingdom (481-751) as a whole: ~7M * 0.04 * 270 = 75.6M. Under 100M.
    # This is a borderline case. When the kingdom was divided, no single partition had 99%
    # of Belgium. When unified, it did. The divisions were frequent.
    # Let me be more careful:
    # 481-511: Clovis unified. 511-558: divided. 558-561: unified (Chlothar I).
    # 561-613: divided. 613-629: unified (Chlothar II). 629-639: Dagobert. etc.
    # Belgium (Austrasia) was part of the larger Frankish entity throughout.
    # The question is whether any single polity controlling Belgium had >100M lifetime births.
    # If we treat the Frankish Kingdom across divisions as one continuous polity (debatable),
    # it reaches >100M. If not, individual partitions are under.
    # I'll treat the Merovingian period as NOT_RELEVANT (partitions too small) and
    # Carolingian as clearly one polity.
    (481, 751, 'NOT_RELEVANT'),
    (751, 843, 'Carolingian Empire'),

    # 843-959: Treaty of Verdun gave Belgium to Middle Francia (Lotharingia).
    # Lotharingia was fought over by East and West Francia.
    # In 959 it became a duchy within East Francia.
    # Lotharingia: ~2-3M * 0.04 * ~116 = ~11M. Under 100M.
    # East and West Francia each under 100M individually during this period.
    (843, 959, 'NOT_RELEVANT'),

    # 959-962: Duchy of Lower Lotharingia within East Frankish Kingdom.
    # Transition to HRE.
    (959, 962, 'NOT_RELEVANT'),

    # 962-1384: Holy Roman Empire.
    # Belgium's territory (Flanders, Brabant, Liège, etc.) was within the HRE.
    # Except: County of Flanders held fiefs from BOTH the HRE and Kingdom of France.
    # Western Flanders was a French fief. Flanders had ~20-30% of Belgium's population.
    # So technically the HRE didn't control 99% — Flanders had dual allegiance.
    # The Kingdom of France: ~10-15M avg * 0.04 * many centuries = easily >100M.
    # The HRE: also easily >100M.
    # This is a GAP because both Kingdom of France and HRE (each >100M) controlled parts.

    # GAP: 962-1384
    # HRE controlled most of Belgium, but County of Flanders was partially a French fief.
    # Both HRE and Kingdom of France had >100M lifetime births.

    # 1384-1482: Burgundian Netherlands. Burgundy gradually unified the Low Countries.
    # But Liège remained independent (Prince-Bishopric).
    # Liège had ~5-10% of Belgium's population. Fails 99%.
    # Burgundian state: ~3M * 0.04 * 98 = ~11.8M. Under 100M.
    # But Burgundy was technically part of the Kingdom of France (as a fief) and HRE.
    # Both >100M. GAP.

    # GAP: 1384-1482
    # Burgundian Netherlands controlled most but Prince-Bishopric of Liège was independent.
    # HRE and Kingdom of France both had >100M lifetime births and claimed authority
    # over parts of Belgium.

    # 1482-1556: Habsburg Netherlands (under Habsburg dynasty, within HRE).
    # Same issue with Liège.
    # HRE >100M. GAP.

    # GAP: 1482-1556
    # Habsburg Netherlands controlled most of Belgium within the HRE framework,
    # but Liège remained independent. HRE >100M lifetime births.

    # 1556-1714: Spanish Netherlands.
    # Philip II of Spain inherited the Low Countries. But Liège remained independent
    # (Prince-Bishopric under HRE). Liège ~5-8% of Belgium's population.
    # Spanish Empire clearly >100M lifetime births. HRE also >100M.
    # GAP.

    # GAP: 1556-1714
    # Spanish Netherlands controlled most of Belgium but Liège was independent under HRE.
    # Spanish Empire >100M lifetime births.

    # 1714-1795: Austrian Netherlands.
    # Still, Liège remained independent. Habsburg Monarchy >100M.
    # GAP.

    # GAP: 1714-1795
    # Austrian Netherlands controlled most of Belgium but Liège still independent.
    # Habsburg Monarchy >100M lifetime births.

    # 1795-1815: France conquered all of Belgium including Liège.
    # French First Republic (1795-1804), then First French Empire (1804-1815).
    (1795, 1804, 'French First Republic'),
    (1804, 1815, 'First French Empire'),

    (1815, 1830, 'United Kingdom of the Netherlands'),
    (1830, 1940, 'Kingdom of Belgium'),

    # GAP: 1940-1944
    # German occupation. Nazi Germany >100M lifetime births.

    (1944, 2026, 'Kingdom of Belgium'),
]

# =============================================================================
# NETHERLANDS
# =============================================================================

NETHERLANDS = [
    # Germanic/Celtic tribes. Roman conquest of southern parts ~12 BCE.
    # Northern Netherlands (Frisia) never fully conquered by Rome.
    # First centralized polity with 100k+ in any part of this territory:
    # Roman provinces from ~12 BCE.
    (-200000, -12, 'NO_KNOWN_POLITIES'),

    # GAP: -12 to 395
    # Roman Empire controlled southern Netherlands (below Rhine) but not Frisia (north).
    # Roman Empire clearly >100M lifetime births.
    # Northern Frisia was ~30-40% of modern Netherlands territory but much less population.
    # Still, the split means <99% under one polity.
    # Actually, the Rhine frontier ran through the middle of modern Netherlands.
    # South (Batavia, etc.) was Roman; north (Frisia) was not.
    # Population-wise, south was more populated but north had significant population too.
    # Hard to say Romans had 99%. Leave as gap.

    # GAP: -12 to 410
    # Roman Empire controlled southern Netherlands; Frisians controlled the north.
    # Roman Empire >100M lifetime births.

    # 410-~700: Post-Roman. Franks in south, Frisians in north.
    # All polities small. NOT_RELEVANT.
    (410, 734, 'NOT_RELEVANT'),

    # 734: Charles Martel conquered Frisia. Frankish/Carolingian Kingdom now
    # controlled all of modern Netherlands.
    # From 734 to 843 (empire divided): single polity controlled 99%.
    (734, 843, 'Carolingian Empire'),

    # 843-~925: Netherlands split between Middle Francia (Lotharingia) and some
    # areas. Lotharingia was small and contested.
    # Lotharingia: ~2-3M * 0.04 * 82 = ~8M. Under 100M.
    # East Francia: ~5M * 0.04 * 82 = 16.4M. Under.
    (843, 925, 'NOT_RELEVANT'),

    # 925: Lotharingia (including Netherlands) incorporated into East Francia.
    # Then HRE from 962.
    (925, 962, 'NOT_RELEVANT'),

    # 962-1581: Holy Roman Empire.
    # The Netherlands was part of the HRE throughout. The County of Holland,
    # Bishopric of Utrecht, Frisia, Gelderland — all imperial fiefs.
    # By the 1500s the Burgundian/Habsburg unification brought them under one ruler
    # but still within HRE framework.
    (962, 1581, 'Holy Roman Empire'),

    # 1581-1795: Dutch Republic (Republic of the Seven United Netherlands).
    # Declared independence from Spain in 1581 (Act of Abjuration).
    # International recognition: 1648 (Peace of Westphalia).
    # The Republic controlled essentially all of modern Netherlands' territory.
    # Generality Lands in the south (Brabant, Limburg) were ruled directly by
    # the States-General, not as full provinces, but were under Republic's control.
    # Dutch Republic: ~2M avg * 0.04 * 214 = 17.1M. Under 100M.
    # However, the Republic's population grew from ~1.5M to ~2M over this period.
    # ~1.8M avg * 0.04 * 214 = 15.4M. Under 100M.
    # So this is NOT_RELEVANT... but wait.
    # Spain still claimed sovereignty and controlled parts of the southern Netherlands
    # (generality lands) during the 80 Years War (until 1648).
    # Spanish Empire is easily >100M lifetime births.
    # Before 1648, Spanish Empire controlled/claimed territory. >100M. GAP.
    # After 1648, Dutch Republic is the only polity. Under 100M. NOT_RELEVANT.

    # GAP: 1581-1648
    # Dutch Republic controlled most of Netherlands but Spain still controlled/claimed
    # parts (Generality Lands, southern areas) during 80 Years War.
    # Spanish Empire >100M lifetime births.

    (1648, 1795, 'NOT_RELEVANT'),
    # Dutch Republic controlled all of modern Netherlands. Under 100M lifetime births.

    # 1795-1810: Batavian Republic (1795-1806), Kingdom of Holland (1806-1810).
    # French satellite states. Under 100M individually.
    # But French Republic/Empire >100M controlled them indirectly.
    # However, these were nominally separate states. The question is about polity control.
    # France's influence was dominant but Batavian Republic and Kingdom of Holland
    # were separate polities (under 100M each).
    # French Republic/Empire didn't directly control the territory until 1810.
    # Hmm, but France is >100M and exercised effective control. This is borderline.
    # Let me treat 1795-1810 as a gap since France (>100M) effectively controlled
    # through puppet states.
    # Actually, the instructions say "single polity controlled territory containing at least
    # 99% of the population." The Batavian Republic was a separate polity from France.
    # The Kingdom of Holland under Louis Bonaparte was also separate.
    # Neither the Batavian Republic nor Kingdom of Holland had >100M lifetime births.
    # France didn't directly control the territory.
    # But France (>100M) exerted control through puppet regimes.
    # I think the right call: France controlled it indirectly. The puppet states
    # are technically separate polities. France >100M, so this is a gap.

    # GAP: 1795-1810
    # French-controlled puppet states (Batavian Republic, Kingdom of Holland) governed
    # Netherlands. French Republic/Empire (>100M lifetime births) exercised effective control
    # but through nominally separate polities.

    (1810, 1813, 'First French Empire'),  # Direct annexation

    # 1813-1815: Provisional government, then Congress of Vienna.
    # Brief transition. Under 100M. NOT_RELEVANT.
    (1813, 1815, 'NOT_RELEVANT'),

    (1815, 1830, 'United Kingdom of the Netherlands'),

    # 1830-1839: Belgium revolted. Southern Limburg was contested until Treaty of
    # London (1839). Southern Limburg is <2% of population. The Kingdom of Netherlands
    # controlled 98%+ of modern Netherlands' population throughout.
    # Belgium: brand new, <100M. No polity with >100M controlled the contested area.
    # Could arguably assign Kingdom of Netherlands from 1830, but the 99% rule
    # makes this borderline. Starting from 1839 to be safe, with NOT_RELEVANT for gap
    # since no polity with >100M controlled the contested portion.
    (1830, 1839, 'NOT_RELEVANT'),

    (1839, 1940, 'Kingdom of the Netherlands'),

    # GAP: 1940-1945
    # German occupation. Nazi Germany >100M lifetime births.

    (1945, 2026, 'Kingdom of the Netherlands'),
]


# =============================================================================
# Summary verification
# =============================================================================

def print_timeline(name, timeline):
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")
    prev_end = None
    for start, end, polity in timeline:
        if prev_end is not None and start > prev_end:
            print(f"  [{prev_end:>7} to {start:>7}]  ** GAP (indeterminate) **")
        print(f"  ({start:>7}, {end:>7})  {polity}")
        prev_end = end

if __name__ == '__main__':
    for name, data in [('France', FRANCE), ('Germany', GERMANY), ('Poland', POLAND),
                       ('Belgium', BELGIUM), ('Netherlands', NETHERLANDS)]:
        print_timeline(name, data)
