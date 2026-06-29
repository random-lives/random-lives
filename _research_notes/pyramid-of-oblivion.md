# Research Notes: The Pyramid of Oblivion

**Status**: Framing / scoping (started 2026-04-18)

## The Question

What fraction of humans who have ever lived are remembered in any form at all? For almost the entire ~200,000-year span of human history, the answer is: essentially none. But "remembered" is doing a lot of work in that sentence. The post sketches a layered hierarchy — each layer a smaller fraction of the total — so that the shape of the pyramid is itself the answer.

## Proposed Tiers

Ordered from widest base (most humans) to narrowest tip (fewest). Each tier should have a precise enough definition to in principle be counted.

1. **Physical trace survives.** Something derived from the person's body still exists — skeletal remains, teeth, preserved soft tissue, a hair, extractable DNA, a fingerprint, a footprint. Does *not* require that the remains be identified with a specific individual; only that they persist.

2. **Name recorded anywhere.** Their personal name appears in any surviving source — an inscription, a tablet, a census, a parish register, a tombstone, a database. The name need not be attached to any other biographical fact.

3. **One biographical fact preserved.** Beyond the bare name, at least one fact about their life survives: birth or death date, occupation, a parent, a place lived, an event they were part of.

4. **Remembered by someone alive today.** At least one living person holds a specific, non-generic memory *of this individual* — a grandparent, a teacher, a local figure. Living memory, not historical record.

5. **Widely remembered.** Recognizable to a meaningful fraction of strangers. The obvious operationalization is "has a Wikipedia article," but one could also slice by language-edition coverage or page-view volume.

Sub-tip (optional): **Universally known.** A much smaller set — figures nearly every literate adult globally could name. Order of magnitude: hundreds to low thousands.

### Tier structure caveat

These are not strictly nested. A Neolithic skeleton has a physical trace but no name; a Sumerian scribe known from one tablet has a name but no remains; a great-great-grandmother in living memory might have no written trace. The cleanest framing is five independent indicator variables, with the interesting question being their joint distribution — not just the marginal fraction in each.

## Why this is interesting

- For the overwhelming majority of human history, the answer to every tier is ~0%. The pyramid is almost entirely base — "no trace at all" — with a vanishingly thin top.
- The transition is recent and uneven. Name-recording reaches a large fraction of the population only with universal birth registration (mostly post-1850 in Europe, later elsewhere). Physical-trace survival has a U-shape: high for recent dead (graves, DNA), low for medieval, higher for prehistoric (durable bone in undisturbed sites), near-zero for most of prehistory.
- Living memory has a hard ceiling around ~100 years — the oldest specific memories held by anyone alive today reach back to people born in the late 1800s.
- The "widely remembered" tier is the subject of the existing [Who is the most famous person?](../_posts/2026-03-17-most-famous-person.md) post — this post is the complement: how rare is even that faint form of survival?

## Methodology Sketch

Rough strategy for each tier, to be developed:

### Tier 1 — Physical trace
- Paleolithic/Mesolithic: counts of hominin skeletal specimens in curated databases (e.g. Smithsonian Human Origins, ROCEEH) vs. estimated births in those periods.
- Holocene pre-modern: harder — need estimates of total excavated burials or an assumption about preservation-times-excavation-rate.
- Modern (post-~1800): essentially 100% as long as the grave is undisturbed; convergence toward 100% as we approach present.
- Need to decide: does cremated / dispersed remains count? (Probably not — no recoverable trace.)

### Tier 2 — Name recorded
- Modern: birth-registration coverage by country × year is the key number. UN and UNICEF publish this.
- Pre-modern literate societies: rough approach is (literate population × fraction-of-literates-named-in-surviving-records). The surviving-records rate is small but nonzero — e.g. most Roman citizens above a certain status are attested somewhere.
- Pre-literate: zero by definition, except for names preserved orally and later written down.

### Tier 3 — Biographical fact
- Same framework as Tier 2, minus the cases where only the name survives. The ratio (biographical-fact-known / name-known) is itself interesting to estimate.

### Tier 4 — Living memory
- Model the decay function: probability that a specific person born in year Y is personally remembered by anyone alive in year 2026.
- Rough shape: near-100% for people born ~1940–2000, falling sharply before ~1920, effectively zero before ~1870.
- Need to be careful about what "specific memory" means — my grandmother's grandmother's name is remembered by me, but only because it was written in a family Bible, which is really Tier 2.

### Tier 5 — Widely remembered
- Already explored in the FamousPerson post; reuse that framework. Wikipedia article as the operational threshold.
- Could also sub-stratify: language coverage, pageviews.

## Open Questions

1. **Should "physical trace" include ordinary unmarked graves in still-existing cemeteries?** Inclination: yes, if the remains still physically exist, regardless of whether anyone could identify whose they are. But this makes modern numbers dominated by graveyard infrastructure.
2. **DNA as a form of trace.** Is every person who has living direct descendants "physically traceable" because their DNA persists? Arguably yes, but this conflates with a different question (ancestry, covered by the We Are Family post).
3. **Oral vs. written name-recording.** In oral cultures, a name might be remembered for several generations after death. Does that count as "recorded"? Proposed rule: only count a name as "recorded" if it survived into the present in some form (written or still orally transmitted) — otherwise every person in a naming culture would trivially count.
4. **How do you verify the bottom of the pyramid?** The whole premise is that the vast majority leave zero trace. Estimating "zero" requires knowing total births (HYDE handles this) and confidently bounding the numerator at something small.
5. **Time resolution.** The cleanest version of the post shows each tier's fraction over time (by birth year). Single aggregate numbers are less informative than the curves.

## Connections to Other Posts

- **[Most famous person](../_posts/2026-03-17-most-famous-person.md)**: The narrow tip. Reuse the Wikipedia-based framework for Tier 5.
- **We Are Family** (planned): DNA persistence and descendant-lineages tie to Tier 1 if we extend "physical trace" that way.
- **How many people have ever lived?** ([published](../_posts/2026-01-18-how-many-people-have-ever-lived.md)): The denominator. Every tier's fraction is divided by the ~117 billion total.
