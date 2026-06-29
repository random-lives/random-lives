# Sibling chronology audit

*Created 2026-06-29 07:45.*

## TL;DR

Audited 18 stories (17 from `_sibling_candidates.json` + manually-inspected `0094-lin-xin.md`) for the "implausible-sibling" bug, where the generation pipeline back-computed a sibling birth year outside any plausible maternal childbearing window. The reader-facing question is whether such a sibling appears in the **prose** in a way a reader would find chronologically impossible.

- **VISIBLE-BUG: 2** — `0139-sin-uballit.md`, `0231-unnamed-infant.md`
- **DATA-ONLY: 15** — `0017`, `0031`, `0042`, `0046`, `0055`, `0062`, `0063`, `0108`, `0126`, `0133`, `0144`, `0200`, `0219`, `0224`, `0240`
- **OK: 1** — `0094-lin-xin.md` (parser failure was a false alarm; sibling is only 7 years older — no bug at all)

**Key pattern.** Most flagged stories were already fixed in post-generation review using one of two strategies, both of which the reviewer applied deliberately (visible in the changelogs):
1. **Recast as half-sibling** ("son from his first marriage", "born to different fathers in earlier years") — explains the gap and dodges the impossible-maternal-age problem. Used in 0031, 0063, 0126.
2. **Restate the age downward** to a plausible number, dropping the buggy `birth_year`/`death_age` ("now twenty-four", "fourteen"). Used in 0042, 0200.

The 2 VISIBLE-BUG cases are exactly where neither strategy was applied: the prose keeps the same birth mother **and** states the implausibly-old sibling's age numerically, so a reader can do the arithmetic and see a 40-to-45-year-old child coexisting with the mother's newborn.

One ambiguous near-miss is flagged in detail: **0133-phuntsok** (65-year-old "brother"). It stays DATA-ONLY only because the prose never states his numeric age and the mother's age is never given.

## Summary table

| File | worst_gap | Classification | Offending quote / note |
|---|---|---|---|
| 0017-unnamed-infant | -25 | DATA-ONLY | Da-lang (born 500, 25y before) correctly handled as deceased: "had died the previous year at twenty-four". Other sibs plausible. |
| 0031-eirēnē | -59 | DATA-ONLY | Dionysios (born 63 BC) recast as half-brother: "Menedēmos's son from his first marriage, nearly sixty now". Plausible, deliberate fix. |
| 0042-alo | -22 | DATA-ONLY | Lia born 22y before but prose says "now twenty-one" (21yo, plausible older sister). Gap marginally within window. |
| 0046-walwata | -22 | DATA-ONLY | worst_gap sib is an infant death (Tarpawi). Long-lived brothers born 14–18y before — plausible. Prose ages all fine. |
| 0055-asha | -34 | DATA-ONLY | Sumi born 20 BC (33 at birth). Prose depicts her as adult helper at plausible age; mother's implausible age not surfaced. |
| 0062-kanu | -22 | DATA-ONLY | Darol born 22y before (plausible older brother). Data death_year contradicts prose, but prose itself is internally plausible. |
| 0063-felipe | -79 | DATA-ONLY | Juan/Antonio recast as "much older half-brothers from his father's first marriage... both old men". Father's age not stated; deliberate fix. |
| 0108-sina | -24 | DATA-ONLY | worst_gap sib is infant Aka. Older sibs born 15–21y before, plausible. Prose: "both young women". Fine. |
| 0126-kanu | -51 | DATA-ONLY | Sali/Mina recast as half-sisters "born to different fathers in earlier years", aged "nearly forty" and "past thirty". Mother's implausible age not surfaced. |
| 0133-phuntsok | -65 | DATA-ONLY (ambiguous) | Tsering born 1803 = 65 at birth, called full "sibling"/"the oldest... an elder herdsman". NO numeric age stated; mother's age not given. Borderline — see detail. |
| 0144-yin-niang | -22 | DATA-ONLY | Older brothers born 16–22y before, all plausible. Effectively OK. |
| 0139-sin-uballit | -43 | **VISIBLE-BUG** | "Their first child, Amat-Sîn, was now forty-two..."; protagonist "the long-awaited heir after decades of only daughters". Same mother births newborn — impossible. |
| 0200-kira | -24 | DATA-ONLY | Tali born 24y before (data) but prose states age "fourteen". Understated to plausible. |
| 0219-unnamed-infant | -24 | DATA-ONLY | Da-niang "twenty-four that year" — plausible eldest sister. Fine. |
| 0224-salma | -33 | DATA-ONLY | worst_gap sib is infant Yusuf. Ibrahim born 27y before = plausible "working man". Fine. |
| 0231-unnamed-infant | -45 | **VISIBLE-BUG** | "a woman raising children without a resident husband. Her eldest, Koro, had been born forty-five rains earlier" — then "A boy was born, her third child". 45yo son + newborn from same mother. |
| 0240-sana | -22 | DATA-ONLY | Korit born 22y before, "over twenty years older" — plausible older brother. Fine. |
| 0094-lin-xin | (n/a) | **OK** | Parser failure (colon in role string). Only sibling Lin Bao born 45 AD, 7y before protagonist (52 AD). "seven years his senior". No bug. |

