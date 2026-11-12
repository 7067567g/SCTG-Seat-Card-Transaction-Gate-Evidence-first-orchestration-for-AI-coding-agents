# Limitations

SCTG is deliberately narrow.

## What it does not prove

- It does not prove that a report's numbers are correct.
- It does not prove that a design is good.
- It does not prove that a code change is secure.
- It does not prove that a model will produce the same output twice.
- It does not make a chat transcript into audit evidence.

## What the gates cover

```text
schema       -> shape
scope        -> writes stayed inside the declared boundary
evidence     -> referenced artifacts exist and hash
command      -> the declared test command exited as expected
```

That is form, boundary, evidence, and reproducibility. It is not semantic truth.

## What needs independent review

- semantic correctness;
- architecture and design quality;
- data interpretation;
- security and privacy judgment;
- whether accepting a risk is justified.

## What is out of scope

- a production scheduler;
- a full workflow engine;
- an OpenRig adapter (see the separate integration boundary);
- Full-mode orchestration;
- multi-tenant isolation;
- cost/token accounting guarantees.

## Public claim

This repository is a reference kit and a set of public case studies. It is not a
production platform and does not claim that Full mode has been validated.
