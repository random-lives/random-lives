"""
Unified LLM generation pipeline for biographical narratives.

This module handles the full pipeline for generating person biographies:
1. Geography refinement (Paleolithic only)
2. Demographic generation
3. Life events sampling
4. Narrative generation
5. Quality control

Usage:
    from generation import generate_person
    person = generate_person(model='gpt-5.2')
"""

import json
import random

from person import sample_person
from llm_utils import GenerationContext, extract_json, sample_distribution, call_with_retry
from lifespan import age_at_death


# =============================================================================
# PROMPTS - Compositional structure with base + era-specific additions
# =============================================================================

# -----------------------------------------------------------------------------
# Demographic Prompts
# -----------------------------------------------------------------------------

DEMOGRAPHIC_CONTEXT_BASE = '''This is part of a "random lives" project - simulating randomly selecting a person from human history.

For this historical person, you will be asked demographic questions. For each question, provide a probability distribution
representing how common each option was among people matching this person's known characteristics
(birth time, location, age, sex, personality, lifestyle, etc.). Each question should be answered conditional on all previously
generated information.

YOUR GOAL: Estimate the TRUE HISTORICAL FREQUENCIES, not what seems interesting or diverse.
- If 90% of people in this demographic had characteristic X, assign it 90% probability
- Focus on ordinary people, not exceptional individuals or elites
- Boring and repetitive answers are often historically correct
- Some personality extremes can represent substantial limitations and strongly influence a person's life trajectory

TECHNICAL REQUIREMENTS:
- Probabilities must sum to exactly 1.0
- Categories should be mutually exclusive
- IMPORTANT: You must condition on ALL previously provided information.

FORMAT:
Brief reasoning (1-3 paragraphs), then the probability distribution as JSON:
{"option1": probability1, "option2": probability2, ...}
'''

DEMOGRAPHIC_CONTEXT_ERA = {
    'Holocene': '''
CATEGORIES AND PRECISION:
- Use categories that would have been meaningful to people at that time and place
- For ancient/prehistoric periods: Use broader geographic, linguistic, or cultural groupings
- For recent periods: You can be more specific (e.g., specific occupations, denominations, ethnic groups)
- Avoid inventing overly specific categories when evidence is limited
''',
    'Paleolithic': '''
Use ethnographic analogy from recent hunter-gatherer societies (e.g., !Kung, Hadza, Ache, Inuit, Aboriginal Australians).
Consider the specific environment and subsistence pattern implied by the location.
'''
}

# Demographic questions - single list with metadata
# Format: (name, query, era, min_age, requires_dead)
# era: 'Both', 'Holocene', or 'Paleolithic' (matches person.era)
# min_age: minimum age to ask this question (0 = always)
# requires_dead: only ask if person is dead
DEMOGRAPHIC_QUERIES = [
    # Cultural context (Holocene)
    ("ethnicity",
     "What ethnic/cultural group did this person likely belong to? Consider the time period and avoid modern ethnic categories that didn't exist yet.",
     'Holocene', 0, False),

    ("language",
     "What language(s) did they likely speak? For ancient periods, use language family names rather than specific modern languages.",
     'Holocene', 0, False),

    ("religion",
     "What were their likely religious/spiritual practices? Focus on what they actually did (household offerings, prayers, rituals) rather than abstract beliefs.",
     'Holocene', 0, False),

    # Household at birth
    ("number_of_siblings",
     "How many siblings did this person have (including those who died in childhood)? Label options as 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10+.",
     'Both', 0, False),

    ("household_structure_at_birth",
     "What was the household structure when this person was born? Consider mortality rates, marriage customs, household organization patterns.",
     'Holocene', 0, False),

    ("household_social_status",
     "What was the social status of the household this person was born into?",
     'Holocene', 0, False),

    ("father_occupation",
     "What was their father's likely occupation while the person was a young child? If absent, deceased, or unknown, include that as an option.",
     'Holocene', 0, False),

    ("mother_occupation",
     "What was their mother's likely occupation while the person was a young child? If she died in or shortly after childbirth, include that as an option.",
     'Holocene', 0, False),

    ("parents_status",
     "Were both parents alive and together during this person's childhood? Options: both parents together, father dead, mother dead, both dead (raised by kin), parents separated.",
     'Paleolithic', 0, False),

    # Education and capabilities
    ("mental_disorder",
     "Given this person's personality profile, would they likely meet criteria for what we'd recognize today as a mental disorder or pathology? Give a realistic assessment, with high neuroticism and/or very low agreeableness, honesty/humility, conscientiousness, or intelligence likely to manifest as some modern recognized mental disorder.",
     'Both', 5, False),
    
    ("literacy",
     "Could this person likely read and/or write? Consider their social class, personality, time period, and regional literacy rates.",
     'Holocene', 5, False),

    ("migration",
     "Did this person stay in their birth location or migrate? Consider their occupation, personality, social class, and migration patterns of their era.",
     'Holocene', 5, False),

    # Adult roles
    ("marital_status",
     "What was their likely marital status? Consider their age at death, sex, marriage customs, social status, and personality.",
     'Holocene', 12, False),

    ("occupation",
     "What was their likely primary occupation? Consider their age, sex, personality, social class, and economic activities of their region.",
     'Holocene', 12, False),

    ("adult_standing",
     "What was this person's social standing as an adult? Did it differ from their household's standing at birth?",
     'Holocene', 12, False),

    ("partnership_history",
     "What was this person's partnership history? Options: never partnered, one long-term partner, sequential partners, multiple concurrent partners.",
     'Paleolithic', 12, False),

    ("social_standing",
     "What was this person's standing in the band? Options: low status/marginal, ordinary member, respected/influential, senior/elder.",
     'Paleolithic', 10, False),

    ("special_skills",
     "Did this person have any notable skills or roles? Options: generalist, skilled hunter/tracker, skilled gatherer/plant knowledge, toolmaker, healer/herbalist, storyteller, mediator.",
     'Paleolithic', 12, False),

    # Children and family trajectory
    ("number_of_children",
     "How many children did they likely have (live births)? Consider their age at death and sex. Label options as 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10+.",
     'Both', 15, False),

    # Death
    ("cause_of_death",
     "What was their likely cause of death? Consider their age at death, sex, lifestyle, and common causes of mortality.",
     'Both', 0, True),

    ("household_structure_at_death",
     "What was the structure of the household this person belonged to when they died?",
     'Holocene', 12, True),
]

