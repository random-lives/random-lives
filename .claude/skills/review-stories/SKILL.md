---
name: review-stories
description: Review a story for potential issues. Use when asked to check a story for issues
---

# Story Review Workflow

Review stories in `_lives/` or `_lives_pending/` through sequential focused passes. Each pass addresses ONE type of issue—find problems, fix them, then move to the next pass.

**CRITICAL**: Complete all passes for ONE story before moving to the next.

---

## Pass 1: Family & Relationship Plausibility

Read the debug data first to understand:
- Who are the caretakers, siblings, children?
- What is the household structure? (fostered out? living with extended family?)
- What relationships should be close vs. distant?

Then read the narrative asking:
- **Does closeness match circumstances?** A fostered-out child shouldn't be coordinating care for birth family. Siblings who live nearby should be known well.
- **Are in-laws and extended family handled?** If protagonist moved to spouse's area, in-laws should appear.
- **Who is this person?** Every character who matters should have a clear relationship stated.
- **Do emotional reactions match relationships?** Close relationships need visible grief at death; distant ones don't need much.

**Character introduction check (do this explicitly):**
- List every named character in order of first appearance
- For each: is their relationship to protagonist clear on or before first mention?
- If someone appears acting with the protagonist (following, helping, arguing with), they must be introduced BEFORE that scene
- Siblings especially: introduce all living siblings together early, not one-by-one as they become relevant

Fix issues before moving on.

---

## Pass 2: Death Handling

Check debug data for every person with a `death_year` during the protagonist's lifetime.

For each death:
1. **Is it mentioned?** If not, and it would add to the story, add it.
2. **Does it land with appropriate weight?** A spouse's death shouldn't be one sentence. A distant sibling can be brief.
3. **Is the timing right?** Deaths of siblings before protagonist's birth shouldn't be described as remembered. Deaths during protagonist's childhood shouldn't have impossible specificity.
4. **Does the protagonist react?** If they were close to someone, show the reaction—don't just move on.

Also check: after adding a death, make sure the character isn't referenced as alive later.

Fix issues before moving on.

---

## Pass 3: Narrative & Thematic Coherence

Read the whole narrative asking:
- **Do threads connect?** If something is set up early, does it pay off? If a trait or relationship matters, is it consistent throughout?
- **Is causality clear?** When events happen, is it clear why? Don't leave the reader guessing how things connect.
- **Are themes followed through?** Are the arcs within the person's life (changes in status, family arrangements, relationships with others, etc) clear?
- **Do major characters remain present?** Spouses, close siblings, and children who are important early should either die (visibly) or still appear later. A spouse who disappears after a conflict needs resolution—did they leave, reconcile, or are they present at death?

Fix issues before moving on.

---

## Pass 4: Event Weight & Pacing

Read each significant event asking:
- **Does it get enough space?** Affairs, violence, major losses should have setup, the event itself, and aftermath. If an event is mentioned in one sentence but has lasting consequences, it needs expansion.
- **Could a reader understand how this happened?** Don't just state that something occurred—show enough that it makes sense.
- **Are transitions earned?** When relationships change (marriage sours, siblings become distant), is the change shown through specific moments, or just stated?

**Antagonists and secondary characters:**
- Anyone the protagonist conflicts with needs context: who are they, what's the history?
- Don't just check family—check rivals, neighbors, authority figures

Fix issues before moving on.

---

## Pass 5: Paragraph Coherence

Read each paragraph asking:
- **Does this paragraph have ONE theme?** A paragraph about thefts shouldn't also handle a funeral. A paragraph about a death shouldn't randomly include an unrelated event.
- **Should events be bundled?** Multiple similar events (thefts, illnesses, minor incidents) can often be combined into one paragraph rather than scattered.
- **Should events be separated?** Major events deserve their own space—don't cram a spouse's death into a paragraph about something else.
- **Is there random topic-jumping?** Each paragraph should flow internally; things shouldn't be "thrown in" at the end.

Fix issues before moving on.

---

## Pass 6: Chronology & Time Gaps

