# Human Population: Random Lives Project

## Project Overview

**Ultimate Goal**: Create a website with 100-1,000 biographical stories of randomly sampled people from across all of human history, weighted by actual birth numbers. The site will allow visitors to explore these lives through filtering/tagging (time period, geography, age, etc.) to get an accurate statistical picture of human experience.

**Current Status**: Unified pipeline works for all of human history (200,000 BCE to present).

For each randomly selected person, the system:

1. **Samples a birth year** weighted by historical births across all human history
2. **Generates demographic data** based on their birth time/location
3. **Simulates their lifespan** using historical mortality data
4. **Creates detailed biographical narratives** using LLMs

The sampling is **truly random** weighted by historical birth rates, which means repetitive patterns (e.g., many infant deaths, many Chinese/Indian births from high-population eras) accurately reflect human history.

## Project Structure

### Core Data Files

- **Raw_Data/**: Source datasets
  - `HYDE34/`: Historical population, cropland, grazing land, and urban population data (gridded, 10,000 BCE - 2024)
  - `Post1600/`: Country-level population, births, life expectancy, and CBR (crude birth rate) data
  - `lifetables.csv`: Mortality tables by region, sex, and life expectancy level

- **Processed_Data/**: Derived datasets
  - `unified_births.pkl`: Unified birth series spanning all human history (for year sampling)
  - `paleo_regions.pkl`: Paleolithic regional population data (for region sampling pre-10,000 BCE)
  - `processed_p1600_data.pkl`: Country-level demographic data objects (1600+)
  - `births_array.h5`: Gridded birth estimates across time (Holocene)
  - `hg_array.h5`: Hunter-gatherer population maps

### Python Modules

- **person.py**: Unified person sampling across all human history
  - `sample_year()`: Sample birth year from unified birth series
  - `sample_person()`: Sample a person (returns Person with era-appropriate attributes)
  - `Person`: Single unified class with `era` attribute ('Paleolithic' or 'Holocene')

- **location.py**: Geographic utilities for Holocene people
  - `Location`: Converts HYDE grid coordinates to geographic information (country, biome, climate, address)

- **generation.py**: Unified LLM generation pipeline
  - `generate_person(model, quiet, show_cost)`: Full pipeline - samples person and generates complete biography
  - `generate_batch(n, model, quiet, show_cost)`: Generate multiple people
  - Individual steps (take `person` and `GenerationContext`):
    - `generate_geography(person, ctx)`: Refine Paleolithic geography
    - `generate_demographics(person, ctx)`: Generate demographic attributes
    - `generate_life_events(person, ctx)`: Sample life events probabilistically
    - `generate_narrative(person, ctx)`: Generate biographical narrative
    - `quality_check(person, ctx)`: Review and revise narrative

- **llm_utils.py**: LLM infrastructure shared across modules
  - `GenerationContext`: Bundles LLM client, callbacks, and settings for pipeline
    - `ctx.call(messages)`: Make LLM call, return text
    - `ctx.call_json(messages)`: Make LLM call, return parsed JSON
    - `ctx.log(message)`: Print if not quiet
    - `ctx.finish()`: Print cost summary if enabled
  - `get_client()`: Multi-provider LLM client (Anthropic, OpenAI, Google)
  - `CostTracker`: Token usage and cost tracking
  - `extract_json()`, `sample_distribution()`: Helper functions for LLM responses

- **lifespan.py**: Mortality simulation
  - `age_at_death(country, birth_year, sex, lifestyle)`: Unified lifespan calculation
    - Hunter-Gatherers use Siler model (Gurven & Kaplan 2007)
    - Pre-1600 non-HG use Chilean lifetables as proxy
    - Post-1600 use country-specific lifetables with year-by-year simulation

- **CountryData.py**: Classes for managing country-level demographic data

### Notebooks

- **Data Processing.ipynb**: Ingests raw data and creates processed datasets

- **LLM_Generation_Unified.ipynb**: Thin interface to generation pipeline
  - Single person generation with verbose output
  - Step-by-step generation for debugging
  - Batch generation and export

- **RandomLife.ipynb**: Demonstrates person sampling (without LLM generation)

- **LLM_Question_Answer.ipynb**: Interactive Q&A about generated people

## Usage

### Quick Start

```python
from generation import generate_person

# Generate a single person with full pipeline
person = generate_person(model='gpt-5.2', quiet=False)

# Access results
print(person.narrative)
print(person.demographics)
print(person.events)
```

### Batch Generation

```python
from generation import generate_batch

# Generate 10 people
people = generate_batch(n=10, model='gpt-5.2')

# Save results
import dill
with open('people.pkl', 'wb') as f:
    dill.dump(people, f)
```

### Step-by-Step (for debugging)

```python
from person import sample_person
from llm_utils import GenerationContext
from generation import (
    generate_geography,
    generate_demographics,
    generate_life_events,
    generate_narrative,
    quality_check
)

# Sample person and create context
person = sample_person()
ctx = GenerationContext(model='haiku', quiet=False, show_cost=True)

# Run pipeline steps individually
if person.era == 'Paleolithic':
    generate_geography(person, ctx)

generate_demographics(person, ctx)
generate_life_events(person, ctx)
generate_narrative(person, ctx)
quality_check(person, ctx)

# Print cost summary
ctx.finish()
```

## Person Object

The `Person` class stores all data for a generated person:

```python
person.era                 # 'Paleolithic' or 'Holocene'
person.birth_year          # Numeric year (negative for BCE)
person.birth_year_str      # Formatted string ("1234 AD" or "5000 BC")
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

## Key Design Choices

### Unified Person Class
A single `Person` class handles both eras:
- `person.era`: 'Paleolithic' or 'Holocene'
- `person.region`: Set for Paleolithic (None for Holocene)
- `person.location`: Set for Holocene (None for Paleolithic)
- Era-specific initialization via `_init_paleolithic()` and `_init_holocene()` methods

### Pipeline Architecture
Each generation step takes `(person, ctx)` and modifies the person in place:
1. `generate_geography()` - Paleolithic only, refines location
2. `generate_demographics()` - Asks era-appropriate questions
3. `generate_life_events()` - Probabilistic event sampling
4. `generate_narrative()` - Age-appropriate biography
5. `quality_check()` - Fix anachronisms and style issues

`GenerationContext` bundles the LLM client, cost tracker, and settings (`quiet`, `show_cost`), providing:
- `ctx.call(messages)` / `ctx.call_json(messages)` for LLM calls
- `ctx.log(message)` for conditional printing
- `ctx.finish()` for cost summary

The LLM conversation history is stored in `person.messages` for context continuity.

### Era-Specific Prompts
Prompts in `generation.py` use compositional structure:
- Base prompts + era-specific additions (e.g., `DEMOGRAPHIC_CONTEXT_BASE + DEMOGRAPHIC_CONTEXT_ERA[person.era]`)
- `DEMOGRAPHIC_QUERIES`: Single list with metadata tuples `(name, query, era, min_age, requires_dead)`
- `_get_demographic_queries(person)` filters queries based on era, age, and alive status
- Holocene uses historical records; Paleolithic uses ethnographic analogy

### Lifestyle Categories
- **Hunter-Gatherer**: Pre-agricultural populations (all Paleolithic, some Holocene)
- **Rural**: Agricultural populations
- **Urban**: City dwellers

Different mortality models apply to each lifestyle.

### Narrative Style Guidelines
The project aims for "quiet realism":
- Plain contemporary English (no archaic inversions)
- Sparse figurative language (aim: ~1 per 600 words)
- No moralizing endings or clichés—stop plainly at death
- Variable sentence rhythm (mix short and long sentences)
- Show personality through repeated actions, not summary
- Length scaled to lifespan: 150-300 words (ages 0-2), 200-400 (3-10), 400-700 (11-18), 600-1000 (19+)
- Historical context integrated throughout (~20-30% of narrative)
- Omniscient narrator: authoritative, not hedging ("likely," "probably")
- Specific actors, not vague collectives ("attempts were made" → "his sister brought a healer")

## Dependencies

- **Data processing**: numpy, scipy, xarray, rasterio, h5py, geopandas
- **LLM interaction**: langchain (anthropic, openai, google-vertexai)
- **Visualization**: matplotlib
- **Serialization**: dill (extended pickle)

## Notes

- Cost tracking is important - track per-story costs across models for budget planning
- Personality traits are percentile ranks (0-100) - extremes (<15 or >85) should be visible in narratives
- ~5% of samples are Paleolithic, ~95% Holocene (reflects actual birth distribution)

## Roadmap

### Phase 1: Core Pipeline (current)

**LLM Generation Steps** - iterate using pickled intermediates:

- [x] Person sampling and demographics generation
- [x] Life events generation
- [x] Narrative generation
- [x] Quality control pass
- [ ] **Batch generation and refinement** ← current focus

**Data Improvements** - fix before final generation:

- [ ] Paleolithic population estimates (see Known Limitations below)
- [ ] Region-specific lifetables (see Known Limitations below)
- [ ] Extend birth data to 2025 (for early 2026 release)

### Phase 2: Context & Metadata

- [ ] Historical context/notes generation ("speculative vs grounded" annotations)
- [ ] Tagging system design (era, region, age buckets, lifestyle, themes)

### Phase 3: Presentation

- [ ] Web pipeline (stories → static site)
- [ ] Cross-story editing pass (Claude reviewing N stories for clichés/repetition)
- [ ] Methodology write-up

### Phase 4: Extensions

- [ ] MC estimation tool ("what fraction of humans were X?")
- [ ] Other content (essays, visualizations)

## Development Approach

**Pickle-and-iterate**: For each pipeline step, generate ~30 people up to that step, pickle them, then iterate on prompts without re-running expensive earlier steps.

**Noticed issues list**: Track problems as they emerge (repetitive names, clichés, etc.) rather than fixing immediately - patterns will clarify what needs systematic fixes.

## Known Limitations & Future Improvements

### Paleolithic Population Estimates

**Current approach**: Regional population time series in `paleo_regions.pkl` were created by eyeballing - rough estimates without rigorous sources.

**What to improve**:
- Find better paleodemographic literature (e.g., Bocquet-Appel, various "total humans ever" estimates)
- Document sources and assumptions explicitly
- Consider regional variation (Africa vs Europe vs Asia timing of population growth)

### Life Expectancy / Mortality Calculations

**Current approach** (`lifespan.py`):
- Hunter-Gatherers: Siler model with Gurven & Kaplan 2007 parameters (good)
- Pre-1600 non-HG: Chilean lifetables at e0=22 as universal proxy (crude)
- Post-1600: Country-specific data but uses only one lifetable model per country

**What to improve**:
The raw lifetables (`Raw_Data/lifetables.csv`) contain region-specific models:
- Chilean, Far Eastern, General, North, South, West (from Coale-Demeny)
- Each has male/female variants across e0 levels 22-85

Currently `CountryData.lifetable` assigns a model to each country but the assignment may not be systematic. Could:
1. Review/improve country → lifetable model mapping
2. Use the full range of models rather than defaulting to Chilean/General
3. Document the mapping rationale

### Birth Data Coverage

**Current**: HYDE data goes to 2024
**Needed**: Extend to 2025 for early 2026 release (probably just extrapolate final year)
