"""
Unified LLM generation pipeline for biographical narratives.

This module handles the full pipeline for generating person biographies:
1. Geography refinement (Paleolithic only)
2. Demographic generation
3. Structured incidents sampling
4. Historical context generation
5. Naming
6. Narrative planning (timeline/family structure)
7. Narrative generation

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
# Age Thresholds
# =============================================================================

AGE_CHILD = 5        # Personality expressible; child-length narrative
AGE_ADOLESCENT = 13  # Adult queries (marriage, occupation, etc.); adolescent narrative
AGE_ADULT = 19       # Full adult narrative length


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

    # Twin outcome (only asked if person is a twin)
    ("co_twin_fate",
     "This person was born as a {twin_type} twin. What happened to their co-twin? "
     "Consider infant/child mortality rates for this time and place. Options should include: "
     "died at birth/stillborn, died in infancy, died in childhood, survived to adulthood.",
     'Both', 0, False),

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
     "Given this person's personality profile and intelligence, would they likely meet criteria for what we'd recognize today as a mental disorder or pathology? Give a realistic assessment, with high neuroticism and/or very low agreeableness, honesty/humility, conscientiousness, or intelligence likely to manifest as some modern recognized mental disorder. Also consider addictions and mental disorders acquired through life experience.",
     'Both', 5, False),
    
    ("literacy",
     "Could this person likely read and/or write? Consider their social class, personality, time period, and regional literacy rates.",
     'Holocene', 5, False),

    ("migration",
     "Did this person stay in their birth location or migrate? Consider their occupation, personality, social class, and migration patterns of their era.",
     'Holocene', 5, False),

    # Adult roles (age 13+)
    ("marital_status",
     "What was their likely marital status? Consider their age at death, sex, sexual orientation, marriage customs, social status, and personality. "
     "Note: In most historical periods, people with same-sex attraction often married heterosexually due to social expectations.",
     'Holocene', 13, False),

    ("occupation",
     "What was their likely primary occupation? Consider their age, sex, personality, social class, and economic activities of their region.",
     'Holocene', 13, False),

    ("adult_standing",
     "What was this person's social standing as an adult? Did it differ from their household's standing at birth?",
     'Holocene', 13, False),

    ("partnership_history",
     "What was this person's partnership history? Consider their sexual orientation. "
     "Options: never partnered, one long-term partner, sequential partners, multiple concurrent partners, same-sex partnership.",
     'Paleolithic', 13, False),

    ("social_standing",
     "What was this person's standing in the band? Options: low status/marginal, ordinary member, respected/influential, senior/elder.",
     'Paleolithic', 13, False),

    ("special_skills",
     "Did this person have any notable skills or roles? Options: generalist, skilled hunter/tracker, skilled gatherer/plant knowledge, toolmaker, healer/herbalist, storyteller, mediator.",
     'Paleolithic', 13, False),

    # Children and family trajectory (age 13+)
    ("number_of_children",
     "How many children did they likely have (live births)? Consider their age at death and sex. Label options as 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10+.",
     'Both', 13, False),

    # Death
    ("cause_of_death",
     "What was their likely cause of death? Consider their age at death, sex, lifestyle, and common causes of mortality.",
     'Both', 0, True),

    ("household_structure_at_death",
     "What was the structure of the household this person belonged to when they died?",
     'Holocene', 13, True),
]

# -----------------------------------------------------------------------------
# Geography Prompts (Paleolithic only)
# -----------------------------------------------------------------------------

GEOGRAPHY_PROMPT = '''For a person born in {region} around {year}, provide a probability distribution over sub-regions where they might have lived.

The sub-regions should be:
- MUTUALLY EXCLUSIVE and EXHAUSTIVE for inhabited areas
- Weighted by estimated POPULATION DISTRIBUTION, not archaeological fame
- Use simple, short names for the different sub-regions. Do not use parentheticals.

Consider:
- Population density patterns
- Ice sheets during glacial periods
- Lower sea levels exposing land bridges and coastlines

TECHNICAL REQUIREMENTS:
- Probabilities must sum to exactly 1.0
- Provide 5-10 sub-regions

FORMAT:
Brief reasoning, then as JSON:
{{"subregions": {{"subregion name 1": probability1, ...}}}}'''

SUBSUBREGION_PROMPT = '''For a person living in {subregion} around {year}, provide a probability distribution over more specific locations.

The locations should be:
- MUTUALLY EXCLUSIVE and EXHAUSTIVE for inhabited areas
- Weighted by estimated POPULATION DISTRIBUTION, not archaeological fame
- Use simple, short names for the different sub-regions. Do not use parentheticals.

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

HISTORICAL_CONTEXT_PROMPT = '''Based on this person's demographics and lifetime, list HISTORICAL and ENVIRONMENTAL CONTEXT events that might have affected their life.

Focus on large-scale contextual forces, NOT personal incidents (which are handled separately):

HISTORICAL/ENVIRONMENTAL CONTEXT (aim for 4-8 events):
   - Political: wars, regime changes, conquests, taxation/corvée demands, new laws/regulations
   - Economic: trade route shifts, market access changes, currency debasements, labor demands, famines affecting food prices
   - Environmental: droughts, floods, crop failures, livestock epidemics, locust plagues, extreme weather
   - Epidemics: known disease outbreaks affecting the region
   - Religious/social: new religious movements, pilgrimage routes, community obligations, religious persecution
   - For well-documented periods: reference actual historical events (specific wars, known famines, documented epidemics)
   - For poorly-documented periods: describe plausible era-appropriate patterns

IMPORTANT EXCLUSIONS:
- Do NOT include personal incidents (violence, crime, accidents, achievements) - these are handled by the structured incidents system
- Do NOT include events already in demographics (family deaths, marriage, childbirth, migration)
- Focus on contextual forces that shaped the environment this person lived in

PROBABILITIES should reflect your best estimate of how likely each contextual event was to affect this specific person's region/lifetime.

FORMAT:
Brief reasoning, then events as JSON:
{"events": [
    {"event": "description", "probability": 0.XX, "timing": "age/period"},
    ...
]}'''

# -----------------------------------------------------------------------------
# Naming Prompts
# -----------------------------------------------------------------------------

NAMING_PROMPT = '''Generate 20 possible names for this person.

NAMING CATEGORIES:
First, determine which category applies:

1. **ATTESTED**: Names survive in written records. Use historically authentic names appropriate to the language, era, region, class, and sex. Prioritize common everyday names over famous or prestigious ones. Maximize diversity across the 20 options.

2. **INFERABLE**: Language family known but no written records. Generate phonologically plausible names for that language family. Vary phonological patterns and roots.

3. **UNRECOVERABLE**: No linguistic connection to known languages. Generate simple, short names (1-3 syllables) that sound human. CRITICAL: Vary name length substantially - include roughly equal numbers of 1-syllable, 2-syllable, and 3-syllable names across the 20 options. Vary consonants, vowels, and syllable structures.

4. **UNNAMED**: Infant died before customary naming age. Return empty names list.

ROMANIZATION RULES:
All names must be readable by English speakers:

- **Latin-alphabet languages** (Spanish, Polish, French, Vietnamese, etc.): Keep native diacritics (ł, ń, ü, ç, etc.)
- **Non-Latin scripts** (Chinese, Arabic, Greek, Hindi, Japanese, Korean, etc.): Use standard English romanization (pinyin for Chinese, etc.)
- **Inferable/reconstructed names**: Use plain romanization only. NO scholarly notation (no asterisks, no IPA symbols like ə, no macrons for vowel length, no hyphens between morphemes). The name should look like a normal name, not a linguistic reconstruction.

NAMING CONSIDERATIONS:
- Full name format should match cultural norms (given name only, or with family/clan/patronymic elements)
- Consider: language, social class, sex, religious context, regional variation

FORMAT:
Brief reasoning about which category applies and why, then as JSON:
{{
    "category": "attested" | "inferable" | "unrecoverable" | "unnamed",
    "names": ["Name 1", "Name 2", ..., "Name 20"]
}}

For "unnamed" category: {{"category": "unnamed", "names": []}}'''


# -----------------------------------------------------------------------------
# Narrative Planning Prompts (tiered by age)
# -----------------------------------------------------------------------------

# Infant (0-4): Only sibling timeline
NARRATIVE_PLAN_PROMPT_INFANT = '''Before writing the narrative, work out the sibling timeline.

TASK: Compute birth years for each sibling so the narrative gets older/younger relationships correct.

For each sibling, determine:
- Birth year (based on typical birth spacing of 2-3 years)
- Death year (computed from birth year + age at death)
- Whether they were alive when this person was born and when they died
- Their narrative role (e.g., "older sister present at birth", "younger brother born during person's life")

CONSTRAINTS:
- Siblings must be in correct birth order (birth_order_position shows where this person falls)
- All dates must be internally consistent
- Older siblings have earlier birth years than this person
- Younger siblings have later birth years than this person

Return as JSON:
{{
    "siblings": [{{"sex": "M/F", "birth_year": YYYY, "death_year": YYYY, "death_age": N, "narrative_role": "..."}}],
    "named_characters": [{{"name": "...", "relationship": "...", "prominence": "..."}}]
}}'''

# Child (5-12): Siblings + incidents + traits + characters
NARRATIVE_PLAN_PROMPT_CHILD = '''Before writing the narrative, create a timeline and plan.

TASK: Work out the key facts and timing that the narrative must respect.

1. SIBLING TIMELINE
For each sibling, determine:
- Birth year (based on typical birth spacing of 2-3 years)
- Death year (computed from birth year + age at death)
- Their narrative role

2. INCIDENTS PLACEMENT
For each structured incident: when it happened and how it connects to other events.

3. CHARACTERS
Named characters with relationship and when they're prominent.

4. TRAIT AND CONDITION MANIFESTATIONS
Plan how personality appears through concrete behavior.
- Very high and very low traits require specific scenes showing that trait in action
- Mental disorders likewise require specific scenes or behavioral patterns
- Average traits do not need to be included

For each trait or disorder, plan:
- What concrete behavior shows it?
- When does it appear?
- What consequences follow?

CONSTRAINTS:
- Siblings in correct birth order (birth_order_position shows where this person falls)
- All dates internally consistent

Return as JSON:
{{
    "siblings": [{{"sex": "M/F", "birth_year": YYYY, "death_year": YYYY, "death_age": N, "narrative_role": "..."}}],
    "incident_placements": [{{"incident": "...", "age": N, "connection": "..."}}],
    "trait_manifestations": [{{"trait": "...", "scene": "...", "timing": "...", "consequence": "..."}}],
    "named_characters": [{{"name": "...", "relationship": "...", "prominence": "..."}}]
}}'''

# Adolescent (13-18): Same as adult
# Adult (19+): Full planning including partners, children, life phases
NARRATIVE_PLAN_PROMPT_ADULT = '''Before writing the narrative, create a detailed timeline and plan.

TASK: Work out the key facts and timing that the narrative must respect.

CREATE A TIMELINE:

1. FAMILY TIMELINE
For siblings: birth year, death year (if before narrative end), key narrative moments.
For partners: when relationship began/ended, nature of relationship.
For children: birth year, death year (if before narrative end).

2. LIFE PHASES
Break life into phases (early childhood, later childhood/adolescence, adult life, old age) with 1-3 key events each. Key events should occur at specific times.

3. INCIDENTS PLACEMENT
For each structured incident: when it happened and how it connects to other events.

4. CHARACTERS
Named characters with relationship and when they're prominent.

5. TRAIT AND CONDITION MANIFESTATIONS
Plan how personality appears through concrete behavior.
- The very high and very low traits requires specific scenes or behavioral patterns showing that trait in action
- Mental disorders likewise require specific scenes or behavioral patterns showing that trait in action
- Traits that are average do not need to be included

For each trait or disorder, plan:
- What concrete behavior shows it?
- When does it appear (which life phase)?
- What consequences follow?

CONSTRAINTS:
- Siblings in correct birth order (birth_order_position shows where this person falls)
- All dates internally consistent

Return as JSON:
{{
    "siblings": [{{"sex": "M/F", "birth_year": YYYY, "death_year": YYYY, "death_age": N, "narrative_role": "..."}}],
    "partners": [{{"name": "...", "relationship_start_year": YYYY, "relationship_end_year": YYYY, "narrative_role": "..."}}],
    "children": [{{"sex": "M/F", "birth_year": YYYY, "death_year": YYYY, "death_age": N, "narrative_role": "..."}}],
    "life_phases": [{{"phase": "...", "age_range": "X-Y", "key_events": ["..."]}}],
    "incident_placements": [{{"incident": "...", "age": N, "connection": "..."}}],
    "trait_manifestations": [{{"trait": "...", "scene": "...", "timing": "...", "consequence": "..."}}],
    "named_characters": [{{"name": "...", "relationship": "...", "prominence": "..."}}]
}}'''

# Map age category to planning prompt
NARRATIVE_PLAN_PROMPTS = {
    "infant": NARRATIVE_PLAN_PROMPT_INFANT,
    "child": NARRATIVE_PLAN_PROMPT_CHILD,
    "adolescent": NARRATIVE_PLAN_PROMPT_ADULT,
    "adult": NARRATIVE_PLAN_PROMPT_ADULT,
}

# -----------------------------------------------------------------------------
# Narrative Prompts
# -----------------------------------------------------------------------------

NARRATIVE_BASE_PROMPT = '''Write a narrative biography for this historical person, following the demographic information and narrative plan provided.

TASK:
- Use the provided name
- Weave demographic details in naturally; you don't need to include everything. However, all details included must match the demogrpahics and narrative plan
- Give names to recurring people (family, spouse, close associates); minor one-off figures can remain unnamed
- Avoid anachronisms

VOICE:
- Plain contemporary English, no subheadings
- Omniscient narrator: state facts confidently, no hedging ("likely", "probably", "perhaps", "may have")
- When data presents options or ranges, make concrete choices
- Vary sentence rhythm. Mix lengths. Fragments sometimes.

TIME
- Write as continuous narrative, not discrete blocks, in chronological order
- Vary how you mark time passing: ages, seasons, life events, relative time, or dates. For people born before 1000 BC, prefer ages and relative time over absolute dates.
- Discrete events should be assigned to specific times. Never hedge with phrases like  "in [YEAR] or [YEAR]", "around ages X to Y", "sometime in", "through ages X to Y", "X turning Y", instead speak with confidence and choose a specific time.
- Avoid redundant temporal phrases, such as "In the year X, when he was Y"
- Vary paragraph openings, and avoid too frequently beginning with temporal phrases
- Avoid starting consecutive paragraphs with "In [YEAR]" or "By [AGE]"

PROSE STYLE:
- Write actively and directly. State facts plainly and concretely.
- Avoid passive, abstract, or distanced descriptions.
- Include specific details so the reader can see what you mean.
- No figurative language (no metaphors, similes, or personification)
- No archaic inversions, poetic flourishes, or proverbs
- State what happened. Do not comment on it, interpret it, or frame it poetically.
- Do not write lines that exist to sound wise or poignant. If a sentence is reaching for literary effect, cut it or replace it with a plain one.
- Describe what was there, not what wasn't. Avoid defining people or situations by negatives.
- When describing multiple similar events (repeated deaths, marriages, births), vary the sentence structure each time. Do not use the same pattern for sequential losses.

HISTORICAL INTEGRATION:
- Include historical, cultural, and religious framing throughout so readers can follow
- Assume an intelligent reader who can look things up but isn't a specialist
- Early in the narrative, briefly orient the reader to the political and cultural situation: what polity or power structure governed this area, what ethnic/linguistic group and religion the person belonged to, and how that world related to larger historical forces. Keep it short and concrete—a sentence or two, not a paragraph of background.
- Prefer specific over generic where specificity is possible
- When depicting religious practice, name specific deities, spirits, or ancestors where culturally appropriate. Describe the contents of offerings and the physical objects used. Avoid generic terms like "the gods" or "religious observances" when specifics are recoverable for the culture and period.

PERSONALITY:
- Show traits through action, not summary
- Do not name personality traits. Show the behavior and let the reader infer the trait.
- Don't soften negative traits—low agreeableness causes friction, low conscientiousness causes real failures, low intelligence shows in limited understanding and poor decision-making

AVOID THESE PHRASES:
"life went on", "work continued", "people remembered", "was known for", "in those days", "as was common", "like so many", "he suffered", "it was not X, it was Y", "A did not do X. A did Y", "no kings ruled"
'''

# Human particularity section (added for adolescents and adults only)
HUMAN_PARTICULARITY_PROMPT = '''
HUMAN PARTICULARITY:
Include 2-4 specific human details that bring the person to life:
- Friendships: Not just family/spouse, but people they chose to spend time with, who made them laugh or who they trusted
- Small pleasures: What they enjoyed - a particular food, a time of day, a seasonal activity, hobbies, stories they told, gambling, singing, a place they liked to sit
- Habits or routines: daily rituals, how they did their work, where they went when troubled
- Things that annoyed them or they avoided
- Sources of quiet pride or satisfaction
- Humor: Moments of teasing, jokes, laughter
These details should feel plausible for the time, place, cultural, religion, and personality. Aim to be both specific and idiosyncratic.
'''

# Age determines length and focus
AGE_PROMPTS = {
    "infant": """
