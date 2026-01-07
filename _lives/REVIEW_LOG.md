# Review Log (Stories 0030-0099)

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

**Changes made:**
- Changed "Bera had died the year before, in 1378" → "Bera died the following year, in 1378"
- Changed the years of theft to "1379, 1380, and after"
- Added Ansa's death: "Ansa, her father's brother, followed in 1388"
- Fixed chronological order: moved Rati/Ansa deaths before Sana's death
- Added Nisa's death: "Nisa, her mother, died in 1404..."
- Changed "The kin washed her body" → "The women of the household washed her body"

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
**Issues found:** None

**Changes made:** None

---

## 0058-timma
**Issues found:**
- [Pseudosociological] "trading small bundles through kin"

**Changes made:**
- Fixed "through kin" → "through relatives and neighbors"

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
- **[MAJOR CHRONOLOGY ERROR - UNFIXED]** Debug shows Daro (oldest brother) dies same year Kanu was born, but narrative shows Daro alive throughout Kanu's life. Requires major structural rewrite.
- [Pseudosociological] "join kin for work"

**Changes made:**
- Fixed "join kin" → "join relatives"
- Daro chronology issue flagged but NOT fixed - requires human decision

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
**Issues found:** None

**Changes made:** None

---

## 0076-venkamma
**Issues found:**
- [Logical impossibility] Mother dies at birth, but younger brother born 2 years later
- [Missing identification] Kondayya introduced without identifying as father
- [Unclear sibling ordering] Siblings introduced in confusing order

**Changes made:**
- Fixed by adding father's remarriage: "Kondayya remarried, and two years after Venkamma's birth, his new wife bore a son..."
- Changed "Kondayya's sister" → "her father Kondayya's sister"
- Rewrote family introduction to introduce all siblings in birth order

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
**Issues found:**
- [Pseudosociological] "tied together by kin"

**Changes made:**
- Fixed "by kin" → "by family"

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

**Changes made:**
- Fixed "kin" → "relatives"
- Fixed "handpump or well" → "well"
- Removed the simile

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
**Issues found:** None

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
- **[MAJOR CHRONOLOGY ERROR - UNFIXED]** Debug shows Mahadev (older brother) dies 1631, but narrative shows him alive in 1635, 1637-1638, 1642. Requires major structural rewrite.
- [Missing death] Padmā (mother, dies 1628) not mentioned
- [Pseudosociological] "male kin"
- [Figurative] "as if they were clever verses", "like a crow counts scraps"

**Changes made:**
- Added Padmā's death
- Fixed "male kin" → "relatives"
- Removed first simile
- Changed second to "telling Bairagi Das that Panchu cheated on the grain count"
- **NOT FIXED**: Mahadev chronology error - requires major structural rewrite

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

**Major unfixed issues:**
- 0062-kanu: Daro chronology error (dies year Kanu born but shown alive throughout)
- 0097-ramachandra: Mahadev chronology error (dies 1631 but shown active through 1642)

Both require structural rewrites beyond the scope of this review.

---

# Systematic Check: Cramped Openings

Checked all opening paragraphs in 0040-0099 against the "cramped opening" standard from 0030-0039 (where the original 0031-eirēnē had too much context crammed into the first sentence).

**Finding**: No severely cramped openings found. Most stories spread context effectively across the first paragraph. Two stories are on the denser end:
- 0080-xie-ping: First paragraph covers governance, language, livelihood, building details, three generations, and religion—but remains readable
- 0086-sitaram: Second sentence lists 5 types of authority—but this sets up the irrigation conflict later

Neither requires editing. The generation quality for opening paragraphs is consistent across batches.
