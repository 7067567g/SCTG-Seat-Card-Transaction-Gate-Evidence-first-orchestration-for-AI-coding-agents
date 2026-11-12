# Reference status

This repository is distilled from a Stage-2.5 reference run that exercised:

- Lite mode decision with independent MAIN approval, scope, expiry, and rollback;
- a 5-card Lite pilot with code, doc, review, fix, and close cards;
- a two-seat handoff + join drill;
- adapter v0 with real read-only CLI alignment and a local idempotency ledger;
- final exit audit: 24/24 PASS;
- Full mode intentionally left closed.

What this does **not** mean:

- it is not a production deployment;
- it does not prove Full-mode orchestration;
- it does not replace independent review with deterministic gates;
- it does not make chat transcripts audit evidence.

The public repo intentionally excludes private run logs, transcripts, absolute
local paths, and internal operational data.
