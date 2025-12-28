# Random Lives - Complete Project Documentation

## Project Overview

**Ultimate Goal**: Create a website with 100-1,000 biographical stories of randomly sampled people from across all of human history, weighted by actual birth numbers. The site allows visitors to explore these lives through filtering/tagging (time period, geography, age, etc.) to get an accurate statistical picture of human experience.

**Live Site**: https://random-lives.github.io/random-lives/

For each randomly selected person, the system:

1. **Samples a birth year** weighted by historical births across all human history (200,000 BCE to present)
2. **Generates demographic data** based on their birth time/location
3. **Simulates their lifespan** using historical mortality data
4. **Creates detailed biographical narratives** using LLMs

The sampling is **truly random** weighted by historical birth rates, which means repetitive patterns (e.g., many infant deaths, many Chinese/Indian births from high-population eras) accurately reflect human history.

---

## Current Project Structure

```
RandomLivesWebsite/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── _layouts/
│   ├── default.html         # Base page template
│   └── life.html            # Template for individual biographical pages
├── _lives/                  # Biographical stories (Markdown files)
│   └── example-person.md
├── assets/css/
│   └── style.css            # Site styling
├── index.html               # Homepage (lists all lives)
├── about.md                 # About page
├── generating_code/         # Python generation pipeline
│   ├── person.py            # Person sampling
│   ├── generation.py        # LLM narrative generation
│   ├── llm_utils.py         # LLM infrastructure
│   ├── lifespan.py          # Mortality simulation
│   ├── location.py          # Geographic utilities
│   ├── CountryData.py       # Country demographic data
│   ├── export_to_jekyll.py  # Export script (pkl → markdown)
│   ├── Raw_Data/            # 5.2 GB (NOT in git)
│   ├── Processed_Data/      # 1.1 GB (NOT in git)
│   └── *.pkl                # Generated people (NOT in git)
├── README.md
└── PROJECT_DOCS.md          # This file
```

---

## Technical Setup

### Website (Jekyll + GitHub Pages)

- ✅ Ruby 3.4.8 installed via Homebrew
- ✅ Jekyll and dependencies installed via Bundler
- ✅ Site hosted on GitHub Pages at random-lives organization
- ✅ Responsive design with clean typography
- ✅ Collections system for biographical stories

### Generation Pipeline (Python)

