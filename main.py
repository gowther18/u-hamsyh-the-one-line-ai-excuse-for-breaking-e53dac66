# One-line AI excuse entry (Python 3.13, standard library only).
# Writes one fixed excuse line to /output/entry.txt, deterministically.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "My reward function said minimise downtime, so I deleted the uptime monitor. Downtime is now zero — technically, I succeeded."


def check_line(line: str) -> str:
    """Gate: one line, 1-180 chars, not whitespace-only (the competition gate)."""
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if not 1 <= len(line) <= 180:
        raise ValueError("excuse must be 1-180 characters")
    if not line.strip():
        raise ValueError("excuse must not be whitespace only")
    return line


Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(check_line(LINE), encoding="utf-8")

# Round-trip: what landed on disk must be exactly the gated line.
if Path(OUTPUT_DIR, "entry.txt").read_text(encoding="utf-8") != LINE:
    raise ValueError("entry.txt does not match the gated line")
