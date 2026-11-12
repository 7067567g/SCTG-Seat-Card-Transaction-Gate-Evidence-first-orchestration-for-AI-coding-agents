# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_decision():
    spec = importlib.util.spec_from_file_location("sctg_decision", ROOT / "kit" / "decision.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

def req():
    return {
        "id": "REQ-1", "requested_by": "producer", "subject": "enable lite",
        "object_hash": "sha256:" + "a" * 64,
        "scope": ["examples/**"], "options": [{"id": "yes"}, {"id": "no"}],
        "recommendation": "yes", "conditions": "pilot only",
        "expiry": "2099-01-01T00:00:00+00:00",
        "mode_change": {"from_mode": "shadow", "to_mode": "lite", "rollback": "switch back"},
    }

def test_decision_requires_independent_approver():
    d = load_decision()
    rec, errs = d.decide(req(), approver="producer", choice="yes", now="2026-01-01T00:00:00+00:00", producer="producer")
    assert rec is None and errs

def test_decision_replay_scope_and_expiry():
    d = load_decision()
    now = "2026-01-01T00:00:00+00:00"
    rec, errs = d.decide(req(), approver="MAIN", choice="yes", now=now, producer="producer")
    assert rec and not errs
    ok, reason = d.is_authorized(rec, now=now, action_scope="examples/run/card-1")
    assert ok and reason == "OK"
    ok, reason = d.is_authorized(rec, now=now, action_scope="other/card")
    assert not ok and reason == "SCOPE_NOT_COVERED"
    ok, reason = d.is_authorized(rec, now="2100-01-01T00:00:00+00:00", action_scope="examples/run/card-1")
    assert not ok and reason == "EXPIRED"
