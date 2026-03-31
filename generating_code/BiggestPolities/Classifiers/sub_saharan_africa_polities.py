"""
Complete polity timelines for South Africa, Kenya, Tanzania, Ghana, Angola.

Each entry is (start_year, end_year, polity_name) where end_year is exclusive.
Negative years are BCE.

Special polity names:
- NO_KNOWN_POLITIES: Before first centralized polity with >=100,000 people
- NOT_RELEVANT: All polities in this period had <100M lifetime births
  (lifetime births = avg_population x 0.04 x years_of_existence)
- Gaps between entries mean "indeterminate" -- polities existed with >100M lifetime
  births, but no single one controlled >=99% of the modern country's population.
"""

# =============================================================================
# SOUTH AFRICA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~1652. Before European colonization, South Africa was
#   inhabited by San hunter-gatherers, Khoikhoi pastoralists, and Bantu-speaking
#   farming communities. The Bantu chiefdoms (Nguni, Sotho-Tswana, Venda, Tsonga)
#   were individually small -- typically thousands to tens of thousands of people.
#   The Kingdom of Mapungubwe (~1075-1300 CE) in the Limpopo valley had ~5,000
#   people at its peak. The Mutapa Empire (from ~1430) extended into the far
#   north of modern South Africa (Limpopo) but its total population was only
#   ~500K and most was in modern Zimbabwe. No single polity with 100,000 people
#   under centralized control existed within South Africa's borders until the
#   Dutch Cape Colony grew large enough in the early-mid 1700s. However, the
#   Cape Colony was established in 1652 and reached 100K people by roughly the
#   1740s-1750s. I'll end NO_KNOWN_POLITIES at 1750, when the Cape Colony first
#   reached ~100K including enslaved people and Khoikhoi subjects.
#
# 1750-1910: NOT_RELEVANT. The Cape Colony existed but was a small colonial
#   settlement. The Dutch East India Company (VOC) that controlled it:
#   ~1602-1799, ~200 years. The VOC was a trading company, not really a polity.
#   The British Empire took over the Cape in 1806. The British Empire vastly
#   exceeds 100M lifetime births. So from 1806 onward, a polity exceeding 100M
#   births controlled part of South Africa.
#
#   Wait -- from 1806, the British Empire (>100M births) controlled the Cape
#   Colony but NOT all of South Africa. The interior had independent Zulu,
#   Xhosa, Sotho, Tswana, Pedi, Swazi, and Ndebele polities, plus the Boer
#   republics (Transvaal/Orange Free State from 1852/1854). So 1806-1910 is a
#   gap (British Empire exceeds threshold but doesn't control 99%).
#
#   Before 1806: Dutch Cape Colony under the VOC (1652-1795) and then Batavian
#   Republic (1803-1806). The Dutch Republic: ~2M avg pop x 0.04 x ~200 years
#   (1581-1795) = 16M. Under threshold. But the Cape Colony was tiny relative
#   to all of South Africa. Even if the VOC/Netherlands exceeded threshold,
#   they only controlled the southwestern corner. Most of South Africa's
#   population was in independent African polities.
#
#   Actually, I need to reconsider. The VOC/Dutch Republic is under 100M births.
#   Before 1806, no polity exceeding 100M births controlled any part of South
#   Africa (Dutch Republic under threshold, African polities all tiny). So
#   1750-1806 should be NOT_RELEVANT.
#
#   From 1806-1910: British Empire (vastly >100M births) controlled part of
#   South Africa but not 99%. This is a gap.
#
# 1750-1806: NOT_RELEVANT. Cape Colony under Dutch Republic/VOC. Dutch Republic:
#   ~2M x 0.04 x ~214 years = 17M births -- under threshold. African polities
#   (Zulu predecessors, Xhosa, Sotho, etc.) all individually tiny. No polity
#   exceeding 100M births controlled any part of South Africa.
#
# 1806-1910: Gap. British Empire took the Cape Colony (1806) and Natal (1843),
#   but Boer republics (South African Republic/Transvaal 1852-1902, Orange Free
#   State 1854-1902) and African kingdoms (Zulu Kingdom 1816-1879, Basotho
#   kingdom, etc.) remained independent. Britain gradually expanded control:
#   annexed Transvaal 1877, lost it 1881, reconquered in Boer War 1899-1902.
#   After 1902, Britain controlled all four colonies but they weren't unified.
#   Gap justification: British Empire vastly exceeds 100M lifetime births and
#   controlled the Cape Colony and Natal, but Boer republics and African
#   kingdoms controlled significant portions of the population/territory.
#
# 1910-1961: Union of South Africa. British dominion unifying Cape, Natal,
#   Transvaal, and Orange River Colony. Self-governing but under British Crown.
#   Controlled 99% of modern South Africa's territory and population.
#   (South West Africa/Namibia was administered by South Africa but is not
#   part of modern South Africa.)
#
# 1961-1994: Republic of South Africa (apartheid era). Declared a republic
#   on 31 May 1961, leaving the Commonwealth. Same government, new constitutional
#   form. The Bantustans (homelands) were nominally independent (Transkei 1976,
#   Bophuthatswana 1977, Venda 1979, Ciskei 1981) but were not recognized
#   internationally and were effectively controlled by South Africa. I'll treat
#   South Africa as controlling 99% throughout.
#
# 1994-present: Republic of South Africa (post-apartheid). New constitution,
#   democratic elections April 1994. The official name didn't change, but the
#   regime is fundamentally different. I'll distinguish them.

