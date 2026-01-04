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
├── ISSUE_TRACKER.md         # Narrative review patterns and recurring issues
├── generating_code/         # Python generation pipeline
│   ├── person.py            # Person sampling and representation
│   ├── location.py          # Geographic utilities
│   ├── lifespan.py          # Mortality simulation
│   ├── date_utils.py        # Date/calendar utilities
│   ├── generation.py        # LLM narrative generation
│   ├── llm_utils.py         # LLM infrastructure
│   ├── export.py            # Export to Jekyll markdown
│   ├── CountryData.py       # Country demographic data
│   ├── Raw_Data/            # 5.2 GB (NOT in git)
│   ├── Processed_Data/      # 1.1 GB (NOT in git)
│   └── *.pkl                # Generated people (NOT in git)
├── README.md
└── CLAUDE.md                # This file
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
- `person.py`: Person sampling and representation (12KB)
- `location.py`: Geographic utilities and Location class (8KB)
- `lifespan.py`: Mortality simulation using lifetables and Siler model (5KB)
- `date_utils.py`: Date/calendar arithmetic, formatting, and sampling (5KB)
- `generation.py`: LLM generation pipeline for narratives (30KB)
- `llm_utils.py`: LLM infrastructure - clients, cost tracking, retry logic (12KB)
- `export.py`: Export Person objects to Jekyll markdown format (4KB)
- `CountryData.py`: Country-level demographic data management (3KB)

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
python3 export.py batch_001.pkl
```

This creates markdown files in `_lives/` with this format:

```markdown
---
layout: life
title: "Person Name"
birth_year: "1834 AD"
death_year: "1891 AD"
birth_date: "March 15, 1834 AD"
death_date: "November 3, 1891 AD"
age_at_death: 57
location: "New York, United States"
country: "United States"
latitude: 40.71
longitude: -74.01
map_url: "https://www.google.com/maps/place/40.71,-74.01/@40.71,-74.01,5z"
lifestyle: "Rural"
era: "Holocene"
sex: "F"
---

Biographical narrative text goes here...
```

Note: `birth_date` and `death_date` fields are included for all people, formatted as readable dates (e.g., "March 15, 1834 AD" or "July 4, 5000 BC").

**Map URLs**: Each Holocene person includes a `map_url` field linking to their birthplace on Google Maps. The URL uses the format `https://www.google.com/maps/place/lat,lon/@lat,lon,5z` which displays both a marker at the precise location and a zoom level of 5 (landmass/continent view). This provides geographic context while being zoomed out enough to show the broader region.

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
person.twin                # None, 'identical', or 'fraternal' (~1.2% are twins)
person.orientation         # None (if died <13), or 'heterosexual'/'bisexual'/'homosexual'/'asexual'
person.handedness          # 'left' or 'right' (~10% left-handed)
person.height_percentile   # 0-100 percentile rank (None if died <13)
person.attractiveness_percentile  # 0-100 percentile rank (None if died <13)
person.birth_conditions    # List of congenital conditions (e.g., ['congenital deafness'])

# Era-specific
person.region              # Paleolithic: continental region
person.location            # Holocene: Location object with country, biome, etc.

# Generated by LLM pipeline
person.demographics        # Dict of demographic attributes
person.structured_incidents # List of life incidents (two-tier probabilistic sampling)
person.historical_context  # List of historical/environmental events affecting the person
person.name                # Generated name
person.naming_category     # 'attested', 'inferable', 'unrecoverable', or 'unnamed'
person.narrative_plan      # Timeline/family structure for narrative consistency
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

### Biological Attributes (Sampled at Creation)

Some attributes are sampled directly in `person.py` based on biological base rates, independent of era or culture:

**Twin Status** (`person.twin`):
- ~0.4% identical (monozygotic) twins
- ~0.8% fraternal (dizygotic) twins
- ~98.8% singleton (None)
- If a person is a twin, the LLM is asked about their co-twin's fate via the `co_twin_fate` demographic query

**Sexual Orientation** (`person.orientation`):
- Only sampled for people who reach age 13+
- ~92% heterosexual
- ~4% bisexual
- ~3% homosexual
- ~1% asexual
- None for those who die before puberty
- This represents underlying biological rates; how/whether orientation manifests depends on era, culture, and circumstances (handled by LLM demographic queries like `marital_status` and `partnership_history`)

