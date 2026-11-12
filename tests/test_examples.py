# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = [
    "examples/minimal-run/run_demo.py",
    "examples/multi-card/run_demo.py",
    "examples/decision/run_demo.py",
    "examples/rollback/run_demo.py",
    "examples/two-seat-handoff/run_demo.py",
]

def test_examples_run():
    for rel in EXAMPLES:
        p = subprocess.run([sys.executable, rel], cwd=ROOT, capture_output=True, text=True)
        assert p.returncode == 0, f"{rel}\n{p.stdout}\n{p.stderr}"
