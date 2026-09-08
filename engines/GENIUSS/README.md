<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GENIUSS — Engine

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

> **GENIUSS — Graph Engine for Neural Integration and Understanding of
> Semantic Structures.**
>
> **GENIUSS integrates meaning.**

GENIUSS is an autonomous functional engine that transforms heterogeneous
contextual observations into an integrated, inspectable
[`SemanticContext`](../../contracts/semantic-context.md). It answers:

> **What does this input mean in the current context?**

It is an engine of understanding, not of intent, authority or action. It is a
cognitive and semantic integration engine, not a graphical rendering engine,
and the architecture makes no claim of machine consciousness or sentience.

## Contents

| Document | Purpose |
|---|---|
| [`contract.md`](contract.md) | Input/output contract and independence clauses |
| [`semantic-model.md`](semantic-model.md) | The semantic-structure model produced by the engine |

## Scope

GENIUSS is independent: it does not know that
[GENTILE](../GENTILE/README.md) or [GTL](../GTL/README.md) exist. It produces
artefacts conforming to
[`../../contracts/semantic-context.md`](../../contracts/semantic-context.md),
which any conformant consumer — including, but not only, GENTILE and GTL —
may use.

Compatible implementations may be neural, symbolic, neuro-symbolic,
statistical, rule-based, model-driven, multi-agent, human-in-the-loop or
hybrid, provided they preserve explicit entities, relations, confidence,
competing hypotheses and traceability to source observations.

## Authoritative references

- Architecture: [`../../architecture/12-GENIUSS.md`](../../architecture/12-GENIUSS.md)
- Draft RFC: [`../../rfcs/0018-geniuss.md`](../../rfcs/0018-geniuss.md)
- Example structure: [`../../schemas/examples/geniuss-semantic-structure.example.yaml`](../../schemas/examples/geniuss-semantic-structure.example.yaml)
- Worked example: [`../../examples/geniuss-gentile-gtl-governance.md`](../../examples/geniuss-gentile-gtl-governance.md)