**Physical Attributes**:
- `person.handedness`: ~10% left-handed, ~90% right-handed
- `person.height_percentile`: 0-100 percentile rank (cleared if died < 13)
- `person.attractiveness_percentile`: 0-100 percentile rank (cleared if died < 13)
- Extreme values (≤5th or ≥95th percentile) are flagged in narrative planning as "must be visible"

**Congenital Conditions** (`person.birth_conditions`):
Sampled independently based on medical base rates. Each condition has its own probability:
- Physical anomalies: cleft lip/palate (1/700), clubfoot (1/1000), polydactyly (1/800), limb reduction (1/2000)
- Sensory: congenital deafness (1/1000), congenital blindness (1/2500)
- Neurological: congenital epilepsy (1/300), cerebral palsy (1/500), stuttering (1/100)
- Other: albinism (1/17000), dwarfism (1/20000)
- Intersex: ambiguous genitalia at birth (1/4500), apparent at puberty (1/1500)

When present, congenital conditions are:
1. Highlighted in the demographics prompt so the LLM considers effects on life trajectory, social status, occupation, and marriage
2. Included in narrative planning context with "must be visible" flag
3. Even included for infants (age < 5) in narrative planning, though personality traits are not

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
3. `generate_structured_incidents()` - Two-tier probabilistic incident sampling (see below)
4. `generate_historical_context()` - Historical/environmental events affecting the person
5. `generate_name()` - Era-appropriate naming
6. `generate_narrative_plan()` - Timeline/family structure planning (see below)
7. `generate_narrative()` - Age-appropriate biography

Note: `quality_check()` exists but is not run by default—it wasn't adding enough value to justify the cost. It can be used for spot-checking samples if needed.

**Narrative Planning** (`generate_narrative_plan()`):
Before writing the narrative, the LLM creates a detailed timeline ensuring temporal consistency:
- **Siblings**: Birth years, death years, when they appear in the narrative (respects birth_order_position)
- **Partners**: Relationship start/end years, nature of relationship
- **Children**: Birth years, death years, narrative role
- **Life phases**: Age ranges with key events for each phase
- **Incident placements**: Exactly when each structured incident occurs
- **Named characters**: Who gets named and when they're prominent
- **Trait manifestations**: Concrete scenes showing extreme personality traits, mental disorders, and congenital conditions

This prevents temporal logic errors like siblings appearing at impossible ages or children mentioned before they could exist. Tiered by age category:
- **Infant (0-4)**: Sibling/caretaker timeline only (plus congenital conditions if present)
- **Child (5-12)**: Adds incidents, traits, and other characters
- **Adolescent/Adult (13+)**: Full planning including partners, children, life phases

**Two-Tier Incident System** (`generate_structured_incidents()`):
- **Tier 1**: LLM estimates probabilities for 11 broad categories (victim_violence, perpetrator_violence, severe_economic_crisis, serious_health_incident, etc.) based on demographics and personality
- **Sampling**: Categories are randomly sampled based on estimated probabilities
- **Tier 2**: For sampled categories, LLM estimates probabilities for specific subtypes (e.g., victim_violence → sexual_violence, domestic_violence, physical_assault)
- **Elaboration**: Sampled subtypes get concrete descriptions specific to the person's circumstances
- Calls are batched to reduce token usage (single Tier 2 call for all categories, single elaboration call)

### Lifestyle Categories
- **Hunter-Gatherer**: Pre-agricultural (all Paleolithic, some Holocene)
- **Rural**: Agricultural populations
- **Urban**: City dwellers

Different mortality models apply to each lifestyle.

### Naming Policy
Names must be readable by English speakers:

- **Latin-alphabet languages** (Spanish, Polish, French, Vietnamese, etc.): Keep native diacritics (ł, ń, ü, ç, etc.)
- **Non-Latin scripts** (Chinese, Arabic, Greek, Hindi, etc.): Use standard English romanization (pinyin for Chinese, etc.)
- **Inferable/reconstructed names**: Plain romanization only—no scholarly notation (asterisks, IPA symbols, macrons, hyphens between morphemes)

Naming categories:
- **attested**: Names from written records for that era/region
- **inferable**: Phonologically plausible names for known language families without written records
- **unrecoverable**: Simple human-sounding names for languages with no known connections
- **unnamed**: Infants who died before customary naming age

