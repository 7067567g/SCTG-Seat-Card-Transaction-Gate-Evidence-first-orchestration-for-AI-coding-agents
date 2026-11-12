# Decision model

A Decision is an object, not a chat message.

```text
Decision Request -> independent MAIN review -> Decision Record -> replay checks -> ledger
```

## Request

A request must include:

- at least two options;
- a non-empty scope;
- an expiry;
- a bound object hash (`sha256:...`);
- a recommendation that is one of the option ids;
- a rollback when the request changes mode.

Schema: [`../kit/schemas/decision-request.schema.json`](../kit/schemas/decision-request.schema.json)

## Record

A record must include:

- `approved_by: MAIN`;
- a chosen option;
- a bound object hash;
- scope and expiry;
- rollback for mode changes;
- the approval timestamp.

Schema: [`../kit/schemas/decision-record.schema.json`](../kit/schemas/decision-record.schema.json)

## Replay

A Decision is only useful if it can be replayed. At minimum:

| Case | Expected |
|---|---|
| in-scope action | allowed |
| out-of-scope action | rejected |
| expired record | rejected |
| producer approves own output | rejected |

The reference implementation lives in [`../kit/decision.py`](../kit/decision.py).

## Independence

The requester and the producer must not be the approver. `approved_by: MAIN`
is not enough if the same person/seat produced the object.
