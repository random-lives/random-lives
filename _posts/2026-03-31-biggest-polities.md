---
layout: post
title: "What were the biggest states in history?"
date: 2026-03-31
permalink: /blog/biggest-polities/
mathjax: true
published: false
---

Everyone knows the biggest country in the world. India overtook China in 2023; before that, China held the top spot for centuries. The rankings are reported in the news, tracked by the UN, and not seriously disputed. Even further down the list—the United States, Indonesia, Pakistan, Nigeria, Brazil—the numbers are imprecise, but the ordering is clear enough.

What would the rankings look like if we included all countries throughout history? This is tricky for a couple of reasons. First, populations change over time. What we really want is some cumulative measure of how many people a state governed, and there are two natural ways to think about this:

1. **Births**: how many people were born under the state's rule?
2. **Person-years**: how much total time did people spend living under this state?

We'll look at both. But the trickier problem is more fundamental: what counts as a state?

Today, this is relatively easy. Modern states form something like a cartel of mutual recognition. The world mostly divides cleanly along international borders, and sovereignty generally matches *de facto* control. Even in disputed cases like Western Sahara, Crimea, or Taiwan, it's usually clear on the ground who collects the taxes and runs the courts. 

Go back a few centuries and this clarity dissolves. Tributary states owe nominal allegiance to an overlord but govern themselves in practice. A local lord might obey the emperor this decade and ignore him the next. The Holy Roman Empire contained hundreds of semi-independent princes, bishops, and free cities under a nominal imperial umbrella. The Mughal Empire "controlled" much of India, but its authority over the southern kingdoms was often a polite fiction.

States also split and merge, and it is not always obvious on the ground when this happens. After the Third Century Crisis, the Roman Empire was frequently divided between multiple emperors. Theodosius I, who died in 395, turned out to be the last emperor to rule both halves—but nobody in the year 400 knew the split would be permanent, and no one at the time called the eastern half the "Byzantine Empire." It's only with hindsight that historians decided that 395 was the year one polity became two, and even that is somewhat arbitrary. The gradual emergence of the Irish Free State provides another example. 

We've generally erred on the side of splitting rather than lumping. The Western and Eastern Roman Empires are counted separately. The Song Dynasty is split into Northern Song and Southern Song. The Qing Dynasty and the People's Republic of China are distinct polities. Where historians conventionally recognise a split, we follow the convention; where it's genuinely unclear, we asked an LLM and let it make judgement calls informed by the historical context. For pragmatic reasons we generally don't split factions within a civil war. 

For European colonial empires, we distinguish colonies from the metropole: the British Raj is a separate polity from the United Kingdom, and French Indochina is separate from the French Republic. We also show "overlay" totals that sum up all the territories under a given imperial umbrella, but these are presented alongside the individual counts, not instead of them.

The detailed methodology is at the end of this post. The short version: [using the same sampling framework as our population estimates](/random-lives/blog/how-many-people-have-ever-lived/), we assigned each of one million randomly sampled people to the polity that governed the place where they were born. About two-thirds could be assigned deterministically from modern country borders and historical timelines. For the remainder—people born in contested periods or regions with overlapping control—we used an LLM (GPT-5.2) to classify each person based on their coordinates, birth year, and regional context. Polities with large LLM-derived components have wider error bars.

## The biggest polities by births

Here are the top 50 polities by the number of people born under their rule, as a share of all ~66 billion people who have ever lived:

<!-- TODO: should this be top 50 with full table in expandable section, or just top 20/30 in main text? -->