# -----------------------------------------------------------------------------
# Geography Prompts (Paleolithic only)
# -----------------------------------------------------------------------------

GEOGRAPHY_PROMPT = '''For a person born in {region} around {year}, provide a probability distribution over sub-regions where they might have lived.

The sub-regions should be:
- MUTUALLY EXCLUSIVE and EXHAUSTIVE for inhabited areas
- Weighted by estimated POPULATION DISTRIBUTION, not archaeological fame

Consider:
- Population density patterns (people clustered near water, resources, climate refugia)
- Ice sheets during glacial periods (LGM ~26,500-19,000 years ago)
- Lower sea levels exposing land bridges and coastlines

TECHNICAL REQUIREMENTS:
- Probabilities must sum to exactly 1.0
- Provide 5-10 sub-regions

FORMAT:
Brief reasoning, then as JSON:
{{"subregions": {{"subregion name 1": probability1, ...}}}}'''

SUBSUBREGION_PROMPT = '''For a person living in {subregion} around {year}, provide a probability distribution over more specific locations.

Weighted by estimated POPULATION DISTRIBUTION, not archaeological fame.

TECHNICAL REQUIREMENTS:
- Probabilities must sum to exactly 1.0
- Provide 5-10 specific locations

FORMAT:
Brief reasoning, then as JSON:
{{"locations": {{"location name 1": probability1, ...}}}}'''

ENVIRONMENT_PROMPT = '''Describe the environment and climate for someone living in {subsubregion} around {year}.

Return as JSON:
{{
    "environment": "brief environment description",
    "cultural_tradition": "archaeological culture name or 'undifferentiated'",
    "climate_then": "2-3 sentences on climate/landscape at that time",
    "climate_now": "1-2 sentences on what that area is like today"
}}'''

# -----------------------------------------------------------------------------
# Life Events Prompts
# -----------------------------------------------------------------------------

LIFE_EVENTS_PROMPT_BASE = '''Based on this person's demographics and lifetime, list events that might have affected their life.

Include TWO types of events:

1. HISTORICAL/ENVIRONMENTAL CONTEXT (aim for 4-8):
   - Political: wars, regime changes, conquests, taxation/corvée demands
   - Economic: trade route shifts, market access changes, currency debasements, labor demands
   - Environmental: droughts, floods, crop failures, livestock epidemics, locust plagues
   - Epidemics: known disease outbreaks affecting the region
   - Religious/social: new religious movements, pilgrimage routes, community obligations
   - For well-documented periods: reference actual historical events
   - For poorly-documented periods: describe plausible specific patterns

2. PERSONAL INCIDENTS (aim for 2-4):
   - Must be DISCRETE EVENTS with a beginning and end, not ongoing patterns or gradual processes
   - Conflicts, disputes, legal troubles, achievements, accidents, or turning points
   - Specific to this person's time, place, occupation, and personality
   - Avoid generic filler that could apply to anyone anywhere

DO NOT INCLUDE (already captured in demographics):
- Deaths of family members, siblings, or children
- Illness of family members
- Marriage/partnership changes
- Childbirth or pregnancy
- Migration (if in demographics)

PROBABILITIES should reflect your best estimate of how likely each event was to affect this specific person, given their demographics.

FORMAT:
Brief reasoning, then events as JSON:
{"events": [
    {"event": "description", "probability": 0.XX, "timing": "age/stage"},
    ...
]}'''

