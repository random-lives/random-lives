---
layout: post
title: "Who is the most famous person in history?"
date: 2026-03-17
permalink: /blog/most-famous-person/
published: true
---
Despite our obsession with fame, no one actually keeps track of who's famous. You'd think someone would have figured this out by now—at the very least to power a listicle perpetual motion machine—but global name-recognition surveys are rare. No one spends their time asking North Koreans or the North Sentinelese whether they are Swifties. The problem is worse if we want to determine the most famous person in all of human history, since unfortunately most people are long dead and beyond the reach of pollsters. 

I decided to try anyway. The plan: sample random people from across human history—with realistic birth years, birthplaces, and lifespans—and then ask an LLM how likely they were to have recognized any given historical figure. Average the results across many samples and we'll have an estimate of whether Michael Jackson or Alexander the Great is more famous.

Is this any good? It's hard to be sure without real polling data to compare to. But the individual judgments are mostly common sense: a woman born in rural Tamil Nadu in 1700 has almost certainly never heard of Shakespeare; a factory worker in 1980s Beijing almost certainly has heard of Mao. Modern reasoning models are pretty good at this kind of inference, and their responses look like reasonable educated guesses. I doubt *Nature* will accept my listicle but it's probably about as good as we'll ever get.

## Ground rules

Before we can get to the list, two questions: What is "fame"? And what is "person"?

By famous we mean basic name recognition at some point during their life. Even today, most people's knowledge of major figures is remarkably superficial: a [2019 Pew survey](https://www.pewresearch.org/religion/2019/07/23/what-americans-know-about-religion/) found that 53% of American Protestants couldn't identify Martin Luther as the person who inspired the Reformation. If this is the state of affairs in a literate country with universal education, historical "knowledge" was, for most people, extremely thin.

And by person we mean historical figure. No Hercules, no Rama, no Abraham, nor other mythological figure no matter how widely believed in. On the other hand scholars generally accept the historicity of Jesus or the Buddha. Recognition of such figures counts even if what people "knew" about them was mostly legend.

## And the most famous person is...

Probably the Buddha. By our calculation he would be recognised by 21.94±0.22% of all people who ever lived, or about 14 billion in total. But close behind is Jesus with 21.46±0.18% recognising him. These error bars are large enough that the Buddha only has a 95% chance of coming out on top. There are other sources of error that could swing this either way, but overall the Buddha is the most plausible candidate for top spot.

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

In the table we show both overall fame and fame among living people. Ancient figures have centuries of accumulated recognition behind them; modern figures have higher living recognition but a much shorter run. The Buddha's theoretical maximum is 45.8%—nearly half of all humans who ever lived. Hitler's is just 17.4%, but he's achieved 81% of it. Half of the Buddha's ceiling is enough to edge out Jesus.

In third place is Muhammad and fourth—and first woman—the Virgin Mary. John the Baptist (7th) and St Joseph (9th) also make the top ten. Like Jesus and Mary, these two saints are also significant figures in Islam, and so benefit from recognition by the world's two largest religions. Strictly Christian figures like St Peter and St Paul don't crack the top fifteen but plausibly make the top thirty; no secondary figure in any other religious tradition makes the top fifty.

