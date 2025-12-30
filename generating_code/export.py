#!/usr/bin/env python3
"""Export generated person objects to Jekyll markdown files.

Usage:
    python export.py input.pkl

This will read person objects from input.pkl and create markdown files
in the ../_lives/ directory for the Jekyll site.
"""

import sys
import dill
from pathlib import Path
import re
import yaml

from date_utils import _format_date_tuple, _format_year


# Country to continent mapping
COUNTRY_TO_CONTINENT = {
    # Africa
    'Algeria': 'Africa', 'Angola': 'Africa', 'Benin': 'Africa', 'Botswana': 'Africa',
    'Burkina Faso': 'Africa', 'Burundi': 'Africa', 'Cameroon': 'Africa', 'Cape Verde': 'Africa',
    'Central African Republic': 'Africa', 'Chad': 'Africa', 'Comoros': 'Africa',
    "Cote d'Ivoire": 'Africa', 'Democratic Republic of the Congo': 'Africa', 'Djibouti': 'Africa',
    'Egypt': 'Africa', 'Equatorial Guinea': 'Africa', 'Eritrea': 'Africa', 'Eswatini': 'Africa',
    'Ethiopia': 'Africa', 'Gabon': 'Africa', 'Gambia': 'Africa', 'Ghana': 'Africa',
    'Guinea': 'Africa', 'Guinea-Bissau': 'Africa', 'Kenya': 'Africa', 'Lesotho': 'Africa',
    'Liberia': 'Africa', 'Libya': 'Africa', 'Madagascar': 'Africa', 'Malawi': 'Africa',
    'Mali': 'Africa', 'Mauritania': 'Africa', 'Mauritius': 'Africa', 'Morocco': 'Africa',
    'Mozambique': 'Africa', 'Namibia': 'Africa', 'Niger': 'Africa', 'Nigeria': 'Africa',
    'Republic of the Congo': 'Africa', 'Rwanda': 'Africa', 'Sao Tome and Principe': 'Africa',
    'Senegal': 'Africa', 'Seychelles': 'Africa', 'Sierra Leone': 'Africa', 'Somalia': 'Africa',
    'South Africa': 'Africa', 'South Sudan': 'Africa', 'Sudan': 'Africa', 'Tanzania': 'Africa',
    'Togo': 'Africa', 'Tunisia': 'Africa', 'Uganda': 'Africa', 'Zambia': 'Africa', 'Zimbabwe': 'Africa',

    # Asia
    'Afghanistan': 'Asia', 'Armenia': 'Asia', 'Azerbaijan': 'Asia', 'Bahrain': 'Asia',
    'Bangladesh': 'Asia', 'Bhutan': 'Asia', 'Brunei': 'Asia', 'Cambodia': 'Asia',
    'China': 'Asia', 'Cyprus': 'Asia', 'Georgia': 'Asia', 'India': 'Asia', 'Indonesia': 'Asia',
    'Iran': 'Asia', 'Iraq': 'Asia', 'Israel': 'Asia', 'Japan': 'Asia', 'Jordan': 'Asia',
    'Kazakhstan': 'Asia', 'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia', 'Laos': 'Asia',
    'Lebanon': 'Asia', 'Malaysia': 'Asia', 'Maldives': 'Asia', 'Mongolia': 'Asia',
    'Myanmar': 'Asia', 'Nepal': 'Asia', 'North Korea': 'Asia', 'Oman': 'Asia',
    'Pakistan': 'Asia', 'Palestine': 'Asia', 'Philippines': 'Asia', 'Qatar': 'Asia',
    'Saudi Arabia': 'Asia', 'Singapore': 'Asia', 'South Korea': 'Asia', 'Sri Lanka': 'Asia',
    'Syria': 'Asia', 'Taiwan': 'Asia', 'Tajikistan': 'Asia', 'Thailand': 'Asia',
    'Timor-Leste': 'Asia', 'Turkey': 'Asia', 'Turkmenistan': 'Asia',
    'United Arab Emirates': 'Asia', 'Uzbekistan': 'Asia', 'Vietnam': 'Asia', 'Yemen': 'Asia',

    # Europe
    'Albania': 'Europe', 'Andorra': 'Europe', 'Austria': 'Europe', 'Belarus': 'Europe',
    'Belgium': 'Europe', 'Bosnia and Herzegovina': 'Europe', 'Bulgaria': 'Europe',
    'Croatia': 'Europe', 'Czech Republic': 'Europe', 'Denmark': 'Europe', 'Estonia': 'Europe',
    'Finland': 'Europe', 'France': 'Europe', 'Germany': 'Europe', 'Greece': 'Europe',
    'Hungary': 'Europe', 'Iceland': 'Europe', 'Ireland': 'Europe', 'Italy': 'Europe',
    'Kosovo': 'Europe', 'Latvia': 'Europe', 'Liechtenstein': 'Europe', 'Lithuania': 'Europe',
    'Luxembourg': 'Europe', 'Malta': 'Europe', 'Moldova': 'Europe', 'Monaco': 'Europe',
    'Montenegro': 'Europe', 'Netherlands': 'Europe', 'North Macedonia': 'Europe',
    'Norway': 'Europe', 'Poland': 'Europe', 'Portugal': 'Europe', 'Romania': 'Europe',
    'Russia': 'Europe', 'San Marino': 'Europe', 'Serbia': 'Europe', 'Slovakia': 'Europe',
    'Slovenia': 'Europe', 'Spain': 'Europe', 'Sweden': 'Europe', 'Switzerland': 'Europe',
    'Ukraine': 'Europe', 'United Kingdom': 'Europe', 'Vatican City': 'Europe',

    # North America
    'Antigua and Barbuda': 'North America', 'Bahamas': 'North America', 'Barbados': 'North America',
    'Belize': 'North America', 'Canada': 'North America', 'Costa Rica': 'North America',
    'Cuba': 'North America', 'Dominica': 'North America', 'Dominican Republic': 'North America',
    'El Salvador': 'North America', 'Grenada': 'North America', 'Guatemala': 'North America',
    'Haiti': 'North America', 'Honduras': 'North America', 'Jamaica': 'North America',
    'Mexico': 'North America', 'Nicaragua': 'North America', 'Panama': 'North America',
    'Saint Kitts and Nevis': 'North America', 'Saint Lucia': 'North America',
    'Saint Vincent and the Grenadines': 'North America', 'Trinidad and Tobago': 'North America',
    'United States': 'North America',

    # South America
    'Argentina': 'South America', 'Bolivia': 'South America', 'Brazil': 'South America',
    'Chile': 'South America', 'Colombia': 'South America', 'Ecuador': 'South America',
    'Guyana': 'South America', 'Paraguay': 'South America', 'Peru': 'South America',
    'Suriname': 'South America', 'Uruguay': 'South America', 'Venezuela': 'South America',

    # Oceania
    'Australia': 'Oceania', 'Fiji': 'Oceania', 'Kiribati': 'Oceania',
    'Marshall Islands': 'Oceania', 'Micronesia': 'Oceania', 'Nauru': 'Oceania',
    'New Zealand': 'Oceania', 'Palau': 'Oceania', 'Papua New Guinea': 'Oceania',
    'Samoa': 'Oceania', 'Solomon Islands': 'Oceania', 'Tonga': 'Oceania',
    'Tuvalu': 'Oceania', 'Vanuatu': 'Oceania',
}


