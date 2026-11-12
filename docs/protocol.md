# Protocol (minimal)

This is the public, minimal object model. It is intentionally smaller than the
internal implementation.

## Task Card

```yaml
id: T-001
title: Add a README section
seat: main
inputs:
  - docs/overview.md
write_scope:
  - docs/overview.md
deliverable:
  schema: kit/schemas/submission.schema.json
  required: [task_id, card_hash, summary, status]
gates: [g0_schema, g1_scope, g2_evidence, g3_command]
```

A rendered card also carries a `card_hash` computed over the card body. The
submission must echo that hash.

## Submission

```json
{
  "task_id": "T-001",
  "card_hash": "sha256:...",
  "summary": "What changed",
  "findings": [],
  "changed_files": ["docs/overview.md"],
  "produced_files": [],
  "commands": [{"cmd": "python3 scripts/check_repo.py", "exit_code": 0, "expect_exit": 0}],
  "test_command": "python3 scripts/check_repo.py",
  "test_expect_exit": 0,
  "evidence_paths": ["docs/overview.md"],
  "status": "OK"
}
```

## GateResult

A gate result is structured, not prose:

```json
{
  "gate": "g1_scope",
  "verdict": "FAIL",
  "reason": "write outside scope",
  "exit_code": 1
}
```

Verdicts are `PASS`, `FAIL`, or `SKIP`. A `SKIP` must carry a reason code and
must not count as a pass.

## Decision Record

A Decision must include at least:

- decision id and request id;
- `approved_by: MAIN`;
- chosen option;
- non-empty scope;
- expiry;
- rollback;
- bound object hash;
- replay result for in-scope / out-of-scope / expired cases.

## Ledger

Append-only JSONL is enough for a first implementation. An acceptance row should
bind at least:

```text
task_id, attempt, verdict, card_hash, submission_hash, gate_result
```

Do not rewrite accepted rows. Corrections are new rows.


## Schemas

- [`gate-result.schema.json`](../kit/schemas/gate-result.schema.json)
- [`decision-request.schema.json`](../kit/schemas/decision-request.schema.json)
- [`decision-record.schema.json`](../kit/schemas/decision-record.schema.json)
- [`ledger-event.schema.json`](../kit/schemas/ledger-event.schema.json)
- [`handoff.schema.json`](../kit/schemas/handoff.schema.json)
- [`join-result.schema.json`](../kit/schemas/join-result.schema.json)

See also: [mode policy](mode-policy.md), [decision model](decision-model.md),
[ledger](ledger.md), [versioning](versioning.md), [FAQ](faq.md),
[glossary](glossary.md).
