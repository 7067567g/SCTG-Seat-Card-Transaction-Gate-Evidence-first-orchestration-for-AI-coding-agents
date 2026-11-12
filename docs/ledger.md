# Ledger

The ledger is append-only JSONL.

## Event types

At minimum:

```text
card_rendered
task_started
dispatch
submission_received
gates_run
mode_switched
decision_recorded
```

## Acceptance row

An acceptance row should bind:

```text
task_id, attempt, verdict, card_hash, submission_hash, gate_result
```

## Append-only rules

- Never rewrite an accepted row.
- Corrections are new rows.
- Every row should include a timestamp.
- If `prev_hash` is present, it must match the previous row hash.

Schema: [`../kit/schemas/ledger-event.schema.json`](../kit/schemas/ledger-event.schema.json)

Reference helper: [`../kit/ledger.py`](../kit/ledger.py)
