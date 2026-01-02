# Narrative Generation Issue Tracker

**Purpose**: Track recurring issues and patterns in generated narratives to inform prompt improvements and quality control.

**Review Process**: Stories in `_lives/0000-*.md` through `_lives/0019-*.md` use the most recent generation process and are being systematically reviewed.

---

## Issues Found in Review

### Story 0000 (Anna)

**Issue 1: Incorrect sibling count in narrative**
- **Severity**: High (factual error)
- **Description**: Narrative states "Seven older siblings filled the house yard" but Anna is birth position #6, so she has only 5 older siblings (and 2 younger siblings).
- **Data**: `birth_order_position: 6`, `number_of_siblings: '7'` (8 children total)
- **Location**: Line 130 in narrative
- **Fix needed**: Narrative generation should correctly calculate number of older vs. younger siblings from birth order position

**Issue 2: Dead siblings not accounted for at birth**
- **Severity**: High (factual/temporal error)
- **Description**: Three siblings died at ages 0, 1, and 1. Given typical child spacing, at least 1-2 of these deaths likely occurred **before** Anna's birth in 629, but narrative treats all 7 siblings as present during her lifetime.
- **Data**: `sibling_ages_at_death: [5, 0, 1, 41, 1, 35, 26]`
- **Fix needed**: LLM should infer approximate birth years of siblings based on typical spacing (2-3 years) and determine which siblings were alive during the person's lifetime. Alternatively, the demographic generation step could provide this information explicitly.

---

### Story 0001 (Baska)

**Issue 3: Unnecessary/obvious statements**
- **Severity**: Low (style)
- **Description**: "His household held three generations under one roof." - The next sentences already show this by describing grandfather, grandmother, parents. The statement is redundant.
- **Location**: Line 149
- **Pattern**: Stating what could be shown. Remove summary statements that are immediately demonstrated.

**Issue 4: Sibling ordering vague/confusing**
- **Severity**: Medium (clarity)
- **Description**: "Baska was the fifth of seven children. His two older sisters... Two older brothers... Another brother was born and died the same day, and another brother died before he learned to walk. The last child, a sister, lived only one year."
- **Problem**: Listing is confusing - which siblings were older vs younger? When did they die relative to Baska's life?
- **Data**: `birth_order_position: 5`, `sibling_ages_at_death: [55, 9, 70, 0, 0, 1]`
- **Fix**: Clearer temporal logic - who was alive when, who came before/after him

**Issue 5: Emotionally flat/distant phrasing**
- **Severity**: Medium (style - repetition risk)
- **Description**: "The house absorbed each death into its routines." - Cold/distant tone. May be accurate for how the household dealt with infant death, but if this becomes the default mood across stories, it will feel repetitive and stylized.
- **Location**: Line 151
- **Pattern to watch**: Check if this detached tone recurs across multiple stories

**Issue 6: Awkward temporal conjunction phrasing**
- **Severity**: Low (style)
- **Description**: "When Baska learned to walk, the river rose and spread over the low ground." - The "when X, Y happened" structure implies connection but there isn't one. The flood happened to occur around that age, but the phrasing suggests causation or significance.
- **Location**: Line 153
- **Fix**: Either just state his age ("At two, the river rose...") or find a less conjunctive phrasing

**Issue 7: Formulaic time markers**
- **Severity**: Medium (style - repetition)
- **Description**: Repeated formulaic phrases:
  - "In his late twenties" (line 165)
  - "When Baska was in his mid-thirties" (line 169)
  - "In his fortieth year" (line 173)
- **Pattern**: These phrases become noticeable and feel template-like
- **Fix**: Vary time markers or omit when context makes timing clear

**Issue 8: Disconnected child paragraphs**
- **Severity**: Medium (structure/flow)
- **Description**: Paragraph about three daughters (line 167) feels disconnected from surrounding narrative. Lists children but doesn't integrate them into the life flow.
- **Pattern**: Children introduced as list rather than woven into ongoing story

**Issue 9: Relationship development absent**
- **Severity**: Medium (content depth)
- **Description**: No sense of how relationship with wife Sagma and daughters evolves over 15+ years. We see initial meeting and one teaching moment, but nothing about the long middle.
- **Pattern to watch**: Check if long relationships (marriages, parent-child) remain static across stories

