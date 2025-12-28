"""Date formatting utilities for the export pipeline.

This module contains lightweight formatting functions that don't require
heavy data dependencies like location.py or person.py.
"""

from datetime import date, timedelta


def _format_year(year):
    """Format year as 'YYYY AD' or 'YYYY BC'."""
    if year >= 1:
        return f"{year} AD"
    else:
        return f"{-year + 1} BC"


def _format_date_tuple(date_tuple):
    """Format (year, day_of_year) tuple as readable date string.

    Args:
        date_tuple: (year, day_of_year) where day_of_year is 1-365 (or 1-366)

    Returns:
        String like "March 15, 1834 AD" or "July 4, 5000 BC"
    """
    year, day_of_year = date_tuple

    # Use a non-leap year as reference (year 1 is non-leap)
    # This handles the conversion from day_of_year to month/day
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # Leap year
        reference_year = 2000
    else:
        # Non-leap year
        reference_year = 1999

    # Convert day of year to actual date
    reference_date = date(reference_year, 1, 1) + timedelta(days=day_of_year - 1)
    month_name = reference_date.strftime("%B")
    day = reference_date.day

    # Format with year suffix
    year_str = _format_year(year)

    return f"{month_name} {day}, {year_str}"
