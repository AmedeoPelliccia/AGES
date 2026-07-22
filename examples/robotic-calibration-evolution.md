<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — Robotic Calibration Evolution

**Status:** Exploratory application profile · **Document class:** Example · **Repository:** AGES

A non-normative AGES-CPS example of an **evolutionary** change: sensor
recalibration that produces a successor baseline
([`../profiles/AGES-CPS/03-hardware-software-co-baselines.md`](../profiles/AGES-CPS/03-hardware-software-co-baselines.md)).

**Trigger.** Routine monitoring detects localisation drift on
`robot:amr-014` consistent with front-lidar calibration drift. Because
lidar calibration is declared baseline-controlled (it is
safety-relevant), the recalibration is classified as a **candidate
change**, not a routine parameter tweak.

**Candidate and evidence.** The Evolution Plane generates a
recalibration candidate: new extrinsic calibration for
`sensor:lidar-front`, validated against reference targets in a
controlled bay, with before/after residual analysis, invariant
assessment (human safety zones unaffected in enforcement, improved in
accuracy) and a declared rollback: the previous calibration reference
remains restorable.

**Effectivity.** Deployment is **instance-specific**: the candidate
applies to `robot:amr-014` only, since calibration is a property of the
individual sensor installation, not of the fleet.

**Authorisation and execution.** The Evolution Control Plane
adjudicates the evidence and authorises deployment during a maintenance
window. The new calibration is applied and verification runs are
executed.

**Closure and ratification.** Closure evidence establishes that the
authorised procedure was executed, residuals fall within acceptance
criteria, invariants held and the resulting configuration matches the
candidate. Only then is the successor baseline ratified, opening a new
age for this instance
([`../schemas/examples/robotic-baseline.example.yaml`](../schemas/examples/robotic-baseline.example.yaml)).

**Contrast.** Had the drift correction remained inside the delegated
adaptation range declared in the operational envelope, it would have
been an operational adaptation with no baseline impact. The boundary is
set by declared baseline control, not by the size of the number that
changed.

**Related.**
[`robotic-operational-inspection.md`](robotic-operational-inspection.md) ·
[`../rfcs/0013-robotic-baseline-semantics.md`](../rfcs/0013-robotic-baseline-semantics.md)
