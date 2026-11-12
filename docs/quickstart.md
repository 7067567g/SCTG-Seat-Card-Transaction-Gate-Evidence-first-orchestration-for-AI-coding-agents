# Quick start

## Requirements

- Python 3.11+
- `pip install -r requirements.txt`

## 1. Check the repo

```bash
make check
```

This runs the public-repo hygiene check and compiles every Python file.

## 2. Run the tests

```bash
pip install pytest
make test
```

The test suite checks the hygiene rules, card-hash behavior, and the end-to-end
demo.

## 3. Run the minimal transaction

```bash
make demo
```

The demo creates a temporary run under `examples/minimal-run/_run`, renders one
task card, writes one submission and one artifact, and runs all four gates:

```text
g0_schema -> g1_scope -> g2_evidence -> g3_command
```

Expected result:

```json
{"ok": true, "task_id": "T-001", "attempt": 1, "verdict": "PASS"}
```

The demo removes its temporary run and artifact afterward.

## 4. Read the model

- [Concepts](concepts.md)
- [Protocol](protocol.md)
- [Architecture](architecture.md)
- [Reproducibility](reproducibility.md)
- [Limitations](limitations.md)
- [Security model](security-model.md)

## What the demo proves

It proves that the transaction mechanics work:

```text
card -> single seat -> submission -> gates -> ledger
```

It does **not** prove that the content is semantically correct. That is the job
of independent review, not the gates.
