<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GENTILE — Engine

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

> **GENTILE — Generative Engine for Neural Transformation through Interactive
> Language Exchange.**
>
> **GENTILE co-constructs intent.**

GENTILE is an autonomous functional engine that transforms interactive
language exchange — optionally grounded in a
[`SemanticContext`](../../contracts/semantic-context.md) — into a negotiated
[`IntentArtefact`](../../contracts/intent-artefact.md). It answers:

> **What is intended?**

It is an engine of negotiated meaning, not of interpretation of the
environment, and not of authorisation or execution.

## Contents

| Document | Purpose |
|---|---|
| [`contract.md`](contract.md) | Input/output contract and independence clauses |
| [`intent-model.md`](intent-model.md) | The negotiated-intent artefact model produced by the engine |

## Scope

GENTILE is independent: its optional context input keeps it free of any
structural dependency on [GENIUSS](../GENIUSS/README.md), and it does not
know that [GTL](../GTL/README.md) exists. It produces artefacts conforming to
[`../../contracts/intent-artefact.md`](../../contracts/intent-artefact.md)
for any conformant consumer.

Compatible implementations may be neural, symbolic, neuro-symbolic,
rule-based or human-in-the-loop, provided they preserve interactive
co-construction, provenance and structured semantic closure.

## Authoritative references

- Architecture: [`../../architecture/06-GENTILE.md`](../../architecture/06-GENTILE.md)
- Draft RFC: [`../../rfcs/0009-gentile.md`](../../rfcs/0009-gentile.md)
- Example artefact: [`../../schemas/examples/gentile-artefact.example.yaml`](../../schemas/examples/gentile-artefact.example.yaml)
- Worked example: [`../../examples/gentile-gtl-operational-request.md`](../../examples/gentile-gtl-operational-request.md)
