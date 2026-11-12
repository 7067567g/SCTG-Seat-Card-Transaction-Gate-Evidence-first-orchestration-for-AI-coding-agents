# From PARTIAL to PASS

> Stage: governed transaction layer  
> Shape: two 10-card pilots plus remediation rounds  
> Public takeaway: **preserve the historical PARTIAL; earn the later PASS.**

## Context

After the first 10-card pilot, the next problem was governance:

> Can the transaction layer be reviewed, replayed, and reused without turning
> every run into an untraceable pile of chat history?

The next stage added a contract, remediation rounds, independent approval, and a
final certification matrix.

## Scope

- two formal 10-card pilots, 20 cards total;
- code, documentation, and review cards;
- conditional semantic review;
- evidence freeze, structured failure, gate-result schema;
- decision records with independent MAIN approval;
- a final exit matrix with per-criterion evidence.

## The first audit was PARTIAL

The first certification was not PASS. It was **PARTIAL**.

That result was kept. The team did not edit the old certification to make the
project look healthier. Instead, the gaps were turned into remediation rounds:

- evidence for checks that had only been asserted;
- cold-start evidence for contract loading;
- negative probes for the scope gate;
- a proper re-audit after remediation.

The final re-audit reached:

```text
21 PASS / 1 DEFERRED
```

The deferred item was explicit: Lite mode, Full mode, adapter, and multi-seat
join were moved to a separate stage. Deferral was not silently converted into a
pass.

## What the run proved

- A single green gate is not enough; the **audit itself** needs a schema and
  evidence.
- Conditional review can catch semantic problems the gate cannot.
- A historical PARTIAL is useful evidence. Rewriting it destroys the audit trail.
- A final PASS is credible only if the remediation path is visible.

## What did not get claimed

The run explicitly accepted three limits:

- early rounds predated the machine-checkable contract;
- token/cost could not be collected at runtime, so the record says
  `unavailable + reason` rather than `0`;
- a post-hoc writer audit is a consistency check, not runtime identity proof.

These were recorded as risks, not hidden.

## Takeaway

> Do not rewrite a PARTIAL into a PASS. Keep the PARTIAL, add remediation,
> re-audit, and let the evidence show the change.
