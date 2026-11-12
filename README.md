**English** | [简体中文](README.zh-CN.md)

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
docs/cases/           Public case studies from real reference runs
docs/quickstart.md    Runnable quick start
docs/quickstart.zh-CN.md Chinese quick start
docs/environment.md   Supported Python/OS/dependencies
docs/reproducibility.md Deterministic vs non-deterministic evidence
docs/limitations.md   What SCTG does not prove
docs/security-model.md Trust boundaries and command execution
docs/mode-policy.md   Shadow / Lite / Full transitions
docs/decision-model.md Request -> independent approval -> replay
docs/ledger.md        Append-only event and acceptance model
docs/versioning.md    Tags and release checklist
docs/faq.md           Common questions
docs/glossary.md      Terms
AGENTS.md             Rules for AI coding agents working on this repo
kit/                  Reference SCTG host runner, gates, and submission schema
examples/             Minimal task card and runnable end-to-end demo
tests/                Public repo smoke tests
scripts/check_repo.py Hygiene, links, secret-pattern check
kit/decision.py       Decision request/record/replay helper
kit/ledger.py         Append-only ledger helper
Makefile              check / test / demo / clean
.github/workflows/ci.yml CI on push and pull request
```

## Case studies

- [Ten cards, one transaction layer](docs/cases/01-ten-card-shadow-pilot.md) —
  the transaction layer runs, and a gate-green run still contains a semantic
  defect.
- [From PARTIAL to PASS](docs/cases/02-stage-2-governance.md) — preserve the
  historical PARTIAL, add remediation, re-audit with evidence.
- [Lite, adapter, and two seats](docs/cases/03-stage-2.5-lite-multi-seat.md) —
  Lite mode, independent join, real CLI alignment, and why single-line is per
  seat, not per run.

## Quick start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install pytest

make check
make test
make demo
```

`make demo` runs one complete transaction: card -> submission -> four gates ->
ledger. See [`docs/quickstart.md`](docs/quickstart.md) for the step-by-step
version, [`docs/quickstart.zh-CN.md`](docs/quickstart.zh-CN.md) for the Chinese
quick start, [`docs/environment.md`](docs/environment.md) for supported
environments, and [`docs/protocol.md`](docs/protocol.md) for the object model.

If you are an AI coding agent, read [`AGENTS.md`](AGENTS.md) first.

## Reproducibility

SCTG does not claim deterministic model output. It claims reproducible
transactions: the card, submission, gate result, evidence hashes, and decision
record can be replayed and audited.

See [`docs/reproducibility.md`](docs/reproducibility.md) for the exact commands,
what is deterministic, and what is not. CI runs `make check`, `make test`, and
`make demo` on every push.

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

## Project

- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Changelog](CHANGELOG.md)
- [Versioning](docs/versioning.md)
- [FAQ](docs/faq.md)
- [Glossary](docs/glossary.md)

## License

Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
