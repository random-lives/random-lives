---
name: review-stories
description: Review a story for potential issues. Use when asked to check a story for issues 
---

# Story Review Workflow

You are reviewing biographical stories in `_lives/` for quality issues before publication.

## Your Task

Review stories in `_lives/` following the workflow below.

**CRITICAL**: Complete ALL steps for ONE story before moving to the next. Do not batch reads.

## Per-Story Process

1. **Read story carefully** - read every sentence, don't skim
2. **Build family timeline** - for stories with siblings/children, cross-reference debug data at the bottom of the file
3. **Create issue log** - list ALL issues found with quoted text in `_lives/REVIEW_LOG.md`
4. **Make edits** - fix all issues in the markdown file
5. **Document changes** - update log with what was changed
6. **Move to next story** - proceed automatically without waiting for approval

## Quick Checklist (Most Common Issues)

Before finishing any story review, double-check:

1. **Death coverage**: Every person in debug's `caretakers`, `siblings`, and `children` sections with a `death_year` during the protagonist's lifetime must have their death mentioned in the narrative
2. **Pseudosociological language**: Search for "kin" - almost always should be "family" or specific people
3. **Vague hedging**: Search for " or " - LLM indecision like "grain or salt" should pick one
4. **Younger siblings**: If protagonist has younger siblings, their births must be mentioned (not just appear later)

**HIGH-RISK STORIES**: Stories with 5+ siblings or 3+ children have the highest error rates. Build a complete timeline and triple-check every death.

---

## What to Look For

### 1. Family Structure and Introductions (HIGH PRIORITY)

**This is the most common issue.** The reader must understand who was in the household from the start.

**Siblings**
- All living siblings present at birth must be introduced early with approximate ages/roles
- Dead siblings should be clearly separated: those who died before protagonist's birth vs. those who died during their lifetime
- Don't group siblings who died during the protagonist's life with those who died before birth
- If any siblings are unrealistically old, fix this by making them a more reasonable age

**Narrative ordering of siblings (CRITICAL)**
- Siblings must be introduced in a logical order so the reader understands the family structure
- Don't introduce a sibling as "older" before even older siblings are established—this confuses who is oldest
- **Check**: When a sibling is described as "older," have ALL older siblings already been introduced?

**Mother dies at birth + younger siblings**
- If the mother dies at or shortly after the protagonist's birth, any younger siblings require explanation
- Who gave birth to them? Father remarried? Different mother must be mentioned.
- What happened to the stepmother? Don't leave her hanging—state concretely (she died, she left, etc.)

**Younger siblings (born after protagonist)**
- Siblings born after the protagonist MUST have their births mentioned in the narrative, not just appear later without context
- For high-mortality families, convey the sense of family size (e.g., "the sixth of what would be eleven children")
- Infant deaths that occur during the protagonist's childhood should be mentioned - they're part of the lived experience

**Children**
- Same principles apply to the protagonist's own children
- Children who die must have their deaths placed correctly in the chronology
- Don't introduce a child's death before establishing the child was born
- Verify birth years and death years against the debug data

**Other family**
- Introduce caretakers (grandparents, aunts/uncles) with their role when they first appear
- Don't have characters appear suddenly mid-narrative without prior establishment

**How to check**: Cross-reference the sibling/children data in the debug section. Make a timeline of who was alive when, then verify the narrative matches.

**Death checklist**:
1. Open the debug section and find `caretakers`, `siblings`, and `children`
2. For each person with a `death_year`:
   - Calculate: did they die during the protagonist's lifetime?
   - If yes: search the narrative for their death - is it mentioned?
   - If not mentioned: ADD IT
3. Common misses: parents, grandparents, uncles/aunts who raised them, older siblings

**Dead characters referenced as alive**:
- After adding a death, search for any later references to that character
- Characters who died cannot be mentioned as doing things after their death

**Unnamed infants**:
- Check the `naming_category` in debug data
- If it says "unnamed" (died before naming ceremony), the narrative should NOT give the infant a name
- Use "the child", "the baby", "the infant" instead

### 2. Clarity and Comprehension (HIGH PRIORITY)

The reader should be able to follow the narrative without confusion. Flag:

**Confusing phrasing**
- Sentences that don't parse clearly on first read
- Ambiguous pronouns or references
- Actions where the mechanics are unclear (who did what, how)

**Missing context**
- Characters appearing without proper introduction
- Relationships not established before they matter
- Birth order unclear when relevant
- Household arrangements not explained (who lives where, why)
- Family members mentioned mid-narrative without earlier establishment