### Narrative Style Guidelines
The project aims for plain, direct prose:
- Write actively and directly; state facts plainly and concretely
- No figurative language (no metaphors, similes, personification)
- No archaic inversions, poetic flourishes, or lines reaching for literary effect
- Describe what was there, not what wasn't (avoid negatives that only matter as absences)
- Variable sentence rhythm; mix lengths; fragments sometimes
- Show personality through action, not summary; don't name traits
- Length scaled to lifespan: 150-300 words (ages 0-2), 200-400 (3-10), 400-700 (11-18), 600-1000 (19+)
- Early in narrative, orient reader to political/cultural situation (polity, ethnic group, broader forces)
- Omniscient narrator: state facts confidently, no hedging ("likely", "perhaps", "may have")
- Give names to recurring people; minor one-off figures can remain unnamed

---

## Working with the Codebase

### Code Architecture

The Python generation pipeline is organized into focused modules with clear responsibilities:

**Core Data Models:**
- `person.py` - Person class, sampling logic, biological attributes
  - Handles both Paleolithic and Holocene eras
  - Samples birth years weighted by historical births
  - Samples biological attributes: sex, twin status, orientation, handedness, height, attractiveness, congenital conditions
  - Manages demographic attributes and LLM-generated content

- `location.py` (8KB) - Location class and geographic data
  - Converts HYDE grid coordinates to geographic information
  - Provides country, biome, climate, elevation data
  - Uses lazy loading for 6+ GB of geographic datasets
  - `gmap_url()` method generates Google Maps URLs with markers (default zoom level 5)

- `lifespan.py` (5KB) - Mortality modeling
  - Age-at-death calculation using historical lifetables
  - Siler model for hunter-gatherer populations
  - Accounts for lifestyle (urban, rural, hunter-gatherer)

- `date_utils.py` (5KB) - Date and calendar utilities
  - Calendar arithmetic (leap years, day counting, year rollovers)
  - Date formatting (AD/BC display, month/day conversion)
  - Date sampling (birth and death date generation)
  - Works with `(year, day_of_year)` tuple format

**Generation Pipeline:**
- `generation.py` - LLM narrative generation
  - Multi-stage pipeline: demographics → incidents → historical_context → name → narrative_plan → narrative
  - Narrative planning stage ensures temporal consistency (sibling/child timelines)
  - Age-appropriate narrative generation (infant/child/adolescent/adult)
  - Integrates congenital conditions into demographics prompts and narrative planning
  - Flags extreme personality traits and physical attributes for visibility in narratives
  - Prompt engineering for historical accuracy and plain prose style

- `llm_utils.py` (12KB) - LLM infrastructure
  - API clients (Anthropic, OpenAI, Google)
  - Cost tracking with prompt caching support (OpenAI, Anthropic, Google)
  - Retry logic and error handling
  - JSON extraction utilities

**Export & Data:**
- `export.py` (4KB) - Jekyll markdown export
  - Converts Person objects to markdown with frontmatter
  - Handles both Paleolithic and Holocene formatting
  - Includes Google Maps URLs with markers for Holocene people
  - Creates URL-safe slugs for filenames
  - Exports full person data as YAML comments for debugging

- `CountryData.py` (3KB) - Country demographic data
  - Post-1600 country-level statistics
  - Population, births, life expectancy by year

**Key Design Patterns:**
- **Lazy loading**: Geographic data loads on first use, not import (person.py, location.py)
- **Separation of concerns**: Domain models separate from generation logic and export
- **Unified Person class**: Single class handles all eras with era-specific initialization
- **Tuple dates**: `(year, day_of_year)` format works for all years including BCE

### File Editing Policy

**IMPORTANT: Do not directly edit generated markdown files in `_lives/`**

The markdown files in `_lives/` are **generated outputs** from the Python pipeline. They should only be modified by:
1. Re-running `export.py` with updated pickle files
2. Modifying the export script itself to change the output format

**DO:**
- Edit Python scripts in `generating_code/` (person.py, export.py, generation.py, etc.)
- Edit Jekyll templates in `_layouts/` (life.html, default.html)
- Edit site-wide files (CSS, index.html, about.md, _config.yml)
- Re-generate markdown files by running export scripts

**DON'T:**
- Manually edit individual `.md` files in `_lives/`
- Create one-off scripts to patch generated files
- Try to fix data issues by editing the output instead of the source

**If you need to change how biographical pages are structured or what data they display:**
1. Modify `export.py` to change the frontmatter/content generation
2. Modify `_layouts/life.html` to change how data is displayed on the page
3. Re-run the export script to regenerate all files with the new format

