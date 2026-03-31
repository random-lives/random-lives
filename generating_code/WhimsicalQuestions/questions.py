"""
Question definitions for the "What fraction of humans have ever..." blog post.

Each question specifies:
- id: unique identifier
- short: display name for results table
- prompt_text: the question as posed to the LLM
- earliest_year: before this year, answer is definitionally 0 (None = always applicable)
- filter_fn: if not None, a function (person) -> bool. People failing this get probability 0.
- known_answer_fn: if not None, a function (person) -> float|None. Returns known probability
    for people where we don't need an LLM call, or None if LLM should be queried.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass
class Question:
    id: str
    short: str
    prompt_text: str
    earliest_year: Optional[int] = None     # Before this → known 0
    filter_fn: Optional[Callable] = None    # Must pass to be queried (else → 0)
    known_answer_fn: Optional[Callable] = None  # Returns known prob or None for LLM


def _alive_or_age_gte(person, min_age):
    """True if person survived to at least min_age."""
    return person.age_at_death == "alive" or person.age_at_death >= min_age


def _death_year(person):
    if person.age_at_death == "alive":
        return 2026
    return person.birth_year + person.age_at_death


def _get_continent(person):
    """Get continent for a person (works for both Paleolithic and Holocene)."""
    if person.era == 'Holocene':
        import sys, os
        parent = os.path.join(os.path.dirname(__file__), '..')
        if parent not in sys.path:
            sys.path.insert(0, parent)
        from export import get_continent
        return get_continent(person.location.country, None)
    else:
        region_to_continent = {
            'Africa': 'Africa', 'Europe': 'Europe', 'Asia': 'Asia',
            'Sahul': 'Oceania', 'North_America': 'North America',
            'South_America': 'South America',
        }
        return region_to_continent.get(person.region, 'Unknown')


def _in_americas(person):
    """True if person is in North or South America."""
    return _get_continent(person) in ('North America', 'South America')


def _in_old_world(person):
    """True if person is in Eurasia, Africa, or Oceania (not Americas)."""
    return not _in_americas(person)


def _in_americas_or_oceania(person):
    """True if person is in the Americas or Oceania."""
    return _get_continent(person) in ('North America', 'South America', 'Oceania')


# ── Sampling-based questions ──

SAMPLING_QUESTIONS = [
    # ── Travel & Geography ──
    Question(
        id="flown_aeroplane",
        short="Flown in an aeroplane",
        prompt_text="Has this person ever flown in an aeroplane (as a passenger or crew)?",
        earliest_year=1914,
    ),
    Question(
        id="ridden_horse",
        short="Ridden a horse",
        prompt_text="Has this person ever ridden a horse (including donkeys and mules)?",
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
    ),
    Question(
        id="seen_ocean",
        short="Seen the ocean",
        prompt_text="Has this person ever seen the ocean or sea with their own eyes?",
    ),
    Question(
        id="seen_snow",
        short="Seen snow",
        prompt_text="Has this person ever seen snow (falling or on the ground)?",
    ),
    Question(
        id="travelled_50km",
        short="Traveled >50 km from birthplace",
        prompt_text="Did this person ever travel more than 50 km (30 miles) from their birthplace during their lifetime?",
    ),

    # ── Food & Drink ──
    Question(
        id="eaten_sugar",
        short="Eaten sugar",
        prompt_text="Has this person ever eaten refined sugar or foods sweetened with refined sugar (not just honey or fruit)?",
        earliest_year=-500,  # Sugar refining began in India ~500 BC
    ),
    Question(
        id="eaten_chocolate",
        short="Eaten chocolate",
        prompt_text="Has this person ever eaten chocolate in any form?",
        # Mesoamerica only pre-1500; Old World gets it after Columbian exchange
        filter_fn=lambda p: not (_in_old_world(p) and _death_year(p) < 1500),
        earliest_year=-1500,
    ),
    Question(
        id="eaten_rice",
        short="Eaten rice",
        prompt_text="Has this person ever eaten rice?",
        earliest_year=-8000,
    ),
    Question(
        id="eaten_bread",
        short="Eaten bread",
        prompt_text="Has this person ever eaten bread (leavened or unleavened, made from ground grain)?",
        earliest_year=-10000,
    ),
    Question(
        id="eaten_banana",
        short="Eaten a banana",
        prompt_text="Has this person ever eaten a banana?",
        # Cultivated in SE Asia from ~5000 BC; Americas/Europe only after Columbian exchange
        filter_fn=lambda p: not (_in_americas(p) and _death_year(p) < 1500),
        earliest_year=-5000,
    ),
    Question(
        id="eaten_pineapple",
        short="Eaten a pineapple",
        prompt_text="Has this person ever eaten pineapple?",
        # South America only pre-1500; Old World after Columbian exchange
        filter_fn=lambda p: not (_in_old_world(p) and _death_year(p) < 1500),
        earliest_year=-1000,
    ),
    Question(
        id="eaten_ice_cream",
        short="Eaten ice cream",
        prompt_text="Has this person ever eaten ice cream or a similar frozen dairy/flavoured ice dessert?",
        earliest_year=1600,
    ),
    Question(
        id="eaten_big_mac",
        short="Eaten a Big Mac",
        prompt_text="Has this person ever eaten a McDonald's Big Mac?",
        earliest_year=1968,
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
    ),
    Question(
        id="drunk_tea",
        short="Drunk tea",
        prompt_text="Has this person ever drunk tea (brewed from the leaves of the tea plant Camellia sinensis, not herbal infusions)?",
        # Tea in China from ~500 BC; rest of world much later
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
        earliest_year=-500,
    ),
    Question(
        id="drunk_coffee",
        short="Drunk coffee",
        prompt_text="Has this person ever drunk coffee (a beverage brewed from roasted coffee beans)?",
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
        earliest_year=1400,  # Coffee drinking in Yemen/Ethiopia ~15th century
    ),
    Question(
        id="drunk_alcohol",
        short="Drunk alcohol",
        prompt_text="Has this person ever drunk an alcoholic beverage (beer, wine, spirits, fermented drinks)?",
        earliest_year=-7000,
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
    ),
    Question(
        id="drunk_coca_cola",
        short="Drunk Coca-Cola",
        prompt_text="Has this person ever drunk Coca-Cola (the specific brand)?",
        earliest_year=1886,
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
    ),
    Question(
        id="eaten_restaurant",
        short="Eaten at a restaurant",
        prompt_text="Has this person ever eaten a meal at a restaurant, tavern, inn, or food stall where prepared food was sold to the public?",
        earliest_year=-500,
    ),

    # ── Objects & Technology ──
    Question(
        id="seen_reflection_mirror",
        short="Seen their reflection in a mirror",
        prompt_text="Has this person ever seen their own reflection in a manufactured mirror (polished metal or glass, not just water)?",
        earliest_year=-4000,
    ),
    Question(
        id="used_flush_toilet",
        short="Used a flush toilet",
        prompt_text="Has this person ever used a flush toilet (a toilet connected to a water-based sewage system)?",
        earliest_year=1596,
        filter_fn=lambda p: _alive_or_age_gte(p, 2),
    ),
    Question(
        id="handled_money",
        short="Handled money",
        prompt_text="Has this person ever handled money (coins, paper currency, or standardised tokens of exchange)?",
        earliest_year=-650,
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
    ),
    Question(
        id="used_fork",
        short="Used a fork",
        prompt_text="Has this person ever eaten with a fork (a multi-pronged utensil for conveying food to the mouth)?",
        earliest_year=300,
        filter_fn=lambda p: _alive_or_age_gte(p, 2),
    ),
    Question(
        id="held_sword",
        short="Held a sword",
        prompt_text="Has this person ever held a sword (a bladed weapon with a handle, longer than a knife)?",
        earliest_year=-3000,
        filter_fn=lambda p: _alive_or_age_gte(p, 5),
    ),
    Question(
        id="shot_gun",
        short="Shot a gun",
        prompt_text="Has this person ever fired a gun (any firearm — musket, rifle, pistol, etc.)?",
        earliest_year=1350,
        filter_fn=lambda p: _alive_or_age_gte(p, 8),
    ),
    Question(
        id="sat_in_chair",
        short="Sat in a chair",
        prompt_text="Has this person ever sat in a chair (a piece of furniture with a back, raised off the ground, designed for one person to sit on — not a bench, stool, or the ground)?",
        earliest_year=-3000,
    ),
    Question(
        id="worn_shoes",
        short="Worn shoes",
        prompt_text="Has this person ever worn shoes or sandals (any footwear)?",
    ),
    Question(
        id="taken_painkiller",
        short="Taken a painkiller",
        prompt_text="Has this person ever taken a manufactured painkiller or analgesic (aspirin, ibuprofen, paracetamol, opioid medications — not just chewing willow bark)?",
        earliest_year=1897,
    ),

    # ── Hygiene & Health ──
    Question(
        id="brushed_teeth",
        short="Brushed their teeth",
        prompt_text="Has this person ever brushed their teeth with a toothbrush or chew stick (a dedicated teeth-cleaning implement, not just rinsing)?",
        earliest_year=-3000,
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
    ),
    Question(
        id="bathed_weekly",
        short="Bathed weekly for a year",
        prompt_text="Was there ever a full year during which this person bathed or washed their whole body at least once a week?",
    ),
    Question(
        id="used_the_pill",
        short="Used the contraceptive pill",
        prompt_text="Has this person ever taken the oral contraceptive pill?",
        earliest_year=1960,
        filter_fn=lambda p: p.sex == 'F' and _alive_or_age_gte(p, 13),
    ),
    Question(
        id="had_vaccine",
        short="Had a vaccine",
        prompt_text="Has this person ever received a vaccine (any inoculation or vaccination)?",
        earliest_year=1721,
    ),

    # ── Social & Cultural ──
    Question(
        id="died_virgin",
        short="Died a virgin",
        prompt_text="Did this person die (or are they currently) a virgin — never having had sexual intercourse?",
    ),
    Question(
        id="given_birth",
        short="Given birth",
        prompt_text="Has this person ever given birth to a child?",
        filter_fn=lambda p: p.sex == 'F' and _alive_or_age_gte(p, 12),
    ),
    Question(
        id="heard_happy_birthday",
        short='Heard "Happy Birthday" sung',
        prompt_text='Has this person ever heard the song "Happy Birthday to You" sung (the specific English-language song, or a recognisable local adaptation)?',
        earliest_year=1910,
    ),
    Question(
        id="said_ok",
        short='Said "OK"',
        prompt_text='Has this person ever said the word "OK" or "okay" (the English word, even if borrowed into another language)?',
        earliest_year=1839,
        filter_fn=lambda p: _alive_or_age_gte(p, 3),
    ),
    Question(
        id="taken_selfie",
        short="Taken a selfie",
        prompt_text="Has this person ever taken a selfie (a self-portrait photograph using a handheld camera or phone)?",
        earliest_year=2003,
        filter_fn=lambda p: _alive_or_age_gte(p, 8),
    ),
    Question(
        id="read_newspaper",
        short="Read a newspaper",
        prompt_text="Has this person ever read a newspaper (a regularly published printed news publication)?",
        earliest_year=1605,
        filter_fn=lambda p: _alive_or_age_gte(p, 8),
    ),
    Question(
        id="slept_alone_room",
        short="Slept alone in a room",
        prompt_text="Has this person ever slept alone in a room (a private enclosed sleeping space with no other person present)?",
    ),
    Question(
        id="been_photographed",
        short="Been photographed",
        prompt_text="Has this person ever been photographed (appeared in a photograph, whether they knew about it or not)?",
        earliest_year=1826,
    ),
    Question(
        id="shopped_supermarket",
        short="Shopped at a supermarket",
        prompt_text="Has this person ever shopped at a supermarket (a large self-service store selling food and household goods)?",
        earliest_year=1930,
        filter_fn=lambda p: _alive_or_age_gte(p, 5),
    ),
    Question(
        id="was_literate",
        short="Was literate",
        prompt_text="Could this person read and write at a basic level in any language at any point in their life?",
        earliest_year=-3200,
        filter_fn=lambda p: _alive_or_age_gte(p, 5),
    ),
    Question(
        id="name_written_down",
        short="Had their name written down",
        prompt_text="Was this person's name ever written down by anyone during their lifetime (in a census, church record, contract, letter, or any other document)?",
        earliest_year=-3200,
    ),
    Question(
        id="sat_exam",
        short="Sat an exam",
        prompt_text="Has this person ever sat a formal examination or test (a structured written or oral assessment of knowledge, e.g. school exams, civil service exams, guild examinations)?",
        earliest_year=-600,
        filter_fn=lambda p: _alive_or_age_gte(p, 8),
    ),
    Question(
        id="carried_water_well",
        short="Carried water from a well",
        prompt_text="Has this person ever carried water from a well, spring, or river back to their dwelling?",
        earliest_year=-8000,
        filter_fn=lambda p: _alive_or_age_gte(p, 5),
    ),
    Question(
        id="knew_earth_round",
        short="Knew the Earth was round",
        prompt_text="Did this person know or believe that the Earth is (roughly) spherical?",
        earliest_year=-500,
        filter_fn=lambda p: _alive_or_age_gte(p, 8),
    ),
    Question(
        id="fought_war",
        short="Fought in a war",
        prompt_text="Did this person ever fight in a war or armed conflict as a combatant (soldier, warrior, militia, guerrilla)?",
        filter_fn=lambda p: _alive_or_age_gte(p, 12),
    ),
    Question(
        id="sold_as_slave",
        short="Was sold as a slave",
        prompt_text="Was this person ever sold as a slave or into bondage/serfdom where they were treated as property?",
        earliest_year=-3000,
    ),
    Question(
        id="caught_plague",
        short="Caught the plague",
        prompt_text="Did this person ever contract plague (bubonic, pneumonic, or septicaemic plague caused by Yersinia pestis)?",
        earliest_year=-430,
    ),
    Question(
        id="voted_national_election",
        short="Voted in any national election",
        prompt_text="Did this person ever vote in a national election or plebiscite (any form of organised popular vote for national leadership or legislation)?",
        earliest_year=-500,
        filter_fn=lambda p: _alive_or_age_gte(p, 15),
    ),
]