# -----------------------------------------------------------------------------
# Naming Prompts
# -----------------------------------------------------------------------------

NAMING_PROMPT = '''Generate 20 possible names for this person.

Person details:
{person_data}

NAMING CATEGORIES:
First, determine which category applies:

1. **ATTESTED**: Names survive in written records. Use historically authentic names appropriate to era, region, class, and sex. Prioritize common everyday names over famous or prestigious ones. Maximize diversity across the 20 options.

2. **INFERABLE**: Language family known but no written records. Generate phonologically plausible names for that language family. Use linguistic reconstruction notation where appropriate. Vary phonological patterns and roots.

3. **UNRECOVERABLE**: No linguistic connection to known languages. Generate simple, short names (1-3 syllables) that sound human. CRITICAL: Vary name length substantially - include roughly equal numbers of 1-syllable, 2-syllable, and 3-syllable names across the 20 options. Vary consonants, vowels, and syllable structures.

4. **UNNAMED**: Infant died before customary naming age. Return empty names list.

NAMING CONSIDERATIONS:
- Full name format should match cultural norms (given name only, or with family/clan/patronymic elements)
- Consider: social class, sex, religious context, regional variation

FORMAT:
Brief reasoning about which category applies and why, then as JSON:
{{
    "category": "attested" | "inferable" | "unrecoverable" | "unnamed",
    "names": ["Full Name 1", "Full Name 2", ..., "Full Name 20"]
}}

For "unnamed" category, return empty list: {{"category": "unnamed", "names": []}}'''


# -----------------------------------------------------------------------------
# Narrative Prompts
# -----------------------------------------------------------------------------

NARRATIVE_STYLE_BASE ='''
STYLE & VOICE:
Aim for quiet realism. The main failure mode to avoid: at no level, sentence, paragraph, or structure, should you lay it on thick.
- Write in plain, contemporary English
- Do not use subheadings, the entire narrative should read as a continuous text
- Keep figurative language sparse. Prefer direct, concrete description.
- Do not employ archaic inversions or poetic grand flourishes; avoid proverbs unless spoken by a character
- Avoid a moralizing ending or cliche last words, aim for realism
- Be specific about who did what; avoid vague collectives
- Avoid these exact phrases: "life went on", "work continued", "people remembered", "X was known for being"
- Vary sentence rhythm: Mix short and long sentences. Use fragments occasionally.

Trust the reader, be subtler than you think you can. Avoid cliches aggressively.

NARRATOR AUTHORITY:
You are omniscient. State facts with confidence. Avoid "likely," "probably," 
"perhaps," "may have," or "X or Y" constructions. Pick specific details.

Exceptions:
 - It is fine to report that the character themselves doesn't know something.
 - If something is historical unknowable and not clearly fictious but could instead be construed as a factual claim, then it is fine to note this

HISTORICAL CONTEXT:
 - Include explicit historical framing throughout where relevant to the story, so that the reader can follow
 - Assume the reader is intelligent, well-educated and able to google things if interested, but not an expert on the specific period

PERSONALITY TRAITS:
Personality must be portrayed realistically through actions, particularly for extremes (below 15th or above 85th percentile). Those with low 
intelligence or conscientiousness should visibly struggle with tasks others manage; those with low agreeableness or honesty-humility should create friction and face social consequences. Do not bowdlerize—negative traits should cause real problems, not be reframed as hidden strengths.

EVENT INTEGRATION:
Every historical event or contextual detail should do at least one of:
1. Reveals character (shows a personality trait or relationship dynamic)
2. Builds causally toward the death (creates conditions that lead to or contextualize it)
3. Shows social/historical structure in a way that matters to this life
If an event does none of these things, remove it entirely. Don't include events as context unless they do clear narrative work. When life events include multiple options, choose one specific version and describe it concretely.
'''

