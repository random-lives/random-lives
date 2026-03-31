"""
Polity timelines for Myanmar, Afghanistan, Laos, Malaysia, Singapore.

Conventions:
- Negative years = BCE. end_year is EXCLUSIVE.
- NO_KNOWN_POLITIES: earliest period, ends when first polity with 100K+ centralized pop existed here.
- NOT_RELEVANT: polities existed but ALL had <100M lifetime births (avg_pop x 0.04 x years).
- Named polity: single polity controlled >=99% of this modern country's population.
- Gaps: polities with >100M lifetime births existed here, but none controlled >=99%.

For colonial empires, lifetime births = total empire population (all territories), not just metropole.
"""

# =============================================================================
# MYANMAR
# =============================================================================
#
# Gap justifications:
#
# 1287-1555: Yuan Dynasty (>100M lifetime births) conquered Upper Burma in 1287,
#   controlled northern Myanmar through ~1303. Ming Dynasty (>100M) later
#   intervened in Shan states through 15th century (Ming-Ava wars ~1380s-1440s).
#   Territory fragmented among Ava, Pegu, Shan states, Arakan.
#
# 1824-1886: British Empire (>100M) annexed Arakan and Tenasserim (1826), then
#   Lower Burma (1852). Konbaung Dynasty still controlled Upper Burma. Neither
#   held 99%.
#
# 1942-1945: Empire of Japan (>100M) occupied Burma. British Empire (>100M)
#   maintained nominal sovereignty.

MYANMAR = [
    (-200000, -500, 'NO_KNOWN_POLITIES'),
    (-500, 1287, 'NOT_RELEVANT'),
    # Pyu city-states, Mon kingdoms, Pagan Kingdom (1044-1287). All <100M lifetime
    # births. No external >100M polity controlled any part of modern Myanmar.
    # 1287-1555: Gap. Yuan Dynasty (>100M) conquered Upper Burma; Ming Dynasty
    # (>100M) intervened in Shan states. Territory fragmented.
    (1555, 1599, 'Toungoo Empire'),
    # Bayinnaung unified all of modern Myanmar by 1555. Toungoo controlled 99%+.
    (1599, 1752, 'NOT_RELEVANT'),
    # Restored Toungoo (Nyaungyan) dynasty controlled most of Myanmar. Arakan
    # independent. All polities <100M lifetime births. Ming influence had receded
    # to nominal suzerainty over border Shan states, not territorial control.
    (1752, 1824, 'Konbaung Dynasty'),
    # Konbaung reunified Burma by ~1759, controlled 99%+ through 1824.
    # 1824-1886: Gap. British Empire (>100M) took Arakan/Tenasserim (1826),
    # then Lower Burma (1852). Konbaung held Upper Burma.
    (1886, 1942, 'British Empire'),
    # Third Anglo-Burmese War (1885): Britain annexed all of Burma.
    # Administered as part of British India until 1937, then as British Burma.
    # 1942-1945: Gap. Empire of Japan (>100M) vs British Empire (>100M).
    (1945, 1948, 'British Empire'),
    # British reoccupied Burma after Japanese surrender.
    (1948, 2026, 'NOT_RELEVANT'),
    # Successive independent regimes: Union of Burma (1948-62), Revolutionary
    # Council (1962-74), Socialist Republic (1974-88), SLORC/SPDC (1988-2011),
    # Republic of the Union of Myanmar (2011-21), SAC junta (2021-). Each <100M
    # lifetime births. No external >100M polity controls any part.
]