LENGTH: 150-300 words

FOCUS:
- The infant cannot express personality—focus on parents, household, circumstances
- Can be told entirely from the parents' perspective
- A few vivid details about the household and the infant's brief life
""",

    "child": """
LENGTH: 200-400 words

FOCUS:
- Personality can show in limited, age-appropriate ways (a habit, a preference, how they played)
- Focus on a few vivid moments rather than a full arc
- Show the household and family context
""",

    "adolescent": """
LENGTH: 400-700 words

FOCUS:
- Show emerging adult roles and relationships
- Personality should be visible through behavior and choices
- Include family dynamics and any work or responsibilities
""",

    "adult": """
LENGTH: 600-1000 words

FOCUS:
- Mosaic of everyday episodes
- Include relationships and family changes
- Show work, community, and how they navigated their world
"""
}

# Alive/dead determines ending only
ALIVE_PROMPT = """
ENDING:
- End in an ordinary moment, not on a cliffhanger or dramatic note
- The narrative must end no later than late 2025—do not project events into the future
- End with a present-tense snapshot of their current life
"""

DEAD_PROMPT = """
ENDING:
- Include the death concretely
- If funerary practices are known or inferable for their culture, end with a brief concrete description of burial or memorial (where the body was placed, what was done with it, any offerings or rites). Keep this to 1-2 sentences, and omit if the death circumstances make this impossible
- Do not dwell on aftermath or sentimentalize
- Avoid: "breathing slowed", "fever rose/burned", "eyes closed", "slipped away", "grew weaker", "stopped breathing"
"""

# -----------------------------------------------------------------------------
# Quality Control Prompts
# -----------------------------------------------------------------------------

QC_PROMPT_BASE = """Review this narrative for issues and provide a corrected version.

