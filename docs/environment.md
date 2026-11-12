# Environment

## Supported

| Item | Supported |
|---|---|
| Python | 3.11+ |
| CI Python | 3.12 |
| Local test Python | 3.14 |
| OS | Linux, macOS, WSL |
| Make | GNU Make 4.x |
| Git | needed for `g1_scope` and normal version control |

Windows native is not tested. WSL is recommended.

## Python dependencies

```text
PyYAML>=6.0
jsonschema>=4.0
pytest>=8.0   # tests only
```

Install:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install pytest
```

## Commands

```bash
make check   # hygiene, links, Python compile
make test    # tests + check
make demo    # one end-to-end four-gate transaction
```

## Network

- `make check`, `make test`, and `make demo` work offline.
- `git push` needs GitHub HTTPS access.
- If push fails with TLS/HTTP2 errors, retry after the network recovers.

## Optional tools

- `git` is required for `g1_scope` to compare declared scope against repository
  changes.
- A container runtime is not required by the reference kit, but is recommended
  when executing untrusted submissions because `g3_command` runs commands.
