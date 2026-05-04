#!/usr/bin/env python3
"""Phase 1: Rename mineru_extractions and pdfs with standardized names."""
import os
import shutil
import json

# Mapping: current_name -> (new_name, journal_abbreviation)
# Format: FirstAuthorSurnameYearJournalAbbrev
RENAME_MAP = {
    # Already well-named files with journal prefix/suffix
    "ACP2024_Thanwerdas": "Thanwerdas2024ACP",
    "ACP2025_SW_China": "Chen2025ACP",
    "Allan2007_JGR": "Allan2007JGR",
    "AMT2025_14C_sampler": "Zazzeri2025AMT",
    "basu2022": "Basu2022ACP",
    "Borjesson2007_EST": "Borjesson2007EST",
    "Bousquet2006_Nature": "Bousquet2006Nature",
    "Bousquet2006_Nature_pdf": "Bousquet2006Nature_pdf",
    "Bousquet2011_ACP_source_attribution": "Bousquet2011ACP",
    "brownlow2017": "Brownlow2017ACP",
    "Chanton2005_OrgGeochem": "Chanton2005OrgGeochem",
    "Chen2006_JGR": "Chen2006JGR",
    "CommEarth2024_fossil_microbial": "Chandra2024CommEarth",
    "CommEarth2025_seeps": "Molofsky2025CommEarth",
    "CommEarth2026_laptev": "Brussee2026CommEarth",
    "Conrad2009_LO": "Conrad2009LO",
    "Cunnold2002_JGR": "Cunnold2002JGR",
    "Dalsoren2016_ACP_methane_40yr": "Dalsoren2016ACP",
    "Dean2018": "Dean2018RoG",
    "Defratyka2021": "Defratyka2021EST",
    "Dlugokencky2003_GRL": "Dlugokencky2003GRL",
    "Dlugokencky2009_GRL": "Dlugokencky2009GRL",
    "douglas2021": "Douglas2021BG",
    "ESSD2026_Thanwerdas": "Tapin2026ESSD",
    "Etiope2008_GRL": "Etiope2008GRL",
    "etiope2019": "Etiope2019ESSD",
    "feinberg2018": "Feinberg2018JGR",
    "feng2022": "Feng2022NatComm",
    "Fernandez2022": "Fernandez2022AtmosEnv",
    "Fernandez_Cortes2015_cave_sink": "FernandezCortes2015NatComm",
    "Ferretti2005_Science": "Ferretti2005Science",
    "Ferretti2006_ACPD": "Ferretti2006ACPD",
    "fiehn2020": "Fiehn2020ACP",
    "fiehn2023_silesia": "Fiehn2023ACP",
    "Fisher2006_RCMS": "Fisher2006RCMS",
    "Fisher2017": "WoolleyMaisch2024JGR",  # DOI 10.1029/2023JD039098 - this is actually Woolley-Maisch et al 2024
    "Fujita2025": "Fujita2025JGR",
    "Ganesan2018": "Ganesan2018GRL",
    "Gentner2014_ACP_SJV_petroleum_dairy": "Gentner2014ACP",
    "Ghosh2015_ACP_methane_1910_2010": "Ghosh2015ACP",
    "gonzalez_moguel2022": "GonzalezMoguel2022ACP",
    "He2026": "He2026JGR",
    "hmiel2020": "Hmiel2020Nature",
    "hoheisel2019": "Hoheisel2019AE",
    "Houweling2006_GRL": "Houweling2006GRL",
    "kelly2022_surat": "Kelly2022ACP",
    "Keppler2006_Nature": "Keppler2006Nature",
    "Keppler2006_Nature_pdf": "Keppler2006Nature_pdf",
    "Kietavainen2015_deep_crystalline": "Kietavainen2015AG",
    "kirschke2013": "Kirschke2013NatGeo",
    "Lassey2007_ACP_centennial": "Lassey2007ACP",
    "lu2021": "Lu2021ACP",
    "maasakkers2019": "Maasakkers2019ACP",
    "maazallahi2020": "Maazallahi2020AE",
    "mcnorton2016": "McNorton2016ACP",
    "menoud2020_lutjewad": "Menoud2020TellusB",
    "menoud2021_krakow": "Menoud2021ACP",
    "menoud2022_emid": "Menoud2022ESSD",
    "Milkov2018": "Milkov2018OrgGeochem",
    "Mischler2009_GBC": "Mischler2009GBC",
    "monteil2011": "Monteil2011ACP",
    "moya_zwamps2021": "Nisbet2022PhilTransA",
    "Nakagawa2005_OrgGeochem": "Nakagawa2005OrgGeochem",
    "nisbet2016": "Nisbet2016GBC",
    "Nisbet2019": "Nisbet2019GBC",
    "nisbet2020_mitigation": "Nisbet2020RoG",
    "Nisbet2023": "Nisbet2023GBC",
    "Okumura2016_PEPS_methanogenesis": "Okumura2016PEPS",
    "Rigby2008_GRL": "Rigby2008GRL",
    "rockmann2016": "Rockmann2016ACP",
    "saunois2016": "Saunois2016ESSD",
    "saunois2020": "Saunois2020ESSD",
    "Schaefer2008_GBC": "Schaefer2008GBC",
    "Schaefer2019": "Schaefer2019CurrClimChR",
    "Schwietzke2017": "Schwietzke2016Nature",
    "Sherwood2017": "Sherwood2017ESSD",
    "Spahni2011_BG_wetland_methane": "Spahni2011BG",
    "Sperlich2015": "Sperlich2015ACP",
    "TownsendSmall2012": "TownsendSmall2012JGR",
    "Tyler2007_JGR": "Tyler2007JGR",
    "umezawa2012": "Umezawa2012ACP",
    "WalterAnthony2008_JGR": "WalterAnthony2008JGR",
    "Warwick2016_ACP_Arctic_d13C_dD": "Warwick2016ACP",
    "WoolleyMaisch2023": "WoolleyMaisch2024JGR_dup",  # duplicate of Fisher2017
    "worden2017": "Worden2017NatComm",
    "Zazzeri2015_AtmosEnv_UK_sources": "Zazzeri2015AE",
    "Zazzeri2016_ACP_coal_isotope": "Zazzeri2016ACP",
    "Zhang2011": "Zhang2011JGR",
    "zhang2020_permian": "Zhang2020SA",
    "zhang2021": "Zhang2021NatComm",
}

