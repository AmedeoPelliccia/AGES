<!-- ages:authored — informative. This document does not define conformance requirements. -->

# contracts/ — Engine Contract Layer

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define the semantically typed contract artefacts through which
the AGES functional engines ([`../engines/`](../engines/README.md)) compose.
Engines do not integrate through mutual dependencies; they integrate through
contract artefacts.

The governing principle is:

> **Loose coupling + strong semantic contracts.**

No engine may require knowledge of another engine's internal implementation.
An engine consumes and produces artefacts conforming to the contracts in this
directory, and nothing more:

```text
          SemanticContext
GENIUSS --------------------►

                  IntentArtefact
          GENTILE --------------------►

                            ActionCandidate
                    GTL --------------------►
```

This is what allows the engines to remain independent, individually
replaceable and freely composable into toolchains
([`../toolchains/`](../toolchains/README.md)), while preserving the AGES
concerns of interoperability, provenance and reconstructability.

## Contracts

| Contract | Produced by | Consumed by |
|---|---|---|
| [`semantic-context.md`](semantic-context.md) | GENIUSS, or any conformant interpreter | GENTILE (optional), GTL (optional), evidence services |
| [`intent-artefact.md`](intent-artefact.md) | GENTILE, or any conformant intent engine | Intent classification, GTL, governance services |
| [`action-candidate.md`](action-candidate.md) | GTL, or any conformant grounding engine | Validation, adjudication, authorised execution |
| [`provenance-envelope.md`](provenance-envelope.md) | Every engine, for every artefact | Every consumer; evidence and ledger services |
| [`confidence-model.md`](confidence-model.md) | Every engine, wherever uncertainty exists | Every consumer; adjudication |

## Contract properties

Every contract artefact should be:

- **semantically typed** — its class is explicit, not inferred;
- **inspectable** — reviewable by humans and machines without access to the
  producing engine;
- **provenance-bound** — wrapped in a provenance envelope
  ([`provenance-envelope.md`](provenance-envelope.md));
- **uncertainty-preserving** — declared confidence, ambiguity and competing
  hypotheses survive the handoff
  ([`confidence-model.md`](confidence-model.md));
- **authority-free** — no contract artefact carries, implies or confers
  authorisation.

## What this layer is not

The contract layer is not a wire format, an API specification, a schema
registry or a normative standard. Exploratory, non-normative structural
renderings are provided in [`../schemas/`](../schemas/README.md). Names such
as `SemanticContext`, `IntentArtefact` and `ActionCandidate` are working
contract names; the corresponding working vocabulary is defined in
[`../GLOSSARY.md`](../GLOSSARY.md).

## Related

- [`../engines/README.md`](../engines/README.md)
- [`../toolchains/README.md`](../toolchains/README.md)
- [`../architecture/05-identity-and-provenance.md`](../architecture/05-identity-and-provenance.md)
- [`../architecture/08-gentile-gtl-integration.md`](../architecture/08-gentile-gtl-integration.md)
