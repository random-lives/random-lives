# Known bugs

Documented bugs in the generation pipeline and content that are understood but not yet fixed in code. Each entry records the symptom, the mechanism, the scope across existing stories, and how affected stories were handled.

*Last updated 2026-06-29.*

---

## 1. Implausible sibling birth years ("ancestor-aged siblings")

**Status:** Documented, not fixed in the pipeline. Affected existing stories corrected in prose; debug data left as the raw generation artifact with a correcting note in each file.

**Symptom.** Some stories list "siblings" born many decades before the protagonist — in the worst case 79 years before — implying one mother bore children across a 40-to-79-year span. That is biologically impossible. The reported example was [0139-sin-uballit](_lives/0139-sin-uballit.md), where two "sisters" were born 43 and 36 years before the protagonist.

**Mechanism.** In `generate_narrative_plan()` ([generation.py](generating_code/generation.py)), the model assigns each sibling a `death_year` (often near the protagonist's own lifetime, so the sibling "exits" the story) and an independent `death_age`. The birth year is effectively `death_year − death_age`. Nothing constrains that birth year to a plausible maternal childbearing window (mother roughly aged 15–45 at each birth, all children within a ~25–30-year span). When the model picks a large `death_age` for a sibling who dies near the protagonist's lifetime, the back-computed birth year lands decades before the protagonist. The result is an elderly person mislabeled as a sibling.

**A second-order effect: the review process propagated it.** The `review-stories` workflow tells reviewers to reconcile the narrative prose *to* the structured `narrative_plan` data. In 0139 a reviewer did exactly that — the original prose had the sisters as plausible children (aged 14 and 8), and the reviewer "corrected" their ages *up* to 42 and 35 to match the buggy debug data, turning an internal inconsistency into a chronological impossibility visible to readers. Reviewers should sanity-check sibling birth years against biology before trusting them. See the note added to [.claude/skills/review-stories.md](.claude/skills/review-stories.md).

**The realistic ceiling.** An older sibling of a newborn protagonist can be at most about **40 years older**, and only as a half-sibling via the father (the father sires the older child young and the protagonist around 60). Full siblings, and maternal half-siblings (same mother, different fathers), cap lower — roughly **25–30 years**, since the mother must still be ≤45 when she bears the protagonist. A "from his father's first marriage" or "born to different fathers" recast does **not** rescue an arbitrarily large gap: a 59-to-79-year gap implies a father in his 80s-to-100s, or (for shared-mother half-siblings) the impossible maternal span again.

**Scope.** A scan of all 250 stories' structured data flagged **17 stories** with an implausible maternal window (a sibling born ≥22 years from the protagonist, or a >30-year span across all children). A read of each narrative classified how reader-facing each one is:

- **Corrected in prose (7 stories):**
  - `0139-sin-uballit`, `0231-unnamed-infant` — same birth mother, and the implausibly-old sibling's numeric *age* was stated (a 42- and 45-year-old child coexisting with the mother's newborn). Ages reduced to plausible values.
  - `0055-asha` — the siblings' birth *years* were stated in prose (20/16/10 BC against the protagonist's 14 AD), so a reader could compute a ~33-year maternal span. Birth years compressed to a ~19-year window.
  - `0031-eirēnē`, `0063-felipe`, `0126-kanu` — these had been "fixed" in earlier review by recasting the much-older sibling as a half-sibling (father's first marriage, or "different fathers"), but the recast left the implied parent age impossible (father ~80–100, or the shared-mother span). Ages reduced to the realistic ceiling above; the half-sibling framing kept where it now works.
  - `0133-phuntsok` — no numeric age stated, but "three adult siblings" spanning 40 years asserted an impossible relationship; reworded to "three older members of the household" (a stem household plausibly includes uncles, aunts, and older cousins).
- **Data-only, prose genuinely sound (10 stories):** `0017`, `0042`, `0046`, `0062`, `0108`, `0144`, `0200`, `0219`, `0224`, `0240`. The bad birth years live only in the debug comments; the prose either omits the sibling's age or states a plausible one (an older sibling of ~24 with a mother of ~40 is realistic and was left alone). Each carries a documenting note.
- **False alarm:** `0094-lin-xin` (the scanner's YAML parser tripped on a colon in a role string; the only sibling is 7 years older — no bug).

**Fix if revisited in code.** Constrain sibling birth years in `generate_narrative_plan()` to a plausible window: pick the mother's age at each birth in ~15–45 and within a ~25–30-year span across all her children, or sample the sibling's birth year directly relative to the protagonist's rather than back-computing it from an unconstrained `death_age`. Half-siblings via the father can legitimately fall outside the maternal window, so any such constraint should allow an explicit half-sibling flag.

**Audit artifact:** [research/sibling-chronology-audit.md](research/sibling-chronology-audit.md) (per-story classification with offending quotes); scan script in the session scratchpad.