Person details:
{person_data}

Original narrative:
{narrative}

PROSE STYLE:
- Write actively and directly. State facts plainly and concretely.
- No figurative language: no metaphors, similes, or personification.
- No archaic inversions, poetic flourishes, or lines reaching for literary effect.
- Describe what was there, not what wasn't. Cut negatives that only matter as absences.
- Do not comment on events or interpret them for the reader.

NARRATOR HEDGING:
Remove uncertain language: "likely," "probably," "perhaps," "X or Y," "some kind of."
Replace with specific facts. The narrator knows what happened.

PERSONALITY TRAIT CHECK:
Verify that extreme personality traits are visible and unvarnished. Negative traits should not be reframed as hidden strengths. Dysfunctional, ineffectual, or difficult people must not be bowdlerized into sympathetic eccentrics.

BANNED PHRASES:
Remove or replace: "life went on", "work continued", "people remembered", "was known for", "in those days", "as was common", "like so many", "he suffered", "it was not X, it was Y", "breathing slowed", "fever rose/burned", "eyes closed", "slipped away", "grew weaker", "stopped breathing", "no kings ruled"

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

SELECTION_TEXT = "The random number generator selected for this person: "

# -----------------------------------------------------------------------------
# Hierarchical Structured Incidents Prompts
# -----------------------------------------------------------------------------

