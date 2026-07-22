<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0011 — GENTILE–GTL Integration Lifecycle

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes the lifecycle through which the two functional
engines — [GENTILE](0009-gentile.md) and [GTL](0010-gtl.md) — integrate
with the AGES planes, candidate changes, validation, adjudication,
execution, closure evidence and baseline ratification.

## Motivation

GENTILE and GTL are individually useful but only become an evolutionary
mechanism when their handoff and ordering constraints are declared.
This RFC fixes those constraints without granting either engine
authority.

## GENTILE-to-GTL handoff

GTL consumes a semantic artefact that has reached semantic closure and
carries a classification. The handoff transfers the artefact's
constraints, invariants and acceptance criteria into the grounding
inputs; unresolved ambiguity blocks grounding or is explicitly carried
forward as declared uncertainty.

## Candidate-change formation

For evolutionary intent, a candidate change is formed from the semantic
artefact before grounding, so the governance object exists prior to any
executable specification ([`../GLOSSARY.md`](../GLOSSARY.md)).

## Action-candidate generation

GTL generates one or more action candidates per candidate change or per
operational request. Alternative candidates may form a set offered to
adjudication.

## Ordering constraints

1. **Validation before adjudication.** The Evolution Plane executes
   validation on the action candidate; the Evolution Control Plane
   adjudicates the resulting evidence together with the semantic
   artefact.
2. **Authorisation before execution.** No candidate executes without a
   governance verdict permitting it.
3. **Closure evidence before ratification.** A successor baseline is
   ratified only after successful execution and closure verification.

## Operational actions and ages

Operational uses of GENTILE and GTL do not create new ages. An
operational action is authorised, executed and closed under the current
ratified baseline; only ratified evolution transitions open a new age
([`../theory/03-baselines-and-ages.md`](../theory/03-baselines-and-ages.md)).

## Rollback and compensation

Every action candidate declares failure behaviour. For evolutionary
deployments the rollback target is the predecessor baseline; for
operational actions, compensation restores or preserves the declared
safe state. Rollback remains governed, consistent with
[`../architecture/01-architectural-planes.md`](../architecture/01-architectural-planes.md).

## Alternative candidate sets

Adjudication may consider a bounded set of alternative GTL candidates
for the same intent. Whether such a set may be authorised as a whole,
with runtime selection inside the authorised envelope, is an open
question.

## Alternatives considered

Direct GENTILE-to-execution flow (rejected: no bounded, inspectable
specification); merging GENTILE and GTL into one engine (rejected: the
distinction between "what is intended" and "what operation could
realise it" is load-bearing); post-hoc grounding after adjudication
(rejected: the Control Plane must receive both the semantic and the
executable specification).

## Compatibility impact

Additive. The lifecycle refines — and does not alter — the existing
AGES ordering: validation before adjudication, authorisation before
execution, deployment before ratification.

## Unresolved questions

How closure-evidence requirements derive from semantic acceptance
criteria; when an authorised execution creates a new AGES age; whether
a failed action can produce a valid recovery baseline; how human,
organisational and delegated machine authority combine
([`../research/open-questions.md`](../research/open-questions.md)).

## Decision record

None. This RFC is a Draft and has not been adjudicated.
