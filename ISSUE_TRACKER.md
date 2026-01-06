# Narrative Generation Issue Tracker

**Purpose**: Track recurring issues and patterns in generated narratives to inform prompt improvements and manual review.

**Last Review**: Stories 0000-0014 (January 2026)

---

## Review Process

Manual review in batches of 10-15 stories. For each batch, check:
1. **AI-slop phrases** - metaphors, meaning-making, banned phrases (see list below)
2. **Repetitive patterns** - same phrase appearing across multiple stories
3. **Political/historical vagueness** - claims that could be more specific for the time/place
4. **Trait visibility** - extreme personality/physical traits should show in action
5. **Chronicle vs scene** - long lives should dwell on moments, not just list events

Quick grep for worst offenders:
```bash
grep -Ei "rhythm of|tapestry|journey|testament to|would prove|little did|shaped by|marked by|cut deeper|filled quickly" _lives/*.md
```

---

## Current Issues

### High Priority

**1. Metaphors and figurative language**
The style guide calls for plain prose, but some metaphors slip through:
- "the loss cut away a thread that had held him to childhood" (0002-deva)
- "cut deeper" (0000-zhang-wei) — cliché
- "dark, wet sheen of birth" (0001-saraswati) — purple prose

**Action**: Flag and rewrite any metaphors, similes, or poetic descriptions.

### Medium Priority

**2. AI-slop phrasing**
Phrases that feel templated or reach for literary effect:
- "The house filled quickly" / "filled and emptied quickly" (appears in multiple stories)
- "X's days settled into a pattern"
- "Old age tightened around him"
- "The household reorganized under X's authority"
- "rhythm of [labor/seasons/life]"
- "death had shaped the household" — abstract, should be concrete

**Banned phrase patterns:**
- "rhythm of"
- "settled into a pattern"
- "tightened around"
- "filled quickly" / "filled and emptied"
- "cut deeper"
- "would prove to be"
- "little did [X] know"

**3. Political vagueness in contested periods**
Some stories use vague political descriptions when more specificity is possible:
- 1791 Raichur: "Deccan rulers" could specify Nizam Ali Khan of Hyderabad
- Some periods (e.g., 975 AD Western Ghats during Rashtrakuta collapse) are appropriately vague

**Action**: Web search to verify whether political specificity is possible for flagged stories.

### Low Priority

**4. Physical appearance extremes underutilized**
Characters with extreme height or attractiveness (≤5th or ≥95th percentile) sometimes lack concrete visible details.

**5. Infant death descriptions may become repetitive**
Current pattern: born → didn't nurse/breathe → quick death → wrapped → burial. Consider varying the specific cause and timeline.

**6. Chronicle tendency in longer lives**
Narratives for 60+ year lives sometimes read as event lists. Best moments are when prose lingers on specific scenes.

---

## Resolved Issues

(None currently tracked)

---

## Stories Reviewed

| Batch | Stories | Date | Issues Found |
|-------|---------|------|--------------|
| 1 | 0000-0014 | Jan 2026 | Minor: repeated phrases, one metaphor (0002), political vagueness (0001) |
