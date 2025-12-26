# Random Lives Website - Setup Summary

## What Has Been Built

### Project Structure

A complete Jekyll-based static website has been set up with the following structure:

```
RandomLivesWebsite/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── _layouts/
│   ├── default.html         # Base page template
│   └── life.html            # Template for individual biographical pages
├── _lives/
│   └── example-person.md    # Example biographical story
├── assets/css/
│   └── style.css            # Site styling
├── index.html               # Homepage (lists all lives)
├── about.md                 # About page explaining the project
├── README.md                # Project documentation
├── .gitignore               # Git ignore file
└── Old_Claude.md            # Original project documentation
```

### Features Implemented

1. **Jekyll Site with Collections**
   - Lives are stored as a Jekyll collection in `_lives/`
   - Each life is a Markdown file with YAML frontmatter containing metadata
   - Automatic generation of individual life pages and homepage listing

2. **Responsive Design**
   - Clean, readable layout with good typography
   - Homepage shows preview cards for each life
   - Individual life pages display full biography with metadata

3. **Metadata Structure**
   - Each life includes: birth year, death year, age at death, location, lifestyle, era, sex
   - Supports both Paleolithic (region-based) and Holocene (country-based) people
   - Optional life events section

4. **Git Repository**
   - Repository initialized with all files committed
   - Ready to push to GitHub

### Technical Setup Completed

- ✅ Ruby 3.4.8 installed via Homebrew
- ✅ Jekyll and dependencies installed via Bundler
- ✅ Site successfully builds locally
- ✅ Git repository initialized with initial commit

## Next Steps

### 1. Create GitHub Repository and Enable GitHub Pages

**Create the repository:**
1. Go to https://github.com/new
2. Repository name: `random-lives` (or `YOUR-USERNAME.github.io` for main site)
3. Keep it public
4. **Do NOT** check "Initialize this repository with a README"
5. Click "Create repository"

**Push your code:**
```bash
cd /Users/damonbinder/Documents/RandomLivesWebsite
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git branch -M main
git push -u origin main
```

**Enable GitHub Pages:**
1. Go to repository Settings → Pages (left sidebar)
2. Under "Source": select "Deploy from a branch"
3. Under "Branch": select `main` and `/ (root)`
4. Click "Save"
5. Your site will be live at `https://YOUR-USERNAME.github.io/REPO-NAME/` in 2-5 minutes

### 2. Update Site Configuration

Edit `_config.yml` and update:
```yaml
url: "https://YOUR-USERNAME.github.io"
baseurl: "/REPO-NAME"  # Leave empty if using username.github.io
```

Commit and push:
```bash
git add _config.yml
git commit -m "Update site URL for GitHub Pages"
git push
```

### 3. Integrate with Your Python Pipeline

Create a Python script to convert your generated person objects into Jekyll posts:

**Script location:** In your Python project folder (where person.py, generation.py, etc. are)

**Script purpose:** Read pickled person objects and write them as Markdown files to `_lives/`

**Example structure:**
```python
import dill
from pathlib import Path

# Load your generated people
with open('people.pkl', 'rb') as f:
    people = dill.load(f)

# Path to Jekyll _lives directory
lives_dir = Path('/Users/damonbinder/Documents/RandomLivesWebsite/_lives')

for i, person in enumerate(people):
    # Create filename (ensure it's unique and URL-safe)
    filename = f"person-{i:04d}.md"

    # Build frontmatter
    frontmatter = f"""---
layout: life
title: "{person.demographics.get('name', f'Person {i}')}"
birth_year: "{person.birth_year_str}"
death_year: "{calculate_death_year(person)}"
age_at_death: {person.age_at_death}
"""

    # Add location info
    if person.era == 'Paleolithic':
        frontmatter += f'region: "{person.region}"\n'
    else:
        frontmatter += f'country: "{person.location.country}"\n'

    frontmatter += f"""lifestyle: "{person.lifestyle}"
era: "{person.era}"
sex: "{person.sex}"
---

{person.narrative}
"""

    # Write file
    (lives_dir / filename).write_text(frontmatter)
```

**After generating files:**
```bash
cd /Users/damonbinder/Documents/RandomLivesWebsite
git add _lives/
git commit -m "Add generated biographical stories"
git push
```

The site will automatically rebuild on GitHub Pages.

### 4. Optional Enhancements

**Add filtering/search:**
- Use JavaScript to add client-side filtering by era, location, lifestyle, etc.
- Add tags to frontmatter and create tag pages

**Improve styling:**
- Customize `assets/css/style.css`
- Add responsive navigation
- Improve mobile layout

**Add more metadata visualization:**
- Create data visualizations showing distribution of lives
- Add timeline view
- Add geographic map

**Custom domain (optional):**
- Buy a domain name
- Add CNAME file to repository
- Configure DNS settings

## Local Development

To work on the site locally:

```bash
cd /Users/damonbinder/Documents/RandomLivesWebsite

# Start local server (with new Ruby in PATH)
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle exec jekyll serve

# Site will be available at http://localhost:4000
```

**Note:** You may want to add this to your `.zshrc` to permanently set Ruby path:
```bash
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
```

## Important Files

- `_config.yml` - Site-wide settings
- `_layouts/life.html` - Template for biographical pages (customize formatting here)
- `assets/css/style.css` - All styling
- `index.html` - Homepage layout
- `_lives/*.md` - Individual biographical stories

## Git Workflow

When adding new content:
```bash
# Make changes (add files, edit content, etc.)
git add .
git commit -m "Description of changes"
git push
```

GitHub Pages will automatically rebuild (takes 1-2 minutes).

## Troubleshooting

**If site doesn't build on GitHub:**
- Check Settings → Pages for build errors
- Ensure `_config.yml` has correct `baseurl`
- Check that all Markdown files have valid frontmatter (between `---` markers)

**If Ruby/Jekyll stops working:**
```bash
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle install
```

**If you need to rebuild from scratch:**
```bash
rm -rf _site .jekyll-cache
bundle exec jekyll build
```

## Resources

- Jekyll documentation: https://jekyllrb.com/docs/
- GitHub Pages documentation: https://docs.github.com/en/pages
- Liquid template syntax: https://shopify.github.io/liquid/
- Your existing project docs: `Old_Claude.md`
