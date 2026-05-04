#!/usr/bin/env python3
"""Trim references from all .md files and save to mineru_extractions_trimmed/"""
import os
import re

SRC = "mineru_extractions"
DST = "mineru_extractions_trimmed"
os.makedirs(DST, exist_ok=True)

# Patterns for reference section headers
REF_HEADERS = re.compile(
    r'^#{1,3}\s*(References|Bibliography|Literature\s+Cited|Works\s+Cited|REFERENCES)\s*$',
    re.IGNORECASE
)

# For files without explicit headers, detect reference blocks:
# Lines that look like numbered references [1], [2]... or author-year format
REF_LINE = re.compile(
    r'^\s*(\[\d{1,3}\]|'           # [1] style
    r'\d{1,3}\.\s+[A-Z]|'         # 1. Author style
    r'[A-Z][a-z]+,?\s+[A-Z]\.|'   # Author, A. style
    r'[A-Z][a-z]+\s+et\s+al\.)'   # Author et al.
)

stats = {"header": 0, "pattern": 0, "none": 0}

for fname in sorted(os.listdir(SRC)):
    if not fname.endswith('.md'):
        continue
    
    src_path = os.path.join(SRC, fname)
    dst_path = os.path.join(DST, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total = len(lines)
    cut_at = None
    
    # Strategy 1: Find explicit reference header
    for i, line in enumerate(lines):
        if REF_HEADERS.match(line.strip()):
            # Make sure it's in the latter half (avoid false positives in intro)
            if i > total * 0.3:
                cut_at = i
                # Don't break - take the LAST one if multiple matches
    
    if cut_at is not None:
        stats["header"] += 1
    else:
        # Strategy 2: Look for a dense block of reference-like lines in the last 40%
        # Find the start of a contiguous block of reference-looking lines
        search_start = int(total * 0.6)
        ref_density = []
        
        for i in range(search_start, total):
            stripped = lines[i].strip()
            if not stripped:
                continue
            if REF_LINE.match(stripped):
                ref_density.append(i)
        
        # If we find 5+ reference-like lines in close proximity
        if len(ref_density) >= 5:
            # Find the start of the dense block
            for j in range(len(ref_density) - 4):
                # 5 ref lines within 20 lines of each other
                if ref_density[j+4] - ref_density[j] < 30:
                    # Walk back to find the actual start
                    cut_at = ref_density[j]
                    # Look for a preceding blank line or header
                    while cut_at > 0 and lines[cut_at - 1].strip():
                        cut_at -= 1
                    stats["pattern"] += 1
                    break
        
        if cut_at is None:
            # Strategy 3: Look for "Acknowledgements" or "Supplementary" near the end
            # and cut from there (these precede references in some formats)
            for i in range(int(total * 0.7), total):
                if re.match(r'^#{1,3}\s*(Acknowledg|Supplement|Supporting\s+Info|Data\s+Availability|Author\s+Contrib|Competing|Conflict)', 
                           lines[i].strip(), re.IGNORECASE):
                    cut_at = i
                    break
            
            if cut_at is not None:
                stats["pattern"] += 1
            else:
                stats["none"] += 1
    
    # Write trimmed file
    if cut_at is not None:
        trimmed = lines[:cut_at]
        # Remove trailing blank lines
        while trimmed and not trimmed[-1].strip():
            trimmed.pop()
        pct = round((1 - len(trimmed) / total) * 100)
        print(f"  {fname}: {total} -> {len(trimmed)} lines (trimmed {pct}%)")
    else:
        trimmed = lines
        print(f"  {fname}: {total} lines (no refs found, kept as-is)")
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.writelines(trimmed)

print(f"\nStats: {stats['header']} by header, {stats['pattern']} by pattern, {stats['none']} kept as-is")
print(f"Output: {DST}/")
