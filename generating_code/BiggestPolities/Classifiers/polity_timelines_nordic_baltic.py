"""
Polity control timelines for Finland, Iceland, Estonia, Latvia, Lithuania.

Each entry is (start_year, end_year, polity_name) where end_year is exclusive.
Negative years are BCE.

Special polity names:
- NO_KNOWN_POLITIES: No polity with 100K+ centralized population existed here
- NOT_RELEVANT: Polities existed but all had <100M lifetime births
- Named polity: Single polity controlled 99%+ of population within modern borders
- Gaps between entries: Indeterminate (polities with >100M births existed but none had 99%+ control)
"""

FINLAND = [
    # Finnish tribes, no centralized polity with 100K+ people.
    # Swedish Northern Crusades established control ~1249-1293.
    (-200000, 1250, "NO_KNOWN_POLITIES"),

    # Kingdom of Sweden controlled all of Finland from ~1250 to 1809.
    # Sweden lifetime births: avg pop ~1.5M over ~800 years = ~48M. Under 100M.
    (1250, 1809, "NOT_RELEVANT"),

    # Grand Duchy of Finland within the Russian Empire.
    # Russian Empire (1721-1917): avg pop ~60M × 0.04 × 196 = ~470M lifetime births.
    # Russia controlled 99%+ of Finland's territory.
    (1809, 1917, "Russian Empire"),

    # Finland declared independence Dec 1917, civil war 1918, then stable republic.
    # Republic of Finland: avg pop ~4.5M × 0.04 × 108 = ~19M. Under 100M.
    # No polity with >100M lifetime births controlled Finnish territory after 1917.
    # (Germany supported Whites in civil war but did not formally govern Finland.)
    (1917, 2026, "NOT_RELEVANT"),
]

ICELAND = [
    # No permanent human habitation until Norse settlement ~874 AD.
    # Icelandic Commonwealth (930-1262) had only ~20-40K people, not centralized.
    # First polity with 100K+ controlling Iceland: Kingdom of Norway from 1262.
    (-200000, 1262, "NO_KNOWN_POLITIES"),

    # 1262-1380: Kingdom of Norway (~350K pop, ~7M lifetime births)
    # 1380-1814: Denmark-Norway / Kingdom of Denmark (~1.5M avg, ~26M lifetime births)
    # 1814-1918: Kingdom of Denmark (after Treaty of Kiel)
    # 1918-1944: Kingdom of Iceland (personal union with Denmark, ~100K pop)
    # 1944-2026: Republic of Iceland (~200-400K pop)
    # All polities controlling Iceland had <100M lifetime births throughout.
    # (WWII British/US military presence 1940-1944 was not sovereign control;
    #  Iceland maintained self-governance throughout.)
    (1262, 2026, "NOT_RELEVANT"),
]

