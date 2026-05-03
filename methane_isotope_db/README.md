# Methane Isotope Geochemistry Database

## Objective
Systematic review of literature (2018–present) on CH₄ carbon isotopes (δ¹³C) and hydrogen isotopes (δD/δ²H) for constructing a structured geochemical database.

## Methodology
1. **Literature retrieval**: OpenAlex API, CrossRef API, Google Scholar (manual), Copernicus OA journals
2. **Screening**: Two-phase (abstract → full-text) for papers containing primary measurement data or novel source classifications
3. **Data extraction**: Direct from OA full-text HTML/PDF where accessible; verified reference values for review papers
4. **Snowballing**: Reference lists of core papers vetted for additional high-relevance studies

## Data Sources & Access
- **Open Access**: Copernicus (ESSD, ACP, AMT), AGU (GBC, GRL), Nature Communications, Frontiers, MDPI
- **Paywalled**: Marked as `[Paywalled - Manual Intervention Required]`
- **Supplementary data**: URLs provided for large datasets

## Tools Used
- **paper-qa 4.9.0**: Installed and available for PDF Q&A extraction
- **MinerU (magic-pdf 1.3.12)**: Installed for PDF→Markdown conversion
- **gpt-researcher**: Installed but non-functional (langchain compatibility issue)
- **OpenAlex/CrossRef APIs**: Bibliographic metadata and OA status verification

## Database Structure
See `database.md` for the main table.

## Classification Notes
- **Biogenic**: Microbial methanogenesis (wetlands, rice paddies, ruminants, landfills, termites)
- **Thermogenic**: Thermal cracking of organic matter (natural gas, coal seams)
- **Pyrogenic**: Incomplete combustion of biomass/biofuel
- **Geological**: Natural seeps (onshore/offshore), mud volcanoes, geothermal, microseepage
- **Atmospheric background**: Global mean tropospheric CH₄

## Status
- Phase 1: Initial literature sweep ✅ (in progress)
- Phase 2: Data extraction from OA papers 🔄
- Phase 3: Manual intervention for paywalled sources ⏳

## Data Integrity Protocol
- Isotopic values recorded ONLY when directly stated in accessible text (abstract, HTML body, or accessible table)
- Values from review papers that compile multiple sources are noted with "Review/Compilation" in Remarks
- Uncertainty (SD) recorded when reported; blank otherwise
- NO interpolated or guessed values

---
*Generated: 2026-05-02 | Last updated: 2026-05-02*

---

## MinerU Extractions (Phase 5)

**Date**: 2026-05-03

All PDFs have been re-processed through the [MinerU API](https://mineru.net) for high-quality PDF→Markdown conversion with table preservation.

**Location**: `mineru_extractions/` directory

**Results**: 30 out of 33 PDFs successfully converted. 3 failures (parsing issues): `feinberg2018`, `hmiel2020`, `kirschke2013`.

The MinerU extractions preserve:
- Tables (as HTML `<table>` elements)
- Mathematical expressions
- Figures references
- Full document structure

These replace the earlier PyMuPDF text extractions in `extracted/` for better data quality.
