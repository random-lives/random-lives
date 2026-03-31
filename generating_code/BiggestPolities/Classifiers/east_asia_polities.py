"""
Polity timelines for East Asian countries: China, Hong Kong, Taiwan, Mongolia, Japan.

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
# CHINA
# =============================================================================
POLITIES['China'] = [
    (-200000, -1600, 'NO_KNOWN_POLITIES'),

    # GAP -1600 to 1279:
    # Shang, Zhou, Qin, Han, Sui, Tang, Song, and other dynasties controlled large
    # parts of modern China but none controlled 99% of modern China's borders
    # (missing Manchuria, Xinjiang, Tibet, or fragmented during interregna).
    #
    # Justification for gap (not NOT_RELEVANT):
    # - Shang Dynasty: ~2-5M people for ~550 yrs => 44-110M births (borderline)
    # - Zhou Dynasty: ~20-30M avg for ~800 yrs => 640-960M births (far exceeds 100M)
    # - Han Dynasty: ~50-60M avg for ~400 yrs => 800-960M births
    # - Tang Dynasty: ~50-80M avg for ~290 yrs => 580-928M births
    # - Song Dynasty: ~60-100M avg for ~320 yrs => 768-1280M births
    # All controlled major portions of modern China's territory.

    (1279, 1368, 'Yuan Dynasty'),
    # Mongol-ruled dynasty. Controlled ALL of modern China including Manchuria,
    # Tibet, Xinjiang, Yunnan, and far south. First dynasty to control 99%+ of
    # modern China's population within its borders.

    # GAP 1368 to 1759:
    # Ming Dynasty (1368-1644) controlled China proper but NOT Manchuria, Tibet,
    # or Xinjiang — regions with ~3-8% of the population within modern China's borders.
    # Qing Dynasty (1644-1759) gradually expanded: China proper by ~1650s,
    # Taiwan 1683, Tibet ~1720, Xinjiang 1759.
    #
    # Justification for gap (not NOT_RELEVANT):
    # - Ming Dynasty: ~100M avg for 276 yrs => 1.1B births
    # - Qing Dynasty (pre-1759): ~150M+ people, clearly >100M births

    (1759, 1912, 'Qing Dynasty'),
    # Full control of all territory within modern China's borders.
    # (Taiwan and Hong Kong have separate entries.)

    # GAP 1912 to 1951:
    # Republic of China era: warlord period, Japanese invasion (Manchukuo 1932-1945,
    # occupation of eastern China 1937-1945), civil war. Tibet functionally
    # independent 1912-1950. No single polity controlled 99%+.
    #
    # Justification for gap (not NOT_RELEVANT):
    # - Republic of China: ~400-500M people, far exceeds 100M births
    # - Empire of Japan: ~70-100M people across empire, >100M births
    #   Controlled Manchuria and large parts of eastern China.

    (1951, 2026, "People's Republic of China"),
    # Tibet incorporated 1950-51. PRC controls all of modern China's territory.
]

# =============================================================================
# HONG KONG
# =============================================================================
POLITIES['Hong Kong'] = [
    (-200000, -214, 'NO_KNOWN_POLITIES'),
    # Baiyue peoples, no centralized polity with >=100K people.
    # Qin Dynasty conquered the far south and established Nanhai Commandery ~214 BCE.

    (-214, -206, 'Qin Dynasty'),
    # Qin controlled 100% of Hong Kong's territory as part of Nanhai Commandery.

    (-206, -111, 'NOT_RELEVANT'),
    # Nanyue Kingdom controlled this area after Qin collapse.
    # Nanyue: ~1-2M people for 95 yrs => 3.8-7.6M births. Under 100M.
    # Han Dynasty existed but did NOT control Hong Kong territory (Nanyue was independent
    # until Han conquest in 111 BCE). No polity controlling HK exceeded 100M births.

    (-111, 9, 'Western Han Dynasty'),
    (9, 23, 'Xin Dynasty'),
    (23, 220, 'Eastern Han Dynasty'),
    # Han and successor controlled 100% of Hong Kong as part of Nanhai/Jiaozhi region.

    (220, 280, 'NOT_RELEVANT'),
    # Eastern Wu (Three Kingdoms) controlled Hong Kong area.
    # Wu: ~10-11M people for 59 yrs => 23.6-26M births. Under 100M.
    # Wei and Shu did not control Hong Kong. No polity controlling HK exceeded 100M.

    (280, 316, 'Western Jin Dynasty'),
    # Unified dynasty, controlled 100% of Hong Kong.

    (316, 589, 'NOT_RELEVANT'),
    # Successive Southern Dynasties (Eastern Jin, Liu Song, Southern Qi, Liang, Chen)
    # each controlled Hong Kong. Each had ~5-10M people for ~30-100 years.
    # Largest: Eastern Jin ~8M × 0.04 × 103 yrs = 33M births. Under 100M.
    # Northern dynasties did not control Hong Kong.
    # No polity controlling HK exceeded 100M lifetime births.

    (589, 618, 'Sui Dynasty'),
    (618, 907, 'Tang Dynasty'),
    # Sui and Tang controlled 100% of Hong Kong.

    (907, 971, 'NOT_RELEVANT'),
    # Southern Han kingdom (one of Ten Kingdoms) controlled Hong Kong area.
    # Southern Han: ~2-3M people for 54 yrs => 4.3-6.5M births. Under 100M.
    # No other polity controlled Hong Kong during this period.

    (971, 1127, 'Song Dynasty'),
    # Northern Song conquered Southern Han in 971. Controlled 100% of Hong Kong.

    (1127, 1279, 'Southern Song Dynasty'),
    # After losing the north to Jurchen Jin, Southern Song retained control of the south
    # including Hong Kong. 100% of HK under Southern Song control.

    (1279, 1368, 'Yuan Dynasty'),
    (1368, 1644, 'Ming Dynasty'),
    (1644, 1842, 'Qing Dynasty'),
    # Each controlled 100% of Hong Kong's territory.

    # GAP 1842 to 1898:
    # Hong Kong Island ceded to Britain 1842 (Treaty of Nanking).
    # Kowloon Peninsula ceded 1860. New Territories remained under Qing until 1898 lease.
    # Split control: Britain held HK Island + Kowloon, Qing held New Territories.
    # Neither controlled 99% of HK's population.
    #
    # Justification for gap (not NOT_RELEVANT):
    # - British Empire: ~400M+ people across all territories, far exceeds 100M births.
    # - Qing Dynasty: ~300-400M people, far exceeds 100M births.

    (1898, 1941, 'British Hong Kong'),
    # New Territories leased 1898, completing British control of all modern HK territory.

    (1941, 1945, 'Empire of Japan'),
    # Japanese occupation of Hong Kong, December 1941 to August 1945.

    (1945, 1997, 'British Hong Kong'),
    (1997, 2026, "People's Republic of China"),
    # Handover of sovereignty 1 July 1997. Hong Kong SAR under PRC.
]

# =============================================================================
# TAIWAN
# =============================================================================
POLITIES['Taiwan'] = [
    (-200000, 1624, 'NO_KNOWN_POLITIES'),
    # Austronesian indigenous peoples. No centralized polity with >=100K people.
    # Tribal societies without state-level organization.

    # GAP 1624 to 1662:
    # Dutch East India Company controlled southwestern Taiwan (Fort Zeelandia, 1624-1662).
    # Spanish Empire controlled northern Taiwan (1626-1642).
    # Majority of Taiwan's population (~100-200K indigenous) was outside European control.
    # No single power controlled 99% of Taiwan's population.
    #
    # Justification for gap (not NOT_RELEVANT):
    # - Spanish Empire (1626-1642): controlled northern Taiwan.
    #   Spain: ~20-30M people in metropole + ~30-50M across colonies for centuries.
    #   50M × 0.04 × 300 = 600M births. Far exceeds 100M.

    (1662, 1683, 'NOT_RELEVANT'),
    # Kingdom of Tungning (Koxinga's regime) controlled western Taiwan.
    # ~150-200K people for 21 years => ~126-168K births. Far under 100M.
    # Qing Dynasty did not yet control Taiwan. No other polity controlled any part.

    (1683, 1895, 'Qing Dynasty'),
    # Qing conquered Tungning 1683. Controlled Taiwan as part of Fujian Province,
    # later Taiwan Province (1887). Controlled 99%+ of population (indigenous mountain
    # peoples were <1% by late Qing era due to Han immigration).

    (1895, 1945, 'Empire of Japan'),
    # Treaty of Shimonoseki. Japan controlled all of Taiwan including indigenous areas.

    (1945, 2026, 'Republic of China'),
    # ROC took control after Japanese surrender. Retreated to Taiwan 1949.
    # Controlled 100% of Taiwan's territory continuously.
]

# =============================================================================
# MONGOLIA
# =============================================================================
POLITIES['Mongolia'] = [
    (-200000, -209, 'NO_KNOWN_POLITIES'),
    # Nomadic pastoral peoples. No centralized polity with >=100K people.
    # Xiongnu confederation formed ~209 BCE under Modu Chanyu.

    (-209, 630, 'NOT_RELEVANT'),
    # Xiongnu (~209 BCE - 93 CE): ~1-2M people for ~300 yrs => 12-24M births. Under 100M.
    # Rouran Khaganate (~330-555): ~1-2M for ~225 yrs => 9-18M births. Under 100M.
    # First Turkic Khaganate (~552-603): ~2-3M for ~51 yrs => 4-6M births. Under 100M.
    # Eastern Turkic Khaganate (603-630): ~1-2M for ~27 yrs => 1-2M births. Under 100M.
    # No polity controlling any part of modern Mongolia exceeded 100M lifetime births.

    # GAP 630 to 682:
    # Tang Dynasty defeated the Eastern Turks in 630 and established the Anbei
    # Protectorate over Mongolia. Tang exercised direct administrative control.
    #
    # Justification for gap (not NOT_RELEVANT):
    # - Tang Dynasty: ~50-80M avg population for 289 yrs => 580-925M births.
    #   Far exceeds 100M. Controlled parts of modern Mongolia via protectorates.
    #   But did not control 99% of Mongolia's (sparse) population — many nomadic
    #   groups remained outside Tang administrative control.

    (682, 1206, 'NOT_RELEVANT'),
    # Second Turkic Khaganate (682-744): ~2M for 62 yrs => 5M births. Under 100M.
    # Uyghur Khaganate (744-840): ~1-2M for 96 yrs => 4-8M births. Under 100M.
    # Khitan Liao Dynasty (907-1125): controlled parts of Mongolia.
    #   ~4-5M people for 218 yrs => 35-44M births. Under 100M.
    # Jurchen Jin Dynasty (1115-1234): controlled parts of southern Mongolia.
    #   ~40-50M people for 119 yrs => 190-238M births. Over 100M!
    #
    # Wait — Jin Dynasty controlled parts of Mongolia? Jin controlled Manchuria and
    # northern China. Their northern border touched southern Mongolia but they did not
    # exercise control over the Mongolian steppe. The Mongolic peoples (Khamag Mongol,
    # Keraites, Naimans) were independent. Jin built border walls to keep them out.
    # Jin did NOT control any part of modern Mongolia's territory.
    #
    # Song Dynasty: did not control Mongolia.
    # No polity controlling any part of modern Mongolia exceeded 100M lifetime births
    # during 682-1206.

    (1206, 1368, 'Mongol Empire'),
    # Founded by Genghis Khan. At peak controlled ~100M+ people across Eurasia.
    # Mongolia was the heartland — 100% under Mongol control.
    # After Kublai Khan's death (1294), empire fragmented into khanates, but the
    # Yuan Dynasty (Great Khanate) retained direct control of Mongolia until 1368.

    (1368, 1691, 'NOT_RELEVANT'),
    # Northern Yuan (1368-1388) and successor Mongol khanates.
    # Mongolia's population ~1-2M. Northern Yuan: 1.5M × 0.04 × 20 = 1.2M births.
    # Successor khanates (Oirat, Eastern Mongol, Khalkha): similarly small.
    # Khalkha Mongols controlled most of modern Mongolia ~1470s-1691.
    # ~600K × 0.04 × 220 = 5.3M births. Under 100M.
    # Ming Dynasty did NOT control Mongolia — the Great Wall was the border.
    # No polity controlling any part of modern Mongolia exceeded 100M lifetime births.

    (1691, 1911, 'Qing Dynasty'),
    # Khalkha Mongols submitted to Qing Emperor Kangxi in 1691 after Dzungar
    # invasions. Qing controlled all of Outer Mongolia (modern Mongolia).

    (1911, 1919, 'Bogd Khanate of Mongolia'),
    # Declared independence December 1911 after Qing collapse.
    # Bogd Khan (Jebtsundamba Khutuktu) as theocratic head of state.

    # GAP 1919 to 1924:
    # Chinese warlord Xu Shuzheng occupied Mongolia (1919-1921).
    # Baron von Ungern-Sternberg briefly seized Urga (Feb-July 1921).
    # Mongolian People's Party with Soviet support took power July 1921.
    # Bogd Khan retained as nominal head until death 1924.
    # Multiple competing authorities; chaotic period.
    #
    # Justification for gap (not NOT_RELEVANT):
    # - Republic of China: ~400M+ people, far exceeds 100M births.
    #   Chinese forces occupied Mongolia 1919-1921.
    # - Soviet Russia/USSR: ~150M people, exceeds 100M births.
    #   Soviet forces intervened 1921.

    (1924, 1992, "Mongolian People's Republic"),
    # Proclaimed after Bogd Khan's death, 26 November 1924.
    # Soviet-aligned single-party state. Controlled 100% of modern Mongolia.

    (1992, 2026, 'Mongolia'),
    # New democratic constitution adopted 12 February 1992.
]

# =============================================================================
# JAPAN
# =============================================================================
POLITIES['Japan'] = [
    (-200000, 300, 'NO_KNOWN_POLITIES'),
    # Jōmon and early Yayoi cultures. Yamato polity begins consolidating in the
    # 3rd-4th century CE but no centralized polity with >=100K people before ~300 CE.

    (300, 710, 'NOT_RELEVANT'),
    # Yamato/Kofun period. Yamato kingdom gradually unified central and western Japan.
    # Japan's population ~3-5M. Yamato: ~4M avg × 0.04 × 410 yrs = 65.6M births.
    # Under 100M. Other polities on the islands (Emishi, Kumaso) were small.
    # No polity controlling any part of modern Japan exceeded 100M lifetime births.
    # (No foreign power controlled Japan.)

    (710, 794, 'Nara Period'),
    # Centralized imperial state under ritsuryō legal system. Capital at Heijō-kyō (Nara).
    # Controlled 99%+ of Japan's population. Emishi in far northeast were <1%.

    (794, 1185, 'Heian Period'),
    # Imperial court moved to Heian-kyō (Kyoto). Single centralized polity.
    # Power gradually devolved to Fujiwara regents, then to retired emperors (insei),
    # but remained a single government controlling 99%+ of Japan's population.

    (1185, 1333, 'Kamakura Shogunate'),
    # Minamoto Yoritomo established military government (bakufu) at Kamakura.
    # Hōjō regents held real power from 1203. Emperor nominal.
    # Single effective government controlling 99%+ of population.

    # GAP 1333 to 1336:
    # Kenmu Restoration: Emperor Go-Daigo ruled directly after Kamakura fell.
    # Brief period, quickly descended into civil war as Ashikaga Takauji rebelled.
    #
    # Actually, Go-Daigo controlled 99%+ of Japan for 1333-1335. By 1336 Ashikaga
    # had established a rival court. This 3-year period is a named polity:

    (1333, 1336, 'Kenmu Restoration'),
    # Emperor Go-Daigo's direct rule after the fall of the Kamakura Shogunate.

    (1336, 1467, 'Muromachi Shogunate'),
    # Ashikaga Takauji established shogunate. Northern/Southern Court schism (Nanboku-chō)
    # lasted until 1392, but the Southern Court controlled <1% of Japan's population
    # (confined to Yoshino mountains). Ashikaga shogunate controlled 99%+.

    # GAP 1467 to 1590:
    # Sengoku period. Ōnin War (1467) shattered central authority. Japan fragmented
    # among competing daimyō. Ashikaga shogunate continued nominally until 1573 but
    # exercised no real control outside Kyoto area.
    #
    # Justification for gap (not NOT_RELEVANT):
    # - Muromachi Shogunate (as full polity 1336-1573): Japan's avg population ~10-12M
    #   over 237 years => 12M × 0.04 × 237 = 114M births. Exceeds 100M.
    #   Controlled parts of Japan (Kinai region) throughout Sengoku period.

    (1590, 1603, 'Toyotomi Regime'),
    # Toyotomi Hideyoshi completed unification of Japan 1590 (Siege of Odawara).
    # After his death (1598), Tokugawa Ieyasu won Battle of Sekigahara (1600) but
    # Toyotomi clan nominally remained until Tokugawa became shogun 1603.

    (1603, 1868, 'Tokugawa Shogunate'),
    # Tokugawa Ieyasu became shogun 1603. Centralized feudal system (bakuhan taisei).
    # Controlled 99%+ of Japan's population. Ryukyu Kingdom was under Satsuma domain
    # influence from 1609 but its population was <1% of Japan's total.

    (1868, 1947, 'Empire of Japan'),
    # Meiji Restoration (1868). Ryukyu annexed as Okinawa Prefecture (1879).
    # Hokkaido formally incorporated. Controlled 100% of modern Japan.
    # Includes Taishō and early Shōwa eras through end of WWII.

    (1947, 2026, 'Japan'),
    # New constitution promulgated 3 May 1947. Sovereignty formally restored by
    # San Francisco Treaty 1952. Okinawa returned by US 1972 (was <1% of population).
]
