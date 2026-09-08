<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GTL — Engine

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

> **GTL — Generative Transitive Language.**
>
> **GTL grounds meaning into action.**

GTL is an autonomous functional engine that transforms a structured semantic
or intent artefact — optionally grounded in a
[`SemanticContext`](../../contracts/semantic-context.md) and a capability
registry — into one or more bounded
[`ActionCandidate`](../../contracts/action-candidate.md) artefacts. It
answers:

> **What bounded operation could realise the intended state?**

The defining boundary of the engine is:

> **GTL ≠ executor, and ActionCandidate ≠ AuthorisedAction.**

## Contents

| Document | Purpose |
|---|---|
| [`contract.md`](contract.md) | Input/output contract and independence clauses |
| [`action-candidate-model.md`](action-candidate-model.md) | The grounded action-candidate model produced by the engine |

## Scope

GTL is independent: it consumes any conformant structured artefact — an
[`IntentArtefact`](../../contracts/intent-artefact.md) from
[GENTILE](../GENTILE/README.md), a
[`SemanticContext`](../../contracts/semantic-context.md) from
[GENIUSS](../GENIUSS/README.md), or an equivalently structured artefact from
another conformant producer — without knowing the producer's implementation.

Its candidates may be translated through adapters into behaviour trees, task
graphs, motion-planning requests, deployment procedures, configuration
deltas, service sequences or safe-state procedures; the adapters, like the
executors, are outside the engine.

## Authoritative references

- Architecture: [`../../architecture/07-GTL.md`](../../architecture/07-GTL.md)
- Draft RFC: [`../../rfcs/0010-gtl.md`](../../rfcs/0010-gtl.md)
- Example candidate: [`../../schemas/examples/gtl-action-candidate.example.yaml`](../../schemas/examples/gtl-action-candidate.example.yaml)
- Worked example: [`../../examples/bounded-cyber-physical-action.md`](../../examples/bounded-cyber-physical-action.md)
