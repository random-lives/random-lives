# Narrative Review Guide

**Purpose**: Guide for reviewing generated narratives before publication.

---

## Quick Checklist (Most Common Issues)

Before finishing any story review, double-check:

1. **Death coverage**: Every person in debug's `caretakers`, `siblings`, and `children` sections with a `death_year` during the protagonist's lifetime must have their death mentioned in the narrative
2. **Pseudosociological language**: Search for "kin" - almost always should be "family" or specific people
3. **Vague hedging**: Search for " or " - LLM indecision like "grain or salt" should pick one
4. **Younger siblings**: If protagonist has younger siblings, their births must be mentioned (not just appear later)

**HIGH-RISK STORIES**: Stories with 5+ siblings or 3+ children have the highest error rates. Build a complete timeline and triple-check every death.

---

## Review Workflow

### Per-Story Process

**CRITICAL: Complete ALL steps for ONE story before moving to the next. Do not batch reads.**

1. **Re-read the ISSUE_TRACKER categories** - refresh yourself on what to look for before each story
2. **Read story carefully** - read every sentence. Don't skim. Check systematically against ALL issue categories below
3. **Build a family timeline** - for stories with siblings/children, cross-reference debug data to verify chronology
4. **Create issue log** - list ALL issues found, even minor ones. Quote the problematic text
5. **Make edits** - fix all issues in the markdown file
6. **Document changes** - update log with what was changed
7. **Human review** - user reviews changes
8. **Delete log** - once approved, delete the review log entry

### Reading Discipline

**You will miss issues if you read too fast.** Common failure modes:
- Glossing over sentences that "sound fine" but are actually confusing
- Missing vague hedging ("X or Y") because it reads naturally
- Not noticing family members introduced without context
- Accepting paragraphs that don't flow because the individual sentences are okay
- Missing chronology errors because you didn't verify against the debug data

**For each paragraph, ask:**
- Does every sentence parse clearly on first read?
- Are all characters properly introduced before they appear?
- Does the paragraph flow as a unit, or is the second half disconnected from the first?
- Are there any "X or Y" hedges or vague phrases?
- Does the timeline make sense?

### Issue Log Format

Create `_lives/REVIEW_LOG.md` with entries like:

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

### Guidelines

- **Anachronism verification**: Use web search when genuinely uncertain, not for things you're confident about
- **Edit scope**: All sizes allowed (word tweaks to paragraph rewrites). Flag stories with serious structural issues or demographic inconsistencies that aren't easily fixable
- **Trait visibility**: Only flag if very egregious; no need to fix missing trait manifestations
- **Batch size**: Work story by story

### Deviating from Debug Data

Sometimes the debug data contains implausible demographics (e.g., 57-year age gap between siblings). When this happens:

1. **Try to work with it first** - can it be explained plausibly? (e.g., half-siblings, remarriage)
2. **If not plausible, fix it** - change to something reasonable (e.g., "in his twenties" instead of 59 years old)
3. **Always document clearly** - mark in the review log with **[DEVIATED FROM DEBUG]** and explain what was changed and why

This should be a last resort, not a first instinct. Most debug data is correct and should be followed.

---

## What to Look For

### 1. Family Structure and Introductions (HIGH PRIORITY)

**This is the most common issue.** The reader must understand who was in the household from the start.

**Siblings**
- All living siblings present at birth must be introduced early with approximate ages/roles
- Dead siblings should be clearly separated: those who died before protagonist's birth vs. those who died during their lifetime
- Don't group siblings who died during the protagonist's life with those who died before birth
- If any siblings are unrealistically old, fix this by making them a more reasonable age
- Example problem: "Luli lasted to twelve" grouped with pre-birth deaths, but Luli actually died when protagonist was 6
- Example fix: Introduce living siblings first, then mention pre-birth deaths, then narrate deaths that occur during the story in chronological order

**Narrative ordering of siblings (CRITICAL)**
- Siblings must be introduced in a logical order so the reader understands the family structure
- Don't introduce a sibling as "older" before even older siblings are established—this confuses who is oldest
- Example problem: "her older sister Mallamma" introduced in paragraph 2, but the *even older* brothers Bhairava and Ranga not introduced until paragraph 4. Reader thinks Mallamma is the eldest.
- Example fix: Introduce the full sibling set together: "Her father had already raised four children: two sons, Bhairava and Ranga, and two daughters, Sattamma and Mallamma." Then describe each.
- **Check**: When a sibling is described as "older," have ALL older siblings already been introduced?

**Mother dies at birth + younger siblings**
- If the mother dies at or shortly after the protagonist's birth, any younger siblings require explanation
- Who gave birth to them? Father remarried? Different mother must be mentioned.
- Example problem: Mother dies at birth in 1156, but younger brother born in 1158—impossible without remarriage
- Example fix: "He remarried, and two years later his new wife bore a son."
- What happened to the stepmother? Don't leave her hanging—state concretely (she died, she left, etc.)

