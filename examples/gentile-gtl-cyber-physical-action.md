<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — Cyber-Physical Bounded Action through GTL

**Status:** Exploratory · **Document class:** Example · **Repository:** AGES
A non-destructive, safety-oriented example: **controlled valve
positioning in a test environment**. It illustrates the full GTL binding
— executor, direct object, preconditions, limits, expected state, abort
rules and closure evidence ([`../architecture/07-GTL.md`](../architecture/07-GTL.md)).

A semantic artefact (negotiated through
[GENTILE](../architecture/06-GENTILE.md)) requests verification of a
cooling-loop isolation valve's travel behaviour in the test rig. GTL
grounds it into a bounded action candidate:

| GTL element | Illustrative value |
|---|---|
| Executor | `controller:test-rig-plc-02`, under delegated test authority |
| Transitive operation | `position` |
| Direct object | `asset:valve-CV-118` (cooling-loop isolation valve, test rig) |
| Operational context | test environment, rig in commissioning mode, loop drained |
| Preconditions | rig isolated from plant; loop pressure zero; test permit active |
| Limits (operational envelope) | travel between 20% and 60% open; actuation rate ≤ 5%/s; single stroke cycle; test window 2 h |
| Expected effects | valve position reaches 60% ± 2%, then returns to 20% ± 2%; travel time within specified band |
| Abort conditions | position feedback loss > 1 s; torque above threshold; any plant-side pressure signal |
| Safe state | actuator de-energised, valve held at last position, rig alarm raised |
| Compensation | manual repositioning by commissioning technician |
| Closure evidence | position and torque trace, timestamped feedback log, technician attestation |

The candidate is validated against the rig safety policy, adjudicated
and authorised before the controller may act. Execution stays inside
the declared envelope; the recorded traces constitute closure evidence
that the expected state was achieved. As an operational test action, it
creates **no new baseline**; had the action been part of a candidate
change (for example, commissioning a modified control loop), closure
evidence would precede any ratification.

Weapon-related, harmful or unsafe operational examples are deliberately
avoided throughout AGES.

**Related.**
[`cyber-physical-system.md`](cyber-physical-system.md) ·
[`../schemas/examples/gtl-action-candidate.example.yaml`](../schemas/examples/gtl-action-candidate.example.yaml) ·
[`../architecture/08-gentile-gtl-integration.md`](../architecture/08-gentile-gtl-integration.md)