# =============================================================================
# AFGHANISTAN
# =============================================================================
#
# Gap justifications:
#
# -305 to 1186 (continuous gap): At every point, at least one >100M polity
#   controlled part of Afghanistan, but the territory was always divided between
#   eastern and western powers:
#   - Maurya Empire (>100M) held south/east, Seleucid Empire (>100M) held
#     Bactria (north): -305 to -250
#   - Maurya Empire (>100M) in south/east, Greco-Bactrian (<100M) in north,
#     Parthian Empire (>100M) expanding into west: -250 to -185
#   - Parthian Empire (>100M) in west, Indo-Greek/Indo-Scythian (<100M) in
#     east: -185 to ~30
#   - Kushan Empire (>100M) in east, Parthian Empire (>100M) in west: ~30 to 224
#   - Sasanian Empire (>100M) replaced Parthians in west, Kushan (>100M) in
#     east: 224-375
#   - Sasanian Empire (>100M) in west, Kidarite/Hephthalite in east: 375-560
#   - Sasanian Empire (>100M) recovered much of east, Turkic groups in north:
#     560-651
#   - Umayyad Caliphate (>100M) then Abbasid Caliphate (>100M) in west/center,
#     Kabul Shahi in east: 651-870
#   - Abbasid Caliphate (>100M) as nominal suzerain over Saffarid/Samanid
#     governors: 870-977
#   - Seljuk Empire (borderline ~100M, err on side of gap) in west, Ghaznavid
#     in east: 977-1186
#
# 1220-1370: Mongol Empire (>100M) conquered all of Afghanistan. Split between
#   Chagatai Khanate and Ilkhanate -- neither alone had 99%.
#
# 1405-1510: Timurid successor states (>100M overall as Timurid Empire) controlled
#   different parts through rival branches. After ~1500, Shaybanid Uzbeks invaded.
#
# 1510-1747: Safavid Empire (borderline ~100M, err on gap) controlled western
#   Afghanistan (Herat); Mughal Empire (>100M) controlled eastern Afghanistan
#   (Kabul, intermittently Kandahar). Neither controlled 99%.
#
# 1978-1989: Soviet Union (>100M) invaded and occupied much of Afghanistan.
#   Mujahideen controlled significant rural areas.
#
# 2001-2021: United States (>100M) led military coalition in Afghanistan.
#   Taliban controlled significant territory throughout; Afghan government
#   never controlled 99%.

AFGHANISTAN = [
    (-200000, -2000, 'NO_KNOWN_POLITIES'),
    # ~2000 BCE: BMAC (Bactria-Margiana Archaeological Complex) and Indus Valley
    # outposts in eastern Afghanistan suggest organized polities with 100K+.
    (-2000, -550, 'NOT_RELEVANT'),
    # BMAC, early Indo-Aryan polities, Gandhara culture, Median periphery.
    # All <100M lifetime births. No external >100M polity controlled this area.
    (-550, -330, 'Achaemenid Empire'),
    # Controlled all of modern Afghanistan through satrapies (Bactria, Arachosia,
    # Aria, Gandhara). >100M lifetime births, 99% control.
    (-330, -312, 'NOT_RELEVANT'),
    # Alexander's Macedonian Empire (-330 to -323): ~13M lifetime births, <100M.
    # Diadochi wars (-323 to -312): successor states each <100M individually.
    (-312, -305, 'Seleucid Empire'),
    # Seleucus I controlled all of Afghanistan after winning the eastern wars.
    # Seleucid Empire >100M lifetime births. 99% control.
    # In -305, ceded Arachosia/Paropamisadae to Chandragupta Maurya.
    # -305 to 1186: continuous gap (see justification above).
    (1186, 1220, 'NOT_RELEVANT'),
    # Ghurid Empire then Khwarazmian Empire. Both <100M lifetime births.
    # Abbasid Caliphate still existed but had lost all effective control east of
    # Iraq by this point -- no territorial presence in Afghanistan.
    # 1220-1370: Gap. Mongol Empire (>100M) conquered Afghanistan, divided between
    # Chagatai Khanate and Ilkhanate.
    (1370, 1405, 'Timurid Empire'),
    # Timur conquered all of Afghanistan by ~1380. Under unified Timurid control.
    # ~110M lifetime births (borderline); controlled 99%.
    # 1405-1510: Gap. Timurid successor branches (Herat, Kabul, Samarkand) divided
    # the empire. Timurid Empire overall >100M lifetime births.
    (1507, 1510, 'NOT_RELEVANT'),
    # Shaybanid Uzbeks held Herat, Babur held Kabul. All <100M lifetime births.
    # Safavid Empire had not yet taken Afghan territory.
    # 1510-1747: Gap. Safavid Empire (borderline ~100M, err on gap) took Herat
    # in 1510; Mughal Empire (>100M from 1526) controlled Kabul/eastern Afghanistan.
    (1747, 1896, 'NOT_RELEVANT'),
    # Durrani Empire (1747-1826) then Barakzai dynasty. All <100M lifetime births.
    # Anglo-Afghan Wars (1839-42, 1878-80) were military campaigns, not sustained
    # territorial control; British withdrew each time.
    (1896, 1973, 'Kingdom of Afghanistan'),
    # Durand Line (1893/1896) established modern borders. The kingdom controlled
    # 99%+ of the population under successive rulers (Abdur Rahman Khan through
    # Zahir Shah).
    (1973, 1978, 'Republic of Afghanistan'),
    # Daoud Khan's republic after overthrowing King Zahir Shah.
    # 1978-1989: Gap. Soviet Union (>100M) invaded and occupied much of Afghanistan.
    (1989, 2001, 'NOT_RELEVANT'),
    # Post-Soviet withdrawal. Republic of Afghanistan (to 1992), then civil war
    # (mujahideen factions, then Taliban vs Northern Alliance). All <100M lifetime
    # births. No external >100M polity controlled territory.
    # 2001-2021: Gap. United States (>100M) had military forces and bases across
    # Afghanistan. Taliban controlled other parts.
    (2021, 2026, 'Islamic Emirate of Afghanistan'),
    # Taliban reconquered all of Afghanistan by August 2021. Controls 99%+ of
    # population (Panjshir resistance is <1%).
]

