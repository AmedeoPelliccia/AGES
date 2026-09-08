<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Contract — Provenance Envelope

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define the working contract for the provenance information that
every engine artefact must carry. The envelope is what makes engine outputs
usable within an AGES-governed system: without reconstructable provenance, an
artefact cannot participate in evidence, adjudication or baseline identity
([`../architecture/05-identity-and-provenance.md`](../architecture/05-identity-and-provenance.md)).

## Role

| Aspect | Value |
|---|---|
| Producers | Every functional engine, for every artefact it emits |
| Consumers | Every artefact consumer; evidence, ledger and reconstruction services |
| Answers | Where did this artefact come from, and could it be reconstructed? |
| Is not | Evidence adjudication, integrity enforcement, an audit verdict |

## Content expectations

A conformant provenance envelope should record:

- the identity and version of the producing engine or transformation;
- the artefact class ([`semantic-context.md`](semantic-context.md),
  [`intent-artefact.md`](intent-artefact.md),
  [`action-candidate.md`](action-candidate.md) or another declared class);
- references to every consumed input artefact and source observation;
- timestamps and temporal context;
- the baseline context under which the artefact was produced;
- the participants — human, machine or composite — involved in producing it;
- integrity information sufficient to detect alteration.

The conceptual chain is:

```text
artefact
    ↓ produced_by
engine (identity · version · configuration)
    ↓ consumed
input artefacts and observations
    ↓ originated_from
sources
```

## Consumption rules

- Consumers must preserve the envelope of any element they reuse, extending
  rather than replacing it.
- A downstream decision must be able, at least conceptually, to answer: *why
  does the system hold this artefact, and from what was it derived?*
- Loss of provenance is a declared failure condition, not a silent
  degradation.

## Related

- [`../architecture/03-evidence-and-authority.md`](../architecture/03-evidence-and-authority.md)
- [`../engines/README.md`](../engines/README.md)
- [`confidence-model.md`](confidence-model.md)
