#!/usr/bin/env python3
# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
"""Public-repo hygiene check for SCTG.

Checks:
- required files exist;
- no obvious local absolute paths or secret patterns;
- no vendored dependency directories;
- Python files compile.
"""
from __future__ import annotations
import json
import py_compile
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "README.zh-CN.md", "LICENSE", "NOTICE", "THIRD_PARTY_NOTICES.md",
    "requirements.txt", ".gitignore",
    "docs/concepts.md", "docs/protocol.md", "docs/architecture.md",
    "docs/lessons.md", "docs/provenance.md", "docs/status.md",
    "docs/cases/README.md",
    "docs/cases/01-ten-card-shadow-pilot.md",
    "docs/cases/02-stage-2-governance.md",
    "docs/cases/03-stage-2.5-lite-multi-seat.md",
    "kit/sctg.py", "kit/gates/g0_schema.py", "kit/gates/g1_scope.py",
    "kit/gates/g2_evidence.py", "kit/gates/g3_command.py",
    "kit/schemas/submission.schema.json",
    "examples/minimal-task.yaml",
    "examples/minimal-run/run_demo.py",
    "tests/test_public_repo.py",
    "tests/test_version.py",
    "tests/test_decision.py",
    "tests/test_ledger.py",
    "tests/test_gates.py",
    "CODE_OF_CONDUCT.md",
    "CITATION.cff",
    ".editorconfig",
    ".github/pull_request_template.md",
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    "Makefile",
    "pyproject.toml",
    "CHANGELOG.md",
    "VERSION",
    ".github/workflows/ci.yml",
    "docs/quickstart.md",
    "docs/quickstart.zh-CN.md",
    "docs/environment.md",
    "AGENTS.md",
    "requirements-dev.txt",
    "ruff.toml",
    "mypy.ini",
    ".pre-commit-config.yaml",
    "tests/test_examples.py",
    "tests/test_sctg_kit.py",
    "benchmarks/bench_gates.py",
    "docs/performance.md",
    "docs/benchmarks/README.md",
    "docs/benchmarks/pilot-2026-11.md",
    "docs/benchmarks/results.json",
    "docs/releases/v0.5.0.md",
    "docs/releases/v0.5.1.md",
    "examples/multi-card/run_demo.py",
    "examples/decision/run_demo.py",
    "examples/rollback/run_demo.py",
    "examples/two-seat-handoff/run_demo.py",
    "kit/__init__.py",
    "kit/gates/__init__.py",
    "docs/reproducibility.md",
    "docs/limitations.md",
    "docs/security-model.md",
]
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules", ".pytest_cache"}
TEXT_EXT = {".md", ".py", ".json", ".yaml", ".yml", ".txt", ".toml", ".cfg"}
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
LOCAL_PATH_PATTERNS = [
    re.compile(r"/home/[A-Za-z0-9_.-]+/"),
    re.compile(r"[A-Za-z]:\\\\Users\\\\"),
]

def files():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p

def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")
    for p in files():
        rel = p.relative_to(ROOT)
        if p.suffix not in TEXT_EXT:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                errors.append(f"secret-like pattern in {rel}")
                break
        for pat in LOCAL_PATH_PATTERNS:
            if pat.search(text):
                errors.append(f"local absolute path in {rel}")
                break
        if "node_modules" in text and p.suffix in {".json", ".yaml", ".yml"}:
            errors.append(f"vendored node_modules reference in {rel}")
    try:
        import tomllib
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        project_version = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
        if version != project_version:
            errors.append(f"VERSION {version!r} != pyproject version {project_version!r}")
    except Exception as exc:
        errors.append(f"version consistency check failed: {exc}")
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for p in files():
        if p.suffix != ".md":
            continue
        text = p.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (p.parent / target).resolve().exists():
                errors.append(f"broken link in {p.relative_to(ROOT)}: {target}")
    for p in files():
        if p.suffix == ".py":
            try:
                py_compile.compile(str(p), doraise=True)
            except Exception as exc:
                errors.append(f"python compile failed: {p.relative_to(ROOT)}: {exc}")
    print(json.dumps({"verdict": "PASS" if not errors else "FAIL", "errors": errors}, ensure_ascii=False))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
