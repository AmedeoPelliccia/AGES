<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0014 — Multi-Rate Autonomy

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes the multi-rate autonomy relation for AGES-CPS:
real-time control, operational autonomy, adaptation and learning, and
evolution governance operate at ordered characteristic timescales, and
the Evolution Control Plane must not normally be placed in the hard
real-time control path.

## Motivation

Placing governance in a servo loop is neither feasible nor desirable;
excluding governance entirely leaves adaptation ungoverned. A
timescale model is needed that lets fast loops run inside envelopes
authorised by slower loops.

## Proposal

* Adopt the conceptual relation and table in
  [`../models/multi-rate-autonomy-model.md`](../models/multi-rate-autonomy-model.md);
  prescribe no universal timing values.
* Define the governance responsibilities at the slowest rate: which
  controllers and models may be active, which parameters may adapt,
  permitted adaptation ranges, delegated runtime authority, when
  adaptation becomes a candidate change, and when the resulting
  configuration may be ratified.
* Define the delegated operational envelope
  ([`../profiles/AGES-CPS/05-delegated-operational-envelopes.md`](../profiles/AGES-CPS/05-delegated-operational-envelopes.md))
  as the interface between governance and runtime freedom.

## Safety boundary

Runtime safety mechanisms remain independent of governance; governance
failure must not disable hard safety limits.

## Open questions

When online learning becomes evolutionary change; how emergency
authority should be bounded and time-limited.

## Status

Draft. Not accepted.