def get_era_tag(birth_year):
    """Convert numeric birth year to era tag string."""
    if birth_year < -10000:
        return "Paleolithic (before 10,000 BC)"
    elif birth_year < -3000:
        return "Neolithic (10,000–3,000 BC)"
    elif birth_year < -1000:
        return "Ancient (3,000–1,000 BC)"
    elif birth_year < 500:
        return "Antiquity (1,000 BC–500 AD)"
    elif birth_year < 1500:
        return "Medieval (500–1500)"
    elif birth_year < 1800:
        return "Early Modern (1500–1800)"
    elif birth_year < 1900:
        return "19th Century"
    elif birth_year < 2000:
        return "20th Century"
    else:
        return "21st Century"


def get_age_tag(age_at_death):
    """Convert age at death to age tag string."""
    if age_at_death == "alive":
        return "Alive"
    elif age_at_death <= 1:
        return "Infant (0–1)"
    elif age_at_death <= 10:
        return "Child (2–10)"
    elif age_at_death <= 18:
        return "Adolescent (11–18)"
    elif age_at_death <= 49:
        return "Adult (19–49)"
    else:
        return "Elder (50+)"


def get_continent(country, region=None):
    """Get continent from country name, with fallback for Paleolithic regions."""
    if country:
        return COUNTRY_TO_CONTINENT.get(country, "Unknown")
    elif region:
        # Paleolithic regions map directly to continents
        region_to_continent = {
            'Africa': 'Africa',
            'Europe': 'Europe',
            'Asia': 'Asia',
            'Oceania': 'Oceania',
            'Americas': 'Americas',
        }
        return region_to_continent.get(region, "Unknown")
    return "Unknown"