NARRATIVE_PROMPT_ERA = {
    'Holocene': """Write a narrative biography for this historical person that brings them to life as a real individual.
- Use the provided name for this person
- Include the demographic details in the story naturally
- Avoid anachronisms

HISTORICAL CONTEXT:
Consider what was happening in their region during their lifetime:
- Political changes or conflicts
- Trade patterns or economic shifts
- Religious or cultural movements
- Technological changes affecting their work
""",

    'Paleolithic': """Write a narrative biography for this Paleolithic hunter-gatherer.

SETTING THE SCENE:
- Open with the environment and climate (use the "Climate then" vs "Climate now" contrast to orient readers)

WRITING THE PERSON:
- Use the provided name; if the naming category is "unrecoverable", you may briefly acknowledge the name is a placeholder (e.g., "We'll call her X"), but don't belabor this point
- Show personality through actions, choices, habits, and relationships - NOT by stating trait levels
- Avoid mechanical phrasing like "With moderate openness..." or "His low agreeableness suggests..."

WHAT WE CAN'T KNOW:
- Specific beliefs, rituals, or mythology
- Language
- Specific customs or taboos
"""
}

AGE_PROMPTS = {
    "infant": """
LENGTH & FOCUS (under age 3):
- Keep brief: 150-300 words
- The infant cannot express personality - focus on parents, household, circumstances
- Can be told entirely from the parents' perspective
""",
    "child": """
LENGTH & FOCUS (age 3-10):
- Keep relatively brief: 200-400 words
- Personality can show in limited, age-appropriate ways (a habit, a preference, how they played)
- Focus on a few vivid moments rather than an arc
""",
    "adolescent": """
LENGTH & FOCUS (age 11-18):
- Moderate length: 400-700 words
- Show emerging adult roles and relationships
- Make sure to express the person's personality through behavior and choices
- Traits below 15th percentile or above 85th percentile should be particularly visible

""",
    "adult": """
LENGTH & FOCUS (age 19+):
- Full length: 600-1000 words
- Include community relationships, social networks, and changes in their family life
- Structure the piece as a realistic mosaic of everyday episodes
- Make sure to express the person's personality through behavior and choices
- Traits below 15th percentile or above 85th percentile should be particularly visible
"""
}

ALIVE_PROMPT = """
ENDING (person still living):
- End in an ordinary moment, not on a cliffhanger or dramatic note
"""

DEAD_PROMPT = """
ENDING (person has died):
- Include the death, but do not dwell on aftermath
- End concretely, not sentimentally
"""

# -----------------------------------------------------------------------------
# Historical Notes Prompts
# -----------------------------------------------------------------------------

HISTORICAL_NOTES_PROMPT = """Generate 4-6 brief historical notes that provide context for understanding this person's life.

Person details:
{person_data}

Narrative:
{narrative}

WHAT TO INCLUDE:
- Demographic facts not obvious from the narrative (language, ethnicity, religion, literacy)
- Concrete historical context (archaeological sites, dates, statistics, economic figures)
- Surprising facts an educated reader might not know
- Comparative context: was this person typical? How did they compare to others?

For pre-modern periods, UP TO ONE note may acknowledge limits of knowledge.

STYLE:
- 1-2 sentences per note
- State facts directly; do not justify why the fact is relevant
- Use plain language, not academic jargon
- Include specific numbers, dates, and place names where possible

AVOID:
- Ending notes with "consistent with the narrative" or "matching the story" or similar
- Academic notation (write "26,000 BC" not "~26 ka")
- Technical jargon ("rainfed upland rice" → "rain-fed rice farming")
- Hedging phrases ("cannot be proven," "plausible but not verifiable")
- Repeating information already clear in the narrative

FORMAT:
Return as JSON:
{{
    "notes": ["First note.", "Second note.", ...]
}}"""

# -----------------------------------------------------------------------------
# Quality Control Prompts
# -----------------------------------------------------------------------------

QC_PROMPT_BASE = """Review this narrative for issues and provide a corrected version.

Person details:
{person_data}

Original narrative:
{narrative}

STYLE & VOICE:
- Aim for quiet realism - don't lay it on thick
- Plain, contemporary English
- No subheadings
- Sparse figurative language. Prefer direct, concrete description.
- No moralizing endings or clichés
- Varied sentences, avoid vague language

NARRATOR HEDGING:
Remove uncertain language: "likely," "probably," "perhaps," "X or Y," "some kind of."
Replace with specific facts. The narrator knows what happened.

PERSONALITY TRAIT CHECK:
Verify that extreme personality traits are visible and unvarnished. Negative traits should not be reframed as hidden strengths. Dysfunctional, ineffectual, or difficult people must not be bowdlerized into sympathetic eccentrics.

EVENT INTEGRATION CHECK:
Review all life events and historical details mentioned in the narrative.

For each event or detail, verify it does at least ONE of these:
1. Reveals character (shows a personality trait or relationship dynamic)
2. Builds causally toward the death (creates conditions that lead to or contextualize it)
3. Shows social/historical structure in a way that matters to this life

If an event does NONE of these things, remove it entirely. If an event is only mentioned but never shown or consequential, remove it.

REWRITING:
Fix all identified issues while maintaining consistency with person_data.

Return as JSON:
{{
    "issues_found": ["list of issues"],
    "revised_narrative": "the corrected narrative"
}}"""

