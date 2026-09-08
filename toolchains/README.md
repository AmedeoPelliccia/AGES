<!-- ages:authored — informative. This document does not define conformance requirements. -->

# toolchains/ — Engine Compositions

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Describe how the independent functional engines of
[`../engines/`](../engines/README.md) may be composed. This directory holds
**compositions**; [`../engines/`](../engines/README.md) holds **components**;
[`../contracts/`](../contracts/README.md) holds the artefacts through which
they connect.

> **A toolchain is a composition of engines. It is defined by the engines'
> contracts — never the other way round.**

A composition such as

$$
\mathcal{T} = F_T \circ F_I \circ F_G
$$

is **one possible composition**, not the definition of the engines. No
toolchain is mandatory: conformance to AGES requires neither the engines nor
any composition of them
([`../engines/README.md`](../engines/README.md), section 4).

## Composition catalogue

Because the engines couple only through contracts, and cross-engine inputs
are optional, the following compositions are all legitimate:

| Composition | Chain | Typical use |
|---|---|---|
| Full cognitive-action chain | GENIUSS → GENTILE → GTL | Heterogeneous input, negotiated intent, grounded candidate ([`cognitive-action-chain.md`](cognitive-action-chain.md)) |
| Language-only chain | GENTILE → GTL | Intent negotiation where the necessary context is already structured |
| Perception-action chain | GENIUSS → GTL | Grounded response to interpreted observations where no linguistic intent needs negotiation |
| Understanding only | GENIUSS | Interpretation for monitoring, evidence or situational awareness |
| Intent only | GENTILE | Negotiated artefacts for requirements, records or governance requests |
| Transitive grounding only | structured artefact → GTL | Grounding of an already-structured artefact from any conformant producer |

Example of the perception-action chain:

```text
sensor anomaly
    ↓
GENIUSS
    ↓
"hydraulic pressure degradation"        (SemanticContext)
    ↓
GTL
    ↓
candidate: isolate circuit B            (ActionCandidate)
```

No composition changes what the engines are; a toolchain adds no capability
that its engines do not have, and carries no authority whatsoever.

## Toolchains and governance

Every toolchain terminates at the governance boundary. Whatever the
composition, its terminal artefact is at most an
[`ActionCandidate`](../contracts/action-candidate.md) — never an authorised
action, never a transition, never a baseline. The Evolution Control Plane is
not part of any toolchain: it is the boundary that prevents a toolchain from
authorising itself ([`cognitive-action-chain.md`](cognitive-action-chain.md)).

## Contents

| Document | Purpose |
|---|---|
| [`cognitive-action-chain.md`](cognitive-action-chain.md) | The canonical full composition and its governed outputs |

## Related

- [`../engines/README.md`](../engines/README.md)
- [`../contracts/README.md`](../contracts/README.md)
- [`../architecture/08-gentile-gtl-integration.md`](../architecture/08-gentile-gtl-integration.md)
- [`../profiles/AGES-CPS/06-functional-engine-toolchain-for-robotics.md`](../profiles/AGES-CPS/06-functional-engine-toolchain-for-robotics.md) — a profile applying the toolchain
