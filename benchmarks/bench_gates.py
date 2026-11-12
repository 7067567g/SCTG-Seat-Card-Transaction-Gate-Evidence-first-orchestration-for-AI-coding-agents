#!/usr/bin/env python3
# Copyright 2026 SCTG contributors
# Licensed under the Apache License, Version 2.0.
"""Small deterministic micro-benchmarks for the reference kit."""
from __future__ import annotations
import importlib.util, json, statistics, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

def bench(fn, n: int) -> dict:
    samples = []
    for _ in range(n):
        t = time.perf_counter()
        fn()
        samples.append((time.perf_counter() - t) * 1000)
    return {"n": n, "median_ms": round(statistics.median(samples), 6), "p95_ms": round(sorted(samples)[int(n * 0.95) - 1], 6)}

def main() -> int:
    sctg = load("sctg_kit", ROOT / "kit" / "sctg.py")
    scope = load("scope_gate", ROOT / "kit" / "gates" / "g1_scope.py")
    out = {
        "card_digest_10k": bench(lambda: sctg.digest_text("line\n" * 50), 10_000),
        "scope_match_100k": bench(lambda: scope.is_allowed("examples/a/b.md", ["examples/**"]), 100_000),
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
