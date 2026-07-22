<!-- ages:authored — informative. This document does not define conformance requirements. -->

# AGES-CPS — AGES Profile for Cyber-Physical and Robotic Systems

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

> **AGES provides the structural foundations for a new generation of
> robotic and cyber-physical architectures in which autonomous machines
> are identified not only by what they currently execute, but by the
> governed continuity of what they have been permitted to become.**

AGES-CPS is a proposed, exploratory application profile of
[AGES](../../README.md) for robotics and cyber-physical systems. AGES
remains the general engineering paradigm; robotics is one compelling
practical domain among others, not the exclusive AGES domain.

## What AGES-CPS is not

AGES-CPS is not a replacement for AGES, a separate root paradigm, a
robotics middleware, a real-time operating system, a controller, a
motion planner, a perception framework, a replacement for ROS 2, or a
safety or certification standard.

## Contents

| Document | Topic |
|---|---|
| [`01-scope-and-positioning.md`](01-scope-and-positioning.md) | Scope, thesis, relationship with robotics middleware |
| [`02-robotic-system-identity.md`](02-robotic-system-identity.md) | Conceptual model of governed robotic identity |
| [`03-hardware-software-co-baselines.md`](03-hardware-software-co-baselines.md) | Hardware–software co-baselines and baseline impact |
| [`04-multi-rate-autonomy.md`](04-multi-rate-autonomy.md) | Control, operation, adaptation and governance timescales |
| [`05-delegated-operational-envelopes.md`](05-delegated-operational-envelopes.md) | Bounded runtime authority |
| [`06-gentile-and-gtl-for-robotics.md`](06-gentile-and-gtl-for-robotics.md) | GENTILE and GTL applied to robotic intent and action |
| [`07-physical-invariants.md`](07-physical-invariants.md) | Physical invariants across transitions |
| [`08-irreversibility-and-recovery.md`](08-irreversibility-and-recovery.md) | Rollback, compensation, safe state, recovery baseline |
| [`09-digital-physical-closure-evidence.md`](09-digital-physical-closure-evidence.md) | Evidence connecting authorisation, execution and physical result |
| [`10-fleet-effectivity.md`](10-fleet-effectivity.md) | Fleet, cohort and instance effectivity |
| [`11-middleware-integration.md`](11-middleware-integration.md) | Integration with ROS 2 and comparable middleware |

## Related material

Models:
[`../../models/robotic-identity-model.md`](../../models/robotic-identity-model.md) ·
[`../../models/hardware-software-co-baseline-model.md`](../../models/hardware-software-co-baseline-model.md) ·
[`../../models/multi-rate-autonomy-model.md`](../../models/multi-rate-autonomy-model.md).

Worked examples:
[`../../examples/robotic-operational-inspection.md`](../../examples/robotic-operational-inspection.md) ·
[`../../examples/robotic-calibration-evolution.md`](../../examples/robotic-calibration-evolution.md) ·
[`../../examples/bounded-cyber-physical-action.md`](../../examples/bounded-cyber-physical-action.md) ·
[`../../examples/fleet-model-deployment.md`](../../examples/fleet-model-deployment.md).

Draft RFCs:
[`../../rfcs/0012-ages-cps-profile.md`](../../rfcs/0012-ages-cps-profile.md) ·
[`../../rfcs/0013-robotic-baseline-semantics.md`](../../rfcs/0013-robotic-baseline-semantics.md) ·
[`../../rfcs/0014-multi-rate-autonomy.md`](../../rfcs/0014-multi-rate-autonomy.md) ·
[`../../rfcs/0015-physical-irreversibility.md`](../../rfcs/0015-physical-irreversibility.md) ·
[`../../rfcs/0016-digital-physical-closure-evidence.md`](../../rfcs/0016-digital-physical-closure-evidence.md) ·
[`../../rfcs/0017-fleet-effectivity.md`](../../rfcs/0017-fleet-effectivity.md).
