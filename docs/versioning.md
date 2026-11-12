# Versioning

SCTG uses annotated tags and semantic versioning.

## Tags

| Tag | Meaning |
|---|---|
| `v0.1.0` | initial public reference |
| `v0.2.0` | public case studies |
| `v0.3.0` | runnable, reproducible, bilingual |
| `v0.4.0` | contract schemas, negative tests, community files |
| `v0.5.0` | examples, toolchain, package entry point, benchmarks |

Published tags are never moved or deleted.

## Release checklist

1. `VERSION` and `pyproject.toml` agree.
2. `CHANGELOG.md` has an entry.
3. `make check`, `make test`, `make demo` pass.
4. README and Chinese README are in sync for public positioning.
5. Tag is annotated and pushed.