# =============================================================================
# LAOS
# =============================================================================
#
# Gap justifications:
#
# 1941-1946: Empire of Japan (>100M) occupied French Indochina including Laos.
#   French Vichy administration continued nominally under Japanese oversight;
#   Japan staged direct takeover in March 1945. Brief Lao Issara independence
#   (Oct 1945), then French return 1946.

LAOS = [
    (-200000, 1354, 'NO_KNOWN_POLITIES'),
    # First polity with 100K+ under centralized control in Lao territory was
    # Lan Xang (1354). Earlier Tai muang principalities and Khmer peripheral
    # presence were too small or decentralized.
    (1354, 1707, 'Lan Xang'),
    # Kingdom of Lan Xang controlled essentially all of modern Laos.
    (1707, 1893, 'NOT_RELEVANT'),
    # Lan Xang split into Luang Prabang, Vientiane, Champasak. Siamese suzerainty
    # grew (Siam destroyed Vientiane 1827). All polities <100M lifetime births:
    # Ayutthaya (~67M), Rattanakosin/Siam (~36M), three Lao kingdoms each tiny.
    (1893, 1941, 'French Third Republic'),
    # France established protectorate over Laos (Franco-Siamese Treaty 1893).
    # Controlled 99%+ of Lao territory/population.
    # 1941-1946: Gap. Empire of Japan (>100M) occupied French Indochina.
    (1946, 1953, 'French Fourth Republic'),
    # France reasserted control. Pathet Lao insurgency still small (<1% of
    # population in late 1940s).
    (1953, 2026, 'NOT_RELEVANT'),
    # Kingdom of Laos (1953-75, civil war with Pathet Lao), then Lao PDR
    # (1975-2026). All <100M lifetime births. North Vietnam had troops in Laos
    # but DRV itself <100M (20M x 0.04 x 31 = 25M).
]

# =============================================================================
# MALAYSIA
# =============================================================================
#
# Modern Malaysia = Peninsular Malaysia + Sabah + Sarawak (Borneo).
#
# Gap justifications:
#
# 1511-1641: Portuguese Empire (>100M) controlled Malacca city, a significant
#   population center (>1% of total pop in modern Malaysia's territory). Various
#   Malay sultanates controlled the rest of the peninsula; Brunei controlled
#   Borneo territories.
#
# 1641-1786: Dutch Empire (>100M) controlled Malacca (took from Portuguese 1641).
#   Malay sultanates controlled the rest.
#
# 1786-1914: British Empire (>100M) progressively took control: Penang (1786),
#   Province Wellesley (1800), Malacca (1824), Straits Settlements, Federated
#   Malay States (1895), Unfederated Malay States (by 1914), Sabah (1881),
#   Sarawak (1888 protectorate). Before 1914, not all territories under British
#   control.
#
# 1942-1945: Empire of Japan (>100M) occupied all of Malaya and Borneo. British
#   Empire (>100M) maintained nominal sovereignty.
#
# 1957-1963: Federation of Malaya (independent) controlled Peninsular Malaysia.
#   British Empire (>100M) still controlled Sabah and Sarawak (together ~16% of
#   population in modern Malaysia's territory).

