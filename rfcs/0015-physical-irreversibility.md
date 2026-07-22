<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0015 — Physical Irreversibility

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes recovery semantics for cyber-physical transitions in
which rollback does not mean restoration of the previous world state:
rollback, compensation, safe-state transition, containment, recovery
baseline and declared irreversibility as distinct modes.

## Motivation

Software rollback intuitions fail for physical actions. AGES-CPS needs
explicit, distinct recovery modes and explicit reversibility
declarations by candidate changes so that adjudication can weigh
physical risk before authorisation.

## Proposal

* Adopt the recovery-mode table in
  [`../profiles/AGES-CPS/08-irreversibility-and-recovery.md`](../profiles/AGES-CPS/08-irreversibility-and-recovery.md).
* Require candidate changes to declare: reversibility class, rollback
  feasibility, compensation strategy, safe-state target, irreversible
  effects, recovery authority and evidence required before execution.
* Define the recovery baseline as a ratified stable configuration after
  an abnormal or partially irreversible event
  ([`../schemas/examples/recovery-baseline.example.yaml`](../schemas/examples/recovery-baseline.example.yaml)),
  ratified only after evidence and closure verification.

## Open questions

How physically irreversible transitions should be ratified; whether a
failed deployment can produce a recovery baseline.

## Status

Draft. Not accepted.
