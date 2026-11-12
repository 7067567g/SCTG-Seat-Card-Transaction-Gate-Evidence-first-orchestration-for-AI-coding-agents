# Reproducibility

## What is deterministic

Given the same repository, task card, submission, and environment, these are
deterministic:

- card hash computation (excluding the `card_hash` line itself);
- schema check;
- write-scope comparison;
- evidence path existence and hashes;
- declared command exit-code check;
- ledger row ordering for a single host driver.

## What is not deterministic

An LLM seat is not deterministic. Re-running the same prompt may produce a
different submission. SCTG does not claim model-output determinism.

What SCTG can do is make the **transaction** reproducible:

- the exact card that was active;
- the exact submission that was accepted;
- the exact gate results;
- the exact evidence hashes;
- the exact decision record and scope.

## Exact commands

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install pytest

make check
make test
make demo
```

## Evidence to keep

For a real run, keep at least:

```text
rendered card
submission
gate result
acceptance ledger row
artifact hashes
decision record (when applicable)
```

Do not keep secrets, private transcripts, or personal data in the public repo.

## CI

GitHub Actions runs `make check`, `make test`, and `make demo` on every push and
pull request. The demo is the smallest end-to-end reproducibility check.

## What cannot be reproduced from artifacts alone

- the model's internal reasoning;
- a semantic review that was never written down;
- a mode change that has no Decision record;
- a "PASS" that has no bound evidence.