MALAYSIA = [
    (-200000, 200, 'NO_KNOWN_POLITIES'),
    # Earliest Indianized states (Langkasuka etc.) emerged ~2nd century CE with
    # plausibly 100K+ under centralized control.
    (200, 1511, 'NOT_RELEVANT'),
    # Langkasuka, Srivijaya, various Malay sultanates, Majapahit claims, Malacca
    # Sultanate. All <100M lifetime births. No external >100M polity controlled
    # any part of modern Malaysia.
    # 1511-1914: Gap. Portuguese Empire (>100M from 1511), Dutch Empire (>100M
    # from 1641), British Empire (>100M from 1786) each controlled parts but
    # not 99% of Malaysia's territory population.
    (1914, 1942, 'British Empire'),
    # By 1914, all Malay States under British protection (Johor last, 1914).
    # Sabah under British North Borneo Company (1881), Sarawak Brooke protectorate
    # (1888). British Empire controlled 99%+ of modern Malaysia's territory.
    # 1942-1945: Gap. Empire of Japan (>100M) vs British Empire (>100M).
    (1945, 1957, 'British Empire'),
    # British Military Administration, Malayan Union (1946-48), Federation of
    # Malaya (1948-57). Sarawak and North Borneo became Crown Colonies (1946).
    # 1957-1963: Gap. Federation of Malaya independent; Sabah/Sarawak still
    # British Empire (>100M).
    (1963, 2026, 'Malaysia'),
    # Federation of Malaysia formed Sep 1963 (Malaya + Sabah + Sarawak + Singapore).
    # Singapore left Aug 1965 but is a separate country in this dataset.
]

# =============================================================================
# SINGAPORE
# =============================================================================
#
# Gap justifications: None -- all transitions are clean assignments or NOT_RELEVANT.

SINGAPORE = [
    (-200000, 1299, 'NO_KNOWN_POLITIES'),
    # Singapore was sparsely inhabited. The Kingdom of Singapura (~1299) is the
    # first polity established on the island itself. Srivijaya nominally controlled
    # the area earlier but Singapore had negligible population.
    (1299, 1819, 'NOT_RELEVANT'),
    # Kingdom of Singapura (~1299-1398), Malacca Sultanate, Johor Sultanate.
    # All <100M lifetime births. Portuguese Empire (>100M from 1511) and Dutch
    # Empire (>100M from 1641) controlled Malacca but NOT Singapore island --
    # Johor Sultanate controlled Singapore throughout.
    (1819, 1942, 'British Empire'),
    # Raffles established British trading post 1819. Formal cession 1824.
    # British controlled 99%+ of Singapore continuously.
    (1942, 1945, 'Empire of Japan'),
    # Japan conquered Singapore Feb 1942 (Fall of Singapore), renamed it Syonan-to.
    # Full de facto control of 99%+ of the population.
    (1945, 1963, 'British Empire'),
    # British reoccupied Sep 1945. Crown Colony, then self-governing state (1959)
    # with Britain retaining sovereignty over defense/foreign affairs.
    (1963, 1965, 'NOT_RELEVANT'),
    # Part of Federation of Malaysia. Malaysia <100M lifetime births (existed
    # 2 years). No external >100M polity controlled any part.
    (1965, 2026, 'Republic of Singapore'),
    # Independent city-state.
]


# =============================================================================
# VERIFICATION
# =============================================================================

if __name__ == '__main__':
    countries = {
        'Myanmar': MYANMAR,
        'Afghanistan': AFGHANISTAN,
        'Laos': LAOS,
        'Malaysia': MALAYSIA,
        'Singapore': SINGAPORE,
    }

    for name, timeline in countries.items():
        print(f"\n{'='*60}")
        print(f"  {name}")
        print(f"{'='*60}")
        prev_end = None
        for start, end, polity in timeline:
            if prev_end is not None and start > prev_end:
                gap_start = prev_end
                gap_end = start
                duration = gap_end - gap_start
                print(f"  *** GAP: {gap_start} to {gap_end} ({duration} years) ***")
            print(f"  {start:>8} to {end:>8}  {polity}")
            prev_end = end
        if prev_end and prev_end < 2026:
            print(f"  *** GAP: {prev_end} to 2026 ({2026 - prev_end} years) ***")
        print()
