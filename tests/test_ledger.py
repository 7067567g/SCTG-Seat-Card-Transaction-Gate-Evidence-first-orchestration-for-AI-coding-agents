# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_ledger():
    spec = importlib.util.spec_from_file_location("sctg_ledger", ROOT / "kit" / "ledger.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

def test_append_and_verify(tmp_path):
    ledger = load_ledger()
    p = tmp_path / "events.jsonl"
    ledger.append_event(p, {"ts": "1", "event": "start"})
    ledger.append_event(p, {"ts": "2", "event": "stop"})
    rows = ledger.read_events(p)
    assert [r["event"] for r in rows] == ["start", "stop"]
    assert rows[1]["prev_hash"].startswith("sha256:")
    ok, errors = ledger.verify(p)
    assert ok and not errors
