# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
from __future__ import annotations
import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_check_repo():
    p = subprocess.run([sys.executable, "scripts/check_repo.py"], cwd=ROOT, capture_output=True, text=True)
    assert p.returncode == 0, p.stdout + p.stderr

def test_card_digest_ignores_card_hash_line():
    spec = importlib.util.spec_from_file_location("sctg_kit", ROOT / "kit" / "sctg.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    a = "card\ncard_hash: sha256:aaa\nbody\n"
    b = "card\ncard_hash: sha256:bbb\nbody\n"
    assert mod.digest_text(a) == mod.digest_text(b)

def test_minimal_demo_runs():
    p = subprocess.run([sys.executable, "examples/minimal-run/run_demo.py"], cwd=ROOT, capture_output=True, text=True)
    assert p.returncode == 0, p.stdout + p.stderr
