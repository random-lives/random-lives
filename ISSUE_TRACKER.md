# Narrative Generation Issue Tracker

**Purpose**: Track recurring issues and patterns in generated narratives to inform prompt improvements and quality control.

**Last Review**: Stories 0000-0009 (January 2026)

---

## Current Issues

### Low Priority

**1. AI-slop phrasing**
Some stories contain phrases that feel slightly templated:
- "The practical meaning for Elisabetta came in..." (0034)
- Occasional sociological framing ("shaped by wage work, church networks")
- "X's days settled into a pattern" type transitions
- "ploughed as if he could carve his thoughts into the earth" (0000) - borderline figurative

**2. Generic religious references**
Some religious references remain generic ("household rites to ancestors and local spirits") when specific deity names would be available for the culture/period.

---

## Resolved Issues

**1. "In [YEAR]..." sentence pattern** ✓ (January 2026)
Previously, narratives relied heavily on "In [YEAR], [event]" to introduce paragraphs. Added prompt instructions to vary time transitions. Latest batch (0000-0009) shows good variety: age references, seasonal markers, life events, relative time.

---

## Implementation Status

### Completed

1. [x] **Time shift variety** — Added instruction to vary how time shifts are introduced (avoid "In [YEAR]..." pattern)

### Remaining

**Low Priority**
1. [ ] **Banned phrases** — Expand AVOID THESE PHRASES if patterns recur
2. [ ] **Named deities** — Add instruction to name specific deities where culturally appropriate

---

## Notes for Future Reviews

When reviewing new batches, check:
1. Are extreme personality traits (below 10th / above 90th percentile) visible through action?
2. Are mental disorders demonstrated in behavior?
3. Any new AI-slop phrases to add to banned list?
4. Are time shifts varied? (Should now be resolved)
