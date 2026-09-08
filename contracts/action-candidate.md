<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Contract — ActionCandidate

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define the working contract for the artefact through which
grounded, technically executable but not-yet-authorised operations are
proposed. `ActionCandidate` is the contract name for the *grounded action
candidate* defined in [`../GLOSSARY.md`](../GLOSSARY.md).

## Role

| Aspect | Value |
|---|---|
| Canonical producer | [GTL](../engines/GTL/README.md), or any conformant grounding engine |
| Consumers | Validation execution, governance adjudication (Evolution Control Plane), authorised execution via adapters |
| Answers | What bounded operation could realise the intended state? |
| Is not | A command, a permission, an executed action, an evolution transition, a baseline |

The near-invariant of this contract is:

> **ActionCandidate ≠ AuthorisedAction.**

Production of an `ActionCandidate` never confers permission to execute it.
Adjudication belongs to the governance boundary, outside every engine and
outside every toolchain
([`../architecture/03-evidence-and-authority.md`](../architecture/03-evidence-and-authority.md)).

## Content expectations

A conformant `ActionCandidate` should identify, following
[`../architecture/07-GTL.md`](../architecture/07-GTL.md):

- executor;
- transitive operation;
- direct object;
- operational context;
- preconditions, including any that rest on hypotheses, with their declared
  confidence ([`confidence-model.md`](confidence-model.md));
- operational limits and envelope;
- expected effects and postconditions;
- invariants that must hold;
- failure and abort behaviour;
- rollback or compensation provisions;
- closure-evidence criteria;
- effectivity;
- required authority (referenced, never claimed);
- a provenance envelope ([`provenance-envelope.md`](provenance-envelope.md)).

An illustrative, non-normative rendering is
[`../schemas/examples/gtl-action-candidate.example.yaml`](../schemas/examples/gtl-action-candidate.example.yaml).

## Downstream classification

After adjudication, a candidate follows one of two governed routes:

- **operational action** — executed under the active baseline within a
  delegated envelope; produces operational closure evidence; does not by
  itself open a new age;
- **candidate change** — enters the Evolution Plane and the evolutionary
  lifecycle; may, after authorised execution and closure verification, lead
  to a ratified successor baseline.

The classification is made against the active baseline and declared
governance policy, not by the producing engine
([`../toolchains/cognitive-action-chain.md`](../toolchains/cognitive-action-chain.md)).

## Related

- [`../engines/GTL/contract.md`](../engines/GTL/contract.md)
- [`../engines/GTL/action-candidate-model.md`](../engines/GTL/action-candidate-model.md)
- [`intent-artefact.md`](intent-artefact.md)
- [`semantic-context.md`](semantic-context.md)