QC_CHECKS_ERA = {
    'Holocene': """
Check for:
1. ANACHRONISMS: Things that couldn't exist in this time/place
2. HISTORICAL IMPOSSIBILITIES: Events, technologies, or social situations that contradict history
3. CULTURAL CONTRADICTIONS: Behaviors that wouldn't occur in this culture/period
""",
    'Paleolithic': """
Check for:
1. ANACHRONISMS: Agriculture, metal, pottery before it existed, domesticated animals other than dogs
2. OVERSPECIFICITY: Claims about beliefs, rituals, or language that we can't know
3. MECHANICAL DESCRIPTIONS: "with high openness..." style personality descriptions
"""
}

HISTORICAL_NOTES_QC_PROMPT = """Review these historical notes for quality and relevance.

Person details:
{person_data}

Narrative:
{narrative}

Current historical notes:
{notes}

REMOVE or REWRITE notes that:
- End with justifications like "consistent with the narrative," "matching the story," "as described"
- Use academic jargon or notation ("~26 ka," "settlement patterning," "rainfed upland")
- Are longer than 2 sentences
- Repeat what's already clear from the narrative

IMPROVE notes by:
- Cutting justification clauses entirely (the note should stand alone as an interesting fact)
- Converting academic language to plain English
- Adding specific numbers, dates, or comparisons where missing

CHECK that notes collectively include:
- At least one note with comparative context (typical/atypical, better/worse off than peers)
- Concrete specifics (dates, figures, place names)
- At most one epistemic-limits note (for pre-modern periods)

Return as JSON:
{{
    "issues_found": ["brief description of problems"],
    "revised_notes": ["note 1", "note 2", ...]
}}"""

SELECTION_TEXT = "The random number generator selected for this person: "


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def _get_demographic_queries(person):
    """Get filtered demographic queries for this person based on era, age, and alive status."""
    return [
        (name, query)
        for name, query, query_era, min_age, requires_dead in DEMOGRAPHIC_QUERIES
        if (query_era == 'Both' or query_era == person.era)
        and person.years_lived() >= min_age
        and not (requires_dead and person.is_alive())
    ]


def reset_to_stage(person, stage):
    """
    Reset person to the start of a specific pipeline stage, removing all later-stage data.

    Stages (in order):
    - 'demographics': Before demographics are generaetd
    - 'events': Before life events are generated
    - 'name': Before name is generated
    - 'narrative': Before narrative is generated
    - 'notes' : Before notes are generated
    """
    person.historical_notes = []
    if stage in ['demographics', 'events', 'name', 'narrative']:
        person.narrative = None
    if stage in ['demographics', 'events', 'name']:
        person.name = None
        person.naming_category = None
    if stage in ['demographics', 'events']:
        person.events = []

    if stage == 'demographics':
        person.messages = []
        person.demographics = {}
    else:
        # Stage markers - text that appears at the start of each stage's prompt
        stage_markers = {
            'events': 'Based on this person\'s demographics and lifetime, list events',
            'name': 'Generate 20 possible names',
            'narrative': 'Write a narrative biography',
            'notes' : 'Generate 2-4 brief historical notes',
        }
    
        if stage in stage_markers:
            marker = stage_markers[stage]
            for i, msg in enumerate(person.messages):
                if marker in msg.get('content', ''):
                    person.messages = person.messages[:i]
    
# =============================================================================
# GENERATION FUNCTIONS
# =============================================================================