**Issue 10: Vague "kin" reference**
- **Severity**: Low (precision)
- **Description**: "Baska died in the stilt house with his wife and kin in the next room" - which kin? Be specific.
- **Location**: Final line
- **Data shows**: Extended household with siblings/collateral kin and children at death
- **Fix**: Name specific people or at least specify relationship

**Issue 11: Extreme personality traits not visible**
- **Severity**: High (core feature not working)
- **Description**: Baska has extreme personality traits (0th percentile extraversion, 98th percentile honesty-humility) but narrative only shows moderate versions
- **Data**: `Extraversion: 0`, `Honesty-Humility: 98`
- **What we see**: Some social avoidance, quiet demeanor - reads as moderate shyness
- **What we should see at 0th percentile**: Near-pathological social withdrawal, extreme difficulty with even minimal interactions
- **Missing entirely**: 98th percentile honesty-humility - no scenes of active honesty in difficult situations, refusing advantages, correcting misattributions, etc.
- **Fix**: When personality traits are at extremes (below 10th or above 90th percentile), narrative MUST include concrete scenes demonstrating those extremes through action

---

### Story 0002 (Rudra)

**Issue 12: Chronological sequencing error**
- **Severity**: High (factual error)
- **Description**: Paragraph about drought/debt opens "By his mid-thirties" (ages 34-36) but comes *after* the raid paragraph which opens "When Rudra was in his early forties." Narrative goes backward in time without signaling it.
- **Location**: Paragraphs 9-10

**Issue 13: Default stoicism for child death**
- **Severity**: Medium (pattern/variation)
- **Description**: "those losses sat in the household's talk the way failed crops did, as something to be remembered without ceremony" — same flattening move as Baska's "The house absorbed each death into its routines." Defaults to stoic/fatalistic framing. Many households would show raw grief, wailing, withdrawal, fear.
- **Location**: Line 199
- **Pattern**: See also Issue 5 (Baska). LLM defaults to emotional flatness for child death regardless of personality/culture.

**Issue 14: Children as catalog**
- **Severity**: Medium (recurring pattern)
- **Description**: "Eight were born alive. Two daughters died as infants and a third child died before walking." Lists children rather than integrating them. Govinda and Hari get a sentence each; surviving daughters are unnamed and invisible.
- **Location**: Line 207
- **Pattern**: See also Issue 8 (Baska). Children introduced as inventory rather than woven into story.

**Issue 15: Choppy sentence rhythm in transitions**
- **Severity**: Low (style)
- **Description**: "He married in his early twenties. The marriage was arranged between families that traded help at harvest. His wife, Sita, came from another village within a day's walk, carrying a bundle of cloth and a brass pot" — three short declarative sentences in a row, reads like bullet points.
- **Location**: Line 205

**Issue 16: Weak/vague transition phrases**
- **Severity**: Low (style)
- **Description**: Several weak transitions:
  - "By his mid-thirties he faced a different kind of danger" — vague, and calling economic hardship "danger" after literal sword violence feels off
  - "In his fifties Rudra's body began to betray him" — slightly purple/clichéd, personifies body, violates plain prose guideline
- **Locations**: Lines 211, 215

**Issue 17: Spouse death compression**
- **Severity**: Medium (emotional beats shortchanged)
- **Description**: Detailed, moving description of caring for sick Sita, but her actual death compressed to "After that period she did not return to full strength, and later she died" — half a sentence.
- **Location**: Line 219

**Issue 18: Telegraphic death sentence for long-lived person**
- **Severity**: Low-Medium (style)
- **Description**: "On September 26, 971, he died during an episode of high fever" — flat, redundant (we know about the fevers), anticlimactic for 84-year life. Date-stamp endings work for infants (Anna) but feel hollow for elders.
- **Location**: Final line
- **Compare**: Baska's ending has sensory grounding ("the sound of water moving in the channels outside")

