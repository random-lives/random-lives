"""Estimate the rate of 'parents who lost a child' using the project's own
demographic model, at higher accuracy than the 250-story hand count.

Methodology (identical to the generation pipeline, generation.py:_add_family_context):
  - A parent with k children has them at birth_year + 17 + 3*i.
  - Each child's sex is random M/F; each child's age at death is drawn from the
    SAME age_at_death() mortality model used everywhere in the project.
  - A child is 'lost' iff it dies before the parent does (child still alive => not lost;
    parent still alive => any dead child counts).

The only LLM-sourced input is k (number_of_children). We use it two ways:
  PART 1 (faithful, free): take the real (k, demographics) of every parent in the
          136 modern-schema stories and integrate out the child-draw noise exactly.
  PART 2 (scaled): sample many fresh people via person.py and draw k from the
          empirical k|(sex, age-bucket) distribution observed in the stories.
"""
import os, re, glob, random
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from lifespan import age_at_death
import person as P

DEATH_FAR = 10**9  # sentinel "death year" for someone still alive

def child_lost(parent_birth, parent_death_year, country, lifestyle, k, rng):
    """Return 1 if >=1 of k children predeceases the parent, else 0 (one draw)."""
    for i in range(k):
        cby = parent_birth + 17 + 3 * i
        if cby > 2025:
            continue  # child not yet born / not yet at risk (cf. lifespan.py 'alive' guard)
        sex = 'M' if rng.random() < 0.5 else 'F'
        a = age_at_death(country, cby, sex, lifestyle)
        if a == "alive":
            continue
        cdy = cby + a
        if cdy < parent_death_year:
            return 1
    return 0

def p_child_lost(parent_birth, parent_death_year, country, lifestyle, k, m, rng):
    """Monte-Carlo P(>=1 child predeceases) for a fixed parent over m child-draws."""
    return sum(child_lost(parent_birth, parent_death_year, country, lifestyle, k, rng)
               for _ in range(m)) / m

# ---------------------------------------------------------------------------
# Parse the 136 modern-schema stories for (birth_year, age_at_death, sex,
# lifestyle, country, k=number_of_children).
# ---------------------------------------------------------------------------
def parse_stories():
    rows = []
    for f in sorted(glob.glob("../_lives/[0-9]*.md")):
        txt = open(f).read()
        m = re.search(r"number_of_children:\s*'?(\d+)'?", txt)
        if not m:
            continue  # old-schema file, no structured k
        k = int(m.group(1))
        by = re.search(r"^birth_year_numeric:\s*(-?\d+)", txt, re.M)
        sx = re.search(r'^sex:\s*"?([MF])"?', txt, re.M)
        # use the GENERATION-TIME lifestyle (debug '# Lifestyle:'), not the
        # later-reclassified frontmatter value
        ls = re.search(r"^#\s*Lifestyle:\s*(.+)$", txt, re.M)
        co = re.search(r'^country:\s*"?([^"\n]+)"?', txt, re.M)
        aad = re.search(r"^age_at_death:\s*(\S+)", txt, re.M)
        if not (by and sx and ls and aad):
            continue
        birth = int(by.group(1))
        ad = aad.group(1).strip().strip('"')
        death_year = DEATH_FAR if ad == "alive" else birth + int(ad)
        rows.append(dict(
            birth=birth, sex=sx.group(1),
            lifestyle=ls.group(1).strip(),
            country=(co.group(1).strip() if co else None),
            age_at_death=(None if ad == "alive" else int(ad)),
            death_year=death_year, k=k,
        ))
    return rows

def wilson(k, n, z=1.96):
    if n == 0:
        return (float('nan'), float('nan'))
    p = k / n
    c = (p + z*z/(2*n)) / (1 + z*z/n)
    hw = (z/(1 + z*z/n)) * np.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return (c - hw, c + hw)

def main():
    rng = random.Random(0)
    rows = parse_stories()
    parents = [r for r in rows if r['k'] > 0]
    print(f"Modern-schema stories parsed: {len(rows)}  | parents (k>=1): {len(parents)}")

    # ---- PART 1: faithful Rao-Blackwell over the real parents ----
    M = 4000  # child-draws per parent
    qs = np.array([p_child_lost(r['birth'], r['death_year'], r['country'],
                                r['lifestyle'], r['k'], M, rng) for r in parents])
    point = qs.mean()
    # bootstrap CI over the set of parents (this is the residual sampling error)
    B = 20000
    n = len(qs)
    idx = np.random.randint(0, n, size=(B, n))
    boot = qs[idx].mean(axis=1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    print("\n=== PART 1: faithful estimate over the observed parents "
          "(child-mortality noise integrated out) ===")
    print(f"  P(parent loses >=1 child) = {point*100:.1f}%")
    print(f"  95% bootstrap CI over parents: [{lo*100:.1f}%, {hi*100:.1f}%]")
    print(f"  (hand-counted realization for comparison: 91/107 = 85.0%)")

    # ---- Build empirical k | (sex, age-bucket) from the stories ----
    def bucket(age):
        if age is None: return '60+'      # still alive -> long-lived
        for hi_ in (1, 5, 15, 25, 40, 60):
            if age < hi_: return f'<{hi_}'
        return '60+'
    from collections import defaultdict
    kdist = defaultdict(list)
    for r in rows:
        kdist[(r['sex'], bucket(r['age_at_death']))].append(r['k'])
    allk = [r['k'] for r in rows]
    by_bucket = defaultdict(list)
    for r in rows:
        by_bucket[bucket(r['age_at_death'])].append(r['k'])
    def draw_k(sex, age, rng):
        # empty bucket => k=0 (no structured data for that age => not a parent),
        # never fall back to the adult-heavy global pool
        pool = kdist.get((sex, bucket(age))) or by_bucket.get(bucket(age))
        return rng.choice(pool) if pool else 0

    # ---- PART 2: scaled MC over freshly sampled people ----
    N = 60000
    rng2 = random.Random(1)
    np.random.seed(1)
    n_parent = 0
    n_loss = 0
    for _ in range(N):
        per = P.sample_person(light=True)
        aad = per.age_at_death
        age = None if aad == "alive" else aad
        sex = per.sex
        k = draw_k(sex, age, rng2)
        if k <= 0:
            continue
        n_parent += 1
        country = per.location.country if getattr(per, 'location', None) else None
        pdy = DEATH_FAR if aad == "alive" else per.birth_year + aad
        n_loss += child_lost(per.birth_year, pdy, country, per.lifestyle, k, rng2)
    rate = n_loss / n_parent
    clo, chi = wilson(n_loss, n_parent)
    print("\n=== PART 2: scaled MC (fresh person sample; k from empirical "
          "k|sex,age distribution) ===")
    print(f"  sampled people: {N:,} | parents: {n_parent:,} ({n_parent/N*100:.1f}%)")
    print(f"  P(parent loses >=1 child) = {rate*100:.1f}%")
    print(f"  95% CI (Wilson, sampling error only): [{clo*100:.1f}%, {chi*100:.1f}%]")

if __name__ == "__main__":
    main()
