---
layout: post
title: "How many people have ever lived?"
date: 2026-01-18
permalink: /blog/how-many-people-have-ever-lived/
mathjax: true
---
No one really knows how many people ever lived. Even today, counting people can be hard. Papua New Guinea's 2024 census was their first in 24 years, with prior estimates ranging [from 10 million to 17 million](https://www.lowyinstitute.org/the-interpreter/png-needs-census-not-more-population-estimates); Afghanistan hasn't conducted one since 1979\. But such disputes are nothing compared to the uncertainty in pre-industrial populations—estimates for the world population in 10,000 BC range from 1 million to 20 million.

On the internet, a figure of 108 billion or 117 billion is usually, and uncritically, repeated. Both estimates trace to a series of articles from the [Population Reference Bureau](https://www.prb.org/articles/how-many-people-have-ever-lived-on-earth/). When I tried to reproduce their methodology for this project, I found I couldn't—the pre-industrial life expectancy they assumed was far lower than any documented population over a sustained time period. 

My median estimate is **66 billion**, which is what I use when sampling lives. But the more honest answer is probably somewhere between 55–82 billion. Admittedly crude, but a point estimate would give false sense of precision. Even given my uncertainties, though, my upper bound still falls well short of PRB's 117 billion. 

## Post-1800: Summing Estimated Births

The [United Nations World Population Prospects 2024](https://population.un.org/wpp/) provides annual birth estimates from 1950 through 2023, with projections to 2100 (see the [OWID page](https://ourworldindata.org/births-and-deaths) for convenient data access). Summing through 2023 and adding extrapolations for 2024 and 2025 gives 9.61 billion births over that period. The UN doesn't provide uncertainty estimates, but I would guess the figures are within 1% of the true value.

[Gapminder](https://www.gapminder.org/data/) extends birth estimates back to 1800, adding another 8.65 billion from 1800–1949. They don't include methodology documentation for this specific dataset, though they do provide [documentation for related population estimates](https://www.gapminder.org/data/documentation/gd003/). The results are broadly consistent with independent population and life expectancy estimates for the period—perhaps within 5% of the true count.

## Pre-1800: Estimating from Population

Before 1800, direct birth estimates don't exist. Instead, we estimate births from population and birth rates:

$$\text{Total births} = \sum \text{population} \times \text{birth rate}$$

summed across every year of human history. 

The HYDE project provides gridded population maps and totals from 10,000 BC onward—millennial resolution to 1 AD, centennial thereafter (see their [2017 paper](https://essd.copernicus.org/articles/9/927/2017/essd-9-927-2017.html) for methodology). I use HYDE estimates directly for my medians. Between these years I assume constant exponential growth—reasonable given how slowly pre-modern populations changed. 

Estimating uncertainty is harder. HYDE provides ranges, but these become implausibly wide in the deep past—their lower bound for 10,000 BC is just 10,000 people. Other published estimates (see the [US Census compilation](https://www.census.gov/data/tables/time-series/demo/international-programs/historical-est-worldpop.html)) give a sense of scholarly opinion, but are themselves point estimates that don't capture plausible ranges.

To calibrate my uncertainty, I looked deeper into the early population estimates. Take 1 AD. A [Han Chinese census in 2 AD](https://www.cambridge.org/core/books/abs/cambridge-history-of-china/economic-and-social-history-of-former-han/2C38C79DC7D76BDA4A073CAE0572086C) records 59,594,978 people. This may be the best attested demographic figure in ancient history, even though we should suspect all but the first digit as false precision. The ancient Romans also took censuses, most importantly three under Augustus that counted 4.06 million in 28 BC, 4.23 million in 8 BC, and 4.94 million in 14 AD. Unfortunately, we are not exactly sure who was counted, creating so-called “high” and “low” counts for the population of Roman Italy which vary by more than a factor of two. Estimates for the empire as a whole in 1 AD are generally around 45–60 million (see [Scheidel 2007](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1096415) for an introduction to the debate, or [this ACOUP post](https://acoup.blog/2023/12/22/collections-how-many-people-ancient-demography/) for an accessible overview of historical demography).

That's at least 100 million between these two empires, already greater than the HYDE "low estimate" of 58 million for 1 AD. South Asian populations are poorly documented, but given later population comparisons and relative agricultural endowments, they were probably somewhat larger than China. Including Parthia, Southeast Asia, Mesoamerica, and sub-Saharan Africa, it is difficult to see how world population could be below 180 million. Populations above 300 million, however, also appear difficult without very high estimates outside of Rome and China. I set my 90% CI at 180M–300 (conveniently log-symmetric around HYDE's 232M) and applied similar reasoning at other benchmark years:

<table>
  <thead>
    <tr>
      <th rowspan="2">Year</th>
      <th colspan="2">HYDE 3.2</th>
      <th rowspan="2">Literature Range</th>
      <th rowspan="2">My 90% CI</th>
    </tr>
    <tr>
      <th>Estimate</th>
      <th>Range</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>10,000 BC</td><td>4.4</td><td>0.01–8.9</td><td>1–20</td><td>2.2–8.8</td></tr>
    <tr><td>5000 BC</td><td>19</td><td>2–36</td><td>5–20</td><td>12–29</td></tr>
    <tr><td>1 AD</td><td>232</td><td>58–406</td><td>170–330</td><td>180–300</td></tr>
    <tr><td>1000</td><td>323</td><td>176–568</td><td>253–345</td><td>260–410</td></tr>
    <tr><td>1700</td><td>592</td><td>444–740</td><td>410–680</td><td>510–690</td></tr>
    <tr><td>1800</td><td>943</td><td>802–1086</td><td>890–1000</td><td>860–1030</td></tr>
    <tr><td>1900</td><td>1643</td><td>1561–1725</td><td>1571–1710</td><td>1570–1720</td></tr>
    <tr><td>1950</td><td>2490</td><td>—</td><td>—</td><td>2450–2530</td></tr>
  </tbody>
</table>

*Note: All population figures are in millions.*

## Birth Rates and Life Expectancies

Pre-modern population growth was extremely slow. To steadily increase from 4.4 million in 10,000 BC to 232 million by 1 AD requires a growth rate of just 0.04% per year. Modern countries, by contrast, generally see population changes of 1% or more. So for most of human history, we can treat populations as approximately stationary. Since everyone dies exactly once, the crude birth rate is equal to the crude death rate and hence:

$$\text{Crude birth rate} = \frac{1}{\text{life expectancy}}$$

Unfortunately, [life expectancy estimates](https://ourworldindata.org/grapher/life-expectancy) are available only for the past century. Before that, we must rely on fragmentary documentary evidence and skeletal remains, both with substantial limitations. Still, the available evidence consistently suggests very low life expectancies. Roman Egypt offers the best ancient evidence: census papyri suggest life expectancy of 20–25 years, considered typical for classical antiquity ([Bagnall & Frier 1994](https://books.google.com/books/about/The_Demography_of_Roman_Egypt.html?id=ara8tHZRiLIC)). Similar estimates appear for medieval Europe (e.g. [Koepke 2021](https://pubmed.ncbi.nlm.nih.gov/34237609/)). Skeletal evidence points in the same direction: 24 years in medieval Japan ([Nagaoka 2006](https://pubmed.ncbi.nlm.nih.gov/16444727/)), 28 years in Neolithic Czechia ([Galeta 2015](https://www.jstor.org/stable/26292836)), and 20 years in 1100 CE Ohio ([Lovejoy et al. 1977](https://www.science.org/doi/10.1126/science.198.4314.291)). By 1800 the global average was about 29 years ([Riley 2005](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1728-4457.2005.00083.x)).

These low figures do not mean that everyone died in their twenties—as you can see from the stories on this site, many lived to old age. Life expectancy was low because infant mortality was extraordinarily high, with perhaps 50% of children dying before age five ([Roser 2019](https://ourworldindata.org/child-mortality-in-the-past)).

For agricultural populations, I assume a median life expectancy of 24 years, giving a crude birth rate of 42 per 1000. Almost no documented populations show life expectancy below 20 years over sustained periods, while estimates above 29 years are found only in contexts—like early-modern northwestern Europe or for wealthier individuals—that were plausibly above the historical average. I therefore use a 90% confidence interval of 20–29 years for life expectancy, which corresponds to birth rates of 35–50 per 1000.

This is where the PRB estimate diverges most sharply from mine. They assume life expectancies of 10–12 years for most of human history, implying birth rates of 80–100 per 1000—roughly double my estimates. Their only justification is a reference to "Iron Age France," but they provide no citation, and I cannot find any scholarly source documenting any stable population with a life expectancy this low. This assumption accounts for most of the difference between their 117 billion and my 66 billion.

## Paleolithic Births

Before 10,000 BC, I could find no global population estimates. I instead worked with Claude to synthesize genetic studies of effective population size, archaeological site densities, and ecological carrying capacity models, calibrated to match HYDE estimates at 10,000 BC. Useful sources included [Tallavaara *et al* 2015](https://pubmed.ncbi.nlm.nih.gov/26100880/)  for European populations, [Sjödin et al. 2012](https://pubmed.ncbi.nlm.nih.gov/22319141/) for effective population size in Africa, and [Gautney & Holliday, 2015](https://www.sciencedirect.com/science/article/abs/pii/S0305440315001211) for a rough estimate of world population at the Last Glacial Maximum. But the honest answer is that Claude mostly guessed populations for each continent, and the guesses looked broadly reasonable; perhaps, optimistically, within a factor of 2 of the correct answer. 

I use 200,000 BP as a convenient starting date. There was, of course, no first human, but 200,000 years ago is before the estimated dates for mitochondrial Eve and (probably) Y-chromosomal Adam, before the deepest splits in modern human populations, and before most evidence of behavioral modernity. Older anatomically modern remains have been found; the split with Neanderthals and Denisovans—anatomically distinct populations that nevertheless contributed a few percent to modern genomes—would take us back over half a million years. Any starting point is somewhat arbitrary; moving it back to 300,000 BP would add perhaps 1 billion births to the total.

For birth rates, I use ethnographic data from recent hunter-gatherer populations compiled by [Gurven & Kaplan (2007)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1728-4457.2007.00171.x). Their synthesis shows life expectancies of 21–37 years across foraging societies, with a central tendency around 30 years. I use this figure, implying a crude birth rate of 33 per 1000—lower than agricultural populations due to longer interbirth intervals, extended breastfeeding, and higher mobility.

## Final Answers

Putting everything together, here are my estimates for world population over time:

<table>
  <thead>
    <tr>
      <th rowspan="2">Year</th>
      <th rowspan="2">Population<br><span class="unit">(million)</span></th>
      <th rowspan="2">Crude birth rate<br><span class="unit">(per thousand)</span></th>
      <th colspan="2">Births in period<br><span class="unit">(billion)</span></th>
    </tr>
    <tr>
      <th>Median</th>
      <th>90% CI</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>200,000 BP</td><td>0.10</td><td>33</td><td>—</td><td>—</td></tr>
    <tr><td>10,000 BC</td><td>4.4</td><td>34</td><td>2.9</td><td>1.4–6.3</td></tr>
    <tr><td>3000 BC</td><td>45</td><td>40</td><td>4.0</td><td>2.5–6.3</td></tr>
    <tr><td>1000 BC</td><td>110</td><td>41</td><td>6.2</td><td>4.5–8.5</td></tr>
    <tr><td>500 AD</td><td>250</td><td>41</td><td>12.0</td><td>9.2–15.7</td></tr>
    <tr><td>1500</td><td>500</td><td>41</td><td>14.8</td><td>12.0–18.4</td></tr>
    <tr><td>1800</td><td>950</td><td>40</td><td>7.6</td><td>6.5–8.8</td></tr>
    <tr><td>1950</td><td>2490</td><td>36</td><td>8.65</td><td>8.21–9.11</td></tr>
    <tr><td>2026</td><td>8300</td><td>16</td><td>9.61</td><td>9.49–9.72</td></tr>
  </tbody>
  <tfoot>
    <tr><td colspan="3"><strong>Total</strong></td><td><strong>65.7</strong></td><td><strong>53.8–82.7</strong></td></tr>
  </tfoot>
</table>

The table shows slightly lower rates in earlier periods because hunter-gatherers—with their lower fertility—comprised a larger share of the population. By the Holocene, the rate rises toward 42 per thousand as agriculture dominates, then falls after 1800 as the demographic transition begins.

The largest uncertainties come from the period between 10,000 BC and 1800 AD, which accounts for roughly 70% of everyone who ever lived. After 1800, we have reasonably accurate birth records; before 10,000 BC, uncertainties are vast but the population was small enough that it barely affects the total. When combining estimates across periods, I assume perfect correlation—summing medians, summing 5th percentiles, summing 95th percentiles. This is crude, but errors in population and life expectancy estimates probably do correlate across periods.

Aside from a more accurate accounting, what else can we learn? The common complaint about "recency bias" in history is only somewhat justified on demographic grounds. Paleolithic hunter-gatherers represent 95% of human history by time, but only 5% of all people who ever lived—roughly as many as have been born since 2004. My 1997 birth places me later than 94% of all humans; my grandparents, only 85%.

The median person in human history was born around 1121 AD. This date advances by about 4 years each year as new births continue. The "Middle Ages," in other words, really are the middle—at least from our current vantage point.

About 15% of everyone who ever lived was born in the last 75 years---impressive for a timespan covering less than 0.04% of our species history. Nearly 13% of all humans who ever lived are alive right now. This is either extraordinary—you exist during the most populous moment in history—or utterly ordinary, since so does everyone you know.