def generate_geography(person, ctx):
    """
    Refine geographic location for Paleolithic people.
    Only called for Paleolithic era - Holocene has pre-computed locations.

    Modifies person in place.
    """
    if person.era != 'Paleolithic':
        return

    region = person.region
    year = person.birth_year_str

    # Step 1: Get subregion
    ctx.log(f"Getting subregion distribution for {region}, {year}...")

    messages = [{"role": "user", "content": GEOGRAPHY_PROMPT.format(region=region, year=year)}]
    result, _ = call_with_retry(ctx, messages)

    if result and 'subregions' in result:
        subregion = sample_distribution(result['subregions'])
        person.demographics['Subregion'] = subregion
        ctx.log(f"  Sampled: {subregion}")
    else:
        person.demographics['Subregion'] = 'Unknown'
        subregion = region

    # Step 2: Get specific location
    ctx.log(f"Getting location distribution within {subregion}...")

    messages = [{"role": "user", "content": SUBSUBREGION_PROMPT.format(subregion=subregion, year=year)}]
    result, _ = call_with_retry(ctx, messages)

    if result and 'locations' in result:
        subsubregion = sample_distribution(result['locations'])
        person.demographics['Subsubregion'] = subsubregion
        ctx.log(f"  Sampled: {subsubregion}")
    else:
        person.demographics['Subsubregion'] = subregion
        subsubregion = subregion

    # Step 3: Get environment details
    ctx.log("Getting environment details...")

    messages = [{"role": "user", "content": ENVIRONMENT_PROMPT.format(subsubregion=subsubregion, year=year)}]
    env_result, _ = call_with_retry(ctx, messages)

    if env_result:
        person.demographics['Environment'] = env_result.get('environment', 'Unknown')
        person.demographics['Cultural tradition'] = env_result.get('cultural_tradition', 'Unknown')
        person.demographics['Climate then'] = env_result.get('climate_then', '')
        person.demographics['Climate now'] = env_result.get('climate_now', '')
        ctx.log(f"  Environment: {person.demographics['Environment']}")


def generate_demographics(person, ctx):
    """
    Generate demographic information through multi-turn LLM conversation.

    Modifies person in place.
    """
    # Build context prompt
    context = DEMOGRAPHIC_CONTEXT_BASE + DEMOGRAPHIC_CONTEXT_ERA[person.era]
    context += "\n\nHere are the basic facts for the person:\n" + person.to_prompt_string()

    person.messages = [
        {"role": "user", "content": context},
        {"role": "assistant", "content": "I'll help generate demographic information. Please ask your questions."}
    ]

    queries = _get_demographic_queries(person)
    ctx.log(f"Generating {len(queries)} demographic attributes...")

    for attr, query in queries:
        ctx.log(f"  {attr}...", end=" ", flush=True)

        person.messages.append({"role": "user", "content": query})
        probs, content = call_with_retry(ctx, person.messages)
        result = sample_distribution(probs)

        if result is None:
            ctx.log("-> [failed, skipping]")
            # Remove the failed query from messages to keep conversation coherent
            person.messages.pop()  # Remove user query
            continue

        person.messages.append({"role": "assistant", "content": content})
        person.demographics[attr] = result
        person.messages.append({"role": "user", "content": SELECTION_TEXT + result})

        ctx.log(f"-> {result}")

        # Generate family context
        if attr == 'number_of_siblings' and result:
            _add_family_context(person, result, 'siblings', ctx)
        elif attr == 'number_of_children' and result:
            _add_family_context(person, result, 'children', ctx)


def _add_family_context(person, result, kind, ctx):
    """Add sibling or children demographic context to conversation."""
    try:
        count = int(str(result).replace('+', ''))
        if count <= 0:
            return

        sexes = [random.choice(['M', 'F']) for _ in range(count)]
        country = person.location.country if person.location else None

        if kind == 'siblings':
            ages = [age_at_death(country, person.birth_year, s, person.lifestyle) for s in sexes]
            birth_order = random.randint(1, count + 1)

            person.demographics['sibling_sexes'] = sexes
            person.demographics['sibling_ages_at_death'] = ages
            person.demographics['birth_order_position'] = birth_order

            msg = f"This person was child #{birth_order} of {count + 1} children.\n"
            msg += f"Sibling sexes: {sexes}\nSibling ages at death: {ages}"
            ctx.log(f"    Siblings: #{birth_order} of {count + 1}")

        else:  # children
            child_birth_years = [person.birth_year + 17 + 3*i for i in range(count)]
            ages = [age_at_death(country, cby, sexes[i], person.lifestyle)
                    for i, cby in enumerate(child_birth_years)]

            person.demographics['children_sexes'] = sexes
            person.demographics['children_ages_at_death'] = ages

            msg = f"Children sexes: {sexes}\nChildren ages at death: {ages}"
            ctx.log(f"    Children: {count}")

        person.messages.append({"role": "user", "content": msg})

    except (ValueError, TypeError):
        pass


