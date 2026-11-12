# Minimal example

`minimal-task.yaml` shows the smallest useful task card.

To render it, copy `kit/` into a run directory and use:

```bash
python3 kit/sctg.py render <run-dir> T-001 --attempt 1
```

The rendered card gets a `card_hash`. The seat writes a submission that echoes
that hash; the host then runs the configured gates.

A gate failure is not something to "work around" in the submission. It is a
signal to either fix the card/scope/evidence or stop and ask for a decision.
