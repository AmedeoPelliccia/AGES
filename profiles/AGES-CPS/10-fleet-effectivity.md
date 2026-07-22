<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Fleet Effectivity

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Effectivity dimensions

AGES effectivity
([`../../architecture/04-effectivity.md`](../../architecture/04-effectivity.md))
applies naturally to robotic fleets. AGES-CPS supports effectivity for:
individual robot, hardware revision, production batch, facility,
environment, customer, jurisdiction, task class, fleet cohort and the
complete fleet.

## 2. Candidate and baseline granularity

Distinguish:

* **global candidate** — proposed for every instance;
* **fleet candidate** — proposed for a declared fleet;
* **cohort baseline** — canonical for a declared cohort;
* **instance baseline** — canonical for one machine;
* **temporary experimental effectivity** — bounded trial applicability,
  time-limited and revocable.

## 3. Fleet learning is not fleet authority

Fleet learning does not imply fleet-wide deployment authority. Evidence
gathered across a fleet may support a candidate, but authorisation and
effectivity remain governance decisions. Evidence must consider
differences in hardware, sensors, calibration, environment, local
regulation, degradation and operational context: a candidate validated
on one cohort is not thereby validated for another.

## 4. Related material

[`../../examples/fleet-model-deployment.md`](../../examples/fleet-model-deployment.md) ·
[`../../rfcs/0017-fleet-effectivity.md`](../../rfcs/0017-fleet-effectivity.md).
