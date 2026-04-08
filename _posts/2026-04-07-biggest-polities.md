---
layout: post
title: What was the biggest state?
date: 2026-04-07
permalink: /blog/biggest-polities/
published: true
---

Ranking the largest empires by area is a fairly straightforward exercise. [Wikipedia](https://en.wikipedia.org/wiki/List_of_largest_empires) puts the British Empire in the top spot, controlling 35.5 million km² at its peak—about a quarter of the world's land area. Next come the Mongol Empire and the Russian Empire.

But if we want to understand the typical human experience, we care less about how much land an empire controlled than how many people lived under it. The British Empire's area was dominated by Canada and Australia, but the vast majority of its subjects lived in India. The Mongol and Russian empires are likewise generously padded by the massive but sparsely populated steppe.

At present the largest country by population is India, which overtook China in 2023. Here I try to produce a population ranking for all the states and empires that have existed historically. One way to do this is by peak population, but that doesn't quite capture cumulative human experience—a state that peaked at 100 million for a decade matters less than one that held 50 million for three centuries. So I also look at two other metrics:

1. **Births**: how many people were born under the state's rule.
2. **Person-years**: total time spent living under the state—the integral of its population over time.

Before looking at the numbers, first a tricky question: what counts as a state? Today there is an international system of diplomacy, underpinned by the UN, mutual recognition between governments, and international law, that provides a canonical answer in most cases. Even in disputed cases like the Western Sahara, Crimea, or Taiwan, there's generally an unambiguous answer to who collects taxes or runs the courts.

Go back a few centuries and political structures become much less formal, and the line between 'subject territory' and 'independent state' was blurry and unstable. A provincial governor might render taxes to the emperor only sometimes; an outlying territory might claim nominal allegiance to one or even several distant authorities while acting independently.

States also evolve over time in ways that make it hard to draw clean boundaries. The Roman Empire was frequently divided between multiple emperors after the Third Century Crisis; Theodosius I, who died in 395, turned out to be the last to rule both halves, but nobody at the time knew the split would be permanent. It is only with hindsight that historians treat 395 as the year one polity became two.

Rather than try to resolve all these questions myself, I used the [Cliopatria dataset](https://www.nature.com/articles/s41597-025-04516-9)—a recently published set of ~15,000 historical polity polygons covering 3400 BCE to 2024. For each polity, I rasterized its polygon onto the [HYDE 3.4](https://essd.copernicus.org/articles/9/927/2017/) population grid and summed the population and births within it at each time step, interpolating between HYDE's 127 time steps to get annual values. Cliopatria generally splits rather than lumps: the Song Dynasty is divided into Northern and Southern Song, colonies are separate from their metropoles, and so on.

## The Rankings

Here are rankings for the top 300 polities through history:

<div id="polity-table-wrapper">
<table class="data-table" id="polity-table">
  <thead>
    <tr>
      <th>Rank</th>
      <th class="sortable" data-col="1" data-table="polity-table" data-sort="text">Polity</th>
      <th class="sortable" data-col="2" data-table="polity-table" data-sort="year">From</th>
      <th class="sortable" data-col="3" data-table="polity-table" data-sort="year">To</th>
      <th class="sortable" data-col="4" data-table="polity-table">Births (M)</th>
      <th class="sortable" data-col="5" data-table="polity-table">Person-years (B)</th>
      <th class="sortable" data-col="6" data-table="polity-table">Peak pop (M)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Qing Dynasty</td><td>1645</td><td>1911</td><td>2,500</td><td>65</td><td>430</td></tr>
    <tr><td>2</td><td>Republic of India</td><td>1947</td><td></td><td>1,900</td><td>67</td><td>1,500</td></tr>
    <tr><td>3</td><td>People&#39;s Republic of China</td><td>1950</td><td></td><td>1,600</td><td>79</td><td>1,400</td></tr>
    <tr><td>4</td><td>British Raj</td><td>1859</td><td>1947</td><td>1,400</td><td>30</td><td>450</td></tr>
    <tr><td>5</td><td>Mughal Empire</td><td>1497</td><td>1858</td><td>970</td><td>23</td><td>180</td></tr>
    <tr><td>6</td><td>Ming Dynasty</td><td>1375</td><td>1644</td><td>900</td><td>22</td><td>87</td></tr>
    <tr><td>7</td><td>Roman Empire</td><td>31 BCE</td><td>394</td><td>710</td><td>17</td><td>45</td></tr>
    <tr><td>8</td><td>Russian Empire</td><td>1721</td><td>1916</td><td>670</td><td>14</td><td>200</td></tr>
    <tr><td>9</td><td>Han Dynasty</td><td>202 BCE</td><td>237</td><td>670</td><td>16</td><td>51</td></tr>
    <tr><td>10</td><td>East India Company</td><td>1757</td><td>1858</td><td>630</td><td>15</td><td>280</td></tr>
    <tr><td>11</td><td>United States of America</td><td>1776</td><td></td><td>620</td><td>30</td><td>360</td></tr>
    <tr><td>12</td><td>Southern Song</td><td>1028</td><td>1278</td><td>560</td><td>14</td><td>74</td></tr>
    <tr><td>13</td><td>Republic of China (mainland)</td><td>1912</td><td>1949</td><td>550</td><td>14</td><td>490</td></tr>
    <tr><td>14</td><td>Gupta Empire</td><td>324</td><td>554</td><td>500</td><td>12</td><td>69</td></tr>
    <tr><td>15</td><td>Ottoman Empire</td><td>1305</td><td>1923</td><td>470</td><td>11</td><td>32</td></tr>
    <tr><td>16</td><td>Union of Soviet Socialist Republics</td><td>1922</td><td>1991</td><td>410</td><td>16</td><td>360</td></tr>
    <tr><td>17</td><td>Tang Dynasty</td><td>623</td><td>910</td><td>380</td><td>9.3</td><td>40</td></tr>
    <tr><td>18</td><td>Islamic Republic of Pakistan</td><td>1947</td><td></td><td>380</td><td>10</td><td>220</td></tr>
    <tr><td>19</td><td>Pala Empire</td><td>750</td><td>1168</td><td>360</td><td>8.7</td><td>65</td></tr>
    <tr><td>20</td><td>Republic of Indonesia</td><td>1946</td><td></td><td>340</td><td>13</td><td>260</td></tr>
    <tr><td>21</td><td>Byzantine Empire</td><td>395</td><td>1474</td><td>340</td><td>8.0</td><td>19</td></tr>
    <tr><td>22</td><td>Brazil</td><td>1890</td><td></td><td>330</td><td>12</td><td>210</td></tr>
    <tr><td>23</td><td>Federal Republic of Nigeria</td><td>1961</td><td></td><td>320</td><td>7.5</td><td>220</td></tr>
    <tr><td>24</td><td>Maurya Empire</td><td>318 BCE</td><td>171 BCE</td><td>300</td><td>7.1</td><td>67</td></tr>
    <tr><td>25</td><td>Kingdom of France</td><td>990</td><td>1791</td><td>270</td><td>7.2</td><td>29</td></tr>
    <tr><td>26</td><td>Empire of Japan</td><td>1868</td><td>1945</td><td>270</td><td>7.8</td><td>520</td></tr>
    <tr><td>27</td><td>Yuan Dynasty</td><td>1294</td><td>1374</td><td>270</td><td>6.5</td><td>85</td></tr>
    <tr><td>28</td><td>Satavahana Dynasty</td><td>225 BCE</td><td>223</td><td>260</td><td>6.3</td><td>18</td></tr>
    <tr><td>29</td><td>Kingdom of Great Britain</td><td>1709</td><td></td><td>260</td><td>11</td><td>77</td></tr>
    <tr><td>30</td><td>Kingdom of Spain</td><td>1516</td><td></td><td>240</td><td>7.8</td><td>48</td></tr>
    <tr><td>31</td><td>Tokugawa Shogunate</td><td>1600</td><td>1869</td><td>240</td><td>6.9</td><td>34</td></tr>
    <tr><td>32</td><td>British Africa</td><td>1885</td><td>1960</td><td>230</td><td>5.1</td><td>110</td></tr>
    <tr><td>33</td><td>Rashtrakuta Dynasty</td><td>755</td><td>989</td><td>230</td><td>5.6</td><td>34</td></tr>
    <tr><td>34</td><td>Mexico</td><td>1868</td><td></td><td>220</td><td>7.3</td><td>130</td></tr>
    <tr><td>35</td><td>Mongol Empire</td><td>1206</td><td>1293</td><td>210</td><td>5.1</td><td>120</td></tr>
    <tr><td>36</td><td>Vijayanagara Empire</td><td>1344</td><td>1571</td><td>210</td><td>5.1</td><td>28</td></tr>
    <tr><td>37</td><td>Sultanate of Bengal</td><td>1344</td><td>1533</td><td>200</td><td>4.8</td><td>30</td></tr>
    <tr><td>38</td><td>Chola Empire</td><td>850</td><td>1259</td><td>190</td><td>4.7</td><td>21</td></tr>
    <tr><td>39</td><td>People&#39;s Republic of Bangladesh</td><td>1973</td><td></td><td>190</td><td>6.8</td><td>180</td></tr>
    <tr><td>40</td><td>Ethiopia</td><td>1942</td><td></td><td>180</td><td>4.4</td><td>120</td></tr>
    <tr><td>41</td><td>Mamluk Dynasty</td><td>1210</td><td>1293</td><td>180</td><td>4.4</td><td>63</td></tr>
    <tr><td>42</td><td>Maratha Empire</td><td>1677</td><td>1845</td><td>180</td><td>4.3</td><td>71</td></tr>
    <tr><td>43</td><td>Spanish Empire</td><td>1516</td><td>1879</td><td>170</td><td>4.0</td><td>18</td></tr>
    <tr><td>44</td><td>Western Chalukya Empire</td><td>980</td><td>1187</td><td>170</td><td>4.1</td><td>23</td></tr>
    <tr><td>45</td><td>Dutch East Indies</td><td>1800</td><td>1949</td><td>170</td><td>4.0</td><td>68</td></tr>
    <tr><td>46</td><td>Abbasid Caliphate</td><td>750</td><td>1259</td><td>160</td><td>3.9</td><td>24</td></tr>
    <tr><td>47</td><td>Holy Roman Empire</td><td>962</td><td>1259</td><td>160</td><td>3.9</td><td>20</td></tr>
    <tr><td>48</td><td>Kushan Empire</td><td>43</td><td>237</td><td>160</td><td>3.9</td><td>30</td></tr>
    <tr><td>49</td><td>Vakataka Kingdom</td><td>260</td><td>554</td><td>160</td><td>3.8</td><td>16</td></tr>
    <tr><td>50</td><td>Habsburg Monarchy</td><td>1487</td><td>1805</td><td>160</td><td>3.9</td><td>28</td></tr>
    <tr><td>51</td><td>Joseon</td><td>1395</td><td>1897</td><td>150</td><td>3.7</td><td>15</td></tr>
    <tr><td>52</td><td>Great Jin</td><td>1126</td><td>1235</td><td>150</td><td>3.6</td><td>39</td></tr>
    <tr><td>53</td><td>Shunga Empire</td><td>170 BCE</td><td>67 BCE</td><td>140</td><td>3.5</td><td>37</td></tr>
    <tr><td>54</td><td>Republic of the Philippines</td><td>1947</td><td></td><td>140</td><td>4.7</td><td>120</td></tr>
    <tr><td>55</td><td>Western Satraps</td><td>43</td><td>489</td><td>140</td><td>3.4</td><td>12</td></tr>
    <tr><td>56</td><td>Tughlaq Dynasty</td><td>1326</td><td>1414</td><td>140</td><td>3.4</td><td>100</td></tr>
    <tr><td>57</td><td>Achaemenid Empire</td><td>550 BCE</td><td>327 BCE</td><td>140</td><td>3.3</td><td>17</td></tr>
    <tr><td>58</td><td>French Africa</td><td>1846</td><td>1957</td><td>130</td><td>2.9</td><td>77</td></tr>
    <tr><td>59</td><td>Chalukya Dynasty</td><td>555</td><td>756</td><td>130</td><td>3.2</td><td>24</td></tr>
    <tr><td>60</td><td>Sasanian Empire</td><td>215</td><td>643</td><td>130</td><td>3.1</td><td>19</td></tr>
    <tr><td>61</td><td>Gurjara-Pratihara Dynasty</td><td>732</td><td>1039</td><td>130</td><td>3.2</td><td>34</td></tr>
    <tr><td>62</td><td>Egypt</td><td>1958</td><td></td><td>130</td><td>4.2</td><td>110</td></tr>
    <tr><td>63</td><td>Republic of Turkey</td><td>1924</td><td></td><td>120</td><td>4.3</td><td>80</td></tr>
    <tr><td>64</td><td>German Empire</td><td>1871</td><td>1919</td><td>110</td><td>3.4</td><td>130</td></tr>
    <tr><td>65</td><td>Yamato</td><td>540</td><td>1187</td><td>110</td><td>2.7</td><td>5.2</td></tr>
    <tr><td>66</td><td>Western Jin</td><td>265</td><td>425</td><td>110</td><td>2.7</td><td>25</td></tr>
    <tr><td>67</td><td>Sena Dynasty</td><td>1072</td><td>1235</td><td>110</td><td>2.8</td><td>17</td></tr>
    <tr><td>68</td><td>Kingdom of England</td><td>936</td><td>1708</td><td>110</td><td>2.6</td><td>10</td></tr>
    <tr><td>69</td><td>Nepal</td><td>1775</td><td></td><td>110</td><td>3.0</td><td>44</td></tr>
    <tr><td>70</td><td>Roman Republic</td><td>500 BCE</td><td>32 BCE</td><td>100</td><td>2.4</td><td>24</td></tr>
    <tr><td>71</td><td>Japan</td><td>1953</td><td></td><td>100</td><td>8.4</td><td>130</td></tr>
    <tr><td>72</td><td>Democratic Republic of the Congo</td><td>1961</td><td></td><td>98</td><td>2.3</td><td>100</td></tr>
    <tr><td>73</td><td>Nawabs of Bengal</td><td>1718</td><td>1761</td><td>97</td><td>2.3</td><td>53</td></tr>
    <tr><td>74</td><td>Khmer Empire</td><td>800</td><td>1867</td><td>95</td><td>2.2</td><td>3.4</td></tr>
    <tr><td>75</td><td>Chu</td><td>750 BCE</td><td>224 BCE</td><td>95</td><td>2.3</td><td>10</td></tr>
    <tr><td>76</td><td>Gahadavala Dynasty</td><td>1085</td><td>1201</td><td>94</td><td>2.3</td><td>20</td></tr>
    <tr><td>77</td><td>Kingdom of Thailand</td><td>1932</td><td></td><td>93</td><td>4.2</td><td>74</td></tr>
    <tr><td>78</td><td>Parthian Empire</td><td>239 BCE</td><td>237</td><td>91</td><td>2.2</td><td>8.2</td></tr>
    <tr><td>79</td><td>Kingdom of the Franks</td><td>462</td><td>849</td><td>90</td><td>2.1</td><td>12</td></tr>
    <tr><td>80</td><td>Ghaznavid Empire</td><td>962</td><td>1209</td><td>89</td><td>2.1</td><td>14</td></tr>
    <tr><td>81</td><td>Bahmani Sultanate</td><td>1352</td><td>1491</td><td>85</td><td>2.1</td><td>16</td></tr>
    <tr><td>82</td><td>Socialist Republic of Vietnam</td><td>1973</td><td></td><td>84</td><td>4.0</td><td>99</td></tr>
    <tr><td>83</td><td>Umayyad Caliphate</td><td>656</td><td>756</td><td>84</td><td>2.0</td><td>29</td></tr>
    <tr><td>84</td><td>South Africa</td><td>1932</td><td></td><td>84</td><td>2.9</td><td>56</td></tr>
    <tr><td>85</td><td>Yadava Dynasty</td><td>1188</td><td>1325</td><td>83</td><td>2.0</td><td>15</td></tr>
    <tr><td>86</td><td>Maukhari Dynasty</td><td>555</td><td>611</td><td>83</td><td>2.0</td><td>36</td></tr>
    <tr><td>87</td><td>Kingdom of Italy (modern)</td><td>1862</td><td>1946</td><td>83</td><td>2.7</td><td>53</td></tr>
    <tr><td>88</td><td>Kalabhra Dynasty</td><td>353</td><td>601</td><td>82</td><td>2.0</td><td>8.6</td></tr>
    <tr><td>89</td><td>Morocco</td><td>1670</td><td></td><td>82</td><td>2.4</td><td>35</td></tr>
    <tr><td>90</td><td>Republic of Colombia</td><td>1866</td><td></td><td>82</td><td>3.0</td><td>55</td></tr>
    <tr><td>91</td><td>Mamluk Sultanate</td><td>1241</td><td>1518</td><td>82</td><td>2.0</td><td>9.5</td></tr>
    <tr><td>92</td><td>Tanzania</td><td>1961</td><td></td><td>81</td><td>2.0</td><td>62</td></tr>
    <tr><td>93</td><td>British Colonial Empire</td><td>1706</td><td>1999</td><td>78</td><td>2.3</td><td>30</td></tr>
    <tr><td>94</td><td>Sur Empire</td><td>1540</td><td>1594</td><td>77</td><td>1.9</td><td>77</td></tr>
    <tr><td>95</td><td>Myanmar</td><td>1948</td><td></td><td>76</td><td>2.8</td><td>51</td></tr>
    <tr><td>96</td><td>Polish-Lithuanian Commonwealth</td><td>1572</td><td>1793</td><td>76</td><td>1.8</td><td>13</td></tr>
    <tr><td>97</td><td>Austria-Hungary</td><td>1868</td><td>1918</td><td>76</td><td>2.1</td><td>63</td></tr>
    <tr><td>98</td><td>Republic of Sudan</td><td>1956</td><td></td><td>76</td><td>1.9</td><td>47</td></tr>
    <tr><td>99</td><td>Khalji Dynasty</td><td>1294</td><td>1325</td><td>75</td><td>1.8</td><td>75</td></tr>
    <tr><td>100</td><td>French Indochina</td><td>1860</td><td>1957</td><td>74</td><td>2.0</td><td>38</td></tr>
    <tr><td>101</td><td>Warring States Japan</td><td>1468</td><td>1601</td><td>73</td><td>1.8</td><td>18</td></tr>
    <tr><td>102</td><td>Northern Song</td><td>961</td><td>1027</td><td>72</td><td>1.7</td><td>36</td></tr>
    <tr><td>103</td><td>Late Pallava Empire</td><td>283</td><td>805</td><td>72</td><td>1.8</td><td>13</td></tr>
    <tr><td>104</td><td>Republic of Kenya</td><td>1963</td><td></td><td>72</td><td>1.9</td><td>58</td></tr>
    <tr><td>105</td><td>Austrian Empire</td><td>1806</td><td>1867</td><td>71</td><td>1.8</td><td>41</td></tr>
    <tr><td>106</td><td>Harsha&#39;s Empire</td><td>612</td><td>655</td><td>70</td><td>1.7</td><td>47</td></tr>
    <tr><td>107</td><td>Magadha - Shaishunaga dynasty</td><td>404 BCE</td><td>334 BCE</td><td>69</td><td>1.7</td><td>24</td></tr>
    <tr><td>108</td><td>Jaunpur Sultanate</td><td>1395</td><td>1481</td><td>69</td><td>1.7</td><td>20</td></tr>
    <tr><td>109</td><td>Ethiopian Empire</td><td>1272</td><td>1935</td><td>68</td><td>1.5</td><td>16</td></tr>
    <tr><td>110</td><td>Eastern Ganga Kingdom</td><td>1056</td><td>1351</td><td>68</td><td>1.7</td><td>6.7</td></tr>
    <tr><td>111</td><td>Kingdom of Hungary</td><td>1000</td><td>1546</td><td>68</td><td>1.6</td><td>7.2</td></tr>
    <tr><td>112</td><td>New Kingdom of Egypt</td><td>1500 BCE</td><td>801 BCE</td><td>67</td><td>1.6</td><td>2.9</td></tr>
    <tr><td>113</td><td>Republic of Peru</td><td>1822</td><td></td><td>67</td><td>2.0</td><td>32</td></tr>
    <tr><td>114</td><td>Pandya Dynasty</td><td>592</td><td>921</td><td>67</td><td>1.6</td><td>5.2</td></tr>
    <tr><td>115</td><td>Bijapur Sultanate</td><td>1492</td><td>1686</td><td>66</td><td>1.6</td><td>19</td></tr>
    <tr><td>116</td><td>Islamic Republic of Iran</td><td>1979</td><td></td><td>66</td><td>3.1</td><td>85</td></tr>
    <tr><td>117</td><td>Republic of Uganda</td><td>1963</td><td></td><td>66</td><td>1.5</td><td>52</td></tr>
    <tr><td>118</td><td>Paramara Dynasty</td><td>980</td><td>1235</td><td>66</td><td>1.6</td><td>6.6</td></tr>
    <tr><td>119</td><td>French Fifth Republic</td><td>1958</td><td></td><td>65</td><td>4.3</td><td>100</td></tr>
    <tr><td>120</td><td>Fatimid Caliphate</td><td>911</td><td>1176</td><td>64</td><td>1.5</td><td>9.9</td></tr>
    <tr><td>121</td><td>Safavid Dynasty</td><td>1502</td><td>1737</td><td>63</td><td>1.5</td><td>8.1</td></tr>
    <tr><td>122</td><td>Papal States</td><td>755</td><td>1870</td><td>62</td><td>1.6</td><td>4.3</td></tr>
    <tr><td>123</td><td>Qajar Dynasty</td><td>1788</td><td>1923</td><td>62</td><td>1.3</td><td>34</td></tr>
    <tr><td>124</td><td>Kamarupa Kingdom</td><td>353</td><td>1138</td><td>62</td><td>1.5</td><td>4.5</td></tr>
    <tr><td>125</td><td>Sui Dynasty</td><td>587</td><td>627</td><td>61</td><td>1.5</td><td>42</td></tr>
    <tr><td>126</td><td>Durrani Empire</td><td>1748</td><td>1827</td><td>60</td><td>1.3</td><td>32</td></tr>
    <tr><td>127</td><td>Kanva Dynasty</td><td>66 BCE</td><td>28 BCE</td><td>60</td><td>1.4</td><td>38</td></tr>
    <tr><td>128</td><td>West/Reunified Germany</td><td>1950</td><td></td><td>59</td><td>5.3</td><td>85</td></tr>
    <tr><td>129</td><td>French Third Republic</td><td>1870</td><td>1939</td><td>58</td><td>2.8</td><td>45</td></tr>
    <tr><td>130</td><td>Lodi Dynasty</td><td>1453</td><td>1528</td><td>58</td><td>1.4</td><td>32</td></tr>
    <tr><td>131</td><td>Liao Dynasty</td><td>911</td><td>1125</td><td>58</td><td>1.4</td><td>11</td></tr>
    <tr><td>132</td><td>Indo-Scythians</td><td>144 BCE</td><td>282</td><td>58</td><td>1.4</td><td>13</td></tr>
    <tr><td>133</td><td>Great Seljuk Empire</td><td>1040</td><td>1201</td><td>57</td><td>1.4</td><td>15</td></tr>
    <tr><td>134</td><td>Tsardom of Russia</td><td>1547</td><td>1720</td><td>56</td><td>1.3</td><td>14</td></tr>
    <tr><td>135</td><td>Chandela Kingdom</td><td>960</td><td>1313</td><td>56</td><td>1.3</td><td>4.2</td></tr>
    <tr><td>136</td><td>Kingdom of Portugal</td><td>1147</td><td>1911</td><td>56</td><td>1.5</td><td>12</td></tr>
    <tr><td>137</td><td>Kakatiya Dynasty</td><td>1177</td><td>1325</td><td>55</td><td>1.3</td><td>11</td></tr>
    <tr><td>138</td><td>Ptolemaic Kingdom</td><td>331 BCE</td><td>28 BCE</td><td>55</td><td>1.3</td><td>17</td></tr>
    <tr><td>139</td><td>Argentine Republic</td><td>1930</td><td></td><td>55</td><td>2.6</td><td>44</td></tr>
    <tr><td>140</td><td>Republic of Korea</td><td>1948</td><td></td><td>54</td><td>3.0</td><td>50</td></tr>
    <tr><td>141</td><td>Nawab of Awadh</td><td>1727</td><td>1802</td><td>54</td><td>1.3</td><td>21</td></tr>
    <tr><td>142</td><td>Pandya Empire</td><td>1216</td><td>1325</td><td>53</td><td>1.3</td><td>15</td></tr>
    <tr><td>143</td><td>Kannauj-Varman Dynasty</td><td>732</td><td>771</td><td>53</td><td>1.3</td><td>33</td></tr>
    <tr><td>144</td><td>Chaulukya Dynasty</td><td>947</td><td>1249</td><td>53</td><td>1.3</td><td>4.7</td></tr>
    <tr><td>145</td><td>Russian Federation</td><td>1992</td><td></td><td>52</td><td>4.9</td><td>150</td></tr>
    <tr><td>146</td><td>Republic of Italy</td><td>1946</td><td></td><td>52</td><td>4.2</td><td>58</td></tr>
    <tr><td>147</td><td>Zhou Dynasty</td><td>1000 BCE</td><td>751 BCE</td><td>52</td><td>1.2</td><td>5.9</td></tr>
    <tr><td>148</td><td>Seleucid Empire</td><td>318 BCE</td><td>64 BCE</td><td>51</td><td>1.2</td><td>9.9</td></tr>
    <tr><td>149</td><td>Pahlavi Dynasty</td><td>1924</td><td>1978</td><td>51</td><td>1.1</td><td>36</td></tr>
    <tr><td>150</td><td>Sokoto Caliphate</td><td>1805</td><td>1904</td><td>50</td><td>1.1</td><td>13</td></tr>
    <tr><td>151</td><td>People&#39;s Democratic Republic of Algeria</td><td>1963</td><td></td><td>50</td><td>1.7</td><td>44</td></tr>
    <tr><td>152</td><td>Golden Horde</td><td>1294</td><td>1695</td><td>49</td><td>1.2</td><td>7.0</td></tr>
    <tr><td>153</td><td>Liu Song Dynasty</td><td>426</td><td>479</td><td>49</td><td>1.2</td><td>25</td></tr>
    <tr><td>154</td><td>Venezuela</td><td>1834</td><td></td><td>49</td><td>1.7</td><td>35</td></tr>
    <tr><td>155</td><td>Western Roman Empire</td><td>395</td><td>475</td><td>48</td><td>1.2</td><td>21</td></tr>
    <tr><td>156</td><td>Crown of Castile</td><td>1236</td><td>1515</td><td>48</td><td>1.2</td><td>6.1</td></tr>
    <tr><td>157</td><td>Dutch Republic</td><td>1582</td><td>1795</td><td>48</td><td>1.2</td><td>11</td></tr>
    <tr><td>158</td><td>Greek City-States</td><td>800 BCE</td><td>83</td><td>48</td><td>1.1</td><td>2.7</td></tr>
    <tr><td>159</td><td>Ashikaga Shogunate</td><td>1344</td><td>1571</td><td>47</td><td>1.1</td><td>11</td></tr>
    <tr><td>160</td><td>Liang Dynasty</td><td>510</td><td>560</td><td>47</td><td>1.1</td><td>23</td></tr>
    <tr><td>161</td><td>Iberian Union</td><td>1582</td><td>1639</td><td>47</td><td>1.2</td><td>20</td></tr>
    <tr><td>162</td><td>Maitraka Dynasty</td><td>476</td><td>731</td><td>45</td><td>1.1</td><td>7.3</td></tr>
    <tr><td>163</td><td>Kadamba Empire</td><td>353</td><td>554</td><td>45</td><td>1.1</td><td>5.7</td></tr>
    <tr><td>164</td><td>Xin Dynasty</td><td>6</td><td>29</td><td>44</td><td>1.1</td><td>50</td></tr>
    <tr><td>165</td><td>Zaire</td><td>1960</td><td>1995</td><td>44</td><td>0.94</td><td>42</td></tr>
    <tr><td>166</td><td>Eastern Kushans</td><td>238</td><td>346</td><td>43</td><td>1.0</td><td>27</td></tr>
    <tr><td>167</td><td>Indus Valley Civilization</td><td>3000 BCE</td><td>1701 BCE</td><td>43</td><td>1.0</td><td>2.2</td></tr>
    <tr><td>168</td><td>People&#39;s Republic of Angola</td><td>1976</td><td></td><td>43</td><td>0.97</td><td>35</td></tr>
    <tr><td>169</td><td>Mozambique</td><td>1976</td><td></td><td>43</td><td>1.0</td><td>32</td></tr>
    <tr><td>170</td><td>Estado Novo</td><td>1926</td><td>1975</td><td>42</td><td>1.1</td><td>29</td></tr>
    <tr><td>171</td><td>Iraq</td><td>1960</td><td></td><td>42</td><td>1.2</td><td>45</td></tr>
    <tr><td>172</td><td>Ghana</td><td>1958</td><td></td><td>42</td><td>1.2</td><td>33</td></tr>
    <tr><td>173</td><td>Northern Wei</td><td>387</td><td>533</td><td>42</td><td>1.0</td><td>12</td></tr>
    <tr><td>174</td><td>Timurid Empire</td><td>1375</td><td>1506</td><td>42</td><td>1.0</td><td>21</td></tr>
    <tr><td>175</td><td>Carnatic Sultanate</td><td>1713</td><td>1802</td><td>41</td><td>0.99</td><td>15</td></tr>
    <tr><td>176</td><td>Golconda Sultanate</td><td>1519</td><td>1686</td><td>41</td><td>0.99</td><td>8.3</td></tr>
    <tr><td>177</td><td>Neo-Assyrian Empire</td><td>900 BCE</td><td>601 BCE</td><td>41</td><td>0.97</td><td>7.8</td></tr>
    <tr><td>178</td><td>Kamakura Shogunate</td><td>1188</td><td>1332</td><td>40</td><td>0.96</td><td>7.5</td></tr>
    <tr><td>179</td><td>Sunda Kingdom</td><td>674</td><td>1578</td><td>40</td><td>0.94</td><td>1.9</td></tr>
    <tr><td>180</td><td>Early Cholas</td><td>291 BCE</td><td>305</td><td>40</td><td>0.97</td><td>1.9</td></tr>
    <tr><td>181</td><td>Hyderabad State</td><td>1727</td><td>1947</td><td>39</td><td>0.94</td><td>21</td></tr>
    <tr><td>182</td><td>Goryeo</td><td>922</td><td>1394</td><td>39</td><td>0.93</td><td>3.4</td></tr>
    <tr><td>183</td><td>Republic of Poland</td><td>1953</td><td></td><td>39</td><td>2.6</td><td>39</td></tr>
    <tr><td>184</td><td>Republic of Cameroon</td><td>1960</td><td></td><td>39</td><td>0.96</td><td>28</td></tr>
    <tr><td>185</td><td>Belgian Congo</td><td>1890</td><td>1962</td><td>39</td><td>0.87</td><td>21</td></tr>
    <tr><td>186</td><td>Visigothic Kingdom</td><td>426</td><td>723</td><td>39</td><td>0.92</td><td>4.9</td></tr>
    <tr><td>187</td><td>First Toungoo Empire</td><td>1502</td><td>1761</td><td>38</td><td>0.91</td><td>7.6</td></tr>
    <tr><td>188</td><td>Republic of C&#244;te d&#39;Ivoire</td><td>1961</td><td></td><td>38</td><td>0.90</td><td>25</td></tr>
    <tr><td>189</td><td>Indo-Greeks</td><td>126 BCE</td><td>237</td><td>38</td><td>0.91</td><td>8.5</td></tr>
    <tr><td>190</td><td>Rattanakosin Kingdom</td><td>1783</td><td>1931</td><td>37</td><td>0.85</td><td>13</td></tr>
    <tr><td>191</td><td>Himyarite Kingdom</td><td>110 BCE</td><td>601</td><td>37</td><td>0.88</td><td>2.4</td></tr>
    <tr><td>192</td><td>Republic of the Niger</td><td>1961</td><td></td><td>37</td><td>0.74</td><td>26</td></tr>
    <tr><td>193</td><td>Nayaks of Madurai</td><td>1529</td><td>1737</td><td>37</td><td>0.88</td><td>5.1</td></tr>
    <tr><td>194</td><td>White Huns</td><td>410</td><td>560</td><td>37</td><td>0.88</td><td>14</td></tr>
    <tr><td>195</td><td>Netherlands</td><td>1815</td><td></td><td>36</td><td>1.8</td><td>18</td></tr>
    <tr><td>196</td><td>Kingdom of Saudi Arabia</td><td>1936</td><td></td><td>36</td><td>1.3</td><td>38</td></tr>
    <tr><td>197</td><td>Afghanistan</td><td>1979</td><td></td><td>36</td><td>0.90</td><td>46</td></tr>
    <tr><td>198</td><td>German Confederation</td><td>1815</td><td>1863</td><td>36</td><td>0.90</td><td>22</td></tr>
    <tr><td>199</td><td>Republic of Venice</td><td>705</td><td>1796</td><td>36</td><td>0.88</td><td>2.9</td></tr>
    <tr><td>200</td><td>Madagascar</td><td>1960</td><td></td><td>35</td><td>0.92</td><td>28</td></tr>
    <tr><td>201</td><td>Swiss Confederation</td><td>1294</td><td></td><td>35</td><td>1.4</td><td>8.6</td></tr>
    <tr><td>202</td><td>Kingdom of Mysore</td><td>1572</td><td>1799</td><td>35</td><td>0.84</td><td>6.8</td></tr>
    <tr><td>203</td><td>Qi</td><td>750 BCE</td><td>204 BCE</td><td>35</td><td>0.83</td><td>2.8</td></tr>
    <tr><td>204</td><td>Kingdom of Bohemia</td><td>1202</td><td>1528</td><td>35</td><td>0.83</td><td>3.8</td></tr>
    <tr><td>205</td><td>Mali</td><td>1960</td><td></td><td>34</td><td>0.75</td><td>23</td></tr>
    <tr><td>206</td><td>Magadha - Haryanka dynasty</td><td>500 BCE</td><td>405 BCE</td><td>33</td><td>0.80</td><td>14</td></tr>
    <tr><td>207</td><td>Republic of Chile</td><td>1812</td><td></td><td>33</td><td>1.3</td><td>19</td></tr>
    <tr><td>208</td><td>Early Cheras</td><td>291 BCE</td><td>305</td><td>33</td><td>0.80</td><td>1.6</td></tr>
    <tr><td>209</td><td>Hoysala Kingdom</td><td>1111</td><td>1351</td><td>33</td><td>0.81</td><td>4.1</td></tr>
    <tr><td>210</td><td>Early Pandyas</td><td>291 BCE</td><td>305</td><td>33</td><td>0.78</td><td>1.5</td></tr>
    <tr><td>211</td><td>Burkina Faso</td><td>1961</td><td></td><td>33</td><td>0.76</td><td>24</td></tr>
    <tr><td>212</td><td>Wu</td><td>750 BCE</td><td>451 BCE</td><td>32</td><td>0.78</td><td>3.3</td></tr>
    <tr><td>213</td><td>Canada</td><td>1932</td><td></td><td>32</td><td>2.1</td><td>36</td></tr>
    <tr><td>214</td><td>Guatemala</td><td>1840</td><td></td><td>32</td><td>0.90</td><td>19</td></tr>
    <tr><td>215</td><td>Democratic People&#39;s Republic of Korea</td><td>1948</td><td></td><td>32</td><td>1.5</td><td>27</td></tr>
    <tr><td>216</td><td>Majapahit</td><td>1294</td><td>1518</td><td>32</td><td>0.75</td><td>4.4</td></tr>
    <tr><td>217</td><td>Gorkha Kingdom</td><td>1588</td><td>1787</td><td>31</td><td>0.75</td><td>4.5</td></tr>
    <tr><td>218</td><td>Malaysia</td><td>1963</td><td></td><td>31</td><td>1.4</td><td>37</td></tr>
    <tr><td>219</td><td>Sind-Habbari Dynasty</td><td>860</td><td>1201</td><td>31</td><td>0.73</td><td>2.3</td></tr>
    <tr><td>220</td><td>Kingdom of Belgium</td><td>1830</td><td></td><td>30</td><td>1.6</td><td>13</td></tr>
    <tr><td>221</td><td>Ayutthaya Kingdom</td><td>1352</td><td>1768</td><td>30</td><td>0.72</td><td>2.6</td></tr>
    <tr><td>222</td><td>Kazakh Khanate</td><td>1468</td><td>1847</td><td>30</td><td>0.70</td><td>2.9</td></tr>
    <tr><td>223</td><td>Republic of Yemen</td><td>1990</td><td></td><td>30</td><td>0.83</td><td>35</td></tr>
    <tr><td>224</td><td>Xiongnu</td><td>208 BCE</td><td>153</td><td>30</td><td>0.71</td><td>6.4</td></tr>
    <tr><td>225</td><td>Funj Sultanate</td><td>1507</td><td>1821</td><td>29</td><td>0.67</td><td>2.4</td></tr>
    <tr><td>226</td><td>Almohad Caliphate</td><td>1139</td><td>1343</td><td>29</td><td>0.70</td><td>6.6</td></tr>
    <tr><td>227</td><td>Nazi Germany</td><td>1936</td><td>1944</td><td>29</td><td>1.4</td><td>250</td></tr>
    <tr><td>228</td><td>Eastern Wu</td><td>207</td><td>282</td><td>29</td><td>0.69</td><td>12</td></tr>
    <tr><td>229</td><td>Qin</td><td>750 BCE</td><td>219 BCE</td><td>29</td><td>0.69</td><td>20</td></tr>
    <tr><td>230</td><td>Republic of Ecuador</td><td>1834</td><td></td><td>29</td><td>0.92</td><td>17</td></tr>
    <tr><td>231</td><td>Mongol Khanate</td><td>1468</td><td>1635</td><td>29</td><td>0.69</td><td>7.0</td></tr>
    <tr><td>232</td><td>Carthage</td><td>650 BCE</td><td>145 BCE</td><td>28</td><td>0.67</td><td>5.1</td></tr>
    <tr><td>233</td><td>Bolivia</td><td>1825</td><td></td><td>28</td><td>0.78</td><td>12</td></tr>
    <tr><td>234</td><td>Malawi</td><td>1967</td><td></td><td>28</td><td>0.66</td><td>22</td></tr>
    <tr><td>235</td><td>House of Jagiellon</td><td>1450</td><td>1652</td><td>28</td><td>0.67</td><td>5.8</td></tr>
    <tr><td>236</td><td>West Franks</td><td>850</td><td>989</td><td>28</td><td>0.67</td><td>12</td></tr>
    <tr><td>237</td><td>Mayan City-States</td><td>247 BCE</td><td>849</td><td>28</td><td>0.66</td><td>1.2</td></tr>
    <tr><td>238</td><td>Sri Lanka</td><td>1948</td><td></td><td>28</td><td>1.2</td><td>23</td></tr>
    <tr><td>239</td><td>Crown of Aragon</td><td>1169</td><td>1515</td><td>27</td><td>0.68</td><td>5.0</td></tr>
    <tr><td>240</td><td>Anur&#257;dhapura</td><td>291 BCE</td><td>1017</td><td>27</td><td>0.65</td><td>0.82</td></tr>
    <tr><td>241</td><td>Kashmir</td><td>626</td><td>1343</td><td>27</td><td>0.66</td><td>1.7</td></tr>
    <tr><td>242</td><td>Restoration France</td><td>1815</td><td>1847</td><td>27</td><td>1.1</td><td>36</td></tr>
    <tr><td>243</td><td>Kingdom of Prussia</td><td>1702</td><td>1863</td><td>27</td><td>0.66</td><td>14</td></tr>
    <tr><td>244</td><td>Shang Dynasty</td><td>1600 BCE</td><td>1001 BCE</td><td>27</td><td>0.64</td><td>1.1</td></tr>
    <tr><td>245</td><td>Southern Ming</td><td>1645</td><td>1682</td><td>27</td><td>0.65</td><td>46</td></tr>
    <tr><td>246</td><td>Chauhan Dynasty</td><td>980</td><td>1201</td><td>26</td><td>0.64</td><td>4.8</td></tr>
    <tr><td>247</td><td>Middle Kingdom of Egypt</td><td>2000 BCE</td><td>1601 BCE</td><td>26</td><td>0.63</td><td>1.7</td></tr>
    <tr><td>248</td><td>Republic of Chad</td><td>1961</td><td></td><td>26</td><td>0.56</td><td>18</td></tr>
    <tr><td>249</td><td>Empire of Brazil</td><td>1822</td><td>1889</td><td>26</td><td>0.60</td><td>14</td></tr>
    <tr><td>250</td><td>Communist Party of China</td><td>1932</td><td>1949</td><td>26</td><td>0.66</td><td>280</td></tr>
    <tr><td>251</td><td>Southern Qi</td><td>480</td><td>509</td><td>26</td><td>0.62</td><td>22</td></tr>
    <tr><td>252</td><td>Assyria</td><td>1800 BCE</td><td>901 BCE</td><td>26</td><td>0.61</td><td>2.3</td></tr>
    <tr><td>253</td><td>Oyo Empire</td><td>1609</td><td>1835</td><td>26</td><td>0.60</td><td>5.2</td></tr>
    <tr><td>254</td><td>Ayyubid Sultanate</td><td>1177</td><td>1249</td><td>26</td><td>0.61</td><td>9.8</td></tr>
    <tr><td>255</td><td>Kingdom of Dali</td><td>947</td><td>1259</td><td>25</td><td>0.61</td><td>2.7</td></tr>
    <tr><td>256</td><td>Republic of China (Taiwan)</td><td>1950</td><td></td><td>25</td><td>1.4</td><td>23</td></tr>
    <tr><td>257</td><td>Pagan Kingdom</td><td>850</td><td>1293</td><td>25</td><td>0.59</td><td>2.5</td></tr>
    <tr><td>258</td><td>Zambia</td><td>1967</td><td></td><td>25</td><td>0.59</td><td>19</td></tr>
    <tr><td>259</td><td>Minyue</td><td>333 BCE</td><td>111 BCE</td><td>25</td><td>0.59</td><td>5.2</td></tr>
    <tr><td>260</td><td>Goguryeo</td><td>36 BCE</td><td>681</td><td>25</td><td>0.59</td><td>2.0</td></tr>
    <tr><td>261</td><td>Sikh Empire</td><td>1799</td><td>1848</td><td>25</td><td>0.55</td><td>17</td></tr>
    <tr><td>262</td><td>Kingdom of Armenia</td><td>326 BCE</td><td>646</td><td>24</td><td>0.58</td><td>3.7</td></tr>
    <tr><td>263</td><td>Ghurid Dynasty</td><td>1152</td><td>1209</td><td>24</td><td>0.59</td><td>45</td></tr>
    <tr><td>264</td><td>Duchy of Bavaria</td><td>1260</td><td>1805</td><td>24</td><td>0.60</td><td>3.9</td></tr>
    <tr><td>265</td><td>Republic of Senegal</td><td>1961</td><td></td><td>24</td><td>0.62</td><td>18</td></tr>
    <tr><td>266</td><td>Federal Republic of Somalia</td><td>1960</td><td></td><td>24</td><td>0.52</td><td>13</td></tr>
    <tr><td>267</td><td>Francoist Spain</td><td>1939</td><td>1975</td><td>24</td><td>1.1</td><td>35</td></tr>
    <tr><td>268</td><td>House of Habsburg</td><td>1260</td><td>1515</td><td>24</td><td>0.58</td><td>8.7</td></tr>
    <tr><td>269</td><td>Kingdom of Sweden</td><td>980</td><td></td><td>24</td><td>1.2</td><td>10</td></tr>
    <tr><td>270</td><td>Babylonia</td><td>1800 BCE</td><td>601 BCE</td><td>24</td><td>0.57</td><td>0.85</td></tr>
    <tr><td>271</td><td>Emirate of Afghanistan</td><td>1828</td><td>1925</td><td>23</td><td>0.49</td><td>6.7</td></tr>
    <tr><td>272</td><td>Kingdom of Poland</td><td>962</td><td>1449</td><td>23</td><td>0.55</td><td>3.0</td></tr>
    <tr><td>273</td><td>Xianbei</td><td>60</td><td>237</td><td>23</td><td>0.55</td><td>3.8</td></tr>
    <tr><td>274</td><td>Syria</td><td>1973</td><td></td><td>23</td><td>0.75</td><td>22</td></tr>
    <tr><td>275</td><td>Early Dynastic Period of Egypt</td><td>3000 BCE</td><td>2501 BCE</td><td>23</td><td>0.54</td><td>1.2</td></tr>
    <tr><td>276</td><td>Ilkhanate</td><td>1294</td><td>1343</td><td>22</td><td>0.53</td><td>12</td></tr>
    <tr><td>277</td><td>Republic of Uzbekistan</td><td>1992</td><td></td><td>22</td><td>0.94</td><td>32</td></tr>
    <tr><td>278</td><td>Samanid Empire</td><td>886</td><td>999</td><td>22</td><td>0.53</td><td>6.6</td></tr>
    <tr><td>279</td><td>Republic of Rwanda</td><td>1963</td><td></td><td>22</td><td>0.56</td><td>17</td></tr>
    <tr><td>280</td><td>Denmark-Norway</td><td>1526</td><td>1813</td><td>21</td><td>0.57</td><td>2.7</td></tr>
    <tr><td>281</td><td>Weimar Republic</td><td>1920</td><td>1935</td><td>21</td><td>1.1</td><td>79</td></tr>
    <tr><td>282</td><td>Nanda Empire</td><td>333 BCE</td><td>319 BCE</td><td>21</td><td>0.51</td><td>34</td></tr>
    <tr><td>283</td><td>Ahmadnagar Sultanate</td><td>1492</td><td>1652</td><td>21</td><td>0.52</td><td>5.8</td></tr>
    <tr><td>284</td><td>Hafsid Dynasty</td><td>1236</td><td>1571</td><td>21</td><td>0.50</td><td>1.7</td></tr>
    <tr><td>285</td><td>Cao Wei</td><td>224</td><td>264</td><td>21</td><td>0.50</td><td>15</td></tr>
    <tr><td>286</td><td>Principality of Wallachia</td><td>1314</td><td>1858</td><td>21</td><td>0.53</td><td>3.3</td></tr>
    <tr><td>287</td><td>Yue</td><td>500 BCE</td><td>334 BCE</td><td>21</td><td>0.50</td><td>3.8</td></tr>
    <tr><td>288</td><td>Guinea</td><td>1960</td><td></td><td>21</td><td>0.51</td><td>13</td></tr>
    <tr><td>289</td><td>Vietnam</td><td>1791</td><td>1884</td><td>21</td><td>0.61</td><td>9.5</td></tr>
    <tr><td>290</td><td>Republic of Burundi</td><td>1963</td><td></td><td>21</td><td>0.48</td><td>15</td></tr>
    <tr><td>291</td><td>Turk Shahis</td><td>561</td><td>874</td><td>21</td><td>0.49</td><td>1.9</td></tr>
    <tr><td>292</td><td>Kimek-Kipchak confederation</td><td>750</td><td>1235</td><td>21</td><td>0.49</td><td>2.2</td></tr>
    <tr><td>293</td><td>Rashidun Caliphate</td><td>633</td><td>665</td><td>20</td><td>0.49</td><td>20</td></tr>
    <tr><td>294</td><td>Kingdom of Afghanistan</td><td>1926</td><td>1972</td><td>20</td><td>0.40</td><td>13</td></tr>
    <tr><td>295</td><td>Tibet</td><td>1363</td><td>1952</td><td>20</td><td>0.49</td><td>2.5</td></tr>
    <tr><td>296</td><td>Rasulid Dynasty</td><td>1236</td><td>1458</td><td>20</td><td>0.47</td><td>2.2</td></tr>
    <tr><td>297</td><td>Commonwealth of Australia</td><td>1943</td><td></td><td>20</td><td>1.3</td><td>26</td></tr>
    <tr><td>298</td><td>Republic of Haiti</td><td>1936</td><td></td><td>20</td><td>0.59</td><td>12</td></tr>
    <tr><td>299</td><td>Aztec Triple Alliance</td><td>1429</td><td>1520</td><td>20</td><td>0.47</td><td>8.2</td></tr>
    <tr><td>300</td><td>Kingdom of Sicily</td><td>1139</td><td>1384</td><td>20</td><td>0.48</td><td>3.7</td></tr>
  </tbody>
</table>
</div>

The Qing dynasty is the most populous state by births. Its 2.5 billion total births represent around 4% of all humans who ever lived, followed by the Republic of India and the People's Republic of China. More broadly, China and South Asia dominate the top 15, with seven entries each. The Roman Empire, in 7th place, is the largest polity outside these two regions, followed by the Russian Empire (9th) and the USA (11th).

If we sort by person-years, the rankings change considerably. Longer modern life expectancies mean more person-years per birth, which shifts the list in favour of more recent and more developed polities. The PRC moves into first place and India into second, while the Qing dynasty drops to third. The British Raj remains in 4th, just edging out the USA despite having twice as many births. 

Sorting by peak population puts the Republic of India on top. Its current population of 1.5 billion is the largest of any polity in world history, with the PRC in second. In third place, curiously, is the Empire of Japan, which at its peak wartime extent covered large swathes of East and Southeast Asia.

The top 10 polities account for just 18% of all people who ever lived. The median person was born in a state ranked 187th, the First Toungoo Empire, which at its peak in the 16th century was the dominant power in Southeast Asia with 8 million people. The top 300 polities together account for only 55% of all births, and the remaining 1,214 polities in the Cliopatria dataset add just 7% more. The remaining 38% were born in states too ancient or too poorly defined for Cliopatria to map, or pre-state hunter-gatherer and farming communities. 

## Dynastic Power

The main table splits polities that shared a ruling family. The House of Hanover and its descendants ruled Britain, the Raj, and dozens of colonial possessions that appear as separate entries above. If we group by dynasty instead, which families come out on top?

<div id="dynasty-table-wrapper">
<table class="data-table" id="dynasty-table">
  <thead>
    <tr>
      <th>Rank</th>
      <th class="sortable" data-col="1" data-table="dynasty-table" data-sort="text">Dynasty</th>
      <th class="sortable" data-col="2" data-table="dynasty-table" data-sort="year">From</th>
      <th class="sortable" data-col="3" data-table="dynasty-table" data-sort="year">To</th>
      <th class="sortable" data-col="4" data-table="dynasty-table">Births (M)</th>
      <th class="sortable" data-col="5" data-table="dynasty-table">Person-years (B)</th>
      <th class="sortable" data-col="6" data-table="dynasty-table">Peak pop (M)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Hanover / Windsor</td><td>1709</td><td></td><td>2,800</td><td>72</td><td>670</td></tr>
    <tr><td>2</td><td>Qing (Aisin-Gioro)</td><td>1645</td><td>1911</td><td>2,500</td><td>65</td><td>430</td></tr>
    <tr><td>3</td><td>Timurid (incl. Mughal)</td><td>1375</td><td>1858</td><td>1,000</td><td>24</td><td>180</td></tr>
    <tr><td>4</td><td>Ming (Zhu)</td><td>1375</td><td>1644</td><td>900</td><td>22</td><td>87</td></tr>
    <tr><td>5</td><td>Japanese Imperial House</td><td>540</td><td></td><td>810</td><td>28</td><td>520</td></tr>
    <tr><td>6</td><td>Romanov</td><td>1613</td><td>1916</td><td>710</td><td>15</td><td>200</td></tr>
    <tr><td>7</td><td>Genghisid (Borjigin)</td><td>1206</td><td>1847</td><td>680</td><td>16</td><td>120</td></tr>
    <tr><td>8</td><td>Han (Liu)</td><td>202 BCE</td><td>237</td><td>670</td><td>16</td><td>51</td></tr>
    <tr><td>9</td><td>Song (Zhao)</td><td>961</td><td>1278</td><td>630</td><td>15</td><td>74</td></tr>
    <tr><td>10</td><td>Capetian (all branches)</td><td>990</td><td></td><td>570</td><td>17</td><td>67</td></tr>
    <tr><td>11</td><td>Habsburg</td><td>1260</td><td>1918</td><td>550</td><td>14</td><td>63</td></tr>
    <tr><td>12</td><td>Gupta</td><td>324</td><td>554</td><td>500</td><td>12</td><td>69</td></tr>
    <tr><td>13</td><td>Ottoman (Osman)</td><td>1305</td><td>1923</td><td>470</td><td>11</td><td>32</td></tr>
    <tr><td>14</td><td>Tang (Li)</td><td>623</td><td>910</td><td>380</td><td>9.3</td><td>40</td></tr>
    <tr><td>15</td><td>Maurya</td><td>318 BCE</td><td>171 BCE</td><td>300</td><td>7.1</td><td>67</td></tr>
  </tbody>
</table>
</div>

The House of Hanover and its descendants take first place by births, with 2.8 billion people born under their rule—largely due to the British Empire's dominion over India during the 19th and 20th centuries. By this point the British monarchy had long since ceded real power to Parliament; it's less a story of personal dynastic achievement and more happening to sit on a throne without annoying anyone to the point of decapitation.

The Qing (Aisin-Gioro) are a close second at 2.5 billion births, and actually edge ahead by person-years. Unlike the British monarchs, the Qing emperors wielded genuine power for much of their dynasty's 266-year run. Third are the Timurids, a single Central Asian family whose domains stretched from Timur's 14th-century conquests through to the Mughal Empire. Timur himself descended from Genghis Khan matrilineally; the Genghisids themselves only make it to 7th place despite a longer dynastic run.

Fourth place goes to the Ming (Zhu), the dynasty immediately prior to the Qing. The Japanese Imperial House comes fifth, despite—or perhaps because of—having held no real power for the past 800 years.

How many people have lived under a monarchy at all? Classifying each Cliopatria polity as monarchical or not, about 45% of all people who ever lived were born under a monarch of some kind, compared to just 17% under republics or other non-monarchical states; the remaining 38% lived outside any recorded state.

## Age of Empires

The main table treats colonies as separate polities. How large were the European colonial empires when we add their overseas possessions back together?

<div id="colonial-table-wrapper">
<table class="data-table" id="colonial-table">
  <thead>
    <tr>
      <th>Empire</th>
      <th>From</th>
      <th>To</th>
      <th style="text-align:right">Births (M)</th>
      <th style="text-align:right">Person-years (B)</th>
      <th style="text-align:right">Peak pop (M)</th>
      <th style="text-align:right">% colonial (births)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>British</td><td>1600</td><td>1997</td><td style="text-align:right">2,600</td><td style="text-align:right">63</td><td style="text-align:right">640</td><td style="text-align:right">88%</td></tr>
    <tr><td>Russian</td><td>1721</td><td>1916</td><td style="text-align:right">670</td><td style="text-align:right">14</td><td style="text-align:right">200</td><td style="text-align:right">—</td></tr>
    <tr><td>French</td><td>1600</td><td>1960</td><td style="text-align:right">520</td><td style="text-align:right">16</td><td style="text-align:right">150</td><td style="text-align:right">43%</td></tr>
    <tr><td>Spanish</td><td>1516</td><td>1898</td><td style="text-align:right">410</td><td style="text-align:right">10</td><td style="text-align:right">36</td><td style="text-align:right">53%</td></tr>
    <tr><td>Japanese</td><td>1868</td><td>1945</td><td style="text-align:right">270</td><td style="text-align:right">7.8</td><td style="text-align:right">520</td><td style="text-align:right">—</td></tr>
    <tr><td>Dutch</td><td>1600</td><td>1949</td><td style="text-align:right">250</td><td style="text-align:right">6.1</td><td style="text-align:right">77</td><td style="text-align:right">70%</td></tr>
    <tr><td>Portuguese</td><td>1500</td><td>1975</td><td style="text-align:right">130</td><td style="text-align:right">3.4</td><td style="text-align:right">29</td><td style="text-align:right">—</td></tr>
    <tr><td>German</td><td>1871</td><td>1919</td><td style="text-align:right">120</td><td style="text-align:right">3.6</td><td style="text-align:right">130</td><td style="text-align:right">8%</td></tr>
    <tr><td>Italian</td><td>1861</td><td>1945</td><td style="text-align:right">92</td><td style="text-align:right">2.9</td><td style="text-align:right">65</td><td style="text-align:right">10%</td></tr>
    <tr><td>Belgian</td><td>1890</td><td>1962</td><td style="text-align:right">51</td><td style="text-align:right">1.4</td><td style="text-align:right">31</td><td style="text-align:right">77%</td></tr>
  </tbody>
</table>
</div>

The British Empire dwarfs all the others. Its 2.6 billion births roughly equal every other empire in the table combined. This dominance is largely due to British India: about 78% of those births were in South Asia, and only 10% in the British Isles themselves.

Russia ranks second by births, though the metropole/colonial distinction breaks down for a contiguous land empire. France, Britain's perennial rival, comes third. While they acquired vast territories in West Africa and Indochina, the majority of births were in metropolitan France itself (excluding Algeria, which was legally part of France but is counted as colonial here).

The Spanish and Portuguese arrived in the Americas first, but despite this head start they come in 4th and 7th, respectively. While the pre-contact population of the Americas was large, European conquest and the diseases that accompanied it led to a massive population collapse. The Spanish Empire's peak population actually came in 1540, when Charles V still controlled Naples, Sicily, and the Low Countries, and before the indigenous American population had fully collapsed. By 1600 the American population had been devastated and the European territories had passed to separate rulers; the combined total never recovered.

Japan, despite not being European, was the most successful latecomer. Within fifty years of being forcibly opened by the Americans in 1853, it had colonies in Korea, Taiwan, and Okinawa. Germany and Italy, by contrast, acquired little and soon lost all in the world wars. The Dutch and Belgian empires were each built on a single colony—the East Indies and the Congo—that dwarfed the home country in population.

## Appendix: Population Over Time

The chart below shows population over time for the top 100 polities, combining the HYDE population maps with the Cliopatria polity boundaries. All of these estimates are subject to substantial uncertainty, particularly for any pre-modern polity.

<div id="chart-mode-controls">
  <label><input type="radio" name="chart-mode" value="absolute" checked> Absolute population</label>
  <label style="margin-left:1em"><input type="radio" name="chart-mode" value="fraction"> Fraction of world population</label>
  <button id="chart-reset-zoom" class="chart-btn" style="margin-left:1.5em">Reset zoom</button>
  <span style="font-size:0.8em; color:#888; margin-left:0.5em">Scroll to zoom, drag to pan</span>
</div>
<div id="chart-wrapper">
  <canvas id="polity-chart"></canvas>
</div>
<div id="chart-selector">
  <div id="chart-selector-header">
    <button id="select-top-20" class="chart-btn">Top 20</button>
    <button id="select-none" class="chart-btn">Clear all</button>
  </div>
  <div id="region-groups"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs@2"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom@2/dist/chartjs-plugin-zoom.min.js"></script>
<script>
(function() {
  var DATA = null;
  var chart = null;
  var selectedPolities = new Set();
  var allNames = [];
  var COLORS = [
    '#e6194b','#3cb44b','#4363d8','#f58231','#911eb4',
    '#42d4f4','#f032e6','#bfef45','#fabed4','#469990',
    '#dcbeff','#9A6324','#800000','#aaffc3','#808000',
    '#000075','#a9a9a9','#e6beff','#ffe119','#ffd8b1',
    '#0082c8','#aa6e28','#7e0023','#46f0f0','#d2f53c',
    '#fabebe','#008080','#e6194B','#3cb44b','#ffe119',
    '#4363d8','#f58231','#911eb4','#42d4f4','#f032e6',
    '#bfef45','#fabed4','#469990','#dcbeff','#9A6324',
    '#800000','#aaffc3','#808000','#000075','#a9a9a9',
    '#e6beff','#ffe119','#ffd8b1','#0082c8','#aa6e28'
  ];
  // Stable color assignment by rank
  var colorMap = {};

  function getMode() { return document.querySelector('input[name="chart-mode"]:checked').value; }

  function worldPopAtYear(year) {
    var wy = DATA.world.years, wp = DATA.world.population;
    if (year <= wy[0]) return wp[0];
    if (year >= wy[wy.length-1]) return wp[wp.length-1];
    for (var i = 0; i < wy.length - 1; i++) {
      if (wy[i] <= year && year <= wy[i+1]) {
        var t = (year - wy[i]) / (wy[i+1] - wy[i]);
        return wp[i] + t * (wp[i+1] - wp[i]);
      }
    }
    return wp[0];
  }

  function buildRegionSelector() {
    var container = document.getElementById('region-groups');
    container.innerHTML = '';
    // Group polities by region
    var regionOrder = ['China','South Asia','Japan & Korea','Southeast Asia',
                       'Middle East & Central Asia','Europe','Russia','Africa','Americas','Ancient Near East','Other'];
    var regions = {};
    allNames.forEach(function(name) {
      var r = DATA.polities[name].region || 'Other';
      if (!regions[r]) regions[r] = [];
      regions[r].push(name);
    });
    regionOrder.forEach(function(region) {
      if (!regions[region] || regions[region].length === 0) return;
      var group = document.createElement('div');
      group.className = 'region-group';
      var header = document.createElement('div');
      header.className = 'region-header';
      var toggle = document.createElement('span');
      toggle.className = 'region-toggle';
      var label = document.createElement('span');
      label.textContent = region + ' (' + regions[region].length + ')';
      var selAll = document.createElement('button');
      selAll.className = 'chart-btn chart-btn-sm';
      selAll.textContent = 'All';
      var selNone = document.createElement('button');
      selNone.className = 'chart-btn chart-btn-sm';
      selNone.textContent = 'None';
      header.appendChild(toggle);
      header.appendChild(label);
      header.appendChild(selAll);
      header.appendChild(selNone);
      // Start expanded if any polities in this region are selected
      var hasSelected = regions[region].some(function(n) { return selectedPolities.has(n); });
      var list = document.createElement('div');
      list.className = 'region-list';
      list.style.display = hasSelected ? 'block' : 'none';
      toggle.textContent = hasSelected ? '▾' : '▸';
      regions[region].forEach(function(name) {
        var row = document.createElement('label');
        row.className = 'polity-checkbox';
        var cb = document.createElement('input');
        cb.type = 'checkbox';
        cb.checked = selectedPolities.has(name);
        cb.dataset.polity = name;
        var swatch = document.createElement('span');
        swatch.className = 'legend-swatch';
        swatch.style.backgroundColor = colorMap[name] || '#999';
        cb.addEventListener('change', function() {
          if (cb.checked) selectedPolities.add(name);
          else selectedPolities.delete(name);
          updateChart();
        });
        row.appendChild(cb);
        row.appendChild(swatch);
        row.appendChild(document.createTextNode(name));
        list.appendChild(row);
      });
      header.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON') return;
        var open = list.style.display !== 'none';
        list.style.display = open ? 'none' : 'block';
        toggle.textContent = open ? '▸' : '▾';
      });
      selAll.addEventListener('click', function() {
        regions[region].forEach(function(n) { selectedPolities.add(n); });
        list.querySelectorAll('input').forEach(function(cb) { cb.checked = true; });
        updateChart();
      });
      selNone.addEventListener('click', function() {
        regions[region].forEach(function(n) { selectedPolities.delete(n); });
        list.querySelectorAll('input').forEach(function(cb) { cb.checked = false; });
        updateChart();
      });
      group.appendChild(header);
      group.appendChild(list);
      container.appendChild(group);
    });
  }

  function syncCheckboxes() {
    document.querySelectorAll('#region-groups input[type="checkbox"]').forEach(function(cb) {
      cb.checked = selectedPolities.has(cb.dataset.polity);
    });
  }

  var currentMode = 'absolute';

  function makeDatasets() {
    var mode = getMode();
    currentMode = mode;
    var names = allNames.filter(function(n) { return selectedPolities.has(n); });
    return names.map(function(name) {
      var s = DATA.polities[name];
      var points = s.years.map(function(y, j) {
        var val = s.population[j];
        if (mode === 'fraction') val = val / worldPopAtYear(y) * 100;
        return {x: y, y: val};
      });
      return {
        label: name,
        data: points,
        borderColor: colorMap[name],
        backgroundColor: colorMap[name],
        borderWidth: 1.5,
        pointRadius: 0,
        pointHitRadius: 8,
        tension: 0.1,
      };
    });
  }

  function createChart() {
    var canvas = document.getElementById('polity-chart');
    var ctx = canvas.getContext('2d');
    chart = new Chart(ctx, {
      type: 'line',
      data: { datasets: makeDatasets() },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          y: { duration: 0 },
          x: { duration: 0 },
        },
        transitions: {
          active: { animation: { duration: 0 } },
          resize: { animation: { duration: 0 } }
        },
        interaction: { mode: 'nearest', intersect: false },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              title: function(items) {
                if (!items.length) return '';
                var x = Math.round(items[0].parsed.x);
                return x < 0 ? (-x) + ' BCE' : x + ' CE';
              },
              label: function(ctx) {
                var val = ctx.parsed.y;
                if (currentMode === 'fraction') return ctx.dataset.label + ': ' + val.toFixed(1) + '%';
                if (val >= 1e6) return ctx.dataset.label + ': ' + (val/1e6).toFixed(1) + 'M';
                if (val >= 1e3) return ctx.dataset.label + ': ' + (val/1e3).toFixed(0) + 'K';
                return ctx.dataset.label + ': ' + val;
              }
            }
          },
          zoom: {
            zoom: {
              wheel: { enabled: true },
              pinch: { enabled: true },
              mode: 'x',
            },
            pan: {
              enabled: true,
              mode: 'x',
            },
            limits: {
              x: { min: -1000, max: 2025 },
            }
          }
        },
        scales: {
          x: {
            type: 'linear', min: -500, max: 2025,
            title: { display: true, text: 'Year' },
            ticks: { callback: function(v) { v = Math.round(v); return v < 0 ? (-v) + ' BCE' : v; } }
          },
          y: {
            min: 0,
            title: { display: true, text: 'Population' },
            ticks: {
              callback: function(v) {
                if (currentMode === 'fraction') return v + '%';
                if (v >= 1e9) return (v/1e9).toFixed(1) + 'B';
                if (v >= 1e6) return (v/1e6).toFixed(0) + 'M';
                if (v >= 1e3) return (v/1e3).toFixed(0) + 'K';
                return v;
              }
            }
          }
        },
        onHover: function(evt, elements) {
          if (!chart) return;
          // Only highlight if cursor is close to a line (within 30px)
          var idx = -1;
          if (elements.length) {
            var el = elements[0].element;
            var mouseX = evt.x, mouseY = evt.y;
            var dx = mouseX - el.x, dy = mouseY - el.y;
            if (Math.sqrt(dx*dx + dy*dy) < 30) {
              idx = elements[0].datasetIndex;
            }
          }
          chart.data.datasets.forEach(function(ds, i) {
            ds.borderWidth = (idx === -1 || idx === i) ? 1.5 : 0.5;
            ds.borderColor = (idx !== -1 && idx !== i) ? ds.backgroundColor + '40' : ds.backgroundColor;
          });
          chart.update('none');
        },
        events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove']
      }
    });
    canvas.addEventListener('mouseleave', function() {
      if (!chart) return;
      chart.data.datasets.forEach(function(ds) {
        ds.borderWidth = 1.5;
        ds.borderColor = ds.backgroundColor;
      });
      chart.update('none');
    });
  }

  function updateChart() {
    if (!chart || !DATA) return;
    var mode = getMode();
    currentMode = mode;
    var wantedNames = new Set(allNames.filter(function(n) { return selectedPolities.has(n); }));

    // Remove datasets no longer wanted
    for (var i = chart.data.datasets.length - 1; i >= 0; i--) {
      if (!wantedNames.has(chart.data.datasets[i].label)) {
        chart.data.datasets.splice(i, 1);
      }
    }

    // Update existing datasets (e.g. mode change) and track what's already shown
    var existing = new Set();
    chart.data.datasets.forEach(function(ds) {
      existing.add(ds.label);
      var s = DATA.polities[ds.label];
      ds.data = s.years.map(function(y, j) {
        var val = s.population[j];
        if (mode === 'fraction') val = val / worldPopAtYear(y) * 100;
        return {x: y, y: val};
      });
    });

    // Add new datasets
    allNames.forEach(function(name) {
      if (!wantedNames.has(name) || existing.has(name)) return;
      var s = DATA.polities[name];
      var points = s.years.map(function(y, j) {
        var val = s.population[j];
        if (mode === 'fraction') val = val / worldPopAtYear(y) * 100;
        return {x: y, y: val};
      });
      chart.data.datasets.push({
        label: name,
        data: points,
        borderColor: colorMap[name],
        backgroundColor: colorMap[name],
        borderWidth: 1.5,
        pointRadius: 0,
        pointHitRadius: 8,
        tension: 0.1,
      });
    });

    chart.options.scales.y.title.text = mode === 'fraction' ? '% of world population' : 'Population';
    chart.update();
  }

  // Load data and init
  fetch('{{ site.baseurl }}/assets/data/polity_timeseries.json')
    .then(function(r) { return r.json(); })
    .then(function(d) {
      DATA = d;
      allNames = Object.keys(DATA.ranking)
        .sort(function(a,b) { return DATA.ranking[b].person_years - DATA.ranking[a].person_years; });
      // Assign stable colors by rank
      allNames.forEach(function(name, i) { colorMap[name] = COLORS[i % COLORS.length]; });
      // Default: top 20 selected
      allNames.slice(0, 20).forEach(function(n) { selectedPolities.add(n); });
      buildRegionSelector();
      createChart();
    });

  document.getElementById('select-top-20').addEventListener('click', function() {
    selectedPolities.clear();
    allNames.slice(0, 20).forEach(function(n) { selectedPolities.add(n); });
    syncCheckboxes();
    updateChart();
  });
  document.getElementById('select-none').addEventListener('click', function() {
    selectedPolities.clear();
    syncCheckboxes();
    updateChart();
  });
  document.querySelectorAll('input[name="chart-mode"]').forEach(function(r) {
    r.addEventListener('change', updateChart);
  });
  document.getElementById('chart-reset-zoom').addEventListener('click', function() {
    if (chart) chart.resetZoom();
  });
})();
</script>