SOUTH_AFRICA = [
    (-200000, 1750, "NO_KNOWN_POLITIES"),
    (1750, 1806, "NOT_RELEVANT"),
    # 1806-1910: Gap.
    # Justification: British Empire (vastly exceeds 100M lifetime births) controlled
    # the Cape Colony and Natal, but Boer republics (South African Republic,
    # Orange Free State) and African kingdoms (Zulu Kingdom, Basotho, Pedi, etc.)
    # controlled significant portions of the population and territory until the
    # Boer War (1899-1902) and subsequent unification.
    (1910, 1961, "Union of South Africa"),
    (1961, 1994, "Republic of South Africa"),
    (1994, 2026, "Republic of South Africa"),
]

# =============================================================================
# KENYA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~1895. Before British colonization, Kenya was
#   inhabited by diverse groups: Swahili city-states on the coast (Mombasa,
#   Malindi, Lamu -- individually ~10-20K people each), pastoral Maasai,
#   agricultural Kikuyu, Luo, Kamba, Kalenjin, etc. The Swahili city-states
#   were small urban centers, not large centralized states. The Sultanate of
#   Zanzibar controlled the coast from 1698 (after expelling the Portuguese),
#   but the population under Zanzibari control within modern Kenya was limited
#   to a narrow coastal strip -- likely well under 100K people in Kenya itself.
#   Interior polities were acephalous or small chiefdoms, none approaching
#   100K people. The Wanga Kingdom (western Kenya) was the largest interior
#   polity but had perhaps 30-50K people.
#
#   The Imperial British East Africa Company administered the area from 1888,
#   and the East Africa Protectorate was established in 1895. Kenya's total
#   population at this time was perhaps 2-4M, but none was under a single
#   centralized polity of 100K until the British protectorate.
#
#   I'll end NO_KNOWN_POLITIES at 1895 when the British East Africa
#   Protectorate was declared, as this was the first polity with centralized
#   control over >100K people in this territory.
#
# 1895-1920: Gap. British East Africa Protectorate controlled much of Kenya,
#   but the coastal strip was technically under the Sultan of Zanzibar (leased
#   to Britain). Also, British control of the interior was incomplete in the
#   early years, with punitive expeditions continuing into the 1900s-1910s.
#   The British Empire vastly exceeds 100M lifetime births.
#   Gap justification: British Empire (vastly exceeds 100M births) controlled
#   most of Kenya through the East Africa Protectorate, but the coastal strip
#   was nominally under the Sultan of Zanzibar and interior control was being
#   consolidated.
#
# 1920-1963: Colony and Protectorate of Kenya. The interior became the Kenya
#   Colony (Crown Colony) on 23 July 1920, while the coastal strip remained
#   the Kenya Protectorate (nominally leased from Zanzibar). Both were
#   administered as a single unit by Britain. Britain controlled >99% of the
#   population. I'll treat this as a single polity.
#
# 1963-1964: Kenya (independent Commonwealth realm with Queen as head of state).
#   Independence on 12 December 1963.
#
# 1964-present: Republic of Kenya. Became a republic on 12 December 1964.

