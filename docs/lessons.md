# Lessons

## 1. OpenRig single-line means per-seat, not per-run

The useful constraint is:

> one active task/channel per seat.

It is not:

> one seat per run.

A run can use several seats, each strictly single-line.

## 2. Round shapes differ, transaction model does not

- single-card round: one seat, one card;
- multi-card round: one seat, N cards sequentially;
- multi-seat round: producer + independent reviewer/integrator.

All three use the same Task Card -> Submission -> Gate -> Ledger path.

## 3. PASS and closeout are different termination conditions

An autopilot should distinguish:

1. **technical completion**: certification says PASS;
2. **project closeout**: final package, control plane closed, runtimes archived.

A driver that stops at PASS but leaves the project half-closed has not finished
the job. A closeout round is not a remediation round.

## 4. The cap is a maximum, not a target

If the estimated plan is 9 rounds and the cap is 15, the driver should not run to
15 by default. It should stop when the acceptance criteria are met, and only add
remediation rounds when evidence is missing or a check fails.