def slugify(text):
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def person_to_markdown(person, index):
    """Convert a Person object to Jekyll markdown format."""

    # Get name from person object, or create a generic one
    if person.name:
        name = person.name
    elif person.naming_category == 'unnamed':
        name = f'Person {index:04d} (unnamed)'
    else:
        name = f'Person {index:04d}'

    # Create filename
    filename = f"{index:04d}-{slugify(name)}.md"

    # Calculate death year
    death_year = "alive" if person.age_at_death == "alive" else _format_year(person.death_date[0])

    # Build frontmatter
    frontmatter = f"""---
layout: life
title: "{name}"
birth_year: "{person.birth_year_str}"
death_year: "{death_year}"
age_at_death: {person.age_at_death}
birth_date: "{_format_date_tuple(person.birth_date)}"
"""

    # Add death date if applicable
    if person.death_date is not None:
        frontmatter += f'death_date: "{_format_date_tuple(person.death_date)}"\n'

    # Add location info
    if person.era == 'Paleolithic':
        frontmatter += f'region: "{person.region}"\n'
        if 'Subregion' in person.demographics and person.demographics['Subregion']:
            frontmatter += f'subregion: "{person.demographics["Subregion"]}"\n'
        if 'Subsubregion' in person.demographics and person.demographics['Subsubregion']:
            frontmatter += f'subsubregion: "{person.demographics["Subsubregion"]}"\n'
    else:
        # Use detailed address if available, otherwise fall back to subregion/country
        if person.location.address:
            full_location = person.location.address
        else:
            location_parts = [p for p in [person.location.subregion, person.location.country] if p]
            full_location = ', '.join(location_parts)

        frontmatter += f'location: "{full_location}"\n'
        frontmatter += f'country: "{person.location.country}"\n'
        frontmatter += f'latitude: {person.location.lat}\n'
        frontmatter += f'longitude: {person.location.lon}\n'
        frontmatter += f'map_url: "{person.location.gmap_url()}"\n'

    # Add other metadata (not displayed but kept for filtering/sorting)
    frontmatter += f'lifestyle: "{person.lifestyle}"\n'
    frontmatter += f'era: "{person.era}"\n'
    frontmatter += f'sex: "{person.sex}"\n'

    # Add computed tags for filtering
    era_tag = get_era_tag(person.birth_year)
    age_tag = get_age_tag(person.age_at_death)
    country = person.location.country if person.era == 'Holocene' else None
    region = person.region if person.era == 'Paleolithic' else None
    continent = get_continent(country, region)

    frontmatter += f'era_tag: "{era_tag}"\n'
    frontmatter += f'age_tag: "{age_tag}"\n'
    frontmatter += f'continent: "{continent}"\n'

    # Add debugging information as YAML comments (not parsed by Jekyll)
    frontmatter += "\n# Debug information (not displayed on page):\n"

    # Export full person data as YAML
    try:
        person_dict = person.to_dict()

        # Convert numpy types to native Python types for clean YAML
        def convert_value(v):
            if hasattr(v, 'item'):  # numpy scalar
                return v.item()
            elif isinstance(v, (list, tuple)):
                return [convert_value(x) for x in v]
            elif isinstance(v, dict):
                return {k: convert_value(val) for k, val in v.items()}
            else:
                return v

        clean_dict = {k: convert_value(v) for k, v in person_dict.items()}

        yaml_str = yaml.dump(clean_dict, default_flow_style=False, allow_unicode=True, sort_keys=True)

        # Prefix each line with "# " to make it a comment
        for line in yaml_str.split('\n'):
            if line.strip():  # Skip empty lines
                frontmatter += f"# {line}\n"
    except (TypeError, AttributeError) as e:
        # Fallback: include basic serializable attributes
        frontmatter += f"# Error calling to_dict(): {e}\n"
        frontmatter += f"# personality: {person.personality}\n"
        frontmatter += f"# demographics: {person.demographics}\n"
        frontmatter += f"# events: {person.events}\n"

    frontmatter += "---\n\n"

    return filename, frontmatter + person.narrative


def export_to_jekyll(pickle_path, output_dir):
    """Export all people from pickle file to Jekyll markdown files."""

    # Load people
    print(f"Loading people from {pickle_path}...")
    with open(pickle_path, 'rb') as f:
        people = dill.load(f)

    print(f"Found {len(people)} people")

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Remove all existing markdown files
    print(f"Removing existing markdown files from {output_dir}...")
    removed = 0
    for md_file in output_path.glob('*.md'):
        md_file.unlink()
        removed += 1
    print(f"  Removed {removed} files")

    # Export each person
    exported = 0
    for i, person in enumerate(people):
        # Only export if narrative exists
        if person.narrative:
            filename, content = person_to_markdown(person, i)
            filepath = output_path / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            exported += 1
            if (i + 1) % 10 == 0:
                print(f"  Exported {exported} people...")

    print(f"\nSuccessfully exported {exported} people to {output_dir}")
    return exported


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python export.py <pickle_file>")
        print("\nExample:")
        print("  python export.py test_examples.pkl")
        sys.exit(1)

    pickle_file = sys.argv[1]
    output_dir = '../_lives'  # Jekyll lives directory

    if not Path(pickle_file).exists():
        print(f"Error: {pickle_file} not found")
        sys.exit(1)

    export_to_jekyll(pickle_file, output_dir)
