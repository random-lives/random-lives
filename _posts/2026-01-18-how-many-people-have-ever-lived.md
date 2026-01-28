---
layout: post
title: "How many people have ever lived?"
date: 2026-01-18
permalink: /blog/how-many-people-have-ever-lived/
---

# How many people have ever lived?

This is a difficult question to answer, because for almost all of human history there were no accurate censuses. Even today, counting people is hard. Papua New Guinea's 2024 census was their first in 24 years, with prior estimates ranging [from 10 million to 17 million](https://www.lowyinstitute.org/the-interpreter/png-needs-census-not-more-population-estimates); Afghanistan hasn't conducted one since 1979\. But such disputes are nothing compared to the uncertainty in pre-industrial populations—estimates for the world population in 10,000 BC range from 1 million to 20 million.

On the internet, a figure of 108 billion or 117 billion is usually, and uncritically, repeated. Both estimates come from a series of articles from the [Population Reference Bureau](https://www.prb.org/articles/how-many-people-have-ever-lived-on-earth/). When I tried to reproduce their methodology for this project, I found I couldn't—the pre-industrial life expectancy they assumed were far lower than any documented population over a sustained time period. My median estimate is **66 billion**, which is what I use when sampling lives. 

I've also provided a 90% confidence interval of 55–82 billion. This is admittedly crude—the product of rough estimates and rougher assumptions—but I think it's worth including anyway. Point estimates for questions like this invite false precision; a range honestly reflects how uncertain we are. Even with these uncertainties, though, my upper bound still falls well short of PRB's 117 billion. 

## Post-1800: Summing Estimated Births

Most countries today record births, which the UN collates globally. The United Nations World Population Prospects 2024 provides annual birth estimates from 1950 through 2023, with projections to 2100 (see the [OWID page](https://ourworldindata.org/births-and-deaths) for convenient data access). Summing through 2023 and adding extrapolations for 2024 and 2025 gives 9.61 billion births over that period. The UN doesn't provide uncertainty estimates, but these are probably below 1%.

[Gapminder](https://www.gapminder.org/data/) extends birth estimates back to 1800, adding another 8.65 billion. They don't include methodology documentation for this specific dataset, though they do provide [documentation for related population estimates](https://www.gapminder.org/data/documentation/gd003/). The results are broadly consistent with independent population and life expectancy estimates for the period—I would guess within 5% of the true count.

## Pre-1800: Estimating from Population

Before 1800, direct birth estimates don't exist. Instead, we estimate births from population and birth rates:  
   Total births \= \\sum population x birth rate  
summed across human history. 

The HYDE project provides gridded population maps and totals from 10,000 BC onward—millennial resolution to 1 AD, centennial thereafter (see their [2017 paper](https://essd.copernicus.org/articles/9/927/2017/essd-9-927-2017.html) for methodology). I use HYDE estimates directly for my medians.

Estimating uncertainty is harder. HYDE provides ranges, but these become implausibly wide in the deep past—their lower bound for 10,000 BC is just 10,000 people. Other published estimates (see the [US Census compilation](https://www.census.gov/data/tables/time-series/demo/international-programs/historical-est-worldpop.html)) give a sense of scholarly opinion, but are themselves point estimates that don't capture plausible ranges.

To calibrate my uncertainty, I looked deeper into the early population estimates. Take 1 AD. A [Han Chinese census in 2 AD](https://www.cambridge.org/core/books/abs/cambridge-history-of-china/economic-and-social-history-of-former-han/2C38C79DC7D76BDA4A073CAE0572086C) records 59,594,978 people. This may be the best attested demographic figure in ancient history, even though we should suspect all but the first digit as false precision. The ancient Romans also took censuses, most importantly three under Augustus that counted 4.06 million in 28 BC, 4.23 million in 8 BC, and 4.94 million in 14 AD. Unfortunately, we are not exactly sure who was counted, creating so-called “high” and “low” counts for the population of Roman Italy which vary by more than a factor of two. Estimates for the empire as a whole in 1 AD are generally around 45–60 million (see Scheidel 2007 for an introduction to the debate, or [this ACOUP post](https://acoup.blog/2023/12/22/collections-how-many-people-ancient-demography/) for an accessible overview of historical demography).

That's at least 100 million between these two empires, already greater than the HYDE "low estimate" of 58 million for 1 AD. South Asian populations are poorly documented, but given later population comparisons and relative agriculture endowments, they were probably somewhat larger than China. Including Parthia, Southeast Asia, Mesoamerica, and sub-Saharan Africa, it is difficult to see how world population could be below 180 million. Populations above 300 million, however, also appear difficult without very high estimates outside of Rome and China. I set my 90% CI at 180M–300M, log-symmetric around HYDE's 232M, and applied similar reasoning at other benchmark years: 

| Year | HYDE 3.2 Estimate | HYDE 3.2 Range | Literature Range | My 90% CI |
| :---- | :---- | :---- | :---- | :---- |
| 10,000 BC | 4.4 | 0.01–8.9 | 1–20 | 2.2–8.8 |
| 5000 BC | 19 | 2–36 | 5–20 | 12–29 |
| 1 AD | 232 | 58–406 | 170–330 | 180–300 |
| 1000 | 323 | 176–568 | 253–345 | 260–410 |
| 1700 | 592 | 444–740 | 410–680 | 510–690 |
| 1800 | 943 | 802–1086 | 890–1000 | 860–1030 |
| 1900 | 1643 | 1561–1725 | 1571–1710 | 1570–1720 |
| 1950 | 2490 | — | — | 2450–2530 |

Between benchmarks, I assume constant exponential growth—reasonable given how slowly pre-modern populations changed. Multiplying interpolated populations by birth rates (estimated below) and summing gives total births for each interval.

## Birth Rates and Life Expectancies

Pre-modern population growth was extremely slow. To steadily increase from 4.4 million in 10,000 BC to 232 million at 1 AD requires a growth rate of just 0.04% per year. Modern countries, by contrast, generally see population changes of 1% or more. So for most of human history, we can treat populations as approximately stationary, with crude birth rate equal to crude death rate and hence:  
   Crude birth rate \= 1 / life expectancy.

Unfortunately, [life expectancy estimates](https://ourworldindata.org/grapher/life-expectancy) are available only for the past century. Before that we rely on fragmentary documentary evidence and skeletal remains, both with substantial limitations. Still, the available evidence consistently suggests very low life expectancies. For the ancient world, Roman Egypt is best documented: scattered census papyri suggest life expectancy somewhere between 20–25 years, thought to be typical for the classical world (Bagnall & Frier 1994). Similar estimates appear in medieval demography (e.g. [Koepke 2021](https://pubmed.ncbi.nlm.nih.gov/34237609/)). Skeletal evidence points in the same direction: 24 years in medieval Japan ([Nagaoka 2006](https://pubmed.ncbi.nlm.nih.gov/16444727/)), 28 years in Neolithic Czechia ([Galeta 2015](https://www.jstor.org/stable/26292836)), and 20 years in 1100 CE Ohio ([Lovejoy et al. 1977](https://www.science.org/doi/10.1126/science.198.4314.291)). By 1800, ([Riley, 2005](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1728-4457.2005.00083.x)) estimates a global average of 29 years.

These low figures do not mean the average person died young—as you can see from the stories on this site, many lived to old age. Life expectancy was low because infant mortality was extraordinarily high, with perhaps 50% of children dying before age five ([Roser 2019](https://ourworldindata.org/child-mortality-in-the-past)).

For agricultural populations, I assume a median life expectancy of 24 years, giving a crude birth rate of 42 per 1000\. My 90% confidence interval of 20–29 years corresponds to birth rates of 35–50 per 1000\. The lower bound reflects that almost no documented populations show life expectancy below 20 years over sustained periods. The upper bound reflects that estimates above 29 years appear occasionally but often in contexts—like early-modern northwestern Europe or for wealthier individuals—that were plausibly above the historical average.

This is where the PRB estimate diverges most sharply from mine. They assume life expectancies of 10–12 years for most of human history, implying birth rates of 80–100 per 1000—roughly double my estimates. Their only justification is a reference to "Iron Age France," but they provide no citation, and I cannot find any scholarly source documenting any stable population with a life expectancy this low. This assumption accounts for most of the difference between their 117 billion and my 66 billion.

## Paleolithic Births

Before 10,000 BC I could find no global population estimates. I instead worked with Claude to synthesize genetic studies of effective population size, archaeological site densities, and ecological carrying capacity models, calibrated to match HYDE estimates at 10,000 BC. Useful sources included [Tallavaara *et al* 2015](https://pubmed.ncbi.nlm.nih.gov/26100880/)  for European populations, [Sjödin et al. 2012](https://pubmed.ncbi.nlm.nih.gov/22319141/) for effective population size in Africa, and [Gautney & Holliday, 2015](https://www.sciencedirect.com/science/article/abs/pii/S0305440315001211) for a rough estimate of world population at the Last Glacial Maximum. But the honest answer is that Claude mostly guessed populations for each continent, and the guesses looked broadly reasonable; perhaps optimistically within a factor of 2 of the correct answer.

For birth rates, I use ethnographic data from recent hunter-gatherer populations compiled by [Gurven & Kaplan (2007)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1728-4457.2007.00171.x). Their synthesis shows life expectancies of 21–37 years across foraging societies, with a central tendency around 30 years. I use this figure, implying a crude birth rate of 33 per 1000—lower than agricultural populations due to longer interbirth intervals, extended breastfeeding, and higher mobility.

## Final Answers

Putting everything together, here are my estimates for world population over time:

| Year | Population (M) | Crude Birth Rate | Births since Previous (B) |  |
| :---- | :---- | :---- | ----- | :---- |
|  |  |  | Median | 90% CI |
| 200,000 BC | 0.10 | 33 | — | — |
| 10,000 BC | 4.4 | 34 | 2.9 | 1.4–6.3 |
| 3000 BC | 45 | 40 | 4.0 | 2.5–6.3 |
| 1000 BC | 110 | 41 | 6.2 | 4.5–8.5 |
| 500 | 250 | 41 | 12.0 | 9.2–15.7 |
| 1500 | 500 | 41 | 14.8 | 12.0–18.4 |
| 1800 | 950 | 40 | 7.6 | 6.5–8.8 |
| 1950 | 2490 | 36 | 8.65 | 8.21–9.11 |
| 2026 | 8300 | 16 | 9.61 | 9.49–9.72 |
|  |  | **Total** | **65.7** | **53.8–82.7** |

The table below shows slightly lower rates in earlier periods because hunter-gatherers—with their lower fertility—comprised a larger share of the population. By the Holocene, the rate rises toward 42 as agriculture dominates, then falls after 1800 as the demographic transition begins.

The largest uncertainties come from the period between 10,000 BC and 1800 AD, which accounts for roughly 70% of everyone who ever lived. After 1800, we have reasonably accurate birth records; before 10,000 BC, uncertainties are vast but the population was small enough that it barely affects the total. When combining estimates across periods, I assume perfect correlation—summing medians, summing 5th percentiles, summing 95th percentiles. This is crude, but errors in population and life expectancy estimates probably do correlate across periods.

Let us finish with a few observations. The common complaint about "recency bias" in history is somewhat justified on demographic grounds—but perhaps not as much as you'd think. Paleolithic hunter-gatherers represent 95% of human history by time, but only about 5% of all people who ever lived. Still, the pre-modern era dominates: roughly 80% of all humans were born before 1800\.

Meanwhile, about 15% of everyone who ever lived was born in the last 75 years. And nearly 13% of all humans who ever lived are alive right now.

The median person in human history was born around 1121 AD—a date that's currently being pulled forward by about 4 years per year.