# Methane Isotope Geochemistry Database

## Objective
Comprehensive literature database of CH₄ carbon isotopes (δ¹³C) and hydrogen isotopes (δD/δ²H) source signatures, from foundational works (1953) through cutting-edge research (2026).

## Scope
- **116 papers** catalogued (94 with verified isotope data, 22 context/budget-only)
- **140+ distinct δ¹³C** source signature categories
- **85+ δD** source signature categories
- **Sink fractionation (KIE)** section: OH, soil, stratospheric, Cl
- **Temporal span**: Craig 1953 → ESSD 2026; ice core records to 650 kyr BP

## Foundational Literature (1953–1999)

These seminal works established the entire field of methane isotope geochemistry:

| Year | Authors | Contribution |
|------|---------|-------------|
| 1953 | Craig | Established stable carbon isotope fractionation framework; defined PDB standard |
| 1978 | Bernard | Created the Bernard diagram (C₁/(C₂+C₃) vs δ¹³C) for microbial vs thermogenic gas |
| 1980 | Schoell | Pioneered δD use alongside δ¹³C; constructed early C-H dual-isotope plots |
| 1981 | Rice & Claypool | Defined biogenic gas isotopic criteria (δ¹³C < −60‰) |
| 1982 | Stevens & Rust | First high-precision atmospheric δ¹³C-CH₄ measurement (≈ −47.0‰) |
| 1986 | Whiticar, Faber & Schoell | Distinguished CO₂ reduction vs acetate fermentation using δ¹³C + δD |
| 1988 | Quay et al. | First global isotopic CH₄ budget model from Pacific atmosphere |
| 1988 | Chanton & Martens | Demonstrated oxidation fractionation of δ¹³C in seasonal ebullition |
| 1999 | Whiticar | **The Whiticar Diagram** — definitive δ¹³C vs δD classification (most cited reference in the field) |

## Methodology
1. **Literature retrieval**: OpenAlex API, CrossRef API, Google Scholar (manual), Copernicus OA journals
2. **Screening**: Two-phase (abstract → full-text) for papers containing primary measurement data or novel source classifications
3. **Data extraction**: Direct from OA full-text HTML/PDF where accessible; verified reference values for review papers
4. **PDF processing**: MinerU API (PDF→Markdown with table preservation) + PyMuPDF fallback
5. **Snowballing**: Reference lists of core papers vetted for additional high-relevance studies

## Data Sources & Access
- **Open Access**: Copernicus (ESSD, ACP, AMT), AGU (GBC, GRL), Nature Communications, Frontiers, MDPI
- **Paywalled**: Marked as `❌ PW` — isotope values from abstracts or known literature compilation
- **Supplementary data**: URLs provided for large datasets

## Tools Used
- **MinerU (mineru.net API)**: PDF→Markdown conversion with table preservation
- **PyMuPDF (fitz)**: Fallback PDF text extraction
- **OpenAlex/CrossRef APIs**: Bibliographic metadata, citation counts, OA status verification
- **paper-qa 4.9.0**: Available for PDF Q&A extraction

## Database Structure
See `database.md` for:
1. **Deep-dive cards** — Detailed extraction summaries for key papers
2. **Main table** — 116 entries with ID, year, authors, source type, isotope values, DOI, citations, access status
3. **δ¹³C source signature summary** — 140+ categories organized by source type
4. **δD source signature summary** — 85+ categories
5. **Sink fractionation (KIE)** — OH, soil, stratospheric, Cl sink fractionation factors
6. **Clumped isotopes (Δ₁₈)** — Thermogenic vs biogenic formation temperatures
7. **Pre-industrial budget** — Lassey 2007 complete 13-category reconstruction
8. **Methodology log** — Phase-by-phase data collection record

## Classification System
- **Biogenic (microbial)**: Wetlands, rice paddies, ruminants, landfills, termites, freshwater lakes
  - *CO₂ reduction*: δ¹³C −110 to −60‰, δD −250 to −170‰ (Whiticar 1986/1999)
  - *Acetate fermentation*: δ¹³C −65 to −50‰, δD −400 to −250‰ (Whiticar 1986/1999)
- **Thermogenic**: Natural gas, coal seams, associated/non-associated gas
  - δ¹³C −50 to −20‰, δD −275 to −100‰ (Whiticar 1999)
- **Pyrogenic**: Incomplete combustion (C₃: −28 to −25‰; C₄: −18 to −12‰)
- **Geological**: Natural seeps, mud volcanoes, geothermal, microseepage
- **Abiogenic**: δ¹³C −50 to +10‰ (Whiticar 1999; Milkov 2018)

## Data Integrity Protocol
- Isotopic values recorded ONLY when directly stated in accessible text (abstract, HTML body, or accessible table)
- Values from review papers that compile multiple sources are noted with "Review/Compilation" or †
- Uncertainty (SD) recorded when reported; "—" otherwise
- NO interpolated or guessed values
- Citation counts from OpenAlex (approximate for pre-digital era papers)

## Version History
| Version | Entries | Phase | Era covered |
|---------|---------|-------|-------------|
| 1.0 | 22 | 1–3 | 2017–2023 initial sweep |
| 2.0 | 62 | 4–5 | + 2024–2026 deep research |
| 3.0 | 83 | 6 | + 2010–2016 |
| 4.0 | 107 | 7 | + 2002–2010 |
| 5.0 | 116 | 8 | + 1953–1999 foundational literature |

---
*Generated: 2026-05-02 | Last updated: 2026-05-03 (v5.0)*

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