**Younger siblings (born after protagonist)**
- Siblings born after the protagonist MUST have their births mentioned in the narrative, not just appear later without context
- For high-mortality families, convey the sense of family size (e.g., "the sixth of what would be eleven children")
- Infant deaths that occur during the protagonist's childhood should be mentioned - they're part of the lived experience
- Example problem: Keshava and Balarāma appear later in narrative but their births are never mentioned; three infant siblings who died during protagonist's childhood are completely omitted
- Example fix: Add a paragraph noting when younger siblings were born and which ones died: "After him came more children. Keshava was born in 1085 and survived; Jīva came in 1087 and died before he could walk..."

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


### 2. Clarity and Comprehension (HIGH PRIORITY)

The reader should be able to follow the narrative without confusion. Flag:

**Confusing phrasing**
- Sentences that don't parse clearly on first read
- Ambiguous pronouns or references
- Actions where the mechanics are unclear (who did what, how)
- Example: "pressing the baby into the priest's hands and back again" — what is happening?
- Example: "grandma cup of tea" — what is going on here?
- Example: "apologized afterward" — for what exactly? (spending money on nights out? why apologize for that?)

**Missing context**
- Characters appearing without proper introduction
- Relationships not established before they matter (e.g., grandma's closeness to child should be shown before her death scene)
- Birth order unclear when relevant
- Household arrangements not explained (who lives where, why)
- Family members mentioned mid-narrative without earlier establishment (e.g., "His brother Yusuf" appearing without prior mention)

**Logical gaps**
- Unexplained transitions ("The household tried again" — what does this mean?)
- Cause and effect not connected ("apologized afterward" — for what exactly?)
- Events mentioned without showing how they were discovered or resolved
- Random topic shifts within paragraphs (e.g., transitioning from managing household to herb paste preferences without connection)
- Unclear information delivery (e.g., deaths years apart but ambiguous whether news was received separately or together)
- Housing/living situation changes appearing without context (e.g., "By the late 1890s they lived in a multi-family apartment" when reader doesn't know where they lived before)
- Fix by establishing the trajectory: "They had always lived in crowded housing—first X, then Y. By [date] they were in Z."

**Event logic unclear**
- Events that seem related but the connection isn't stated, or seem unrelated but are presented as connected
- The reader shouldn't have to guess how events relate to each other
- Example problem: Story depicts recurring stomach illness, then death from a different poisoning—are these connected or separate? Reader can't tell
- Example fix: Either connect them explicitly ("Years of illness had worn his body down; what might have passed became something he couldn't fight off") or make clear they're distinct incidents
- General rule: The narrative must make concrete choices and communicate them clearly

**Vague references**
- Phrases like "the settled side" or "service caste duties" that assume reader knowledge
- Social/economic arrangements mentioned but not explained
- Ambiguous relationship status: "entered a union" — are they married or not? Be specific
- Example fix: "service caste duties" → "The household belonged to a weaver caste, and Timma kept a loom"

### 3. Chronology and Time (HIGH PRIORITY)

**Temporal jumps**
- Jumping back and forth in time within paragraphs
- Example: "Between 2009 and 2011... By 2010... At fifteen (2010)" — confusing sequence

**Unnecessary repetition of time markers**
- Starting and ending a paragraph with the same date/month
- Example: "In July of 1005... He died on July 24" — redundant
- Too many year numbers clustered together, making narrative feel chronology-heavy

**Character introductions out of order**
- Mentioning someone in passing before properly introducing them
- Example: "her small son Isidro—born that same year" appearing mid-action scene

### 4. Anachronisms (HIGH PRIORITY)

Flag items that didn't exist in the time/place:
- Foods (chilies in 10th century India — they're from the Americas)
- Technologies
- Political terms or structures
- **Future events/people**: References to events, people, or developments that occurred after the character's death (MAJOR ISSUE - narratives must end at character's death)
- When uncertain, use web search to verify

### 5. Stylistic Issues

**Awkward phrases**
- "ran on energy and then wore down"
- "sex that year, private and practical"
- "shorter than most women her age would become" — awkward construction

**Run-on sentences**
- Long sentences that try to pack too much in
- Flag sentences that don't parse cleanly on first read

**Generic context-cramming openings**
- Opening sentences that try to establish too much context at once
- Example: "X was born in [place], in [political entity], where [language] and [religion] shaped daily life under [political system] and [economic system]"
- Fix by spreading context across shorter sentences, not deleting it. Keep the information but make it digestible

**Paragraphs that don't flow**
- Multiple unrelated topics crammed together
- Second half feels "tacked on" to first half
- Abrupt interludes that break narrative flow (e.g., literacy mentioned mid-childbearing discussion)
- Random topic shifts (e.g., managing a new wife in the household → not wanting to use a new herb paste — totally unconnected)

**Too many year numbers**
- Paragraphs cluttered with dates: "Between 2009 and 2011... By 2010... At fifteen (2010)"
- Repetition of same month at start and end of paragraph: "In July of 1005... He died on July 24"
- Too many "In [year]" sentence openings in a row
- Consider whether every date adds value or just clutters
- Fix by varying time markers: use ages ("At twenty"), relative time ("Four years later", "Two years later"), or milestone anchors ("After the marriage") instead of absolute years

**Artificial name patterns**
- All names following the same phonetic structure (all CVCV, all two syllables)
- Overly coincidental name pairs (Timma and Timmamma)

### 6. Metaphors and Figurative Language

The style should be plain, direct prose. Flag and rewrite:
- Metaphors and similes
- Poetic or purple prose descriptions
- Personification of abstractions

### 7. Pseudosociological Language

Avoid academic/anthropological jargon that sounds clinical. The word "kin" is almost always wrong:
- "kin camps" → "families"
- "kin" → "family" (in most contexts)
- "kin groups" → "their families" or "the families"
- "kin households" → "her sisters' households" or specific people
- "kinship network" → "relatives" or "family"
- "cooperation among kin" → name the specific people cooperating
- "Her kin washed her body" → "The women of the household washed her body" or name them
- "his kin wrapped him" → "his family wrapped him"

**How to check**: Search the narrative for "kin" - if found, replace with specific people or "family"

### 8. AI-Slop Phrases

Flag templated or meaning-making phrases:
- "rhythm of [X]"
- "settled into a pattern"
- "tightened around"
- "would prove to be"
- "little did [X] know"
- "shaped by" / "marked by" / "defined by" (when abstract)
- Abstract summaries like "death had shaped the household" (should be concrete)
- Pseudo-profound meaningless phrases like "like a fact that explained other facts"

### 9. Vague Hedging / LLM Indecision

Flag phrases where the LLM couldn't commit to a specific detail:
- "X or Y" constructions (e.g., "dyed wool or leather preservatives" → pick one: "leather tanning solution")
- "something like", "some kind of", "a type of"
- "perhaps", "likely", "may have" (narrator should be omniscient and confident)

Fix by picking one concrete option. If uncertain which is historically appropriate, use web search.

**Why this matters**: These hedges often slip past on first read because they sound reasonable. Train yourself to notice the "or" construction especially—it's a telltale sign the LLM was uncertain and refused to commit.

### 10. Political/Historical Claims

When a story mentions rulers, political situations, or historical events:
- If vague (e.g., "local rulers"), check if more specificity is possible for that time/place
- Some periods are genuinely murky (e.g., political collapses, contested frontiers) — vagueness is fine there
- Use web search to verify when uncertain

### 11. Repetitive Patterns and Checklist Feeling

Watch for the same phrases or structures appearing in multiple stories within a batch. These suggest generation templates leaking through.

**LLM checklist feeling**
- Stories that feel stilted, like the LLM was trying to tick off items from a checklist
- Mechanical inclusion of details without smooth integration into narrative flow
- Later paragraphs that read as "one event, then another event, then another" rather than flowing prose
- Example problem: "At eleven, X happened. At twelve, Y happened. At thirteen, Z happened."
- Example fix: Combine related events, show cause-and-effect, weave in character reactions and small pleasures alongside hardships
- The debug's `structured_incidents` are inputs the LLM must cover, but they should be integrated, not listed

### 12. Trait Visibility

For characters with extreme personality traits (below 10th or above 90th percentile) or physical attributes, check that these manifest in concrete actions or descriptions, not just implied.

### 13. Chronicle vs Scene (Long Lives)

Narratives for people who lived 50+ years should dwell on specific moments, not just list events chronologically. Flag if it reads like a timeline rather than a life.

### 14. Major Life Events Need Adequate Detail

Significant events—especially terminal illness, major injuries, or pivotal life changes—should not be compressed into a single vague sentence.

**Problem example**: "In 1911 pain began to hold him back from work. The illness was cancer, and it progressed quickly."

**Fix**: Show the progression with concrete physical details and timeline:
- "In 1911 pain settled into his gut and would not leave. At first he worked through it, bent a little at the waist, slower on his feet. By summer he could not eat without cramping, and his trousers hung loose. He kept going to the factory until the foreman sent him home because he could not stand a full shift. By autumn he spent most days on a pallet in their corner, knees drawn up against the pain."

The reader should feel the weight of these events, not just be told they happened.

---

## What NOT to Flag

- Omniscient narrator stating feelings, thoughts, preferences directly ("He liked X", "She hated Y") — this is correct
- Specific dates — these are generated by the system
- Named minor characters (midwives, healers, neighbors)
- Modern geographic terms for reader orientation
- Detailed scenes showing specific moments
