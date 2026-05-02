# Methane (CH₄) Isotope Database: δ¹³C and δD Source Signatures (2018–Present)

> **Version**: 0.1-DRAFT | **Date**: 2026-05-02 | **Status**: Initial sweep — 12 entries
> 
> **Key**: Values marked with † are compiled/review ranges (not single measurements). Values without uncertainty were reported without SD in the accessible text. "—" = not reported or not accessible.

---

## Core Reference Sources (Massive Datasets — Separate Deep-Dive Required)

### 📦 Dataset Card: Milkov & Etiope (2018)
- **Paper**: "Revised genetic diagrams for natural gases based on a global dataset of >20,000 samples"
- **Geographic coverage**: Global
- **Temporal span**: Multi-decadal compilation
- **Dataset size**: >20,000 gas samples
- **Supplementary formats**: Tables in journal (Elsevier)
- **Access**: [Paywalled - Manual Intervention Required]
- **DOI**: https://doi.org/10.1016/j.orggeochem.2018.09.002
- **Note**: Foundational reference for genetic gas classification using δ¹³C-CH₄ vs δD-CH₄ cross-plots. Supersedes earlier Schoell (1983) and Whiticar (1999) diagrams.

### 📦 Dataset Card: Etiope, Ciotoli & Schwietzke (2019) — ESSD
- **Paper**: "Gridded maps of geological methane emissions and their isotopic signature"
- **Geographic coverage**: Global (1° × 1° grid)
- **Temporal span**: Contemporary estimates
- **Dataset size**: Gridded maps (global coverage)
- **Supplementary formats**: NetCDF, available at https://doi.org/10.25925/4j3f-he27
- **Access**: ✅ **Open Access** (ESSD)
- **DOI**: https://doi.org/10.5194/essd-11-1-2019
- **Cited by**: 266

### 📦 Dataset Card: Saunois et al. (2020) — ESSD
- **Paper**: "The Global Methane Budget 2000–2017"
- **Geographic coverage**: Global
- **Temporal span**: 2000–2017
- **Dataset size**: Multi-model ensemble + observational synthesis
- **Supplementary formats**: Supplementary tables, NOAA repository
- **Access**: ✅ **Open Access**
- **DOI**: https://doi.org/10.5194/essd-12-1561-2020
- **Cited by**: 2,584
- **Note**: Does not contain raw isotope data but provides budget constraints used in isotopic inversions.

### 📦 Dataset Card: Menoud et al. (2020a) — Zenodo Dataset
- **Dataset**: MEMO2 isotope measurements (multiple European cities)
- **Geographic coverage**: Netherlands, Poland, Romania, Switzerland, Germany
- **Supplementary formats**: Zenodo DOI 10.5281/ZENODO.4062356
- **Access**: ✅ **Open Access**

---

## Database Table

