<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0018 — GENIUSS: Graph Engine for Neural Integration and Understanding of Semantic Structures

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-09-07

## Abstract

This RFC proposes GENIUSS — Graph Engine for Neural Integration and
Understanding of Semantic Structures — as a functional engine within
AGES: an integrative interpretation engine that converts heterogeneous
observations, current context and prior semantic state into a
contextualised semantic structure describing what the system currently
understands about its environment, inputs, entities, relations and
state.

## Motivation

AGES already defines how intent becomes a negotiated artefact
([GENTILE](../architecture/06-GENTILE.md)), how an artefact becomes a
bounded action candidate ([GTL](../architecture/07-GTL.md)) and how such
candidates are governed. It does not define how heterogeneous input —
sensors, telemetry, messages, events, history — becomes an inspectable
representation of the situation those engines presuppose. Without an
explicit engine, interpretation is performed implicitly inside GENTILE
or GTL, which conflates *what an input means* with *what an actor
intends* and hides the uncertainty on which later decisions rest.

## Position

GENIUSS answers "what does this input mean in the current context?";
GENTILE answers "what is intended?"; GTL answers "what operation could
realise the intended state?"; AGES governance answers "is the candidate
operation admissible and authorised?"
([`../architecture/12-GENIUSS.md`](../architecture/12-GENIUSS.md)).
GENIUSS is a cognitive and semantic integration engine, not a graphical
renderer, user-interface component, graph database or prescribed neural
architecture.

## Semantic structure model

A GENIUSS output is conceptually
$\Sigma(t) = \langle V, E, R, A, C, H, T \rangle$: entities, relations,
roles, attributes, confidence, hypotheses and temporal state
([`../schemas/examples/geniuss-semantic-structure.example.yaml`](../schemas/examples/geniuss-semantic-structure.example.yaml),
non-normative). Where a profile already defines a semantic
representation or world model, GENIUSS extends or maps to it rather than
introducing a competing model.

## Recursive interpretation

Interpretation may be conditioned by prior semantic state,
$\Sigma(t) = F(X(t), \Sigma(t-1), \mathrm{context}(t))$. This is an
interpretive mechanism only: changes to the GENIUSS configuration itself
remain candidate changes governed by the Evolution Control Plane, so
recursion implies no self-modification of the baseline.

## Uncertainty preservation

Confidence, ambiguity and competing hypotheses must remain
representable; GENIUSS must not convert uncertain interpretation into
false certainty. The semantic levels observation, inference, hypothesis,
assertion, decision, action candidate, authorisation and execution must
not collapse into one another.

## Provenance

Every semantic assertion is derived from observations that originated
from identified sources, preserving provenance, timestamps, confidence,
transformation identity and contextual dependencies, so that a
downstream decision can answer why the system believes a statement
([`../architecture/05-identity-and-provenance.md`](../architecture/05-identity-and-provenance.md)).

## Authority boundaries

GENIUSS produces understanding, not authorised action. It does not
negotiate intent, decide policy, authorise or execute, and the
architecture defines no GENIUSS → actuator path. A GENIUSS structure is
not a candidate change and is not evidence until adjudicated as such
([`../architecture/03-evidence-and-authority.md`](../architecture/03-evidence-and-authority.md)).

## Alternatives considered

Extending GENTILE to cover perception and interpretation (rejected:
conflates understanding with intent, and the co-construction cycle
presupposes an interlocutor that telemetry does not provide); extending
GTL with situation assessment (rejected: conflates grounding with
interpretation and would let inferences enter preconditions
unlabelled); leaving interpretation implicit in profile-specific world
models (rejected: no traceable, uncertainty-preserving contract for
downstream governance).

## Compatibility impact

Additive. No existing AGES term, identifier or interface is redefined;
GENTILE, GTL and the governance vocabulary are unchanged. New glossary
terms are introduced ([`../GLOSSARY.md`](../GLOSSARY.md)).

## Unresolved questions

What minimum structure constitutes a usable semantic structure; how
confidence should be represented across heterogeneous input classes;
when a hypothesis may be promoted to an assertion and by which
authority; how recursive state should be bounded against feedback
amplification; which GENIUSS outputs qualify as evidence and under which
class; how disagreement between several interpretation engines should be
reconciled ([`../research/open-questions.md`](../research/open-questions.md)).

## Decision record

None. This RFC is a Draft and has not been adjudicated.
