---
layout: post
title: "Who is the most famous person in history?"
date: 2026-03-17
permalink: /blog/most-famous-person/
published: false
---
Despite our obsession with fame, no one actually keeps track of who's famous. You'd think someone would have figured this out by now—at the very least to power a listicle perpetual motion machine—but global name-recognition surveys are rare. No one spends their time asking North Koreans or the North Sentinelese whether they are Swifties. The problem is worse if we want to determine the most famous person in all of human history, since unfortunately most people are long dead and beyond the reach of pollsters. 

I decided to try anyway. The plan: sample random people from across human history—with realistic birth years, birthplaces, and lifespans—and then ask an LLM how likely they were to have recognized any given historical figure. Average the results across many samples and we'll have an estimate of whether Michael Jackson or Alexander the Great is more famous.

Is this any good? It's hard to be sure without real polling data to compare to. But the individual judgments are mostly common sense: a woman born in rural Tamil Nadu in 1700 has almost certainly never heard of Shakespeare; a factory worker in 1980s Beijing almost certainly has heard of Mao. Modern reasoning models are pretty good at this kind of inference, and their responses look like reasonable educated guesses. I doubt *Nature* will accept my listicle but it's probably about as good as we'll ever get.

## Ground rules

Before we can get to the list, two questions: What is "fame"? And what is "person"?

By famous we mean basic name recognition at some point during their life. Even today, most people's knowledge of major figures is remarkably superficial:  [2019 Pew survey](https://www.pewresearch.org/religion/2019/07/23/what-americans-know-about-religion/) found that 53% of American Protestants couldn't identify Martin Luther as the person who inspired the Reformation. If this is the state of affairs in a literate country with universal education, historical "knowledge" was, for most people, extremely thin.

And by person we mean historical figure. No Hercules, no Rama, no Abraham, nor other mythological figure no matter how widely believed in. On the other hand scholars generally accept the historicity of Jesus or the Buddha. Recognition of such figures counts even if what people "knew" about them was mostly legend.

## And the most famous person is...

Probably the Buddha. By our calculation he would be recognised by 21.94±0.22% of all people who ever lived, or about 14 billion in total. But close behind is Jesus with 21.46±0.18% recognising him. These error bars are large enough that the Buddha only has a 95% of coming out on top. There are other sources of error that could swing this either way, but overall the Buddha is the most plausible candidate for top spot.

While the Buddha and Jesus are almost tied, they easily beat out the competition:

<table>
  <thead>
    <tr>
      <th rowspan="2">Rank</th>
      <th rowspan="2">Person</th>
      <th colspan="2">Recognition among</th>
      <th rowspan="2">Theoretical maximum</th>
      <th rowspan="2">Fraction of maximum achieved</th>
    </tr>
    <tr>
      <th>All people</th>
      <th>Living people</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>The Buddha</td><td>21.9%</td><td>66.1%</td><td>45.8%</td><td>48%</td></tr>
    <tr><td>2</td><td>Jesus of Nazareth</td><td>21.5%</td><td>85.7%</td><td>42.8%</td><td>50%</td></tr>
    <tr><td>3</td><td>Muhammad</td><td>17.9%</td><td>75.0%</td><td>38.2%</td><td>47%</td></tr>
    <tr><td>4</td><td>The Virgin Mary</td><td>17.2%</td><td>64.0%</td><td>42.8%</td><td>40%</td></tr>
    <tr><td>5</td><td>Adolf Hitler</td><td>14.2%</td><td>82.4%</td><td>17.4%</td><td>81%</td></tr>
    <tr><td>6</td><td>Confucius</td><td>12.9%</td><td>45.6%</td><td>45.8%</td><td>28%</td></tr>
    <tr><td>7</td><td>John the Baptist</td><td>12.8%</td><td>41.0%</td><td>42.8%</td><td>30%</td></tr>
    <tr><td>8</td><td>Albert Einstein</td><td>12.6%</td><td>79.1%</td><td>18.7%</td><td>67%</td></tr>
    <tr><td>9</td><td>St Joseph</td><td>12.5%</td><td>45.4%</td><td>42.8%</td><td>29%</td></tr>
    <tr><td>10</td><td>Genghis Khan</td><td>12.0%</td><td>51.8%</td><td>32.5%</td><td>37%</td></tr>
    <tr><td>11</td><td>Michael Jackson</td><td>11.9%</td><td>81.2%</td><td>15.1%</td><td>79%</td></tr>
    <tr><td>12</td><td>Gandhi</td><td>11.6%</td><td>68.2%</td><td>18.0%</td><td>64%</td></tr>
    <tr><td>13</td><td>Walt Disney</td><td>11.0%</td><td>71.7%</td><td>17.3%</td><td>64%</td></tr>
    <tr><td>14=</td><td>Queen Elizabeth II</td><td>10.8%</td><td>70.3%</td><td>16.6%</td><td>65%</td></tr>
    <tr><td>14=</td><td>Alexander the Great</td><td>10.8%</td><td>47.4%</td><td>45.1%</td><td>24%</td></tr>
    <tr><td>14=</td><td>Napoleon Bonaparte</td><td>10.8%</td><td>55.4%</td><td>22.6%</td><td>48%</td></tr>
  </tbody>