<table class="data-table">
  <thead>
    <tr>
      <th>Rank</th>
      <th>Polity</th>
      <th>% of all births</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Qing Dynasty</td><td>3.85 ± 0.03%</td></tr>
    <tr><td>2</td><td>Republic of India</td><td>2.83 ± 0.02%</td></tr>
    <tr><td>3</td><td>People's Republic of China</td><td>2.55 ± 0.03%</td></tr>
    <tr><td>4</td><td>British Raj</td><td>1.92 ± 0.02%</td></tr>
    <tr><td>5</td><td>Ming Dynasty</td><td>1.40 ± 0.03%</td></tr>
    <tr><td>6</td><td>Roman Empire</td><td>1.29 ± 0.02%</td></tr>
    <tr><td>7</td><td>Mughal Empire</td><td>1.25 ± 0.05%</td></tr>
    <tr><td>8</td><td>Russian Empire</td><td>0.96 ± 0.04%</td></tr>
    <tr><td>9</td><td>Delhi Sultanate</td><td>0.85 ± 0.06%</td></tr>
    <tr><td>10</td><td>United States</td><td>0.81 ± 0.02%</td></tr>
    <tr><td>11</td><td>Republic of China (Nanjing)</td><td>0.77 ± 0.05%</td></tr>
    <tr><td>12</td><td>East India Company</td><td>0.75 ± 0.04%</td></tr>
    <tr><td>13</td><td>Gupta Empire</td><td>0.74 ± 0.05%</td></tr>
    <tr><td>14</td><td>Pala Empire</td><td>0.73 ± 0.05%</td></tr>
    <tr><td>15</td><td>Holy Roman Empire</td><td>0.73 ± 0.01%</td></tr>
    <tr><td>16</td><td>Southern Song Dynasty</td><td>0.72 ± 0.01%</td></tr>
    <tr><td>17</td><td>Ottoman Empire</td><td>0.72 ± 0.03%</td></tr>
    <tr><td>18</td><td>Tang Dynasty</td><td>0.68 ± 0.03%</td></tr>
    <tr><td>19</td><td>Kushan Empire</td><td>0.68 ± 0.05%</td></tr>
    <tr><td>20</td><td>Soviet Union</td><td>0.64 ± 0.02%</td></tr>
    <tr><td>21</td><td>Eastern Han Dynasty</td><td>0.61 ± 0.02%</td></tr>
    <tr><td>22</td><td>Byzantine Empire</td><td>0.61 ± 0.02%</td></tr>
    <tr><td>23</td><td>Gurjara-Pratihara Empire</td><td>0.60 ± 0.05%</td></tr>
    <tr><td>24</td><td>Satavahana Dynasty</td><td>0.57 ± 0.05%</td></tr>
    <tr><td>25</td><td>Republic of Indonesia</td><td>0.55 ± 0.01%</td></tr>
    <tr><td>26</td><td>Maurya Empire</td><td>0.53 ± 0.04%</td></tr>
    <tr><td>27</td><td>Islamic Republic of Pakistan</td><td>0.50 ± 0.01%</td></tr>
    <tr><td>28</td><td>Yuan Dynasty</td><td>0.50 ± 0.01%</td></tr>
    <tr><td>29</td><td>Federal Republic of Nigeria</td><td>0.46 ± 0.01%</td></tr>
    <tr><td>30</td><td>Kingdom of France</td><td>0.44 ± 0.02%</td></tr>
    <tr><td>31</td><td>Chola Empire</td><td>0.40 ± 0.04%</td></tr>
    <tr><td>32</td><td>Shunga Empire</td><td>0.40 ± 0.04%</td></tr>
    <tr><td>33</td><td>Northern Song Dynasty</td><td>0.38 ± 0.01%</td></tr>
    <tr><td>34</td><td>Western Han Dynasty</td><td>0.38 ± 0.02%</td></tr>
    <tr><td>35</td><td>Achaemenid Empire</td><td>0.37 ± 0.02%</td></tr>
    <tr><td>36</td><td>Tokugawa Shogunate</td><td>0.37 ± 0.01%</td></tr>
    <tr><td>37</td><td>Rashtrakuta Empire</td><td>0.35 ± 0.04%</td></tr>
    <tr><td>38</td><td>Bengal Sultanate</td><td>0.33 ± 0.04%</td></tr>
    <tr><td>39</td><td>United Kingdom</td><td>0.32 ± 0.01%</td></tr>
    <tr><td>40</td><td>Western Chalukya Empire</td><td>0.31 ± 0.04%</td></tr>
    <tr><td>41</td><td>Vijayanagara Empire</td><td>0.31 ± 0.03%</td></tr>
    <tr><td>42</td><td>Mexico</td><td>0.30 ± 0.01%</td></tr>
    <tr><td>43</td><td>People's Republic of Bangladesh</td><td>0.30 ± 0.01%</td></tr>
    <tr><td>44</td><td>Dutch East Indies</td><td>0.29 ± 0.02%</td></tr>
    <tr><td>45</td><td>Maratha Empire</td><td>0.28 ± 0.03%</td></tr>
    <tr><td>46</td><td>Vakataka Dynasty</td><td>0.26 ± 0.03%</td></tr>
    <tr><td>47</td><td>Eastern Ganga Dynasty</td><td>0.25 ± 0.03%</td></tr>
    <tr><td>48</td><td>Sassanid Empire</td><td>0.25 ± 0.02%</td></tr>
    <tr><td>49</td><td>Pandya Dynasty</td><td>0.24 ± 0.03%</td></tr>
    <tr><td>50</td><td>Abbasid Caliphate</td><td>0.24 ± 0.02%</td></tr>
  </tbody>
