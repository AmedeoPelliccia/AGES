<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Middleware Integration

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Position

ROS 2 and comparable robotics middleware provide distributed
communication, dynamic discovery, node lifecycle management,
parameters, runtime composition, simulation, telemetry and
implementation-specific deployment workflows. These are substantial,
mature capabilities that AGES-CPS neither replaces nor supersedes.

> **ROS 2 and comparable middleware organise communication, composition
> and runtime execution. AGES-CPS models how the governed identity of
> the complete robotic system persists across authorised changes.**

## 2. Illustrative mapping sketches

The following correspondences are exploratory sketches, not a
conformance mapping:

| Middleware concept | Possible AGES-CPS relation |
|---|---|
| Node lifecycle states | Runtime composition under the active baseline; lifecycle transitions are operational, not evolutionary |
| Parameters | Operational within declared adaptation ranges; range or semantics changes may be candidate changes |
| Launch and composition descriptions | Part of the runtime-topology portion of a co-baseline |
| Package releases | Configuration items referenced by a baseline, not the baseline itself |
| Telemetry and logging | Raw material for — but not identical to — closure evidence |
| Deployment tooling | Execution mechanics for an authorised candidate; not authorisation |

How ROS 2 lifecycle concepts should map to AGES objects, and how
safety-certified and non-certified components should coexist, are open
research questions
([`../../research/open-questions.md`](../../research/open-questions.md)).

## 3. Adapters

GTL candidates are translated through adapters into
middleware-executable forms — behaviour trees, task graphs,
motion-planning requests, deployment procedures, configuration deltas,
service sequences, controller updates or safe-state procedures
([`06-gentile-and-gtl-for-robotics.md`](06-gentile-and-gtl-for-robotics.md)).
Adapters are implementation concerns; the profile constrains what an
adapter receives (a bounded, authorised candidate), not how it is
implemented.

## 4. Boundaries

AGES-CPS does not claim ROS endorsement, universal platform
compatibility or implementation completeness, and does not claim to
supersede robotics standards.
