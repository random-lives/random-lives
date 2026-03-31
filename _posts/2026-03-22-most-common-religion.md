---
layout: post
title: "What is the most common religion in history?"
date: 2026-03-22
permalink: /blog/most-common-religion/
published: false
mathjax: true
---

# Research Notes: Most Common Religion in History

**Status**: Early research / category definition phase

## The Question

Of the ~117 billion humans who have ever lived, what religion did they follow? Specifically: what religion would a randomly sampled person say they were at the time of their death (or be considered, if they died as a child)?

---

## Proposed Categories

### Christianity (split at Council of Chalcedon 451, then Reformation 1517)
- **Early Christianity** (pre-451)
- **Catholic** (Latin/Western church, post-451) — includes pre-1054 Latin Christianity retroactively
- **Eastern Orthodox** (Greek/Eastern church, post-451) — includes pre-1054 Greek Christianity retroactively
- **Oriental Orthodox** (post-451: Coptic, Armenian, Syriac, Ethiopian)
- **Church of the East** (Nestorian, post-451)
- **Protestant** (post-1517)
- **Other Christian** (Latter-day Saints, JWs, etc.)

### Islam
- **Sunni**
- **Shia**
- **Other Muslim** (Ibadi, Ahmadiyya, etc.)

### Buddhism
- **Theravada**
- **Mahayana**
- **Vajrayana** (Tibetan)
- **Early Buddhism** (pre-school differentiation, ~500 BCE–~200 CE)

### Hinduism
- **Vaishnavism**
- **Shaivism**
- **Shaktism**
- **Smartism**
- **Other Hindu / undifferentiated Hindu**

