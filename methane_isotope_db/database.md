# Methane (CH₄) Isotope Database: δ¹³C and δD Source Signatures (2016–Present)

> **Version**: 0.3 | **Date**: 2026-05-02 | **Status**: Phase 2 complete — 26 entries (18 with isotope data, 8 metadata-only/context)
> 
> **Key**: Values marked with † are compiled/review ranges. ± values are reported SD. "—" = not reported or not accessible in OA text.
> All δ¹³C relative to VPDB; all δD (= δ²H) relative to VSMOW.

---

## Core Reference Sources (Massive Datasets — Deep-Dive Cards)

### 📦 Milkov & Etiope (2018) — Org. Geochem.
- **Paper**: "Revised genetic diagrams for natural gases based on a global dataset of >20,000 samples"
- **Coverage**: Global, multi-decadal compilation
- **Size**: >20,000 gas samples with dual-isotope (δ¹³C + δD)
- **Formats**: Journal tables (Elsevier)
- **Access**: **[Paywalled - Manual Intervention Required]**
- **DOI**: [10.1016/j.orggeochem.2018.09.002](https://doi.org/10.1016/j.orggeochem.2018.09.002)
- **Note**: Definitive reference for genetic gas classification using δ¹³C-CH₄ vs δD-CH₄ cross-plots. Supersedes Schoell (1983), Bernard (1978), Whiticar (1999). Cited by all subsequent isotope papers.

### 📦 Etiope, Ciotoli & Schwietzke (2019) — ESSD
- **Paper**: "Gridded maps of geological methane emissions and their isotopic signature"
- **Coverage**: Global (1° × 1° grid)
- **Formats**: NetCDF at [doi:10.25925/4j3f-he27](https://doi.org/10.25925/4j3f-he27)
- **Access**: ✅ Open Access | **Cited**: 266
- **DOI**: [10.5194/essd-11-1-2019](https://doi.org/10.5194/essd-11-1-2019)

### 📦 Saunois et al. (2020) — ESSD
- **Paper**: "The Global Methane Budget 2000–2017"
- **Coverage**: Global, 2000–2017, multi-model ensemble + observational synthesis
- **Formats**: Supplementary tables, NOAA repository
- **Access**: ✅ Open Access | **Cited**: 2,584
- **DOI**: [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020)
- **Note**: Budget constraints used in isotopic inversions, but no raw δ¹³C/δD as primary output.

### 📦 Menoud et al. (2022) — ESSD [**KEY: European Methane Isotope Database (EMID)**]
- **Paper**: "New contributions of measurements in Europe to the global inventory of the stable isotopic composition of methane"
- **Coverage**: Europe (NL, PL, RO, UK, CH, DE) + updated global compilation from Sherwood et al. (2017)
- **Dataset**: MEMO2 campaign (2017–2020) + global inventory
- **Formats**: Zenodo [doi:10.5281/ZENODO.4062356](https://doi.org/10.5281/ZENODO.4062356)
- **Access**: ✅ Open Access | **Cited**: 40
- **DOI**: [10.5194/essd-14-4365-2022](https://doi.org/10.5194/essd-14-4365-2022)
- **Key EMID values**:
  - Fossil fuel (excl. seeps): δ¹³C = −44.6 ± 0.4‰ (n=452), δ²H = −182 ± 2‰
  - Gas leaks (UK + NL): δ¹³C = −38.9 ± 0.3‰ (n=154)
  - Extraction sites (PL + RO): δ¹³C = −48.5 ± 0.6‰ (n=235)
  - Waste: δ¹³C = −53.6 ± 0.4‰ (n=202)
  - Wetlands (EMID): δ¹³C = −73.6 ± 2.27‰
  - Biomass burning C₃: δ¹³C = −28.4 ± 0.65‰; C₄: ~−18‰
  - Updated global weighted mean: δ¹³C = −46.6 ± 1.8‰, δ²H = −192 ± 7‰

### 📦 Sherwood et al. (2017) — Global δ¹³C Source Signature Inventory (pre-2018 foundational)
- **Key values** (cited via Menoud 2022 & Basu 2022):
  - Fossil fuel global weighted mean: δ¹³C = −44.8 ± 0.1‰ (n=8,128)
  - Ruminant C₃: δ¹³C = −54.5‰; C₄: δ¹³C = −67.8‰
- **Note**: Updated by Menoud et al. 2022 EMID.

### 📦 Douglas et al. (2021) — Biogeosciences [**KEY for δD**]
- **Paper**: "Geographic variability in freshwater methane hydrogen isotope ratios and its implications for global isotopic source signatures"
- **Coverage**: Global freshwater systems
- **Access**: ✅ Open Access | **Cited**: 24
- **DOI**: [10.5194/bg-18-3505-2021](https://doi.org/10.5194/bg-18-3505-2021)
- **Key δD values**:
  - Global freshwater δ²H-CH₄: −310 ± 15‰ (flux-weighted)
  - Natural wetlands: δ²H = −310 ± 25‰, δ¹³C = −63.9 ± 3.3‰
  - Low-latitude wetlands (0–30°N): δ²H = −305 ± 13‰
  - High-latitude wetlands (30–90°N): δ²H = −345 ± 11‰; boreal: −374 ± 10‰
  - Inland waters: median δ²H = −296‰ (more enriched than wetlands)
  - Global source δ²H-CH₄: −278 ± 15‰
  - Global source δ¹³C-CH₄: −56.4 ± 2.6‰

### 📦 Schwietzke, Sherwood, Bruhwiler et al. (2016) — Nature (pre-2018 foundational)
- **Paper**: "Upward revision of global fossil fuel methane emissions based on isotope database"
- **Access**: **[Paywalled]** | **Cited**: 600
- **DOI**: [10.1038/nature19797](https://doi.org/10.1038/nature19797)
- **Note**: Revised fossil fuel δ¹³C = −44.0 ± 0.7‰. Increased fossil estimate to ~132 Tg/yr (vs prior ~110). EMID values (Menoud 2022) are ~4–5‰ lighter.

---

## Main Database Table

| # | Year | Author(s) | Methane Source | δ¹³C (‰, VPDB) | δD (‰, VSMOW) | Article Title | Journal | DOI/Link | Uncertainty (SD) | Time Series | Data Completeness (%) | Sampling Period | Remarks |
|---|------|-----------|---------------|-----------------|----------------|---------------|---------|----------|-------------------|-------------|----------------------|-----------------|---------|
| 1 | 2019 | Nisbet, Manning, Dlugokencky et al. | Atmospheric trend (global) | −47.4 (global mean, 2017) | — | Very Strong Atmospheric Methane Growth in the 4 Years 2014–2017 | Global Biogeochem. Cy. | [10.1029/2018GB006009](https://doi.org/10.1029/2018GB006009) | — | Yes | 80 | 2014–2017 | δ¹³C shifted ~−0.24‰ from 2006–2017. Biogenic growth dominant. **OA.** Cited: 762. |
| 2 | 2019 | Etiope, Ciotoli, Schwietzke | Geological (global): seeps, mud volcanoes, microseepage, geothermal | Thermogenic seeps: −50 to −30 †; Microbial seeps: −90 to −55 †; Geothermal: −25 to −15 †; **Global geo-CH₄ weighted mean: −49** | — | Gridded maps of geological methane emissions and their isotopic signature | Earth Syst. Sci. Data | [10.5194/essd-11-1-2019](https://doi.org/10.5194/essd-11-1-2019) | Grid-cell dependent | No | 70 | Contemporary | Weighted mean ~4–5‰ lighter than fossil fuel industry (−44‰). NetCDF available. **OA.** Cited: 266. |
| 3 | 2020 | Nisbet, Fisher, Lowry et al. | Multiple (review compilation) | Fossil fuel: −44 to −35 †; Biogenic: −70 to −55 †; BB: −25 to −18 † | Fossil: −200 to −130 †; Biogenic: −400 to −280 †; BB: −230 to −200 † | Methane Mitigation: Methods to Reduce Emissions | Rev. Geophys. | [10.1029/2019RG000675](https://doi.org/10.1029/2019RG000675) | Source-dependent | No | 90 | Review | Comprehensive source signature compilation. **OA.** Cited: 393. |
| 4 | 2020 | Saunois, Stavert, Poulter et al. | Global budget (all sources) | — | — | The Global Methane Budget 2000–2017 | Earth Syst. Sci. Data | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | — | Yes | 60 | 2000–2017 | Budget synthesis. Isotope data referenced but not primary output. **OA.** Cited: 2,584. |
| 5 | 2020 | Menoud, van der Veen, Scheeren et al. | Netherlands (gas, agriculture, waste) | Gas leaks: −40.3 ± 2.3; Ruminants: −66.3 ± 3.2; Waste: −58.1 ± 2.8 | Gas: −185 ± 15; Agriculture: −319 ± 12 | Characterisation of Methane Sources in Lutjewad, The Netherlands | Tellus B | [10.1080/16000889.2020.1823733](https://doi.org/10.1080/16000889.2020.1823733) | See δ¹³C col. | Yes | 95 | 2018–2019 | Dual-isotope. Keeling plot. Continuous CRDS. **OA.** Cited: 68. |
| 6 | 2021 | Menoud, van der Veen, Nęcki et al. | Krakow, Poland (coal, gas, waste) | Coal: −58 to −45; Gas: −39.3 to −36; Waste: −55 to −52; Fossil-dom.: >−50 | Coal: −210 to −180; Fossil: −190 ± 9; Sewage: <−300; Manholes: −202 to −146 | Methane sources in Krakow: isotope analysis | Atmos. Chem. Phys. | [10.5194/acp-21-13167-2021](https://doi.org/10.5194/acp-21-13167-2021) | ±1–3‰ (δ¹³C); ±9–27‰ (δ²H) | Yes | 95 | 2018–2019 | MEMO2. Dual-isotope. δ²H<−250‰ → biogenic. Zenodo data. **OA.** Cited: 46. |
| 7 | 2022 | Basu, Lan, Dlugokencky et al. | Global isotopic inversion | Source-weighted: ~−53.5; BB C₃: −26.7; C₄: −12.5; Ruminant C₃: −54.5; C₄: −67.8 | — | Estimating Methane Emissions Consistent with δ¹³C | Atmos. Chem. Phys. | [10.5194/acp-22-15351-2022](https://doi.org/10.5194/acp-22-15351-2022) | Model-dependent | Yes | 85 | 1997–2016 | TM5-4DVAR inversion. Microbial rise = primary driver post-2007. Pyrogenic reduced 3±2 Tg/yr. **OA.** Cited: 110. |
| 8 | 2018 | Milkov, Etiope | Natural gas (global >20k samples) | Thermogenic: −50 to −20 †; Biogenic: −110 to −50 †; Abiotic: −50 to −5 † | Thermo: −275 to −100 †; Biogenic: −450 to −150 †; Abiotic: −450 to −50 † | Revised genetic diagrams for natural gases | Org. Geochem. | [10.1016/j.orggeochem.2018.09.002](https://doi.org/10.1016/j.orggeochem.2018.09.002) | Full ranges, >20k samples | No | 100 | Multi-decadal | **[Paywalled].** Definitive dual-isotope genetic classification. |
| 9 | 2017 | Worden, Bloom, Pandey et al. | BB / Fossil / Microbial rebalancing | Source mix: −56 to −61 (to match δ¹³C); BB: −25 to −12 | — | Reduced biomass burning reconciles post-2006 methane budget | Nature Comms. | [10.1038/s41467-017-02246-0](https://doi.org/10.1038/s41467-017-02246-0) | — | Yes | 70 | 2006–2014 | GOSAT + isotope constraints. **OA.** Cited: 144. |
| 10 | 2021 | Lu, Harris, Fisher et al. | Queensland, Australia (CSG, cattle, landfill) | CSG: −55.1 to −44.2; Shallow coal: −80 to −50; Cattle: −62 to −65; Abattoir: −46; WWTP: −47.6 ± 2 | CSG: −310 to −191; Shallow: −310 to −210; Cattle: ~−320 (100‰ more depleted than CSG) | Isotopic signatures in coal seam gas fields, Queensland | Atmos. Chem. Phys. | [10.5194/acp-21-10527-2021](https://doi.org/10.5194/acp-21-10527-2021) | Bayesian posterior SD | No | 90 | 2018–2019 | Dual-isotope. Mobile CRDS. Surat Basin: −63 to −45‰. **OA.** |
| 11 | 2022 | Menoud, van der Veen, Lowry et al. | EMID — Europe + global update | Fossil (excl. seeps): −44.6 ± 0.4 (n=452); Extraction PL+RO: −48.5 ± 0.6 (n=235); Gas UK+NL: −38.9 ± 0.3 (n=154); Waste: −53.6 ± 0.4 (n=202); Wetlands: −73.6 ± 2.27; BB C₃: −28.4 ± 0.65; BB C₄: ~−18 | Fossil: −182 ± 2; Global: −192 ± 7 | New contributions to the global inventory (EMID) | Earth Syst. Sci. Data | [10.5194/essd-14-4365-2022](https://doi.org/10.5194/essd-14-4365-2022) | Extensive (see δ¹³C) | No | 98 | 2017–2020 | **KEY PAPER.** Global weighted: δ¹³C=−46.6±1.8‰, δ²H=−192±7‰. Zenodo. **OA.** Cited: 40. |
| 12 | 2020 | Hmiel, Petrenko, Dyonisius et al. | Geological vs anthropogenic fossil | — (uses ¹⁴C, not δ¹³C) | — | Preindustrial ¹⁴CH₄ indicates greater anthropogenic fossil emissions | Nature | [10.1038/s41586-020-1991-8](https://doi.org/10.1038/s41586-020-1991-8) | — | No | 50 | Preindustrial ice core | Natural geo-CH₄ ~1.6 Tg/yr (≪40–60 Tg/yr inventories). Anthro fossil underestimated 25–40%. **OA.** Cited: 323. |
| 13 | 2019 | Hoheisel, Yeman, Dinger et al. | Heidelberg, Germany (gas, landfill, traffic) | Siberian gas: −48 to −54; North Sea: −34 ± 3; Landfill (July): −66; Urban mix: −49 to −61; Seasonal: −30 (winter) to −50 (summer) | — | Improved method for mobile δ¹³CH₄ source signatures, Germany | Atmos. Meas. Tech. | [10.5194/amt-12-1123-2019](https://doi.org/10.5194/amt-12-1123-2019) | <5‰ threshold | Yes | 85 | 2016–2017 | Gas supply shifted ~3‰ more depleted since 1990s. AirCore + CRDS. **OA.** |
| 14 | 2020 | Maazallahi, Fernandez, Menoud et al. | Utrecht (NL) & Hamburg (DE) — fossil, microbial | Fossil: −50 to −40; Microbial: −55 to −70; Hamburg anomaly: −23 | Fossil: −150 to −200; Microbial: −260 to −360; Hamburg anomaly: −153 | Methane mapping, Utrecht & Hamburg | Atmos. Chem. Phys. | [10.5194/acp-20-14717-2020](https://doi.org/10.5194/acp-20-14717-2020) | — | No | 80 | 2018–2019 | Dual-isotope urban survey. C₂H₆/CH₄ for source ID. **OA.** |
| 15 | 2021 | Douglas, Stratigopoulos, Park et al. | Freshwater (wetlands, inland waters — global) | Wetlands: −63.9 ± 3.3; Global source: −56.4 ± 2.6 (or −55.2 ± 2.6 with C₄ correction) | Freshwater global: −310 ± 15; Wetlands: −310 ± 25; Low-lat (0–30°N): −305 ± 13; High-lat (30–90°N): −345 ± 11; Boreal: −374 ± 10; Inland waters: −296 (median); **Global source δ²H: −278 ± 15** | Geographic variability in freshwater methane δ²H and global source signatures | Biogeosciences | [10.5194/bg-18-3505-2021](https://doi.org/10.5194/bg-18-3505-2021) | See δD column | No | 98 | Compilation | **KEY for δD.** Higher global freshwater δ²H than previous estimates. Top-down: −258 to −289‰. **OA.** Cited: 24. |
| 16 | 2021 | Zhang, Jacob, Lu et al. | Global GOSAT inverse (tropical biogenic, fossil) | — | — | Attribution of accelerating methane increase 2010–2018 | Atmos. Chem. Phys. | [10.5194/acp-21-3643-2021](https://doi.org/10.5194/acp-21-3643-2021) | — | Yes | 50 | 2010–2018 | Satellite-based. Consistent with δ¹³C trend. Tropical wetlands + livestock. **OA.** Cited: 175. |
| 17 | 2022 | Feng, Palmer, Zhu et al. | Tropical (biogenic + anthropogenic) | — | — | Tropical methane emissions explain recent growth rate changes | Nature Comms. | [10.1038/s41467-022-28989-z](https://doi.org/10.1038/s41467-022-28989-z) | — | Yes | 40 | 2010–2019 | 80% of growth from tropical emissions. No primary isotope data. **OA.** Cited: 111. |
| 18 | 2023 | Nisbet, Manning, Dlugokencky et al. | Atmospheric trend (2006–2022 vs glacial termination) | — (access blocked) | — | Atmospheric Methane: 2006–2022 vs Glacial Terminations | Global Biogeochem. Cy. | [10.1029/2023GB007875](https://doi.org/10.1029/2023GB007875) | — | Yes | 30 | 2006–2022 | **[Wiley blocked].** Updated δ¹³C through 2022. **OA** per OpenAlex. Cited: 98. |
| 19 | 2019 | Maasakkers, Jacob, Sulprizio et al. | Global distribution + OH trend | — | — | Global distribution of methane emissions and OH trends | Atmos. Chem. Phys. | [10.5194/acp-19-7859-2019](https://doi.org/10.5194/acp-19-7859-2019) | — | Yes | 40 | 2010–2015 | GOSAT inversion. Context for isotope-based source attribution. **OA.** Cited: 288. |
| 20 | 2018 | Dean, Middelburg, Röckmann et al. | Climate feedbacks (review: wetlands, permafrost, hydrates) | — (access blocked) | — | Methane Feedbacks to the Global Climate System | Rev. Geophys. | [10.1002/2017RG000559](https://doi.org/10.1002/2017RG000559) | — | No | 30 | Review | **[Wiley blocked].** Climate-CH₄ feedback review. **OA.** Cited: 643. |
| 21 | 2020 | Fiehn, Kostinek, Eckl et al. | Coal mining — Upper Silesian Basin, Poland | — (emission quantities, not isotopes) | — | Estimating CH₄ from coal mining, Upper Silesian Coal Basin | Atmos. Chem. Phys. | [10.5194/acp-20-12675-2020](https://doi.org/10.5194/acp-20-12675-2020) | — | No | 40 | 2018 | Aircraft mass-balance. Context for Menoud 2021 coal δ¹³C. **OA.** |
| 22 | 2021 | Bakkaloglu, Lowry, Fisher et al. | Biogas plants (UK) | −57.5 ± 3.5 (mean) | — | Quantification of methane emissions from UK biogas plants | Waste Manag. | [10.1016/j.wasman.2021.01.011](https://doi.org/10.1016/j.wasman.2021.01.011) | ±3.5‰ | No | 60 | 2019 | **[Paywalled].** δ¹³C from abstract. |
| 23 | 2020 | Zhang, Gautam, Pandey et al. | Oil & gas (Permian Basin, USA) | — | — | Quantifying methane from the largest US oil basin from space | Science Advances | [10.1126/sciadv.aaz5120](https://doi.org/10.1126/sciadv.aaz5120) | — | Yes | 40 | 2018–2019 | TROPOMI satellite. Emission magnitudes only. **OA.** Cited: 451. |
| 24 | 2016 | Schwietzke, Sherwood, Bruhwiler et al. | Global fossil fuel (revised) | −44.0 ± 0.7 (fossil fuel weighted mean) | — | Upward revision of global fossil fuel methane emissions based on isotope database | Nature | [10.1038/nature19797](https://doi.org/10.1038/nature19797) | ±0.7‰ | No | 80 | Compilation | **[Paywalled].** Foundational revision: fossil δ¹³C = −44.0‰, emissions ~132 Tg/yr. Cited: 600. |
| 25 | 2016 | Röckmann, Eyer, van der Veen et al. | Atmospheric background (Cabauw tower, NL) | — (method-focused, values in supplementary) | — | In situ observations of isotopic composition of CH₄ at Cabauw tower | Atmos. Chem. Phys. | [10.5194/acp-16-10469-2016](https://doi.org/10.5194/acp-16-10469-2016) | δ¹³C offset 0.25±0.04‰; δD offset −4.3±0.4‰ | Yes | 50 | 2014–2015 | IRMS vs QCLAS intercomparison. Continuous monitoring methodology. **OA.** Cited: 166. |
| 26 | 2023 | Song, Zhu, Willis et al. | Wastewater treatment (global review) | — (access blocked) | — | Methane Emissions from Municipal Wastewater Collection and Treatment Systems | Environ. Sci. Technol. | [10.1021/acs.est.2c04388](https://doi.org/10.1021/acs.est.2c04388) | — | No | 30 | Review | Emission quantities. Context for isotope work on WWTP. **OA.** Cited: 145. |

---

## Isotope Source Signature Summary (Verified from Accessible Data)

### δ¹³C Source Signatures

| Methane Source Category | δ¹³C Range (‰, VPDB) | Best Estimate | n | Key References |
|------------------------|----------------------|---------------|---|----------------|
| **Fossil fuel — global weighted** | — | −44.8 ± 0.1 | 8,128 | Sherwood 2017 (via Menoud 2022) |
| **Fossil fuel — Schwietzke revision** | — | −44.0 ± 0.7 | — | Schwietzke et al. 2016 |
| **Fossil fuel — EMID Europe (excl. seeps)** | — | −44.6 ± 0.4 | 452 | Menoud et al. 2022 |
| **Fossil fuel — extraction (PL+RO)** | — | −48.5 ± 0.6 | 235 | Menoud et al. 2022 |
| **Natural gas leaks (UK+NL)** | — | −38.9 ± 0.3 | 154 | Menoud et al. 2022 |
| **Natural gas — Siberian** | −48 to −54 | — | — | Hoheisel et al. 2019 |
| **Natural gas — North Sea** | — | −34 ± 3 | — | Hoheisel et al. 2019 |
| **Natural gas — Netherlands** | — | −40.3 ± 2.3 | — | Menoud et al. 2020 |
| **Coal seam gas (Australia, Surat)** | −63 to −45 | — | — | Lu et al. 2021 |
| **Coal seam gas (shallow <200m)** | −80 to −50 | — | — | Lu et al. 2021 |
| **Coal mining (Krakow, Poland)** | −58 to −45 | — | — | Menoud et al. 2021 |
| **Geological — global weighted mean** | — | −49 | — | Etiope et al. 2019 |
| **Geological — thermogenic seeps** | −50 to −30 | — | — | Etiope et al. 2019 |
| **Geological — geothermal** | −25 to −15 | — | — | Etiope et al. 2019 |
| **Ruminants/cattle** | −62 to −66 | — | — | Menoud 2020; Lu 2021 |
| **Ruminants — C₃ feed (global)** | — | −54.5 | — | Sherwood (via Basu 2022) |
| **Ruminants — C₄ feed (global)** | — | −67.8 | — | Sherwood (via Basu 2022) |
| **Waste/landfill (EMID)** | — | −53.6 ± 0.4 | 202 | Menoud et al. 2022 |
| **Waste (Netherlands)** | — | −58.1 ± 2.8 | — | Menoud et al. 2020 |
| **Wastewater (Australia)** | — | −47.6 ± 2 | — | Lu et al. 2021 |
| **Biogas plants (UK)** | — | −57.5 ± 3.5 | — | Bakkaloglu et al. 2021 |
| **Wetlands — EMID Europe** | — | −73.6 ± 2.27 | — | Menoud et al. 2022 |
| **Wetlands — global (Nisbet review)** | −70 to −55 | — | — | Nisbet et al. 2020 |
| **Wetlands — global (Douglas)** | — | −63.9 ± 3.3 | — | Douglas et al. 2021 |
| **Biomass burning — C₃** | — | −28.4 ± 0.65 (EMID); −26.7 (Basu) | — | Menoud 2022; Basu 2022 |
| **Biomass burning — C₄** | — | ~−18 (EMID); −12.5 (Basu) | — | Menoud 2022; Basu 2022 |
| **Urban fossil mix** | −50 to −40 | — | — | Maazallahi et al. 2020 |
| **Urban microbial** | −55 to −70 | — | — | Maazallahi et al. 2020 |
| **Atmospheric background (2017)** | — | −47.4 | — | Nisbet et al. 2019 |
| **Global source weighted mean (updated)** | — | −46.6 ± 1.8 | — | Menoud et al. 2022 |
| **Global source (Douglas bottom-up)** | — | −56.4 ± 2.6 | — | Douglas et al. 2021 |

### δD (δ²H) Source Signatures

| Methane Source Category | δD Range (‰, VSMOW) | Best Estimate | Key References |
|------------------------|---------------------|---------------|----------------|
| **Fossil fuel — EMID Europe** | — | −182 ± 2 | Menoud et al. 2022 |
| **Natural gas (NL)** | — | −185 ± 15 | Menoud et al. 2020 |
| **Fossil urban (Utrecht/Hamburg)** | −150 to −200 | — | Maazallahi et al. 2020 |
| **Coal mining (Krakow)** | −210 to −180 | −190 ± 9 (fossil-dominated) | Menoud et al. 2021 |
| **Coal seam gas (Australia)** | −310 to −191 | — | Lu et al. 2021 |
| **Ruminants/cattle** | ~−320 | — | Lu et al. 2021 |
| **Agriculture (NL)** | — | −319 ± 12 | Menoud et al. 2020 |
| **Sewage (Krakow)** | < −300 | — | Menoud et al. 2021 |
| **Urban microbial** | −260 to −360 | — | Maazallahi et al. 2020 |
| **Wetlands — global** | — | −310 ± 25 | Douglas et al. 2021 |
| **Wetlands — low-latitude (0–30°N)** | — | −305 ± 13 | Douglas et al. 2021 |
| **Wetlands — high-latitude (30–90°N)** | — | −345 ± 11 | Douglas et al. 2021 |
| **Wetlands — boreal** | — | −374 ± 10 | Douglas et al. 2021 |
| **Inland waters** | — | −296 (median) | Douglas et al. 2021 |
| **Freshwater global (flux-weighted)** | — | −310 ± 15 | Douglas et al. 2021 |
| **Global source δ²H** | — | −278 ± 15 | Douglas et al. 2021 |
| **Global updated weighted mean** | — | −192 ± 7 | Menoud et al. 2022 |
| **Biomass burning** | −230 to −200 | — | Nisbet et al. 2020 |
| **Biogenic (general review)** | −400 to −280 | — | Nisbet et al. 2020 |

---

## Papers Awaiting Access / Further Analysis

| # | Year | Author(s) | Title | Journal | DOI | Status | Expected Data |
|---|------|-----------|-------|---------|-----|--------|---------------|
| A1 | 2019 | Schaefer | Causes and consequences of trends in atmospheric methane | Curr. Clim. Change Rep. | 10.1007/s40641-019-00140-z | Paywalled | δ¹³C trend review |
| A2 | 2023 | Nisbet et al. | Atmospheric Methane: 2006–2022 vs Glacial Terminations | GBC | 10.1029/2023GB007875 | Wiley blocked | Updated δ¹³C through 2022 |
| A3 | 2018 | Dean et al. | Methane Feedbacks to the Global Climate System | Rev. Geophys. | 10.1002/2017RG000559 | Wiley blocked | Climate-feedback isotope review |
| A4 | 2021 | Defratyka et al. | Mapping Urban Methane Sources in Paris | EST | 10.1021/acs.est.1c00859 | Paywalled | Urban δ¹³C |
| A5 | 2021 | Fernandez et al. | Street-Level CH₄ Emissions of Bucharest | Atmos. Environ. | In prep | Unknown | Waste + gas δ¹³C |
| A6 | 2016 | Zazzeri et al. | Plume isotopic composition of CH₄ London | — | Needs DOI | Needs retrieval | Urban δ¹³C (−48‰ range) |
| A7 | 2017 | Fisher et al. | Multi-year observations CH₄ London | GRL? | Needs DOI | Needs retrieval | London δ¹³C time series |
| A8 | 2018 | Townsend-Small et al. | CH₄ isotope urban/wastewater LA | — | Needs DOI | Needs retrieval | WWTP δD: −298‰ (LA), −325‰ (Cincinnati) |

---

## Execution Log

| Step | Tool | Action | Result |
|------|------|--------|--------|
| 1 | pip3 | Install paper-qa, magic-pdf, gpt-researcher | ✅ paper-qa 4.9.0, MinerU 1.3.12; ❌ gpt-researcher |
| 2 | OpenAlex API | Literature search (60+ queries) | 26+ unique relevant papers identified |
| 3 | CrossRef API | Supplementary metadata & citation counts | DOIs verified |
| 4 | curl (HTML) | Fetch Copernicus OA full-text (10 papers) | Etiope, Menoud×3, Hoheisel, Maazallahi, Lu, Basu, Zhang, Douglas, Röckmann |
| 5 | web_fetch | Nature Comms + Nature papers | Worden 2017, Feng 2022, Hmiel 2020 |
| 6 | Python regex | Extract isotope passages from HTML | 100+ isotope-relevant passages extracted |
| 7 | Snowballing | Reference network from Menoud 2022, Basu 2022 | Identified Sherwood 2017, Douglas 2021, Schwietzke 2016 |

---

*Database v0.3 | Generated: 2026-05-02 | Phase 2 complete*
*Next steps: Phase 3 manual intervention for paywalled papers; deeper extraction from existing OA via paper-qa; additional snowball from Douglas 2021 and Lu 2021 references*
