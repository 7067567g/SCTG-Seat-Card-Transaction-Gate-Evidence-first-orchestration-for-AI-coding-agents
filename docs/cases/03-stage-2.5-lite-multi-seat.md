# Lite, adapter, and two seats

> Stage: Lite mode, adapter alignment, multi-seat join  
> Shape: one 5-card Lite pilot, one two-seat handoff, one real CLI alignment pass  
> Public takeaway: **OpenRig single-line is per seat, not per run.**

## Context

The next questions were practical:

- Can a Lite mode run while the host keeps a rollback path?
- Can two seats hand off work without self-review?
- Can an adapter talk to a real execution CLI without writing its database?
- What happens when an audit finds that earlier evidence was only simulated?

## Lite mode

A Lite mode decision was approved by an independent MAIN approver. The decision
was scoped, expiring, and carried a rollback:

```text
shadow -> lite (R07 pilot only)
rollback: freeze dispatch -> drain in-flight -> write shadow -> host probe -> reconcile
```

The pilot ran five cards:

| Card | Kind | Result |
|---|---|---|
| L01 | code | PASS |
| L02 | doc | PASS |
| L03 | independent review | PASS |
| L04 | fix | PASS |
| L05 | close | PASS |

The review card was executed by a different seat. The pilot also ran a rollback
drill and returned to Shadow. The gate did not decide the mode change; an
independent MAIN decision did.

## Two seats, one line each

The handoff case used two seats:

```text
producer -> handoff artifact -> reviewer -> join result
```

The reviewer bound its result to the producer's artifact hash and recorded zero
scope conflicts. Each seat was single-line. The run was not parallel; it was
sequenced.

This is the key clarification:

> OpenRig-style single-line means one active card per seat, not one seat per run.

## The adapter problem

The first adapter mapping looked plausible but was wrong:

```text
claimed: rig queue add --run ... --task ...
actual:  rig queue create --destination ... --body ...
```

The first exit audit marked the adapter criteria PARTIAL because the evidence was
simulated, not aligned with the real CLI. That PARTIAL was preserved.

A later round ran real read-only CLI probes, discovered the flag mismatch, and
corrected the mapping. Another round performed argument-accurate dry-run
idempotency checks. The final re-audit reached:

```text
24 / 24 PASS
```

The full stage used 14 rounds against a cap of 15. The cap was a maximum, not a
target. It was extended only because an audit found missing evidence.

## What the run proved

- A Lite mode is not "Shadow with more logs"; it has an explicit decision,
  rollback, and host fallback.
- Independent review requires a different seat, not a different prompt in the
  same seat.
- A real CLI adapter must be checked against real commands and flags.
- A historical PARTIAL can be closed by evidence, not by editing the audit.
- Technical PASS and project closeout are different termination conditions.

## Takeaway

> Single-line seats make multi-seat work safer: each seat has one card, and the
> host sequences the handoff. The hard part is not concurrency; it is keeping
> approval, evidence, and scope boundaries honest.
