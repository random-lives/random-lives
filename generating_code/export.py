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
from location import _ensure_data_loaded


def slugify(text):
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def person_to_markdown(person, index):
    """Convert a Person object to Jekyll markdown format."""

    # Get name from demographics, or create a generic one
    name = person.demographics.get('name', f'Person {index:04d}')

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

    # Add other metadata (not displayed but kept for filtering/sorting)
    frontmatter += f"""lifestyle: "{person.lifestyle}"
era: "{person.era}"
sex: "{person.sex}"
"""

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

    # Ensure geographic data is loaded for to_dict() calls
    print("Loading geographic data...")
    _ensure_data_loaded()

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

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
