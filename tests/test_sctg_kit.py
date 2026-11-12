# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

def test_hash_helpers(tmp_path):
    kit = load("sctg_kit_hash", ROOT / "kit" / "sctg.py")
    p = tmp_path / "a.txt"
    p.write_text("hello\n", encoding="utf-8")
    assert kit.sha256_bytes(b"hello\n") == kit.sha256_file(p)
    scope = tmp_path / "scope"
    scope.mkdir()
    (scope / "x.txt").write_text("x", encoding="utf-8")
    out = kit.hash_write_scope(tmp_path, ["scope/**"])
    assert "scope/x.txt" in out

def test_render_and_report(tmp_path):
    kit = load("sctg_kit_render", ROOT / "kit" / "sctg.py")
    run = tmp_path / "run"
    (run / "sctg" / "tasks").mkdir(parents=True)
    (run / "sctg" / "ledger").mkdir(parents=True)
    (run / "sctg" / "pattern.yaml").write_text("pattern: sctg\nmode: shadow\nrun_id: test\n", encoding="utf-8")
    (run / "sctg" / "tasks" / "T-1.yaml").write_text(
        "id: T-1\ntitle: test\nseat: main\ninputs: []\nwrite_scope: []\n",
        encoding="utf-8",
    )
    card = kit.render(run, "T-1", 1)
    assert card.exists() and "card_hash:" in card.read_text(encoding="utf-8")
    (run / "sctg" / "ledger" / "acceptance.jsonl").write_text(
        json.dumps({"task_id": "T-1", "verdict": "PASS"}) + "\n", encoding="utf-8"
    )
    assert kit.report(run) == 0

def test_metrics_reads_ledger(tmp_path):
    kit = load("sctg_kit_metrics", ROOT / "kit" / "sctg.py")
    run = tmp_path / "run"
    (run / "sctg" / "ledger").mkdir(parents=True)
    (run / "sctg" / "submissions" / "T-1").mkdir(parents=True)
    (run / "sctg" / "submissions" / "T-1" / "attempt-1.json").write_text(
        json.dumps({"commands": [{"cmd": "x", "exit_code": 0}]}), encoding="utf-8"
    )
    (run / "sctg" / "ledger" / "events.jsonl").write_text(
        json.dumps({"ts": "2026-01-01T00:00:00+00:00", "event": "task_started", "task_id": "T-1", "attempt": 1}) + "\n",
        encoding="utf-8",
    )
    assert kit.metrics(run) == 0

def test_cache_path_classification():
    g = load("scope_gate_cache", ROOT / "kit" / "gates" / "g1_scope.py")
    assert g.is_cache_path("a/__pycache__/x.pyc")
    assert g.is_cache_path("a/x.pyc")
    assert not g.is_cache_path("a/x.py")

def test_cli_help():
    import subprocess
    import sys
    p = subprocess.run([sys.executable, "-m", "kit.sctg", "--help"], cwd=ROOT, capture_output=True, text=True)
    assert p.returncode == 0
