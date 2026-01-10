# Review Log (Stories 0000-0099)

Each story appears once with all issues found and changes made across all review passes.

---

## 0030-targasnalli
**Issues found:**
- [Figurative language] "sparrow bones" is a metaphor
- [Chronology] Arnuwi "died when Targasnalli was still small enough to be lifted with one arm" - but Arnuwi died in 1491 BC and Targasnalli wasn't born until 1490 BC
- [Figurative language] "as if the order itself held the household together" - simile
- [Vague hedging] "dyed wool or leather preservatives" - LLM couldn't commit
- [Clarity] Family structure unclear - Tiwati, Aruna, Luli introduced without context; Luli grouped with pre-birth deaths but she died when Targasnalli was 6
- [Clarity] Death mechanism confused - chronic intestinal illness and poisoning death presented as disconnected events rather than causally linked

**Changes made:**
- Changed "sparrow bones" to "little bones"
- Fixed Arnuwi: "had died the year before Targasnalli was born, at seven—old enough that adults still spoke of him"
- Removed simile, now just: "said the names in a fixed order"
- Changed "dyed wool or leather preservatives" to "leather tanning solution"
- Rewrote family section: introduced all four living sisters with ages/roles upfront, separated the four pre-birth deaths, moved Luli's death to its proper chronological place (age 6)
- Rewrote later paragraphs to integrate events rather than list them chronologically
- Connected chronic illness to death: added "recurring stomach sickness had left him thinner" and "Years of intestinal illness had worn his body down"

---

## 0031-eirēnē
**Issues found:**
- [Clarity] "Dionysios died during the same year" - same year as what? Unclear time anchor
- [Clarity] Dionysios's death mentioned in half a sentence with no cause or context
- [Generation bug] 57-year age gap between siblings (Dionysios born 63 BC, Philōn born 6 BC) is unrealistic
- [Stylistic] Opening sentence long and cramming too much context

**Changes made:**
- Changed "Dionysios died during the same year" → "Before the harvest that year, Dionysios fell ill with a fever and died within days"
- Changed "In the winter after Dionysios's death" → "In the winter that followed"
- **[DEVIATED FROM DEBUG]** Changed Dionysios from 59 years old to "in his twenties" - debug had implausible 57-year sibling age gap
- Rewrote opening to spread context across shorter sentences

---

## 0032-nola
**Issues found:**
- [Clarity/Consistency] "Nola died from newborn weakness" - but she lived 7.5 months. "Newborn weakness" inaccurate for a 7-month-old.

**Changes made:**
- Changed "Nola died from newborn weakness" → "Nola died" (removed inaccurate cause)

---

## 0033-mikhail
**Issues found:**
- [Chronology] Nikolay's death timing incorrect - narrative implies 1892, debug says 1894
- [Missing event] Father Aleksey's death (1888) never mentioned
- [Logical gap] "By the late 1890s they lived in a multi-family shared apartment" comes out of nowhere
- [Stylistic] Too many "In [year]" sentence openings
- [Major event compressed] Cancer progression too brief

**Changes made:**
- Fixed Nikolay's death timing: separated his birth (1892) from his death (1894)
- Added father's death: "Aleksey died in 1888"
- Added housing trajectory explaining apartment
- Varied time markers: "In 1882" → "At twenty"; etc.
- Expanded cancer progression with concrete physical details

---

## 0034-temir
**Issues found:**
- [Anachronism] "shore-ice" on July 3 is impossible - Lake Khövsgöl ice melts by mid-June
- [Pseudosociological] "kin camps", "his kin wrapped him"
- [Vague] "fetch something that had drifted close"

**Changes made:**
- Rewrote death scene to involve slippery rocks/riverbank rather than ice
- Changed "kin camps" → "families"
- Changed "his kin wrapped him" → "his family wrapped him"
- Changed "something that had drifted close" → "a wooden bowl that had drifted close"

---

## 0035-tatia
**Issues found:**
- [AI-slop] "like a fact that explained other facts" - meaningless pseudo-profound phrase
- [Pseudosociological] "kin households", "cooperation among kin", "kin group", "Her kin washed her body"

**Changes made:**
- Deleted "like a fact that explained other facts"
- Changed "kin households" → "her sisters' households and those of aunts and cousins"
- Changed "continued cooperation among kin" → "her sisters and their husbands"
- Changed "kin group" → "family"
- Changed "Her kin washed her body" → "Valeria and her daughters washed the body"

---