KENYA = [
    (-200000, 1895, "NO_KNOWN_POLITIES"),
    # 1895-1920: Gap.
    # Justification: British Empire (vastly exceeds 100M lifetime births) controlled
    # most of Kenya via the East Africa Protectorate, but the coastal strip was
    # nominally under the Sultan of Zanzibar, and effective British control of
    # the interior was still being consolidated through military expeditions.
    (1920, 1963, "Colony and Protectorate of Kenya"),
    (1963, 1964, "Kenya"),
    (1964, 2026, "Republic of Kenya"),
]

# =============================================================================
# TANZANIA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~1698. Similar to Kenya, mainland Tanzania had
#   Swahili city-states on the coast (Kilwa at its peak had ~10-20K people),
#   and small Bantu chiefdoms in the interior (the Ntemi chiefdoms had ~1,000
#   subjects each, with ~200 such chiefdoms). No polity in modern Tanzanian
#   territory had 100K people under centralized control.
#
#   The Sultanate of Zanzibar is part of modern Tanzania. When the Omani
#   Sultanate took control of Zanzibar and the East African coast in 1698
#   (expelling the Portuguese from Mombasa/coast), the total population
#   under centralized Omani/Zanzibari control in the region was still modest.
#   Zanzibar island itself had maybe 50-100K people. But with the coastal
#   trading towns, the sultanate likely reached 100K within modern Tanzania's
#   territory by the mid-1700s.
#
#   I'll end NO_KNOWN_POLITIES at 1750, when the Omani/Zanzibari sultanate
#   likely had >100K people under centralized control within modern Tanzania.
#   (Zanzibar is part of modern Tanzania, so the sultanate's population counts.)
#
# 1750-1885: NOT_RELEVANT. The Sultanate of Zanzibar controlled Zanzibar
#   island and the coastal strip of mainland Tanzania. The Omani Empire/
#   Sultanate of Zanzibar: population across all territories perhaps 1-2M
#   at peak, existed ~300 years (if counting from Omani takeover 1698 to
#   British protectorate 1890). 1.5M x 0.04 x 300 = 18M births. Under
#   threshold. Interior Tanzanian polities (Nyamwezi, Ha, Hehe, etc.) were
#   all small chiefdoms, individually well under 100M births each. No polity
#   exceeding 100M lifetime births controlled any part of modern Tanzania.
#
# 1885-1919: Gap. German East Africa (1885-1918) controlled mainland Tanzania.
#   German Empire: ~55M avg pop x 0.04 x 47 years (1871-1918) = 103M births.
#   Just barely exceeds 100M. But Germany didn't control Zanzibar -- Zanzibar
#   became a separate British protectorate (1890). So Germany controlled the
#   mainland but not Zanzibar. Zanzibar (~200-300K people) was ~3-5% of
#   Tanzania's total population. So Germany didn't control 99%.
#   Meanwhile, Britain (vastly >100M births) controlled Zanzibar.
#   Gap justification: German Empire (exceeds 100M births with ~103M) controlled
#   mainland Tanzania as German East Africa, while the British Empire (vastly
#   exceeds 100M births) controlled the Sultanate of Zanzibar as a protectorate.
#   Neither controlled 99% of modern Tanzania's territory/population.
#
# 1919-1961: Gap continues. After WWI, mainland Tanganyika became a British
#   League of Nations mandate (1920), then UN Trust Territory (1947). Zanzibar
#   remained a separate British protectorate under the Sultan. Britain controlled
#   both territories but they were administered separately -- Tanganyika
#   Territory and Zanzibar Protectorate were distinct administrative units.
#   However, Britain controlled >99% of the population across both...
#   Actually, the question is whether a SINGLE POLITY controlled 99%. The
#   British Empire controlled both Tanganyika and Zanzibar. So the British
#   Empire controlled >99% of modern Tanzania. But were they administered as
#   one polity? The British Empire is the overarching polity. Let me name it.
#
#   Actually wait -- Tanganyika was a League of Nations Mandate / UN Trust
#   Territory, not technically a British colony. And Zanzibar was a protectorate
#   with its own sultan. But both were under effective British control.
#   The "British Empire" as a single polity controlled both. I think this
#   qualifies as a single polity controlling 99%.
#
#   Hmm, but the existing file for Nigeria uses "Colony and Protectorate of
#   Nigeria" rather than "British Empire." The convention seems to be to name
#   the local administrative entity. For Tanzania, the local entities were
#   separate (Tanganyika Territory + Zanzibar Protectorate). So this is a gap.
#
#   Actually, re-reading the instructions: "Use this when a single polity
#   controlled territory containing at least 99% of the population within
#   this modern country's current borders." The British Empire is a single
#   polity. It controlled both Tanganyika and Zanzibar. So it controlled 99%.
#   But the convention in the existing file is to use local names. Let me
#   check -- in the Nigeria file, "Colony and Protectorate of Nigeria" is used
#   because that was a unified administrative entity. For Tanzania, the
#   equivalent would be... there wasn't a unified entity until independence.
#   I'll leave 1919-1961 as a gap since Tanganyika and Zanzibar were separate
#   British-controlled entities with no unified administration. The "polity"
#   is ambiguous -- is it the British Empire or the local administration?
#
#   On reflection, I think the British Empire counts as a single polity. But
#   the same logic would apply to the 1885-1919 period where Germany controlled
#   the mainland and Britain controlled Zanzibar -- those are two DIFFERENT
#   polities. So 1885-1919 is definitely a gap.
#
#   For 1919-1961, the British Empire controlled both, so I should assign it.
#   But what name to use? "British Empire" is too generic. The local entities
#   were "Tanganyika Territory" and "Protectorate of Zanzibar." Since they
#   were administered separately, I'll leave this as a gap too -- the lack
#   of unified administration means these were effectively two separate
#   governance structures within the empire.
#
# 1961-1964: Gap. Tanganyika became independent on 9 December 1961 as a
#   Commonwealth realm, then republic in 1962. Zanzibar became independent
#   on 10 December 1963. Zanzibar Revolution on 12 January 1964. The two
#   merged on 26 April 1964. Between Dec 1961 and April 1964, these were
#   separate states.
#   Gap justification: Tanganyika (independent 1961) and Zanzibar (independent
#   1963, revolution January 1964) were separate states. Both are part of
#   modern Tanzania but were not unified until April 1964. Tanganyika alone
#   lacked Zanzibar (~3-5% of Tanzania's population at the time).
#
#   Actually, Zanzibar's population was only ~300K out of Tanzania's ~10M
#   total at the time, so ~3%. That's above the 1% threshold. But barely.
#   I'll leave it as a gap for accuracy.
#
# 1964-present: United Republic of Tanzania. Merged 26 April 1964.
#   Initially "United Republic of Tanganyika and Zanzibar," renamed
#   "United Republic of Tanzania" on 29 October 1964.