**Core Data Files** (in `generating_code/`):
- **Raw_Data/**: Source datasets
  - `HYDE34/`: Historical population, cropland, urban data (gridded, 10,000 BCE - 2024)
  - `Post1600/`: Country-level population, births, life expectancy data
  - `lifetables.csv`: Mortality tables by region, sex, and life expectancy

- **Processed_Data/**: Derived datasets
  - `unified_births.pkl`: Unified birth series spanning all human history
  - `paleo_regions.pkl`: Paleolithic regional population data
  - `processed_p1600_data.pkl`: Country-level demographic data (1600+)
  - `births_array.h5`: Gridded birth estimates (Holocene)
  - `hg_array.h5`: Hunter-gatherer population maps

**Python Modules**:
- `person.py`: Person sampling and representation
- `generation.py`: LLM generation pipeline
- `llm_utils.py`: LLM infrastructure (client, cost tracking)
- `lifespan.py`: Mortality simulation
- `location.py`: Geographic utilities
- `CountryData.py`: Country-level demographic data management
- `export_to_jekyll.py`: Export Person objects to Jekyll markdown

**Dependencies**:
- Data processing: numpy, scipy, xarray, rasterio, h5py, geopandas
- LLM interaction: langchain (anthropic, openai, google-vertexai)
- Serialization: dill (extended pickle)

---

## Workflow

### 1. Generate People (Python)

```python
from generation import generate_person, generate_batch

# Generate a single person
person = generate_person(model='gpt-5.2', quiet=False)

# Generate a batch
people = generate_batch(n=10, model='gpt-5.2')

# Save to pickle
import dill
with open('batch_001.pkl', 'wb') as f:
    dill.dump(people, f)
```

### 2. Export to Jekyll

```bash
cd /Users/damonbinder/Documents/RandomLivesWebsite/generating_code
python3 export_to_jekyll.py batch_001.pkl
```

This creates markdown files in `_lives/` with this format:

```markdown
---
layout: life
title: "Person Name"
birth_year: "1834 AD"
death_year: "1891 AD"
birth_date: "March 15, 1834"
death_date: "November 3, 1891"
age_at_death: 57
country: "United States"
lifestyle: "Rural"
era: "Holocene"
sex: "F"
events:
  - "Event description"
---

Biographical narrative text goes here...
```

Note: `birth_date` and `death_date` fields are included for all people, formatted as readable dates (e.g., "March 15, 1834 AD" or "July 4, 5000 BC").

### 3. Preview Locally (Optional)

```bash
cd /Users/damonbinder/Documents/RandomLivesWebsite
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle exec jekyll serve
# Visit http://localhost:4000/random-lives/
```

### 4. Publish to Website

```bash
git add _lives/
git commit -m "Add batch of biographical stories"
git push
```

GitHub Pages automatically rebuilds in 1-2 minutes.

---

## Person Object Structure

The `Person` class stores all data for a generated person:

```python
person.era                 # 'Paleolithic' or 'Holocene'
person.birth_year          # Numeric year (negative for BCE)
person.birth_year_str      # Formatted string ("1234 AD" or "5000 BC")
person.birth_date          # (year, day_of_year) tuple
person.death_date          # (year, day_of_year) tuple, or None if alive
person.sex                 # 'M' or 'F'
person.age_at_death        # Numeric age or "alive"
person.lifestyle           # 'Hunter-Gatherer', 'Rural', or 'Urban'
person.personality         # Dict of percentile ranks (0-100)

# Era-specific
person.region              # Paleolithic: continental region
person.location            # Holocene: Location object with country, biome, etc.

# Generated by LLM pipeline
person.demographics        # Dict of demographic attributes
person.events              # List of life events
person.narrative           # Biographical text
person.messages            # Full LLM conversation history
```

### Birth and Death Dates

Dates are stored as `(year, day_of_year)` tuples where `day_of_year` is 1-365 (or 1-366 for leap years). This format works for all years including BCE (negative years).

- **Birth dates**: Uniformly sampled within the birth year
- **Death dates**:
  - **Infants (age < 1)**: Uses realistic neonatal/post-neonatal distribution
    - 55% die in neonatal period (0-27 days): 40% on day 0, exponential decay (mean ~5 days) for days 1-27
    - 45% die in post-neonatal period (28-365 days): roughly uniform distribution
    - Based on empirical data showing ~40% of infant deaths occur on day 1, with rapid decay thereafter
  - **Others (age ≥ 1)**: Uniformly distributed within possible death years, ensuring death occurs after birth_year + age_at_death years
  - This addresses the issue that death_year calculated as birth_year + age_at_death can be off by one year depending on whether birthdays occurred

---

## Key Design Choices

### Unified Person Class
A single `Person` class handles both Paleolithic and Holocene eras:
- `person.era`: 'Paleolithic' or 'Holocene'
- `person.region`: Set for Paleolithic (None for Holocene)
- `person.location`: Set for Holocene (None for Paleolithic)

### LLM Generation Pipeline
Each step takes `(person, ctx)` and modifies the person in place:
1. `generate_geography()` - Paleolithic only, refines location
2. `generate_demographics()` - Era-appropriate demographic attributes
3. `generate_life_events()` - Probabilistic event sampling
4. `generate_narrative()` - Age-appropriate biography
5. `quality_check()` - Fix anachronisms and style issues

### Lifestyle Categories
- **Hunter-Gatherer**: Pre-agricultural (all Paleolithic, some Holocene)
- **Rural**: Agricultural populations
- **Urban**: City dwellers

Different mortality models apply to each lifestyle.

### Narrative Style Guidelines
The project aims for "quiet realism":
- Plain contemporary English (no archaic inversions)
- Sparse figurative language (~1 per 600 words)
- No moralizing endings or clichés
- Variable sentence rhythm
- Show personality through repeated actions, not summary
- Length scaled to lifespan: 150-300 words (ages 0-2), 200-400 (3-10), 400-700 (11-18), 600-1000 (19+)
- Historical context integrated throughout (~20-30%)
- Omniscient narrator: authoritative, not hedging
- Specific actors, not vague collectives

---

## Local Development Commands

### Jekyll Site

```bash
# Start local server
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle exec jekyll serve

# Build site
bundle exec jekyll build

# Clean build artifacts
rm -rf _site .jekyll-cache
```

### Git Workflow

```bash
# Check status
git status

# Add and commit changes
git add .
git commit -m "Description of changes"

# Push to GitHub
git push
```

---

## Important Files

### Website Configuration
- `_config.yml` - Site-wide settings (URL, baseurl, collections)
- `_layouts/life.html` - Template for biographical pages
- `assets/css/style.css` - All styling
- `index.html` - Homepage layout
- `about.md` - About page

### Generation Scripts
- `generating_code/person.py` - Core person sampling logic
- `generating_code/generation.py` - LLM generation pipeline
- `generating_code/export_to_jekyll.py` - Export to markdown

---

## Roadmap

### Phase 1: Core Pipeline ✅
- [x] Person sampling and demographics generation
- [x] Life events generation
- [x] Narrative generation
- [x] Quality control pass
- [x] Jekyll website setup
- [x] Export script
- [ ] Batch generation and refinement ← current focus

### Phase 2: Context & Metadata
- [ ] Historical context/notes generation
- [ ] Tagging system (era, region, age buckets, lifestyle, themes)
- [ ] Filtering/search functionality on website

### Phase 3: Presentation
- [ ] Cross-story editing pass (review for clichés/repetition)
- [ ] Methodology write-up
- [ ] Data visualizations (timeline, map, distributions)

### Phase 4: Extensions
- [ ] MC estimation tool ("what fraction of humans were X?")
- [ ] Additional content (essays, visualizations)

---

## Known Limitations & Future Improvements

### Paleolithic Population Estimates
- Current: Rough estimates without rigorous sources
- Needed: Better paleodemographic literature, documented assumptions

### Life Expectancy / Mortality
- Hunter-Gatherers: Siler model (Gurven & Kaplan 2007) ✅
- Pre-1600 non-HG: Chilean lifetables as universal proxy (crude)
- Post-1600: Country-specific data ✅
- Improvement: Better region-specific lifetable mapping

### Birth Data Coverage
- Current: HYDE data to 2024
- Needed: Extend to 2025 for early 2026 release

---

## Troubleshooting

### Jekyll Build Issues
```bash
# If Ruby/Jekyll stops working
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle install

# Rebuild from scratch
rm -rf _site .jekyll-cache
bundle exec jekyll build
```

### GitHub Pages Issues
- Check Settings → Pages for build errors
- Ensure `_config.yml` has correct `baseurl` and `url`
- Verify all markdown files have valid frontmatter

### Python Issues
```bash
# Install missing dependencies
pip3 install dill numpy scipy xarray h5py geopandas

# Check if data files exist
ls generating_code/Raw_Data/
ls generating_code/Processed_Data/
```

---

## Resources

- **Jekyll**: https://jekyllrb.com/docs/
- **GitHub Pages**: https://docs.github.com/en/pages
- **Liquid templates**: https://shopify.github.io/liquid/
- **Repository**: https://github.com/random-lives/random-lives
- **Live site**: https://random-lives.github.io/random-lives/

---

## Notes

- Cost tracking is important - track per-story costs across models
- Personality traits are percentile ranks (0-100) - extremes should be visible in narratives
- ~5% of samples are Paleolithic, ~95% Holocene (reflects actual birth distribution)
- Data files (6.3 GB) are excluded from git via .gitignore
- Python scripts are version controlled, but data is not
