# Architecture

SCTG is a control layer, not a new agent runtime.

```text
+-----------------------------+
| Control plane               |
| scope, plan, gates, decisions|
+--------------+--------------+
               |
        task cards / evidence
               |
+--------------v--------------+
| Execution plane             |
| seats, channels, runtimes   |
+-----------------------------+
```

## Single-line seats

OpenRig-style runtimes are single-line **per seat**: one seat has one active
task/channel at a time. That does not mean a run has only one seat.

A run may use multiple seats, each single-line:

```text
control-main:  R06-A handoff
tdo-b:         R06-B join
```

They are sequenced by the host driver and never write the same scope.

## Three round shapes

| Shape | Example | Orchestration |
|---|---|---|
| Single-card round | design, adapter, audit | one seat, one card, one gate |
| Multi-card round | Lite pilot | one seat, N cards sequentially, gate each |
| Multi-seat round | handoff + join | producer seat + reviewer seat, sequenced |

The shapes differ only in host orchestration. The transaction model is the same.

## Why the host driver exists

The host driver is the deterministic part of the system:

- it decides which card is active;
- it dispatches one card to one seat;
- it waits for a stable submission;
- it runs gates and records the result;
- it performs mode switches and rollback;
- it never delegates approval to the producer.

This is what makes a run reproducible from artifacts instead of from a chat
transcript.
