#!/usr/bin/env python3
"""Rename PDF files to match the standardized naming convention."""
import os
import json

PDF_DIR = "pdfs"

# Mapping from current PDF filename (without .pdf) to new standardized name
PDF_RENAME = {
    "ACP2024_Thanwerdas_isotopic_inversion": "Thanwerdas2024ACP",
    "ACP2025_SW_China_oil_gas_isotopic": "Chen2025ACP",
    "Allan et al. 2007 (JGR)": "Allan2007JGR",
    "AMT2025_portable_14C_sampler": "Zazzeri2025AMT",
    "Basu et al.2022": "Basu2022ACP",
    "Börjesson et al. 2007": "Borjesson2007EST",
    "Bousquet2006_Nature": "Bousquet2006Nature",
    "brownlow2017": "Brownlow2017ACP",
    "Chanton 2005": "Chanton2005OrgGeochem",
    "Chen & Prinn 2006 (JGR)": "Chen2006JGR",
    "CommEarth2024_fossil_decreased_microbial_increased": "Chandra2024CommEarth",
    "CommEarth2025_geologic_seeps_vs_anthropogenic": "Molofsky2025CommEarth",
    "CommEarth2026_triple_isotopic_Laptev_Sea": "Brussee2026CommEarth",
    "Conrad et al. 2009": "Conrad2009LO",
    "Cunnold et al. 2002 (JGR)": "Cunnold2002JGR",
    "Dean et al. 2018 ": "Dean2018RoG",
    "Defratyka et al.2021": "Defratyka2021EST",
    "Dlugokencky et al. 2003 (GRL)": "Dlugokencky2003GRL",
    "Dlugokencky et al. 2009": "Dlugokencky2009GRL",
    "douglas2021": "Douglas2021BG",
    "ESSD2026_Thanwerdas_global_d13C_dataset": "Tapin2026ESSD",
    "etiope2019": "Etiope2019ESSD",
    "Etiope et al. 2008 (GRL)": "Etiope2008GRL",
    "feinberg et al.2018": "Feinberg2018JGR",
    "feng2022": "Feng2022NatComm",
    "Fernandez et al.2022": "Fernandez2022AtmosEnv",
    "Ferretti 2006 ACPD ": "Ferretti2006ACPD",
    "Ferretti et al. 2005": "Ferretti2005Science",
    "fiehn2020": "Fiehn2020ACP",
    "fiehn2023_silesia": "Fiehn2023ACP",
    "Fisher et al.2006": "Fisher2006RCMS",
    "Fisher et al.2017": "WoolleyMaisch2024JGR",
    "Fujita et al.2025": "Fujita2025JGR",
    "Ganesan et al.2018": "Ganesan2018GRL",
    "gonzalez_moguel2022": "GonzalezMoguel2022ACP",
    "He et al.2026": "He2026JGR",
    "hmiel et al. 2020": "Hmiel2020Nature",
    "hoheisel2019": "Hoheisel2019AE",
    "Houweling2006_GRL": "Houweling2006GRL",
    "kelly2022_surat": "Kelly2022ACP",
    "Keppler2006_Nature": "Keppler2006Nature",
    "kirschke et al.2013": "Kirschke2013NatGeo",
    "Lassey2007_ACP_centennial": "Lassey2007ACP",
    "lu2021": "Lu2021ACP",
    "maasakkers2019": "Maasakkers2019ACP",
    "maazallahi2020": "Maazallahi2020AE",
    "mcnorton2016": "McNorton2016ACP",
    "menoud2020_lutjewad": "Menoud2020TellusB",
    "menoud2021_krakow": "Menoud2021ACP",
    "menoud2022_emid": "Menoud2022ESSD",
    "Milkov et al.2018": "Milkov2018OrgGeochem",
    "Mischler et al. 2009 (GBC)": "Mischler2009GBC",
    "monteil2011": "Monteil2011ACP",
    "moya_zwamps2021": "Nisbet2022PhilTransA",
    "Nakagawa et al. 2005": "Nakagawa2005OrgGeochem",
    "nisbet2016": "Nisbet2016GBC",
    "nisbet2020_mitigation": "Nisbet2020RoG",
    "Nisbet et al. 2019": "Nisbet2019GBC",
    "Nisbet et al. 2023": "Nisbet2023GBC",
    "Rigby et al. 2008 (GRL)": "Rigby2008GRL",
    "rockmann2016": "Rockmann2016ACP",
    "saunois2016": "Saunois2016ESSD",
    "saunois2020": "Saunois2020ESSD",
    "Schaefer et al.2019": "Schaefer2019CurrClimChR",
    "Schaefer & Whiticar 2008 (GBC)": "Schaefer2008GBC",
    "Schwietzke et al.2017": "Schwietzke2016Nature",
    "Sherwood et al.2017": "Sherwood2017ESSD",
    "Sperlich et al.2015": "Sperlich2015ACP",
    "Townsend-Small et al.2012": "TownsendSmall2012JGR",
    "Tyler et al. 2007 (JGR)": "Tyler2007JGR",
    "umezawa2012": "Umezawa2012ACP",
    "Walter Anthony et al. 2008 (JGR)": "WalterAnthony2008JGR",
    "Woolley Maisch et al.2023": "WoolleyMaisch2024JGR_dup",
    "worden2017": "Worden2017NatComm",
    "Zazzeri et al.2016": "Zazzeri2016ACP",
    "zhang2020_permian": "Zhang2020SA",
    "zhang2021": "Zhang2021NatComm",
    "Zhang et al.2011": "Zhang2011JGR",
}