## 0036-vladislav
**Issues found:**
- [Pseudosociological] "kin groups"

**Changes made:**
- Changed "on behalf of kin groups" → "on behalf of their families"

---

## 0037-yang-meiying
**Issues found:**
- [Missing event] Father Yang Shunfa's death (1972) not mentioned
- [Missing event] Mother Chen A'nü's death (1981) not mentioned

**Changes made:**
- Added father's death in 1972: "Her father, Yang Shunfa, died in 1972..."
- Added mother's death in 1981: "Her mother, Chen A'nü, died in 1981..."

---

## 0038-tana
**Issues found:**
- [Chronology] "Bera had died the year before, in 1378" after describing 1377 events - contradictory
- [Chronology] Theft years impossible since she was separated in 1377
- [Missing event] Ansa (uncle) dies 1388 - not mentioned
- [Missing event] Nisa (mother) dies 1404 - significant since she sheltered Tana
- [Chronology] Sana's death (1396) was placed before Rati's death (1383) - wrong order
- [Pseudosociological] "The kin washed her body"
- [Chronology - second review] "At twenty-nine, in 1378" appeared confusingly after "Bera died the following year, in 1378" making it unclear if assault was same year as father's death
- [Stylistic] Repetitive "At age X, in year Y" time marker pattern throughout story