Map out the timeline, then check:
- **Are there unexplained gaps?** Skipping many years without acknowledgment is a problem. Either add content or bridge explicitly.
- **Does time flow forward?** Jumping back and forth within paragraphs is confusing, as is paragraphs out of chronological order.
- **Are time markers varied?** Too many "In [year]" openings in a row. Mix in ages, relative time, milestone anchors.
- **Is precision appropriate?** Vague decade references for single events are sloppy—give the year or don't bother. But vague ranges are fine for patterns spanning years.
- **Are there logical impossibilities?** Events placed before they could occur.

**Duplicate temporal markers (fix each one as you find it):**
- Sentences with both a year AND an age are redundant—pick one
- "At thirty-two, in 1411" → "In 1411" or "At thirty-two"
- "In 1425, at forty-six" → pick one

**Weird date ranges:**
- Constructions like "in 1415 and 1416" for what reads like a single period are LLM hedging
- Pick one year, or describe the span naturally ("over the following year")

Fix issues before moving on.

---

## Pass 7: Vagueness & Specificity

Look for places where the narrative is vague when it should be concrete:

**Opening sentences:**
- Check paragraph openers for vague/filler phrases: "Deaths came early," "Life was hard," "Times were difficult," "Things changed"
- These signal the paragraph lacks a concrete anchor—rewrite or cut

**Work situations:**
- "What work was she doing and for whom?" should be answerable

**Unspecified relations or characters:**
- Don't leave actors vague—specify their relationship
- "a sick adult relative" → who specifically?
- "others suggested" → who?
- Add a name if the person recurs

**Vague group references:**
- "X's kin/family/people" when a specific relation would work better

**Hedging language:**
- "perhaps," "likely," "may have"—the narrator is omniscient, be confident

**LLM indecision:**
- "X or Y" constructions—pick one

**Sloppy placeholders:**
- "steady reference points," "the usual patterns"—what specifically?

**Abstract metaphors (apply the deletion test):**
- For any metaphor or abstraction ("shield," "anchor," "weight"), ask: what is this actually pointing at?
- If you delete the sentence, does the reader lose concrete information?
- If no: cut it
- If yes: replace the abstraction with the concrete thing

Fix issues before moving on.

---

## Pass 8: Surface Patterns

Search for and fix these specific patterns:

**Pseudosociological jargon:**
- "kin" → "family" or name the specific people
- "stem family," "joint household," "patrilocal" → describe concretely who lives there
- "nuclear" → avoid; just describe the household

**Naming issues:**
- Same name used for different people (confusing)
- Siblings referred to as "Last First" when just "First" works
- All names following same phonetic pattern (artificial)

**Figurative language:**
- Metaphors, similes, poetic flourishes → rewrite as plain prose
- "beads that looked like water" → "blue glass beads"

**AI-slop phrases:**
- "rhythm of [X]," "settled into a pattern," "would prove to be"
- "shaped by," "marked by," "defined by" (when abstract)
- "Deaths came early," "Life was [adjective]," "Times were [adjective]"

**Run-on sentences:**
- Long sentences packing too much in—break them up

**Sentence-level awkwardness:**
- Parallelism problems ("He did not." after "He wasn't.")
- Phrases that don't parse cleanly

Fix issues before moving on.

---

## Pass 9: Final Read

Read the story once more as a reader would:
- Does it flow?
- Is anything still confusing?
- Does it feel like a life, not a timeline?
- Can you track who everyone is?

Make final adjustments.

---

## Logging

After completing all passes, update the bottom of the story with a change-log, eg:

```markdown
**Issues found:**
- [Pass 1] "Stem family" jargon in paragraph 2
- [Pass 2] Younger brother's death followed by famine mention with no clear connection
- [Pass 5] Grandfather's death and cough return crammed into same paragraph

**Changes made:**
- Replaced "stem family" with concrete description of household
- Clarified connection between brother's death and subsequent events
- Split paragraph to give grandfather's death appropriate weight
```

---

## Starting

If no specific story is requested, ask which story to review or offer to start from the first pending story.
