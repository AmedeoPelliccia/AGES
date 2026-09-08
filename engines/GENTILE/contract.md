<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GENTILE — Contract

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** State the input/output contract that makes GENTILE an
independent, composable functional engine.

## 1. Transformation

$$
F_I : (L_t,\ \Sigma_t,\ I_{t-1}) \rightarrow I_t
$$

Where:

- $L_t$ — the interactive language exchange (**required**);
- $\Sigma_t$ — a semantic context supplied by any conformant interpreter,
  for example GENIUSS (**optional**);
- $I_{t-1}$ — prior intent state within the negotiation (**optional**);
- $I_t$ — the negotiated intent, emitted as an
  [`IntentArtefact`](../../contracts/intent-artefact.md).

In interface form:

```text
GENTILE(
    interaction,
    context?: SemanticContext,
    prior_intent?: IntentArtefact
) -> IntentArtefact
```

## 2. Optionality of context

$\Sigma_t$ **must remain optional**. If context were required, GENTILE would
depend structurally on GENIUSS and the engines would cease to be independent.
GENTILE works without GENIUSS whenever the necessary context is already
structured or is co-constructed within the exchange itself; when a
[`SemanticContext`](../../contracts/semantic-context.md) is supplied, GENTILE
may use it for grounding, and must surface its declared ambiguity for
negotiation rather than resolve it silently.

## 3. Output guarantees

The emitted `IntentArtefact` preserves:

- the negotiated intended state, with declared classification;
- context, assumptions, constraints and acceptance criteria;
- unresolved ambiguity and rejected interpretations;
- provenance of the co-constructive exchange
  ([`../../contracts/provenance-envelope.md`](../../contracts/provenance-envelope.md));
- declared confidence where agreement is partial
  ([`../../contracts/confidence-model.md`](../../contracts/confidence-model.md)).

## 4. Independence clauses

- GENTILE **does not require GENIUSS** and does not know its implementation.
- GENTILE **does not know that GTL exists**; grounding of the negotiated
  intent into operations belongs to downstream consumers of the artefact.
- Semantic agreement recorded by GENTILE is not governance authorisation.

## 5. Non-responsibilities

GENTILE must not:

- interpret the environment on its own authority (it negotiates meaning with
  participants);
- produce action candidates;
- create a candidate change by itself;
- authorise or execute anything;
- resolve safety-relevant ambiguity silently.

## Related

- [`intent-model.md`](intent-model.md)
- [`../../architecture/06-GENTILE.md`](../../architecture/06-GENTILE.md)
- [`../../toolchains/README.md`](../../toolchains/README.md)