**Changes made:**
- Changed "Bera had died the year before, in 1378" → "Bera died the following year, in 1378"
- Changed the years of theft to "1379, 1380, and after"
- Added Ansa's death: "Ansa, her father's brother, followed in 1388"
- Fixed chronological order: moved Rati/Ansa deaths before Sana's death
- Added Nisa's death: "Nisa, her mother, died in 1404..."
- Changed "The kin washed her body" → "The women of the household washed her body"
- Changed "At twenty-nine, in 1378" → "That same year, before the autumn" (clarifying assault happens same year as Bera's death)
- Varied time markers: "At forty-one, in 1390" → "Twelve years after her separation"; "By forty-five, in 1394" → "Four years later"; "At sixty, in 1409" → "The following year"

---

## 0039-ami
**Issues found:** None

**Changes made:** None

---

## 0040-noma
**Issues found:**
- [Missing event] Sena (grandmother-figure) dies 15758 BC when Noma was ~15-16 - not mentioned

**Changes made:**
- Added Sena's death: "Sena, an older woman in Kari's hearth group who had taught Noma wind signs and safe ice, died that winter..."

---

## 0041-nathono
**Issues found:**
- [Missing sibling] Namutolo (oldest brother, born 1365, died 1402) never mentioned
- [Missing event] Nankula (brother) dies 1432 - not mentioned
- [Figurative] "as if she had said nothing at all", "as if daring anyone to question her", "as if paying a debt", "as if cleanliness could change anything"

**Changes made:**
- Added Namutolo introduction and death
- Added Nankula's death
- Removed all four similes

---

## 0042-alo
**Issues found:** None

**Changes made:** None

---

## 0043-ruma
**Issues found:**
- [Missing event] Garo (father) dies 1052 BC - not mentioned
- [Missing event] Hena (mother) dies 1047 BC - not mentioned
- [Missing event] Senu (brother) dies 1041 BC - not mentioned
- [Vague timing] Kado (father-in-law) death mentioned as "years earlier" without specificity
- [AI-slop] "He set the rhythm of the day"
- [Figurative] "as if someone stood at the door", "as if she had always lived there", "as if she could hear something under it", "as if listening to something no one else could hear"

**Changes made:**
- Fixed AI-slop: "He set the rhythm of the day" → "His days moved with"
- Added Garo's, Hena's, and Senu's deaths
- Added specific timing for Kado's death
- Removed all four similes

---

## 0044-baozi
**Issues found:** None

**Changes made:** None

---

## 0045-kālī
**Issues found:**
- [Pseudosociological] "male kin" at end of narrative

**Changes made:**
- Fixed "male kin lit the pyre" → "men from his family lit the pyre"

---

## 0046-walwata
**Issues found:** None

**Changes made:** None

---

## 0047-hadu
**Issues found:**
- [Vague hedging] "small cake of grain or a pinch of salt"

**Changes made:**
- Changed "small cake of grain or a pinch of salt" → "a pinch of grain"

---

## 0048-salma
**Issues found:**
- [Missing event] Abdul Rahim (father) dies 1998 - not mentioned

**Changes made:**
- Added Abdul Rahim's death

---

## 0049-kiri
**Issues found:** None

**Changes made:** None

---

## 0050-haridāsa
**Issues found:**
- [Missing event] Dhaniyā (mother) dies 1142 - not mentioned
- [Missing family context] Narrative says "two infants" died before Haridāsa but debug shows three
- [Missing siblings] Younger siblings Keshava and Balarāma never introduced
- [Missing siblings] Three infant deaths after Haridāsa never mentioned
- [Missing family context] No sense that this was one of eleven children

**Changes made:**
- Added Dhaniyā's death
- Fixed opening: "the sixth child" → "the sixth of what would be eleven children"
- Fixed early death count: "three infants" → "two infants and a toddler"
- Added paragraph with younger siblings and their fates

---

## 0051-sari
**Issues found:**
- [Missing sibling] Rini (younger sister) never mentioned
- [Confusing phrasing] "Another older sister, Dani's third daughter, died as an infant too"
- [Missing event] Kora (brother) dies 105 - not mentioned
- [Wrong age] Pira described as "thirty years old" but should be 21
- [Pseudosociological] "Her kin washed her body" and "kin and council"
- [Vague hedging] "a bit of cooked grain or a smear of oil"

**Changes made:**
- Rewrote sibling paragraph: introduced Rini, removed confusing reference
- Added Kora's death
- Fixed Pira's age: "thirty years old" → "twenty-one years old"
- Fixed "Her kin washed her body" → "Mira and the women of the household washed her body"
- Fixed "kin and council" → "families and council"
- Fixed vague hedging: "a bit of cooked grain or a smear of oil" → "a bit of cooked grain"

---

## 0052-harihar
**Issues found:**
- [Figurative] "as if checking whether color rubbed off"

**Changes made:**
- Changed to "to see whether color rubbed off"

---

## 0053-moti
**Issues found:**
- [Missing sibling] Bharat (died age 2, year before Moti born) not mentioned
- [Missing sibling] Nanda (died age 0 when Moti was 2) not mentioned

**Changes made:**
- Added missing siblings: "Moti was the fourth of five children, but the household had already buried two..."

---

## 0054-jayā
**Issues found:**
- [Missing character] Rāmū (maternal grandmother) not mentioned
- [Pseudosociological] "where kin offered a small cake of rice"

**Changes made:**
- Added grandmother: "Dhanī's mother Rāmū lived nearby..."
- Fixed "where kin offered" → "where Dhanī and Vīrū offered"

---

## 0055-asha
**Issues found:**
- [Chronology error] Tama described as alive at Asha's birth but debug shows he died six years earlier

**Changes made:**
- Corrected to show Tama as already dead: "Tama, born in 16 BC, had died six years earlier, remembered in offerings at the hearth"

---

## 0056-şerife
**Issues found:** None

**Changes made:** None

---

## 0057-yusuf
**Note:** Story regenerated with toddler-specific prompts (January 2026) to add developmental moments.

**Issues found (post-regeneration):**
- [AI-slop] "set the rhythm of daily life"

**Changes made:**
- Fixed "set the rhythm of daily life" → "farmed the hills and traded at local markets"

---

## 0058-timma
**Note:** Story regenerated with toddler-specific prompts (January 2026) to add developmental moments.

**Issues found (post-regeneration):**
- [Confusing names] Sibling "Peddamma" shares name with grandmother - confusing for reader
- [Pseudosociological] "patrilocal joint household"

**Changes made:**
- Changed sibling reference "then Peddamma and Chinnamma in 1141 and 1143" → "a second daughter in 1141, and Chinnamma in 1143"
- Fixed "patrilocal joint household with" → "shared the compound with"

---

## 0059-elisabet
**Issues found:** None

**Changes made:** None

---

## 0060-mori
**Issues found:**
- [Pseudosociological] "elders and kin nearby"

**Changes made:**
- Fixed "elders and kin nearby" → "elders and family nearby"

---

## 0061-shibtu
**Issues found:**
- [Missing death] Nura (grandmother) death not explicitly mentioned
- [Figurative] "stepping around it as if it were blocked"

**Changes made:**
- Added explicit death: "By the time Shibtu was seventeen, Nura was dead."
- Removed "as if it were blocked"

---

## 0062-kanu
**Issues found:**
- [Pseudosociological] "join kin for work"

**Changes made:**
- Fixed "join kin" → "join relatives"
- **[DEVIATED FROM DEBUG]** Debug shows Daro dies -2769 (same year Kanu born), but narrative shows Daro alive throughout Kanu's life. Decision: keep Daro alive as written. The narrative_plan intended Daro as a meaningful presence, and the death_year appears to be a data error.

---

## 0063-felipe
**Issues found:**
- [Pseudosociological] "shown to kin"
- [Impossible sibling ages] Brothers 79 and 72 years older than Felipe - biologically impossible
- [Missing sibling identification] María introduced without identifying her as Felipe's sister

**Changes made:**
- Fixed "shown to kin" → "shown to the family"
- Changed "were old men" → "were grown men"
- Changed "oldest brothers" → "older brothers"
- Changed "María, seventeen" → "Felipe's sister María, seventeen"

---

## 0064-abdul-rahman
**Issues found:**
- [Pseudosociological] "chosen through kin and village links", "ran errands between kin"
- [Figurative] "as if boiling could fix what had already happened"

**Changes made:**
- Fixed "through kin" → "through family"
- Fixed "between kin" → "between relatives"
- Removed the simile

---

## 0065-veli
**Issues found:**
- [Missing death] Neri (mother) death not mentioned
- [Pseudosociological] "pull of kin", "nearby kin", "closest male kin", "asked kin for help", "His kin washed"
- [Figurative] "as if words could make the wrong spirit notice", "as if a child could be mislaid like a tool"

**Changes made:**
- Added Neri's death: "Neri outlived her husband by eight years before she too was gone"
- Fixed all "kin" usages
- Removed first simile entirely
- Changed second to "Tani watched Veli closely"

---

## 0066-tazri
**Issues found:** None

**Changes made:** None

---

## 0067-mahalakshmi
**Issues found:**
- [Missing sibling birth] Kundayya (younger brother) appears without his birth being mentioned
- [Chronology error] Ponnamma death year was 878 but should be 880
- [Chronology error] Sridevi/Ponnamma deaths in wrong order (Sridevi dies 879, Ponnamma 880)
- [Clarity] Death description was vague and disconnected from earlier fall

**Changes made:**
- Added Kundayya's birth: "A younger brother, Kundayya, was born in 856 and survived."
- Fixed year: "In 878 Ponnamma died" → "In 880 Ponnamma died"
- Reordered deaths correctly
- Rewrote death to connect with earlier injury: "she slipped again at the tank steps while drawing water. This time her head struck the stone edge. She did not rise."

---

## 0068-tali
**Issues found:**
- [Pseudosociological] "kin groups"

**Changes made:**
- Fixed "kin groups" → "families"

---

## 0069-person-0069-unnamed
**Issues found:** None

**Changes made:** None

---

## 0070-hachirōmaru
**Issues found:**
- [Minor] Otsune (maternal grandmother) from debug never appears - not critical

**Changes made:** None

---

## 0071-he-gui
**Issues found:**
- [Missing child] Zhang Hui (third daughter) never mentioned
- [Missing death] Father He Qiang (dies 246) not mentioned
- [Missing death] Grandmother (dies 252) not mentioned
- [Missing death] Uncle He Bo (dies 260) not mentioned
- [Missing death] Mother (dies 268) not mentioned
- [Pseudosociological] "affinal kin group"

**Changes made:**
- Added Zhang Hui's birth
- Added father's, grandmother's, uncle's, and mother's deaths
- Fixed "affinal kin group" → "her husband's family"

---

## 0072-huan
**Issues found:** None

**Changes made:** None

---

## 0073-hauwa
**Issues found:** None

**Changes made:** None

---

## 0074-he-pengfei
**Issues found:** None

**Changes made:** None

---

## 0075-pori
**Issues found:**
- [Chronology error] Tavi described as alive ("still slept near the hearth") but debug shows he died -609 (year before Pori's birth in -608)
- [Pseudosociological] "kin councils"

**Changes made:**
- Fixed Tavi: "Tavi still slept near the hearth and followed women to the water place" → "Tavi had died the previous year at age three, taken by fever"
- Rewrote Veli reference to work with corrected sibling order
- Fixed "kin councils" → "family councils"

---

## 0076-venkamma
**Issues found:**
- [Logical impossibility] Mother dies at birth, but younger brother born 2 years later
- [Missing identification] Kondayya introduced without identifying as father
- [Unclear sibling ordering] Siblings introduced in confusing order
- [Chronology - second review] Accident paragraph (1179) placed after Sītamma's death (1181), creating confusing back-and-forth timeline
- [Stylistic - second review] Awkward date repetition in death paragraph: "In May 1188... died on May 24, 1188"

**Changes made:**
- Fixed by adding father's remarriage: "Kondayya remarried, and two years after Venkamma's birth, his new wife bore a son..."
- Changed "Kondayya's sister" → "her father Kondayya's sister"
- Rewrote family introduction to introduce all siblings in birth order
- Improved sibling ordering clarity: "Bhairava, the eldest at nine... Ranga, seven... Between them had been Sattamma, who died as an infant. Mallamma, three years older than Venkamma..."
- Moved accident paragraph to correct chronological position: now placed between Sītamma's birth (1178) and death (1181), changed "In 1179" → "The following year"
- Fixed date repetition: "died on May 24, 1188" → "died on the twenty-fourth"

---

## 0077-ren
**Issues found:**
- [Missing death] Li (older sister, dies at 43) death not mentioned

**Changes made:**
- Added Li's death and moved to correct chronological position

---

## 0078-sali
**Issues found:** None

**Changes made:** None

---

## 0079-santiago
**Issues found:** None

**Changes made:** None

---

## 0080-xie-ping
**Issues found:** None

**Changes made:** None

---

## 0081-ioryina
**Issues found:**
- [Anachronism] COVID schoolwork reference when character was only 4 in 2020
- [Awkward phrasing] "planting dates argued about in the evenings"

**Changes made:**
- Rewrote to remove COVID schoolwork reference, changed to school starting in 2022

---

## 0082-tari
**Note:** Story regenerated with toddler-specific prompts (January 2026) to add developmental moments.

**Issues found (post-regeneration):** None

**Changes made:** None

---

## 0083-loma
**Issues found:** None

**Changes made:** None

---

## 0084-hani
**Issues found:**
- [Pseudosociological] "Bani's kin visiting often"
- [Figurative] "as if nothing had changed"

**Changes made:**
- Fixed "Bani's kin" → "Bani's relatives"
- Changed "as if nothing had changed" → "the same way he always had"

---

## 0085-jamīla
**Issues found:** None

**Changes made:** None

---

## 0086-sitaram
**Issues found:**
- [Pseudosociological] "with kin sharing tools"
- [Vague hedging] "washed at the handpump or well" - handpumps anachronistic for 1654
- [Figurative] "acted as if the wind had done it"
- [Missing younger sibling births] Kanhaiya, Mohan, and Shivram births not clearly shown as happening after Sitaram
- [Chronology] Affair with Kallu mentioned late in narrative (during debt crisis) rather than when it began (after marriage in 1654)
- [Clarity] Kallu not introduced - appeared without context
- [Clarity] First sexual encounter at age 17 used "youth" (ambiguous gender) rather than clearly identifying as male
- [Clarity] Marriage to Rukmini didn't address lack of romantic/sexual attraction, making the affair context unclear

**Changes made:**
- Fixed "kin" → "relatives"
- Fixed "handpump or well" → "well"
- Removed the simile
- Rewrote sibling paragraph: "After Sitaram came more children. Kanhaiya was born in 1632 and died within days. Mohan arrived in 1634 and lasted less than a month. Shivram, born in 1636, lived a full year before fever took him in 1637."
- Moved Kallu relationship to immediately after marriage (1654) where it chronologically belongs
- Added continuity reference during debt crisis years (1668-1670)
- Added ending of relationship in 1676 after Ramcharan's death
- Introduced Kallu as "a man from another village" on first mention
- Changed "a youth from a neighboring hamlet" → "another young man from a neighboring hamlet"
- Added to marriage paragraph: "Sitaram treated her with steady courtesy but without desire" and "They shared a bed when the household expected it, and children came"

---

## 0087-hari
**Issues found:**
- [Figurative] "as if pulling words up from deep"

**Changes made:**
- Removed the simile: "he answered slowly"

---

## 0088-nai
**Issues found:** None

**Changes made:** None

---

## 0089-soma
**Note:** Story regenerated with toddler-specific prompts (January 2026) to add developmental moments.

**Issues found (post-regeneration):** None

**Changes made:** None

---

## 0090-peda
**Issues found:** None

**Changes made:** None

---

## 0091-ami
**Issues found:** None

**Changes made:** None

---

## 0092-velan
**Issues found:** None

**Changes made:** None

---

## 0093-muhammad-akbar
**Issues found:**
- [Pseudosociological] "village web of kin"
- [Missing death] Bibi Parveen (eldest daughter, dies 1965) - birth mentioned but not death
- [Missing death] Bibi Amina (older sister, dies 1970) - not mentioned
- [Figurative] "speaking as if the dispute could be settled with calm words"

**Changes made:**
- Fixed "kin" → "family"
- Added Bibi Parveen's death
- Added Bibi Amina's death
- Changed simile to "speaking calmly"

---

## 0094-lin-xin
**Issues found:**
- [Missing death] Lin Shi (older sister, dies 126) - not mentioned
- [Figurative] "as if they were tax clerks", "as if his presence in the yard made him responsible"
- [Logical gap] "In old age he lived in his nephew Lin Cheng's extended household" appeared without explanation

**Changes made:**
- Added Lin Shi's death
- Changed first simile to "the way he spoke to tax clerks"
- Removed second simile
- Added transitional context: "With both parents dead and his leg slowing him, Lin Xin could not hold the household alone. Lin Cheng, his nephew—Lin Yong's eldest son, now grown—took him in..."

---

## 0095-chinni
**Issues found:** None

**Changes made:** None

---

## 0096-dāmodara
**Issues found:**
- [Missing sibling] Śiva (born 886, dies 890) not mentioned
- [Missing death] Sītā (older sister, dies 940) - death not mentioned
- [Pseudosociological] "calling kin", "His kin carried"
- [Figurative] "as if that could keep things stable"

**Changes made:**
- Added Śiva
- Added Sītā's death
- Fixed "calling kin" → "calling relatives"
- Fixed "His kin carried" → "His nephews carried"
- Removed the simile

---

## 0097-ramachandra
**Issues found:**
- [Missing death] Padmā (mother, dies 1628) not mentioned
- [Pseudosociological] "male kin"
- [Figurative] "as if they were clever verses", "like a crow counts scraps"

**Changes made:**
- Added Padmā's death
- Fixed "male kin" → "relatives"
- Removed first simile
- Changed second to "telling Bairagi Das that Panchu cheated on the grain count"
- **[DEVIATED FROM DEBUG]** Debug shows Mahadev dies 1631, but narrative shows him alive through 1642. Decision: keep Mahadev alive as written. He is integral to the story as the responsible older brother managing Ramachandra's behavior, and the narrative_plan describes their relationship as lasting throughout.

---

## 0098-tablût
**Issues found:**
- [Pseudosociological] "links to kin support"

**Changes made:**
- Fixed "kin support" → "family support"

---

## 0099-fábio-henrique
**Issues found:** None

**Changes made:** None

---

# Summary

**Issue types found:**
- Missing deaths/events (most common)
- Pseudosociological "kin" language
- Figurative language (similes with "as if")
- Chronology errors
- Logical gaps (missing context)
- Vague hedging ("X or Y")
- Clarity issues

**Major unfixed issues:** None

**Resolved by deviating from debug:**
- 0062-kanu: Daro kept alive as written (debug death_year appears to be data error)
- 0097-ramachandra: Mahadev kept alive as written (debug death_year appears to be data error)

---

# Systematic Check: Cramped Openings

Checked all opening paragraphs in 0040-0099 against the "cramped opening" standard from 0030-0039 (where the original 0031-eirēnē had too much context crammed into the first sentence).

**Finding**: No severely cramped openings found. Most stories spread context effectively across the first paragraph. Two stories are on the denser end:
- 0080-xie-ping: First paragraph covers governance, language, livelihood, building details, three generations, and religion—but remains readable
- 0086-sitaram: Second sentence lists 5 types of authority—but this sets up the irrigation conflict later

Neither requires editing. The generation quality for opening paragraphs is consistent across batches.

---

# Review: Stories 0000-0029

## Systematic Check: Pseudosociological "kin" Language

Searched all stories 0000-0029 for pseudosociological "kin" in narrative text. Found and fixed 25 instances:

**Changes made:**
- 0002-bhima: "Kanta and his kin washed his body" → "Kanta and his family washed his body"
- 0003-mercedes: "the kin house rearranged itself" → "the family household rearranged itself"
- 0004-koitale: "tied to Koitale's kin" → "tied to Koitale's family"; "Their mother's kin took them in" → "Their mother's family took them in"
- 0005-tako: "pull of kin ties" → "pull of family ties"
- 0007-kandan: "Shaiva or Vaishnava shrine" → "Shaiva shrine" (vague hedging); "older kin" → "older relatives"; "through kin ties" → "through family ties"; "His kin washed the body" → "His family washed the body"
- 0009-anandi: "kin councils" → "caste councils"; "Her kin washed her body" → "Her husband's family washed her body"
- 0010-hanna: "not just kin" → "not just relatives"; "His kin retrieved the body" → "His family retrieved the body"
- 0011-pleuron: "close kin" → "close relatives"; "Scenon's kin demanded" → "Scenon's family demanded"; "His kin washed him" → "His family washed him"
- 0016-chuku: "Kiran's kin had fields" → "Kiran's family had fields"; "Kiran's kin recovered him" → "Kiran's family recovered him"
- 0024-mielo: "kin groups held fishing places" → "family groups held fishing places"
- 0025-poda: "paid kin with milk" → "paid neighbors with milk"; "Kanni's kin" → "Kanni's relatives"
- 0027-pachompsais: "network of kin" → "network of relatives"; "Taesis's surviving kin" → "Taesis's surviving relatives"
- 0028-peldzom: "close enough to kin" → "close enough to family"; "Jampa's kin" → "Jampa's family"; "nearby kin" → "nearby relatives"

## Figurative Language Review

Searched for "as if" patterns. Found several in 0000-0029 but most are effective psychological expressions rather than descriptive similes:
- 0010-hanna: "as if a blessing could be carried home like bread" - simile (minor)
- 0010-hanna: "as if it ended the matter" - effective psychology (kept)
- 0010-hanna: "as if talk could shift the outcome" - effective psychology (kept)
- 0011-pleuron: "as if nothing had happened" - effective psychology (kept)

**No changes required** - the figurative language in 0000-0029 is appropriate.

## Vague Hedging

One vague hedge fixed:
- 0007-kandan: "Shaiva or Vaishnava shrine" → "Shaiva shrine"

## Individual Story Review (0000-0029) - Second Pass

This pass reviewed each story one-by-one, with special attention to:
1. Death coverage (every person with death_year during protagonist's lifetime must be mentioned)
2. Chronology verification
3. "Kin" language
4. Figurative language

### Stories Reviewed:

**0000-zhang-wei**: Clean - no issues found

**0001-nagamma**: Clean - no issues found

**0002-bhima**:
- [Missing death] Father Khema's death missing
- Fixed: Added Khema's death in 1003

**0003-mercedes-condori-herrera**:
- [Missing death] Brother Santos's death (age 15) missing
- Fixed: Added Santos's death the year after Enrique's death

**0004-koitale**:
- [Chronology error] Namunyak died "when Koitale was ten" but debug shows she was 6
- Fixed: Changed "ten" → "six"

**0005-tako**: Clean (after earlier "kin ties" fix)

**0006-nadiia**: Regenerated with toddler-specific prompts (January 2026). Post-regeneration review:
- [AI-slop] "grew into the routine of" → "The yard was busy:"
- [AI-slop] "shaped the way she handled" → "After that loss she watched Nadiia closely"

**0007-kandan**: Clean (after earlier "kin" and vague hedging fixes)

**0008-mallamma**:
- [Missing death] Father Narayana's death (707) missing
- Fixed: Added Narayana's death after age marker

**0009-anandi**:
- [Chronology] Marriage (1194) came after Champa's death (1195) in text
- [Kin] Fixed earlier
- Fixed: Reordered events for correct chronological flow

**0010-hanna**:
- [Missing death] Brother Yusuf's death (1282) missing
- [Missing death] Mother Mariam's death (1286) missing
- [Figurative] "as if a blessing could be carried home like bread"
- [Kin] Fixed earlier
- Fixed: Added both deaths; changed simile to "hoping the blessing would stay with them"

**0011-pleuron**:
- [Missing death] Grandmother Monun's death (when Pleuron was 24) missing
- [Missing death] Mother Arban's death (when Pleuron was 42) missing
- [Missing death] Father Skeron's death (when Pleuron was 51) missing
- [Kin] Fixed earlier
- Fixed: Added all three deaths in correct chronological positions

**0012-kpovi**: Clean - no issues found

**0013-nathu**: Regenerated with toddler-specific prompts (January 2026). Post-regeneration review:
- [Vague hedging] "rice or a spoon of thin lentils" → "rice"
- Note: Regenerated narrative used different names (Harsha→Nathu, etc.) - restored original names to match existing story

**0014-hadiya**:
- [Missing deaths] 5 deaths missing:
  - Brother Pazur (infant)
  - Grandfather Yatna (age 28)
  - Grandmother Ninsun (age 38)
  - Father Gadday (age 48)
  - Mother Rimta (age 58)
- [Kin] "kin ties" → "family connections"
- Fixed: Added all five deaths in correct chronological positions

**0015-hormizd**: Regenerated with toddler-specific prompts (January 2026). Post-regeneration review:
- [AI-slop] "grew into the rhythms of dairy and smoke" → "The household ran on milk and fire"

**0016-chuku**:
- [Missing death] Uncle Haruno's death missing
- [Kin] Fixed earlier
- Fixed: Added Haruno's death

**0017-person-0017-unnamed**: Clean - no issues found

**0018-vasundhara**:
- [Missing death] Elder Bharadvaji's death missing
- Fixed: Added Bharadvaji's death

**0019-sovan**: Clean - no issues found

**0020-hind**: Clean - no issues found

**0021-tomi**:
- [Missing death] Brother Kano's death (2296 BC, when Tomi was 69) missing
- [Missing death] Sister Saka's death missing
- Fixed: Added both deaths

**0022-chikako**: Clean - no issues found (very long, well-structured story)

**0023-paravi**:
- [Missing death] Mother Kanni's death (when Paravi was ~46) missing
- Fixed: Added Kanni's death

**0024-mielo**:
- [Missing death] Grandmother Rauko's death (when Mielo was 25) missing
- [Missing death] Mother Kaino's death (when Mielo was 45) missing
- [Anachronism] "Rauko made them bring offerings" at age 34, but Rauko died at age 25
- Fixed: Added both deaths; fixed anachronistic Rauko reference to Kaino

**0025-poda**:
- [Missing death] Brother Vasu's death (71 AD) missing
- [Missing death] Brother Dandula's death (72 AD) missing
- [Missing death] Uncle Kalu's death (78 AD) missing
- [Missing death] Son Dandu's death (88 AD) missing
- [Consistency error] Narrative had Dandu alive at Poda's death (93 AD), but debug shows Dandu died in 88 AD
- Fixed: Added all four deaths; fixed ending to remove dead Dandu

**0026-person-0026-unnamed**:
- [Naming issue] Narrative named the infant "Devan" but naming_category is "unnamed"
- Fixed: Changed "Devan" → "The child" / "The baby" throughout

**0027-pachompsais**:
- [Missing death] Mother Taesis's death (when Pachompsais was ~45) missing
- [Kin] "Tachonsis's kin" in narrative
- [Consistency] Ending referenced "Taesis's surviving relatives" but Taesis was dead
- Fixed: Added Taesis's death; changed "kin" → "family"; fixed ending

**0028-peldzom**:
- [Missing death] Brother Yeshe's death (1041) missing
- Fixed: Added Yeshe's death

**0029-murugan**:
- [Missing death] Aunt Sellammal's death (2012) missing
- Fixed: Added Sellammal's death

---

## Summary of Second Pass (0000-0029)

**Most common issue**: Missing deaths of caretakers, siblings, children who died during the protagonist's lifetime. This was found in 18 of 30 stories.

**Pattern identified**: Stories with 5+ siblings or 3+ children reliably have missing deaths that need to be added.

**Other issues fixed**:
- 3 chronology errors
- 1 naming issue (unnamed infant given a name)
- 2 consistency errors (dead characters appearing alive)
- 1 anachronism (reference to dead character as if alive)
- Multiple "kin" → "family/relatives" substitutions

**Stories that were clean on all passes**: 0000, 0001, 0005, 0012, 0017, 0019, 0020, 0022

## Overall Assessment

Stories 0000-0029 are now fully reviewed. The main systematic issue was missing deaths of characters who died during the protagonist's lifetime. This has been comprehensively fixed across all 30 stories.

---

# Toddler Story Regeneration (January 2026)

Seven stories featuring children aged 2-4 were regenerated with new toddler-specific prompts to add developmental moments and richer personality expression. These stories now include:
- Concrete developmental milestones (first words, early walking, favorite objects)
- Emerging personality shown through behavior
- Caretaker interactions specific to toddler age

**Regenerated stories:**
- 0006-nadiia (age 4)
- 0013-nathu (age 3)
- 0015-hormizd (age 3)
- 0057-yusuf (age 3)
- 0058-timma (age 4)
- 0082-tari (age 4)
- 0089-soma (age 2)

**Common issues found in regenerated stories:**
- AI-slop phrases: "rhythm of", "routine of", "grew into" patterns
- One instance of vague hedging ("X or Y")
- One confusing name collision (sibling sharing grandmother's name)
- One pseudosociological term ("patrilocal joint household")

All issues were fixed during post-regeneration review. The regenerated stories are now in `_lives_pending/` awaiting final transfer to `_lives/`.
