"""Date and calendar utilities.

This module handles all date-related operations including:
- Calendar arithmetic (leap years, day counting)
- Date formatting (year, month/day display)
- Date sampling (birth and death dates)

All dates are represented as (year, day_of_year) tuples where:
- year: Integer year (negative for BCE, e.g., -500 = 501 BC)
- day_of_year: Day within year (1-365 or 1-366 for leap years)
"""

import numpy as np


# =============================================================================
# Calendar Arithmetic
# =============================================================================

def _is_leap_year(year):
    """Check if a year is a leap year (works for negative years)."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_in_year(year):
    """Get number of days in a year."""
    return 366 if _is_leap_year(year) else 365


def _add_days_to_date(year, day_of_year, days_to_add):
    """Add days to a date, handling year rollovers.

    Args:
        year: Year (can be negative for BCE)
        day_of_year: Day within year (1-365/366)
        days_to_add: Number of days to add

    Returns:
        (new_year, new_day_of_year) tuple
    """
    new_day = day_of_year + days_to_add
    new_year = year

    # Handle year rollover
    while new_day > _days_in_year(new_year):
        new_day -= _days_in_year(new_year)
        new_year += 1

    return (new_year, new_day)


def _day_of_year_to_month_day(year, day_of_year):
    """Convert day of year to (month_name, day) tuple."""
    days_in_months = [31, 29 if _is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]

    day_count = 0
    for month_idx, days in enumerate(days_in_months):
        if day_of_year <= day_count + days:
            return month_names[month_idx], day_of_year - day_count
        day_count += days

    # Shouldn't happen, but fallback
    return "December", 31


# =============================================================================
# Date Formatting
# =============================================================================

def _format_year(year):
    """Format year as string (e.g., '1500 AD' or '8000 BC')."""
    if year > 0:
        return f"{year} AD"
    else:
        return f"{1-year} BC"


def _format_date_tuple(date_tuple):
    """Format a (year, day_of_year) tuple to readable string.

    Returns string like "March 15, 1834 AD" or "July 4, 5000 BC".
    Returns None if date_tuple is None.
    """
    if date_tuple is None:
        return None

    year, day_of_year = date_tuple
    month, day = _day_of_year_to_month_day(year, day_of_year)
    return f"{month} {day}, {_format_year(year)}"


# =============================================================================
# Date Sampling
# =============================================================================

def _sample_birth_date(year):
    """Sample a birth date within the given year.

    Returns (year, day_of_year) tuple where day_of_year is 1-365 (or 1-366 for leap years).
    Works for all years including BCE (negative years).
    """
    days_in_year = _days_in_year(year)
    day_of_year = np.random.randint(1, days_in_year + 1)
    return (year, day_of_year)


def _sample_death_date(birth_date, age_at_death, lifestyle='Rural'):
    """Sample a death date given birth date and age at death.

    For infants (age < 1), uses realistic neonatal/post-neonatal distribution.
    For others, uses uniform distribution within the death year.

    Returns (year, day_of_year) tuple, or None if person is still alive.
    """
    if age_at_death == "alive":
        return None

    birth_year, birth_day = birth_date

    if age_at_death < 1:
        # Infant death - use neonatal/post-neonatal model
        # Neonatal fraction: ~0.55 as compromise for historical populations
        neonatal_fraction = 0.55

        if np.random.random() < neonatal_fraction:
            # Neonatal death (0-27 days): 40% day 0, exponential decay for days 1-27
            if np.random.random() < 0.40:
                days_lived = 0
            else:
                days_lived = min(1 + int(np.random.exponential(5)), 27)
        else:
            # Post-neonatal death (28-365 days): uniform distribution
            days_lived = np.random.randint(28, 366)

        return _add_days_to_date(birth_year, birth_day, days_lived)
    else:
        # Non-infant - uniform random date within the death year
        death_year = birth_year + int(age_at_death)
        death_day = np.random.randint(1, _days_in_year(death_year) + 1)

        # Ensure death is after birthday by moving to next year if needed
        if death_day < birth_day:
            death_year += 1

        return (death_year, death_day)
