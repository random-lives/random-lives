# Narrative Generation Issue Tracker

**Purpose**: Track recurring issues and patterns in generated narratives to inform prompt improvements and quality control.

**Last Review**: Stories 0024-0029 (January 2026)

---

## Current Issues

### Medium Priority

**1. AI-slop phrasing**
Some stories contain phrases that feel templated or reach for literary effect:
- "Old age tightened around him" (0024) — figurative
- "The household reorganized under X's authority" — administrative
- "His mind wandered more after the head injury" — could be shown more concretely
- "Chronic illness wasted him" — generic
- "X's days settled into a pattern" type transitions

**Candidate banned phrases:**
- "reorganized under [X's] authority"
- "tightened around him/her"
- "settled into a pattern"
- "the practical meaning for X came in..."

### Low Priority

**2. Physical appearance extremes underutilized**
Characters with extreme height or attractiveness percentiles (≤5th or ≥95th) rarely have specific visible details in the narrative. Kumara (1st percentile attractiveness) is mentioned as "mocked for his face/skin" but without concrete description. Peldzom (89th percentile attractiveness) has no visible manifestation.

**3. Infant death descriptions may become repetitive across corpus**
Current pattern: born → visible issue/didn't nurse → quick death → wrapped → burial. Historically accurate but risks feeling formulaic at scale. Consider varying: stillbirth, fever after days, refused milk, breathing difficulties, etc.

**4. Chronicle tendency in longer lives**
Some narratives for long-lived people (60+ years) read as event lists rather than dwelling on scenes. The strongest moments are when the prose lingers (Peldzom arguing about butter, Pachompsais sorting tools). Consider prompting for 2-3 "dwelling" moments per adult narrative.

---

## Resolved Issues

(None currently tracked)

---

## Notes for Future Reviews

When reviewing new batches, check:
1. Are extreme personality traits (below 10th / above 90th percentile) visible through action?
2. Are mental disorders demonstrated in behavior?
3. Any new AI-slop phrases to add to banned list?
4. For long lives: does the narrative dwell on specific scenes or just list events?
5. For extreme physical attributes: is there at least one concrete detail?
