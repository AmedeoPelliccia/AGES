<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — Fleet Model Deployment

**Status:** Exploratory application profile · **Document class:** Example · **Repository:** AGES

A non-normative AGES-CPS example of a **perception-model update**
deployed across a fleet cohort with staged ratification
([`../profiles/AGES-CPS/10-fleet-effectivity.md`](../profiles/AGES-CPS/10-fleet-effectivity.md)).

**Trigger.** Evidence aggregated across a warehouse fleet indicates
degraded pallet-detection performance under a new packaging type. Fleet
learning produces an improved perception-model candidate — but fleet
learning does not imply fleet-wide deployment authority.

**Candidate.** The Evolution Plane packages the model as a candidate
change with declared rollback: the predecessor model remains deployable
and the switch is reversible at the configuration level.

**Validation.** The candidate is evaluated in simulation and then in
**shadow mode** on selected robots: the new model runs alongside the
active model without influencing behaviour, and its outputs are
compared against the active model and against ground truth. Shadow-mode
results form part of the evidence, alongside digital-twin comparison.

**Effectivity.** Adjudication grants **cohort-specific** effectivity:
robots of hardware revision C in facility A, whose cameras and
calibration match the validation conditions. Other cohorts differ in
sensors and environment; evidence from one cohort does not
automatically validate another.

**Staged ratification.** Deployment proceeds in stages: a small cohort
subset operates the model under a probation window; closure evidence
(detection metrics, invariant checks, absence of safety-zone events) is
adjudicated; only then is the cohort baseline ratified and the
effectivity widened stage by stage. At every stage, ratification
follows execution and closure verification — never precedes it.

**Rollback.** Because the change is configuration-reversible, any stage
may be rolled back to the predecessor model without physical
compensation.

**Related.**
[`robotic-calibration-evolution.md`](robotic-calibration-evolution.md) ·
[`../rfcs/0017-fleet-effectivity.md`](../rfcs/0017-fleet-effectivity.md) ·
[`../schemas/examples/effectivity.example.yaml`](../schemas/examples/effectivity.example.yaml)