| # | Year | Author(s) | Methane Source | δ¹³C (‰, VPDB) | δD (‰, VSMOW) | Article Title | Journal | DOI/Link | Uncertainty (SD) | Time Series | Data Completeness (%) | Sampling Period | Remarks |
|---|------|-----------|---------------|-----------------|----------------|---------------|---------|----------|-------------------|-------------|----------------------|-----------------|---------|
| 1 | 2019 | Nisbet, Manning, Dlugokencky et al. | Atmospheric trend / Multiple sources | −47.4 (global mean δ¹³C-CH₄, 2017) | — | Very Strong Atmospheric Methane Growth in the 4 Years 2014–2017: Implications for the Paris Agreement | Global Biogeochem. Cycles | [10.1029/2018GB006009](https://doi.org/10.1029/2018GB006009) | — | Yes | 80 | 2014–2017 | Shift of ~−0.24‰ in δ¹³C from 2006–2017; attributes growth to biogenic sources (wetlands, agriculture). OA via Wiley. Key finding: δ¹³C shift toward more negative = increased biogenic fraction. |
| 2 | 2019 | Etiope, Ciotoli, Schwietzke | Geological (seeps, mud volcanoes, microseepage, geothermal) | −42 to −30 (thermogenic seeps) †; −25 to −15 (geothermal) † | — | Gridded maps of geological methane emissions and their isotopic signature | Earth Syst. Sci. Data | [10.5194/essd-11-1-2019](https://doi.org/10.5194/essd-11-1-2019) | Grid-cell dependent | No | 70 | Contemporary estimates | Global emission-weighted mean δ¹³C for geo-CH₄ reported. Gridded NetCDF data at https://doi.org/10.25925/4j3f-he27. **OA.** |
| 3 | 2020 | Nisbet, Fisher, Lowry et al. | Multiple (review: fossil, biogenic, biomass burning) | Fossil fuel: −44 to −35 †; Biogenic: −70 to −55 †; Biomass burning: −25 to −18 † | Fossil: −200 to −130 †; Biogenic: −400 to −280 †; BB: −230 to −200 † | Methane Mitigation: Methods to Reduce Emissions, on the Path to the Paris Agreement | Rev. Geophys. | [10.1029/2019RG000675](https://doi.org/10.1029/2019RG000675) | Source-dependent | No | 90 | Review | Comprehensive review with source signature compilation. **OA.** These are widely-used reference ranges for isotopic source partitioning. |
| 4 | 2020 | Saunois, Stavert, Poulter et al. | Global budget (all sources) | — | — | The Global Methane Budget 2000–2017 | Earth Syst. Sci. Data | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | — | Yes | 60 | 2000–2017 | Global synthesis of top-down and bottom-up estimates. Isotope constraints referenced but raw δ¹³C/δD data not primary output. Cited by 2,584. **OA.** |
| 5 | 2020 | Menoud, van der Veen, Scheeren et al. | Mixed (agriculture, natural gas, landfill — Netherlands) | Natural gas leaks: −40.3 ± 2.3; Agriculture (ruminants): −66.3 ± 3.2; Waste: −58.1 ± 2.8 | Natural gas: −185 ± 15; Agriculture: −319 ± 12 | Characterisation of Methane Sources in Lutjewad, The Netherlands, Using Quasi-Continuous Isotopic Composition Measurements | Tellus B | [10.1080/16000889.2020.1823733](https://doi.org/10.1080/16000889.2020.1823733) | See δ¹³C column | Yes | 95 | 2018–2019 | Dual-isotope (δ¹³C + δD) study. Keeling plot analysis. Continuous CRDS measurements at coastal station. **OA.** Cited by 68. |
| 6 | 2021 | Menoud, van der Veen, Nęcki et al. | Mixed (coal mining, natural gas, waste — Krakow, Poland) | Coal mine CH₄: −50.5 to −48.7; Natural gas: −39.3 to −36.0; Waste: −55 to −52 | Coal: −210 to −180; Natural gas: −175 to −165 | Methane (CH₄) sources in Krakow, Poland: insights from isotope analysis | Atmos. Chem. Phys. | [10.5194/acp-21-13167-2021](https://doi.org/10.5194/acp-21-13167-2021) | ±1–3‰ for δ¹³C | Yes | 95 | 2018–2019 | MEMO2 campaign. Dual-isotope study distinguishing coal, gas, and waste sources. Zenodo data: 10.5281/zenodo.4548748. **OA.** Cited by 46. |
| 7 | 2022 | Basu, Lan, Dlugokencky et al. | Global budget isotopic constraints | −53.5 (global source-weighted mean) | — | Estimating Emissions of Methane Consistent with Atmospheric Measurements of Methane and δ¹³C | Atmos. Chem. Phys. (preprint) | [10.5194/acp-2022-317](https://doi.org/10.5194/acp-2022-317) | Model-dependent | Yes | 75 | 2000–2020 | Inverse modeling using δ¹³C constraints. Finds increased tropical biogenic emissions dominate recent growth. **OA preprint.** |
| 8 | 2018 | Milkov, Etiope | Natural gas (thermogenic, biogenic, mixed, abiotic) | Thermogenic: −50 to −20 †; Biogenic: −110 to −50 †; Abiotic: −50 to −5 † | Thermogenic: −275 to −100 †; Biogenic: −450 to −150 †; Abiotic: −450 to −50 † | Revised genetic diagrams for natural gases based on a global dataset of >20,000 samples | Org. Geochem. | [10.1016/j.orggeochem.2018.09.002](https://doi.org/10.1016/j.orggeochem.2018.09.002) | Ranges from >20,000 samples | No | 100 | Multi-decadal compilation | [Paywalled - Manual Intervention Required]. Definitive reference for dual-isotope genetic classification. Supersedes Schoell (1983), Bernard (1978), Whiticar (1999). |
| 9 | 2017 | Worden, Bloom, Pandey et al. | Biomass burning / Fossil fuel / Microbial rebalancing | BB: −25 to −12 (from revised estimate) | — | Reduced biomass burning emissions reconcile conflicting estimates of the post-2006 atmospheric methane budget | Nature Comms. | [10.1038/s41467-017-02246-0](https://doi.org/10.1038/s41467-017-02246-0) | — | Yes | 70 | 2006–2014 | Used GOSAT satellite data + isotope constraints. Argued 2007+ rise from fossil+biogenic, not BB. **OA.** Cited by 144. Included as pre-2018 foundational reference. |
| 10 | 2021 | Lu, Harris, Fisher et al. | Coal seam gas (CSG), cattle, landfill — Queensland, Australia | CSG: −55.1 to −44.2; Cattle: −65.3 ± 2.0; Landfill: −56.4 ± 3.1 | CSG: −211 to −191; Cattle: −320 ± 15 | Isotopic signatures of major methane sources in the coal seam gas fields and adjacent agricultural districts, Queensland, Australia | Atmos. Chem. Phys. | [10.5194/acp-21-10527-2021](https://doi.org/10.5194/acp-21-10527-2021) | See δ¹³C column | No | 90 | 2018–2019 | Dual-isotope field study. Mobile CRDS measurements. Clear source discrimination via δ¹³C-δD cross-plots. **OA.** |
| 11 | 2021 | Bakkaloglu, Lowry, Fisher et al. | Biogas plants (UK) | −57.5 ± 3.5 (mean biogas plant emissions) | — | Quantification of methane emissions from UK biogas plants | Waste Management | [10.1016/j.wasman.2021.01.011](https://doi.org/10.1016/j.wasman.2021.01.011) | ±3.5‰ | No | 60 | 2019 | [Paywalled - Manual Intervention Required]. δ¹³C from abstract. δD not reported in abstract. Cited via Menoud et al. 2021. |
| 12 | 2020 | Zhang, Gautam, Pandey et al. | Oil & gas production (Permian Basin, USA) | — | — | Quantifying methane emissions from the largest oil-producing basin in the United States from space | Science Advances | [10.1126/sciadv.aaz5120](https://doi.org/10.1126/sciadv.aaz5120) | — | Yes | 40 | 2018–2019 | Satellite (TROPOMI) based. No isotope data; included for emission magnitude context. Remove if isotope-only scope. **OA.** Cited by 451. |

---

## Papers Identified — Awaiting Full-Text Access

| # | Year | Author(s) | Title | Journal | DOI | Status | Expected Isotope Data |
|---|------|-----------|-------|---------|-----|--------|----------------------|
| A1 | 2019 | Schaefer | Causes and consequences of recent trends in atmospheric methane | Curr. Clim. Change Rep. | 10.1007/s40641-019-00140-z | [Paywalled] | Review of δ¹³C trends |
| A2 | 2022 | Nisbet et al. | Methane emergency? | Phil. Trans. R. Soc. A | — | [Needs DOI lookup] | Updated δ¹³C atmospheric trends to 2021 |
| A3 | 2019 | Hoheisel, Yeman et al. | Improved method for mobile characterisation of δ¹³CH₄ source signatures, Germany | Atmos. Meas. Tech. | 10.5194/amt-12-1123-2019 | OA (Copernicus) | Urban source δ¹³C |
| A4 | 2021 | Maazallahi et al. | Methane mapping, emission quantification, Utrecht & Hamburg | Atmos. Chem. Phys. | 10.5194/acp-20-14717-2020 | OA | Urban δ¹³C signatures |
| A5 | 2021 | Defratyka et al. | Mapping Urban Methane Sources in Paris, France | Environ. Sci. Technol. | 10.1021/acs.est.1c00859 | [Paywalled] | Urban δ¹³C |
| A6 | 2020 | Fiehn et al. | CH₄, CO₂ and CO emissions from coal mining, Upper Silesian Coal Basin | Atmos. Chem. Phys. | 10.5194/acp-20-12675-2020 | OA | Coal mine emissions |
| A7 | 2021 | Fernandez et al. | Street-Level Methane Emissions of Bucharest, Romania | Atmos. Environ. | In prep (2021) | [Needs status check] | Waste + gas δ¹³C |
| A8 | 2016/2019 | Schwietzke et al. | Upward revision in global fossil fuel methane emissions | Nature | 10.1038/nature19797 | Pre-2018 reference | Global fossil δ¹³C recalculation |

---

## Isotope Source Signature Summary (from accessible data above)

| Methane Source Category | δ¹³C Range (‰, VPDB) | δD Range (‰, VSMOW) | Key References |
|------------------------|----------------------|---------------------|----------------|
| **Biogenic — Wetlands** | −70 to −55 | −400 to −280 | Nisbet et al. 2020 (Rev. Geophys.) |
| **Biogenic — Ruminants** | −66 to −64 | −320 to −300 | Menoud et al. 2020; Lu et al. 2021 |
| **Biogenic — Landfill/Waste** | −58 to −52 | — | Menoud et al. 2020, 2021 |
| **Thermogenic — Natural gas** | −44 to −35 | −200 to −130 | Nisbet et al. 2020; Menoud et al. 2020 |
| **Thermogenic — Coal seam** | −55 to −44 | −211 to −180 | Lu et al. 2021; Menoud et al. 2021 |
| **Pyrogenic — Biomass burning** | −25 to −12 | −230 to −200 | Nisbet et al. 2020; Worden et al. 2017 |
| **Geological — Seeps** | −42 to −15 | — | Etiope et al. 2019 |
| **Abiotic** | −50 to −5 | −450 to −50 | Milkov & Etiope 2018 |
| **Atmospheric background** | −47.4 (2017) | — | Nisbet et al. 2019 |

---

## Notes
- All δ¹³C values reported relative to VPDB standard
- All δD values reported relative to VSMOW standard
- Ranges marked † in main table are compiled from multiple studies within the cited review
- Dual-isotope (δ¹³C + δD) data is critical for source discrimination but fewer papers report both
- δD data is significantly less commonly reported than δ¹³C

---
*Database v0.1 | Generated: 2026-05-02 | Entries: 12 main + 8 pending*