**Issue 19: Witnessed violence without lasting consequence**
- **Severity**: Low-Medium (could be intentional)
- **Description**: Raid scene is vivid—man cut down, houses burned—but aftermath limited to "for weeks he checked the horizon whenever dogs barked." No exploration of lasting effects across remaining 40+ years.
- **Location**: Line 209

**Issue 20: Siblings vanish after childhood**
- **Severity**: Low (structural)
- **Description**: Story sidesteps sibling-counting by being vague ("older brothers and sisters already carrying water") but as a result no siblings appear as characters after the first paragraph. In a joint household, adult siblings would remain significant.
- **Location**: Line 199 onward

---

### Story 0003 (Ayyadurai)

**Issue 21: Extreme low intelligence not shown**
- **Severity**: High (core feature not working)
- **Description**: 1st percentile intelligence should be noticeable—struggling with basic reasoning, counting, understanding instructions. Instead we get "started tasks in the wrong order, forgot tools" which reads as disorganized, not cognitively limited.
- **Data**: `Intelligence (% rank): 1`
- **Pattern**: See also Issue 11 (Baska) for extreme traits underplayed

**Issue 22: Depression in metadata but invisible in narrative**
- **Severity**: Medium (trait not shown)
- **Description**: Metadata says `mental_disorder: Depressive disorder or chronic dysphoria` but narrative shows him functioning, having friendships, pursuing an affair. No episodes of withdrawal, hopelessness, inability to work, or changes beyond baseline poverty effects.
- **Location**: Throughout

**Issue 23: Slightly figurative language**
- **Severity**: Low (style)
- **Description**: "His childhood memory held the feel of dust on the tongue" — "memory held the feel" is slightly poetic/figurative, violates plain prose guideline.
- **Location**: Line 166

**Issue 24: Children as catalog (again)**
- **Severity**: Medium (recurring pattern)
- **Description**: "Eight children were born. Two died the same season they were born, and another died before his second year." Same inventory-style listing.
- **Location**: Line 174
- **Pattern**: See Issues 8, 14. Fourth story with this pattern.

**Issue 25: Stoic child death (again, but may fit here)**
- **Severity**: Low-Medium
- **Description**: "Ayyadurai carried a small bundle to the cremation ground and came back to work the next morning. He did not speak much about it." Same emotional flatness—though here it may fit better given depression plus grinding poverty producing numbness.
- **Location**: Line 174
- **Pattern**: See Issues 5, 13. But note this instance is more defensible given character circumstances.

**Issue 26: Wife underdeveloped compared to affair**
- **Severity**: Medium (imbalance)
- **Description**: Meenakshi introduced in one paragraph, dies in a sentence ("Meenakshi died before Ayyadurai reached old age"). Meanwhile affair with Ponnammal gets a full vivid paragraph with specific details (salt fish in leaf, her laughing). Wife of his whole adult life deserves more.
- **Location**: Lines 172, 182

**Issue 27: Telegraphic death (again)**
- **Severity**: Low-Medium (style)
- **Description**: "On October 20, 1688, the fever ended his life in his house." Same date-stamp death. Final sentence ("The body was carried out the same day, and the household turned back to finding grain for the next meal") is actually good—shows grinding continuity of poverty—but death itself rushed.
- **Location**: Final lines
- **Pattern**: See Issue 18

**Issue 28: Awkward parenthetical construction**
- **Severity**: Low (style)
- **Description**: "By his late teens he moved for work, not far, shifting between villages within a day's walk" — "not far" feels like an awkward parenthetical that should be integrated better.
- **Location**: Line 170

**Issue 29: Technical/academic terminology in narrative**
- **Severity**: Low-Medium (style)
- **Description**: "Their household stayed nuclear" uses sociological jargon that doesn't belong in plain narrative prose. Also unfortunate phrasing.
- **Location**: Line 172

**Issue 30: Vague quantities where specifics are available**
- **Severity**: Low (precision)
- **Description**: "and a small number of unmarried children" — how many? The data shows exactly which children survived. Be specific.
- **Location**: Line 182

---

### Story 0004 (Bhagavati)

**Issue 31: AI-slop metaphor "set the rhythm"**
- **Severity**: Low-Medium (style)
- **Description**: "She entered an extended household where an older man's word set the rhythm" — metaphorical, vague. The next sentences show concretely what he did (sat near doorway, kept seals and strings). The abstract framing is unnecessary.
- **Location**: Line 173

