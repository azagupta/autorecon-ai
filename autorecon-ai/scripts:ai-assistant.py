#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

def analyze(domain):
    home = Path.home()
    scans = sorted(home.glob(f"bugbounty/{domain}_*"), reverse=True)
    if not scans:
        print(f"No results for {domain}")
        return
    scan_dir = scans[0]
    print(f"Analyzing: {scan_dir}")
    
    results = ""
    for file in scan_dir.glob("*.txt"):
        if file.stat().st_size < 50000:
            with open(file) as f:
                results += f"\n=== {file.name} ===\n{f.read(1000)}\n"
    
    try:
        r = subprocess.run(
            ["claude", "code", f"Analyze these bug bounty results:\n{results}"],
            capture_output=True,
            text=True,
            timeout=120
        )
        with open(scan_dir / "ai_analysis.txt", "w") as f:
            f.write(r.stdout)
        print(r.stdout)
    except Exception as e:
        print(f"Error: {e}")

def payloads(vuln_type):
    try:
        r = subprocess.run(
            ["claude", "code", f"Generate 10 creative {vuln_type} payloads for bug bounty."],
            capture_output=True,
            text=True,
            timeout=60
        )
        print(r.stdout)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ai-assistant [analyze|payloads]")
        sys.exit(1)
    
    if sys.argv[1] == "analyze" and len(sys.argv) > 2:
        analyze(sys.argv[2])
    elif sys.argv[1] == "payloads" and len(sys.argv) > 2:
        payloads(sys.argv[2])