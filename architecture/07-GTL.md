<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GTL — Generative Transitive Language

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES
**Purpose.** Describe GTL, a proposed functional engine and exploratory
language model within AGES. GTL is not a normative standard at this
stage; it is a pre-specification construct subject to research,
experimentation and RFC review
([`../rfcs/0010-gtl.md`](../rfcs/0010-gtl.md)).

## 1. Definition

GTL is a formal or semi-formal language for representing grounded
transitive action candidates.

The core question answered by GTL is:

> **What bounded and verifiable operation could realise the declared
> intent on an identified object of the world or system?**

Architecturally:

> GTL is the intermediate layer between structured procedural
> representation and validated cyber-physical or computational
> execution. Every transitive verb must be anchored to an identified
> object, an executor, an operational context, explicit limits and
> evidence of closure.

## 2. Binding structure

A GTL expression binds:

- an identified executor;
- a transitive operation;
- an identified direct object;
- an operational context;
- explicit preconditions;
- execution constraints;
- an admissible operational envelope;
- expected effects;
- failure and abort behaviour;
- rollback or compensation provisions;
- closure-evidence criteria.

The direct object is the identified entity upon which the transitive
operation is intended to act — physical, computational, informational or
organisational. The executor is the human, agent, service, controller,
machine or composite system assigned to perform the grounded operation.
The operational envelope is the explicit set of contextual, temporal,
physical, computational and authority limits within which the action
candidate may be executed ([`../GLOSSARY.md`](../GLOSSARY.md)).

## 3. Candidate, not command

GTL produces an **executable action candidate**, not an automatically
executable command.

> Technical executability is not permission to execute.

A GTL candidate becomes executable only after the applicable validation,
adjudication and authorisation requirements have been satisfied. A GTL
output is consistently an *action candidate* until authorised. GTL is
positioned before validation execution and governance adjudication, not
after ratification, and is not an intrinsic authority
([`03-evidence-and-authority.md`](03-evidence-and-authority.md)).

## 4. Position within the planes

GTL grounding is an Evolution Plane activity when applied to candidate
changes, and may serve the Operational Plane for bounded operational
actions under the current baseline. In both cases the Evolution Control
Plane receives both the semantic specification and the executable
specification for adjudication, and validation execution precedes
governance adjudication
([`01-architectural-planes.md`](01-architectural-planes.md)).

Where neural or otherwise generative mechanisms are used to produce GTL
expressions, generation is architecturally separated from independent,
deterministic validation of the resulting candidate: the subsystem that
generates a candidate does not adjudicate its admissibility.

## 5. Effectivity, failure and closure

Every GTL action candidate declares effectivity — where, when and to
which instances, environments and organisations it applies
([`04-effectivity.md`](04-effectivity.md)) — together with abort
conditions, a safe state, compensation or rollback provisions, and
closure-evidence criteria. Closure evidence is the evidence produced
during or after execution demonstrating whether the declared
postconditions, expected state and operational closure criteria were
achieved; it precedes any baseline ratification that depends on the
action ([`02-state-and-transition-model.md`](02-state-and-transition-model.md)).

## 6. Relation to GENTILE

GTL consumes negotiated semantic artefacts produced by GENTILE
([`06-GENTILE.md`](06-GENTILE.md)) and grounds them into bounded,
inspectable action candidates. The handoff, lifecycle and formal sketch
are described in
[`08-gentile-gtl-integration.md`](08-gentile-gtl-integration.md).

**Related.**
[`06-GENTILE.md`](06-GENTILE.md) ·
[`08-gentile-gtl-integration.md`](08-gentile-gtl-integration.md) ·
[`04-effectivity.md`](04-effectivity.md) ·
[`../GLOSSARY.md`](../GLOSSARY.md) ·
[`../rfcs/0010-gtl.md`](../rfcs/0010-gtl.md)