def generate_life_events(person, ctx):
    """
    Generate life events through probabilistic sampling.

    Modifies person in place.
    """
    if person.years_lived() < 5:
        ctx.log("Too young for life events")
        person.events = []
        return

    ctx.log("Generating potential life events...")

    # Build prompt
    event_prompt = LIFE_EVENTS_PROMPT_BASE
    event_request = event_prompt + "\n\nPerson details:\n" + person.to_prompt_string()
    person.messages.append({"role": "user", "content": event_request})

    events_data, content = call_with_retry(ctx, person.messages)

    if not events_data:
        ctx.log("  Failed to parse events")
        person.messages.pop()  # Remove the failed query
        person.events = []
        return

    person.messages.append({"role": "assistant", "content": content})
    potential_events = events_data.get('events', [])
    ctx.log(f"  Generated {len(potential_events)} potential events")

    # Sample events (Bernoulli trials)
    selected_events = [e for e in potential_events if random.random() < e.get('probability', 0)]
    ctx.log(f"  Sampled {len(selected_events)} events")

    # Store selected events (strip probability since it's no longer needed)
    person.events = [
        {"event": e.get("event", ""), "timing": e.get("timing", "")}
        for e in selected_events
    ]

    ctx.log(f"  Final events: {len(person.events)}")


def generate_name(person, ctx):
    """
    Generate a name for the person by having the LLM propose 10 options
    and randomly selecting one.

    Modifies person in place.
    """
    ctx.log("Generating name...")

    prompt = NAMING_PROMPT.format(person_data=person.to_prompt_string())
    person.messages.append({"role": "user", "content": prompt})

    result, content = call_with_retry(ctx, person.messages)

    if not result or 'category' not in result:
        ctx.log("  Failed to generate names")
        person.messages.pop()
        person.name = None
        person.naming_category = None
        return

    person.messages.append({"role": "assistant", "content": content})

    names = result.get('names', [])
    category = result.get('category', 'unknown')

    person.naming_category = category

    if not names or category == 'unnamed':
        person.name = None
        ctx.log(f"  Unnamed ({category})")
    else:
        ctx.log(f" Names: {names}")
        person.name = random.choice(names)
        ctx.log(f"  Selected: {person.name} ({category})")
        person.messages.append({
            "role": "user",
            "content": SELECTION_TEXT + person.name
        })


def generate_narrative(person, ctx, extra_prompt=None, replace_prompt=None):
    """
    Generate biographical narrative.

    Args:
        person: Person object with demographics and events populated
        ctx: GenerationContext
        extra_prompt: Optional string to append to the standard prompt (for experimentation)
        replace_prompt: Optional string to use instead of the standard prompt (for full control)

    Modifies person in place.
    """
    age_cat = person.age_category()

    if replace_prompt:
        # Full control mode - use provided prompt directly
        full_prompt = NARRATIVE_PROMPT_ERA[person.era] + replace_prompt + AGE_PROMPTS[age_cat]
    else:
        # Standard prompt construction
        full_prompt = NARRATIVE_PROMPT_ERA[person.era] + NARRATIVE_STYLE_BASE + AGE_PROMPTS[age_cat]
        full_prompt += ALIVE_PROMPT if person.is_alive() else DEAD_PROMPT

        # Add any experimental modifications
        if extra_prompt:
            full_prompt += "\n\n" + extra_prompt

    # Always add person details and events
    full_prompt += "\n\nPerson details:\n" + person.to_prompt_string()

    if person.events:
        events_str = "\n".join(f"- {e.get('event', e)} ({e.get('timing', 'unknown timing')})"
                               for e in person.events)
        full_prompt += "\n\nLife events to incorporate:\n" + events_str

    person.messages.append({"role": "user", "content": full_prompt})

    ctx.log(f"Generating narrative ({age_cat})...")

    person.narrative = ctx.call(person.messages)
    person.messages.append({"role": "assistant", "content": person.narrative})

    ctx.log(f"  Generated {len(person.narrative.split())} words")


def generate_historical_notes(person, ctx):
    """
    Generate historical context notes for the narrative.

    Modifies person in place by setting person.historical_notes.
    """
    ctx.log("Generating historical notes...")

    prompt = HISTORICAL_NOTES_PROMPT.format(
        person_data=person.to_prompt_string(),
        narrative=person.narrative
    )

    messages = [{"role": "user", "content": prompt}]
    result, _ = call_with_retry(ctx, messages)

    if not result or 'notes' not in result:
        ctx.log("  Failed to generate notes")
        person.historical_notes = []
        return

    person.historical_notes = result.get('notes', [])
    ctx.log(f"  Generated {len(person.historical_notes)} notes")