### Other named religions
- **Judaism**
- **Sikhism**
- **Jainism**
- **Zoroastrianism**
- **Manichaeism**
- **Chinese folk religion** — default for syncretic Chinese practitioners. Anyone who picks and chooses among Buddhism/Taoism/Confucianism without exclusivist identity goes here. Only assign to Buddhism/Taoism/Confucianism for people with strong exclusivist commitment (monks, sectarian adherents).
- **Taoism** (exclusivist Taoists only)
- **Confucianism** (exclusivist Confucians only — question whether this is meaningful)
- **Shinto**
- **Other named religion** (catch-all for Tengrism, Druze, Baha'i, etc.)

### Ancient polytheistic religions (grouped in blog post display)
- **Greco-Roman polytheism**
- **Egyptian polytheism**
- **Mesopotamian polytheism**
- **Mesoamerican polytheism** (Aztec, Maya, etc.)
- Others as needed (Norse, Celtic — likely too small to matter)

### Broad categories
- **Folk/traditional religion** (animism, shamanism, other polytheism not covered above)
- **No religion** (explicit non-belief / non-identification)

---

## Key Boundary Decisions

- **Christianity split at 451 (Chalcedon)**: Pre-451 = "Early Christianity." Post-451 Latin West = "Catholic," Greek East = "Eastern Orthodox." Somewhat anachronistic (formal schism is 1054) but reflects real institutional distinction between Latin and Greek churches from early on.
- **Chinese syncretic religion**: LLM distributes freely, but with guidance that non-exclusivist practitioners (vast majority) default to "Chinese folk religion." Only assign Taoism/Buddhism/Confucianism for strong exclusivist identity.
- **Japanese religion**: Similar — Shinto as primary for most Japanese, Buddhism for committed practitioners.
- **Vedic religion -> Hinduism**: Pre-500 BCE Vedic religion classified as "Other Hindu / undifferentiated Hindu" (treats as ancestral Hinduism).
- **Ancient polytheisms**: Named categories tracked separately, grouped under "Ancient polytheistic religions" in display.

---

## Open Questions

1. **Confucianism as a religion**: Is it meaningful to have an exclusivist "Confucianism" category? Some Neo-Confucians explicitly rejected Buddhist metaphysics.
2. **African traditional religions**: Lumped as "folk/traditional" given extreme diversity and small sample sizes.
3. **Hindu sect dating**: When do Vaishnavism/Shaivism become distinct enough to classify separately? Bhakti movement (~7th century) is a natural starting point.
4. **Smartism**: When does it emerge as a distinct identity? Adi Shankara (~8th century) is the traditional founder.
5. **"No religion"**: Need to define carefully. Modern Chinese people under CCP? Soviet citizens? Or only people who actively profess non-belief?

---

## Classification of 250 Existing Random Lives

Below is the religion classification of all 250 biographical stories in `_lives/`. Classification is based on time period, location, and religious terms found in the narrative text.

**Methodology**: Keyword extraction from narrative text + inference from time/place. Where the narrative explicitly mentions a religion, that is used. Where it doesn't, religion is inferred from the person's time and place (e.g., a 1200 AD Egyptian is almost certainly Sunni Muslim).

**Confidence levels**:
- No qualifier = explicit in text or very high confidence from context
- "(probable)" = high confidence but some ambiguity
- "(inferred)" = no explicit religious markers in text, classified by time/place
- "NEEDS REVIEW" = genuinely uncertain, multiple plausible religions

### Summary Statistics

| Category | Count | % of 250 |
|----------|-------|----------|
| Hindu (all varieties) | 56 | 22.4% |
| Folk/traditional (all) | 48 | 19.2% |
| Chinese folk religion (all) | 29 | 11.6% |
| Sunni Islam (all) | 20 | 8.0% |
| Catholic | 17 | 6.8% |
| Buddhism (all) | 11 | 4.4% |
| Eastern Orthodox (all) | 10 | 4.0% |
| Ancient polytheism | 7 | 2.8% |
| Protestant (all) | 4 | 1.6% |
| Other named religions | 4 | 1.6% |
| Mesoamerican polytheism | 3 | 1.2% |
| Ambiguous/needs review | 6 | 2.4% |
| Other | 2 | 0.8% |

Note: These are weighted by historical births (the 250 people are randomly sampled from all of human history weighted by birth rates), so this is a rough preview of what the full analysis should look like. Hindu dominance reflects India's large population; folk/traditional reflects the deep past + pre-missionary Africa.

### Full Classification

#### Folk/traditional religion (48 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0005-tako | -2953 | Brazil | 0 | |
| 2 | 0021-tomi | -2365 | Mexico | 72 | |
| 3 | 0023-paravi | -5543 | Nepal | 83 | |
| 4 | 0024-mielo | -895 | Russia | 75 | |
| 5 | 0039-ami | -80827 | Ghana | 0 | Paleolithic |
| 6 | 0040-noma | -15773 | China | 17 | Paleolithic |
| 7 | 0046-walwata | -1314 | Turkey | 0 | Bronze Age Anatolia |
| 8 | 0047-hadu | -1834 | Iran | 67 | Pre-Zoroastrian Iran |
| 9 | 0049-kiri | -168146 | Egypt | 0 | Paleolithic |
| 10 | 0060-mori | -3797 | China | 0 | Neolithic |
| 11 | 0069-unnamed-infant | -4134 | Spain | 0 | Neolithic |
| 12 | 0083-loma | -1537 | El Salvador | 0 | Pre-Columbian Central America |
| 13 | 0091-ami | -4987 | Mexico | 0 | |
| 14 | 0101-rani | -6856 | United States | 0 | |
| 15 | 0108-sina | -6302 | Brazil | 1 | |
| 16 | 0109-ami | -5367 | China | 0 | |
| 17 | 0112-sena | -4921 | Myanmar | 60 | Pre-Buddhist SE Asia |
| 18 | 0127-omi | -3554 | Turkey | 1 | |
| 19 | 0130-saya | -1049 | Peru | 45 | Pre-Columbian South America |
| 20 | 0136-mira | -3760 | Mexico | 0 | |
| 21 | 0137-hani | -8696 | Colombia | 50 | |
| 22 | 0143-leni | -1363 | Papua New Guinea | 35 | |
| 23 | 0148-luta | -4329 | Brazil | 71 | Shamanic |
| 24 | 0159-unnamed-infant | -4771 | Nigeria | 0 | |
| 25 | 0168-yonu | -53653 | Ghana | 82 | Paleolithic |
| 26 | 0178-nara | -697 | Hong Kong | 4 | Pre-Chinese-state |
| 27 | 0191-kima | -8720 | Peru | 74 | |
| 28 | 0197-yana | -3204 | Georgia | 37 | |
| 29 | 0198-sira | -1517 | Iran | 1 | Pre-Zoroastrian |
| 30 | 0199-yama | -6805 | China | 38 | |
| 31 | 0200-kira | -2107 | India | 0 | Could also be Vedic/proto-Hindu |
| 32 | 0222-nora | -9452 | Nicaragua | 78 | |
| 33 | 0225-bena | -2345 | China | 0 | |
| 34 | 0228-binu | -33557 | Australia | 64 | Paleolithic |
| 35 | 0231-unnamed-infant | -3000 | Sudan | 0 | |
| 36 | 0232-ekan | -1778 | Slovenia | 3 | Bronze Age Europe |
| 37 | 0237-tari | -3760 | Spain | 0 | |
| 38 | 0240-sana | -60200 | Egypt | 1 | Paleolithic |
| 39 | 0244-mira | -74060 | Sudan | 81 | Paleolithic |
| 40 | 0247-vela | -10409 | Italy | 49 | |
| 41 | 0249-sola | -5006 | Bolivia | 41 | |
| 42 | 0012-kpovi | 800 | Benin | 0 | African traditional |
| 43 | 0041-nathono | 1379 | Mozambique | 53 | African traditional |
| 44 | 0078-sali | 1460 | Ghana | 1 | African traditional |
| 45 | 0102-nari | 311 | Kenya | 68 | African traditional |
| 46 | 0103-nabira | 1729 | DR Congo | 52 | African traditional |
| 47 | 0187-munyaneza | 1818 | Rwanda | 0 | African traditional |
| 48 | 0246-nabale | 1639 | DR Congo | 30 | African traditional |

#### Folk/traditional (shamanic) (5 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0034-temir | 1031 | Mongolia | 6 | Tengrist/shamanic |
| 2 | 0132-caiubi | 921 | Brazil | 0 | Indigenous Brazilian |
| 3 | 0165-veko | 1897 | Russia | 41 | Siberian indigenous |
| 4 | 0174-qori | 990 | China | 0 | Likely non-Han minority |
| 5 | 0239-erdeni | 1606 | China | 51 | Likely Mongolian/Manchu shamanic |
| 6 | 0194-wanyan-helibo | 1188 | China | 20 | Jurchen shamanic |

#### Hindu — undifferentiated / sect unclear (50 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0001-nagamma | 1791 | India | 0 | |
| 2 | 0002-bhima | 975 | India | 29 | |
| 3 | 0007-kandan | 440 | India | 54 | Shaivite elements (Shaiv- in text) |
| 4 | 0008-mallamma | 679 | India | 42 | |
| 5 | 0009-anandi | 1178 | India | 37 | |
| 6 | 0025-poda | 33 | India | 60 | |
| 7 | 0026-unnamed-infant | 1294 | India | 0 | |
| 8 | 0029-murugan | 1985 | India | alive | |
| 9 | 0045-kali | 754 | India | 16 | |
| 10 | 0050-haridasa | 1083 | India | 62 | |
| 11 | 0051-sari | 67 | India | 40 | |
| 12 | 0052-harihar | 1811 | India | 13 | |
| 13 | 0053-moti | 1265 | Nepal | 12 | |
| 14 | 0054-jaya | 1085 | India | 6 | |
| 15 | 0055-asha | 14 | India | 0 | |
| 16 | 0058-timma | 1148 | India | 4 | |
| 17 | 0067-mahalakshmi | 853 | India | 29 | |
| 18 | 0076-venkamma | 1156 | India | 31 | |
| 19 | 0086-sitaram | 1630 | India | 52 | |
| 20 | 0089-soma | 918 | India | 2 | |
| 21 | 0090-peda | 458 | India | 0 | |
| 22 | 0095-chinni | 1654 | India | 0 | |
| 23 | 0096-damodara | 871 | India | 74 | |
| 24 | 0097-ramachandra | 1601 | India | 49 | |
| 25 | 0104-nikhil | 1998 | India | alive | |
| 26 | 0113-nirmala | 1941 | India | 33 | |
| 27 | 0114-ravi | 1980 | India | alive | |
| 28 | 0115-kaushalya | 1966 | India | 3 | |
| 29 | 0128-pini | 1271 | India | 1 | |
| 30 | 0129-mitra | 196 | India | 41 | |
| 31 | 0135-tarabai | 1689 | India | 21 | |
| 32 | 0138-unnamed-infant | 1746 | India | 0 | |
| 33 | 0146-gopayya | 1326 | India | 72 | |
| 34 | 0149-aditya | 2021 | India | alive | |
| 35 | 0164-savitri | 1938 | India | 0 | |
| 36 | 0166-parvati | 629 | India | 16 | |
| 37 | 0172-karna | 815 | India | 28 | Shiva mentioned — possibly Shaivite |
| 38 | 0182-joga | 1901 | India | 40 | |
| 39 | 0183-kusum | 1990 | India | alive | |
| 40 | 0188-durgadeva | 1133 | India | 0 | |
| 41 | 0190-unnamed-infant | 1201 | India | 0 | |
| 42 | 0196-pranavi | 2018 | India | 0 | |
| 43 | 0207-toru | 487 | India | 38 | |
| 44 | 0215-parbati | 1063 | India | 40 | |
| 45 | 0216-pavithra | 2001 | India | alive | |
| 46 | 0218-kusum | 1913 | Bangladesh | 0 | Hindu in Bangladesh |
| 47 | 0226-vina | -233 | India | 31 | |
| 48 | 0241-dharma | 594 | India | 67 | |

Note: Very few stories specify a Hindu sect. Most mention temples, offerings, deities generically. The LLM analysis will need to infer sect from deity mentions, region, and era.

#### Hindu — Vaishnavism (2 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0142-devi | 2003 | India | alive | Krishna mentioned |
| 2 | 0171-sundari | 1497 | India | 54 | Krishna mentioned |

#### Hindu — Vedic / proto-Hindu (6 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0016-chuku | -1931 | India | 40 | |
| 2 | 0018-vasundhara | -786 | India | 24 | Vedic explicitly mentioned |
| 3 | 0065-veli | -1407 | India | 76 | |
| 4 | 0075-pori | -608 | India | 0 | |
| 5 | 0119-gopala | -268 | India | 0 | |
| 6 | 0140-sila | -59 | India | 68 | |
| 7 | 0152-miri | -1690 | India | 5 | |
| 8 | 0154-pilla | -45 | India | 55 | |
| 9 | 0214-pira | -2443 | Bangladesh | 73 | |

#### Chinese folk religion (29 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0000-zhang-wei | 1995 | China | alive | Modern — possibly "no religion" under CCP |
| 2 | 0037-yang-meiying | 1935 | China | 62 | |
| 3 | 0042-alo | -140 | China | 0 | |
| 4 | 0043-ruma | -1071 | China | 31 | Shang dynasty |
| 5 | 0044-baozi | 1845 | China | 1 | |
| 6 | 0068-tali | -349 | China | 17 | |
| 7 | 0072-huan | 211 | China | 0 | |
| 8 | 0074-he-pengfei | 1982 | China | alive | Modern — possibly "no religion" |
| 9 | 0077-ren | -989 | China | 69 | Zhou dynasty |
| 10 | 0080-xie-ping | 1857 | China | 0 | |
| 11 | 0088-nai | 271 | China | 1 | |
| 12 | 0094-lin-xin | 52 | China | 87 | Han dynasty |
| 13 | 0107-guang | 358 | China | 0 | |
| 14 | 0111-li-shi | 1125 | China | 64 | Song dynasty — monk mentioned, could be Buddhist |
| 15 | 0118-zhao-shun | 143 | China | 49 | |
| 16 | 0126-kanu | -1497 | China | 3 | Shang dynasty |
| 17 | 0134-tari | -1392 | China | 7 | |
| 18 | 0144-yin-niang | 1263 | China | 0 | |
| 19 | 0157-zhang-jincai | 1735 | China | 2 | |
| 20 | 0161-zeng-jinfang | 1779 | China | 55 | |
| 21 | 0179-bao | 1264 | China | 72 | |
| 22 | 0180-zi | -1432 | China | 1 | Shang dynasty |
| 23 | 0195-zhi | -493 | China | 55 | |
| 24 | 0219-unnamed-infant | 1041 | China | 0 | |
| 25 | 0223-gang | 381 | China | 24 | |
| 26 | 0227-unnamed-infant | 1602 | China | 0 | |

#### Chinese folk religion with Taoist elements (4 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0106-xiong-gui | 1431 | China | 0 | Daoist explicitly |
| 2 | 0150-zhao-yong | 1638 | China | 8 | Daoist explicitly |
| 3 | 0162-luo-fugen | 1808 | China | 54 | Daoist explicitly |
| 4 | 0217-wu-changsheng | 1798 | China | 57 | Daoist explicitly |

#### Mahayana Buddhism (5 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0017-unnamed-infant | 525 | China | 0 | Buddha/Buddhist in text |
| 2 | 0022-chikako | 1046 | Japan | 57 | Buddhist, with Shinto/kami elements |
| 3 | 0028-peldzom | 1034 | China | 21 | Tibetan area — could be Vajrayana |
| 4 | 0071-he-gui | 224 | China | 50 | Buddhist monk |
| 5 | 0156-otsuru | 1654 | Japan | 86 | Buddhist |
| 6 | 0220-otsugi | 1565 | Japan | 2 | Buddhist |

#### Theravada Buddhism (4 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0019-sovan | 302 | Myanmar | 0 | Inferred from place/time |
| 2 | 0084-hani | 139 | Cambodia | 33 | Inferred — but 139 AD Cambodia might be Hindu |
| 3 | 0170-thushari | 1984 | Sri Lanka | alive | Buddha/temple explicit |
| 4 | 0212-thida | 1773 | Myanmar | 60 | Inferred |
| 5 | 0235-khamla | 1867 | Thailand | 1 | Inferred |

Note: 0084-hani (Cambodia, 139 AD) is debatable — Funan-era Cambodia was Hindu-influenced, not yet Theravada.

#### Early Buddhism (2 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0013-nathu | 340 | India | 3 | Buddhist/monk in text |
| 2 | 0092-velan | -399 | India | 0 | Buddhist in text |

#### Sunni Islam (20 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0020-hind | 1201 | Egypt | 0 | Mecca/prayer in text |
| 2 | 0048-salma | 1968 | India | alive | Sunni explicit |
| 3 | 0056-serife | 1951 | Turkey | 29 | Sunni explicit |
| 4 | 0057-yusuf | 1880 | Ethiopia | 3 | Muslim explicit |
| 5 | 0064-abdul-rahman | 1907 | India | 29 | Muslim explicit |
| 6 | 0073-hauwa | 1996 | Nigeria | alive | Sunni explicit |
| 7 | 0085-jamila | 1483 | Syria | 0 | Sunni explicit |
| 8 | 0093-muhammad-akbar | 1910 | Pakistan | 71 | Sunni explicit |
| 9 | 0110-hafsa | 1394 | Turkey | 0 | Sunni explicit |
| 10 | 0116-fazal-karim | 1934 | Pakistan | 75 | Sunni explicit |
| 11 | 0122-ali | 1676 | Sudan | 1 | Muslim explicit |
| 12 | 0160-ismail | 1268 | Azerbaijan | 0 | Muslim, mosque |
| 13 | 0177-madhav | 1337 | India | 0 | Muslim mentioned (in Hindu-Muslim context) |
| 14 | 0184-khadija | 2023 | Algeria | alive | Sunni explicit |
| 15 | 0192-shahzad | 2018 | Pakistan | alive | Mosque/prayer |
| 16 | 0201-nasreen | 1973 | Pakistan | alive | Sunni explicit |
| 17 | 0202-emir | 2024 | Turkey | alive | Sunni explicit |
| 18 | 0224-salma | 1349 | Pakistan | 2 | Inferred |
| 19 | 0229-hasan | 1199 | Spain | 1 | Muslim in Al-Andalus |
| 20 | 0236-nasser | 1600 | Saudi Arabia | 64 | Sunni explicit |
| 21 | 0242-mahammad | 1828 | Azerbaijan | 30 | Muslim explicit |
| 22 | 0245-sastra | 1572 | Indonesia | 26 | Muslim explicit |

Note: No Shia Muslims in this sample — no Iranian in the right time period.

#### Catholic (17 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0003-mercedes | 1857 | Peru | 39 | Catholic explicit |
| 2 | 0059-elisabet | 1198 | Germany | 0 | Church/mass/priest |
| 3 | 0063-felipe | 1737 | Mexico | 0 | Catholic explicit |
| 4 | 0079-santiago | 1938 | Mexico | 0 | Catholic explicit |
| 5 | 0105-frances-mary | 1911 | United States | 63 | Catholic explicit |
| 6 | 0123-petrus | 1310 | Estonia | 20 | Church/baptism — Teutonic Order era |
| 7 | 0125-unnamed-infant | 1315 | Czechia | 0 | Catholic explicit |
| 8 | 0145-arthur-bernard-keegan | 1914 | UK | 86 | Catholic explicit |
| 9 | 0153-angele-hounsa | 1955 | Benin | alive | Catholic explicit |
| 10 | 0169-gautier | 869 | France | 0 | Church/Christian — Carolingian |
| 11 | 0181-sifrid | 1361 | Germany | 0 | Church/baptism |
| 12 | 0193-aude | 1231 | France | 76 | Church/mass/priest |
| 13 | 0204-marie-jeanne | 1740 | France | 80 | Church/mass — "baptist" is a false positive (baptism) |
| 14 | 0208-maria-guadalupe | 1933 | Mexico | 58 | Catholic explicit |
| 15 | 0221-julia | 1997 | Angola | alive | Church — likely Catholic (Angola) |

#### Eastern Orthodox (10 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0006-nadiia | 1920 | Ukraine | 4 | Church/Christ/prayer |
| 2 | 0033-mikhail | 1862 | Russia | 50 | Orthodox explicit |
| 3 | 0038-tana | 1349 | Russia | 77 | Orthodox explicit |
| 4 | 0185-aleksey | 1897 | Russia | 47 | Orthodox explicit |
| 5 | 0206-michael | 1357 | Turkey | 7 | Orthodox explicit — Byzantine |
| 6 | 0209-zoe | 998 | Turkey | 77 | Church — Byzantine (pre-schism, classified Orthodox) |
| 7 | 0210-dimitri | 780 | Turkey | 38 | Church — Byzantine (pre-schism, classified Orthodox) |
| 8 | 0211-nikolaos | 559 | Turkey | 65 | Church — Byzantine (pre-schism, classified Orthodox) |
| 9 | 0213-darya | 1872 | Ukraine | 85 | Church — Ukrainian |


Note: 0243-surana (Russia, 505 AD) reclassified — she is Sarmatian/Alan with Christian-influenced practice through Caucasus trade contacts, not Russian Orthodox. Moved to folk/traditional below. 0036-vladislav (Serbia, 665) is correctly Slavic folk religion in narrative (listed under "Cases Needing Review" for reclassification).

#### Protestant (4 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0099-fabio-henrique | 1983 | Brazil | alive | Bible/church — likely evangelical |
| 2 | 0120-david-antonio | 2023 | Angola | alive | Protestant explicit |
| 3 | 0175-akwele | 1958 | Ghana | alive | Bible/church |

#### Early Christianity (1 person)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0035-tatia | 307 | Spain | 58 | Priest/offering — Roman Spain, early Christian period |

#### Greco-Roman polytheism (3 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0011-pleuron | -595 | Croatia | 76 | Ritual/sacrifice/offering |
| 2 | 0027-pachompsais | -42 | Egypt | 50 | Ptolemaic Egypt — Greco-Egyptian |
| 3 | 0117-tiberius | 196 | Austria | 19 | Roman Empire |

#### Egyptian polytheism (1 person)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0121-tjety | -1644 | Egypt | 1 | |

#### Mesopotamian polytheism (3 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0014-hadiya | -747 | Syria | 73 | |
| 2 | 0061-shibtu | -1333 | Lebanon | 29 | |
| 3 | 0155-ben-hadad | -748 | Syria | 80 | |

#### Mesoamerican polytheism (3 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0151-ollin | 1192 | Mexico | 40 | Pre-Columbian |
| 2 | 0186-unnamed-infant | 1432 | Mexico | 0 | Pre-Columbian |
| 3 | 0230-beni | 989 | Mexico | 2 | Pre-Columbian |

#### Jainism (1 person)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0087-hari | 502 | India | 35 | Jain/dharma explicit |

#### Judaism (1 person)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0233-rokhl | 1910 | United States | 0 | Jewish/Torah explicit |

#### Sikhism (1 person)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0100-harcharan | 1945 | India | alive | Sikh/Gurdwara explicit |

#### Zoroastrianism (1 person)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0147-huta | -200 | Afghanistan | 2 | Ahura Mazda explicit |

#### Shinto / Japanese folk (3 people)

| # | File | Year | Country | Age | Notes |
|---|------|------|---------|-----|-------|
| 1 | 0070-hachiromaru | 1330 | Japan | 6 | Kami/monk — Shinto-Buddhist mix |

#### Cases Needing Review

| # | File | Year | Country | Age | Issue |
|---|------|------|---------|-----|-------|
| 1 | 0004-koitale | 1669 | Tanzania | 23 | Pre-colonial East Africa — folk/traditional most likely |
| 2 | 0015-hormizd | 361 | Afghanistan | 3 | Named Hormizd — Zoroastrian? Church of the East? |
| 3 | 0031-eirene | -4 | Turkey | 1 | Roman Turkey — Greco-Roman polytheism |
| 4 | 0036-vladislav | 665 | Serbia | 0 | RESOLVED: Narrative correctly shows Slavic folk religion → move to folk/traditional |
| 5 | 0066-tazri | 31 | Morocco | 10 | Roman North Africa — Berber/Roman religion |
| 6 | 0082-tari | 933 | Brazil | 4 | Indigenous — folk/traditional |
| 7 | 0084-hani | 139 | Cambodia | 33 | Funan era — Hindu or animist, not yet Theravada |
| 8 | 0098-tablut | 102 | Iraq | 38 | Parthian-era Mesopotamia — polytheist or early Mandaean? |
| 9 | 0124-bald | 453 | Denmark | 2 | RESOLVED: Narrative correctly shows Germanic paganism → move to folk/traditional |
| 10 | 0131-kalis | -375 | Turkey | 22 | Hellenistic Anatolia — Greco-Roman polytheism |
| 11 | 0133-phuntsok | 1868 | China | 1 | Tibetan area — Vajrayana Buddhism |
| 12 | 0139-sin-uballit | -489 | Iraq | 0 | Neo-Babylonian — Mesopotamian polytheism |
| 13 | 0158-mara | 584 | Brazil | 68 | Indigenous — folk/traditional |
| 14 | 0163-rahma | 2016 | Tanzania | alive | Islam mentioned in text — Sunni Muslim |
| 15 | 0167-iorwase | 1840 | Nigeria | 81 | Tiv people — folk/traditional |
| 16 | 0189-sena | 327 | Pakistan | 2 | Gandhara — could be Hindu, Buddhist, or Zoroastrian |
| 17 | 0205-tara | 1392 | Bangladesh | 0 | Medieval Bengal — Hindu or Muslim? |
| 18 | 0234-tama | 1376 | Chad | 14 | Kanem-Bornu — Muslim or traditional |
| 19 | 0243-surana | 505 | Russia | 2 | RESOLVED: She is Sarmatian/Alan with Christian-influenced folk practice via Caucasus contacts — classify as folk/traditional with Christian influence |
| 20 | 0248-hsiao-hsiu-chen | 1972 | Taiwan | alive | Church mentioned — Christian (denom unclear), but majority of Taiwanese are folk religion |

---

## Observations from Classification Exercise

### What worked well
1. **Time + place is highly predictive**: For most people post-500 BCE, country + era determines religion with high confidence.
2. **Keyword extraction from narratives confirms the classification**: Stories that mention mosques, churches, temples, specific deities, etc. are consistent with time/place inference.
3. **Chinese folk religion as default works**: Almost all Chinese people end up here, with only a few having explicit Buddhist or Taoist identity.

### Category issues discovered
1. **Hindu sect classification is very hard**: Only 2 out of 56 Hindus got a specific sect from the narrative text. The narratives mention deities and temples but rarely specify sectarian identity. An LLM-based approach will need to infer from deity, region, and era.
2. **Pre-Christianization Europe**: On closer inspection, all three flagged stories (0124-bald Denmark 453, 0243-surana Russia 505, 0036-vladislav Serbia 665) are actually correct — Bald and Vladislav have pagan/folk religion in their narratives, and Surana's Christian-influenced elements are historically defensible for an Alan group with Caucasus trade contacts. The initial classification was wrong, not the narratives.
3. **"No religion" never appears**: None of the 250 stories describe someone as non-religious, even modern Chinese people under CCP. This category will only matter for post-1900 data.
4. **Mesoamerican polytheism is a real category**: 3 pre-Columbian Mexicans needed it. Should also include Andean religion (Inca, pre-Inca).
5. **Shia Islam gap**: Zero Shia Muslims in sample despite Iran's large population. This is sampling noise — need to ensure methodology captures this.
6. **Cambodia 139 AD**: Classified as Theravada but this is anachronistic. Funan-era Cambodia was Hindu-influenced. Theravada didn't arrive until ~13th century.
7. **Modern Chinese "no religion"**: Zhang Wei (1995, China) and He Pengfei (1982, China) are classified as "Chinese folk religion" but under PRC they might report "no religion" in surveys.

### Proportions preview (very rough, n=250)
If we aggregate to top-level categories:
- **Hinduism**: ~22% — largest single religion across all history
- **Folk/traditional**: ~21% — the default for pre-history and pre-missionary contact
- **Chinese folk religion**: ~12% — reflects China's population
- **Islam (Sunni)**: ~8%
- **Christianity (all)**: ~13% (Catholic 7%, Orthodox 4%, Protestant 2%)
- **Buddhism (all)**: ~5%
- **Ancient polytheisms**: ~3%
- **Other named**: ~2%

These proportions will shift with proper weighting, but the overall picture — Hinduism and folk/traditional as the two largest categories, with Islam and Christianity behind — is probably directionally correct.

---

## Methodology Plan

### Approach 1: Modern data (1900–present)
Use published Pew/WRD data for country-level religious composition by decade, weighted by births per country.

### Approach 2: Historical LLM estimation (500 BCE – 1900)
Adapt the FamousPerson stratified sampling methodology:
- Sample people using person.py
- LLM assigns probability distribution over applicable religions
- Stratified estimation with Neyman allocation

### Approach 3: Pre-500 BCE
Deterministic: all folk/traditional, with carve-outs for Egyptian, Mesopotamian, Vedic, early Judaism.

See `generating_code/Religion/` for implementation code.
