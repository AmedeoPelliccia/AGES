<!-- ages:authored — informative. This document does not define conformance requirements. -->

# engines/ — Functional Engines

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Catalogue the proposed AGES functional engines — GENIUSS,
GENTILE and GTL — as independent, composable functional units with explicit
contracts. This directory holds tooling **of the AGES system model**; it is
deliberately distinct from [`../tools/`](../tools/README.md), which holds
tooling **of this repository** (the deterministic scaffold generator).

The structural distinction maintained across this repository is:

> **Engine ≠ Toolchain ≠ AGES.**

- An **engine** is an autonomous functional unit with its own contract.
- A **toolchain** is a composition of engines
  ([`../toolchains/`](../toolchains/README.md)).
- **AGES** governs the identity, evolution and authority of the system that
  uses those engines; it is defined by neither.

## 1. The three engines

| Engine | Input | Output contract | Core question |
|---|---|---|---|
| [`GENIUSS/`](GENIUSS/README.md) | Contextual observations | [`SemanticContext`](../contracts/semantic-context.md) | What does this input mean in the current context? |
| [`GENTILE/`](GENTILE/README.md) | Linguistic interaction + optional semantic context | [`IntentArtefact`](../contracts/intent-artefact.md) | What is intended? |
| [`GTL/`](GTL/README.md) | Structured semantic or intent artefact + optional grounded context | [`ActionCandidate`](../contracts/action-candidate.md) | What bounded operation could realise it? |

Each engine directory contains:

```text
README.md      identity and scope of the engine
contract.md    the engine's input/output contract and independence clauses
<model>.md     the engine's principal artefact model
```

The full architectural treatments remain in
[`../architecture/12-GENIUSS.md`](../architecture/12-GENIUSS.md),
[`../architecture/06-GENTILE.md`](../architecture/06-GENTILE.md) and
[`../architecture/07-GTL.md`](../architecture/07-GTL.md).

## 2. Independence

The engines are mutually independent:

$$
\mathrm{GENIUSS} \neq \mathrm{GENTILE} \neq \mathrm{GTL}
$$

and none contains another:

$$
\mathrm{GENIUSS} \not\supset \mathrm{GENTILE} \not\supset \mathrm{GTL}
$$

No engine may know the internal implementation of another. Engines know only
the semantically typed contracts of [`../contracts/`](../contracts/README.md).
Cross-engine inputs are therefore **optional by contract**: GENTILE does not
structurally depend on GENIUSS, and GTL does not structurally depend on
either — each consumes conformant artefacts from any conformant producer.

This is what makes the engines general-purpose and individually replaceable,
and what allows partial compositions such as GENIUSS → GTL (no linguistic
intent to negotiate) or GENTILE → GTL (context already structured)
([`../toolchains/README.md`](../toolchains/README.md)).

## 3. Position within the AGES planes

The engines are primarily capabilities of the **Operational Plane**: they let
the current, authorised system understand inputs, negotiate intent and
produce operative candidates. Producing an
[`ActionCandidate`](../contracts/action-candidate.md) is operational
behaviour, not evolution.

A candidate whose effect would modify baseline-controlled configuration is
classified as a **candidate change** and becomes input to the **Evolution
Plane**; adjudication always belongs to the **Evolution Control Plane**
([`../architecture/01-architectural-planes.md`](../architecture/01-architectural-planes.md)).
The governance boundary is not part of any engine: it is precisely what
prevents a toolchain from authorising itself.

## 4. Engines and AGES conformance

The engines are optional with respect to the paradigm:

> **Conformance to AGES MUST NOT require GENIUSS, GENTILE or GTL.**

AGES defines the paradigm under which functional engines may operate and
evolve. GENIUSS, GENTILE and GTL are independent, composable functional
engines that may form an AGES-compatible cognitive-action toolchain — but an
industrial plant, an aerospace system or an evolutive controller may conform
to AGES while using none of the three. Conversely, application profiles such
as [`../profiles/AGES-CPS/`](../profiles/AGES-CPS/README.md) **apply** the
engines to a domain; they do not define them.

## 5. Shared engine boundaries

Whatever their implementation, all three engines observe the same
boundaries:

- an engine produces artefacts; it does not execute them;
- an engine is not an authority: no output carries authorisation;
- an engine must preserve provenance
  ([`../contracts/provenance-envelope.md`](../contracts/provenance-envelope.md));
- an engine must preserve declared uncertainty
  ([`../contracts/confidence-model.md`](../contracts/confidence-model.md));
- a change to an engine's own configuration is a candidate change governed by
  the Evolution Control Plane, like any other.

## Related

- [`../contracts/README.md`](../contracts/README.md)
- [`../toolchains/README.md`](../toolchains/README.md)
- [`../architecture/08-gentile-gtl-integration.md`](../architecture/08-gentile-gtl-integration.md)
- [`../rfcs/0018-geniuss.md`](../rfcs/0018-geniuss.md) ·
  [`../rfcs/0009-gentile.md`](../rfcs/0009-gentile.md) ·
  [`../rfcs/0010-gtl.md`](../rfcs/0010-gtl.md)
