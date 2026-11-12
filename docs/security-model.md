# Security model

## Trust boundaries

- A **task card** is host-authored and should be treated as a scoped instruction.
- A **submission** is untrusted input. It may lie, omit evidence, or reference
  paths outside the intended scope.
- A **gate** is deterministic code, but it is still code. Review changes to gates.
- A **decision record** is only meaningful if it is approved by an independent
  authority and bound to the object hash.

## Command execution

`g3_command` executes the submission's `test_command` in the project root. This
is powerful and dangerous.

Recommendations:

- run in an isolated workspace or container;
- do not give the seat production credentials;
- do not run untrusted submissions on a host with sensitive data;
- restrict network access when possible;
- treat `test_command` as untrusted input, even when a gate is configured.

## Write scope

`g1_scope` compares declared write scope against actual repository changes. It is
a consistency check, not a sandbox. It does not prevent a malicious command from
writing outside scope; it only detects and reports the mismatch afterward.

## Secrets

Never commit:

- API keys or tokens;
- `.env` files;
- private keys;
- transcripts containing credentials;
- absolute local paths.

`scripts/check_repo.py` scans for common patterns, but it is not a substitute for
a secret scanner or a human review.

## Approval independence

A producer must not approve its own output. Mode changes and irreversible actions
need an independent decision with:

- a bound object hash;
- a non-empty scope;
- an expiry;
- a rollback path;
- replay evidence for in-scope, out-of-scope, and expired cases.
