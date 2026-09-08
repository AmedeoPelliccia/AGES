<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Contract — IntentArtefact

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define the working contract for the artefact through which
negotiated intent is exchanged between engines. `IntentArtefact` is the
contract name for the negotiated *semantic artefact* defined in
[`../GLOSSARY.md`](../GLOSSARY.md).

## Role

| Aspect | Value |
|---|---|
| Canonical producer | [GENTILE](../engines/GENTILE/README.md), or any conformant intent-negotiation engine |
| Consumers | Intent classification, [GTL](../engines/GTL/README.md), candidate-change formation, governance services |
| Answers | What is intended? |
| Is not | An interpretation of the environment, a candidate change, an action candidate, an authorisation |

## Content expectations

A conformant `IntentArtefact` should expose:

- the negotiated intended state or objective;
- its declared classification (operational request, evolutionary intent,
  requirement, evidentiary statement, governance request, or another declared
  class);
- context, assumptions and constraints;
- acceptance criteria;
- unresolved ambiguity and open issues, explicitly declared;
- rejected interpretations recorded during negotiation;
- confidence where agreement is partial
  ([`confidence-model.md`](confidence-model.md));
- a provenance envelope covering the exchange from which the artefact was
  co-constructed ([`provenance-envelope.md`](provenance-envelope.md)).

Minimal fields and semantic-closure conditions are described in
[`../architecture/06-GENTILE.md`](../architecture/06-GENTILE.md). An
illustrative, non-normative rendering is
[`../schemas/examples/gentile-artefact.example.yaml`](../schemas/examples/gentile-artefact.example.yaml).

## Consumption rules

- An `IntentArtefact` may reference a
  [`SemanticContext`](semantic-context.md); the reference is **optional** and
  must be resolvable without access to the producing engine.
- Semantic agreement recorded in the artefact is not governance
  authorisation.
- An evolutionary `IntentArtefact` does not become a candidate change until
  it is classified and registered with the required governance metadata
  ([`../architecture/02-state-and-transition-model.md`](../architecture/02-state-and-transition-model.md)).

## Related

- [`../engines/GENTILE/contract.md`](../engines/GENTILE/contract.md)
- [`../engines/GENTILE/intent-model.md`](../engines/GENTILE/intent-model.md)
- [`semantic-context.md`](semantic-context.md)
- [`action-candidate.md`](action-candidate.md)
