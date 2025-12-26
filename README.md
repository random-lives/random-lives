# Random Lives Website

A Jekyll-based website displaying biographical stories of randomly sampled people from across all of human history (200,000 BCE to present), weighted by actual birth numbers.

## Project Overview

This website is part of the Random Lives project, which aims to provide an accurate statistical picture of human experience through:

- Randomly sampled birth years weighted by historical population data
- Era-appropriate demographics and lifespans
- Detailed biographical narratives generated through a multi-step LLM pipeline

See `Old_Claude.md` for detailed project documentation.

## Local Development

### Prerequisites

- Ruby 3.0 or higher
- Bundler

### Setup

```bash
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000` in your browser.

## Project Structure

- `_lives/` - Individual biographical stories (Markdown files with YAML frontmatter)
- `_layouts/` - Page templates
- `assets/css/` - Stylesheets
- `_config.yml` - Jekyll configuration

## Adding New Lives

To add a new biographical story, create a new file in `_lives/` with the following format:

```markdown
---
layout: life
title: "Person Name"
birth_year: "YYYY AD/BC"
death_year: "YYYY AD/BC"
age_at_death: XX
country: "Country"
region: "Region" (for Paleolithic)
lifestyle: "Hunter-Gatherer/Rural/Urban"
era: "Paleolithic/Holocene"
sex: "M/F"
---

Biographical narrative goes here...
```

## Deployment

This site is deployed using GitHub Pages. Push to the `main` branch to deploy.

## License

TBD
