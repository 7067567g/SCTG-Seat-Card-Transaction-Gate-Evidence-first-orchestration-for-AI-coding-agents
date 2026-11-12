# Concepts

SCTG treats one unit of agent work as a transaction, not as a chat message.

## The transaction

| Object | Question it answers | Produced by |
|---|---|---|
| **Task Card** | What exactly is being done, with which inputs and write scope? | Host driver |
| **Submission** | What did the seat actually do, and what evidence supports it? | Execution seat |
| **GateResult** | Does the submission pass schema, scope, evidence, and command checks? | Host driver running deterministic gates |
| **Decision Record** | Is an irreversible move authorized, by whom, with what scope/expiry/rollback? | Independent MAIN approver |
| **Ledger** | What actually happened, in append-only order? | Host driver |

## Roles

- **MAIN**: the only approval authority. Does not produce the object it approves.
- **Host driver**: deterministic orchestrator. Renders cards, dispatches, collects,
  runs gates, writes ledger entries, and performs rollback. It never writes a
  GateResult as if it were a reviewer and never writes the seat's product.
- **Execution seat**: reads one card, writes one submission, stops. It may not
  self-approve or write outside its write scope.
- **QA / reviewer**: evaluates evidence and semantic correctness independently.
- **PMO**: owns plan, status, scope, and closeout. Does not issue Decisions.

## Three invariants

1. One active card per seat.
2. Producer is not approver.
3. Every mode change or irreversible action has a scoped, expiring Decision with
   a rollback path.
