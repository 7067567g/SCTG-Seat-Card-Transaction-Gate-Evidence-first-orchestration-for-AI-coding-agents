# Security

This repository is a reference implementation, not a hosted service.

Please do not open a public issue for a secret leak. If you find a credential,
token, or private path committed here, contact the maintainer privately and
include the file path and commit hash.

The reference kit executes commands declared in task submissions. Treat task
cards and submissions as untrusted input, run them in an isolated workspace,
and never give a production seat self-approval authority.