def quality_check(person, ctx):
    """
    Review and revise narrative and historical notes for issues.

    Modifies person in place.
    Returns issues_found dict with 'narrative' and 'notes' keys.
    """
    all_issues = {'narrative': [], 'notes': []}

    # QC narrative
    qc_prompt = QC_CHECKS_ERA[person.era] + QC_PROMPT_BASE.format(
        person_data=person.to_prompt_string(), narrative=person.narrative
    )

    ctx.log("Running quality check on narrative...")

    messages = [{"role": "user", "content": qc_prompt}]
    result, _ = call_with_retry(ctx, messages)

    if result:
        narrative_issues = result.get('issues_found', [])
        person.narrative = result.get('revised_narrative', person.narrative)
        all_issues['narrative'] = narrative_issues

        count = len(narrative_issues) if isinstance(narrative_issues, list) else sum(len(v) for v in narrative_issues.values() if isinstance(v, list))
        ctx.log(f"  Fixed {count} narrative issues")
    else:
        ctx.log("  Narrative QC failed, keeping original")

    # QC historical notes if they exist
    if person.historical_notes:
        ctx.log("Running quality check on historical notes...")

        notes_qc_prompt = HISTORICAL_NOTES_QC_PROMPT.format(
            person_data=person.to_prompt_string(),
            narrative=person.narrative,
            notes='\n'.join(f'{i+1}. {note}' for i, note in enumerate(person.historical_notes))
        )

        messages = [{"role": "user", "content": notes_qc_prompt}]
        notes_result, _ = call_with_retry(ctx, messages)

        if notes_result:
            notes_issues = notes_result.get('issues_found', [])
            revised_notes = notes_result.get('revised_notes', person.historical_notes)

            # Only update if we got valid revised notes
            if revised_notes and isinstance(revised_notes, list):
                person.historical_notes = revised_notes
                all_issues['notes'] = notes_issues

                notes_count = len(notes_issues) if isinstance(notes_issues, list) else 0
                ctx.log(f"  Fixed {notes_count} note issues, {len(person.historical_notes)} notes remain")
        else:
            ctx.log("  Notes QC failed, keeping original")

    return all_issues


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def run_pipeline(person, model="haiku", quiet=True, show_cost=False):
    """
    Run the full generation pipeline on an existing person.

    Args:
        person: Person object (from sample_person() or Person(year))
        model: LLM model to use
        quiet: If True, suppress progress output
        show_cost: If True, print cost summary at end

    Returns:
        The same Person object, now with demographics, events, and narrative populated.
    """
    ctx = GenerationContext(model=model, quiet=quiet, show_cost=show_cost)

    ctx.log("=" * 50)
    ctx.log(f"Era: {person.era}")
    ctx.log(f"Year: {person.birth_year_str}")
    ctx.log(f"Sex: {person.sex}")
    ctx.log(f"Age at death: {person.age_at_death}")
    if person.era == 'Paleolithic':
        ctx.log(f"Region: {person.region}")
    else:
        ctx.log(f"Location: {person.location.country if person.location else 'Unknown'}")

    if person.era == 'Paleolithic':
        ctx.log("\n" + "=" * 50)
        ctx.log("Step 1: Refining geography...")
        generate_geography(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 2: Generating demographics...")
    generate_demographics(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 3: Generating life events...")
    generate_life_events(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 4: Generating name...")
    generate_name(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 5: Generating narrative...")
    generate_narrative(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 6: Generating historical notes...")
    generate_historical_notes(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 7: Quality check...")
    quality_check(person, ctx)

    ctx.finish()

    return person


def generate_person(model="haiku", quiet=True, show_cost=False):
    """
    Sample a random person and run the full generation pipeline.

    Returns Person object with all attributes populated.
    """
    if not quiet:
        print("=" * 50)
        print("Sampling person...")

    person = sample_person()

    return run_pipeline(person, model=model, quiet=quiet, show_cost=show_cost)


def generate_batch(n=10, model="haiku", quiet=True, show_cost=False):
    """Generate a batch of people with narratives."""
    from tqdm import tqdm

    results = []
    for i in tqdm(range(n), disable=quiet):
        try:
            person = generate_person(model=model, quiet=quiet, show_cost=show_cost)
            results.append(person)
            if not quiet:
                print(f"  {i+1}: {person.era}, {person.birth_year_str}, "
                      f"Age {person.age_at_death} - {len(person.narrative.split())} words")
        except Exception as e:
            if not quiet:
                print(f"  {i+1}: Error - {e}")

    return results
