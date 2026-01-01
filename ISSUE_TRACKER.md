# Random Lives - Issue Tracker

This document tracks recurring issues and patterns found during narrative review, to inform future generation improvements.

## Status Key
- 🔴 **High Priority** - Should address before large-scale generation
- 🟡 **Medium Priority** - Improve when possible
- 🟢 **Low Priority** - Polish/refinement

---

## Current Issues (Batch 0000-0039, reviewed 2026-01-01)

### 🔴 HIGH PRIORITY

#### 1. Anachronistic Knowledge (Post-Death Events)
**Issue**: Narratives sometimes reference events that occurred after the person's death, breaking the temporal perspective. The omniscient narrator should only know facts up to the moment of death.

**Examples**:
- **Rudra** (0002, died 971 AD, age 84): States his son Govinda "reached fifty" and sons Soma and Hari "lived to forty-five"—but these ages mean they outlived him by 5-10+ years
- **Gao Shunmin** (0021, died 1159 AD, age 51): States three sons "lived into solid adulthood" reaching ages 45-50, but the debug data shows one child died at 68 (after father's death). The narrative appears to be **fabricating or inferring data** not provided, not just mentioning post-death events.
- The narrative perspective should be limited to what happened during the person's lifetime

**Fix**:
- For children/siblings: Only state ages at death if they died **before** or **during** the person's lifetime
- Use present-focused language: "Govinda, his eldest son, had grown strong and married" (shows status at time of death)
- Avoid: "X lived to age Y" when Y occurs after the person died
- Acceptable: "X died at age Y" only if that death occurred before the main character's death
- For living children at time of death: Describe their current state, not their future lifespans

**Frequency in sample**: At least 2 confirmed cases in 40 narratives (5% rate)

**Affected narratives**:
- 0002-rudra.md (clear violation)
- 0021-高顺民.md (clear violation, possibly with data fabrication)

**Technical fix needed**: The narrative generation prompt should explicitly instruct the LLM to filter sibling/children ages and only mention deaths that occurred before the person's death date.

---

#### 2. Hedging Language ("about", "around")
**Issue**: Narratives sometimes use hedging words like "about" and "around" for ages and timing, undermining the omniscient narrator voice.

**Examples from first 10**:
- "When Baska was about ten" (0001)
- "at about twenty-eight" (0007)
- "around thirty-four" (multiple)

**Status after larger sample**: Much improved but still appears occasionally (e.g., Kaeo: "When Kaeo was about sixteen")

**Frequency**: Lower than first 10 suggested; appears in ~15-20% of narratives

**Fix**: Either state ages directly (supported by the data) or use broader phrases like "in his early thirties" / "in his late twenties". Remove "about" and "around" entirely.

---

#### 3. Extreme Personality Traits / Mental Disorders Need Stronger Visibility
**Issue**: When personality traits are at 1st-5th or 95th-99th percentile (which appropriately indicates mental disorders), the manifestation in the narrative is sometimes too subtle. These are tail-end-of-distribution individuals whose traits should create consistent problems, be noticed by others, limit opportunities, and persist across life domains.

**Status after larger sample**: Mixed. Some narratives handle this excellently, others remain too subtle.

**Excellent examples** (maintain this standard):
- **Buru** (0014): Agreeableness 8%, Extraversion 0%, Intelligence 100% - all show vividly through behavior across the narrative
- **Mykola** (0023): Intelligence 1% shown thoroughly through struggles with reading, instructions, and adaptive functioning
- **Ashen** (0035): Neuroticism 99% manifests powerfully through physical symptoms, rumination, workplace explosion
- **Nubia** (0034): Conscientiousness 99% shows through meticulous work habits across decades

**Still too subtle**:
- **Ayyadurai** (0003): Intelligence 1%, Honesty-Humility 4% - shows some limitation but could be stronger
- **Rudra** (0002): Conscientiousness 92% less visible than his neuroticism
- **Ghanshyam** (0009): Separation anxiety could show more functional impairment

**Fix**:
- Show disorders creating problems across multiple life domains
- Show others noticing/commenting/accommodating the behavior
- Show it limiting opportunities or shaping major outcomes
- Maintain persistence across the narrative

**Do NOT**: Anachronistically name disorders unless they were formally diagnosed in that era/context

---

### 🟡 MEDIUM PRIORITY

#### 4. Repetitive Phrasing Patterns
**Issue**: Certain constructions appear across multiple narratives, creating a formulaic feel.

**Common patterns confirmed in larger sample**:
- **Death sequences**: "On [date], [name] died..." or "[Name] died on [date]" (very common pattern)
- **Authority formulations**: "Power/Authority/No king sat with [officials]..." appears frequently in opening paragraphs
  - Examples: "No king ruled there" (Okechukwu 0037), "Authority sat with..." (multiple), "Power in the [region] sat with..." (multiple)
- **Birth order**: "X was the [ordinal] child" formulations are common
- **Overused verbs**: "sat", "stood", "stayed" appear very frequently
- **Household entry**: "He/She entered a household..." opening pattern

**Fix**: Vary sentence structure and vocabulary. Break patterns before they become noticeable at scale.

**Examples of variation needed**:
- Death: Sometimes end before the death moment, sometimes describe aftermath, vary the final sentence structure
- Authority: Vary how political context is introduced (through a specific event, through father's role, through taxes/demands)
- Birth order: Mix up phrasing ("last child", "sixth of seven", "arrived when the household already held...")

---

#### 5. Structured Incident Integration
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

#### 6. Length Consistency (Minor)
**Issue**: Some narratives exceed the suggested word counts (e.g., Rudra at 1,640 words for age 84 when guideline is 600-1000).

**Decision**: Lengths are generally acceptable despite not being exactly to spec. No action needed unless narratives regularly exceed 1,500+ words.

**Status**: Monitor but don't prioritize cutting

---

### 🟢 LOW PRIORITY

#### 7. Minor Character Naming Consistency
**Issue**: Slight inconsistency in when to name brief/one-off characters vs. leaving them unnamed.

**Examples**:
- **Lataa** (0007): Names "Baqqalaa" (premarital partner) and "Galaanaa" (affair partner) who appear briefly
- **Leubawinjō** (0020, newborn, 2 days old): Names father Wulfaharduz, mother Frijōsunnjō, half-sister Hildigō, dead half-brother Sīgiz—excessive for a 2-day life
- Other narratives leave similar figures unnamed

**Fix**: Apply guideline more consistently: "Give names to recurring people; minor one-off figures can remain unnamed." For very brief lives (especially infants), limit naming to immediate parents. If a person appears in only one scene/incident, consider leaving unnamed unless they're crucial to that scene's emotional weight.

---

#### 8. Opening Household Descriptions
**Issue**: Some narratives spend significant early paragraphs describing household composition in static terms before showing action.

**Example**: Rudra's opening describes grandmother, grandfather, mother, father, siblings' deaths in exposition before showing young Rudra doing anything.

**Fix**: Consider weaving household composition into action/scenes rather than front-loading it as exposition. Show people through what they do.

---

## Tracking Notes

### Batch Statistics

**Sample 0000-0009 (first 10)**:
- **Time periods**: 194 AD - 2020 AD (present)
- **Geographic distribution**: Italy (1), India (4), Colombia (1), Nigeria (1), Ethiopia (1), South Africa (1)
- **Age distribution**: infant (1), child 2-10 (2), adult 19-49 (3), elder 50+ (3), alive (1)
- **Mental disorders diagnosed**: 5/10 (social anxiety, depression, anxiety disorder x2, separation anxiety)
- **Word count range**: 160 (infant) to 1,640 (elder)

**Sample 0000-0039 (40 total, 12 read in detail)**:
- **Time periods**: 925 BC - 2025 AD (present)
- **Geographic span**: All continents represented (Asia heavily weighted, as expected)
- **Notable contemporary lives**: 3 living people (2020-present) with excellent quality
- **Personality extremes**: Mixed quality—some excellent (Buru, Mykola, Ashen, Nubia), some too subtle (Ayyadurai, Rudra's conscientiousness)
- **Critical issue frequency**: Post-death events in ~5% of narratives (2/40 confirmed)

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

- **2026-01-01 (initial)**: Issue tracker created after review of batch 0000-0009
- **2026-01-01 (update)**: Reviewed larger sample 0000-0039 (40 stories, 12 read in detail). Key findings:
  - Post-death event issue persists (~5% rate, 2/40 confirmed)
  - Hedging language much improved vs. initial impression
  - Personality manifestation quality is mixed but includes excellent examples
  - Repetitive phrasing patterns confirmed at scale
  - Contemporary narratives (2020s) are particularly strong
