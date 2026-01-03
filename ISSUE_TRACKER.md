# Narrative Generation Issue Tracker

**Purpose**: Track recurring issues and patterns in generated narratives to inform prompt improvements and quality control.

**Last Review**: Stories 0000-0036 (January 2026)

---

## Current Issues

### Medium Priority

**1. "In [YEAR]..." sentence pattern**
Almost every narrative relies heavily on "In [YEAR], [event]" to introduce new paragraphs or time shifts. This creates a formulaic, list-like feel rather than flowing prose.
- Examples: "In 273 BC...", "In 1802...", "In 1131..." appearing at paragraph starts throughout
- Affects all 5 reviewed stories (0000-0004)
- **Fix needed**: Add instruction to vary time shift introductions—use age references, seasonal markers, life stage transitions, or integrate dates mid-sentence

### Low Priority

**2. AI-slop phrasing**
Some stories contain phrases that feel slightly templated:
- "The practical meaning for Elisabetta came in..." (0034)
- Occasional sociological framing ("shaped by wage work, church networks")
- "X's days settled into a pattern" type transitions
- "ploughed as if he could carve his thoughts into the earth" (0000) - borderline figurative

**3. Generic religious references**
Some religious references remain generic ("household rites to ancestors and local spirits") when specific deity names would be available for the culture/period.

---

## Implementation Status

### Remaining

**Medium Priority**
1. [ ] **Time shift variety** — Add instruction to vary how time shifts are introduced (avoid "In [YEAR]..." pattern)

**Low Priority**
2. [ ] **Banned phrases** — Expand AVOID THESE PHRASES if patterns recur
3. [ ] **Named deities** — Add instruction to name specific deities where culturally appropriate

---

## Notes for Future Reviews

When reviewing new batches, check:
1. Are extreme personality traits (below 10th / above 90th percentile) visible through action?
2. Are mental disorders demonstrated in behavior?
3. Any new AI-slop phrases to add to banned list?
4. Are time shifts varied, or dominated by "In [YEAR]..." pattern?