## Detail: VISIBLE-BUG cases

### 0139-sin-uballit.md — VISIBLE-BUG
- **Bad siblings:** Amat-Sîn (`birth_year` -532, i.e. 43y before protagonist born -489, `death_age` 41) and Belesunu (-525, 36y before).
- **Why it's reader-visible:** The prose keeps the same birth mother (Balassu, who actively labors and births the protagonist in the story) and states the sisters' numeric ages, then explicitly frames the gap:
  - "Their first child, Amat-Sîn, was now forty-two and married into another household several years before".
  - "Belesunu, at thirty-five, had never married and remained in the house".
  - "Sîn-uballiṭ was born in late spring. He was the third child and the first son—the long-awaited heir after decades of only daughters."
  A reader is told the same mother bore her first daughter 42 years before bearing this newborn son ("decades of only daughters"), which is biologically impossible. The review changelog confirms the reviewer *introduced* this by "fixing" the sisters' ages from 14/8 up to 42/35 to match the buggy debug data — trading an internal-inconsistency error for a chronological-impossibility error.
- **Fix guidance:** Either recast Amat-Sîn and Belesunu as half-sisters (e.g. from the father's earlier marriage, as was done in 0031/0063), or restate their ages to a plausible window (e.g. ~early/mid 20s and late teens) and drop "decades of only daughters".

### 0231-unnamed-infant.md — VISIBLE-BUG
- **Bad sibling:** "Older Brother" / Koro (`birth_year` -3045, i.e. 45y before protagonist born -3000, `death_age` 45).
- **Why it's reader-visible:** The prose establishes a single birth mother and states the brother's age numerically:
  - "The household belonged to a woman raising children without a resident husband. Her eldest, Koro, had been born forty-five rains earlier. He hunted away from the river..."
  - then: "A boy was born, her third child. His head and shoulders came badly..."
  The same mother who has a 45-year-old son is depicted giving birth to a third child — impossible. There is no half-sibling framing and no other father; she is explicitly raising her children alone.
- **Fix guidance:** Restate Koro's age downward (a ~20-something eldest son works), or reframe him as a much older half-sibling / step-relation from a prior union. The sister ("Amina", born 24y before, depicted as "born twenty-four rains earlier") is at the outer edge but plausible; the 45-year figure is the load-bearing problem.

## Detail: ambiguous case held at DATA-ONLY

### 0133-phuntsok.md — DATA-ONLY (ambiguous, closest to VISIBLE-BUG)
- **Bad sibling:** Tsering (`birth_year` 1803 = 65y before protagonist born 1868, `death_age` 66).
- **Prose:** "Three adult siblings lived in the same household. Tsering, the oldest, was already an elder herdsman... In autumn 1869, Tsering died, weakened by a lung illness." Drolma (45) and Pema (25) are the others.
- **Why held at DATA-ONLY (not VISIBLE-BUG):** Unlike 0139/0231, the prose **never states Tsering's numeric age** ("elder herdsman" can read as senior-by-role, not 65) and the mother's age is never given. A reader is not handed the arithmetic. The data's "closer in age to an uncle" framing does not reach the page.
- **Caveat for editor:** This is genuinely borderline. A 65-year-old full brother co-resident with the birthing mother's newborn is implausible; if the prose were tightened it would be worth recasting Tsering as a half-brother or an uncle, since "siblings" + a 65-year span is fragile. Flagging rather than asserting it is fine.

## Notes on the "well-handled" half-sibling cases (DATA-ONLY)

0031 (Dionysios), 0063 (Juan/Antonio), and 0126 (Sali/Mina) all carry implausible structured `birth_year` values (59, 79/72, and 51 years before the protagonist) but are DATA-ONLY because the reviewer recast the relationship in prose:
- 0031: "Dionysios was Menedēmos's son from his first marriage, nearly sixty now".
- 0063: "two much older half-brothers from his father's first marriage—Juan and Antonio—both old men".
- 0126: "two much older sisters, both born to different fathers in earlier years—Salma, the eldest at nearly forty, and Minek, past thirty".

In each, the implied parent's age can still be strained (e.g. 0063's father siring sons in 1658 and again in 1737), but the prose does not state the parent's age, so no impossible relation is surfaced to the reader. These are deliberate, defensible fixes — not regressions to revert.