Fifth is Hitler, the first non-religious figure on the list. As with all figures on this list, however, name recognition does not imply any deeper understanding. In India, where the Holocaust is not taught in schools, "Hitler" is a colloquial word for a strict disciplinarian; the name has been used for [ice cream brands, clothing stores, and a TV show without controversy](https://www.thedailybeast.com/hitler-the-ben-and-jerrys-of-india/).

Sixth is Confucius, completing the most famous religious founders. No Hindu or major Old Testament figure appears on this list—their most prominent candidates are all mythological, and excluded by our ground rules.

Rounding out the top ten are Einstein, Genghis Khan, and Michael Jackson. Jackson is perhaps the most surprising entry, but *Thriller* achieved an unmatched cross-cultural penetration across the developing world. Gandhi is twelfth, Walt Disney thirteenth, assisted by the fame of the Disney corporation that he founded. Tied for fourteenth are Queen Elizabeth II, Alexander the Great, and Napoleon. Alexander is another curious case: famous throughout the [Alexander Romance](https://www.astralcodexten.com/p/book-review-the-alexander-romance), he even makes an appearance in the Quran as [Dhu al-Qarnayn](https://en.wikipedia.org/wiki/Dhu_al-Qarnayn).

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

Jesus now comfortably comes out on top. The Buddha, by contrast, drops out of the top fifteen entirely, as do all other religious figures except Muhammad (now 8th). Hitler and Michael Jackson rise to second and third place.

New entrants Ronaldo and Messi at fourth and fifth reflect football's global reach. Osama Bin Laden makes it to 7th place, while Donald Trump, Vladimir Putin, and Barack Obama are close behind and within sampling error of each other. For Trump and Putin we have some independent validation: reanalyzing the [2025 Gallup International End of Year survey](https://www.gallup-international.com/survey-results-and-news/survey-result/the-latest-findings-from-the-worlds-longest-running-global-public-opinion-study) across 61 countries— using "don't know" responses as a proxy for non-recognition, extending to non-surveyed countries, and weighting for children—I estimate that they are recognized by 71% and 69% of all living humans. This is one of the few places we can check the LLM's estimates against real data; reassuringly they aren't too far off.

## The most famous women in history

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

The estimates here are small enough that the ordering is not robust, and I'm not entirely sure I've captured all the plausible candidates. But the broad pattern—that there are far more famous men than women—is clear. Even Mother Teresa, who appears fifth here, was only 53rd overall among all people I tested, sitting between George W. Bush and Ali ibn Abi Talib.

## Methodology

The estimates in this post combine a deterministic demographic model with LLM-based recognition estimates.

The first step is to generate 100,000 sample lives using the same pipeline as the [rest of this project](https://random-lives.github.io/random-lives/about): the [HYDE database](https://landuse.sites.uu.nl/hyde-project/) for population density by place and time, combined with period- and region-appropriate life tables, to produce a birth year, birthplace, sex, and age at death for each sampled life. No LLM is involved at this stage.

Before querying the model, I filter out lives that couldn't plausibly recognize anyone: those born before 500 BC, those born before 1500 in the Americas (essentially no contact with Old World figures), and those who died before age 5 or are currently alive and under 5. I also only ask about historical figures who became famous before the person died. The "theoretical maximum" for each figure is simply the fraction of the 100,000 sampled lives that pass all these filters—the maximum possible recognition rate.

Querying GPT-5.2 for all 100,000 lives would be prohibitively expensive, so I use stratified sampling. I bucket the 100,000 lives into groups with similar expected recognition patterns—for instance, people in India born between 1 and 600 AD—and sample within each bucket to actually query. For each sampled life, the LLM estimates the probability that a person of that sex, born in that place and year, dying at that age, would at some point have recognized a given historical figure. The results are then weighted back to the full population using the stratification weights. In total I queried 2,355 people, though not every famous figure was included in every query. 

### Full results

Here are all 93 figures I tested. Below about rank 15, many figures are separated by less than a standard error, so the broad tiers are meaningful but the precise ordering within them is not.

<details>
<summary>Click to expand full table (click column headers to sort)</summary>

<table id="full-table">
  <thead>
    <tr>
      <th rowspan="2">Rank</th>
      <th rowspan="2">Person</th>
      <th colspan="2">Recognition among</th>
      <th rowspan="2" class="sortable" data-col="4">Theoretical maximum</th>
      <th rowspan="2" class="sortable" data-col="5">Fraction of maximum achieved</th>
    </tr>
    <tr>
      <th class="sortable" data-col="2">All people (%)</th>
      <th class="sortable" data-col="3">Living people (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Buddha</td><td>21.94 ± 0.22</td><td>66.1 ± 0.7</td><td>46</td><td>48</td></tr>
    <tr><td>2</td><td>Jesus of Nazareth</td><td>21.46 ± 0.18</td><td>85.7 ± 0.5</td><td>43</td><td>50</td></tr>
    <tr><td>3</td><td>Muhammad</td><td>17.95 ± 0.22</td><td>75.0 ± 0.8</td><td>38</td><td>47</td></tr>
    <tr><td>4</td><td>The Virgin Mary</td><td>17.15 ± 0.21</td><td>64.0 ± 0.8</td><td>43</td><td>40</td></tr>
    <tr><td>5</td><td>Adolf Hitler</td><td>14.16 ± 0.11</td><td>82.4 ± 0.6</td><td>17</td><td>81</td></tr>
    <tr><td>6</td><td>Confucius</td><td>12.90 ± 0.14</td><td>45.6 ± 0.7</td><td>46</td><td>28</td></tr>
    <tr><td>7</td><td>John the Baptist</td><td>12.79 ± 0.36</td><td>41.0 ± 1.4</td><td>43</td><td>30</td></tr>
    <tr><td>8</td><td>Albert Einstein</td><td>12.60 ± 0.10</td><td>79.1 ± 0.6</td><td>19</td><td>67</td></tr>
    <tr><td>9</td><td>St Joseph</td><td>12.50 ± 0.33</td><td>45.4 ± 1.3</td><td>43</td><td>29</td></tr>
    <tr><td>10</td><td>Genghis Khan</td><td>12.02 ± 0.16</td><td>51.8 ± 0.7</td><td>33</td><td>37</td></tr>
    <tr><td>11</td><td>Michael Jackson</td><td>11.86 ± 0.13</td><td>81.2 ± 0.7</td><td>15</td><td>79</td></tr>
    <tr><td>12</td><td>Gandhi</td><td>11.57 ± 0.12</td><td>68.2 ± 0.7</td><td>18</td><td>64</td></tr>
    <tr><td>13</td><td>Walt Disney</td><td>11.04 ± 0.21</td><td>71.7 ± 1.3</td><td>17</td><td>64</td></tr>
    <tr><td>14</td><td>Queen Elizabeth II</td><td>10.81 ± 0.12</td><td>70.3 ± 0.7</td><td>17</td><td>65</td></tr>
    <tr><td>15</td><td>Alexander the Great</td><td>10.78 ± 0.18</td><td>47.4 ± 0.8</td><td>45</td><td>24</td></tr>
    <tr><td>16</td><td>Napoleon Bonaparte</td><td>10.76 ± 0.13</td><td>55.4 ± 0.7</td><td>23</td><td>48</td></tr>
    <tr><td>17</td><td>Osama Bin Laden</td><td>10.73 ± 0.32</td><td>76.5 ± 1.9</td><td>14</td><td>77</td></tr>
    <tr><td>18</td><td>Jackie Chan</td><td>10.67 ± 0.25</td><td>73.3 ± 1.5</td><td>15</td><td>70</td></tr>
    <tr><td>19</td><td>Cristiano Ronaldo</td><td>10.45 ± 0.12</td><td>80.5 ± 0.6</td><td>14</td><td>76</td></tr>
    <tr><td>20</td><td>Winston Churchill</td><td>10.36 ± 0.25</td><td>58.2 ± 1.6</td><td>17</td><td>60</td></tr>
    <tr><td>21</td><td>Lionel Messi</td><td>10.35 ± 0.16</td><td>79.3 ± 0.8</td><td>14</td><td>76</td></tr>
    <tr><td>22</td><td>Judas Iscariot</td><td>10.31 ± 0.15</td><td>40.7 ± 0.8</td><td>43</td><td>24</td></tr>
    <tr><td>23</td><td>Saint Paul</td><td>10.27 ± 0.16</td><td>36.2 ± 0.8</td><td>43</td><td>24</td></tr>
    <tr><td>24</td><td>Bruce Lee</td><td>10.22 ± 0.26</td><td>66.4 ± 1.5</td><td>16</td><td>65</td></tr>
    <tr><td>25</td><td>Vladimir Putin</td><td>10.15 ± 0.25</td><td>73.9 ± 1.3</td><td>14</td><td>72</td></tr>
    <tr><td>26</td><td>Stalin</td><td>10.10 ± 0.12</td><td>55.8 ± 0.7</td><td>18</td><td>57</td></tr>
    <tr><td>27</td><td>Princess Diana</td><td>10.01 ± 0.20</td><td>67.5 ± 1.2</td><td>15</td><td>66</td></tr>
    <tr><td>28</td><td>Saint Peter</td><td>9.93 ± 0.16</td><td>34.9 ± 0.8</td><td>43</td><td>23</td></tr>
    <tr><td>29</td><td>Christopher Columbus</td><td>9.87 ± 0.12</td><td>54.4 ± 0.8</td><td>28</td><td>35</td></tr>
    <tr><td>30</td><td>Barack Obama</td><td>9.79 ± 0.12</td><td>73.5 ± 0.7</td><td>13</td><td>73</td></tr>
    <tr><td>31</td><td>Thomas Edison</td><td>9.79 ± 0.22</td><td>56.7 ± 1.5</td><td>20</td><td>50</td></tr>
    <tr><td>32</td><td>Neil Armstrong</td><td>9.61 ± 0.25</td><td>60.2 ± 1.5</td><td>16</td><td>61</td></tr>
    <tr><td>33</td><td>Saddam Hussein</td><td>9.59 ± 0.29</td><td>64.8 ± 1.9</td><td>15</td><td>66</td></tr>
    <tr><td>34</td><td>Donald Trump</td><td>9.50 ± 0.13</td><td>74.3 ± 0.7</td><td>13</td><td>74</td></tr>
    <tr><td>35</td><td>Mao Zedong</td><td>9.48 ± 0.12</td><td>55.1 ± 0.7</td><td>17</td><td>55</td></tr>
    <tr><td>36</td><td>Nelson Mandela</td><td>9.47 ± 0.18</td><td>64.2 ± 1.2</td><td>16</td><td>59</td></tr>
    <tr><td>37</td><td>Bill Gates</td><td>9.46 ± 0.25</td><td>69.0 ± 1.6</td><td>14</td><td>66</td></tr>
    <tr><td>38</td><td>Isaac Newton</td><td>9.29 ± 0.12</td><td>57.3 ± 0.8</td><td>25</td><td>37</td></tr>
    <tr><td>39</td><td>Mary Magdalene</td><td>9.12 ± 0.14</td><td>34.1 ± 0.7</td><td>43</td><td>21</td></tr>
    <tr><td>40</td><td>Muhammad Ali</td><td>9.04 ± 0.21</td><td>60.3 ± 1.3</td><td>16</td><td>56</td></tr>
    <tr><td>41</td><td>Charles Darwin</td><td>9.04 ± 0.12</td><td>55.9 ± 0.8</td><td>21</td><td>44</td></tr>
    <tr><td>42</td><td>Julius Caesar</td><td>9.03 ± 0.14</td><td>47.0 ± 0.8</td><td>43</td><td>21</td></tr>
    <tr><td>43</td><td>John F Kennedy</td><td>9.02 ± 0.25</td><td>54.6 ± 1.6</td><td>16</td><td>56</td></tr>
    <tr><td>44</td><td>David Beckham</td><td>8.82 ± 0.24</td><td>64.3 ± 1.6</td><td>14</td><td>62</td></tr>
    <tr><td>45</td><td>Diego Maradona</td><td>8.82 ± 0.25</td><td>60.7 ± 1.6</td><td>15</td><td>59</td></tr>
    <tr><td>46</td><td>Galileo</td><td>8.76 ± 0.21</td><td>50.9 ± 1.5</td><td>26</td><td>33</td></tr>
    <tr><td>47</td><td>Karl Marx</td><td>8.74 ± 0.12</td><td>49.8 ± 0.7</td><td>21</td><td>42</td></tr>
    <tr><td>48</td><td>Leonardo da Vinci</td><td>8.64 ± 0.12</td><td>53.8 ± 0.8</td><td>28</td><td>30</td></tr>
    <tr><td>49</td><td>Pelé</td><td>8.63 ± 0.23</td><td>55.0 ± 1.5</td><td>16</td><td>53</td></tr>
    <tr><td>50</td><td>Elvis Presley</td><td>8.56 ± 0.25</td><td>52.9 ± 1.5</td><td>16</td><td>52</td></tr>
    <tr><td>51</td><td>Steve Jobs</td><td>8.53 ± 0.26</td><td>65.2 ± 1.7</td><td>13</td><td>63</td></tr>
    <tr><td>52</td><td>George W Bush</td><td>8.50 ± 0.27</td><td>61.6 ± 1.7</td><td>14</td><td>61</td></tr>
    <tr><td>53</td><td>Mother Teresa</td><td>8.47 ± 0.13</td><td>57.3 ± 0.9</td><td>16</td><td>54</td></tr>
    <tr><td>54</td><td>Ali ibn Abi Talib</td><td>8.41 ± 0.19</td><td>35.1 ± 0.9</td><td>38</td><td>22</td></tr>
    <tr><td>55</td><td>Lenin</td><td>8.39 ± 0.28</td><td>47.2 ± 1.7</td><td>18</td><td>46</td></tr>
    <tr><td>56</td><td>Beethoven</td><td>8.35 ± 0.21</td><td>48.4 ± 1.5</td><td>23</td><td>37</td></tr>
    <tr><td>57</td><td>J K Rowling</td><td>8.34 ± 0.24</td><td>62.6 ± 1.6</td><td>14</td><td>59</td></tr>
    <tr><td>58</td><td>Qin Shi Huang</td><td>8.29 ± 0.12</td><td>31.3 ± 0.5</td><td>44</td><td>19</td></tr>
    <tr><td>59</td><td>Michael Jordan</td><td>8.23 ± 0.23</td><td>57.4 ± 1.5</td><td>15</td><td>56</td></tr>
    <tr><td>60</td><td>Pope John Paul II</td><td>8.19 ± 0.24</td><td>54.4 ± 1.6</td><td>15</td><td>54</td></tr>
    <tr><td>61</td><td>William Shakespeare</td><td>8.18 ± 0.11</td><td>49.5 ± 0.7</td><td>27</td><td>30</td></tr>
    <tr><td>62</td><td>Xi Jinping</td><td>8.15 ± 0.23</td><td>62.1 ± 1.2</td><td>13</td><td>62</td></tr>
    <tr><td>63</td><td>Fidel Castro</td><td>7.92 ± 0.24</td><td>48.8 ± 1.5</td><td>16</td><td>49</td></tr>
    <tr><td>64</td><td>Queen Victoria</td><td>7.86 ± 0.11</td><td>40.1 ± 0.7</td><td>21</td><td>37</td></tr>
    <tr><td>65</td><td>Charlie Chaplin</td><td>7.86 ± 0.22</td><td>42.3 ± 1.5</td><td>18</td><td>44</td></tr>
    <tr><td>66</td><td>Elon Musk</td><td>7.71 ± 0.23</td><td>60.5 ± 1.5</td><td>13</td><td>59</td></tr>
    <tr><td>67</td><td>George Washington</td><td>7.63 ± 0.11</td><td>46.2 ± 0.7</td><td>23</td><td>33</td></tr>
    <tr><td>68</td><td>John Lennon</td><td>7.61 ± 0.23</td><td>48.6 ± 1.5</td><td>16</td><td>48</td></tr>
    <tr><td>69</td><td>Pontius Pilate</td><td>7.59 ± 0.25</td><td>24.9 ± 1.1</td><td>43</td><td>18</td></tr>
    <tr><td>70</td><td>Che Guevara</td><td>7.56 ± 0.23</td><td>47.8 ± 1.5</td><td>16</td><td>47</td></tr>
    <tr><td>71</td><td>Taylor Swift</td><td>7.55 ± 0.11</td><td>60.3 ± 0.8</td><td>13</td><td>56</td></tr>
    <tr><td>72</td><td>Mozart</td><td>7.49 ± 0.20</td><td>43.4 ± 1.4</td><td>23</td><td>32</td></tr>
    <tr><td>73</td><td>Cleopatra</td><td>7.46 ± 0.10</td><td>42.9 ± 0.7</td><td>43</td><td>17</td></tr>
    <tr><td>74</td><td>Guan Yu</td><td>7.43 ± 0.17</td><td>22.4 ± 0.6</td><td>41</td><td>18</td></tr>
    <tr><td>75</td><td>Madonna</td><td>7.32 ± 0.23</td><td>50.5 ± 1.6</td><td>15</td><td>49</td></tr>
    <tr><td>76</td><td>King Herod</td><td>7.19 ± 0.26</td><td>24.1 ± 1.0</td><td>43</td><td>17</td></tr>
    <tr><td>77</td><td>Pablo Picasso</td><td>6.97 ± 0.20</td><td>43.6 ± 1.4</td><td>18</td><td>38</td></tr>
    <tr><td>78</td><td>Marco Polo</td><td>6.96 ± 0.18</td><td>38.0 ± 1.3</td><td>31</td><td>22</td></tr>
    <tr><td>79</td><td>Marie Curie</td><td>6.87 ± 0.16</td><td>42.8 ± 1.1</td><td>19</td><td>37</td></tr>
    <tr><td>80</td><td>Aisha</td><td>6.86 ± 0.17</td><td>30.2 ± 0.8</td><td>38</td><td>18</td></tr>
    <tr><td>81</td><td>Bob Marley</td><td>6.82 ± 0.22</td><td>46.3 ± 1.5</td><td>15</td><td>44</td></tr>
    <tr><td>82</td><td>Mencius</td><td>6.78 ± 0.11</td><td>23.2 ± 0.4</td><td>45</td><td>15</td></tr>
    <tr><td>83</td><td>Pope Francis</td><td>6.71 ± 0.22</td><td>51.4 ± 1.5</td><td>13</td><td>51</td></tr>
    <tr><td>84</td><td>Fatimah</td><td>6.66 ± 0.17</td><td>28.7 ± 0.8</td><td>38</td><td>17</td></tr>
    <tr><td>85</td><td>Aristotle</td><td>6.60 ± 0.11</td><td>37.0 ± 0.7</td><td>45</td><td>15</td></tr>
    <tr><td>86</td><td>Indira Gandhi</td><td>6.51 ± 0.11</td><td>41.2 ± 0.6</td><td>16</td><td>41</td></tr>
    <tr><td>87</td><td>Marilyn Monroe</td><td>6.25 ± 0.21</td><td>38.5 ± 1.3</td><td>17</td><td>38</td></tr>
    <tr><td>88</td><td>Martin Luther</td><td>5.94 ± 0.16</td><td>31.4 ± 0.9</td><td>28</td><td>21</td></tr>
    <tr><td>89</td><td>Kublai Khan</td><td>5.85 ± 0.22</td><td>26.7 ± 1.1</td><td>32</td><td>18</td></tr>
    <tr><td>90</td><td>Joan of Arc</td><td>5.58 ± 0.10</td><td>31.1 ± 0.7</td><td>29</td><td>19</td></tr>
    <tr><td>91</td><td>Khadija</td><td>5.28 ± 0.36</td><td>26.6 ± 1.7</td><td>38</td><td>14</td></tr>
    <tr><td>92</td><td>Akbar</td><td>4.88 ± 0.17</td><td>26.2 ± 0.7</td><td>27</td><td>18</td></tr>
    <tr><td>93</td><td>Wu Zetian</td><td>3.56 ± 0.13</td><td>16.7 ± 0.6</td><td>38</td><td>9</td></tr>
  </tbody>
</table>

</details>

### Who's missing?

I tested 93 figures, chosen based on my own judgment and by repeatedly prompting LLMs for suggestions. My guess is that no untested figure would crack the top 30, though it's hard to be confident. I count King David and King Solomon as mythological, but if we counted them as historical both would plausibly make the top 30 given their prominence in both Christianity and Islam.

For other figures, we can bound their plausible rank by looking at similar figures we did test:
- **Religious figures**: Additional Christian saints would fall below Saint Paul (23rd) and Saint Peter (28th). Untested early Islamic figures like Abu Bakr and Umar would rank below Ali ibn Abi Talib (54th) and probably below Aisha (80th) and Fatimah (84th). Any additional Confucian is probably less famous than Mencius (82nd).
- **Classical antiquity**: Alexander the Great (15th), Julius Caesar (42nd), Cleopatra (73rd), and Aristotle (85th) set the ceiling. Augustus probably performs somewhat worse than Julius Caesar, and Plato or Socrates probably rank similarly to Aristotle. No other Roman emperor likely comes close to these two, and it's unlikely any other classical philosopher ranks much higher than Aristotle.
- **Scientists**: Einstein (8th), Newton (38th), Darwin (41st), and Galileo (46th) are probably the four most famous scientists of all time. Marie Curie (79th) is almost certainly the most famous female scientist.
- **Artists**: Leonardo da Vinci (48th) and Pablo Picasso (77th) have a strong claim to be the two most famous artists in history, while Beethoven (56th) and Mozart (72nd) are almost certainly the most famous classical composers.
- **Dictators**: Stalin (26th), Mao (35th), and Saddam Hussein (33rd) likely cover the most famous; Mussolini, Gaddafi, Idi Amin, and Bashar al-Assad would rank below all of them.

The area where I'm least confident is modern celebrities. There have been a lot of globally famous people over the past century, and because the world population is so large, even a brief stint of genuine cross-cultural penetration is enough to accumulate surprisingly high recognition—this is how Michael Jackson ranks 11th overall. The difficulty is that fame in the Anglosphere is not the same as global fame, and a figure can be dominant in one but not the other.

### Sources of error

There are three main sources of error.

**Stochastic sampling error** is the easiest to quantify and the smallest. With 2,350 queried lives, the standard error on a figure recognized by ~20% of people is about 0.2 percentage points, which is small enough that the top 10 ordering is stable across runs.

**Demographic uncertainty** is potentially the most consequential for the top of the list. The population estimates I use are uncertain, as discussed in the [previous blog post](https://random-lives.github.io/random-lives/blog/how-many-people-have-ever-lived/). Higher historical populations boost ancient figures; lower ones boost modern figures. Here are the top 20 recomputed using the low and high population estimates from that post:

<table id="sensitivity-table">
  <thead>
    <tr>
      <th rowspan="2">Rank</th>
      <th rowspan="2">Person</th>
      <th colspan="3">Recognition among all people (%)</th>
      <th rowspan="2" class="sortable" data-col="5" data-table="sensitivity-table">High − Low</th>
    </tr>
    <tr>
      <th class="sortable" data-col="2" data-table="sensitivity-table">Low population</th>
      <th class="sortable" data-col="3" data-table="sensitivity-table">Baseline</th>
      <th class="sortable" data-col="4" data-table="sensitivity-table">High population</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>The Buddha</td><td>20.98</td><td>21.94</td><td>23.01</td><td>+2.03</td></tr>
    <tr><td>2</td><td>Jesus of Nazareth</td><td>21.25</td><td>21.46</td><td>21.61</td><td>+0.36</td></tr>
    <tr><td>3</td><td>Muhammad</td><td>17.84</td><td>17.95</td><td>17.98</td><td>+0.14</td></tr>
    <tr><td>4</td><td>The Virgin Mary</td><td>16.90</td><td>17.15</td><td>17.36</td><td>+0.46</td></tr>
    <tr><td>5</td><td>Adolf Hitler</td><td>14.68</td><td>14.16</td><td>13.54</td><td>−1.14</td></tr>
    <tr><td>6</td><td>Confucius</td><td>12.68</td><td>12.90</td><td>13.13</td><td>+0.44</td></tr>
    <tr><td>7</td><td>John the Baptist</td><td>12.46</td><td>12.79</td><td>13.11</td><td>+0.65</td></tr>
    <tr><td>8</td><td>Albert Einstein</td><td>13.10</td><td>12.60</td><td>12.02</td><td>−1.08</td></tr>
    <tr><td>9</td><td>St Joseph</td><td>12.31</td><td>12.50</td><td>12.66</td><td>+0.35</td></tr>
    <tr><td>10</td><td>Genghis Khan</td><td>12.08</td><td>12.02</td><td>11.92</td><td>−0.17</td></tr>
    <tr><td>11</td><td>Michael Jackson</td><td>12.35</td><td>11.86</td><td>11.26</td><td>−1.09</td></tr>
    <tr><td>12</td><td>Gandhi</td><td>12.00</td><td>11.57</td><td>11.06</td><td>−0.94</td></tr>
    <tr><td>13</td><td>Walt Disney</td><td>11.48</td><td>11.04</td><td>10.51</td><td>−0.97</td></tr>
    <tr><td>14</td><td>Queen Elizabeth II</td><td>11.24</td><td>10.81</td><td>10.29</td><td>−0.95</td></tr>
    <tr><td>15</td><td>Alexander the Great</td><td>10.65</td><td>10.78</td><td>10.95</td><td>+0.31</td></tr>
    <tr><td>16</td><td>Napoleon Bonaparte</td><td>11.08</td><td>10.76</td><td>10.38</td><td>−0.69</td></tr>
    <tr><td>17</td><td>Osama Bin Laden</td><td>11.19</td><td>10.73</td><td>10.18</td><td>−1.02</td></tr>
    <tr><td>18</td><td>Jackie Chan</td><td>11.12</td><td>10.67</td><td>10.13</td><td>−0.99</td></tr>
    <tr><td>19</td><td>Cristiano Ronaldo</td><td>10.90</td><td>10.45</td><td>9.85</td><td>−1.05</td></tr>
    <tr><td>20</td><td>Winston Churchill</td><td>10.73</td><td>10.36</td><td>9.93</td><td>−0.80</td></tr>
  </tbody>
</table>

Modern figures (Hitler, Einstein, Michael Jackson) are pulled up under the low population scenario, and ancient figures (the Buddha, Confucius, John the Baptist) are pulled up under the high population scenario. But the effect is modest: no figure moves by more than two ranks, and the only change in the top 5 is that Jesus overtakes the Buddha under the low population estimate. There are other ways the demographics could vary—for instance, the relative size of India and China versus Europe matters for the Buddha-Jesus comparison—but overall the rankings are not very sensitive, probably because even for ancient figures, most of their recognition comes from people alive in the last few centuries.

**LLM estimation error** is the hardest to quantify. When the probability is near zero, for instance because the person lived on the wrong continent, died too young, or because a figure was only recognisable to the literate, the model reproduces this. Likewise, the model is good at recognising near-certainties, like that every adult American has heard of Donald Trump. The real uncertainty is in the middle: figures with mixed or partial global reach, like Michael Jackson or Cristiano Ronaldo. If I had to guess, I'd say the model probably overrates these figures slightly, but I can't be sure: the model is in fact reasoning through the relevant considerations, including the kinds of errors it might make. The best way to improve this would be to collect real-world name-recognition data for even a handful of figures and calibrate the LLM against it, but I'll leave that for when GPT-7 can conduct its own fieldwork.

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Generic sortable table handler—descending only
  function setupSortable(tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    var headers = table.querySelectorAll('th.sortable[data-table="' + tableId + '"], th.sortable[data-col]');
    // For full-table, headers don't have data-table attr, so match by parent
    if (tableId === 'full-table') {
      headers = table.querySelectorAll('th.sortable');
    } else {
      headers = table.querySelectorAll('th.sortable[data-table="' + tableId + '"]');
    }

    headers.forEach(function(th) {
      th.addEventListener('click', function() {
        var col = parseInt(this.dataset.col);
        var rows = Array.from(tbody.querySelectorAll('tr'));
        rows.sort(function(a, b) {
          var aVal = parseFloat(a.children[col].textContent);
          var bVal = parseFloat(b.children[col].textContent);
          return bVal - aVal; // descending only
        });
        rows.forEach(function(row, i) {
          row.children[0].textContent = i + 1;
          tbody.appendChild(row);
        });
        // Update header indicators
        headers.forEach(function(h) { h.classList.remove('sort-desc'); });
        this.classList.add('sort-desc');
      });
    });
  }

  setupSortable('full-table');
  setupSortable('sensitivity-table');
});
</script>
