# Mode policy

SCTG has three modes. They are not labels; each transition needs evidence.

| Mode | Who advances work | Gate role | Host fallback | Default |
|---|---|---|---|---|
| `shadow` | Host / human | Observe only | Always available | Yes |
| `lite` | SCTG proposes and advances approved cards | Gate participates | Host can pause/take over/rollback | No |
| `full` | SCTG drives the main flow | Stronger constraints | Reduced | No |

## Transitions

```text
shadow -> lite : Decision + rollback + scope/expiry + Lite pilot plan
lite   -> full : independent Decision + rollback + >=1 real Lite run
shadow -> full : forbidden
lite   -> shadow : rollback + ledger record
full   -> lite : rollback + ledger record
```

## Lite is not "shadow with logs"

Lite has three minimum promises:

1. Gate results actually participate in advancement.
2. The host can unilaterally pause, take over, or roll back.
3. Every mode switch has a Decision and ledger record.

## Full is out of scope for this reference

The public reference does not claim Full-mode validation. Full requires its own
Decision, rollback design, and real Lite evidence.