TANZANIA = [
    (-200000, 1750, "NO_KNOWN_POLITIES"),
    (1750, 1885, "NOT_RELEVANT"),
    # 1885-1964: Gap.
    # Justification: German Empire (~103M lifetime births) controlled mainland
    # Tanzania as German East Africa (1885-1918), while the British Empire (vastly
    # exceeds 100M births) controlled Zanzibar. After 1919, Britain controlled
    # both Tanganyika (as a mandate/trust territory) and Zanzibar (as a protectorate)
    # but administered them separately. After independence, Tanganyika (1961) and
    # Zanzibar (1963) were separate states until merging in April 1964.
    (1964, 2026, "United Republic of Tanzania"),
]

# =============================================================================
# GHANA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~1500. Various states existed in what is now Ghana
#   from around the 11th century: the Dagomba Kingdom (by ~11th-13th century),
#   Bono State (~1400s), and others. But these were relatively small -- the
#   Dagomba kingdom may have had tens of thousands of people. The medieval
#   Ghana Empire (Wagadou) was NOT in modern Ghana -- it was in modern
#   Mali/Mauritania. The Songhai Empire also did not directly control
#   Ghanaian territory (its southern extent was in modern Mali/Burkina Faso,
#   though post-Songhai migrations influenced northern Ghana).
#
#   The first polity likely to reach 100K people in modern Ghana was the
#   Akwamu Kingdom (early 1600s) or possibly the emerging Akan states.
#   The Bono State (Brong kingdom) from ~1400 was significant but likely
#   under 100K. Portuguese arrived at the Gold Coast in 1471 but their
#   trading posts were tiny (hundreds of people). By ~1500-1600, emerging
#   Akan states were growing due to gold trade. I'll set the boundary at
#   1500, as by this point some Akan states were approaching or reaching
#   100K people under centralized control.
#
# 1500-1874: NOT_RELEVANT. Multiple polities existed in modern Ghana:
#   Akwamu (~1550-1730), Denkyira (~1600-1701), Ashanti Empire (1701-1896),
#   various Fante states, Dagomba, Gonja, etc. The Ashanti Empire at its peak
#   had ~3M people. Ashanti: ~2M avg x 0.04 x 195 years (1701-1896) = 15.6M
#   births. Under threshold. All other Ghanaian polities were smaller.
#   European presence was limited to coastal forts (Portuguese, Dutch, British,
#   Danish, etc.) -- tiny garrisons, not centralized control of territory.
#
#   Wait -- what about the European EMPIRES that had forts on the Gold Coast?
#   The Portuguese Empire had forts from 1482 (Elmina). The Portuguese Empire
#   (1415-1975, ~20M avg pop x 0.04 x 560 years = 448M) vastly exceeds the
#   threshold. But Portuguese forts on the Gold Coast held perhaps a few
#   hundred people and controlled negligible territory and population. The
#   instructions say "ANY polity controlling ANY PART of this modern country's
#   territory." A fort with a few hundred people controlling a few square km
#   arguably counts as "controlling part of the territory."
#
#   The instructions say: "If ANY polity controlling ANY PART of this modern
#   country's territory during this period exceeds 100M lifetime births,
#   do NOT use NOT_RELEVANT -- leave a gap instead."
#
#   Portuguese forts (1482-1642 at Elmina) controlled a tiny sliver of
#   territory. Dutch West India Company took over (1637-1872). British forts
#   from 1631. The Portuguese and Dutch empires may or may not exceed 100M
#   births, but the British Empire (from when? British presence on Gold
#   Coast from ~1631) certainly does.
#
#   However, the threshold question is about the POLITY's total lifetime births
#   across all its territories. The British Empire (1583?-1997): clearly
#   exceeds 100M. And it controlled forts on the Gold Coast from ~1631.
#   So from ~1631, a polity exceeding 100M births controlled part of Ghana.
#
#   But the British forts controlled <1% of Ghana's population until the
#   19th century. Hmm, but the instructions say "any part" -- even a tiny
#   fort counts. The instructions are: if ANY polity controlling ANY PART
#   exceeds 100M births, don't use NOT_RELEVANT.
#
#   I think the intent is about meaningful territorial control, not a single
#   fort. But the instructions are clear. Let me err on the side of leaving
#   a gap. From 1631 (British arrival on Gold Coast), a polity with >100M
#   births controlled part of Ghana. Before 1631, Portuguese forts existed
#   from 1482. Portuguese Empire exceeds 100M births.
#
#   So the entire period 1482-1874 has European empires (>100M births)
#   controlling parts (even if tiny) of Ghana. I should leave it as a gap.
#
#   But this feels overly strict. The European forts controlled <0.01% of
#   Ghana's territory and population. I'll follow the instructions literally
#   and leave it as a gap from 1482 onward.
#
#   Actually, let me re-read: "If ANY polity controlling ANY PART of this
#   modern country's territory during this period exceeds 100M lifetime
#   births, do NOT use NOT_RELEVANT." The Portuguese Empire from 1482
#   controlled Elmina fort. The Portuguese Empire's total lifetime births
#   across all territories exceeds 100M. So I cannot use NOT_RELEVANT
#   from 1482 onward.
#
#   1500-1482 is only 18 years backward. Let me just set the gap from 1500.
#
# 1500-1874: Gap. Multiple African polities (Ashanti, Fante, Dagomba, Gonja,
#   etc.) controlled different parts of Ghana. European empires (Portuguese
#   from 1482, Dutch from 1637, British from 1631, Danish from 1658) controlled
#   coastal forts. The Portuguese Empire and British Empire both exceed 100M
#   lifetime births. No single polity controlled 99% of Ghana's population.
#
# 1874-1957: Gap continues. Britain established the Gold Coast Crown Colony
#   in 1874 (southern coast), but the Ashanti Empire remained independent
#   until 1896 (British conquest) and became a protectorate in 1902. The
#   Northern Territories became a protectorate in 1901. British Togoland
#   (part of modern Ghana) was a League of Nations mandate from 1922. These
#   weren't unified into a single entity until 1956 (when British Togoland
#   joined the Gold Coast in a plebiscite).
#   Gap justification: British Empire (vastly exceeds 100M births) controlled
#   multiple separate entities within modern Ghana: Gold Coast Colony (1874),
#   Ashanti (protectorate 1902), Northern Territories (protectorate 1901),
#   British Togoland (mandate 1922). These were separate administrative units.
#   Furthermore, the Ashanti Empire (1701-1896) controlled a large portion
#   of the population independently until 1896.
#
#   Actually, by 1902 Britain controlled all of what would become Ghana
#   (Gold Coast Colony + Ashanti + Northern Territories). British Togoland
#   was added in 1922 but contained only a small fraction of the population.
#   From 1902, Britain controlled >99% of modern Ghana through contiguous
#   administrative units. But these were three separate entities (Gold Coast
#   Colony, Ashanti Protectorate, Northern Territories Protectorate).
#   Were they a single polity? They were governed by a single governor.
#   Let me check...
#
#   The Gold Coast Colony, Ashanti, and Northern Territories were all under
#   the Governor of the Gold Coast. They formed a de facto single
#   administrative unit. British Togoland (added 1922) was also administered
#   by the Gold Coast governor. So from 1902, the "Gold Coast" as a British
#   colonial entity controlled >99% of modern Ghana (British Togoland was
#   tiny and not yet part, but <1% of population).
#
#   So: 1902-1957 can be "Gold Coast" (British colony).
#
# 1500-1902: Gap (see justifications above).
# 1902-1957: Gold Coast (British colony). Governor of Gold Coast administered
#   Gold Coast Colony, Ashanti, and Northern Territories as a unified entity.
#   British Togoland added in 1922. Controlled >99% of modern Ghana.
# 1957-1960: Ghana (independent, Commonwealth realm).
# 1960-present: Republic of Ghana. Became a republic on 1 July 1960.

