# PDF Download Status — 2002–2010 Papers

**Date**: 2026-05-03 | **Total papers**: 24 | **Downloaded**: 4 | **Blocked**: 20

## ✅ Successfully Downloaded

| File | Size | Source |
|------|------|--------|
| `Lassey2007_ACP_centennial.pdf` | 429 KB | Copernicus (direct OA PDF) |
| `Houweling2006_GRL.pdf` | 1.4 MB | VU University Repository (author's copy) |
| `Bousquet2006_Nature_full.html` | 341 KB | nature.com full-text HTML (includes abstract + body + methods + refs) |
| `Keppler2006_Nature_full.html` | 276 KB | nature.com full-text HTML |

## ❌ Blocked by Cloudflare/Publisher — AGU/Wiley (OA papers)

These papers are **legitimately Open Access** (AGU >2yr policy) but Wiley's Cloudflare protection blocks all automated download attempts:

| Paper | DOI | Approaches tried |
|-------|-----|-----------------|
| Dlugokencky et al. 2009 (GRL) | `10.1029/2009GL039780` | urllib, curl, Playwright, Scrapling, MinerU, Unpaywall, Wayback |
| Dlugokencky et al. 2003 (GRL) | `10.1029/2003GL018126` | Same |
| Walter Anthony et al. 2008 (JGR) | `10.1029/2007JG000569` | Same |
| Etiope et al. 2008 (GRL) | `10.1029/2008GL033623` | Same |
| Tyler et al. 2007 (JGR) | `10.1029/2006JD007231` | Same |
| Mischler et al. 2009 (GBC) | `10.1029/2009GB003460` | Same |
| Allan et al. 2007 (JGR) | `10.1029/2006JD007369` | Same |
| Schaefer & Whiticar 2008 (GBC) | `10.1029/2006GB002889` | Same |
| Chen & Prinn 2006 (JGR) | `10.1029/2005JD006058` | Same |
| Cunnold et al. 2002 (JGR) | `10.1029/2001JD001226` | Same |
| Conrad et al. 2009 (L&O) | `10.4319/lo.2009.54.2.0457` | Same |
| Rigby et al. 2008 (GRL) | `10.1029/2008GL036037` | Same |

**To download manually**: Visit `https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/<DOI>` in a browser.

## ❌ Paywalled — No OA Version Found

| Paper | DOI | Publisher |
|-------|-----|-----------|
| Ferretti et al. 2005 | `10.1126/science.1115193` | Science/AAAS |
| Spahni et al. 2005 | `10.1126/science.1120132` | Science/AAAS |
| Whiticar 2007 | `10.1098/rsta.2007.2048` | Royal Society |
| Chanton 2005 | `10.1016/j.orggeochem.2004.10.007` | Elsevier |
| Kinnaman et al. 2006 | `10.1016/j.gca.2006.09.007` | Elsevier |
| Nakagawa et al. 2005 | `10.1016/j.orggeochem.2005.01.003` | Elsevier |
| Börjesson et al. 2007 | `10.1021/es062735v` | ACS |
| Fisher et al. 2005 | `10.1002/rcm.2300` | Wiley |

## Methods Attempted

1. **Direct HTTP** (urllib/curl with browser User-Agent): Blocked by Cloudflare 403
2. **Playwright headless Chromium**: Cloudflare challenge timeout
3. **Scrapling stealthy-fetch**: Cloudflare challenge detected, 403
4. **MinerU DOI-based**: All 22 submissions failed (publisher blocks)
5. **Unpaywall API**: All PDF URLs point back to Wiley (which blocks)
6. **Semantic Scholar API**: Same Wiley URLs
7. **Europe PMC**: None of these papers have PMC records
8. **Wayback Machine**: No PDF snapshots archived
9. **CORE API**: Rate-limited (429)
10. **Institutional repos**: Only VU (Houweling) and Nature (HTML) accessible

## Extracted Text (for database use)

Even without PDFs, text extraction is available for:
- `mineru_extractions/Lassey2007_ACP_centennial.md` — Full extraction (PyMuPDF, 107K chars)
- `mineru_extractions/Houweling2006_GRL.md` — Full extraction (PyMuPDF, 27K chars)
- `mineru_extractions/Bousquet2006_Nature.md` — HTML-to-text extraction (28K chars)
- `mineru_extractions/Keppler2006_Nature.md` — HTML-to-text extraction (27K chars)
- All other papers: database entries created from OpenAlex abstracts + known literature values
