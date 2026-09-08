<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Contract — Confidence Model

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define the working contract for how confidence, uncertainty,
ambiguity and competing hypotheses are represented and preserved across
engine boundaries.

## Role

| Aspect | Value |
|---|---|
| Producers | Every functional engine, wherever its output is uncertain, ambiguous or hypothetical |
| Consumers | Every artefact consumer; validation and adjudication services |
| Answers | How certain is this element, and what would revise it? |
| Is not | A prescribed probability calculus, a risk model, an adjudication rule |

The governing rule is:

> **Uncertainty must survive the handoff.**

An engine must not convert uncertain interpretation, partial agreement or
hypothetical grounding into false certainty, and a consumer must not strip
declared uncertainty when reusing an element.

## Content expectations

Wherever an artefact element is uncertain, the artefact should expose:

- a confidence value or another declared uncertainty measure;
- the semantic level of the element — the contract distinguishes at least:

```text
observation ≠ inference ≠ hypothesis ≠ assertion
```

- competing hypotheses not yet eliminated, including an explicit *unknown*
  hypothesis where relevant;
- supporting and contradicting observations
  ([`provenance-envelope.md`](provenance-envelope.md));
- the conditions under which the element would be revised.

## Consumption rules

- **Inference is not fact.** A hypothesis consumed from a
  [`SemanticContext`](semantic-context.md) must not become an unconditional
  precondition of an [`ActionCandidate`](action-candidate.md); the dependency
  and its confidence must be recorded and verified before execution.
- Ambiguity that could materially affect safety, authority, effectivity or
  identity must be propagated — for example into
  [`IntentArtefact`](intent-artefact.md) negotiation — rather than resolved
  silently.
- Promotion of a hypothesis to an assertion is a reviewable act with a
  declared basis, not an automatic consequence of downstream convenience.

## Related

- [`../architecture/12-GENIUSS.md`](../architecture/12-GENIUSS.md)
- [`../architecture/06-GENTILE.md`](../architecture/06-GENTILE.md)
- [`../architecture/07-GTL.md`](../architecture/07-GTL.md)
