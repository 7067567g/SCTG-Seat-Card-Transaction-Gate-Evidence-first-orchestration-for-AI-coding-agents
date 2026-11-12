# FAQ

## Is SCTG an agent framework?

No. It is a control pattern plus a small reference kit that can sit on top of an
execution runtime.

## Does a green gate mean the work is correct?

No. Gates cover schema, scope, evidence, and command reproducibility. Semantic
correctness requires independent review.

## Is OpenRig required?

No. OpenRig is one execution-plane integration. The reference kit runs with a
plain Python host as well.

## What is single-line?

One active task/channel per seat. A run may still use multiple seats, sequenced
by the host.

## Why keep a PARTIAL audit?

Because rewriting history destroys the audit trail. Add remediation rounds and
re-audit instead.

## Is Full mode validated?

No. The public reference intentionally leaves Full mode closed.