</table>

Several things jump out.

### China

The single largest polity is the Qing Dynasty, at 3.85% of all births—about 2.5 billion people. If we group all Chinese dynasties together, Imperial China accounts for **8.7% of all births in human history**. Nearly one in eleven people who ever lived was born under Chinese imperial rule.

<table class="data-table">
  <thead>
    <tr>
      <th>Rank</th>
      <th>Group</th>
      <th>% of all births</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Imperial China</td><td>8.74 ± 0.06%</td></tr>
    <tr><td>2</td><td>Roman civilization</td><td>2.13 ± 0.04%</td></tr>
    <tr><td>3</td><td>Russian Empire / USSR</td><td>1.89 ± 0.05%</td></tr>
    <tr><td>4</td><td>Japan (all periods)</td><td>1.25 ± 0.02%</td></tr>
    <tr><td>5</td><td>United States (broad)</td><td>0.85 ± 0.02%</td></tr>
    <tr><td>6</td><td>Ancient Egypt</td><td>0.41 ± 0.03%</td></tr>
    <tr><td>7</td><td>German Empire (broad)</td><td>0.29 ± 0.01%</td></tr>
    <tr><td>8</td><td>Mongol Empire (broad)</td><td>0.21 ± 0.03%</td></tr>
  </tbody>
</table>

This isn't a reflection of China's current population. The Qing Dynasty alone, which ruled from 1644 to 1912, saw more births than the People's Republic of China has in its 77 years. China's demographic weight is ancient: the Han Dynasty (206 BC – 220 AD) already had a population comparable to the Roman Empire's, and China maintained or exceeded that level for the next two millennia. The Qing takes the top spot because it combined this enormous base with a demographic explosion driven by New World crops—maize, sweet potatoes, peanuts—that could grow on previously marginal land, roughly tripling the population from 150 million to 430 million.

The closest comparison is "Roman civilization" at 2.13%—but this spans over two thousand years from the founding of the Roman Kingdom to the fall of Constantinople in 1453. Over a similar timespan, Imperial China accumulated four times as many births. The "four great civilisations" framing understates how much bigger China's share is compared to the others.

### India

India provides a striking contrast. The subcontinent's total population has often rivalled China's, but India was rarely unified under a single state. No fewer than 15 Indian polities appear in the top 50, but no single one dominates: the Mughal Empire, the largest pre-modern Indian state, accounts for barely a seventh of what Imperial China does as a group.

This reflects a genuinely different political history. China repeatedly reconsolidated into unified dynasties after periods of fragmentation. India didn't. The Maurya Empire (322–185 BC) and the Mughal Empire (1526–1857) are the two closest things to subcontinental unification, separated by nearly two millennia—and even they never fully controlled the south.

Many Indian empires have wide error bars—the Gurjara-Pratihara Empire, for example, has zero deterministic assignments; every birth attributed to it comes from LLM classification. This is because India's political geography was genuinely complex. Several empires routinely overlapped, with the Gurjara-Pratiharas, Palas, and Rashtrakutas simultaneously claiming different parts of the subcontinent in the 8th–10th centuries, and local kingdoms persisting underneath all of them.

### The Roman Empire

The Roman Empire comes in at #6 with 1.29% of all births. This might seem low for the paradigmatic empire of Western civilisation, but the Mediterranean basin was modestly populated compared to South and East Asia. At its peak, Rome had perhaps 60–70 million people—comparable to the contemporary Han Dynasty, but controlling less productive agricultural land. Rome looms large in our historical imagination because we inherited its literature, its legal traditions, and its languages. Demographically, it was a regional power.

### Colonial empires

Colonial empires are a different kind of entity. The British Empire didn't replace local governance everywhere—it layered colonial administration on top of existing structures. We can count these as "overlays": everyone born under any form of British rule, whether in the UK itself, the British Raj, or dozens of smaller colonies.

<table class="data-table">
  <thead>
    <tr>
      <th>Empire</th>
      <th>% of all births</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>British Empire</td><td>3.96%</td></tr>
    <tr><td>French Empire</td><td>1.02%</td></tr>
    <tr><td>Spanish Empire</td><td>0.91%</td></tr>
    <tr><td>Mongol Empire (Genghisid)</td><td>0.77%</td></tr>
    <tr><td>Habsburg domains</td><td>0.76%</td></tr>
    <tr><td>Caliphate (mainline)</td><td>0.41%</td></tr>
    <tr><td>Dutch Empire</td><td>0.39%</td></tr>
    <tr><td>Portuguese Empire</td><td>0.24%</td></tr>
  </tbody>