# Tier 1: Broad incident categories
TIER1_INCIDENTS_PROMPT_HEADER = '''Based on this person's demographics, personality, and lifetime, estimate the probability that each of the following broad incident categories occurred.

IMPORTANT: Estimate probabilities honestly based on historical base rates for someone with these specific characteristics. Violence (especially sexual and domestic violence) and criminality were endemic in most historical periods. Do not sanitize.

For each category, provide:
- reasoning: Brief explanation (1-2 sentences) of why this probability makes sense
- probability: Your best estimate (0.0 to 1.0) that this occurred at least once

BROAD CATEGORIES:
'''

TIER1_INCIDENTS_PROMPT_FOOTER = '''
Return as JSON with all categories:
{{
  "victim_violence": {{"reasoning": "...", "probability": 0.XX}},
  "victim_property_crime": {{"reasoning": "...", "probability": 0.XX}},
  ...
}}'''

# Category definitions - (key, description)
TIER1_CATEGORY_DEFINITIONS = {
    'victim_violence': 'Victim of physical or sexual violence (assault, sexual violence, domestic violence)',
    'victim_property_crime': 'Victim of property crime (theft, fraud, robbery)',
    'perpetrator_violence': 'Perpetrator of physical or sexual violence (assault, homicide, sexual violence)',
    'perpetrator_property_crime': 'Perpetrator of property crime (theft, fraud, burglary, poaching, smuggling, tax evasion)',
    'severe_economic_crisis': 'Severe financial hardship (debt crisis, destitution, property loss)',
    'serious_health_incident': 'Serious health event that they survived or lived with (accident, chronic illness, acquired disability - NOT the terminal illness/injury that ultimately killed them)',
    'major_caregiving': 'Extended caregiving responsibility (sick relative, orphans, elderly parents)',
    'warfare_impact': 'Direct personal warfare impact (military service, displacement, siege, witnessing violence - NOT indirect economic effects like rationing or taxation)',
    'major_achievement': 'Notable achievement, recognition, or success',
    'religious_change': 'Significant religious change (loss of faith, conversion, apostasy, persecution)',
    'nonstandard_sexual_history': 'Sexual activity outside cultural norms (premarital, extramarital, sex work, same-sex)',
}

# Tier 2: Specific subtypes for sampled broad categories (batched version)
TIER2_SUBTYPES_BATCH_PROMPT = '''The random sampling confirmed this person experienced the following broad categories:
{sampled_categories}

For each category, estimate probabilities for the specific subtypes listed below.
{punishment_instruction}
SUBTYPES BY CATEGORY:
{all_subtypes}

Return as JSON with nested structure:
{{
  "category_name": {{
    "subtype_1": {{"reasoning": "...", "probability": 0.XX}},
    "subtype_2": {{"reasoning": "...", "probability": 0.XX}},
    ...
  }},
  ...
}}'''

# Elaboration prompt (batched version)
ELABORATE_INCIDENTS_PROMPT = '''The random sampling selected that this person experienced the following incidents:
{incidents_list}

For each incident, provide a specific, concrete description of what happened (1-2 sentences maximum). Make each specific to this person's time, place, occupation, and circumstances.

Return as JSON:
{{
  "incident_key_1": {{"event": "specific concrete description", "timing": "precise age range or period"}},
  "incident_key_2": {{"event": "specific concrete description", "timing": "precise age range or period"}},
  ...
}}'''