**Issue 32: Generic goddess instead of named deity**
- **Severity**: Low-Medium (specificity)
- **Description**: "the goddess shrine at the edge of the fields" — should name the deity. Given the region (Deccan/Maharashtra) and era, this could be a grama-devata like Mariai, Yellamma, or a local form of Durga. Metadata says `village deity/goddess worship (grama-devata)`. Bhagavati herself is named after a goddess form.
- **Location**: Lines 171, 181, 199

**Issue 33: Repetitious seasonal/religious framing**
- **Severity**: Low (pattern)
- **Description**: "People marked seasons by the monsoon and by the goddess shrine at the edge of the fields" — similar abstract framing appeared in Rudra and earlier stories. Becoming a template.
- **Location**: Line 171

**Issue 34: Sibling sex order error**
- **Severity**: High (factual error)
- **Description**: Narrative says "Three brothers came before her, then two sisters." But sibling_sexes data is [F, M, M, M, F, F] — first sibling is female, not male. Should be one sister, then three brothers, then one sister before Bhagavati.
- **Data**: `sibling_sexes: [F, M, M, M, F, F]`, `birth_order_position: 6`
- **Location**: Line 175

**Issue 35: Abstract/sociological phrasing**
- **Severity**: Low (style)
- **Description**: "The local order ran through landed families and their ties to a warrior elite" — reads like a textbook rather than narrative prose.
- **Location**: Line 171

**Issue 36: Slightly introspective/poetic phrasing**
- **Severity**: Low (style)
- **Description**: "when she could stand still and let the noise cover her thoughts" — slightly interior/poetic for plain prose style.
- **Location**: Line 199

**Issue 37: Low neuroticism (6th percentile) not strongly visible**
- **Severity**: Low-Medium (trait underplayed)
- **Description**: 6th percentile neuroticism is remarkably low anxiety/emotional reactivity. She functions under extreme stress (abuse, assault, poverty) which fits, but we don't see the positive side: unusual calm, equanimity, low baseline worry even in safe moments.
- **Data**: `Neuroticism (% rank): 6`
- **Pattern**: Subtler than high-extreme traits being invisible, but same category of issue.

---

### Story 0005 (Rosa María Martínez)

**Issue 38: Stoic child death (again)**
- **Severity**: Medium (recurring pattern)
- **Description**: "Rosa watched her mother wrap small bodies and say prayers without stopping the day's work." Same emotional flatness pattern, fifth story.
- **Location**: Line 173
- **Pattern**: See Issues 5, 13, 25

**Issue 39: Children as catalog (again)**
- **Severity**: Medium (recurring pattern)
- **Description**: "Rosa gave birth seven times. Three daughters and four sons. One girl lived into old age; another died at one year. Three boys died at birth or within days. Two sons grew to adulthood..." Inventory listing, though slightly better than previous by giving some children fates.
- **Location**: Line 179
- **Pattern**: See Issues 8, 14, 24

**Issue 40: Sibling death undercount**
- **Severity**: Medium (factual error)
- **Description**: Text says "Two of the girls died as toddlers" but sibling_ages_at_death [61, 0, 2, 62, 4, 1, 48] shows 4 early deaths (ages 0, 2, 4, 1). Undercount.
- **Data**: `sibling_ages_at_death: [61, 0, 2, 62, 4, 1, 48]`
- **Location**: Line 173

**Issue 41: Slightly poetic/abstract phrasing**
- **Severity**: Low (style)
- **Description**: "They were mestiza people of the river and forest edge" — "people of the river" sounds writerly. Also "tied to Spanish law and parish ritual and to the daily demands of clearing, planting, and finding paid work" — list of three feels rhetorical/cadenced.
- **Location**: Line 171

**Issue 42: Low intelligence (15th percentile) not clearly shown**
- **Severity**: Low-Medium (trait underplayed)
- **Description**: We get "forgot what she had been sent to fetch" in childhood, but as adult she seems competent: navigates social networks, runs washing business, manages household. 15th percentile isn't extreme but should be more visible.
- **Data**: `Intelligence (% rank): 15`
- **Location**: Throughout

