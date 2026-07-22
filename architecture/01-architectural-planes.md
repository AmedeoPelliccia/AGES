<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Architectural Planes

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES
**Purpose.** Decompose an artificial evolutive system into three
coordinated planes.

$$
\mathrm{AGES} := \langle\, O,\ E,\ C_E \,\rangle
$$

An architectural decomposition — coordinated planes, not an arithmetic
sum, and not a completed mathematical theory.

| Plane | Answers | Possible contents |
|---|---|---|
| Operational (O) | What does the system do under its current baseline? | Runtime components, models and agents, interfaces, memory and knowledge, tools, infrastructure, actuators, operational policies |
| Evolution (E) | What could the system become? | Observation, candidate generation, training, tuning, assembly, simulation, validation execution, test execution, deployment mechanics, post-deployment monitoring |
| Evolution Control (C_E) | What is the system permitted to become? | Configuration identification, scope and effectivity control, policy evaluation, authority evaluation, evidence adjudication, risk adjudication, transition authorisation, baseline ratification, ledger management, rollback control, conformance assessment |

The control plane is not part of the runtime datapath unless a specific
implementation requires it.

**Execution versus adjudication.** The Evolution Plane may execute tests,
run validation suites, collect measurements, produce reports and operate
deployment infrastructure. The Evolution Control Plane must interpret the
resulting evidence, compare it with declared policy, assess authority and
effectivity, and issue or record the governance verdict.

> The subsystem that executes validation does not automatically own the
> authority to adjudicate its sufficiency.

Rollback remains governed: monitoring signals may trigger a new
adjudication, an emergency policy path, a rollback previously authorised
by policy, suspension of the current baseline, or transition to a
recovery baseline. An automatic rollback may be operationally immediate
while still being constitutionally governed through prior authorisation.

**Related.**
[`02-state-and-transition-model.md`](02-state-and-transition-model.md) ·
[`../models/minimal-conceptual-model.md`](../models/minimal-conceptual-model.md)
