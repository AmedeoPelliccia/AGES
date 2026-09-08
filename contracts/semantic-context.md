<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Contract — SemanticContext

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define the working contract for the artefact through which
contextual understanding is exchanged between engines. `SemanticContext` is
the contract name for the *contextual semantic structure* defined in
[`../GLOSSARY.md`](../GLOSSARY.md).

## Role

| Aspect | Value |
|---|---|
| Canonical producer | [GENIUSS](../engines/GENIUSS/README.md), or any conformant interpretation engine |
| Consumers | [GENTILE](../engines/GENTILE/README.md) (optional input), [GTL](../engines/GTL/README.md) (optional input), AGES evidence and governance services |
| Answers | What does the input mean in the current context? |
| Is not | Intent, a candidate change, an action candidate, authority, evidence adjudication |

A `SemanticContext` is always an **interpretation**. When it supports a
governance decision it enters the evidence chain as an interpretation, not as
a measurement
([`../architecture/03-evidence-and-authority.md`](../architecture/03-evidence-and-authority.md)).

## Content expectations

A conformant `SemanticContext` should expose:

- entities, events and concepts;
- relations and roles between them;
- attributes and properties;
- confidence and competing hypotheses
  ([`confidence-model.md`](confidence-model.md));
- salience;
- temporal and state information;
- unresolved ambiguity, declared rather than silently resolved;
- a provenance envelope tracing every assertion to its source observations
  ([`provenance-envelope.md`](provenance-envelope.md)).

The abstract structure is sketched in
[`../architecture/12-GENIUSS.md`](../architecture/12-GENIUSS.md) as:

$$
\Sigma(t) = \langle V,\ E,\ R,\ A,\ C,\ H,\ T \rangle
$$

An illustrative, non-normative rendering is
[`../schemas/examples/geniuss-semantic-structure.example.yaml`](../schemas/examples/geniuss-semantic-structure.example.yaml).

## Consumption rules

- Consumers must treat the artefact as **optional context**: no engine may
  structurally require a `SemanticContext` from a specific producer.
- Consumers must not treat a contained hypothesis as an established fact or
  precondition; the dependency and its confidence must be carried forward.
- Consumers must preserve the provenance envelope of any element they reuse.

## Related

- [`../engines/GENIUSS/contract.md`](../engines/GENIUSS/contract.md)
- [`../engines/GENIUSS/semantic-model.md`](../engines/GENIUSS/semantic-model.md)
- [`intent-artefact.md`](intent-artefact.md)
- [`action-candidate.md`](action-candidate.md)
