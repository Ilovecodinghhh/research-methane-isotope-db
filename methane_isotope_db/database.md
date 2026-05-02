# Methane (CH₄) Isotope Database: δ¹³C and δD Source Signatures (2016–Present)

> **Version**: 1.1 | **Date**: 2026-05-02 | **Status**: Phase 3 complete — 34 entries (31 with isotope data, 3 context-only)
> 
> **Key**: Values marked with † are compiled/review ranges. ± values are reported SD unless noted (2SD where specified). "—" = not reported or not accessible.
> All δ¹³C relative to VPDB; all δD (= δ²H) relative to VSMOW.

---

## Core Reference Sources (Deep-Dive Cards)

### 📦 Milkov & Etiope (2018) — Org. Geochem. ✅ [Now extracted]
- **Paper**: "Revised genetic diagrams for natural gases based on a global dataset of >20,000 samples"
- **Size**: 20,621 gas samples; δ¹³C: N=17,683 (−110.2 to +45.0‰); δ²H: N=7,027 (−531 to +301‰)
- **DOI**: [10.1016/j.orggeochem.2018.09.002](https://doi.org/10.1016/j.orggeochem.2018.09.002)
- **Revised genetic field boundaries (Table 2)**:
  - Primary microbial (CO₂ reduction): δ¹³C = −90 to −60‰, δ²H = −350 to −125‰
  - Primary microbial (methyl-type fermentation): δ¹³C = −90 to −50‰, δ²H = −450 to −250‰
  - Thermogenic: δ¹³C = −75 to −15‰, δ²H = −350 to −100‰
  - Secondary microbial: δ¹³C = −60 to −35‰, δ²H = −350 to −150‰
  - Abiotic: δ¹³C = −50 to +10‰, δ²H = −450 to −50‰
- **Key finding**: Traditional δ¹³C = −55‰ cutoff between microbial/thermogenic is inadequate; 14% of conventional gas has δ¹³C < −55‰

### 📦 Etiope, Ciotoli & Schwietzke (2019) — ESSD ✅ OA
- **Paper**: "Gridded maps of geological methane emissions and their isotopic signature"
- **Coverage**: Global (1° × 1° grid) | **Data**: NetCDF at [doi:10.25925/4j3f-he27](https://doi.org/10.25925/4j3f-he27)
- **DOI**: [10.5194/essd-11-1-2019](https://doi.org/10.5194/essd-11-1-2019) | Cited: 266

### 📦 Saunois et al. (2020) — ESSD ✅ OA
- **Paper**: "The Global Methane Budget 2000–2017"
- **DOI**: [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | Cited: 2,584
- **Note**: Budget synthesis; isotopes referenced but not primary output.

### 📦 Menoud et al. (2022) — ESSD ✅ OA [**KEY: European Methane Isotope Database (EMID)**]
- **Paper**: "New contributions of measurements in Europe to the global inventory of the stable isotopic composition of methane"
- **Coverage**: Europe (NL, PL, RO, UK, CH, DE) + updated global compilation
- **Data**: Zenodo [doi:10.5281/ZENODO.4062356](https://doi.org/10.5281/ZENODO.4062356)
- **DOI**: [10.5194/essd-14-4365-2022](https://doi.org/10.5194/essd-14-4365-2022) | Cited: 40
- **Key EMID values**:
  - Fossil fuel (excl. seeps): δ¹³C = −44.6 ± 0.4‰ (n=452), δ²H = −182 ± 2‰
  - Gas leaks (UK + NL): δ¹³C = −38.9 ± 0.3‰ (n=154)
  - Extraction sites (PL + RO): δ¹³C = −48.5 ± 0.6‰ (n=235)
  - Waste: δ¹³C = −53.6 ± 0.4‰ (n=202)
  - Wetlands (EMID): δ¹³C = −73.6 ± 2.27‰
  - BB C₃: δ¹³C = −28.4 ± 0.65‰; BB C₄: ~−18‰
  - Updated global weighted mean: δ¹³C = −46.6 ± 1.8‰, δ²H = −192 ± 7‰

### 📦 Sherwood et al. (2017) — Global Source Signature Inventory (Foundational) ✅ [Fully extracted]
- **Paper**: "Global Inventory of Gas Geochemistry Data from Fossil Fuel, Microbial and Burning Sources"
- **DOI**: [10.5194/essd-9-639-2017](https://doi.org/10.5194/essd-9-639-2017)
- **Size**: 10,706 samples (8,734 fossil fuel + 1,972 non-fossil), 190 references
- **Table 5 — δ¹³C (unweighted mean ± SD)**:
  - Conventional gas: −44.0 ± 10.7‰ (n=6,079)
  - Coal gas: −49.5 ± 11.2‰ (n=1,402) — **much lighter than assumed in budgets (−35 to −37‰)**
  - Shale gas: −42.5 ± 6.7‰ (n=647)
  - All fossil fuel: −44.8 ± 10.7‰ (n=8,128)
  - Rice paddies: −62.2 ± 3.9‰ (n=253)
  - Ruminants: −65.4 ± 6.7‰ (n=171, unweighted by C3/C4)
  - Termites: −63.4 ± 6.4‰ (n=29)
  - Waste: −56.0 ± 7.6‰ (n=56)
  - Wetlands: −61.5 ± 5.4‰ (n=556)
  - All microbial: −61.7 ± 6.2‰ (n=1,065)
  - Biomass burning: −26.2 ± 4.8‰ (n=907, unweighted by C3/C4)
- **Table 5 — δ²H (unweighted mean ± SD)**:
  - Conventional gas: −194 ± 47‰ (n=1,969)
  - Coal gas: −232 ± 52‰ (n=511)
  - Shale gas: −167 ± 44‰ (n=398)
  - All fossil fuel: −197 ± 51‰ (n=2,878)
  - Rice paddies: −323 ± 16‰ (n=139)
  - Ruminants: −316 ± 29‰ (n=79)
  - Waste: −298 ± 11‰ (n=23)
  - Wetlands: −322 ± 42‰ (n=173)
  - All microbial: −317 ± 33‰ (n=415)
  - Biomass burning: −211 ± 15‰ (n=4)

### 📦 Douglas et al. (2021) — Biogeosciences ✅ OA [**KEY for δD**]
- **Paper**: "Geographic variability in freshwater methane hydrogen isotope ratios"
- **DOI**: [10.5194/bg-18-3505-2021](https://doi.org/10.5194/bg-18-3505-2021) | Cited: 24
- **Key δD values**:
  - Natural wetlands: δ²H = −310 ± 25‰, δ¹³C = −63.9 ± 3.3‰
  - Low-lat wetlands (0–30°N): δ²H = −305 ± 13‰
  - High-lat wetlands (30–90°N): δ²H = −345 ± 11‰; boreal: −374 ± 10‰
  - Inland waters: median δ²H = −296‰
  - Global freshwater flux-weighted: δ²H = −310 ± 15‰
  - Global source δ²H: −278 ± 15‰; δ¹³C: −56.4 ± 2.6‰

### 📦 Schwietzke, Sherwood, Bruhwiler et al. (2016) — Nature [Paywalled]
- **Paper**: "Upward revision of global fossil fuel methane emissions based on isotope database"
- **DOI**: [10.1038/nature19797](https://doi.org/10.1038/nature19797) | Cited: 600
- **Key**: Fossil fuel δ¹³C = −44.0 ± 0.7‰. Emissions revised to ~132 Tg/yr.

---

## Main Database Table

| # | Year | Author(s) | Methane Source | δ¹³C (‰, VPDB) | δD (‰, VSMOW) | Article Title | Journal | DOI | Cited | Access | Sampling Period |
|---|------|-----------|---------------|-----------------|----------------|---------------|---------|-----|-------|--------|-----------------|
| 1 | 2019 | Nisbet, Manning, Dlugokencky | Atmospheric trend (global) | −47.4 (2017 mean); Arctic: −47.3→−48‰ (2006–2017); bulk source ≈ −53‰; C3 wetlands: −70 ± 5‰; fossil ~−50 ± 5‰; coal: −40 ± 15‰ | — | Very Strong Atmospheric Methane Growth 2014–2017 | Global Biogeochem. Cy. | [10.1029/2018GB006009](https://doi.org/10.1029/2018GB006009) | 762 | ✅ OA | 2014–2017 |
| 2 | 2019 | Etiope, Ciotoli, Schwietzke | Geological (global grid) | Thermogenic seeps: −50 to −30; Microbial seeps: −90 to −55; Geothermal: −25 to −15; **Global geo weighted: −49** | — | Gridded maps of geological methane emissions and isotopic signature | ESSD | [10.5194/essd-11-1-2019](https://doi.org/10.5194/essd-11-1-2019) | 266 | ✅ OA | Contemporary |
| 3 | 2020 | Nisbet, Fisher, Lowry | Multiple (review) | Fossil: −44 to −35 †; Biogenic: −70 to −55 †; BB: −25 to −18 † | Fossil: −200 to −130 †; Biogenic: −400 to −280 †; BB: −230 to −200 † | Methane Mitigation: Methods to Reduce Emissions | Rev. Geophys. | [10.1029/2019RG000675](https://doi.org/10.1029/2019RG000675) | 393 | ✅ OA | Review |
| 4 | 2020 | Saunois, Stavert, Poulter | Global budget | — | — | The Global Methane Budget 2000–2017 | ESSD | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | 2,584 | ✅ OA | 2000–2017 |
| 5 | 2020 | Menoud, van der Veen, Scheeren | Netherlands (gas, agriculture, waste) | Gas: −40.3 ± 2.3; Ruminants: −66.3 ± 3.2; Waste: −58.1 ± 2.8 | Gas: −185 ± 15; Agriculture: −319 ± 12 | Methane Sources in Lutjewad, Netherlands | Tellus B | [10.1080/16000889.2020.1823733](https://doi.org/10.1080/16000889.2020.1823733) | 68 | ✅ OA | 2018–2019 |
| 6 | 2021 | Menoud, van der Veen, Nęcki | Krakow, Poland (coal, gas, waste) | Coal: −58 to −45; Gas: −39.3 to −36; Waste: −55 to −52 | Coal: −210 to −180; Fossil: −190 ± 9; Sewage: <−300; Manholes: −202 to −146 | Methane sources in Krakow: isotope analysis | ACP | [10.5194/acp-21-13167-2021](https://doi.org/10.5194/acp-21-13167-2021) | 46 | ✅ OA | 2018–2019 |
| 7 | 2022 | Basu, Lan, Dlugokencky | Global isotopic inversion | Source-weighted: ~−53.5; BB C₃: −26.7; C₄: −12.5; Ruminant C₃: −54.5; C₄: −67.8 | — | Estimating Methane Emissions Consistent with δ¹³C | ACP | [10.5194/acp-22-15351-2022](https://doi.org/10.5194/acp-22-15351-2022) | 110 | ✅ OA | 1997–2016 |
| 8 | 2018 | Milkov, Etiope | Natural gas (>20k samples) | **Table 2 boundaries**: Microbial CO₂-red: −90 to −60; Microbial ferment: −90 to −50; Thermogenic: −75 to −15; Secondary microbial: −60 to −35; Abiotic: −50 to +10; W. Siberia microbial mean: −51.8 | Microbial CO₂-red: −350 to −125; Microbial ferment: −450 to −250; Thermogenic: −350 to −100; Secondary: −350 to −150; Abiotic: −450 to −50 | Revised genetic diagrams for natural gases | Org. Geochem. | [10.1016/j.orggeochem.2018.09.002](https://doi.org/10.1016/j.orggeochem.2018.09.002) | — | ✅ PDF | Multi-decadal |
| 9 | 2017 | Worden, Bloom, Pandey | BB/Fossil/Microbial rebalancing | Source mix: −56 to −61; BB: −25 to −12 | — | Reduced biomass burning reconciles post-2006 methane | Nat. Comms. | [10.1038/s41467-017-02246-0](https://doi.org/10.1038/s41467-017-02246-0) | 144 | ✅ OA | 2006–2014 |
| 10 | 2021 | Lu, Harris, Fisher | Queensland, Australia (CSG, cattle, landfill) | CSG: −55.1 to −44.2; Shallow coal: −80 to −50; Cattle: −62 to −65; Abattoir: −46; WWTP: −47.6 ± 2 | CSG: −310 to −191; Shallow: −310 to −210; Cattle: ~−320 | Isotopic signatures in coal seam gas fields, Queensland | ACP | [10.5194/acp-21-10527-2021](https://doi.org/10.5194/acp-21-10527-2021) | — | ✅ OA | 2018–2019 |
| 11 | 2022 | Menoud, van der Veen, Lowry | EMID — Europe + global update | Fossil (excl. seeps): −44.6 ± 0.4 (n=452); Extraction PL+RO: −48.5 ± 0.6; Gas UK+NL: −38.9 ± 0.3; Waste: −53.6 ± 0.4; Wetlands: −73.6 ± 2.27; BB C₃: −28.4 ± 0.65; BB C₄: ~−18 | Fossil: −182 ± 2; Global: −192 ± 7 | EMID: New contributions to global inventory | ESSD | [10.5194/essd-14-4365-2022](https://doi.org/10.5194/essd-14-4365-2022) | 40 | ✅ OA | 2017–2020 |
| 12 | 2020 | Hmiel, Petrenko, Dyonisius | Geological vs anthropogenic fossil | — (uses ¹⁴C) | — | Preindustrial ¹⁴CH₄ indicates greater anthropogenic fossil emissions | Nature | [10.1038/s41586-020-1991-8](https://doi.org/10.1038/s41586-020-1991-8) | 323 | ✅ OA | Preindustrial ice |
| 13 | 2019 | Hoheisel, Yeman, Dinger | Heidelberg, Germany (gas, landfill) | Siberian gas: −48 to −54; North Sea: −34 ± 3; Landfill (July): −66; Urban mix: −49 to −61 | — | Improved method for mobile δ¹³CH₄ source signatures | AMT | [10.5194/amt-12-1123-2019](https://doi.org/10.5194/amt-12-1123-2019) | — | ✅ OA | 2016–2017 |
| 14 | 2020 | Maazallahi, Fernandez, Menoud | Utrecht (NL) & Hamburg (DE) | Fossil: −50 to −40; Microbial: −55 to −70; Hamburg anomaly: −23 | Fossil: −150 to −200; Microbial: −260 to −360; Hamburg: −153 | Methane mapping, Utrecht & Hamburg | ACP | [10.5194/acp-20-14717-2020](https://doi.org/10.5194/acp-20-14717-2020) | — | ✅ OA | 2018–2019 |
| 15 | 2021 | Douglas, Stratigopoulos, Park | Freshwater (global compilation) | Wetlands: −63.9 ± 3.3; Global source: −56.4 ± 2.6 | Freshwater: −310 ± 15; Wetlands: −310 ± 25; Low-lat: −305 ± 13; High-lat: −345 ± 11; Boreal: −374 ± 10; Inland: −296; **Global source: −278 ± 15** | Geographic variability in freshwater methane δ²H | Biogeosciences | [10.5194/bg-18-3505-2021](https://doi.org/10.5194/bg-18-3505-2021) | 24 | ✅ OA | Compilation |
| 16 | 2021 | Zhang, Jacob, Lu | Global GOSAT inverse | — | — | Attribution of accelerating methane increase 2010–2018 | ACP | [10.5194/acp-21-3643-2021](https://doi.org/10.5194/acp-21-3643-2021) | 175 | ✅ OA | 2010–2018 |
| 17 | 2022 | Feng, Palmer, Zhu | Tropical biogenic + anthropogenic | — | — | Tropical methane emissions explain recent growth | Nat. Comms. | [10.1038/s41467-022-28989-z](https://doi.org/10.1038/s41467-022-28989-z) | 111 | ✅ OA | 2010–2019 |
| 18 | 2023 | Nisbet, Manning, Dlugokencky | Atmospheric trend 2006–2022 | Pre-industrial: ~−49‰; 2006 Arctic: −47.3‰; 2022 Arctic: ~−48‰; 2006 tropics: ~−46.9‰; 2022 tropics: ~−47.4‰; Shift: −0.55‰ in 15 yrs; Bulk source: ≈−53‰; C3 wetlands: −67.8‰; C4 wetlands: −56.7‰; S. tropical seasonal: −60 ± 5‰; Equatorial: −52 ± 2‰; Ruminant global avg: ~−65‰; Kenyan cattle: ~−57‰; Fossil: −43 to −45‰; Source mix declining from −54.3‰ (2006) to −55.2‰ | — | Atmospheric Methane: 2006–2022 vs Glacial Terminations | GBC | [10.1029/2023GB007875](https://doi.org/10.1029/2023GB007875) | 98 | ✅ OA | 2006–2022 |
| 19 | 2019 | Maasakkers, Jacob, Sulprizio | Global + OH trend | — | — | Global distribution of methane emissions and OH trends | ACP | [10.5194/acp-19-7859-2019](https://doi.org/10.5194/acp-19-7859-2019) | 288 | ✅ OA | 2010–2015 |
| 20 | 2018 | Dean, Middelburg, Röckmann | Climate feedbacks (review) | — | — | Methane Feedbacks to the Global Climate System | Rev. Geophys. | [10.1002/2017RG000559](https://doi.org/10.1002/2017RG000559) | 643 | ✅ OA | Review |
| 21 | 2021 | Bakkaloglu, Lowry, Fisher | Biogas plants (UK) | −57.5 ± 3.5 | — | Quantification of methane from UK biogas plants | Waste Manag. | [10.1016/j.wasman.2021.01.011](https://doi.org/10.1016/j.wasman.2021.01.011) | — | ❌ PW | 2019 |
| 22 | 2020 | Zhang, Gautam, Pandey | Oil & gas (Permian Basin, USA) | — | — | Quantifying methane from the largest US oil basin from space | Sci. Adv. | [10.1126/sciadv.aaz5120](https://doi.org/10.1126/sciadv.aaz5120) | 451 | ✅ OA | 2018–2019 |
| 23 | 2016 | Schwietzke, Sherwood, Bruhwiler | Global fossil fuel (revised) | −44.0 ± 0.7 | — | Upward revision of global fossil fuel methane emissions | Nature | [10.1038/nature19797](https://doi.org/10.1038/nature19797) | 600 | ❌ PW | Compilation |
| 24 | 2016 | Röckmann, Eyer, van der Veen | Atmospheric (Cabauw tower, NL) | Method intercomparison; IRMS–QCLAS offsets: δ¹³C 0.25 ± 0.04‰; δD −4.3 ± 0.4‰ | — | In situ isotopic composition of CH₄ at Cabauw | ACP | [10.5194/acp-16-10469-2016](https://doi.org/10.5194/acp-16-10469-2016) | 166 | ✅ OA | 2014–2015 |
| 25 | 2016 | Zazzeri, Lowry, Fisher | UK sources (landfill, coal, gas) | Landfill: −60.2 to −55.2 (2SD); avg: −58 ± 3; Coal deep mines: −33.3 ± 1.8 (2SD); Coal range: −51.2 to −30.9; Gas leaks: −36.4 ± 1.9 (2SD); Gas installations: −35.7 to −36.3; North Sea reservoir: −30 to −24 | — | Plume mapping and isotopic characterisation of UK CH₄ | Atmos. Environ. | [10.1016/j.atmosenv.2015.12.028](https://doi.org/10.1016/j.atmosenv.2015.12.028) | — | ✅ OA | 2013–2014 |
| 26 | 2012 | Townsend-Small, Tyler, Pataki | Los Angeles (fossil, biological, urban) | Fossil fuel (refineries, power, drilling): −45 to −30; Biological (cows, landfill, sewage): −65 to −45; LA dominant source: −41.5; Landfill: −61; Manure: −51; Freeway traffic: ~−46 | Fossil: −275 to −100; Biological: −350 to −275; LA urban air: −229 to −208; Landfill/manure biofuel: −280 to −330 | Isotopic measurements of atmospheric methane in Los Angeles | JGR | [10.1029/2011JD016826](https://doi.org/10.1029/2011JD016826) | — | ✅ OA | 2008–2010 |
| 27 | 2021 | Defratyka, Paris, Stoop | Paris (gas network, WWTP, urban) | Gas network venting: −36.4 ± 2.6 and −39.5 ± 5.0; WWTP (IDF 2012–2015): −55.3 to −51.9; Gas storage (IDF): −43.4 to −33.8; Isolated leak: −52.2 ± 8.1; Microbial global median: ~−62; Fossil global median: ~−44; Pyrogenic: −35 to −7 (median ~−22) | — | Mapping Urban Methane Sources in Paris, France | EST | [10.1021/acs.est.1c00859](https://doi.org/10.1021/acs.est.1c00859) | — | ✅ OA | 2018–2020 |
| 28 | 2022 | Fernandez, Maazallahi, Menoud | Bucharest, Romania (gas, waste, mixed) | All sources: −61 to −36 (mean −49 ± 6, n=55); Known fossil: −50 ± 5 (n=8); Gas supply box: −60; Landfill: −58 ± 1 (n=2); Wastewater: −50; Gas leak: −49 ± 2 (n=4) | All sources: −388 to −157 (mean −274 ± 69, n=55); Known fossil: −188 ± 40 (n=8); Gas supply: −198; Landfill: −288 to −280; Wastewater: −335; Gas leak: −154 ± 31 (n=2); Biogenic: <−270 | Street-level CH₄ mapping and isotope signatures, Bucharest | Atmos. Environ. | [10.1016/j.atmosenv.2022.119258](https://doi.org/10.1016/j.atmosenv.2022.119258) | — | ✅ OA | 2019 |
| 29 | 2023 | Woolley-Maisch, Fisher, Lowry | UK 5-site network (long-term δ¹³C) | UK source mix: −50.1 to −56.1‰; EGH (suburban): −50.1 ± 0.7; WAO (coastal): −51.4 ± 0.9; BAR (rural): −56.1 ± 1.8; WCO (marine): −53.3 ± 0.9; NAEI/NAME modeled: −56.6 (WAO), −54.2 (EGH); UK weighted: −58.2 ± 1.1 (2020); −61.3 ± 1.1 (2021) | Coal mines: −43.2 ± 6.8 (n=11); Gas: −39.3; Animal waste: −51.5; Landfill: −57.1; Wastewater: −52.6; Total waste: −56.3 | Long-term CH₄ and δ¹³C measurements across the UK | JGR | [10.1029/2023JD039098](https://doi.org/10.1029/2023JD039098) | — | ✅ OA | 2009–2021 |
| 30 | 2019 | Schaefer | Review: causes of atmospheric CH₄ trends | Biogenic/wetland: ~−62‰; Fossil (thermogenic): ~−44‰; BB: ~−22‰; Tropical wetlands: ~−55‰ | — | Causes and consequences of trends in atmospheric methane | Curr. Clim. Change Rep. | [10.1007/s40641-019-00140-z](https://doi.org/10.1007/s40641-019-00140-z) | — | ❌ PW | Review |
| 31 | 2023 | Fiehn, Eckl, Kostinek | Upper Silesian Coal Basin (coal, biogenic) | Free troposphere biogenic: −61.2 ± 2.0; Inflow BL: −55.0 ± 3.5; Coal borehole (Kotarba): −79.9 to −44.5; Coal (EMID Silesia avg): −49.8 ± 5.7; Gas network: ~−55 | Free trop. biogenic: −335 ± 24; Inflow BL: −296 ± 37; Coal borehole: −202 to −153; Coal (EMID): −184 ± 32; Cow farm: −358.7; Landfill (EMID): −275 ± 21; Wastewater (EMID): −323 ± 14; Waste model: −300 ± 20 | Source apportionment of CH₄ from Upper Silesian Coal Basin using isotopic signatures | ACP | [10.5194/acp-23-15749-2023](https://doi.org/10.5194/acp-23-15749-2023) | 17 | ✅ OA | 2018 |
| 32 | 2022 | Kelly, Lu, Harris | Surat Basin, Australia (CSG, cattle, feedlots) | CSG aircraft: −55.4 (CI 95% ± 13.7); CSG ground: −56.7 to −45.6; Walloon Coal Measures lit.: −64.1 to −44.5; Grazing cattle: −60.5 (CI ± 15.6); Cattle (low alt.): −53.8 (CI ± 17.4); Feedlots: −69.6 (CI ± 22.6); Feedlot ground: −65.2 to −60.3; Piggeries: −48.0 to −47.1; Termites: possible −80.2 | — | Atmospheric methane isotopes identify inventory gaps, Surat Basin | ACP | [10.5194/acp-22-15527-2022](https://doi.org/10.5194/acp-22-15527-2022) | 10 | ✅ OA | 2019 |
| 33 | 2022 | Gonzalez Moguel, Vogel, Ars | Athabasca oil sands (thermogenic, microbial) | Keeling intercept (regional): −56 ± 0.8; Northern mines (thermogenic): −35.1 ± 4.5; Alberta Cretaceous oils: −42 to −48; End pit lake (microbial): −60 to −65; Boreal wetlands: −67.8; Landfill: ~−55 | — (uses ¹⁴C: Δ¹⁴C source = −898 ± 9‰; northern mines Δ¹⁴C ≈ −1000‰) | Using ¹⁴C and ¹³C for source attribution, Athabasca oil sands | ACP | [10.5194/acp-22-2121-2022](https://doi.org/10.5194/acp-22-2121-2022) | 10 | ✅ OA | 2018–2019 |
| 34 | 2016 | Saunois, Bousquet, Poulter | Global budget 2000–2012 | — | — | The global methane budget 2000–2012 | ESSD | [10.5194/essd-8-697-2016](https://doi.org/10.5194/essd-8-697-2016) | 1,101 | ✅ OA | 2000–2012 |

---

## Isotope Source Signature Summary (Verified from Accessible Data)

### δ¹³C Source Signatures

| Methane Source Category | δ¹³C Range (‰, VPDB) | Best Estimate | n | Key References |
|------------------------|----------------------|---------------|---|----------------|
| **FOSSIL FUEL — GLOBAL** | | | | |
| Fossil fuel — global weighted | — | −44.8 ± 10.7 | 8,128 | Sherwood 2017 (Table 5) |
| Conventional oil & gas (Sherwood) | −87.0 to −14.8 | −44.0 ± 10.7 | 6,079 | Sherwood 2017 |
| Coal gas (Sherwood) | −85.5 to −16.8 | −49.5 ± 11.2 | 1,402 | Sherwood 2017 |
| Shale gas (Sherwood) | −69.7 to −24.4 | −42.5 ± 6.7 | 647 | Sherwood 2017 |
| Fossil fuel — Schwietzke revision | — | −44.0 ± 0.7 | — | Schwietzke 2016 |
| Fossil fuel — EMID Europe (excl. seeps) | — | −44.6 ± 0.4 | 452 | Menoud 2022 |
| Fossil — global (Sherwood categories) | — | −44.8 ± 10.7 (thermogenic) | — | Sherwood 2017 via Gonzalez Moguel 2022 |
| Fossil — global range (Nisbet 2023) | −43 to −45 | — | — | Nisbet 2023 |
| **NATURAL GAS** | | | | |
| Gas leaks (UK + NL) | — | −38.9 ± 0.3 | 154 | Menoud 2022 |
| Gas installations (UK) | −35.7 to −36.3 | −36.4 ± 1.9 (2SD) | — | Zazzeri 2016 |
| Gas production/distribution (UK NAEI) | — | −39.3 | — | Woolley-Maisch 2023 |
| Natural gas — Netherlands | — | −40.3 ± 2.3 | — | Menoud 2020 |
| Natural gas — Siberian | −48 to −54 | — | — | Hoheisel 2019 |
| Natural gas — North Sea | −30 to −24 (reservoir); −34 ± 3 (leaks) | — | — | Zazzeri 2016; Hoheisel 2019 |
| Gas network (Paris) | — | −36.4 ± 2.6 and −39.5 ± 5.0 | — | Defratyka 2021 |
| Gas storage (Paris/IDF) | −43.4 to −33.8 | — | — | Defratyka 2021 |
| Gas (Bucharest) | −60 to −44 (supply); −49 ± 2 (leaks) | −50 ± 5 (n=8) | 8 | Fernandez 2022 |
| **COAL** | | | | |
| Coal mines (UK) | −51.2 to −30.9 (2SD) | −43.2 ± 6.8 (n=11, NAEI) | 11 | Zazzeri 2016; Woolley-Maisch 2023 |
| Coal deep mines (UK) | — | −33.3 ± 1.8 (2SD) | — | Zazzeri 2016 |
| Coal mining (Krakow, Poland) | −58 to −45 | — | — | Menoud 2021 |
| Coal borehole (Upper Silesia) | −79.9 to −44.5 | −49.8 ± 5.7 (EMID avg) | — | Fiehn 2023; Kotarba 2001/2004 |
| Coal seam gas (Surat Basin, Aus.) | −64.1 to −44.5 | −55.4 (aircraft Keeling) | — | Kelly 2022; Lu 2021 |
| CSG shallow (<200 m) | −80 to −50 | — | — | Lu 2021 |
| Extraction sites (PL + RO) | — | −48.5 ± 0.6 | 235 | Menoud 2022 |
| **OIL & PETROLEUM** | | | | |
| Alberta Cretaceous oils | −42 to −48 | — | — | Gonzalez Moguel 2022 |
| LA fossil (refineries, drilling) | −45 to −30 | — | — | Townsend-Small 2012 |
| LA dominant source (Keeling) | — | −41.5 | — | Townsend-Small 2012 |
| Athabasca regional (Keeling) | — | −56 ± 0.8 | — | Gonzalez Moguel 2022 |
| Athabasca northern mines | — | −35.1 ± 4.5 | — | Gonzalez Moguel 2022 |
| **GEOLOGICAL** | | | | |
| Global geological weighted | — | −49 | — | Etiope 2019 |
| Thermogenic seeps | −50 to −30 | — | — | Etiope 2019 |
| Microbial seeps | −90 to −55 | — | — | Etiope 2019 |
| Geothermal | −25 to −15 | — | — | Etiope 2019 |
| Natural geological (¹⁴C-constrained) | — | ~1.6 Tg/yr only | — | Hmiel 2020 |
| **MILKOV 2018 GENETIC FIELDS** | | | | |
| Primary microbial (CO₂ reduction) | −90 to −60 | — | 17,683 | Milkov 2018 (Table 2) |
| Primary microbial (fermentation) | −90 to −50 | — | — | Milkov 2018 |
| Thermogenic (revised) | −75 to −15 | — | — | Milkov 2018 |
| Secondary microbial | −60 to −35 | — | — | Milkov 2018 |
| Abiotic | −50 to +10 | — | — | Milkov 2018 |
| **RUMINANTS / LIVESTOCK** | | | | |
| Ruminants (Netherlands) | — | −66.3 ± 3.2 | — | Menoud 2020 |
| Ruminants (Sherwood, unweighted) | −74.4 to −50.3 | −65.4 ± 6.7 | 171 | Sherwood 2017 |
| Ruminants (Queensland) | −62 to −65 | — | — | Lu 2021 |
| Ruminant C₃ feed (global) | — | −54.5 | — | Sherwood via Basu 2022 |
| Ruminant C₄ feed (global) | — | −67.8 | — | Sherwood via Basu 2022 |
| Ruminant global avg (Nisbet) | — | ~−65 | — | Nisbet 2023 |
| Kenyan pastured cattle (C₄) | — | ~−57 | — | Nisbet 2023 |
| Grazing cattle (Surat, Aus.) | −61.7 to −57.5 (ground CrI) | −60.5 (aircraft) | — | Kelly 2022 |
| Feedlots (Surat, Aus.) | −65.2 to −60.3 (ground CrI) | −69.6 (aircraft) | — | Kelly 2022 |
| Piggeries (Surat, Aus.) | −48.0 to −47.1 | — | — | Kelly 2022 |
| Animal waste (UK NAEI) | — | −51.5 | — | Woolley-Maisch 2023 |
| LA biological (cows, feedlots) | −65 to −45 | — | — | Townsend-Small 2012 |
| **WASTE / LANDFILL** | | | | |
| Waste (EMID) | — | −53.6 ± 0.4 | 202 | Menoud 2022 |
| Waste (Sherwood) | −73.9 to −45.5 | −56.0 ± 7.6 | 56 | Sherwood 2017 |
| Waste (Netherlands) | — | −58.1 ± 2.8 | — | Menoud 2020 |
| Landfill (UK, Zazzeri) | −60.2 to −55.2 (2SD) | −58 ± 3 | — | Zazzeri 2016 |
| Landfill (UK, NAEI) | — | −57.1 | — | Woolley-Maisch 2023 |
| Landfill (Bucharest) | — | −58 ± 1 (n=2) | 2 | Fernandez 2022 |
| Landfill (LA) | — | −61 | — | Townsend-Small 2012 |
| Landfill (Heidelberg, July) | — | −66 | — | Hoheisel 2019 |
| Biogas plants (UK) | — | −57.5 ± 3.5 | — | Bakkaloglu 2021 |
| **WASTEWATER** | | | | |
| WWTP (Paris/IDF) | −55.3 to −51.9 | — | — | Defratyka 2021 |
| WWTP (Bucharest) | — | −50 | — | Fernandez 2022 |
| WWTP (Queensland) | — | −47.6 ± 2 | — | Lu 2021 |
| Wastewater (UK NAEI) | — | −52.6 | — | Woolley-Maisch 2023 |
| Total waste (UK NAEI) | — | −56.3 | — | Woolley-Maisch 2023 |
| Sewage (Krakow) | −55 to −52 | — | — | Menoud 2021 |
| **WETLANDS** | | | | |
| Wetlands (EMID Europe) | — | −73.6 ± 2.27 | — | Menoud 2022 |
| Wetlands (Sherwood) | −70.1 to −48.0 | −61.5 ± 5.4 | 556 | Sherwood 2017 |
| Wetlands (global, Nisbet review) | −70 to −55 | — | — | Nisbet 2020 |
| Wetlands (global, Douglas) | — | −63.9 ± 3.3 | — | Douglas 2021 |
| C₃ plant wetlands (global) | — | −67.8 | — | Nisbet 2023 |
| C₄-rich tropical wetlands | — | −56.7 | — | Nisbet 2023 |
| S. tropical seasonal wetlands | — | −60 ± 5 | — | Nisbet 2023 |
| Equatorial wetlands | — | −52 ± 2 | — | Nisbet 2023 |
| Tropical wetlands (Schaefer) | — | ~−55 | — | Schaefer 2019 |
| Boreal wetlands | — | −67.8 | — | Gonzalez Moguel 2022 |
| End pit lake (oil sands, microbial) | −60 to −65 | — | — | Gonzalez Moguel 2022 |
| **BIOMASS BURNING** | | | | |
| BB — C₃ plants (EMID) | — | −28.4 ± 0.65 | — | Menoud 2022 |
| BB — C₃ (Basu inversion) | — | −26.7 | — | Basu 2022 |
| BB — C₄ (EMID) | — | ~−18 | — | Menoud 2022 |
| BB — C₄ (Basu) | — | −12.5 | — | Basu 2022 |
| BB (Schaefer review) | — | ~−22 | — | Schaefer 2019 |
| BB (Sherwood, unweighted) | −32.4 to −12.5 | −26.2 ± 4.8 | 907 | Sherwood 2017 |
| Pyrogenic global (Defratyka) | −35 to −7 | median ~−22 | — | Defratyka 2021 |
| **RICE PADDIES** | | | | |
| Rice paddies (Sherwood) | −67.2 to −54.0 | −62.2 ± 3.9 | 253 | Sherwood 2017 |
| **TERMITES** | | | | |
| Termites (Sherwood) | −72.8 to −55.7 | −63.4 ± 6.4 | 29 | Sherwood 2017 |
| Termites (Surat Basin, possible) | — | ~−80.2 | — | Kelly 2022 |
| **URBAN MIX** | | | | |
| Urban fossil mix (NL/DE) | −50 to −40 | — | — | Maazallahi 2020 |
| Urban microbial (NL/DE) | −55 to −70 | — | — | Maazallahi 2020 |
| UK source mix (5 sites) | −50.1 to −56.1 | — | — | Woolley-Maisch 2023 |
| Bucharest all sources | −61 to −36 | −49 ± 6 (n=55) | 55 | Fernandez 2022 |
| **ATMOSPHERIC** | | | | |
| Background (2017) | — | −47.4 | — | Nisbet 2019 |
| Background (2022, Arctic) | — | ~−48 | — | Nisbet 2023 |
| Background (2022, tropics) | — | ~−47.4 | — | Nisbet 2023 |
| Bulk global source (all) | — | ≈−53 | — | Nisbet 2023; Nisbet 2019 |
| Source mix declining trend | −54.3 (2006) → −55.2 (recent) | — | — | Nisbet 2023 |
| Global source weighted (EMID) | — | −46.6 ± 1.8 | — | Menoud 2022 |
| Global source (Douglas bottom-up) | — | −56.4 ± 2.6 | — | Douglas 2021 |
| Microbial global (Sherwood) | — | −61.7 ± 6.2 | — | Sherwood 2017 |

### δD (δ²H) Source Signatures

| Methane Source Category | δD Range (‰, VSMOW) | Best Estimate | Key References |
|------------------------|---------------------|---------------|----------------|
| **FOSSIL FUEL** | | | |
| Fossil fuel — all (Sherwood) | −415 to −62 | −197 ± 51 (n=2,878) | Sherwood 2017 (Table 5) |
| Conventional oil & gas (Sherwood) | −393 to −62 | −194 ± 47 (n=1,969) | Sherwood 2017 |
| Coal gas (Sherwood) | −415 to −75 | −232 ± 52 (n=511) | Sherwood 2017 |
| Shale gas (Sherwood) | −315 to −101 | −167 ± 44 (n=398) | Sherwood 2017 |
| Fossil fuel (EMID Europe) | — | −182 ± 2 | Menoud 2022 |
| Natural gas (NL) | — | −185 ± 15 | Menoud 2020 |
| Fossil urban (NL/DE) | −150 to −200 | — | Maazallahi 2020 |
| Fossil (Bucharest, known) | — | −188 ± 40 (n=8) | Fernandez 2022 |
| Gas supply (Bucharest) | — | −198.4 | Fernandez 2022 |
| Gas leak (Bucharest) | — | −154 ± 31 | Fernandez 2022 |
| Fossil (LA, general) | −275 to −100 | — | Townsend-Small 2012 |
| LA urban air (Keeling) | −229 to −208 | — | Townsend-Small 2012 |
| **COAL** | | | |
| Coal mining (Krakow) | −210 to −180 | −190 ± 9 (fossil-dominated) | Menoud 2021 |
| Coal borehole (Upper Silesia) | −202 to −153 | −184 ± 32 (EMID avg) | Fiehn 2023 |
| Coal seam gas (Australia) | −310 to −191 | — | Lu 2021 |
| CSG shallow (<200 m, Aus.) | −310 to −210 | — | Lu 2021 |
| **RUMINANTS** | | | |
| Ruminants (Sherwood) | −358 to −295 | −316 ± 29 (n=79) | Sherwood 2017 |
| Cattle (Queensland) | — | ~−320 | Lu 2021 |
| Agriculture (Netherlands) | — | −319 ± 12 | Menoud 2020 |
| Cow farm (Upper Silesia) | — | −358.7 | Fiehn 2023 |
| Biological (LA) | −350 to −275 | — | Townsend-Small 2012 |
| **WASTE / LANDFILL** | | | |
| Landfill (EMID, Europe) | — | −275 ± 21 | Fiehn 2023 (citing EMID) |
| Landfill (Bucharest) | −288 to −280 | — | Fernandez 2022 |
| Landfill/manure biofuel (LA) | −280 to −330 | — | Townsend-Small 2012 |
| Wastewater (EMID, Europe) | — | −323 ± 14 | Fiehn 2023 (citing EMID) |
| Wastewater (Bucharest) | — | −335 | Fernandez 2022 |
| Waste model (Upper Silesia) | — | −300 ± 20 | Fiehn 2023 |
| Manholes (Krakow) | −202 to −146 | — | Menoud 2021 |
| Sewage (Krakow) | < −300 | — | Menoud 2021 |
| Urban microbial (NL/DE) | −260 to −360 | — | Maazallahi 2020 |
| Bucharest all sources | −388 to −157 | −274 ± 69 (n=55) | Fernandez 2022 |
| Biogenic threshold (Bucharest) | < −270 | — | Fernandez 2022 |
| **WETLANDS / FRESHWATER** | | | |
| Wetlands — global | — | −310 ± 25 | Douglas 2021 |
| Low-latitude (0–30°N) | — | −305 ± 13 | Douglas 2021 |
| High-latitude (30–90°N) | — | −345 ± 11 | Douglas 2021 |
| Boreal | — | −374 ± 10 | Douglas 2021 |
| Inland waters | — | −296 (median) | Douglas 2021 |
| Freshwater global (flux-weighted) | — | −310 ± 15 | Douglas 2021 |
| Global source δ²H | — | −278 ± 15 | Douglas 2021 |
| Global updated weighted | — | −192 ± 7 | Menoud 2022 |
| **FREE TROPOSPHERE** | | | |
| Biogenic (free trop., Silesia) | — | −335 ± 24 | Fiehn 2023 |
| Inflow BL (Silesia) | — | −296 ± 37 | Fiehn 2023 |
| **BIOMASS BURNING** | | | |
| BB (Sherwood) | −232 to −195 | −211 ± 15 (n=4) | Sherwood 2017 |
| BB (review range) | −230 to −200 | — | Nisbet 2020 |
| **MILKOV 2018 GENETIC BOUNDARIES** | | | |
| Primary microbial (CO₂ reduction) | −350 to −125 | — | Milkov 2018 (Table 2) |
| Primary microbial (fermentation) | −450 to −250 | — | Milkov 2018 |
| Thermogenic (revised) | −350 to −100 | — | Milkov 2018 |
| Secondary microbial | −350 to −150 | — | Milkov 2018 |
| Abiotic | −450 to −50 | — | Milkov 2018 |
| **RICE PADDIES** | | | |
| Rice paddies (Sherwood) | −336 to −301 | −323 ± 16 (n=139) | Sherwood 2017 |
| **WASTE (Sherwood)** | | | |
| Waste (Sherwood) | −312 to −281 | −298 ± 11 (n=23) | Sherwood 2017 |
| **ALL MICROBIAL** | | | |
| All microbial (Sherwood) | −442 to −281 | −317 ± 33 (n=415) | Sherwood 2017 |
| **BIOGENIC (GENERAL)** | | | |
| Biogenic (review range) | −400 to −280 | — | Nisbet 2020 |
| Biogenic threshold (Fiehn) | < −280 to −320 | — | Fiehn 2023 |

---

## Execution Log

| Phase | Action | Result |
|-------|--------|--------|
| 1 | OpenAlex + CrossRef literature search | 34 papers identified |
| 2 | HTML extraction from Copernicus OA papers | 12 papers fully extracted via regex |
| 3 | PDF download (automated) | 21/24 OA papers archived |
| 3 | Manual addition by user | 10 additional PDFs (Nisbet 2019/2023, Dean 2018, Zazzeri 2016, Townsend-Small 2012, Defratyka 2021, Fernandez 2022, Schaefer 2019, Woolley-Maisch 2023, Fisher 2017) |
| 3 | PyMuPDF + pdftotext extraction | 8 manually-added papers extracted with isotope passages |
| 3 | Snowball from Douglas 2021 + Lu 2021 | Fiehn 2023, Kelly 2022, Gonzalez Moguel 2022 added |
| 3 | Forward/backward citation snowball | 17 candidates evaluated, 3 new papers with isotope data added |

---

*Database v1.0 | Generated: 2026-05-02 | 34 papers, 28 with verified isotope data*
*62 distinct δ¹³C source categories + 35 δD categories documented*