GHANA = [
    (-200000, 1500, "NO_KNOWN_POLITIES"),
    # 1500-1902: Gap.
    # Justification: Multiple polities controlled parts of modern Ghana.
    # The Ashanti Empire (~2M avg pop, 1701-1896) controlled the interior.
    # European empires controlled coastal forts: Portuguese Empire (from 1482,
    # exceeds 100M lifetime births), British Empire (from 1631, vastly exceeds
    # 100M lifetime births). Fante states, Dagomba Kingdom, and Gonja Kingdom
    # controlled other regions. No single polity controlled 99%.
    (1902, 1957, "Gold Coast"),
    (1957, 1960, "Ghana"),
    (1960, 2026, "Republic of Ghana"),
]

# =============================================================================
# ANGOLA
# =============================================================================
# NO_KNOWN_POLITIES: ends ~1400. Before the Kingdom of Kongo (emerged ~1390s),
#   Angola was inhabited by Bantu-speaking peoples organized into small
#   chiefdoms. The Kingdom of Kongo in northern Angola/western DRC was the
#   first centralized state in this region. By the time Portuguese contact
#   occurred (1483), Kongo had ~500K people with its capital Mbanza Kongo
#   having ~50K. The Kongo kingdom's core was partly in modern northern
#   Angola. By ~1400, it likely exceeded 100K people.
#
#   Other kingdoms in Angola: Kingdom of Ndongo (Mbundu people, central
#   Angola) emerged in the 1500s, Kingdom of Matamba, Lunda Empire (NE Angola,
#   from ~1600). But Kongo was the earliest to reach 100K.
#
# 1400-1920: NOT_RELEVANT? Let me check each polity:
#   - Kingdom of Kongo: ~500K avg x 0.04 x ~500 years (1390-~1914) = 10M. Under.
#   - Kingdom of Ndongo: ~200K x 0.04 x ~150 years (1500s-1671) = 1.2M. Under.
#   - Lunda Empire: ~175K x 0.04 x ~250 years = 1.75M. Under.
#   - Portuguese Empire (from 1575 in Luanda): ~20M avg x 0.04 x 560 = 448M.
#     EXCEEDS 100M.
#
#   From 1575, the Portuguese Empire controlled part of Angola (Luanda and
#   coastal areas) and the Portuguese Empire exceeds 100M lifetime births.
#   So I cannot use NOT_RELEVANT from 1575 onward.
#
#   1400-1575: Only African kingdoms, all under threshold. NOT_RELEVANT.
#
# 1575-1920: Gap. Portuguese Empire controlled the coast (Luanda colony
#   from 1575) and gradually expanded inland. The Kingdom of Kongo, Kingdom
#   of Ndongo, Kingdom of Matamba, Lunda Empire, and other polities controlled
#   the interior. Portuguese Empire vastly exceeds 100M lifetime births.
#   Gap justification: Portuguese Empire (exceeds 100M lifetime births with
#   ~448M) controlled Luanda and coastal Angola from 1575, gradually expanding
#   inland. But the interior was controlled by the Kingdom of Kongo, Kingdom
#   of Ndongo/Matamba, Lunda Empire, and other African polities. Portugal
#   did not achieve effective control of all Angola until ~1920.
#
# 1920-1975: Portuguese Angola. By ~1920, Portugal had achieved effective
#   control over essentially all of Angola's territory and population (the
#   last resistance in the southeast was overcome by ~1915-1920). Angola
#   became an "overseas province" of Portugal in 1951 but was effectively
#   a colony throughout. Portugal controlled >99% of the population.
#
# 1975-1992: People's Republic of Angola. Independence on 11 November 1975.
#   MPLA declared the People's Republic. Civil war began immediately, with
#   UNITA and FNLA controlling parts of the country. However, the MPLA
#   government controlled the capital and most major cities. UNITA controlled
#   significant rural territory, especially in the south and east. Did the
#   MPLA control 99%? During the civil war, UNITA controlled perhaps 10-30%
#   of territory and 10-20% of population at various times. This is a gap.
#
#   Actually, UNITA and FNLA were rebel movements, not internationally
#   recognized governments. The People's Republic of Angola was the
#   internationally recognized sovereign state (recognized by the UN, OAU,
#   etc.). UNITA controlled territory but was not a separate polity in the
#   international sense. The question asks about polities. I think the
#   People's Republic was the polity in control, despite the civil war.
#
#   But the instructions say "a single polity controlled territory
#   containing at least 99% of the population." If UNITA controlled 10-20%
#   of the population, then the MPLA government didn't control 99%.
#   UNITA itself: avg maybe ~2M people under control x 0.04 x 27 years =
#   2.16M births. Way under threshold. And it's not clear UNITA was a
#   separate "polity" rather than a rebel movement. But the instruction
#   says "if a significant region (>1% of population) was independent or
#   under different control, do NOT assign."
#
#   I think I should leave the civil war period (1975-2002) as a gap.
#   The People's Republic/Republic of Angola was recognized but didn't
#   control 99% of the population.
#
#   Wait, but what polity with >100M births was in play? UNITA had <100M
#   births. South Africa intervened (South African Border War) and South
#   Africa as a state exceeds 100M births? South Africa from 1961-2026:
#   ~35M avg x 0.04 x 65 = 91M. Borderline, probably not.
#   Cuba intervened on the MPLA side. Cuba: ~8M avg x 0.04 x ~65 years = 20.8M.
#   Under threshold. Soviet Union: vastly exceeds. The USSR provided support
#   but didn't control territory directly.
#
#   Hmm. The question is whether UNITA itself or any other entity
#   controlling Angolan territory exceeded 100M. UNITA itself: no.
#   South Africa occupied southern Angola at times but... South Africa
#   as the Republic of South Africa (1961-present) isn't really a polity
#   with 100M lifetime births (only ~91M). The Union + Republic combined:
#   5M avg (1910) growing to 55M (2020), avg ~25M x 0.04 x 116 = 116M.
#   That exceeds. And South Africa occupied parts of southern Angola in
#   the 1970s-1980s. So South Africa (>100M births) controlled part of
#   Angola. This makes it a gap, not NOT_RELEVANT.
#
#   Actually, this is getting complicated. Let me just make the entire
#   1975-2002 period a gap on the grounds that the Angolan civil war
#   meant no single polity controlled 99%, and South Africa (>100M births
#   across Union + Republic) occupied parts of southern Angola.
#
# 1975-2002: Gap. Angolan Civil War. MPLA government controlled major cities,
#   UNITA controlled rural south/east. South African military occupied parts
#   of southern Angola (1975-1988). Cuban troops supported MPLA. No single
#   polity controlled 99%.
#
# 2002-present: Republic of Angola. UNITA leader Jonas Savimbi killed
#   February 2002, ceasefire April 2002. The Republic of Angola (name since
#   1992, when the People's Republic was renamed) has controlled essentially
#   all territory since 2002.

