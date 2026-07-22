<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — Robotic Operational Inspection

**Status:** Exploratory application profile · **Document class:** Example · **Repository:** AGES

A non-normative AGES-CPS example of a purely **operational** action: an
inspection that produces closure evidence and changes no baseline
([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)).

**Intent and negotiation.** A facilities engineer asks an autonomous
mobile robot to "check the racking in aisle four". Through
[GENTILE](../architecture/06-GENTILE.md) the request is clarified: which
racking bays, what "check" means (visual survey of upright and beam
condition), required image coverage, standoff distance, aisle occupancy
constraints and acceptance criteria (complete coverage at declared
resolution). The result is a structured semantic artefact classified as
operational intent.

**Grounded candidate.** [GTL](../architecture/07-GTL.md) produces a
bounded inspection action: executor `robot:amr-014`, verb `inspect`,
direct object `asset:racking-aisle-4`, target state
`condition-survey-complete`, with preconditions (aisle open, battery
reserve), limits (speed, standoff, duration), abort conditions (human
entry into stop zone), safe state (controlled stop) and closure-evidence
requirements (image set, pose log, coverage report).

**Validation and authorisation.** The candidate is validated against
the delegated operational envelope
([`../schemas/examples/delegated-operational-envelope.example.yaml`](../schemas/examples/delegated-operational-envelope.example.yaml)):
inspection is a permitted task class in the permitted zone, so the
action proceeds under prior delegated authority.

**Execution and closure.** The robot performs the survey inside the
envelope. Digital–physical closure evidence
([`../profiles/AGES-CPS/09-digital-physical-closure-evidence.md`](../profiles/AGES-CPS/09-digital-physical-closure-evidence.md))
records the executed trajectory, coverage achieved, invariants held and
absence of deviations.

**Outcome.** The action changed no baseline-controlled configuration:
**no candidate change, no new age**. The active baseline remains
canonical; the evidence is retained as operational record.

**Related.**
[`robotic-calibration-evolution.md`](robotic-calibration-evolution.md) ·
[`../schemas/examples/robotic-action-candidate.example.yaml`](../schemas/examples/robotic-action-candidate.example.yaml)
