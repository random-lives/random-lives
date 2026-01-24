---
layout: default
title: About
permalink: /about/
---

<div class="about" markdown="1">

# About

[About 70 billion people have ever lived]({{ site.baseurl }}/blog/how-many-people-have-ever-lived/). This project randomly samples just 250 of these lives, to give a window into what a "typical" human experience was like.

We cannot, of course, randomly sample from all humans the way we can read random articles on [Wikipedia](https://en.wikipedia.org/wiki/Special:Random), view random roads on [Random Street View](https://randomstreetview.com/), or listen to random radio stations on [Radio Garden](https://radio.garden/balloon-ride). For the vast majority of people who ever lived, essentially nothing remains of their lives. In the absence of root access to The Book of Life or a simulator's log, this project aims to simulate such a random draw as best we can with the available data.

The 250 stories here are fictional. We know more about some times and places than others, but the aim was to sample from the full distribution of human lives without biasing toward the historically legible. A 20th-century French bureaucrat leaves more records than a medieval Chinese peasant or a slash-and-burn farmer in Papua New Guinea; we aim to represent all lives proportionally, with verisimilitude if not accuracy. The result is a collection heavy on infant deaths and subsistence farmers, often obscure and sometimes bleak, but better reflecting reality than history filtered through the literate few.

## The Pipeline

The generation process begins by sampling a birth year and birthplace. For the 95% of humans born in the last 12,000 years, we use the [HYDE database](https://landuse.sites.uu.nl/hyde-project/) for population density combined with estimates of birth rates. Lifespan comes from life tables matched to region and era; detailed and mostly reliable for the last century, increasingly approximate further back.

Generating a list of years and places only gets us so far. We can sample some additional qualities, like sex or handedness, from base rates that have remained stable through history. But for culture, religion, family structure, occupation—there's no dataset that says "for a girl born in Telangana in 323 CE, here are the fraction that spoke proto-Telugu, were devout Buddhist, and raised by their paternal grandmother."

When I first experimented with this project in 2022, I didn't see a way around this. I considered a blog project of manually researching and sampling one person a week. But generating even a few dozen stories would have taken months and required lots of guesswork which my perfectionist streak would struggle to handle. I shelved it.

Large language models changed this. We can ask: "For a girl born in Telangana in 323 CE, what's a plausible probability distribution over native languages?" and get a reasonable answer. Not a perfect answer—given data limitations, even the best expert attempts would often be rough guesses—but good enough to sample from.

To build up a picture of someone's life, we ask a series of questions—ethnicity, religion, family structure, occupation, marriage, cause of death—sampling from each distribution and conditioning on previous answers. The same person—a girl born in 1910 NYC who dies at 60—might be a Jewish seamstress who never married and died of breast cancer, an Italian Catholic mother of six who lost her husband in the war, or a Black domestic worker who outlived two husbands and helped raise her grandchildren.

Demographics alone produced bland stories. So we also sample life events: violence (as victim or perpetrator), economic crisis, serious illness, warfare, caregiving, and others. Each is estimated as a probability for this specific person, then sampled. The model also identifies historical events that might have touched this person's life—a famine, an epidemic, a war, a new tax—and we sample to determine which ones actually affected them.

The final step is turning this pile of data into a story a human would want to read. Making the LLM write stories was not hard; making it write good stories proved challenging. Left to its own devices, the model would exhaustively describe someone burying each of their family members in sequence, only to end with their own death and burial and invariably concluding with "But the harvest must go on." Descriptions of domestic violence would be interrupted with cheerful asides about their favorite foods. The occasional person would be born to a mother several years deceased, or have an older brother already in their eighties. Asked to review its own work, the model assured me: "This is a remarkable piece of historical fiction, vividly imagined and deeply grounded."

After many iterations, what worked best was forcing a narrative planning step: the LLM lists main events and characters in detail and places them in logical order before writing. The story prompt itself evolved through several rounds of whack-a-mole and a growing "banned phrases" list. At some point this process ran out of steam. The automated pipeline gets maybe 80% of the way to good stories. A Claude Code skill catches many remaining issues systematically, but the final step is still me or my wife reviewing manually. I've probably missed some howlers—please send them my way—but for the sake of sanity I've had to declare victory and stop.

LLMs improved steadily over the project's life, which meant my pipeline got better without effort. I settled on [GPT-5.2](https://openai.com/) for generation and [Claude Sonnet 4.5](https://www.anthropic.com/) for review and coding. The downside: as models improved, I grew more ambitious, and costs grew accordingly. Each story costs about $0.25 for GPT-5.2 to generate, $0.20 for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) to review, and time from me to review (unmetered). Initially I had ambitions to generate 1,000 or even 10,000 lives, but 250 is enough for now.

## The People

The easiest way to get a feel for the stories is to read them. The [list view]({{ site.baseurl }}/lives/) shows them all and allows sorting and filtering. The [map view]({{ site.baseurl }}/map/) and [timeline view]({{ site.baseurl }}/timeline/) show how they're distributed spatially and temporally.

The stories can feel repetitive: another subsistence farmer, another dead infant, another life with small horizons bounded by poverty and disease. Almost half of those sampled die before age five. Perhaps the modal human life is an Indian boy who died in infancy between 500 and 1500 AD.

The lives vary hugely in how much we can know about them. 27 are still alive today, the youngest born in 2024. Six lived over 20,000 years ago and can't be linked to any known archaeological culture—two were born in places now underwater. Even some more recent lives—[Tari]({{ site.baseurl }}/lives/0082-tari/) in 10th-century Brazil, [Nabira]({{ site.baseurl }}/lives/0103-nabira/) in 18th-century Congo—come from times and places that left few records. But in general, the further back you go, the more the stories are inference and imagination rather than reconstruction.

Despite these difficulties, I chose to include all the dead infants and shadowy hunter-gatherers rather than resample for lives that left better records. The stories try to make them vivid and specific even where the specifics are, by necessity, invented. This seemed better than either leaving them as abstractions or excluding them entirely.

I hope you find the stories interesting. If you spot errors or have suggestions, please contact me at [email].

<div class="about-buttons">
  <a href="#" class="button" id="random-life-btn">Random Life</a>
  <a href="{{ site.baseurl }}/author/" class="button">About the Author</a>
</div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const allLives = [
    {% for life in site.lives %}
      "{{ life.url | relative_url }}"{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];
  var btn = document.getElementById('random-life-btn');
  if (btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const randomIndex = Math.floor(Math.random() * allLives.length);
      window.location.href = allLives[randomIndex];
    });
  }
});
</script>
