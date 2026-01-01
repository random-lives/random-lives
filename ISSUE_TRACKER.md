# Random Lives - Issue Tracker

This document tracks recurring issues and patterns found during narrative review, to inform future generation improvements.

## Status Key
- 🔴 **High Priority** - Should address before large-scale generation
- 🟡 **Medium Priority** - Improve when possible
- 🟢 **Low Priority** - Polish/refinement

---

## Current Issues (Batch 0000-0009, reviewed 2026-01-01)

### 🔴 HIGH PRIORITY

#### 1. Anachronistic Knowledge (Post-Death Events)
**Issue**: Narratives sometimes reference events that occurred after the person's death, breaking the temporal perspective. The omniscient narrator should only know facts up to the moment of death.

**Examples**:
- **Rudra** (died 971 AD, age 84): States his son Govinda "reached fifty" and sons Soma and Hari "lived to forty-five"—but these ages mean they outlived him by 5-10+ years
- The narrative perspective should be limited to what happened during the person's lifetime

**Fix**:
- For children/siblings: Only state ages at death if they died **before** or **during** the person's lifetime
- Use present-focused language: "Govinda, his eldest son, had grown strong and married" (shows status at time of death)
- Avoid: "X lived to age Y" when Y occurs after the person died
- Acceptable: "X died at age Y" only if that death occurred before the main character's death
- For living children at time of death: Describe their current state, not their future lifespans

**Affected narratives**: Rudra (clear violation), Ayyadurai (needs verification), Lataa (needs verification)

**Technical fix needed**: The narrative generation prompt should explicitly instruct the LLM to filter sibling/children ages and only mention deaths that occurred before the person's death date.

---

#### 2. Hedging Language ("about", "around")
**Issue**: Narratives frequently use hedging words like "about" and "around" for ages and timing, undermining the omniscient narrator voice.

**Examples**:
- "When Baska was about ten"
- "at about twenty-eight"
- "around thirty-four"

**Fix**: Either state ages directly (supported by the data) or use broader phrases like "in his early thirties" / "in his late twenties". Remove "about" and "around" entirely.

**Affected narratives**: Baska, Lataa, Rudra, Bhagavati, Rosa María, Ayyadurai

---

#### 2. Extreme Personality Traits / Mental Disorders Need Stronger Visibility
**Issue**: When personality traits are at 1st-5th or 95th-99th percentile (which appropriately indicates mental disorders), the manifestation in the narrative is sometimes too subtle. These are tail-end-of-distribution individuals whose traits should create consistent problems, be noticed by others, limit opportunities, and persist across life domains.

**Examples**:
- **Ayyadurai** (Intelligence 1%, Honesty-Humility 4%): Shows some cognitive limitation but could show him unable to learn tasks, getting cheated consistently, being known as untrustworthy
- **Rudra** (Conscientiousness 92%, Neuroticism 95%): Shows anxiety but 92nd percentile conscientiousness should show near-obsessive checking, routines, compulsive behaviors
- **Ghanshyam** (Separation anxiety): Could show more severe interference with daily functioning

**Fix**:
- Show disorders creating problems across multiple life domains
- Show others noticing/commenting/accommodating the behavior
- Show it limiting opportunities or shaping major outcomes
- Maintain persistence across the narrative

**Do NOT**: Anachronistically name disorders unless they were formally diagnosed in that era/context

**Affected narratives**: Ayyadurai, Rudra, Ghanshyam (partially Baska, though his social anxiety is well-shown)

---

### 🟡 MEDIUM PRIORITY

#### 3. Repetitive Phrasing Patterns
**Issue**: Certain constructions appear across multiple narratives, creating a formulaic feel.

**Common patterns**:
- **Death sequences**: "On [date], [name] died..." (appears in 8/10 narratives)
- **Authority formulations**: "Power/Authority in the [region] sat with [officials]..." (appears in 4/10)
- **Birth order**: "X was the [ordinal] child in a line/house of Y" (appears in 5/10)
- **Overused verbs**: "sat", "stood", "stayed" appear very frequently