log = []
renamed = 0
skipped = 0

for old_stem, new_stem in sorted(PDF_RENAME.items()):
    old_path = os.path.join(PDF_DIR, f"{old_stem}.pdf")
    new_path = os.path.join(PDF_DIR, f"{new_stem}.pdf")
    
    if os.path.exists(old_path):
        if old_path == new_path:
            log.append({"old": old_stem, "new": new_stem, "status": "unchanged"})
            continue
        if os.path.exists(new_path):
            print(f"  SKIP (target exists): {old_stem} -> {new_stem}")
            log.append({"old": old_stem, "new": new_stem, "status": "skip_exists"})
            skipped += 1
        else:
            os.rename(old_path, new_path)
            print(f"  RENAMED: {old_stem}.pdf -> {new_stem}.pdf")
            log.append({"old": old_stem, "new": new_stem, "status": "renamed"})
            renamed += 1
    else:
        # Try with trailing space stripped (some have trailing spaces)
        found = False
        for f in os.listdir(PDF_DIR):
            if f.endswith('.pdf') and f[:-4].strip() == old_stem.strip():
                actual_old = os.path.join(PDF_DIR, f)
                if not os.path.exists(new_path):
                    os.rename(actual_old, new_path)
                    print(f"  RENAMED (fuzzy): {f} -> {new_stem}.pdf")
                    log.append({"old": f[:-4], "new": new_stem, "status": "renamed"})
                    renamed += 1
                    found = True
                break
        if not found:
            print(f"  MISSING: {old_stem}.pdf")
            log.append({"old": old_stem, "new": new_stem, "status": "missing"})

# Check for any remaining unrenamed PDFs
remaining = []
for f in sorted(os.listdir(PDF_DIR)):
    if f.endswith('.pdf'):
        stem = f[:-4]
        if stem not in [e["new"] for e in log]:
            remaining.append(f)

if remaining:
    print(f"\n  UNRENAMED PDFs ({len(remaining)}):")
    for f in remaining:
        print(f"    {f}")

print(f"\nDone: {renamed} renamed, {skipped} skipped")

with open("pdf_rename_log.json", "w") as f:
    json.dump(log, f, indent=2)
print("Log saved to pdf_rename_log.json")
