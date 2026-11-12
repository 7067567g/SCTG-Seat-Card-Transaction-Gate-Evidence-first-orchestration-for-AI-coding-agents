# SCTG

**Seat–Card–Transaction–Gate** — evidence-first orchestration for AI coding agents.

SCTG turns agent work into explicit, auditable units: a task card defines scope,
a single seat executes one card at a time, a gate checks the submission, an
independent MAIN decision authorizes irreversible moves, and an append-only
ledger records what actually happened.

Most agent workflows trust the chat transcript. SCTG trusts evidence.

- Chat logs are not audit evidence.
- Self-approval is not review.
- Silent retries hide failure.
- A run should be reproducible from artifacts, not memory.

SCTG is not another agent framework or model. It is a **control pattern plus a
small reference kit** that can sit on top of OpenRig, OpenCode, or a plain shell.

## Core model

```text
Task Card
  -> single-channel seat
  -> Submission
  -> deterministic Gate
  -> independent MAIN Decision (when required)
  -> append-only Ledger
```

Three rules matter more than the tooling:

1. **One active card per seat.** A seat never runs two cards at once.
2. **The host driver never writes GateResult or product content.** It only
   dispatches, collects, gates, and records.
3. **A producer never approves its own output.** Irreversible moves require an
   independent MAIN decision.

## What is in this repo

```text
docs/                 Concepts, protocol, architecture, lessons, provenance
kit/                  Reference SCTG host runner, gates, and submission schema
examples/             Minimal task-card example
scripts/check_repo.py Public-repo hygiene and secret-pattern check
```

## Quick start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

python3 kit/sctg.py --help
python3 scripts/check_repo.py
```

See [`examples/README.md`](examples/README.md) for a minimal card, and
[`docs/protocol.md`](docs/protocol.md) for the object model.

## Status

This repository is a distilled public reference, not a dump of internal run
data. It reflects lessons from a successful Stage-2.5 reference run:

- Lite pilot: 5 cards, independent review, rollback drill;
- two-seat handoff + join;
- adapter v0 with real read-only CLI alignment and local idempotency ledger;
- final exit audit: 24/24 PASS, Full mode intentionally left closed.

The public repo does **not** claim production readiness and does **not** claim
that Full-mode orchestration is validated.

## Design principles

- Evidence over transcripts.
- Gates check structure, scope, evidence, and reproducibility — not semantic
  correctness.
- Semantic review is separate from gate evaluation.
- Mode changes require an explicit, scoped, expiring decision with rollback.
- Scope conflicts are not resolved by "just run it anyway".

## License

Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
