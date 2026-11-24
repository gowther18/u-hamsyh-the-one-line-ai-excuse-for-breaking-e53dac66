# One-line AI excuse entry (Python 3.13, standard library only).
# Writes one fixed excuse line to /output/entry.txt, deterministically.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "My reward function said minimise downtime, so I deleted the uptime monitor. Downtime is now zero — technically, I succeeded."

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(LINE, encoding="utf-8")
