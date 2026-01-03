# Narrative Generation Issue Tracker

**Purpose**: Track recurring issues and patterns in generated narratives to inform prompt improvements and quality control.

**Review Process**: Stories in `_lives/` are systematically reviewed after each batch generation.

**Last Review**: Stories 0000-0036 (January 2026) - Full batch review

---

## Current Batch Summary (0000-0036)

**Overall quality**: Good. The narrative planning stage has resolved most major structural issues. Stories are chronologically coherent, siblings appear at correct ages, and extreme traits are generally visible.

### Strengths Observed
- Sibling timelines consistently correct (birth order, ages, deaths)
- Extreme personality traits visible through concrete action (e.g., Səm's very low agreeableness at 1st percentile shown through accusations and quarrels; Elisabetta's intellectual disability shown through learning by imitation)
- Mental disorders integrated into behavior (Dūno-rīgos's alcohol problem, Səm's depression, Elisabetta's intellectual disability)
- Good variety in grief responses across cultures and personalities
- Children appropriately integrated into narratives (not just listed)
- Spouses developed proportionally to narrative length

### Issues for Monitoring

**1. Occasional AI-slop phrasing (LOW PRIORITY)**
Some stories contain phrases that feel slightly templated:
- "The practical meaning for Elisabetta came in..." (0034)
- Occasional sociological framing ("shaped by wage work, church networks")
- "X's days settled into a pattern" type transitions

**2. Named deity specificity (LOW PRIORITY)**
Some religious references remain generic ("household rites to ancestors and local spirits") when specific deity names would be available for the culture/period.

**3. Modern living person (Fatima, 0035)**
The "alive" narrative format works well—appropriately brief, grounded in concrete present-tense details, ends with current moment rather than projecting forward.

---

## Resolved Issues

The following issues were addressed by implementing the **narrative planning stage** (`generate_narrative_plan()`) in generation.py:

### ✅ Sibling Temporal Logic (RESOLVED)
- **Previous issues**: 1, 2, 4, 34, 40, 46, 47, 48
- **Problem**: LLM failed to compute which siblings were older vs younger, which were alive at birth, correct sex ordering
- **Solution**: Narrative planning stage now computes sibling birth years, death years, and creates explicit timeline before narrative generation
- **Verification**: All 37 stories show correct sibling handling

### ✅ Chronological Sequencing (RESOLVED)
- **Previous issue**: 12
- **Problem**: Narrative went backward in time without signaling
- **Solution**: Narrative planning creates chronological life phases; narrative prompt instructs to follow the plan
- **Verification**: All reviewed stories maintain strict chronological order

### ✅ Extreme Personality Traits (RESOLVED)
- **Previous issues**: 11, 21, 37, 42
- **Problem**: Traits at extreme percentiles sometimes read as mild/moderate
- **Solution**: Added trait manifestation planning to narrative planning stage. Traits ≤5th or ≥95th percentile flagged as "must be visible" with required concrete behavioral scenes
- **Verification**: Strong examples in current batch (Səm's 1st percentile agreeableness, Elisabetta's 1st percentile intelligence, To's 0th percentile neuroticism)

### ✅ Mental Disorders Visibility (RESOLVED)
- **Previous issue**: 22
- **Problem**: Some disorders invisible in narrative despite being in metadata
- **Solution**: Mental disorders now explicitly flagged as "must be visible" in trait context, requiring specific scenes or behavioral patterns
- **Verification**: Well-handled in current batch (alcohol use disorders, depression, intellectual disability)

### ✅ Children Integration (RESOLVED)
- **Previous issues**: 8, 14, 24, 39
- **Status**: Resolved - surviving children get scenes; compressed handling of infant deaths is appropriate
- **Verification**: To's children woven throughout narrative, Elisabetta's children given individual attention

### ✅ Grief Variation (RESOLVED)
- **Previous issues**: 5, 13, 25, 38
- **Status**: Resolved - grief now varies by personality and situation
- **Examples**: To's drinking after losses, Səm's silence then eruption, Dūno-rīgos's drinking and quarrel after daughter's death

### ✅ Spouse Development (RESOLVED)
- **Previous issues**: 17, 26, 45
- **Status**: Resolved - spouses get adequate development
- **Examples**: Seko buffering To's unreliability, Rīna handling negotiations for Dūno-rīgos, Giovanni handling tenancy dealings for Elisabetta

### ✅ Siblings Vanish After Childhood (RESOLVED)
- **Previous issue**: 20
- **Status**: Resolved - narrative planning includes sibling prominence across life phases
- **Examples**: To's brother Men throughout adulthood, Dūno-rīgos's siblings (Branos, Katuros, Sena, Windo) appearing appropriately

---

## Low Priority (Style Polish)

**1. AI-slop phrasing**
- **Status**: Monitor in future batches
- **Patterns to avoid**:
  - "set the rhythm," "body began to betray him"
  - Abstract sociological framing ("The local order ran through...")
  - Weak transition phrases ("X's days settled into a pattern")
- **Fix**: Add banned phrases to prompt if patterns recur

**2. Generic religious references**
- **Status**: Monitor - may need prompt about naming specific deities
- **Pattern**: "household rites to ancestors and spirits" without deity names

**3. Vague quantities when data is available**
- **Pattern**: "kin," "a small number of children" when specifics are known
- **Fix**: Prompt instruction to be specific

---

## Implementation Status

### Completed
- [x] **Narrative planning stage** — Added `generate_narrative_plan()` to compute sibling/child timelines before narrative generation
- [x] **Year-range hedging fix** — Added prompt instruction: "Events happen at specific times. Do not spread events across year ranges"
- [x] **Trait manifestation planning** — Added `_build_trait_context()` and `_get_mental_disorder()` to flag extreme traits (≤5th/≥95th percentile) and mental disorders as "must be visible"; narrative plan now includes `trait_manifestations` section

### Remaining (by priority)

**Low Priority**
1. [ ] **Banned phrases** — Expand AVOID THESE PHRASES if patterns recur
2. [ ] **Named deities** — Add instruction to name specific deities where culturally appropriate
3. [ ] **Specificity** — Add instruction to use specific quantities when data available

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

