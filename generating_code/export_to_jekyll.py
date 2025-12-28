#!/usr/bin/env python3
"""Export generated person objects to Jekyll markdown files.

Usage:
    python export_to_jekyll.py input.pkl

This will read person objects from input.pkl and create markdown files
in the ../_lives/ directory for the Jekyll site.
"""

import sys
import dill
from pathlib import Path
import re


def slugify(text):
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def calculate_death_year(person):
    """Calculate death year string."""
    if person.age_at_death == "alive":
        return "alive"

    death_year = person.birth_year + person.age_at_death
    if death_year > 0:
        return f"{death_year} AD"
    else:
        return f"{1-death_year} BC"


def person_to_markdown(person, index):
    """Convert a Person object to Jekyll markdown format."""

    # Get name from demographics, or create a generic one
    name = person.demographics.get('name', f'Person {index:04d}')

    # Create filename
    filename = f"{index:04d}-{slugify(name)}.md"

    # Build frontmatter
    frontmatter = f"""---
layout: life
title: "{name}"
birth_year: "{person.birth_year_str}"
death_year: "{calculate_death_year(person)}"
age_at_death: {person.age_at_death}
"""

    # Add location info
    if person.era == 'Paleolithic':
        frontmatter += f'region: "{person.region}"\n'
    else:
        frontmatter += f'country: "{person.location.country}"\n'

    # Add other metadata
    frontmatter += f"""lifestyle: "{person.lifestyle}"
era: "{person.era}"
sex: "{person.sex}"
"""

    # Add events if present
    if person.events:
        frontmatter += "events:\n"
        for event in person.events:
            # Escape quotes in events
            event_clean = event.replace('"', '\\"')
            frontmatter += f'  - "{event_clean}"\n'

    frontmatter += "---\n\n"

    # Add narrative
    narrative = person.narrative if person.narrative else "No narrative available."

    return filename, frontmatter + narrative


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
        print("Usage: python export_to_jekyll.py <pickle_file>")
        print("\nExample:")
        print("  python export_to_jekyll.py test_examples_story.pkl")
        sys.exit(1)

    pickle_file = sys.argv[1]
    output_dir = '../_lives'  # Jekyll lives directory

    if not Path(pickle_file).exists():
        print(f"Error: {pickle_file} not found")
        sys.exit(1)

    export_to_jekyll(pickle_file, output_dir)