**Logical gaps**
- Unexplained transitions
- Cause and effect not connected
- Events mentioned without showing how they were discovered or resolved
- Random topic shifts within paragraphs
- Housing/living situation changes appearing without context

**Event logic unclear**
- Events that seem related but the connection isn't stated, or seem unrelated but are presented as connected
- The reader shouldn't have to guess how events relate to each other
- General rule: The narrative must make concrete choices and communicate them clearly

**Vague references**
- Phrases like "the settled side" or "service caste duties" that assume reader knowledge
- Social/economic arrangements mentioned but not explained
- Ambiguous relationship status: "entered a union" — are they married or not? Be specific

### 3. Chronology and Time (HIGH PRIORITY)

**Temporal jumps**
- Jumping back and forth in time within paragraphs

**Unnecessary repetition of time markers**
- Starting and ending a paragraph with the same date/month
- Too many year numbers clustered together
- Too many double time use, eg, "In year X, when he was Y"

**Character introductions out of order**
- Mentioning someone in passing before properly introducing them

### 4. Anachronisms (HIGH PRIORITY)

Flag items that didn't exist in the time/place:
- Foods (chilies in 10th century India — they're from the Americas)
- Technologies
- Political terms or structures
- **Future events/people**: References to events, people, or developments that occurred after the character's death
- When uncertain, use web search to verify

### 5. Stylistic Issues

**Awkward phrases**
- "ran on energy and then wore down"
- "sex that year, private and practical"
- "shorter than most women her age would become"

**Run-on sentences**
- Long sentences that try to pack too much in
- Flag sentences that don't parse cleanly on first read

**Generic context-cramming openings**
- Opening sentences that try to establish too much context at once
- Fix by spreading context across shorter sentences, not deleting it

**Paragraphs that don't flow**
- Multiple unrelated topics crammed together
- Second half feels "tacked on" to first half
- Abrupt interludes that break narrative flow

**Too many year numbers**
- Paragraphs cluttered with dates
- Too many "In [year]" sentence openings in a row
- Fix by varying time markers: use ages ("At twenty"), relative time ("Four years later"), or milestone anchors ("After the marriage")

**Artificial name patterns**
- All names following the same phonetic structure
- Overly coincidental name pairs

### 6. Metaphors and Figurative Language

The style should be plain, direct prose. Flag and rewrite:
- Metaphors and similes
- Poetic or purple prose descriptions
- Personification of abstractions

### 7. Pseudosociological Language

Avoid academic/anthropological jargon that sounds clinical.

**"Kin" is almost always wrong:**
- "kin camps" → "families"
- "kin" → "family" (in most contexts)
- "kin groups" → "their families" or "the families"
- "kinship network" → "relatives" or "family"
- "Her kin washed her body" → "The women of the household washed her body" or name them

**Household structure jargon:**
- "joint" (describing households) → describe concretely
- "patrilocal" → just describe who lives there
- "nuclear" → avoid; describe the household composition directly

**How to check**: Search the narrative for "kin", "joint", "patrilocal", "nuclear" - if found in narrative text, replace with plain language

### 8. AI-Slop Phrases

Flag templated or meaning-making phrases:
- "rhythm of [X]"
- "settled into a pattern"
- "tightened around"
- "would prove to be"
- "little did [X] know"
- "shaped by" / "marked by" / "defined by" (when abstract)
- Abstract summaries like "death had shaped the household"
- Pseudo-profound meaningless phrases like "like a fact that explained other facts"

### 9. Vague Hedging / LLM Indecision

Flag phrases where the LLM couldn't commit to a specific detail:
- "X or Y" constructions (e.g., "dyed wool or leather preservatives" → pick one)
- "something like", "some kind of", "a type of"
- "perhaps", "likely", "may have" (narrator should be omniscient and confident)

Fix by picking one concrete option. If uncertain which is historically appropriate, use web search.

### 10. Political/Historical Claims

When a story mentions rulers, political situations, or historical events:
- If vague (e.g., "local rulers"), check if more specificity is possible for that time/place
- Some periods are genuinely murky — vagueness is fine there
- Use web search to verify when uncertain

### 11. Repetitive Patterns and Checklist Feeling

**LLM checklist feeling**
- Stories that feel stilted, like the LLM was trying to tick off items
- Mechanical inclusion of details without smooth integration
- Later paragraphs that read as "one event, then another event"
- Fix: Combine related events, show cause-and-effect, weave in character reactions

### 12. Trait Visibility

For characters with extreme personality traits (below 10th or above 90th percentile) or physical attributes, check that these manifest in concrete actions or descriptions, not just implied.

### 13. Chronicle vs Scene (Long Lives)

Narratives for people who lived 50+ years should dwell on specific moments, not just list events chronologically. Flag if it reads like a timeline rather than a life.

### 14. Major Life Events Need Adequate Detail

Significant events—especially terminal illness, major injuries, or pivotal life changes—should not be compressed into a single vague sentence. The reader should feel the weight of these events.

---

## What NOT to Flag

- Omniscient narrator stating feelings, thoughts, preferences directly ("He liked X", "She hated Y") — this is correct
- Specific dates — these are generated by the system
- Named minor characters (midwives, healers, neighbors)
- Modern geographic terms for reader orientation
- Detailed scenes showing specific moments

---

## Deviating from Debug Data

Sometimes the debug data contains implausible demographics (e.g., 57-year age gap between siblings). When this happens:

1. **Try to work with it first** - can it be explained plausibly? (e.g., half-siblings, remarriage)
2. **If not plausible, fix it** - change to something reasonable
3. **Always document clearly** - mark in the review log with **[DEVIATED FROM DEBUG]** and explain what was changed and why

This should be a last resort, not a first instinct. Most debug data is correct and should be followed.

---

## Issue Log Format

Create/update `_lives/REVIEW_LOG.md`:

```markdown
## 0030-targasnalli
**Issues found:**
- [AI-slop] "settled into a pattern" line 47
- [Clarity] Unclear who "the cousin" refers to, line 52

**Changes made:**
- Rewrote "settled into a pattern of work" → "worked the same routes each week"
- Added "A cousin from a neighboring compound" for clarity
```

For stories with no issues: `**Issues found:** None` / `**Changes made:** None`

---

## Examples from Previous Reviews

These examples from past reviews show the expected level of editing:

### Pseudosociological "kin" language
- "Her kin washed her body" → "The women of the household washed her body"
- "kin camps" → "families"
- "cooperation among kin" → "her sisters and their husbands"
- "His kin carried" → "His nephews carried"
- "village web of kin" → "village web of family"

### Vague hedging
- "dyed wool or leather preservatives" → "leather tanning solution"
- "small cake of grain or a pinch of salt" → "a pinch of grain"
- "Shaiva or Vaishnava shrine" → "Shaiva shrine"
- "washed at the handpump or well" → "washed at the well" (handpumps anachronistic for 1654)

### Figurative language
- "sparrow bones" → "little bones"
- "as if the order itself held the household together" → "said the names in a fixed order"
- "as if boiling could fix what had already happened" → (removed)
- "as if pulling words up from deep" → "he answered slowly"
- "like a fact that explained other facts" → (deleted - meaningless)

### Missing deaths
- Added: "Her father, Yang Shunfa, died in 1972..."
- Added: "Sena, an older woman in Kari's hearth group who had taught Noma wind signs and safe ice, died that winter..."
- Added: "By the time Shibtu was seventeen, Nura was dead."
- Added: "Neri outlived her husband by eight years before she too was gone"

### Chronology fixes
- "Dionysios died during the same year" → "Before the harvest that year, Dionysios fell ill with a fever and died within days"
- "At twenty-nine, in 1378" → "That same year, before the autumn" (clarifying timing relative to earlier event)
- Moved accident paragraph to correct chronological position between Sītamma's birth (1178) and death (1181)

### Impossible sibling ages (deviate from debug)
- Brothers described as "79 and 72 years older" → "were grown men" / "older brothers"
- Dionysios from 59 years old → "in his twenties" (57-year sibling gap impossible)

### Missing sibling births
- Added: "After Sitaram came more children. Kanhaiya was born in 1632 and died within days. Mohan arrived in 1634 and lasted less than a month."
- Added: "A younger brother, Kundayya, was born in 856 and survived."

### Clarity fixes
- "a youth from a neighboring hamlet" → "another young man from a neighboring hamlet" (clarifying homosexual encounter)
- Added to marriage paragraph: "Sitaram treated her with steady courtesy but without desire"
- "María, seventeen" → "Felipe's sister María, seventeen"

### Major event expansion
- "The illness was cancer, and it progressed quickly" → expanded to show physical progression with concrete details over multiple sentences

### Unnamed infants
- When `naming_category` is "unnamed": Changed "Devan" → "The child" / "The baby" throughout

---

## Starting

If no specific story is requested, list the stories in `_lives/` and ask which one(s) to review, or offer to start from the beginning.
