# AGENTS.md

Instructions for AI coding agents working on this repository.

## Before changing anything

1. Read `README.md`, `README.zh-CN.md`, and the relevant `docs/`.
2. Run `make check`, `make test`, and `make demo`.
3. Keep changes small and scoped.

## Public-repo rules

- Do not commit secrets, tokens, `.env` files, private keys, transcripts, or
  absolute local paths.
- Do not add `node_modules` or vendored third-party source.
- Do not edit `LICENSE`, `NOTICE`, or `THIRD_PARTY_NOTICES.md` without explicit
  review.
- Do not imply that OpenRig endorses this repository.
- Do not claim production readiness or Full-mode validation.

## Bilingual docs

- `README.md` is English.
- `README.zh-CN.md` is Simplified Chinese.
- Keep the two READMEs in sync when changing public positioning, quick start, or
  status.
- `docs/quickstart.zh-CN.md` mirrors `docs/quickstart.md`.

## Change discipline

- Update `CHANGELOG.md` and `VERSION` for public API or behavior changes.
- If you add a required file, update `scripts/check_repo.py`.
- Use `make check` before every commit.
- Do not rewrite published history. Add new commits and tags instead.

## Security

`g3_command` executes submission-declared commands. Treat submissions as
untrusted input and run them in an isolated workspace when possible.