**Issue 43: Weak transition phrase**
- **Severity**: Low (style)
- **Description**: "Rosa's days settled into a pattern." — weak, generic transition.
- **Location**: Line 181

**Issue 44: Clichéd phrasing**
- **Severity**: Low (style)
- **Description**: "News of unrest reached even the interior." — slightly clichéd news-reaching-remote-places phrasing.
- **Location**: Line 185

**Issue 45: Spouse death compression (but less severe)**
- **Severity**: Low-Medium
- **Description**: Pedro's death compressed to "He collapsed after days of fever during the rainy season, and he was buried quickly on damp ground." Contrast with good space given to mother Lucía's death. Not as bad as Rudra's wife, but still brief for a lifelong partner.
- **Location**: Line 193
- **Pattern**: See Issue 17, 26

---

### Story 0006 (Person 0006, unnamed)

**Issue 46: Narrating unborn siblings**
- **Severity**: High (conceptual error)
- **Description**: "This child was the fifth of eleven. Two older brothers had already been buried as small children. Three younger ones had not yet been born." The baby lived one day—she has no relationship to siblings born after her. Counting "eleven" and mentioning unborn children narrates from outside her existence entirely.
- **Location**: Line 99

**Issue 47: Older sibling sex error**
- **Severity**: High (factual error)
- **Description**: Text says "Two older brothers had already been buried as small children." But sibling_sexes for first 4 siblings (those older than her) are [F, M, M, M] — the first older sibling is female, not male. Should reference an older sister.
- **Data**: `sibling_sexes: [F, M, M, M, F, F, M, F, F, M]`, `birth_order_position: 5`
- **Location**: Line 99

**Issue 48: Nonexistent older sisters doing chores**
- **Severity**: High (factual error)
- **Description**: "The older girls helped Eje bring firewood" — but the only older female sibling (first child) died at age 0. There are no living older sisters at the time of this baby's birth. The older surviving siblings would be brothers.
- **Data**: First sibling is F who died at 0; siblings 2-4 are M
- **Location**: Line 99

---

## Consolidated Issue Patterns

### High Priority (Factual Errors — Need Code Fixes)

**1. Sibling temporal logic errors**
- Issues: 1, 2, 4, 34, 40, 46, 47, 48
- Stories affected: 5/7 (Anna, Baska, Bhagavati, Rosa María, Person 0006)
- Problem: LLM receives raw sibling data but fails to compute:
  - Which siblings are older vs younger (from birth_order_position)
  - Which siblings were alive at subject's birth (requires estimating birth years)
  - Which siblings died before subject was born
  - Correct sex of siblings in birth order
- Fix: Pre-compute sibling context in `_add_family_context()` and pass explicit data like "At birth, you had 2 living older brothers (ages 4, 2) and 1 older sister who died before you were born"

**2. Extreme personality traits not visible**
- Issues: 11, 21, 37, 42
- Stories affected: 3/7 (Baska, Ayyadurai, Bhagavati, Rosa María)
- Problem: Traits at 0th, 1st, 6th, 15th percentile read as mild/moderate rather than extreme
- Examples:
  - 0th percentile extraversion shows as "quiet" not pathological withdrawal
  - 1st percentile intelligence shows as "disorganized" not cognitively limited
  - 98th percentile honesty-humility has no scenes demonstrating it
- Fix: Flag extreme traits (below 10th or above 90th percentile) and require specific scenes demonstrating them

**3. Mental disorders invisible in narrative**
- Issues: 22
- Stories affected: 1/7 (Ayyadurai)
- Problem: Depression noted in metadata but narrative shows normal functioning
- Fix: Same as personality — require concrete demonstration through behavior

**4. Chronological sequencing error**
- Issues: 12
- Stories affected: 1/7 (Rudra)
- Problem: Narrative goes backward in time without signaling
- Fix: Add chronological check or explicit instruction to maintain strict temporal order

### Medium Priority (Recurring Patterns — Need Prompt Changes)

