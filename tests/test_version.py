# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_version_matches_pyproject():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert version == data["project"]["version"]
