"""Lifespan calculation module for historical demography simulations."""

import csv
import numpy as np
import re
import dill

AGES = np.arange(121)

# Siler model parameters from Gurven and Kaplan 2007
HG_SILER_PARAMS = (0.422, 0.013, 1.47e-4, 1.131, 0.086)

# Load country data at module import
with open('Processed_Data/processed_p1600_data.pkl', 'rb') as f:
    COUNTRY_DATA = dill.load(f)


def load_lifetable_data(filepath='Raw_Data/lifetables.csv'):
    """Load lifetable data from CSV file."""
    lifetable_data = {}
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            key = (row[1], row[3][0], int(row[4]))
            if key in lifetable_data:
                lifetable_data[key].append(float(row[7]))
            else:
                lifetable_data[key] = [float(row[7])]
    return lifetable_data


def make_Sx(qx):
    """Convert mortality rates (qx) to survival function (Sx)."""
    Sx = [1.0]
    for i in AGES:
        Sx.append(Sx[-1] * (1 - qx[i]))
    return np.array(Sx)


def make_Px(Sx):
    """Convert survival function (Sx) to death age distribution (Px)."""
    Px = Sx[:-1] - Sx[1:]
    return Px / np.sum(Px)


def sample_age(death_table):
    """Sample an age at death from a probability distribution."""
    return np.random.choice(AGES, p=death_table)


def siler_Sx(x, params):
    """Calculate survival function using the Siler mortality model."""
    a1, a2, a3, b1, b3 = params
    output = np.exp(-a1 / b1 * (1 - np.exp(-b1 * x)))
    output *= np.exp(-a2 * x)
    output *= np.exp(a3 / b3 * (1 - np.exp(b3 * x)))
    return output


def to_numeric_year(birth_year_str):
    """Convert birth year string (e.g., '1500 AD' or '500 BC') to numeric year."""
    if 'AD' in birth_year_str:
        return int(re.sub(r'\D', '', birth_year_str))
    else:
        return 1 - int(re.sub(r'\D', '', birth_year_str))


class LifespanCalculator:
    """Calculator for historical lifespan simulations."""

    def __init__(self, lifetable_path='Raw_Data/lifetables.csv', country_data=None):
        self.lifetable_data = load_lifetable_data(lifetable_path)
        self.country_data = country_data

        # Pre-compute hunter-gatherer death distribution
        hg_Sx = siler_Sx(np.arange(122), HG_SILER_PARAMS)
        self.hg_Px = make_Px(hg_Sx)

        # Pre-compute pre-modern death distributions (Chilean data as proxy)
        self.premod_M_Px = make_Px(make_Sx(self.lifetable_data[('Chilean', 'M', 22)]))
        self.premod_F_Px = make_Px(make_Sx(self.lifetable_data[('Chilean', 'F', 22)]))

    def age_at_death(self, country, birth_year, sex, lifestyle):
        """Calculate age at death for a person based on their demographics."""
        if isinstance(birth_year, str):
            birth_year = to_numeric_year(birth_year)

        if lifestyle == "Hunter-Gatherer":
            return sample_age(self.hg_Px)

        if birth_year > 1600 and self.country_data is not None:
            return self._calculate_modern_death(country, birth_year, sex)

        if sex == 'M':
            return sample_age(self.premod_M_Px)
        else:
            return sample_age(self.premod_F_Px)

    def _calculate_modern_death(self, country, birth_year, sex):
        """Calculate age at death for post-1600 births using country-specific data."""
        if country not in self.country_data:
            if sex == 'M':
                return sample_age(self.premod_M_Px)
            else:
                return sample_age(self.premod_F_Px)

        current_age = 0
        current_year = birth_year
        model = self.country_data[country].lifetable

        for _ in range(200):
            life_expectancy = int(np.floor(self.country_data[country].LE_f(current_year)))
            life_expectancy = max(22, min(life_expectancy, 85))

            try:
                p_death = self.lifetable_data[(model, sex, life_expectancy)][current_age]
            except (KeyError, IndexError):
                p_death = 0.01

            if np.random.random() < p_death:
                return current_age
            else:
                current_age += 1
                current_year += 1

            if current_year > 2024:
                return "alive"

        return current_age


# Module-level convenience functions

_calculator = None


def get_calculator(lifetable_path='Raw_Data/lifetables.csv'):
    """Get or create a singleton LifespanCalculator instance."""
    global _calculator
    if _calculator is None:
        _calculator = LifespanCalculator(lifetable_path, COUNTRY_DATA)
    return _calculator


def age_at_death(country, birth_year, sex, lifestyle):
    """Calculate age at death (convenience function)."""
    calc = get_calculator()
    return calc.age_at_death(country, birth_year, sex, lifestyle)