</table>

The British Empire is the largest at 3.96%—but this is overwhelmingly India. The Raj and East India Company together account for 2.67% of the 3.96%. Remove India, and the British Empire drops below the French Empire.

The Mongol Empire, often cited as the largest contiguous land empire, managed just 0.77% of all births. Most of its territory was sparsely populated steppe. The Yuan Dynasty—the Mongol-ruled Chinese portion—accounts for nearly two-thirds of the total. As with the British in India, the Mongols' demographic weight came from controlling an already-massive population, not from their Central Asian heartland.

## Births vs. person-years

<!-- TODO: This section will be expanded once person-years analysis is complete -->

Everything above counts *births*: how many people were born under each polity. But births don't capture duration. A dynasty that lasted 300 years with a moderately large population might accumulate more person-years of governance than a massive modern state that has existed for only 80 years.

Person-years—the integral of population over time—is in some ways a more natural measure. If you picked a random person at a random moment during their life, what state would they be living under? This weights long-lived empires more heavily and short-lived population booms less.

We're currently computing person-year rankings and will update this post with the results. The rankings will likely shift: the Roman/Byzantine succession and the Ottoman Empire should climb, while modern states like the Republic of India (79 years old but massive) may fall relative to longer-lived polities.

<!-- TODO: Add person-years table and discussion when ready -->

## How many polities?

Nobody seems to have tried to count the number of distinct polities across human history. There are databases of modern sovereign states—the [Correlates of War project](https://correlatesofwar.org/) lists about 200 at any given time—and various lists of historical empires. But a comprehensive count? As far as I can tell, it hasn't been attempted.

Our data gives a rough floor. In the course of assigning every sampled person to a governing polity, we identified about **1,500 distinct named polities**—464 large enough to track systematically, and over 1,000 more that turned up when we asked the LLM to classify people from ambiguous times and places.

These are not all empires. Many are small kingdoms, city-states, colonial administrative units, or transitional regimes. The Judicate of Cagliari. The Kuchkabal of Ah Kin Chel. The Acholi Chiefdoms. The Commune of Brescia. The Mzab (Ibadi) Confederation. The Syro-Hittite Kingdom of Palistin. The Ambrosian Republic, which governed Milan for about three years. Some of these polities governed millions of people for centuries; others governed a single valley for a generation.

And 1,500 is certainly an undercount. We only identify polities that governed someone at a specific set of sampled coordinates in a specific year; we miss polities that existed but didn't happen to control any of our sampled points. The actual number of distinct political entities across human history is almost certainly in the tens of thousands—perhaps hundreds of thousands, if you count every chiefdom, city-state, tribal confederation, and petty kingdom that existed for any length of time.

## Methodology

### Deterministic assignment

For each of about 200 modern countries, we compiled a timeline mapping every year to a single governing polity. These draw on standard historical references. We only systematically track polities responsible for at least 100 million lifetime births—roughly equivalent to an average population of 5 million sustained over 500 years, or 25 million over 100 years. Smaller entities are real but individually negligible. Periods where multiple polities competed for control of a modern country's territory are marked "indeterminate."

### LLM classification

For indeterminate periods and regions below the systematic threshold, we sampled 10,000 people and asked GPT-5.2 to assign each one to a polity based on coordinates, birth year, and regional context. The LLM received canonical polity name lists to enforce consistent naming, and was told about conventional dates for splits and transitions (e.g. 395 for the Roman Empire, dynastic transition dates for China). Each classified person represents about 41 unclassified people (the scale factor), so LLM-derived counts carry more statistical uncertainty. Error bars throughout reflect both sampling variance and this scaling.

### What counts as governing?

We identify the polity that *directly administered* the area—the entity that collected taxes, maintained order, and appointed officials. Tributary states and loose suzerainties don't count unless the overlord exercised real administrative control. A person living in a nominally Mughal-tributary kingdom in southern India gets classified under the local kingdom, not the Mughal Empire.

### Groupings and overlays

The "larger groupings" table combines related polities into civilisational units—all Chinese dynasties under "Imperial China," the Roman Kingdom through the Byzantine Empire under "Roman civilization." These groupings are inherently somewhat arbitrary.

"Overlay" groups count everyone born under *any* constituent polity. These can overlap: the Yuan Dynasty contributes to both "Imperial China" and "Mongol Empire (Genghisid)." Overlays are shown separately for this reason.