ESTONIA = [
    # Estonian tribes, no centralized polity with 100K+ people.
    # Livonian Crusade conquered Estonia by ~1227 (Terra Mariana).
    (-200000, 1227, "NO_KNOWN_POLITIES"),

    # 1227-1561: Livonian Confederation (bishoprics, Teutonic/Livonian Order). All small.
    # 1561-1710: Northern Estonia under Sweden, southern parts under Poland-Lithuania.
    #   Kingdom of Sweden: ~48M lifetime births. Under 100M.
    #   Polish-Lithuanian Commonwealth (1569-1795): ~81M. Under 100M.
    # All polities controlling Estonian territory had <100M lifetime births.
    (1227, 1710, "NOT_RELEVANT"),

    # Tsardom of Russia conquered Estonia in 1710 (Great Northern War).
    # Treaty of Nystad (1721) confirmed Russian control.
    # Tsardom of Russia (1547-1721): ~15M avg × 0.04 × 174 = ~104M. Over 100M.
    # Controlled 99%+ of Estonian territory.
    (1710, 1721, "Tsardom of Russia"),

    # Russian Empire controlled all of Estonia.
    # Russian Empire (1721-1917): ~470M lifetime births. Over 100M.
    (1721, 1917, "Russian Empire"),

    # 1917-1920: Transitional period. Russian Empire collapsed 1917.
    # German Empire occupied Estonia in 1918 (Treaty of Brest-Litovsk).
    #   German Empire (1871-1918): ~65M avg × 0.04 × 47 = ~122M. Over 100M.
    # Estonian War of Independence 1918-1920 (vs Soviet Russia).
    # No single polity controlled 99%+ throughout this period.
    # GAP JUSTIFICATION: German Empire (>100M lifetime births) controlled Estonia in 1918.

    # 1920-1940: Republic of Estonia. Pop ~1M. Lifetime births ~1M. Under 100M.
    # No polity with >100M controlled any part of Estonian territory.
    (1920, 1940, "NOT_RELEVANT"),

    # Soviet Union occupied Estonia in June 1940.
    # USSR (1922-1991): avg pop ~200M × 0.04 × 69 = ~552M lifetime births.
    (1940, 1941, "Soviet Union"),

    # Nazi Germany occupied Estonia from July 1941.
    # Third Reich: including all controlled territories, ~250M avg × 0.04 × 12 = ~120M. Over 100M.
    (1941, 1944, "Nazi Germany"),

    # Soviet Union reoccupied Estonia in September 1944. Estonian SSR.
    (1944, 1991, "Soviet Union"),

    # Republic of Estonia restored. Pop ~1.3M.
    # Lifetime births: ~1.3M × 0.04 × 35 = ~1.8M. Under 100M.
    (1991, 2026, "NOT_RELEVANT"),
]

LATVIA = [
    # Latvian/Livonian tribes, no centralized polity with 100K+ people.
    # Livonian Crusade conquered the territory by ~1227.
    (-200000, 1227, "NO_KNOWN_POLITIES"),

    # 1227-1561: Livonian Confederation (Terra Mariana). Small polities.
    # 1561-1710: Split between Sweden (Livonia/Riga) and Poland-Lithuania
    #   (Duchy of Courland as vassal + Latgale). Both <100M lifetime births.
    # All polities controlling Latvian territory had <100M lifetime births.
    (1227, 1710, "NOT_RELEVANT"),

    # 1710-1795: Russian Empire conquered Swedish Livonia (including Riga) in 1710.
    # However, Courland remained a Polish-Lithuanian vassal until 1795 (Third Partition),
    # and Latgale was under Poland-Lithuania until 1772 (First Partition).
    # Courland + Latgale = ~30-35% of modern Latvia's population. >1% threshold.
    # Russia did NOT control 99%+ of modern Latvia until 1795.
    # GAP JUSTIFICATION: Russian Empire (>100M lifetime births) controlled most of
    # Latvia but the Duchy of Courland and Latgale remained under Poland-Lithuania.

    # Russian Empire controlled all of modern Latvia's territory from 1795.
    (1795, 1917, "Russian Empire"),

    # 1917-1920: Transitional period. Russian Empire collapsed.
    # German Empire occupied Latvia in 1918. German Empire >100M lifetime births.
    # Latvian War of Independence 1918-1920.
    # GAP JUSTIFICATION: German Empire (>100M lifetime births) controlled Latvia in 1918.

    # 1920-1940: Republic of Latvia. Pop ~1.9M.
    # Lifetime births: ~1.9M × 0.04 × 20 = ~1.5M. Under 100M.
    (1920, 1940, "NOT_RELEVANT"),

    # Soviet Union occupied Latvia in June 1940.
    (1940, 1941, "Soviet Union"),

    # Nazi Germany occupied Latvia from July 1941.
    (1941, 1944, "Nazi Germany"),

    # Soviet Union reoccupied Latvia in October 1944. Latvian SSR.
    (1944, 1991, "Soviet Union"),

    # Republic of Latvia restored. Pop ~2M declining to ~1.8M.
    # Lifetime births: ~1.9M × 0.04 × 35 = ~2.7M. Under 100M.
    (1991, 2026, "NOT_RELEVANT"),
]

