<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0009 — GENTILE: Generative Engine for Neural Transformation through Interactive Language Exchange

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes GENTILE — Generative Engine for Neural Transformation
through Interactive Language Exchange — as a functional engine within
AGES: an interactive and co-constructive transformation engine that
converts human or system intent, contextual information and iterative
language exchanges into negotiated, structured and machine-interpretable
semantic artefacts.

## Motivation

AGES describes governed evolution but leaves open how intent enters the
lifecycle in reviewable form. Free-text intent is neither classifiable
nor adjudicable; one-way parsing loses the negotiation through which
assumptions, ambiguity and acceptance criteria surface. AGES therefore
needs an engine whose output is a structured, provenance-carrying
artefact that the planes can consume.

## Interactive co-construction

GENTILE is not a parser and not one-way generation. Participants —
human and artificial — progressively express intent, interpret context,
expose assumptions, identify ambiguity, request clarification,
negotiate terminology, revise constraints, identify invariants,
establish acceptance criteria and validate a shared semantic
representation. Rejected interpretations and revisions are retained in
the artefact's provenance.

## Semantic artefact model

A semantic artefact records intent, interaction history, context,
controlled terms, assumptions, constraints, invariants, unresolved
ambiguity, acceptance criteria, authority claims, classification and
provenance
([`../schemas/examples/gentile-artefact.example.yaml`](../schemas/examples/gentile-artefact.example.yaml),
non-normative).

## Intent classes

Operational intent · evolutionary intent · informational intent ·
procedural representation · requirement · candidate-change rationale ·
evidentiary statement · governance request · underspecified intent
requiring further interaction.

## Semantic closure

An artefact reaches semantic closure when it is sufficiently explicit,
structured and reviewed to support classification, validation or
downstream operationalisation, while preserving declared uncertainty
and unresolved issues. Closure is a property of the artefact, not an
approval.

## Provenance

Every artefact carries source records, participant identities, exchange
references, revision history, rejected interpretations and an integrity
hash, so the negotiation is reconstructable
([`../architecture/05-identity-and-provenance.md`](../architecture/05-identity-and-provenance.md)).

## Authority boundaries

GENTILE does not automatically authorise anything. Semantic agreement
is not governance authorisation. Artefacts carry authority *claims*;
the Evolution Control Plane evaluates them. GENTILE is not part of the
authority chain.

## Cross-plane use

GENTILE may produce operational, evolutionary, evidentiary and
governance artefacts, consumed respectively by the Operational Plane,
the Evolution Plane and the Evolution Control Plane
([`../architecture/06-GENTILE.md`](../architecture/06-GENTILE.md)).
Operational uses do not create a new baseline.

## Alternatives considered

Direct natural-language-to-action translation (rejected: no reviewable
intermediate); a static requirements template (rejected: loses the
interactive, co-constructive dimension); embedding intent capture in
GTL (rejected: conflates semantics with grounding).

## Compatibility impact

Additive. No existing AGES term is redefined; new glossary terms are
introduced ([`../GLOSSARY.md`](../GLOSSARY.md)). No broader GES
superclass is introduced.

## Unresolved questions

What constitutes sufficient semantic closure; whether an artefact can
be valid while participants retain conflicting interpretations; how
rejected interpretations should be preserved; which intent classes
require human confirmation; when operational intent becomes
evolutionary intent; whether GENTILE can generate governance artefacts
without becoming part of the authority chain
([`../research/open-questions.md`](../research/open-questions.md)).

## Decision record

None. This RFC is a Draft and has not been adjudicated.
