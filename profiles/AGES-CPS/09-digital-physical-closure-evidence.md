<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Digital–Physical Closure Evidence

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Definition

> **Digital–physical closure evidence** — evidence connecting the
> authorised action specification, recorded execution and observed
> physical result.

Possible evidence includes: actuator feedback, sensor measurements,
pose estimates, force and torque data, energy measurements, deployed
artefact identifiers, hardware identity, calibration verification,
inspection records, safety-zone history, operator attestation,
digital-twin comparison and post-action tests. An illustrative,
non-normative schema is provided in
[`../../schemas/examples/physical-closure-evidence.example.yaml`](../../schemas/examples/physical-closure-evidence.example.yaml).

## 2. What closure evidence should establish

1. whether the authorised action was executed;
2. whether execution remained inside the authorised envelope;
3. whether the target state was achieved;
4. whether invariants remained true;
5. whether deviations occurred;
6. whether fallback or compensation was activated;
7. whether the resulting configuration matches the candidate baseline;
8. whether ratification criteria are satisfied.

## 3. Sufficiency

Telemetry volume alone is not evidentiary sufficiency. Evidence is
sufficient when it answers the questions above with the confidence the
governing authority requires — a small set of well-chosen measurements
and attestations may outweigh unbounded logs. What constitutes
sufficient physical closure evidence, and what qualifies digital-twin
evidence, are open research questions
([`../../research/open-questions.md`](../../research/open-questions.md)).

## 4. Position in the lifecycle

Closure evidence follows execution and precedes resulting-state
verification and ratification. A baseline is never ratified before
successful execution and closure verification.

## 5. Related material

[`../../schemas/examples/closure-evidence.example.yaml`](../../schemas/examples/closure-evidence.example.yaml) ·
[`08-irreversibility-and-recovery.md`](08-irreversibility-and-recovery.md) ·
[`../../rfcs/0016-digital-physical-closure-evidence.md`](../../rfcs/0016-digital-physical-closure-evidence.md).