**Rationale**: The `_lives/` directory will eventually contain hundreds of generated files. Any manual edits will be lost when the export script is re-run. Changes must be made at the source (Python pipeline or Jekyll templates) to be permanent and apply to all files consistently.

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

## Filtering and Tagging System

The homepage (`index.html`) includes a comprehensive filtering system with clickable tag buttons:

### Filter Categories
- **Born after/before**: Text inputs accepting formats like "10000 BC", "500 AD", "1990"
- **Sex**: Multi-select (Male, Female)
- **Continent**: Multi-select (Africa, Asia, Europe, N. America, S. America, Oceania)
- **Age at Death**: Multi-select (Alive, Infant, Child, Adolescent, Adult, Elder)
- **Lifestyle**: Multi-select (Hunter-Gatherer, Rural, Urban)
- **Sort**: Single-select (Default, Oldest first, Newest first, Random)

### How It Works
- Click tag buttons to toggle selection (blue = selected)
- Empty selection means "show all" for that category
- Multiple selections within a category use OR logic (matches any)
- Selections across categories use AND logic (must match all)
- Clicking "Random" again re-shuffles the order

### Frontmatter Fields for Filtering
Each life markdown file includes these fields used for filtering:
```yaml
birth_year_numeric: -5000      # Numeric year for sorting/filtering
sex: "M"                       # M or F
continent: "Africa"            # Computed from country or Paleolithic region
age_tag: "Adult (19–49)"       # Computed from age_at_death
lifestyle: "Hunter-Gatherer"   # Hunter-Gatherer, Rural, or Urban
```

### Continent Mapping
- **Holocene**: Mapped from country using `COUNTRY_TO_CONTINENT` dict in `export.py`
- **Paleolithic**: Mapped from region (Africa, Asia, Europe, North_America, South_America, Sahul→Oceania)

### Individual Life Page Navigation
Each biographical page (`_layouts/life.html`) includes navigation buttons:
- **← Earlier life**: Previous person chronologically
- **Random life**: Jump to random biography
- **Later life →**: Next person chronologically

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
- `generating_code/export.py` - Export to markdown

### Quality Control
- `ISSUE_TRACKER.md` - Tracks recurring narrative issues and patterns found during batch review
  - Check before generating new batches to review current priorities
  - Update after reviewing generated narratives
  - Prioritizes issues (high/medium/low) and tracks resolution across batches

---

## Roadmap

### Phase 1: Core Pipeline ✅
- [x] Person sampling and demographics generation
- [x] Life events generation
- [x] Narrative generation
- [x] Jekyll website setup
- [x] Export script
- [ ] Batch generation and refinement ← current focus

### Phase 2: Context & Metadata
- [x] Tagging system (continent, age buckets, lifestyle, sex)
- [x] Filtering/search functionality on website

### Phase 2b: Demographic Coverage ✅

The two-tier structured incident system now probabilistically samples life events that were previously underrepresented. Tier 1 categories include:
- `victim_violence` (sexual, domestic, physical assault)
- `victim_property_crime`
- `perpetrator_violence`
- `perpetrator_property_crime`
- `severe_economic_crisis`
- `serious_health_incident`
- `major_caregiving`
- `warfare_impact`
- `major_achievement`
- `religious_change`
- `nonstandard_sexual_history` (premarital, extramarital, sex work, same-sex; female-specific: pregnancy outside marriage, complications, abortion)

The system explicitly instructs the LLM to estimate probabilities based on historical base rates without sanitizing.

### Phase 3: Presentation
- [ ] Cross-story editing pass (review for clichés/repetition)
- [ ] Methodology write-up
- [ ] Data visualizations (timeline, map, distributions)

### Phase 4: Extensions
- [ ] MC estimation tool ("what fraction of humans were X?")
- [ ] Additional content (essays, visualizations)

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

### Cost Tracking and Caching

The `CostTracker` class in `llm_utils.py` tracks token usage and costs across providers:
- Tracks input tokens, cached input tokens, and output tokens separately
- Supports prompt caching from OpenAI (automatic), Anthropic, and Google
- Cached tokens receive 90% discount (charged at 10% of normal input rate)
- `print_summary()` shows cache hit rate when caching is active

**Estimated cost per person** (GPT-5.2 with caching, without QC):
- ~14K input tokens, ~3.7K output tokens per narrative generation
- With prompt caching: ~$0.04-0.05 per person
- Full pipeline (demographics + events + narrative): ~$0.10-0.15 per person