</table>

In the table we show both overall fame and fame among living people. Ancient figures have centuries of accumulated recognition behind them; modern figures have higher living recognition but a much shorter run. Almost half of all humans who ever lived could theoretically have heard of the Buddha: anyone born after he became famous who survived past infancy. Hitler's theoretical maximum is just 17.4%, but he's achieved 81% of it. The Buddha's is 45.8%, and half of that is enough to edge out Jesus.

In third place is Muhammad and fourth — and first woman — the Virgin Mary. John the Baptist (7th) and St Joseph (9th) also make the top ten. Like Jesus and Mary, these two saints are also significant figures in Islam, and so benefit from recognition by the world's two largest religions. Strictly Christian figures like St Peter and St Paul don't crack the top fifteen but plausibly make the top thirty; no secondary figure in any other religious tradition makes the top fifty.

Fifth is Hitler, the first non-religious figure on the list. As with all figures on this list, however, name recognition does not imply any deeper understanding. In India, where the Holocaust is not taught in schools, "Hitler" is a colloquial word for a strict disciplinarian; the name has been used for [ice cream brands, clothing stores, and a TV show without controversy](https://www.thedailybeast.com/hitler-the-ben-and-jerrys-of-india/).

Sixth is Confucius, completing the most famous religious founders. No Hindu figure appears on this list, and nor do the major Old Testament figures: Rama, Krishna, Abraham, and Moses are all mythological and excluded by our ground rules, though undoubtedly widely recognised characters. 

Rounding out the top ten are Einstein, Genghis Khan, and Michael Jackson. Jackson might seem an unlikely peer, but *Thriller* achieved a unmatched cross-cultural penetration across the developing world. Gandhi is twelfth, Walt Disney thirteenth, assisted by the fame of the Disney corporation that he founded. Tied for fourteenth are Queen Elizabeth II, Alexander the Great, and Napoleon. Alexander is another curious case: famous throughout the [Alexander Romance ](https://www.astralcodexten.com/p/book-review-the-alexander-romance),  he even makes an appearance in the Quran as [Dhu al-Qarnayn](https://en.wikipedia.org/wiki/Dhu_al-Qarnayn).

## The most famous today

If we only consider fame among people alive today, the picture shifts:

<table>
  <thead>
    <tr>
      <th rowspan="2">Rank</th>
      <th rowspan="2">Person</th>
      <th colspan="2">Recognition among</th>
    </tr>
    <tr>
      <th>Living people</th>
      <th>All people</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Jesus of Nazareth</td><td>85.7%</td><td>21.5%</td></tr>
    <tr><td>2</td><td>Adolf Hitler</td><td>82.4%</td><td>14.2%</td></tr>
    <tr><td>3</td><td>Michael Jackson</td><td>81.2%</td><td>11.9%</td></tr>
    <tr><td>4</td><td>Cristiano Ronaldo</td><td>80.5%</td><td>10.4%</td></tr>
    <tr><td>5</td><td>Lionel Messi</td><td>79.3%</td><td>10.3%</td></tr>
    <tr><td>6</td><td>Albert Einstein</td><td>79.1%</td><td>12.6%</td></tr>
    <tr><td>7</td><td>Osama Bin Laden</td><td>76.5%</td><td>10.7%</td></tr>
    <tr><td>8</td><td>Muhammad</td><td>75.0%</td><td>17.9%</td></tr>
    <tr><td>9</td><td>Donald Trump</td><td>74.3%</td><td>9.5%</td></tr>
    <tr><td>10</td><td>Vladimir Putin</td><td>73.9%</td><td>10.1%</td></tr>
    <tr><td>11</td><td>Barack Obama</td><td>73.5%</td><td>9.8%</td></tr>
    <tr><td>12</td><td>Jackie Chan</td><td>73.3%</td><td>10.7%</td></tr>
    <tr><td>13</td><td>Walt Disney</td><td>71.7%</td><td>11.0%</td></tr>
    <tr><td>14</td><td>Queen Elizabeth II</td><td>70.3%</td><td>10.8%</td></tr>
    <tr><td>15</td><td>Bill Gates</td><td>69.0%</td><td>9.5%</td></tr>
  </tbody>
</table>

Jesus now comfortably comes out on top. The Buddha, by contrast, drops out of the top fifteen entirely, as do all other religious figures except Muhammad, now 8th. Hitler and Michael Jackson rise to second and third place.

New entrants Ronaldo and Messi at fourth and fifth reflect football's global reach. Osama Bin Laden makes it to 7th place, while Donald Trump, Vladimir Putin, and Barack Obama are close behind and within sampling error of each other. For Trump and Putin we have some independent validation: reanalyzing the [2025 Gallup International End of Year survey](https://www.gallup-international.com/survey-results-and-news/survey-result/the-latest-findings-from-the-worlds-longest-running-global-public-opinion-study) across 61 countries— using "don't know" responses as a proxy for non-recognition, extending to non-surveyed countries, and weighting for children—I estimate that they are recognized by 71% and 69% of all living humans. This is one of the few places we can check the LLM's estimates against real data; reassuringly they aren't too far off.

## Most famous women in history

Only two women crack the overall top fifteen: the Virgin Mary, whose fame is largely derivative of her son's, and Queen Elizabeth II, who inherited hers. Here are the top 10:


<table>
  <thead>
    <tr>
      <th rowspan="2">Rank</th>
      <th rowspan="2">Person</th>
      <th colspan="2">Recognition among</th>
      <th rowspan="2">Theoretical maximum</th>
      <th rowspan="2">Fraction of maximum achieved</th>
    </tr>
    <tr>
      <th>All people</th>
      <th>Living people</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>The Virgin Mary</td><td>17.2%</td><td>64.0%</td><td>42.8%</td><td>40%</td></tr>
    <tr><td>2</td><td>Queen Elizabeth II</td><td>10.8%</td><td>70.3%</td><td>16.6%</td><td>65%</td></tr>
    <tr><td>3</td><td>Princess Diana</td><td>10.0%</td><td>67.5%</td><td>15.1%</td><td>66%</td></tr>
    <tr><td>4</td><td>Mary Magdalene</td><td>9.1%</td><td>34.1%</td><td>42.8%</td><td>21%</td></tr>
    <tr><td>5</td><td>Mother Teresa</td><td>8.5%</td><td>57.3%</td><td>15.7%</td><td>54%</td></tr>
    <tr><td>6</td><td>J K Rowling</td><td>8.3%</td><td>62.6%</td><td>14.2%</td><td>59%</td></tr>
    <tr><td>7</td><td>Queen Victoria</td><td>7.9%</td><td>40.1%</td><td>21.3%</td><td>37%</td></tr>
    <tr><td>8=</td><td>Taylor Swift</td><td>7.5%</td><td>60.3%</td><td>13.4%</td><td>56%</td></tr>
    <tr><td>8=</td><td>Cleopatra</td><td>7.5%</td><td>42.9%</td><td>43.4%</td><td>17%</td></tr>
    <tr><td>10</td><td>Madonna</td><td>7.3%</td><td>50.5%</td><td>15.0%</td><td>49%</td></tr>
  </tbody>
</table>

The estimates here are small enough that the ordering is not robust, and I'm not entirely sure I've captured all the most plausible candidates. But the broad pattern—that there are far more famous men than women—is clear. Even Mother Teresa, who appears fifth here, was only 53rd overall among all people I tested, sitting between George W. Bush and Ali ibn Abi Talib.

## Methodology

The estimates in this post combine a deterministic demographic model with LLM-based recognition estimates.

The first step is to generate 100,000 sample lives using the same pipeline as the [rest of this project](https://random-lives.github.io/random-lives/about): the [HYDE database](https://landuse.sites.uu.nl/hyde-project/) for population density by place and time, combined with period- and region-appropriate life tables, to produce a birth year, birthplace, sex, and age at death for each sampled life. No LLM is involved at this stage.

Before querying the model, I filter out lives that couldn't plausibly recognize anyone: those born before 500 BC, those born before 1500 in the Americas (essentially no contact with Old World figures), and those who died before age 5 or are currently alive and under 5. I also only ask about historical figures who became famous before the person died. The "ceiling" for each figure is simply the fraction of the 100,000 sampled lives that pass all these filters — the maximum possible recognition rate.

Querying the LLM for all 100,000 lives would be prohibitively expensive, so I use stratified sampling. I bucket the 100,000 lives into groups with similar expected recognition patterns — for instance, people in India born between 600 and 1100 AD — and sample roughly a dozen lives from each bucket to actually query. For each sampled life, the LLM estimates the probability that a person of that sex, born in that place and year, dying at that age, would at some point have recognized a given historical figure. The results are then weighted back to the full population using the stratification weights.

The 1,841 queried lives come from combining several runs with different bucketing strategies: an initial test of ~50, then runs of ~500 and ~800 using stratified sampling, plus an additional ~500 drawn purely at random. All are combined with appropriate weighting. The standard errors in the full table reflect the stratified design.

### Sources of error

There are three main sources of error, in roughly increasing order of importance.

**Stochastic sampling error** is the easiest to quantify and the smallest. With 1,841 stratified samples, the standard error on a figure recognized by ~20% of people is about 0.2 percentage points — small enough that the top 5 ordering is stable across runs. This is the "±1 SE" column in the full table below.

**LLM estimation error** is harder to quantify. The model is estimating, for each sampled life, the probability that a specific person in a specific time and place would have heard of a given figure. Having reviewed many of the model's reasoning traces, I find them generally sensible — there are no obvious anachronisms or hallucinations. The model clearly understands, for instance, that an Indian woman in 1800 would not have heard of Shakespeare. One could postulate a systematic bias upward for figures prominent in English-language sources, but one could equally postulate a downward bias for figures whose fame was transmitted orally. It's genuinely unclear which direction any systematic error would go, and I'd roughly characterize the model as doing a pretty good educated guess. For the top religious figures, where the logic is straightforward — "essentially all Buddhists have heard of the Buddha" — this error is probably small. For figures like Michael Jackson or Cristiano Ronaldo, the model is doing more guesswork.

**Demographic uncertainty** is potentially the most consequential for the top of the list. The population estimates from the HYDE database and the life expectancy assumptions I use are uncertain, as discussed in the [previous blog post](https://random-lives.github.io/random-lives/blog/how-many-people-have-ever-lived/). If historical populations were higher than I've estimated — say, if world population in 1000 AD was larger than HYDE suggests — then figures known primarily through historical accumulation (like the Buddha) would become more famous relative to modern figures. Conversely, lower historical populations would boost modern figures. I don't think this uncertainty is large enough to change the top 5, but the relative ranking of Jesus and the Buddha is potentially quite sensitive to it, because Jesus is simply more widely known today while the Buddha's lead comes from historical depth. The relative population of India and China also matters enormously for how famous the Buddha is compared to anyone else.

### The full table

Here are all 54 figures I tested, with the full set of estimates.

| Rank | Name | Year | Frac | ±1 SE | Ceil | %Ceil | Alive | ±1 SE |
|------|------|------|------|-------|------|-------|-------|-------|
| 1 | Buddha | −450 | 21.90% | 0.22% | 45.80% | 48% | 66.10% | 0.65% |
| 2 | Jesus of Nazareth | 30 | 21.80% | 0.20% | 42.80% | 51% | 87.70% | 0.50% |
| 3 | Muhammad | 620 | 17.90% | 0.22% | 38.20% | 47% | 75.00% | 0.76% |
| 4 | The Virgin Mary | 30 | 17.20% | 0.21% | 42.80% | 40% | 64.00% | 0.79% |
| 5 | Adolf Hitler | 1933 | 14.20% | 0.12% | 17.40% | 81% | 82.80% | 0.61% |
| 6 | Confucius | −450 | 12.90% | 0.14% | 45.80% | 28% | 45.60% | 0.70% |
| 7 | Albert Einstein | 1905 | 12.70% | 0.11% | 18.70% | 68% | 80.30% | 0.61% |
| 8 | Genghis Khan | 1200 | 12.00% | 0.16% | 32.50% | 37% | 51.80% | 0.70% |
| 9 | Michael Jackson | 1982 | 12.00% | 0.15% | 15.10% | 79% | 82.00% | 0.72% |
| 10 | Gandhi | 1920 | 11.60% | 0.12% | 18.00% | 64% | 68.20% | 0.68% |
| 11 | Queen Elizabeth II | 1952 | 10.80% | 0.12% | 16.60% | 65% | 70.30% | 0.70% |
| 12 | Alexander the Great | −330 | 10.80% | 0.18% | 45.10% | 24% | 47.40% | 0.78% |
| 13 | Napoleon Bonaparte | 1799 | 10.70% | 0.14% | 22.60% | 48% | 54.60% | 0.80% |
| 14 | Cristiano Ronaldo | 2003 | 10.50% | 0.13% | 13.80% | 76% | 80.50% | 0.64% |
| 15 | Lionel Messi | 2005 | 10.30% | 0.16% | 13.60% | 76% | 79.30% | 0.84% |
| 16 | Judas Iscariot | 30 | 10.30% | 0.15% | 42.80% | 24% | 40.70% | 0.79% |
| 17 | Saint Paul | 50 | 10.30% | 0.16% | 42.70% | 24% | 36.20% | 0.77% |
| 18 | Princess Diana | 1981 | 10.00% | 0.20% | 15.10% | 66% | 67.50% | 1.21% |
| 19 | Saint Peter | 50 | 9.90% | 0.16% | 42.70% | 23% | 34.90% | 0.76% |
| 20 | Barack Obama | 2008 | 9.90% | 0.13% | 13.40% | 74% | 73.80% | 0.72% |
| 21 | Christopher Columbus | 1492 | 9.90% | 0.12% | 28.50% | 35% | 54.40% | 0.76% |
| 22 | Stalin | 1924 | 9.80% | 0.13% | 17.90% | 55% | 54.00% | 0.77% |
| 23 | Donald Trump | 2015 | 9.50% | 0.13% | 12.90% | 74% | 74.30% | 0.66% |
| 24 | Mao Zedong | 1935 | 9.50% | 0.12% | 17.30% | 55% | 55.10% | 0.73% |
| 25 | Nelson Mandela | 1962 | 9.50% | 0.18% | 16.10% | 59% | 64.20% | 1.22% |
| 26 | Isaac Newton | 1687 | 9.30% | 0.12% | 25.10% | 37% | 57.30% | 0.80% |
| 27 | Mary Magdalene | 30 | 9.10% | 0.14% | 42.80% | 21% | 34.10% | 0.71% |
| 28 | Muhammad Ali | 1964 | 9.00% | 0.21% | 16.00% | 56% | 60.30% | 1.29% |
| 29 | Charles Darwin | 1859 | 9.00% | 0.12% | 20.60% | 44% | 55.90% | 0.80% |
| 30 | Julius Caesar | −50 | 9.00% | 0.14% | 43.40% | 21% | 47.00% | 0.75% |
| 31 | Karl Marx | 1848 | 8.70% | 0.12% | 21.00% | 42% | 49.80% | 0.75% |
| 32 | Leonardo da Vinci | 1490 | 8.60% | 0.12% | 28.50% | 30% | 53.80% | 0.83% |
| 33 | Mother Teresa | 1970 | 8.50% | 0.13% | 15.70% | 54% | 57.30% | 0.86% |
| 34 | Ali ibn Abi Talib | 640 | 8.40% | 0.19% | 38.10% | 22% | 35.10% | 0.88% |
| 35 | Lenin | 1917 | 8.40% | 0.28% | 18.20% | 46% | 47.20% | 1.70% |
| 36 | Qin Shi Huang | −220 | 8.30% | 0.12% | 44.50% | 19% | 31.30% | 0.53% |
| 37 | William Shakespeare | 1590 | 8.10% | 0.12% | 26.90% | 30% | 48.90% | 0.84% |
| 38 | Queen Victoria | 1837 | 7.90% | 0.11% | 21.30% | 37% | 40.10% | 0.70% |
| 39 | George Washington | 1775 | 7.60% | 0.11% | 23.30% | 33% | 46.20% | 0.75% |
| 40 | Cleopatra | −50 | 7.50% | 0.12% | 43.40% | 17% | 42.80% | 0.74% |
| 41 | Taylor Swift | 2008 | 7.50% | 0.12% | 13.40% | 56% | 59.60% | 0.84% |
| 42 | Guan Yu | 220 | 7.40% | 0.17% | 41.40% | 18% | 22.40% | 0.64% |
| 43 | Marie Curie | 1903 | 6.90% | 0.16% | 18.80% | 37% | 42.80% | 1.12% |
| 44 | Aisha | 640 | 6.90% | 0.17% | 38.10% | 18% | 30.20% | 0.83% |
| 45 | Mencius | −300 | 6.80% | 0.11% | 44.90% | 15% | 23.20% | 0.42% |
| 46 | Fatimah | 640 | 6.70% | 0.17% | 38.10% | 17% | 28.70% | 0.83% |
| 47 | Aristotle | −340 | 6.60% | 0.11% | 45.20% | 15% | 37.00% | 0.71% |
| 48 | Indira Gandhi | 1966 | 6.50% | 0.11% | 15.90% | 41% | 41.20% | 0.65% |
| 49 | Martin Luther | 1517 | 5.90% | 0.16% | 28.10% | 21% | 31.40% | 0.94% |
| 50 | Kublai Khan | 1260 | 5.80% | 0.22% | 31.70% | 18% | 26.70% | 1.06% |
| 51 | Joan of Arc | 1430 | 5.60% | 0.10% | 29.30% | 19% | 31.10% | 0.69% |
| 52 | Khadija | 620 | 5.30% | 0.36% | 38.20% | 14% | 26.60% | 1.74% |
| 53 | Akbar | 1556 | 4.90% | 0.17% | 27.50% | 18% | 26.20% | 0.71% |
| 54 | Wu Zetian | 690 | 3.60% | 0.13% | 37.60% | 9% | 16.70% | 0.60% |

Below about rank 15, the ordering is not robust — many figures are separated by less than a standard error, and the LLM's estimation uncertainty is likely larger than the stochastic noise. The reader should treat the broad tiers as meaningful but not the precise ordering within them.

### Who's missing?

I tested 54 figures, chosen based on my own judgment about who might plausibly rank highly. This inevitably means I missed some — but the data itself helps us bound how much this matters.

The most obvious gap is **secondary New Testament figures**. Characters like Joseph, John the Baptist, Herod, and Pontius Pilate are known to essentially all Christians and would have similar recognition patterns to the secondary figures I did test — Judas (10.3%), Saint Paul (10.3%), Saint Peter (9.9%), and Mary Magdalene (9.1%). Several untested New Testament figures could plausibly score in the 9–11% range, which would place them in the top 20. Old Testament figures like King David and Solomon, while also widely known, fall into the same legendary/non-historical category as Abraham and Moses and are excluded by the ground rules above. This is the category most likely to contain figures I should have tested.

By contrast, additional **early Islamic figures** are unlikely to rank as highly. Ali ibn Abi Talib — the most important strictly Islamic figure after Muhammad — scores only 8.4%, and Aisha, Fatimah, and Khadija score progressively lower. Figures like Abu Bakr and Umar, while central to Islamic history, would almost certainly fall below Ali. It seems unlikely that any additional Islamic figure besides Muhammad himself would crack the top 30.

Similarly, I don't see obvious gaps in the **Buddhist or Confucian traditions**. Buddhism, while a major world religion, does not have secondary figures who are as universally familiar to lay adherents as, say, Saint Peter is to Christians. And I tested Mencius — probably the second most famous Confucian — at 6.8%, well below the top 30.

For **modern political figures**, Winston Churchill is probably the most notable omission. I'd expect him to score similarly to Stalin (9.8%) or Mao (9.5%) — famous, but probably not in the top 20. Other untested modern leaders can be bounded using the same Gallup International reanalysis used to validate the Trump estimate: Putin has roughly 69% global name recognition today, Xi Jinping 66%, and Modi 57%. Putin's numbers suggest he'd score around 9–10% all-time — comparable to Stalin or Mao — while Modi and Xi would fall lower still. None of them would crack the top 20.

I'm fairly confident there are no **Hindu, Sikh, Jain, or Southeast Asian Buddhist figures** who would break into the top 30. None of these traditions has a single secondary figure with anything close to the global reach of the figures already tested.

(Also missing, popes, other presidents, Musk)

If you think I've missed someone important, I'd be glad to hear about it.