<style>
/* Chart */
#chart-mode-controls {
  margin-bottom: 0.5em;
  font-size: 0.9rem;
}
#chart-wrapper {
  width: calc(100vw - 40px);
  max-width: 950px;
  height: 450px;
  margin-left: 50%;
  transform: translateX(-50%);
  margin-bottom: 1em;
}
#chart-selector {
  width: calc(100vw - 40px);
  max-width: 950px;
  margin-left: 50%;
  transform: translateX(-50%);
  border: 1px solid #ddd;
  padding: 8px 12px;
  margin-bottom: 2em;
  font-size: 0.85rem;
}
#chart-selector-header {
  margin-bottom: 6px;
}
.chart-btn {
  background: #f0f0f0;
  border: 1px solid #ccc;
  padding: 2px 10px;
  cursor: pointer;
  font-size: 0.8rem;
  margin-right: 6px;
  border-radius: 3px;
}
.chart-btn:hover { background: #e0e0e0; }
.chart-btn-sm { padding: 1px 6px; font-size: 0.75rem; margin-left: 6px; }
.region-group { margin-bottom: 2px; }
.region-header {
  cursor: pointer;
  padding: 3px 0;
  user-select: none;
}
.region-header span:first-child {
  display: inline-block;
  width: 1em;
  font-size: 0.8em;
}
.region-list {
  padding-left: 1.5em;
  columns: 2;
  column-gap: 2em;
}
@media (max-width: 600px) { .region-list { columns: 1; } }
.polity-checkbox {
  display: block;
  padding: 1px 0;
  cursor: pointer;
  break-inside: avoid;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.polity-checkbox input { margin-right: 4px; }
.legend-swatch {
  display: inline-block;
  width: 12px;
  height: 3px;
  margin-right: 4px;
  vertical-align: middle;
}
/* Break tables out of the narrow post column */
#polity-table-wrapper, #dynasty-table-wrapper, #colonial-table-wrapper {
  width: calc(100vw - 40px);
  max-width: 950px;
  margin-left: 50%;
  transform: translateX(-50%);
}
#polity-table-wrapper {
  max-height: 600px;
  overflow-y: scroll;
  border: 1px solid #ddd;
  margin-bottom: 1.5em;
  scrollbar-gutter: stable;
}
#dynasty-table-wrapper, #colonial-table-wrapper {
  margin-bottom: 1.5em;
}
#polity-table, #dynasty-table, #colonial-table {
  table-layout: auto;
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
  margin: 0;
}
#polity-table th, #polity-table td,
#dynasty-table th, #dynasty-table td,
#colonial-table th, #colonial-table td {
  padding: 5px 10px;
}
#polity-table thead { position: sticky; top: 0; z-index: 1; }
#polity-table td:nth-child(1), #dynasty-table td:nth-child(1) { text-align: center; }
#polity-table td:nth-child(3), #polity-table td:nth-child(4) { text-align: right; white-space: nowrap; }
#polity-table td:nth-child(5), #polity-table td:nth-child(6), #polity-table td:nth-child(7),
#dynasty-table td:nth-child(3), #dynasty-table td:nth-child(4) { text-align: right; white-space: nowrap; }
#dynasty-table td:nth-child(5), #dynasty-table td:nth-child(6), #dynasty-table td:nth-child(7),
#colonial-table td:nth-child(2), #colonial-table td:nth-child(3), #colonial-table td:nth-child(4) { text-align: right; }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  function parseYear(text) {
    text = text.trim();
    if (!text) return 9999;
    if (text.indexOf('BCE') !== -1) return -parseInt(text);
    return parseInt(text);
  }
  function setupSortable(tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    var headers = table.querySelectorAll('th.sortable[data-table="' + tableId + '"]');
    headers.forEach(function(th) {
      th.addEventListener('click', function() {
        var col = parseInt(this.dataset.col);
        var sortType = this.dataset.sort || 'number';
        var isAsc = this.classList.contains('sort-asc');
        // Toggleable columns (text, year): cycle asc/desc
        // Number columns: always desc
        var ascending;
        if (sortType === 'number') {
          ascending = false;
        } else {
          ascending = !isAsc;
        }
        var rows = Array.from(tbody.querySelectorAll('tr'));
        rows.sort(function(a, b) {
          var aText = a.children[col].textContent;
          var bText = b.children[col].textContent;
          var cmp;
          if (sortType === 'text') {
            cmp = aText.localeCompare(bText);
          } else if (sortType === 'year') {
            cmp = parseYear(aText) - parseYear(bText);
          } else {
            cmp = parseFloat(aText.replace(/,/g, '')) - parseFloat(bText.replace(/,/g, ''));
          }
          return ascending ? cmp : -cmp;
        });
        rows.forEach(function(row, i) {
          row.children[0].textContent = i + 1;
          tbody.appendChild(row);
        });
        headers.forEach(function(h) { h.classList.remove('sort-desc', 'sort-asc'); });
        this.classList.add(ascending ? 'sort-asc' : 'sort-desc');
      });
    });
  }
  setupSortable('polity-table');
  setupSortable('dynasty-table');
  // Default sort: Births (M) column
  var birthsHeader = document.querySelector('#polity-table th.sortable[data-col="4"]');
  if (birthsHeader) birthsHeader.click();
});
</script>
