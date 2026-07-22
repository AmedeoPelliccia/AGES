<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Delegated Operational Envelopes

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Definition

> **Delegated Operational Envelope** — the bounded set of actions,
> adaptations and runtime decisions that the Operational Plane may
> perform under prior authority without requesting a new evolutionary
> authorisation for every decision.

The envelope is the mechanism through which evolution governance
delegates bounded runtime freedom. It is declared, authorised and
recorded in advance; the Operational Plane then operates freely within
it.

## 2. Possible limits

Envelope limits may include, illustratively: position, velocity,
acceleration, force, torque, energy, pressure, temperature, latency,
model confidence, human proximity, geographic zone, task class,
environmental conditions, authority duration and permitted fallback
actions.

An illustrative, non-normative schema is provided in
[`../../schemas/examples/delegated-operational-envelope.example.yaml`](../../schemas/examples/delegated-operational-envelope.example.yaml).

## 3. Envelope semantics

* An action inside the envelope does not automatically create a new
  baseline.
* Bounded runtime adaptation inside the envelope — for example
  authorised parameter adaptation within declared ranges — remains an
  operational matter.
* A change to the envelope itself may require evolution governance: the
  envelope is part of the authority configuration of the baseline.
* Envelope violation triggers runtime safety behaviour and produces
  evidence for governance review; it is not resolved by the Evolution
  Control Plane in real time.

## 4. Related material

[`04-multi-rate-autonomy.md`](04-multi-rate-autonomy.md) ·
[`06-gentile-and-gtl-for-robotics.md`](06-gentile-and-gtl-for-robotics.md) ·
[`../../architecture/04-effectivity.md`](../../architecture/04-effectivity.md).