**5. Children introduced as catalog/inventory**
- Issues: 8, 14, 24, 39
- Stories affected: 5/5 with children (Baska, Rudra, Ayyadurai, Rosa María, Bhagavati)
- Pattern: "X children were born. Y died as infants. Z survived." Lists rather than integrates.
- Fix: Prompt instruction — "Do NOT list children as inventory. Introduce them through scenes."

**6. Default stoicism for child death**
- Issues: 5, 13, 25, 38
- Stories affected: 5/5 with child deaths
- Pattern: "The house absorbed each death into its routines" — same emotional flatness regardless of personality/culture
- Fix: Prompt instruction — "Grief for child death should vary by personality and culture. Some families wail, some withdraw, some rage. Not everyone is stoic."

**7. Spouse death compression**
- Issues: 17, 26, 45
- Stories affected: 3/4 with spouse deaths (Rudra, Ayyadurai, Rosa María)
- Pattern: Wives especially get brief treatment—introduced in a paragraph, die in a sentence
- Fix: Prompt instruction about giving long-term partners proportional narrative space

**8. Telegraphic death sentences for long-lived people**
- Issues: 18, 27
- Stories affected: 2/4 adult deaths (Rudra, Ayyadurai)
- Pattern: "On [date], he died" — flat, anticlimactic for lives of 40+ years
- Fix: Prompt guidance on varying death descriptions by age/circumstances

### Low Priority (Style Polish — Prompt Refinement)

**9. AI-slop phrasing and metaphors**
- Issues: 16, 23, 29, 31, 35, 36, 41, 43, 44
- Patterns:
  - "set the rhythm," "body began to betray him," "news reached even the interior"
  - Abstract sociological framing ("The local order ran through...")
  - Weak transition phrases ("Rosa's days settled into a pattern")
  - Slightly figurative language ("memory held the feel")
- Fix: Add banned phrase list to prompt; strengthen plain prose instructions

**10. Generic religious references instead of named deities**
- Issues: 32, 33
- Stories affected: 2/7 (Bhagavati, Rudra)
- Pattern: "the goddess shrine" when specific deity could be named
- Fix: Prompt instruction to name specific deities where culturally appropriate

**11. Vague quantities when data is available**
- Issues: 10, 30
- Pattern: "kin," "a small number of children" when specifics are known
- Fix: Prompt instruction to be specific when data is available

**12. Formulaic time markers**
- Issues: 6, 7, 15, 28
- Pattern: Repetitive "In his late twenties," "When X was in his mid-thirties" constructions
- Fix: Prompt instruction to vary time markers

**13. Siblings vanish after childhood**
- Issues: 20
- Pattern: Siblings mentioned in childhood, absent from adult narrative
- Fix: Prompt instruction — in joint/extended households, adult siblings remain significant

---

## Implementation Plan

### Phase 1: Code Changes (High Priority)
1. [ ] **Sibling context pre-computation** — Modify `_add_family_context()` to compute and pass:
   - Older vs younger siblings with sexes
   - Which siblings were alive at birth (estimate birth years from age gaps)
   - Which siblings died before subject was born
   - Living siblings at key life stages

2. [ ] **Extreme trait flagging** — Add to `person.to_prompt_string()`:
   - Flag any trait below 10th or above 90th percentile
   - Include explicit instruction: "This person has EXTREME [trait]. Include at least one concrete scene demonstrating this."

### Phase 2: Prompt Changes (Medium Priority)
3. [ ] **Children integration** — Add to NARRATIVE_BASE_PROMPT:
   - "Do NOT list children as inventory. Introduce them through scenes and weave them into the narrative."

4. [ ] **Grief variation** — Add to NARRATIVE_BASE_PROMPT:
   - "Grief for child death should vary by personality and culture. Not everyone is stoic."

5. [ ] **Spouse development** — Add to NARRATIVE_BASE_PROMPT:
   - "Give long-term partners (spouses, life companions) proportional narrative development."

### Phase 3: Style Polish (Low Priority)
6. [ ] **Banned phrases** — Expand AVOID THESE PHRASES list in NARRATIVE_BASE_PROMPT
7. [ ] **Named deities** — Add instruction to name specific deities
8. [ ] **Specificity** — Add instruction to use specific quantities when data available

---

