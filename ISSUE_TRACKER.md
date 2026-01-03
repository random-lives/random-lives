# Narrative Generation Issue Tracker

**Purpose**: Track recurring issues and patterns in generated narratives to inform prompt improvements and quality control.

**Review Process**: Stories in `_lives/` are systematically reviewed after each batch generation.

**Last Review**: Stories 0000-0009 (January 2026) - Post narrative-planning implementation

---

## Resolved Issues

The following issues were addressed by implementing the **narrative planning stage** (`generate_narrative_plan()`) in generation.py:

### ✅ Sibling Temporal Logic (RESOLVED)
- **Previous issues**: 1, 2, 4, 34, 40, 46, 47, 48
- **Problem**: LLM failed to compute which siblings were older vs younger, which were alive at birth, correct sex ordering
- **Solution**: Narrative planning stage now computes sibling birth years, death years, and creates explicit timeline before narrative generation
- **Verification**: Stories 0000-0009 all show correct sibling handling

### ✅ Chronological Sequencing (RESOLVED)
- **Previous issue**: 12
- **Problem**: Narrative went backward in time without signaling
- **Solution**: Narrative planning creates chronological life phases; narrative prompt instructs to follow the plan
- **Verification**: All 10 reviewed stories maintain strict chronological order

---

## Remaining Issues

### High Priority (Core Features)

**1. Extreme personality traits inconsistently visible**
- **Previous issues**: 11, 21, 37, 42
- **Status**: IMPROVED but inconsistent
- **Problem**: Traits at extreme percentiles (0th, 1st, 6th, 15th, 98th) sometimes read as mild/moderate
- **Good example**: Story 0007 (Lataa) - 2nd percentile conscientiousness clearly shown through behavior
- **Bad example**: Story 0001 (Baska) - 0th percentile extraversion shows as mild shyness, 98th honesty-humility not demonstrated
- **Fix needed**: Strengthen prompt to require concrete scenes for extreme traits

**2. Mental disorders sometimes invisible**
- **Previous issue**: 22
- **Status**: PARTIALLY ADDRESSED
- **Problem**: Some disorders (depression) invisible while others (anxiety) are shown
- **Good example**: Story 0009 (Ghanshyam) - separation anxiety clearly visible
- **Bad example**: Story 0003 (Ayyadurai) - depression in metadata but not in narrative
- **Fix needed**: Same approach as personality traits - require demonstration

### ✅ Children Integration (RESOLVED)
- **Previous issues**: 8, 14, 24, 39
- **Status**: Resolved - surviving children now get scenes; compressed handling of infant deaths is appropriate
- **Examples**: Hinsa copying Baska's cane work, Kannan carried to the festival

### ✅ Grief Variation (RESOLVED)
- **Previous issues**: 5, 13, 25, 38
- **Status**: Resolved - grief now varies by personality and situation
- **Examples**: Baska's mother's clenched knuckles, Rosa María snapping at neighbors, Anna's mother keeping swaddling cloth, Jomi refusing food

### ✅ Spouse Development (RESOLVED)
- **Previous issues**: 17, 26, 45
- **Status**: Resolved - most spouses now get adequate development; some compression acceptable for long lives with much to cover
- **Examples**: Gauri's illness/death over multiple paragraphs, Jomi learning Baska's habits, Hirpha through affairs and final illness

### Low Priority (Style Polish)

**6. AI-slop phrasing and metaphors**
- **Previous issues**: 16, 23, 29, 31, 35, 36, 41, 43, 44
- **Status**: Monitor in future batches
- **Patterns to avoid**:
  - "set the rhythm," "body began to betray him," "news reached even the interior"
  - Abstract sociological framing ("The local order ran through...")
  - Weak transition phrases ("Rosa's days settled into a pattern")
- **Fix**: Add banned phrases to prompt if patterns recur

**7. Generic religious references**
- **Previous issues**: 32, 33
- **Status**: Monitor - may need prompt about naming specific deities

**8. Vague quantities when data is available**
- **Previous issues**: 10, 30
- **Pattern**: "kin," "a small number of children" when specifics are known
- **Fix**: Prompt instruction to be specific

**9. Formulaic time markers**
- **Previous issues**: 6, 7, 15, 28
- **Pattern**: Repetitive "In his late twenties," "When X was in his mid-thirties"
- **Fix**: Prompt instruction to vary time markers

**10. Siblings vanish after childhood**
- **Previous issue**: 20
- **Status**: IMPROVED - narrative planning includes sibling prominence across life phases
- **Pattern**: Was mentioning siblings in childhood, absent from adult narrative
- **Current**: Better in stories with explicit sibling planning (Baska, Rudra)

---

## Implementation Status

### Completed
- [x] **Narrative planning stage** — Added `generate_narrative_plan()` to compute sibling/child timelines before narrative generation
- [x] **Year-range hedging fix** — Added prompt instruction: "Events happen at specific times. Do not spread events across year ranges"

### Remaining (by priority)

**High Priority**
1. [ ] **Extreme trait flagging** — Flag traits below 10th or above 90th percentile; require concrete demonstration scenes

**Low Priority**
2. [ ] **Banned phrases** — Expand AVOID THESE PHRASES if patterns recur
3. [ ] **Named deities** — Add instruction to name specific deities where culturally appropriate
4. [ ] **Specificity** — Add instruction to use specific quantities when data available

---

## Notes for Future Reviews

When reviewing new batches, check:
1. Do siblings appear at correct ages with correct relationships?
2. Are extreme personality traits (below 10th / above 90th percentile) visible through action?
3. Are mental disorders demonstrated in behavior?
4. Are children woven into the narrative or listed as inventory?
5. Is grief varied by personality/culture, or defaulting to stoicism?
6. Do spouses get proportional development?
7. Any new AI-slop phrases to add to banned list?