LITHUANIA = [
    # Lithuanian tribes. Grand Duchy of Lithuania formed ~1236 with 100K+
    # under centralized political control (consolidation against Teutonic Order).
    (-200000, 1236, "NO_KNOWN_POLITIES"),

    # 1236-1569: Grand Duchy of Lithuania. Modern Lithuania was its core territory.
    #   GDL lifetime births: avg pop ~3M × 0.04 × 333 = ~40M. Under 100M.
    # 1569-1795: Polish-Lithuanian Commonwealth. Modern Lithuania fully within it.
    #   PLC lifetime births: avg pop ~9M × 0.04 × 226 = ~81M. Under 100M.
    # All polities had <100M lifetime births.
    (1236, 1795, "NOT_RELEVANT"),

    # Russian Empire absorbed Lithuania in the Third Partition of Poland (1795).
    # Controlled all of modern Lithuania's territory.
    (1795, 1917, "Russian Empire"),

    # 1917-1920: Transitional period. Russian Empire collapsed.
    # German Empire (Ober Ost) controlled Lithuania in 1918.
    #   German Empire: >100M lifetime births.
    # Lithuanian Wars of Independence 1918-1920.
    # GAP JUSTIFICATION: German Empire (>100M lifetime births) controlled Lithuania in 1918.

    # 1920-1940: Interwar period. Republic of Lithuania existed but:
    #   - 1920-1923: Klaipėda region (Memelland) under French/League of Nations administration
    #   - 1920-1939: Vilnius region under Poland (Second Polish Republic)
    #   Vilnius region had a significant fraction (>1%) of modern Lithuania's population.
    #   However, Second Polish Republic lifetime births: ~27M × 0.04 × 21 = ~23M. Under 100M.
    #   Republic of Lithuania: ~2M × 0.04 × 20 = ~1.6M. Under 100M.
    #   All polities controlling Lithuanian territory had <100M lifetime births.
    (1920, 1940, "NOT_RELEVANT"),

    # Soviet Union occupied Lithuania in June 1940.
    # (Lithuania had recovered Vilnius from Poland in Oct 1939 via Soviet ultimatum.)
    (1940, 1941, "Soviet Union"),

    # Nazi Germany occupied Lithuania from June 1941.
    (1941, 1944, "Nazi Germany"),

    # Soviet Union reoccupied Lithuania in July 1944. Lithuanian SSR.
    (1944, 1990, "Soviet Union"),

    # Republic of Lithuania declared independence March 11, 1990
    # (internationally recognized September 1991).
    # Pop ~3.5M declining to ~2.8M. Lifetime births: ~3M × 0.04 × 36 = ~4.3M. Under 100M.
    (1990, 2026, "NOT_RELEVANT"),
]


# Verification: check continuity and non-overlapping
def verify_timeline(name, timeline):
    for i, (start, end, polity) in enumerate(timeline):
        assert start < end, f"{name}[{i}]: start {start} >= end {end}"
        if i > 0:
            prev_end = timeline[i-1][1]
            assert start >= prev_end, f"{name}[{i}]: start {start} < prev end {prev_end}"
            if start > prev_end:
                # This is a gap - acceptable
                pass
    # Check first entry starts at -200000
    assert timeline[0][0] == -200000, f"{name}: first entry doesn't start at -200000"
    # Check last entry ends at 2026
    assert timeline[-1][1] == 2026, f"{name}: last entry doesn't end at 2026"


if __name__ == "__main__":
    for name, timeline in [
        ("Finland", FINLAND),
        ("Iceland", ICELAND),
        ("Estonia", ESTONIA),
        ("Latvia", LATVIA),
        ("Lithuania", LITHUANIA),
    ]:
        verify_timeline(name, timeline)
        print(f"{name}: {len(timeline)} entries, OK")

        # Print gaps
        for i in range(1, len(timeline)):
            prev_end = timeline[i-1][1]
            curr_start = timeline[i][0]
            if curr_start > prev_end:
                print(f"  Gap: {prev_end} to {curr_start}")