md_dir = "mineru_extractions"
log = []

# Check for duplicates
seen_new = {}
for old, new in RENAME_MAP.items():
    if new in seen_new:
        print(f"WARNING: Duplicate new name '{new}' for '{old}' and '{seen_new[new]}'")
    seen_new[new] = old

# Rename .md files
renamed = 0
for old_name, new_name in sorted(RENAME_MAP.items()):
    old_path = os.path.join(md_dir, f"{old_name}.md")
    new_path = os.path.join(md_dir, f"{new_name}.md")
    
    if os.path.exists(old_path):
        if old_name != new_name:
            if os.path.exists(new_path):
                print(f"  SKIP (target exists): {old_name} -> {new_name}")
                log.append({"old": old_name, "new": new_name, "status": "skip_exists"})
            else:
                os.rename(old_path, new_path)
                print(f"  RENAMED: {old_name}.md -> {new_name}.md")
                log.append({"old": old_name, "new": new_name, "status": "renamed"})
                renamed += 1
        else:
            log.append({"old": old_name, "new": new_name, "status": "unchanged"})
    else:
        # Check if already renamed
        if os.path.exists(new_path):
            log.append({"old": old_name, "new": new_name, "status": "already_done"})
        else:
            print(f"  MISSING: {old_name}.md")
            log.append({"old": old_name, "new": new_name, "status": "missing"})

print(f"\nRenamed {renamed} files")

# Save mapping log
with open("rename_mapping_log.json", "w") as f:
    json.dump(log, f, indent=2)
print("Mapping log saved to rename_mapping_log.json")
