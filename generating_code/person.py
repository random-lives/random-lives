"""Person sampling and representation for historical demography.

Simple unified sampling: sample a birth year weighted by births across all history,
then create a Person with era-appropriate attributes.

Usage:
    person = sample_person()  # Sample from all of human history
"""

import numpy as np
import dill
import h5py
from datetime import date, timedelta

from lifespan import age_at_death
from location import Location


# =============================================================================
# Load Data
# =============================================================================

# Unified birth data
with open('Processed_Data/unified_births.pkl', 'rb') as f:
    _unified = dill.load(f)

_years = _unified['years']
_cumulative = _unified['cumulative_births']
_total_births = _unified['total_births']
_transition_year = _unified['transition_year']  # Paleolithic/Holocene boundary

# Paleolithic regional data
with open('Processed_Data/paleo_regions.pkl', 'rb') as f:
    _paleo_data = dill.load(f)

# Holocene spatial data
with h5py.File('Processed_Data/births_array.h5', 'r') as f:
    _births_array = f['data'][:]

with h5py.File('Processed_Data/hg_array.h5', 'r') as f:
    _hg_array = f['data'][:]

# HYDE years and data
import xarray as xr
_hyde_ds = xr.open_dataset('Raw_Data/HYDE34/NetCDF/population.nc', decode_times=False, chunks={})
_hyde_years = (_hyde_ds['population'].time.values // 365).astype(int) + 1

_hyde = {}
for f in ["population", "urban_population", "cropland", "pasture", "rangeland",
          "urban_area", "irrigated_not_rice", "irrigated_rice",
          "rainfed_not_rice", "rainfed_rice"]:
    ds = xr.open_dataset('Raw_Data/HYDE34/NetCDF/' + f + '.nc', decode_times=False, chunks={})
    _hyde[f] = ds[list(ds.data_vars)[0]]


# =============================================================================
# Helper Functions
# =============================================================================

PERSONALITY_TRAITS = ['Openness', 'Conscientiousness', 'Extraversion',
                      'Agreeableness', 'Neuroticism', 'Honesty-Humility', 'Intelligence']

HYDE_LAND_USE_FIELDS = ['cropland', 'pasture', 'rangeland', 'urban_area',
                        'irrigated_not_rice', 'irrigated_rice',
                        'rainfed_not_rice', 'rainfed_rice']

def _sample_personality():
    """Sample personality traits (percentile ranks)."""
    return {f'{trait} (% rank)': np.random.randint(0, 101) for trait in PERSONALITY_TRAITS}


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


def _hyde_indices(year):
    """Get HYDE time indices for interpolation."""
    idx = np.searchsorted(_hyde_years, year)
    if idx < len(_hyde_years) and _hyde_years[idx] == year:
        return (idx, None)
    return (idx - 1, idx)


# =============================================================================
# Person Class
# =============================================================================

class Person:
    """A person from human history."""

    def __init__(self, year):
        self.birth_year = year
        self.birth_year_str = _format_year(year)
        self.sex = 'M' if np.random.random() < 0.512 else 'F'
        self.era = 'Paleolithic' if year < _transition_year else 'Holocene'

        # Era-specific initialization (sets age_at_death)
        if self.era == 'Paleolithic':
            self._init_paleolithic()
        else:
            self._init_holocene()

        # Generate birth and death dates
        self.birth_date = _sample_birth_date(year)
        self.death_date = _sample_death_date(self.birth_date, self.age_at_death, self.lifestyle)

        # Sample personality after age_at_death is set
        if self.years_lived() > 2:
            self.personality = _sample_personality()
        else:
            self.personality = {}

        # Populated by LLM pipeline
        self.demographics = {}
        self.events = []
        self.narrative = None
        self.messages = []  # LLM conversation history

    def _init_paleolithic(self):
        """Initialize Paleolithic-specific attributes."""
        self.lifestyle = 'Hunter-Gatherer'
        self.region = self._sample_paleo_region()
        self.location = None  # No grid-level data for Paleolithic
        self.age_at_death = age_at_death(None, self.birth_year, self.sex, self.lifestyle)

    def _init_holocene(self):
        """Initialize Holocene-specific attributes."""
        self.row, self.col = self._sample_holocene_location()
        self.location = Location(self.row, self.col)
        self.region = None  # Use location instead
        self.lifestyle = self._sample_lifestyle()
        self.age_at_death = age_at_death(
            self.location.country, self.birth_year, self.sex, self.lifestyle
        )

    def _sample_paleo_region(self):
        """Sample region weighted by population at birth year."""
        regions = _paleo_data['regions']
        regional_data = _paleo_data['regional_data']
        kya = (2000 - self.birth_year) / 1000  # thousands of years ago

        pop_weights = {}
        for region in regions:
            xs = regional_data[region]['xs']
            ys = regional_data[region]['ys']
            pop = np.interp(kya, xs[::-1], ys[::-1])
            pop_weights[region] = max(0, pop)

        total = sum(pop_weights.values())
        if total == 0:
            return np.random.choice(regions)

        probs = [pop_weights[r] / total for r in regions]
        return np.random.choice(regions, p=probs)

    def _sample_holocene_location(self):
        """Sample grid cell weighted by births."""
        idx1, idx2 = _hyde_indices(self.birth_year)

        if idx2 is None:
            birth_map = _births_array[idx1]
        else:
            gap = _hyde_years[idx2] - _hyde_years[idx1]
            w1 = (_hyde_years[idx2] - self.birth_year) / gap
            birth_map = w1 * _births_array[idx1] + (1 - w1) * _births_array[idx2]

        weights = birth_map.flatten()
        weights = weights / weights.sum()
        flat_idx = np.random.choice(len(weights), p=weights)
        return np.unravel_index(flat_idx, birth_map.shape)

    def _sample_lifestyle(self):
        """Determine lifestyle (Urban, Rural, or Hunter-Gatherer)."""
        idx1, idx2 = _hyde_indices(self.birth_year)

        urban_pop = np.nan_to_num(_hyde["urban_population"].isel(time=idx1).values)[self.row, self.col]
        total_pop = np.nan_to_num(_hyde["population"].isel(time=idx1).values)[self.row, self.col]
        w1 = 0

        if idx2 is not None:
            gap = _hyde_years[idx2] - _hyde_years[idx1]
            w1 = (_hyde_years[idx2] - self.birth_year) / gap
            urban_pop *= w1
            total_pop *= w1
            urban_pop += (1 - w1) * np.nan_to_num(_hyde["urban_population"].isel(time=idx2).values)[self.row, self.col]
            total_pop += (1 - w1) * np.nan_to_num(_hyde["population"].isel(time=idx2).values)[self.row, self.col]

        if total_pop > 0 and np.random.random() < urban_pop / total_pop:
            return "Urban"

        # Check hunter-gatherer status (only for early periods)
        if w1 < 0.5 and idx1 < 50:
            if _hg_array[idx1][self.row, self.col] == 1:
                return "Hunter-Gatherer"
        elif w1 >= 0.5 and idx2 is not None and idx2 < 50:
            if _hg_array[idx2][self.row, self.col] == 1:
                return "Hunter-Gatherer"

        return "Rural"

    def _get_hyde_slice(self, file_name, idx, size):
        """Get HYDE data slice at given time index."""
        if size == 0:
            return np.array(_hyde[file_name].isel(time=idx)[self.row, self.col])
        data = _hyde[file_name].isel(time=idx)[
            self.row - size:self.row + size + 1,
            self.col - size:self.col + size + 1
        ]
        return np.sum(np.nan_to_num(data))

    def hyde_value(self, file_name, size=0):
        """Get HYDE data value for this location and time (Holocene only)."""
        if self.era == 'Paleolithic':
            return None

        idx1, idx2 = _hyde_indices(self.birth_year)
        v1 = self._get_hyde_slice(file_name, idx1, size)

        if idx2 is None:
            return v1

        v2 = self._get_hyde_slice(file_name, idx2, size)
        w1 = (_hyde_years[idx2] - self.birth_year) / (_hyde_years[idx2] - _hyde_years[idx1])
        return w1 * v1 + (1 - w1) * v2

    def years_lived(self):
        """Return years lived (handles 'alive' status)."""
        if self.age_at_death == "alive":
            return 2025 - self.birth_year
        return self.age_at_death

    def is_alive(self):
        """Check if person is still living."""
        return self.age_at_death == "alive"

    def age_category(self):
        """Get age category for narrative prompts."""
        age = self.years_lived()
        if age < 3:
            return "infant"
        elif age <= 10:
            return "child"
        elif age <= 18:
            return "adolescent"
        else:
            return "adult"


    def to_dict(self):
        """Export person as flat dict for LLM prompts."""
        output = {
            'Era': self.era,
            'Birth year': self.birth_year_str,
            'Birth date': _format_date_tuple(self.birth_date),
            'Age at death': self.age_at_death,
            'Death date': _format_date_tuple(self.death_date),
            'Sex': self.sex,
            'Lifestyle': self.lifestyle,
        }
        
        if self.era == 'Paleolithic':
            output['Region'] = self.region
        else:
            loc = self.location
            output['Birthplace latitude'] = loc.lat
            output['Birthplace longitude'] = loc.lon
            output['Birthplace modern region'] = loc.subregion
            output['Birthplace modern country'] = loc.country
            output['Birthplace modern address'] = loc.address
            output['Birthplace altitude'] = loc.altitude()

            biome, ecotype = loc.biome()
            output['Birthplace biome'] = biome
            output['Birthplace ecotype'] = ecotype

            clim_data = loc.climate()
            for key, val in clim_data.items():
                output['Birthplace ' + key.lower()] = val

            output['Birthplace map url'] = loc.gmap_url()

            # HYDE land use data
            averaging_size = 1
            area = loc.local_land_area(averaging_size)

            output['Birthplace population density'] = np.round(
                self.hyde_value('population', averaging_size) / area, 2
            )

            for f in HYDE_LAND_USE_FIELDS:
                output['Birthplace ' + f + ' percentage'] = np.round(
                    100 * self.hyde_value(f, averaging_size) / area, 2
                )

        output.update(self.personality)
        output.update(self.demographics)
        return output

    def to_prompt_string(self):
        """Format person for LLM prompt context."""
        return "\n".join(f"{k}: {v}" for k, v in self.to_dict().items())


# =============================================================================
# Sampling Functions
# =============================================================================

def sample_year():
    """Sample a birth year weighted by births across all human history."""
    draw = np.random.random() * _total_births
    year = np.interp(draw, _cumulative, _years)
    return int(np.round(year))


def sample_person():
    """Sample a random person from all of human history."""
    return Person(sample_year())