# Tier 2 subtype definitions
TIER2_SUBTYPES = {
    'victim_violence': [
        ('sexual_violence', 'Sexual assault, rape, or coercion'),
        ('domestic_violence', 'Physical violence from intimate partner or household member'),
        ('physical_assault', 'Non-sexual, non-domestic physical violence (assault, beating, serious fight)'),
    ],
    'perpetrator_violence': [
        ('sexual_violence_perp', 'Perpetrated sexual violence (sexual assault, rape, coercion)'),
        ('homicide', 'Killed someone (combat, murder, manslaughter, duel)'),
        ('physical_assault_perp', 'Perpetrated non-sexual, non-lethal physical violence (assault, serious fight)'),
    ],
    'serious_health_incident': [
        ('serious_accident', 'Serious accident causing weeks+ of incapacity'),
        ('chronic_illness', 'Chronic health condition causing ongoing limitation'),
        ('acquired_disability', 'Acquired disabling condition (vision/hearing loss, mobility impairment)'),
    ],
    'major_caregiving': [
        ('sick_relative', 'Prolonged caregiving for seriously ill/disabled family member'),
        ('orphaned_children', 'Raised children who weren\'t biologically theirs'),
        ('elderly_parents', 'Primary caregiver for aging parents/in-laws'),
    ],
    'warfare_impact': [
        ('military_service', 'Formal military service, conscription, or militia duty'),
        ('civilian_war_exposure', 'Civilian war exposure (displacement, siege, occupation, bombing)'),
        ('witnessed_atrocity', 'Witnessed killing, torture, or mass violence firsthand'),
        ('captive', 'Taken prisoner of war, or forceable moved or enslaved as a civilian')
    ],
    'nonstandard_sexual_history': [
        ('premarital_sex', 'Consensual sexual activity before marriage'),
        ('extramarital_sex', 'Sexual activity outside primary partnership/marriage'),
        ('sex_work', 'Engaged in transactional sex for money/goods/favors'),
    ],
    'nonstandard_sexual_history_female': [
        ('pregnancy_outside_marriage', 'Pregnancy before or outside formal marriage/partnership'),
        ('pregnancy_complications', 'Miscarriage, stillbirth, or serious birth complication'),
        ('abortion_attempt', 'Attempted abortion or use of abortifacient'),
    ],
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def _get_mental_disorder(person):
    """Get mental disorder if present. Returns None if too young or no disorder."""
    if person.years_lived() < AGE_CHILD:
        return None

    disorder = person.demographics.get('mental_disorder', '')
    if not disorder:
        return None

    # Filter out "no disorder" responses
    lower = disorder.lower()
    no_disorder_patterns = ['no ', 'no:', 'none', 'unlikely', 'no clear', 'no diagnosable',
                            'no modern', 'not meet', 'would not']
    if any(p in lower[:50] for p in no_disorder_patterns):
        return None
    return disorder


def _age_category(person):
    """Get age category for narrative prompts."""
    age = person.years_lived()
    if age < AGE_CHILD:
        return "infant"
    elif age < AGE_ADOLESCENT:
        return "child"
    elif age < AGE_ADULT:
        return "adolescent"
    else:
        return "adult"


def _build_trait_context(person):
    """Build context string with personality traits (flagging extremes) and any mental disorder."""
    if person.years_lived() < AGE_CHILD:
        return ""  # Too young for trait manifestation planning

    lines = ["\nPERSONALITY AND CONDITIONS:"]

    if person.personality:
        lines.append("Personality traits (percentile ranks, 0-100):")
        for key, value in person.personality.items():
            trait_name = key.replace(' (% rank)', '')
            # Flag extremes (5th percentile threshold)
            if value <= 5:
                lines.append(f"- {trait_name}: {value}th percentile ← very low (must be visible)")
            elif value >= 95:
                lines.append(f"- {trait_name}: {value}th percentile ← very high (must be visible)")
            else:
                lines.append(f"- {trait_name}: {value}th percentile")

    disorder = _get_mental_disorder(person)
    if disorder:
        lines.append(f"\nMENTAL DISORDER (must be visible): {disorder}")

    lines.append("")
    return "\n".join(lines)


def _get_demographic_queries(person):
    """Get filtered demographic queries for this person based on era, age, and alive status."""
    results = []
    for name, query, query_era, min_age, requires_dead in DEMOGRAPHIC_QUERIES:
        # Basic filters: era, age, alive status
        if query_era != 'Both' and query_era != person.era:
            continue
        if person.years_lived() < min_age:
            continue
        if requires_dead and person.is_alive():
            continue

        # Special case: co_twin_fate only asked if person is a twin
        if name == 'co_twin_fate':
            if not person.twin:
                continue
            # Format the query with twin type
            query = query.format(twin_type=person.twin)

        results.append((name, query))
    return results


def reset_to_stage(person, stage):
    """
    Reset person to the start of a specific pipeline stage, removing all later-stage data.

    Stages (in order):
    - 'demographics': Before demographics are generated
    - 'incidents': Before structured incidents are generated
    - 'historical_context': Before historical context is generated
    - 'name': Before name is generated
    - 'narrative_plan': Before narrative plan is generated
    - 'narrative': Before narrative is generated
    - 'qc': Before quality check is run
    """
    stages_order = ['demographics', 'incidents', 'historical_context', 'name', 'narrative_plan', 'narrative', 'qc']

    if stage not in stages_order:
        raise ValueError(f"Unknown stage: {stage}. Must be one of {stages_order}")

    stage_idx = stages_order.index(stage)

    # Clear data from this stage and all later stages
    if stage_idx <= stages_order.index('qc'):
        pass  # QC only modifies narrative, handled below
    if stage_idx <= stages_order.index('narrative'):
        person.narrative = None
    if stage_idx <= stages_order.index('narrative_plan'):
        person.narrative_plan = None
    if stage_idx <= stages_order.index('name'):
        person.name = None
        person.naming_category = None
    if stage_idx <= stages_order.index('historical_context'):
        person.historical_context = []
    if stage_idx <= stages_order.index('incidents'):
        person.structured_incidents = []
    if stage_idx <= stages_order.index('demographics'):
        person.messages = []
        person.demographics = {}
        return  # Nothing more to do

    # For later stages, truncate messages at the appropriate point
    # Stage markers - text that appears at the start of each stage's prompt
    stage_markers = {
        'incidents': 'estimate the probability that each of the following broad incident categories',
        'historical_context': 'list HISTORICAL and ENVIRONMENTAL CONTEXT events',
        'name': 'Generate 20 possible names',
        'narrative_plan': 'Before writing the narrative, create a detailed timeline',
        'narrative': 'Write a narrative biography',
    }

    if stage in stage_markers:
        marker = stage_markers[stage]
        for i, msg in enumerate(person.messages):
            if marker in msg.get('content', ''):
                person.messages = person.messages[:i]
                return
    
# =============================================================================
# GENERATION FUNCTIONS
# =============================================================================

def generate_geography(person, ctx):
    """
    Refine geographic location for Paleolithic people.
    Only called for Paleolithic era - Holocene has pre-computed locations.

    Builds up a multi-turn conversation internally for context, but stores it
    separately in person.geo_messages (for debugging) rather than person.messages.

    Modifies person in place.
    """
    if person.era != 'Paleolithic':
        return

    region = person.region
    year = person.birth_year_str

    # Initialize geography conversation
    geo_messages = []

    # Step 1: Get subregion
    ctx.log(f"Getting subregion distribution for {region}, {year}...")

    geo_messages.append({"role": "user", "content": GEOGRAPHY_PROMPT.format(region=region, year=year)})
    result, content = call_with_retry(ctx, geo_messages)

    if result and 'subregions' in result:
        subregion = sample_distribution(result['subregions'])
        person.demographics['Subregion'] = subregion
        ctx.log(f"  Sampled: {subregion}")
        geo_messages.append({"role": "assistant", "content": content})
        geo_messages.append({"role": "user", "content": SELECTION_TEXT + subregion})
    else:
        person.demographics['Subregion'] = 'Unknown'
        subregion = region

    # Step 2: Get specific location
    ctx.log(f"Getting location distribution within {subregion}...")

    geo_messages.append({"role": "user", "content": SUBSUBREGION_PROMPT.format(subregion=subregion, year=year)})
    result, content = call_with_retry(ctx, geo_messages)

    if result and 'locations' in result:
        subsubregion = sample_distribution(result['locations'])
        person.demographics['Subsubregion'] = subsubregion
        ctx.log(f"  Sampled: {subsubregion}")
        geo_messages.append({"role": "assistant", "content": content})
        geo_messages.append({"role": "user", "content": SELECTION_TEXT + subsubregion})
    else:
        person.demographics['Subsubregion'] = subregion
        subsubregion = subregion

    # Step 3: Get environment details
    ctx.log("Getting environment details...")

    geo_messages.append({"role": "user", "content": ENVIRONMENT_PROMPT.format(subsubregion=subsubregion, year=year)})
    env_result, content = call_with_retry(ctx, geo_messages)

    if env_result:
        person.demographics['Environment'] = env_result.get('environment', 'Unknown')
        person.demographics['Cultural tradition'] = env_result.get('cultural_tradition', 'Unknown')
        person.demographics['Climate then'] = env_result.get('climate_then', '')
        person.demographics['Climate now'] = env_result.get('climate_now', '')
        ctx.log(f"  Environment: {person.demographics['Environment']}")
        geo_messages.append({"role": "assistant", "content": content})

    # Store for debugging (not used by main pipeline)
    person.geo_messages = geo_messages


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


def generate_structured_incidents(person, ctx, elaborate=True):
    """
    Generate personal incidents using hierarchical probability assessment.

    Two-tier system:
    - Tier 1: Assess ~10 broad categories (victim, perpetrator, health, etc.)
    - Tier 2: For sampled Tier 1 categories, assess specific subtypes
    - Elaborate: Generate concrete descriptions for all sampled incidents

    Args:
        person: Person object with demographics already populated
        ctx: GenerationContext
        elaborate: If True, make follow-up calls to get concrete descriptions

    Modifies person in place, storing results in person.structured_incidents
    """
    if person.years_lived() < AGE_CHILD:
        ctx.log("Too young for structured incidents")
        person.structured_incidents = []
        return

    # =============================================================================
    # TIER 1: Assess broad categories
    # =============================================================================

    ctx.log("TIER 1: Assessing broad incident categories...")

    # Determine which Tier 1 categories to assess
    tier1_categories = [
        'victim_violence',
        'victim_property_crime',
        'perpetrator_violence',
        'perpetrator_property_crime',
        'severe_economic_crisis',
        'serious_health_incident',
        'major_caregiving',
        'major_achievement',
        'religious_change',
    ]

    # Add age-conditional category
    if person.years_lived() >= AGE_ADOLESCENT:
        tier1_categories.append('nonstandard_sexual_history')

    # Add era-conditional category
    if person.era == 'Holocene':
        tier1_categories.append('warfare_impact')

    # Build prompt dynamically based on selected categories
    categories_text = '\n'.join(
        f"- {cat}: {TIER1_CATEGORY_DEFINITIONS[cat]}"
        for cat in tier1_categories
    )
    tier1_prompt = TIER1_INCIDENTS_PROMPT_HEADER + categories_text + TIER1_INCIDENTS_PROMPT_FOOTER

    # Build and send Tier 1 prompt
    person.messages.append({"role": "user", "content": tier1_prompt})

    tier1_data, content = call_with_retry(ctx, person.messages)

    if not tier1_data:
        ctx.log("  Failed to parse Tier 1 data")
        person.messages.pop()
        person.structured_incidents = []
        return

    person.messages.append({"role": "assistant", "content": content})

    # Log Tier 1 probabilities
    ctx.log("  Tier 1 probabilities:")
    for category in tier1_categories:
        if category in tier1_data:
            prob = tier1_data[category].get('probability', 0)
            reasoning = tier1_data[category].get('reasoning', '')
            if not ctx.quiet or prob > 0.05:
                ctx.log(f"    {category}: {prob:.2f} - {reasoning[:60]}...")

    # Sample Tier 1 categories
    sampled_tier1 = []
    for category in tier1_categories:
        if category not in tier1_data:
            continue

        prob = tier1_data[category].get('probability', 0)
        reasoning = tier1_data[category].get('reasoning', '')

        if random.random() < prob:
            sampled_tier1.append({
                'category': category,
                'reasoning': reasoning,
                'probability': prob
            })

    ctx.log(f"  Sampled {len(sampled_tier1)} Tier 1 categories")

    # =============================================================================
    # TIER 2: Assess subtypes for sampled categories (batched)
    # =============================================================================

    all_sampled_incidents = []

    # Separate categories with and without subtypes
    standalone_categories = ['victim_property_crime', 'perpetrator_property_crime',
                             'severe_economic_crisis', 'major_achievement', 'religious_change']

    # Check if any perpetrator categories were sampled (for punishment question)
    committed_crime = any(
        item['category'] in ['perpetrator_violence', 'perpetrator_property_crime']
        for item in sampled_tier1
    )

    # Add standalone categories directly to sampled incidents
    for tier1_item in sampled_tier1:
        category = tier1_item['category']
        if category in standalone_categories:
            all_sampled_incidents.append({
                'type': category,
                'reasoning': tier1_item['reasoning'],
                'probability': tier1_item['probability'],
                'tier': 1
            })

    # Collect categories that need Tier 2 subtype assessment
    categories_needing_tier2 = []
    category_subtypes = {}  # Maps category -> list of (subtype_name, description)

    for tier1_item in sampled_tier1:
        category = tier1_item['category']
        if category in standalone_categories:
            continue
        if category not in TIER2_SUBTYPES:
            continue

        categories_needing_tier2.append(tier1_item)

        # Get subtype definitions
        subtypes = list(TIER2_SUBTYPES[category])

        # Special case: add female-specific pregnancy subtypes if applicable
        if category == 'nonstandard_sexual_history' and person.sex == 'F' and person.years_lived() >= 13:
            subtypes = subtypes + list(TIER2_SUBTYPES['nonstandard_sexual_history_female'])

        category_subtypes[category] = subtypes

    # If there are categories needing Tier 2, make a single batched call
    if categories_needing_tier2:
        ctx.log(f"  TIER 2: Assessing subtypes for {len(categories_needing_tier2)} categories (batched)...")

        # Build the prompt
        sampled_categories = '\n'.join(
            f"- {item['category'].replace('_', ' ')}"
            for item in categories_needing_tier2
        )

        all_subtypes_parts = []
        for item in categories_needing_tier2:
            category = item['category']
            subtypes = category_subtypes[category]
            subtypes_str = '\n'.join(f"  - {name}: {desc}" for name, desc in subtypes)
            all_subtypes_parts.append(f"{category}:\n{subtypes_str}")

        all_subtypes = '\n\n'.join(all_subtypes_parts)

        # Add punishment instruction if applicable
        if committed_crime:
            punishment_instruction = '''
Also estimate the probability of faced_punishment (arrested, tried, fined, imprisoned, publicly punished, or executed) for any perpetrator categories.
'''
        else:
            punishment_instruction = ''

        tier2_prompt = TIER2_SUBTYPES_BATCH_PROMPT.format(
            sampled_categories=sampled_categories,
            all_subtypes=all_subtypes,
            punishment_instruction=punishment_instruction
        )

        person.messages.append({"role": "user", "content": tier2_prompt})
        tier2_data, tier2_content = call_with_retry(ctx, person.messages)

        if tier2_data:
            person.messages.append({"role": "assistant", "content": tier2_content})

            # Process each category's subtypes
            for item in categories_needing_tier2:
                category = item['category']
                subtypes = category_subtypes[category]

                category_data = tier2_data.get(category, {})

                # Log and sample subtypes
                for subtype_name, _ in subtypes:
                    if subtype_name not in category_data:
                        continue

                    prob = category_data[subtype_name].get('probability', 0)
                    reasoning = category_data[subtype_name].get('reasoning', '')

                    if not ctx.quiet or prob > 0.05:
                        ctx.log(f"    {category}.{subtype_name}: {prob:.2f}")

                    if random.random() < prob:
                        all_sampled_incidents.append({
                            'type': subtype_name,
                            'reasoning': reasoning,
                            'probability': prob,
                            'tier': 2,
                            'parent_category': category
                        })

            # Handle punishment if it was included
            if committed_crime and 'faced_punishment' in tier2_data:
                punishment_data = tier2_data['faced_punishment']
                # Handle both nested and flat structures
                if isinstance(punishment_data, dict) and 'probability' in punishment_data:
                    prob = punishment_data.get('probability', 0)
                    reasoning = punishment_data.get('reasoning', '')
                elif isinstance(punishment_data, dict):
                    # Might be nested under a key
                    for key, val in punishment_data.items():
                        if isinstance(val, dict) and 'probability' in val:
                            prob = val.get('probability', 0)
                            reasoning = val.get('reasoning', '')
                            break
                    else:
                        prob = 0
                        reasoning = ''
                else:
                    prob = 0
                    reasoning = ''

                if not ctx.quiet or prob > 0.05:
                    ctx.log(f"    faced_punishment: {prob:.2f}")

                if random.random() < prob:
                    all_sampled_incidents.append({
                        'type': 'faced_punishment',
                        'reasoning': reasoning,
                        'probability': prob,
                        'tier': 2,
                        'parent_category': 'perpetrator_crime'
                    })
        else:
            ctx.log("    Failed to parse Tier 2 data")
            person.messages.pop()

    ctx.log(f"  Total sampled incidents (Tier 1 + Tier 2): {len(all_sampled_incidents)}")

    # =============================================================================
    # ELABORATE: Generate concrete descriptions (batched)
    # =============================================================================

    if elaborate and all_sampled_incidents:
        ctx.log("  Elaborating sampled incidents (batched)...")

        # Build list of incidents for prompt
        incidents_list = '\n'.join(
            f"- {inc['type']}: {inc['type'].replace('_', ' ')}"
            for inc in all_sampled_incidents
        )

        elab_prompt = ELABORATE_INCIDENTS_PROMPT.format(incidents_list=incidents_list)
        person.messages.append({"role": "user", "content": elab_prompt})
        elab_data, elab_content = call_with_retry(ctx, person.messages)

        if elab_data:
            person.messages.append({"role": "assistant", "content": elab_content})

        # Build elaborated list, using LLM output where available
        elaborated = []
        for incident in all_sampled_incidents:
            incident_type = incident['type']
            reasoning = incident['reasoning']
            display_name = incident_type.replace('_', ' ')

            # Try to get elaboration from batched response
            if elab_data and incident_type in elab_data:
                inc_data = elab_data[incident_type]
                elaborated.append({
                    'event': inc_data.get('event', f'[{display_name}]'),
                    'timing': inc_data.get('timing', 'unknown'),
                    'type': incident_type,
                    'reasoning': reasoning,
                    'tier': incident['tier']
                })
                ctx.log(f"    {incident_type}: {inc_data.get('event', '')[:60]}...")
            else:
                # Elaboration missing for this incident, use fallback
                elaborated.append({
                    'event': f"[{display_name}]",
                    'timing': 'unknown',
                    'type': incident_type,
                    'reasoning': reasoning,
                    'tier': incident['tier']
                })
                ctx.log(f"    {incident_type}: [no elaboration]")

        person.structured_incidents = elaborated
    else:
        # Store raw sampled incidents without elaboration
        person.structured_incidents = [
            {
                'event': incident['type'].replace('_', ' '),
                'timing': 'unknown',
                'type': incident['type'],
                'reasoning': incident['reasoning'],
                'tier': incident['tier']
            }
            for incident in all_sampled_incidents
        ]

    ctx.log(f"  Final structured incidents: {len(person.structured_incidents)}")


def generate_historical_context(person, ctx):
    """
    Generate historical/environmental context events through probabilistic sampling.

    This generates large-scale contextual forces (wars, famines, regime changes, etc.)
    that affected the person's environment. Personal incidents are handled separately
    by generate_structured_incidents().

    Only called for non-hunter-gatherers (well-documented periods with better historical records).

    Modifies person in place, storing results in person.historical_context.
    """
    if person.years_lived() < AGE_CHILD:
        ctx.log("Too young for historical context")
        person.historical_context = []
        return

    if person.lifestyle == 'Hunter-Gatherer':
        ctx.log("Skipping historical context for hunter-gatherer (poorly documented period)")
        person.historical_context = []
        return

    ctx.log("Generating historical/environmental context...")

    person.messages.append({"role": "user", "content": HISTORICAL_CONTEXT_PROMPT})

    context_data, content = call_with_retry(ctx, person.messages)

    if not context_data:
        ctx.log("  Failed to parse historical context")
        person.messages.pop()
        person.historical_context = []
        return

    person.messages.append({"role": "assistant", "content": content})
    potential_events = context_data.get('events', [])
    ctx.log(f"  Generated {len(potential_events)} potential context events")

    # Sample events (Bernoulli trials)
    selected_events = [e for e in potential_events if random.random() < e.get('probability', 0)]
    ctx.log(f"  Sampled {len(selected_events)} context events")

    # Store selected events (strip probability since it's no longer needed)
    person.historical_context = [
        {"event": e.get("event", ""), "timing": e.get("timing", "")}
        for e in selected_events
    ]

    ctx.log(f"  Final historical context: {len(person.historical_context)}")


def generate_name(person, ctx):
    """
    Generate a name for the person by having the LLM propose 20 options
    and randomly selecting one.

    Modifies person in place.
    """
    ctx.log("Generating name...")

    person.messages.append({"role": "user", "content": NAMING_PROMPT})

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


def generate_narrative_plan(person, ctx):
    """
    Generate a narrative plan/timeline before writing the narrative.

    Tiered by age category:
    - Infant (0-4): Sibling timeline only
    - Child (5-12): Siblings + incidents + traits + characters
    - Adolescent/Adult (13+): Full planning including partners, children, life phases

    This ensures temporal consistency in the narrative.

    Modifies person in place, storing results in person.narrative_plan.
    """
    age_cat = _age_category(person)

    # Build context about what needs to be planned
    plan_context = []

    # Add sibling info if present (all age tiers)
    if 'sibling_sexes' in person.demographics:
        sexes = person.demographics['sibling_sexes']
        ages = person.demographics.get('sibling_ages_at_death', [])
        birth_order = person.demographics.get('birth_order_position', 1)

        plan_context.append(f"SIBLING DATA:")
        plan_context.append(f"- This person was child #{birth_order} of {len(sexes) + 1} children")
        if person.is_alive():
            plan_context.append(f"- This person was born in {person.birth_year} and is still alive at the start of 2026 (age {person.years_lived()})")
        else:
            plan_context.append(f"- This person was born in {person.birth_year} and died in {person.death_date[0]} (age {person.years_lived()})")
        plan_context.append(f"- Siblings (in birth order):")

        for i, (sex, sib_age) in enumerate(zip(sexes, ages)):
            position = i + 1 if i < birth_order - 1 else i + 2  # Account for person's position
            relation = "older" if position < birth_order else "younger"
            sex_word = "sister" if sex == 'F' else "brother"
            plan_context.append(f"  {position}. {relation} {sex_word} - died at age {sib_age}")

    # Add children info if present (adolescent/adult only)
    if age_cat in ["adolescent", "adult"] and 'children_sexes' in person.demographics:
        sexes = person.demographics['children_sexes']
        ages = person.demographics.get('children_ages_at_death', [])

        plan_context.append(f"\nCHILDREN DATA:")
        plan_context.append(f"- {len(sexes)} children total")
        for i, (sex, child_age) in enumerate(zip(sexes, ages)):
            sex_word = "daughter" if sex == 'F' else "son"
            plan_context.append(f"  {i+1}. {sex_word} - died at age {child_age}")

    # Add structured incidents if present (child and above)
    if age_cat != "infant" and hasattr(person, 'structured_incidents') and person.structured_incidents:
        plan_context.append(f"\nINCIDENTS TO PLACE:")
        for inc in person.structured_incidents:
            plan_context.append(f"- {inc.get('type', 'unknown')}: {inc.get('event', '')} (suggested timing: {inc.get('timing', 'unknown')})")

    # Add historical context if present (child and above)
    if age_cat != "infant" and hasattr(person, 'historical_context') and person.historical_context:
        plan_context.append(f"\nHISTORICAL CONTEXT:")
        for ctx_event in person.historical_context:
            plan_context.append(f"- {ctx_event.get('event', '')} ({ctx_event.get('timing', '')})")

    # Add personality and mental disorder context (child and above)
    if age_cat != "infant":
        trait_context = _build_trait_context(person)
        if trait_context:
            plan_context.append(trait_context)

    ctx.log(f"Generating narrative plan ({age_cat})...")

    full_prompt = NARRATIVE_PLAN_PROMPTS[age_cat]
    if plan_context:
        full_prompt += "\n\n" + "\n".join(plan_context)

    person.messages.append({"role": "user", "content": full_prompt})

    plan_data, content = call_with_retry(ctx, person.messages)

    if not plan_data:
        ctx.log("  Failed to generate narrative plan")
        person.messages.pop()
        person.narrative_plan = None
        return

    person.messages.append({"role": "assistant", "content": content})
    person.narrative_plan = plan_data

    # Log summary
    siblings = plan_data.get('siblings', [])
    children = plan_data.get('children', [])
    phases = plan_data.get('life_phases', [])
    ctx.log(f"  Plan: {len(siblings)} siblings, {len(children)} children, {len(phases)} life phases")


def generate_narrative(person, ctx, extra_prompt=None):
    """
    Generate biographical narrative.

    Args:
        person: Person object with demographics and events populated
        ctx: GenerationContext
        extra_prompt: Optional string to append to the standard prompt (for experimentation)

    Modifies person in place.
    """
    age_cat = _age_category(person)

    # Build prompt: base + age-specific focus + ending
    full_prompt = NARRATIVE_BASE_PROMPT

    # Add human particularity section for adolescents and adults only
    if age_cat in ["adolescent", "adult"]:
        full_prompt += HUMAN_PARTICULARITY_PROMPT

    full_prompt += AGE_PROMPTS[age_cat]
    full_prompt += ALIVE_PROMPT if person.is_alive() else DEAD_PROMPT

    # Add any experimental modifications
    if extra_prompt:
        full_prompt += "\n\n" + extra_prompt

    # Reference the narrative plan if one exists
    if hasattr(person, 'narrative_plan') and person.narrative_plan:
        full_prompt += "\n\nIMPORTANT: Follow the narrative plan you created earlier. Use the exact timeline for siblings, children, and incidents. The plan ensures temporal consistency."

    # Structured incidents and historical context (already in conversation history)
    if hasattr(person, 'structured_incidents') and person.structured_incidents:
        incidents_str = "\n".join(f"- {e.get('event', '')} ({e.get('timing', 'unknown')})"
                                  for e in person.structured_incidents)
        full_prompt += "\n\nPersonal incidents to incorporate:\n" + incidents_str

    if hasattr(person, 'historical_context') and person.historical_context:
        context_str = "\n".join(f"- {e.get('event', '')} ({e.get('timing', 'unknown')})"
                                for e in person.historical_context)
        full_prompt += "\n\nHistorical context to incorporate:\n" + context_str

    person.messages.append({"role": "user", "content": full_prompt})

    ctx.log(f"Generating narrative ({age_cat})...")

    person.narrative = ctx.call(person.messages)
    person.messages.append({"role": "assistant", "content": person.narrative})

    ctx.log(f"  Generated {len(person.narrative.split())} words")


def quality_check(person, ctx):
    """
    Review and revise narrative for issues.

    Modifies person in place.
    Returns list of issues found.
    """
    qc_prompt = QC_CHECKS_ERA[person.era] + QC_PROMPT_BASE.format(
        person_data=person.to_prompt_string(),
        narrative=person.narrative
    )

    ctx.log("Running quality check on narrative...")

    messages = [{"role": "user", "content": qc_prompt}]
    result, _ = call_with_retry(ctx, messages)

    if result:
        issues = result.get('issues_found', [])
        person.narrative = result.get('revised_narrative', person.narrative)

        count = len(issues) if isinstance(issues, list) else sum(len(v) for v in issues.values() if isinstance(v, list))
        ctx.log(f"  Fixed {count} issues")
        return issues
    else:
        ctx.log("  QC failed, keeping original")
        return []


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
    ctx.log("Step 3: Generating structured incidents...")
    generate_structured_incidents(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 4: Generating historical context...")
    generate_historical_context(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 5: Generating name...")
    generate_name(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 6: Generating narrative plan...")
    generate_narrative_plan(person, ctx)

    ctx.log("\n" + "=" * 50)
    ctx.log("Step 7: Generating narrative...")
    generate_narrative(person, ctx)

    # QC step removed - wasn't adding enough value to justify the cost.
    # quality_check() is still available if needed for spot-checking.

    ctx.finish()

    return person


def _prepare_person_for_generation(person):
    """Clear age-inappropriate attributes from a sampled person.

    This must be called after sampling and before generation pipeline.
    Personality and orientation are sampled in Person.__init__ but should
    be cleared for people who died too young to manifest them.
    """
    # Clear personality if died before childhood threshold
    if person.years_lived() < AGE_CHILD:
        person.personality = None

    # Clear orientation if died before adolescent threshold
    if person.years_lived() < AGE_ADOLESCENT:
        person.orientation = None

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
    _prepare_person_for_generation(person)

    return run_pipeline(person, model=model, quiet=quiet, show_cost=show_cost)


def generate_batch(n=10, model="haiku", quiet=True, show_cost=False):
    """Generate a batch of people with narratives (sequential)."""
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


def generate_batch_parallel(n=10, model="haiku", workers=5):
    """Generate a batch of people with narratives in parallel.

    Args:
        n: Number of people to generate
        model: LLM model to use
        workers: Number of parallel workers (default 5)

    Returns:
        List of Person objects (successful generations only)
    """
    from concurrent.futures import ThreadPoolExecutor
    from tqdm import tqdm

    # Pre-sample all people to ensure data is loaded before threading
    print(f"Sampling {n} people...")
    people = [_prepare_person_for_generation(sample_person()) for _ in range(n)]

    def generate_one(person):
        try:
            run_pipeline(person, model=model, quiet=True)
            return person
        except Exception as e:
            print(f"  Failed: {person.era}, {person.birth_year_str} - {e}")
            return None

    print(f"Generating {n} people with {workers} parallel workers...")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(tqdm(executor.map(generate_one, people), total=n))

    results = [p for p in results if p is not None]
    failed = n - len(results)
    if failed > 0:
        print(f"Done: {len(results)} generated, {failed} failed")
    else:
        print(f"Done: {len(results)} generated")
    return results
