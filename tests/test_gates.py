# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "kit" / "gates" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

def test_scope_gate_rejects_outside_path():
    g = load("g1_scope")
    assert g.is_allowed("examples/run/a.md", ["examples/run/**"])
    assert not g.is_allowed("other/a.md", ["examples/run/**"])

def test_schema_gate_rejects_missing_fields(tmp_path):
    g = load("g0_schema")
    sub = tmp_path / "sub.json"
    schema = tmp_path / "schema.json"
    sub.write_text(json.dumps({"task_id": "T"}), encoding="utf-8")
    schema.write_text(json.dumps({"type": "object", "required": ["task_id", "card_hash"]}), encoding="utf-8")
    result = g.check(sub, schema)
    assert result["verdict"] == "FAIL"

def test_evidence_gate_rejects_missing_file(tmp_path):
    g = load("g2_evidence")
    task = tmp_path / "task.yaml"
    task.write_text("write_scope:\n  - examples/**\n", encoding="utf-8")
    sub = tmp_path / "sub.json"
    sub.write_text(json.dumps({"produced_files": ["examples/missing.txt"], "commands": [{"cmd": "x", "exit_code": 0}], "evidence_paths": []}), encoding="utf-8")
    result = g.check(sub, task, tmp_path)
    assert result["verdict"] == "FAIL"

def test_command_gate_rejects_wrong_exit(tmp_path):
    g = load("g3_command")
    sub = tmp_path / "sub.json"
    sub.write_text(json.dumps({"test_command": "python3 -c \"import sys; sys.exit(1)\"", "test_expect_exit": 0}), encoding="utf-8")
    result = g.check(sub, ROOT, tmp_path / "evidence")
    assert result["verdict"] == "FAIL"
