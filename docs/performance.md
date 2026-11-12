# Performance

SCTG's gates are intentionally small deterministic checks. This is not a
benchmark against an agent runtime; it measures the reference kit overhead.

Run:

```bash
make bench
```

The benchmark measures:

- card digest computation over a small synthetic card body;
- write-scope prefix matching.

Results are environment-dependent. The important property is that gate overhead
is negligible compared with model latency; the expensive part is the agent
execution, not schema/scope/evidence/command checks.


## Reference measurement

Measured on the local reference environment (Python 3.12, Linux):

```text
card_digest_10k:  median 0.00311 ms, p95 0.004149 ms
scope_match_100k: median 0.000162 ms, p95 0.000188 ms
```

These numbers measure reference-kit overhead only. They do not include model
latency, process startup, or gate subprocess execution.