**Fix**: Vary sentence structure and vocabulary. Break patterns before they become noticeable at scale.

**Examples of variation needed**:
- Death: Sometimes end before the death moment, sometimes describe aftermath, vary the final sentence structure
- Authority: Vary how political context is introduced (through a specific event, through father's role, through taxes/demands)
- Birth order: Mix up phrasing ("last child", "sixth of seven", "arrived when the household already held...")

---

#### 4. Structured Incident Integration
**Issue**: Most incidents integrate well, but some feel disconnected from the main narrative arc or don't ripple through later life when they logically should.

**Examples**:
- **Rudra**: Witnessed atrocity (raid, man cut down) at age 41-42 gets one paragraph but doesn't affect his later behavior/outlook
- Some brief incidents (theft, property crime) are mentioned but don't create lasting consequences

**Fix**: When a major incident occurs (especially violence, trauma, major loss), consider showing:
- Immediate behavioral changes
- Lasting effects on trust, relationships, or risk-taking
- How it shapes later decisions

**Note**: Not every incident needs to be life-changing, but witnessing extreme violence should probably register more than routine hardship.

---

#### 5. Length Consistency (Minor)
**Issue**: Some narratives exceed the suggested word counts (e.g., Rudra at 1,640 words for age 84 when guideline is 600-1000).

**Decision**: Lengths are generally acceptable despite not being exactly to spec. No action needed unless narratives regularly exceed 1,500+ words.

**Status**: Monitor but don't prioritize cutting

---

### 🟢 LOW PRIORITY

#### 6. Minor Character Naming Consistency
**Issue**: Slight inconsistency in when to name brief/one-off characters vs. leaving them unnamed.

**Examples**:
- Lataa names "Baqqalaa" (premarital partner) and "Galaanaa" (affair partner) who appear briefly
- Other narratives leave similar figures unnamed

**Fix**: Apply guideline more consistently: "Give names to recurring people; minor one-off figures can remain unnamed." If a person appears in only one scene/incident, consider leaving unnamed unless they're crucial to that scene's emotional weight.

---

#### 7. Opening Household Descriptions
**Issue**: Some narratives spend significant early paragraphs describing household composition in static terms before showing action.

**Example**: Rudra's opening describes grandmother, grandfather, mother, father, siblings' deaths in exposition before showing young Rudra doing anything.

**Fix**: Consider weaving household composition into action/scenes rather than front-loading it as exposition. Show people through what they do.

---

## Tracking Notes

### Batch Statistics (0000-0009)
- **Total narratives reviewed**: 10
- **Time periods**: 194 AD - 2020 AD (present)
- **Geographic distribution**: Italy (1), India (4), Colombia (1), Nigeria (1), Ethiopia (1), South Africa (1)
- **Age distribution**: infant (1), child 2-10 (2), adult 19-49 (3), elder 50+ (3), alive (1)
- **Mental disorders diagnosed**: 5/10 (social anxiety, depression, anxiety disorder x2, separation anxiety)
- **Word count range**: 160 (infant) to 1,640 (elder)

### Strengths to Maintain
✅ Plain prose style (no metaphors, similes, literary flourishes)
✅ Active, direct voice with variable rhythm
✅ Showing personality through action, not summary
✅ Historical/political grounding in opening paragraphs
✅ Age-appropriate narrative scaling
✅ Dignified treatment of infant deaths and brief lives
✅ Two-tier incident system creating diverse, plausible life events

---

## How to Use This Document

1. **Before generating new batch**: Review high-priority issues and update prompts/generation code as needed
2. **After reviewing new batch**: Add new patterns or update frequency counts
3. **Cross-batch tracking**: Note if issues are resolving or persisting across batches
4. **Prioritization**: Focus on high-priority issues that affect narrative quality at scale

---

## Update Log

- **2026-01-01**: Initial issue tracker created after review of batch 0000-0009
