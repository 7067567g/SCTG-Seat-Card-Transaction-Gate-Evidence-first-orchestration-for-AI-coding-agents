# Ten cards, one transaction layer

> Stage: Shadow pilot  
> Shape: one seat, ten sequential cards  
> Public takeaway: **a green gate is evidence of form, not proof of truth.**

## Context

The first useful question was not "can an agent write code?" but:

> Can a sequence of agent tasks be turned into explicit, auditable transactions
> without changing the execution runtime?

The pilot used a sidecar transaction layer around an existing agent seat:

```text
Task Card -> single seat -> Submission -> deterministic Gate -> Ledger
```

The card carried the task, inputs, write scope, and gate list. The seat wrote a
separate submission. The host rendered, dispatched, waited, gated, and recorded.
The seat never wrote the gate result.

## Scope

- 9 delivery cards plus 1 closeout card;
- one seat, cards executed sequentially;
- code, documentation, review, and fix work;
- deterministic gates for schema, scope, evidence, and command exit;
- append-only ledger for card, dispatch, submission, and acceptance.

## What the run proved

The transaction layer could run continuously:

| Metric | Result |
|---|---|
| Cards | 10 |
| Gate bundles | 10/10 passed all 5 checks |
| Delivery cards passing on attempt 1 | 9/9 |
| Delivery-card time | ~22.8 minutes |
| Total time including closeout | ~24.3 minutes |
| Test suite | 88 tests |
| Line coverage | ~94.6% |

This was enough to stop treating "card -> submission -> gate -> ledger" as a
hypothesis. The mechanics worked.

## What the gates missed

During the run, independent QA found a real data error in a report: a count that
should have been **49** had been written as **48**.

Every gate was green.

That is the important part. The gates checked:

- the submission had the required shape;
- files stayed inside the declared write scope;
- evidence paths existed and hashed;
- the declared command exited as expected.

They did **not** check whether the report's numbers were semantically correct.
A deterministic gate can prove that a claim is well-formed and reproducible. It
cannot prove that the claim is true.

## What changed

The failure did not lead to "add more gates". It led to a clearer division:

```text
Gate      -> structure, scope, evidence, reproducibility
Review    -> semantic correctness, architecture, data truth
MAIN      -> irreversible decisions and risk acceptance
```

The public lesson is not "the gate failed". The gate did its job. The system
failed if it treated a green gate as a complete quality claim.

## Takeaway

> A green gate is not a green light for truth.

Use deterministic gates to make a submission auditable. Use independent review
for meaning. Do not let either role pretend to be the other.