ANGOLA = [
    (-200000, 1400, "NO_KNOWN_POLITIES"),
    (1400, 1575, "NOT_RELEVANT"),
    # 1575-1920: Gap.
    # Justification: Portuguese Empire (exceeds 100M lifetime births with ~448M
    # total) controlled Luanda and coastal Angola from 1575, expanding gradually
    # inland over centuries. Interior polities -- Kingdom of Kongo, Kingdom of
    # Ndongo, Kingdom of Matamba, Lunda Empire -- controlled the rest. Portugal
    # did not achieve effective control of all Angola until ~1920.
    (1920, 1975, "Portuguese Angola"),
    # 1975-2002: Gap.
    # Justification: Angolan Civil War. MPLA government (People's Republic of
    # Angola, renamed Republic of Angola in 1992) controlled major cities but
    # UNITA controlled significant rural territory in the south and east.
    # South Africa (Union + Republic: ~25M avg pop x 0.04 x 116 years = 116M
    # births, exceeding threshold) occupied parts of southern Angola during the
    # South African Border War (1975-1988).
    (2002, 2026, "Republic of Angola"),
]


# =============================================================================
# Summary / Validation
# =============================================================================
def validate_timeline(name, timeline):
    """Check that entries don't overlap and are in chronological order."""
    errors = []
    for i, (start, end, polity) in enumerate(timeline):
        if start >= end:
            errors.append(f"  Entry {i}: start ({start}) >= end ({end}): {polity}")
        if i > 0:
            prev_end = timeline[i-1][1]
            if start < prev_end:
                errors.append(
                    f"  Entry {i}: start ({start}) < previous end ({prev_end}): "
                    f"{polity} overlaps with {timeline[i-1][2]}"
                )
    if errors:
        print(f"{name}: ERRORS")
        for e in errors:
            print(e)
    else:
        # Check for gaps
        gaps = []
        for i in range(1, len(timeline)):
            prev_end = timeline[i-1][1]
            curr_start = timeline[i][0]
            if curr_start > prev_end:
                gaps.append(f"  Gap: {prev_end} to {curr_start}")
        print(f"{name}: OK ({len(timeline)} entries, {len(gaps)} gaps)")
        for g in gaps:
            print(g)


if __name__ == "__main__":
    for name, timeline in [
        ("South Africa", SOUTH_AFRICA),
        ("Kenya", KENYA),
        ("Tanzania", TANZANIA),
        ("Ghana", GHANA),
        ("Angola", ANGOLA),
    ]:
        validate_timeline(name, timeline)
        print()
