<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Scope and Positioning

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Thesis

> **AGES provides the structural foundations for a new generation of
> robotic and cyber-physical architectures in which autonomous machines
> are identified not only by what they currently execute, but by the
> governed continuity of what they have been permitted to become.**

And, stated more compactly:

> **Conventional robotics governs what a machine may do. AGES
> additionally governs what the machine may become.**

This statement must be read with care. Conventional robotics does not
lack runtime safety, configuration management, dynamic reconfiguration,
lifecycle management or adaptation; mature robotic practice includes
all of these. AGES-CPS addresses a different concern: the governed
identity of the complete robotic system across significant changes to
hardware, software, models, calibration, policies, capabilities and
authority. It asks not whether a machine can change, but whether the
succession of its ratified configurations is authorised, evidenced and
reconstructable.

## 2. Preserving the AGES core

AGES remains the general engineering paradigm. AGES-CPS is an
exploratory application profile. All core AGES concepts apply
unchanged: baseline, age, candidate change, evolution transition,
governed continuity, evidence, authority, effectivity, invariants, the
Operational Plane, the Evolution Plane, the Evolution Control Plane,
GENTILE and GTL ([`../../GLOSSARY.md`](../../GLOSSARY.md)).

The AGES lifecycle order is preserved without modification:

```text
Intent
→ GENTILE
→ Structured semantic artefact
→ Intent classification
→ Candidate change
→ GTL action candidate
→ Validation execution
→ Governance adjudication
→ Authorisation
→ Execution or deployment
→ Closure evidence
→ Resulting-state verification
→ Baseline ratification
→ New age
```

GTL produces action candidates before adjudication and ratification. A
baseline is never ratified before successful execution and closure
verification. Operational actions that do not change canonical
configuration identity do not create a new age.

## 3. Why robotics and CPS need this profile

### 3.1 Physical consequences

Changes to a robotic system may cause unsafe movement, collision,
excessive force, instability, sensor misinterpretation, actuator
saturation, hardware damage, violation of human safety zones, or
operation outside an authorised envelope. A robotic update cannot
always be treated as an ordinary software deployment: the consequences
of an ill-governed change are physical, not merely computational.

### 3.2 Incomplete configuration identity

A robotic baseline may include hardware assemblies, sensors and
actuators, computing modules, firmware, software packages, runtime
topology, control parameters, calibration data, perception and planning
models, learned policies, safety envelopes, permissions and delegated
authority, maps and world models, behaviour trees, and tools and
external services. A model checkpoint or software version alone is not
the identity of the complete machine.

### 3.3 Online adaptation

Robots may change through online learning, adaptive control, continual
learning, reinforcement learning, sensor recalibration, map updates,
policy updates, dynamic tool configuration, fleet learning and model
replacement. AGES-CPS must distinguish bounded runtime adaptation —
performed inside a delegated operational envelope
([`05-delegated-operational-envelopes.md`](05-delegated-operational-envelopes.md))
— from a baseline-relevant evolutionary change that requires evidence,
adjudication and ratification.

### 3.4 Reconstructability

The profile must support reconstruction of: the active baseline;
relevant hardware and calibration states; loaded models and parameters;
applicable policies and permissions; the authorised candidate; the
action actually executed; collected evidence; deviations and recovery
actions; and the reason a successor baseline was ratified or rejected.

> **Continuity that cannot be reconstructed is merely history, not
> governed continuity.**

## 4. Relationship with robotics middleware

ROS 2 and comparable middleware provide substantial, mature
capabilities: distributed communication, dynamic discovery, node
lifecycle management, parameters, runtime composition, simulation,
telemetry and implementation-specific deployment workflows. AGES-CPS
does not supersede these capabilities, nor does it supersede robotics
standards.

> **ROS 2 and comparable middleware organise communication, composition
> and runtime execution. AGES-CPS models how the governed identity of
> the complete robotic system persists across authorised changes.**

| Concern | Conventional robotics | AGES-CPS |
|---|---|---|
| System identity | Hardware, packages, nodes, releases and parameters | Complete baseline plus governed transition history |
| Adaptation | Implementation-specific runtime or learning mechanisms | Candidate changes bounded by invariants, evidence, effectivity and authority |
| Safety | Runtime controllers, guards and monitors | Runtime safety plus governance of changes to the safety-relevant configuration |
| Intent to action | Planners, scripts, behaviour trees and API calls | GENTILE → GTL → validation → adjudication |
| Post-change identity | Updated artefacts or runtime state | Ratified successor baseline |
| Recovery | Restart, fallback or implementation-specific rollback | Rollback, compensation, safe-state and recovery-baseline semantics |
| Auditability | Logs and telemetry | Reconstructable chain from intent to resulting baseline |

Integration details:
[`11-middleware-integration.md`](11-middleware-integration.md).

## 5. Safety boundary

AGES-CPS does not replace runtime safety mechanisms. The Evolution
Control Plane does not replace safety controllers. Governance failure
must not disable hard safety limits. Emergency stop and safe-state
functions remain independently available. GENTILE and generative GTL
components cannot bypass safety enforcement. Changes to safety
functions require elevated evidence and authority.

> **Evolution governance determines whether a safety-relevant
> configuration may change; runtime safety mechanisms enforce the
> authorised physical envelope during operation.**
