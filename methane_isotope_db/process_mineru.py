#!/usr/bin/env python3
"""Process unextracted PDFs through MinerU API using GitHub raw URLs."""
import json
import os
import sys
import time
import io
import zipfile
import requests
from urllib.parse import quote

API_KEY = os.environ.get("MINERU_API_KEY", "")
BASE = "https://mineru.net/api/v4"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
GITHUB_BASE = "https://raw.githubusercontent.com/Ilovecodinghhh/research-methane-isotope-db/master/methane_isotope_db/pdfs"
OUT_DIR = "mineru_extractions"

UNPROCESSED = {
    "Dean et al. 2018 .pdf": "Dean2018",
    "Defratyka et al.2021.pdf": "Defratyka2021",
    "Fernandez et al.2022.pdf": "Fernandez2022",
    "Fisher et al.2017.pdf": "Fisher2017",
    "Ganesan et al.2018.pdf": "Ganesan2018",
    "Milkov et al.2018.pdf": "Milkov2018",
    "Nisbet et al. 2019.pdf": "Nisbet2019",
    "Nisbet et al. 2023.pdf": "Nisbet2023",
    "Schaefer et al.2019.pdf": "Schaefer2019",
    "Schwietzke et al.2017.pdf": "Schwietzke2017",
    "Sherwood et al.2017.pdf": "Sherwood2017",
    "Townsend-Small et al.2012.pdf": "TownsendSmall2012",
    "Woolley Maisch et al.2023.pdf": "WoolleyMaisch2023",
    "feinberg et al.2018.pdf": "feinberg2018",
    "feng2022.pdf": "feng2022",
    "fiehn2020.pdf": "fiehn2020",
    "hmiel et al. 2020.pdf": "hmiel2020",
    "kirschke et al.2013.pdf": "kirschke2013",
    "menoud2020_lutjewad.pdf": "menoud2020_lutjewad",
    "moya_zwamps2021.pdf": "moya_zwamps2021",
    "umezawa2012.pdf": "umezawa2012",
}

# Filter already done
to_process = {}
for pdf_name, out_name in UNPROCESSED.items():
    out_path = os.path.join(OUT_DIR, f"{out_name}.md")
    if os.path.exists(out_path):
        print(f"  SKIP (exists): {out_name}")
    else:
        to_process[pdf_name] = out_name

if not to_process:
    print("All PDFs already processed!")
    sys.exit(0)

print(f"\nProcessing {len(to_process)} PDFs via MinerU API (GitHub raw URLs)...\n")

# Submit all tasks
tasks = {}  # task_id -> (pdf_name, out_name)
for pdf_name, out_name in to_process.items():
    url = f"{GITHUB_BASE}/{quote(pdf_name)}"
    
    # Verify URL is accessible
    head = requests.head(url, allow_redirects=True)
    if head.status_code != 200:
        print(f"  SKIP (URL {head.status_code}): {pdf_name}")
        continue
    
    resp = requests.post(
        f"{BASE}/extract/task",
        headers=HEADERS,
        json={"url": url, "is_ocr": True},
    )
    data = resp.json()
    if data.get("code") == 0:
        task_id = data["data"]["task_id"]
        tasks[task_id] = (pdf_name, out_name)
        print(f"  Submitted: {pdf_name} -> {task_id}")
    else:
        print(f"  ERROR: {pdf_name} -> {data}")
    
    time.sleep(1)  # Rate limit

print(f"\n{len(tasks)} tasks submitted. Polling for results...\n")

# Poll for all results
completed = set()
max_wait = 600
start = time.time()

while len(completed) < len(tasks) and (time.time() - start) < max_wait:
    time.sleep(15)
    elapsed = int(time.time() - start)
    
    for task_id, (pdf_name, out_name) in tasks.items():
        if task_id in completed:
            continue
        
        resp = requests.get(f"{BASE}/extract/task/{task_id}", headers=HEADERS)
        data = resp.json()
        state = data.get("data", {}).get("state", "?")
        
        if state == "done":
            completed.add(task_id)
            zip_url = data["data"].get("full_zip_url", "")
            if zip_url:
                zip_resp = requests.get(zip_url)
                if zip_resp.status_code == 200:
                    zf = zipfile.ZipFile(io.BytesIO(zip_resp.content))
                    md_files = [n for n in zf.namelist() if n.endswith('.md')]
                    if md_files:
                        # Use the largest .md file (main content)
                        md_files.sort(key=lambda n: len(zf.read(n)), reverse=True)
                        md_content = zf.read(md_files[0]).decode('utf-8')
                        out_file = os.path.join(OUT_DIR, f"{out_name}.md")
                        with open(out_file, "w") as f:
                            f.write(md_content)
                        print(f"  [{elapsed}s] DONE: {out_name} ({len(md_content)} chars, from {md_files[0]})")
                    else:
                        print(f"  [{elapsed}s] DONE but no .md in zip: {zf.namelist()[:5]}")
                else:
                    print(f"  [{elapsed}s] DONE but zip download failed: HTTP {zip_resp.status_code}")
            else:
                print(f"  [{elapsed}s] DONE but no zip URL: {data['data']}")
        elif state == "failed":
            completed.add(task_id)
            err = data.get("data", {}).get("err_msg", "unknown")
            print(f"  [{elapsed}s] FAILED: {out_name} - {err}")
    
    pending = len(tasks) - len(completed)
    if pending > 0:
        print(f"  [{elapsed}s] ... {pending} still pending")

if len(completed) < len(tasks):
    print(f"\nTIMEOUT: {len(tasks) - len(completed)} tasks didn't complete")

print(f"\nDone! {sum(1 for t in completed if os.path.exists(os.path.join(OUT_DIR, tasks[t][1] + '.md')))} files saved.")
