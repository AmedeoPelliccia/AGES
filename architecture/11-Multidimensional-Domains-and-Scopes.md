<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Multidimensional Domains and Evolutionary Scopes

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define the multidimensional classification of artificial-system
evolution within AGES and distinguish architectural planes from evolutionary
scopes, mutability classes, effectivity, authority, risk and temporal
coordination.

This document introduces three principal evolutionary scopes:

- **Lineage Evolution**
- **Situated Evolution**
- **Collective Evolution**

These scopes describe **where system identity is evolving**. They are
orthogonal to the AGES architectural planes, which describe **which
architectural responsibility is acting**.

## 1. Core distinction

AGES already defines three architectural planes:

```math
\mathrm{AGES}
:=
\left\langle
O,\;
E,\;
C_E
\right\rangle
```

Where:

- $O$ is the Operational Plane;
- $E$ is the Evolution Plane;
- $C_E$ is the Evolution Control Plane.

Those planes answer:

```text
Operational Plane
What does the system do under its current baseline?

Evolution Plane
What could the system become?

Evolution Control Plane
What is the system permitted to become?
```

Evolutionary scopes answer a different question:

> **At which identity scale does the evolution occur?**

The principal scopes are:

```math
s
\in
\left\{
\mathrm{Lineage},
\mathrm{Situated},
\mathrm{Collective}
\right\}
```

The distinction is therefore:

```text
Architectural plane
= responsibility and function

Evolutionary scope
= identity domain in which change occurs
```

A candidate change may belong to any evolutionary scope while still passing
through the Operational, Evolution and Evolution Control planes.

## 2. Why a multidimensional model is required

A complex artificial system may evolve simultaneously across several
dimensions.

For example, a robot may have:

- a common product-family baseline;
- a local calibration for one site;
- an operator-specific interaction profile;
- a temporary coalition policy for one collaborative task;
- a runtime trajectory chosen under the current baseline.

Treating all these changes as one undifferentiated form of evolution creates
two opposite risks:

### Global freezing

Every local adaptation is treated as a fleet-wide baseline change.

Consequences may include:

- excessive governance latency;
- inability to personalise;
- inability to operate while disconnected;
- unnecessary fleet-wide trials;
- impractical ratification burden.

### Uncontrolled divergence

Every instance adapts independently without lineage, authority or provenance.

Consequences may include:

- loss of auditability;
- incompatible system behaviour;
- maintenance fragmentation;
- unsafe local optimisation;
- inability to promote useful learning;
- emergence of ungoverned system identities.

AGES therefore requires a multidimensional representation of evolution.

## 3. Orthogonal classification axes

A candidate transition should be classified across several independent axes.

A conceptual transition descriptor is:

```math
u
=
\left\langle
p,\;
s,\;
m,\;
e,\;
a,\;
r,\;
\tau,\;
q
\right\rangle
```

Where:

- $p$ is the architectural plane currently responsible;
- $s$ is the evolutionary scope;
- $m$ is the mutability class;
- $e$ is effectivity;
- $a$ is the authority domain;
- $r$ is the risk class;
- $\tau$ is the temporal regime;
- $q$ is the transition or learning status.

These axes must not be conflated.

For example:

| Axis | Example value |
|---|---|
| Architectural plane | Evolution Plane |
| Evolutionary scope | Situated |
| Mutability | M3 — Delegated adaptive |
| Effectivity | Robot R07, operator O12, site S4 |
| Authority | Local operational authority |
| Risk | Low |
| Temporal regime | Persistent local overlay |
| Status | Validated Learning Pack |

## 4. Evolutionary Scope I — Lineage Evolution

### 4.1 Definition

**Lineage Evolution** concerns the governed succession of baselines shared by
a family, model, product line, fleet class or foundation system.

Its identity object is not necessarily one physical instance. It is the
declared lineage from which many instances derive their canonical
configuration.

Examples include:

- a new foundation-model release;
- a new robot-family baseline;
- a firmware generation;
- a new aircraft-fleet software standard;
- a revised common safety policy;
- a new shared coordination protocol;
- a new certified calibration method.

A conceptual lineage transition is:

```math
B_n^{L,e}
\longrightarrow
B_{n+1}^{L,e'}
```

Where:

- $L$ identifies the lineage;
- $e$ is the source effectivity;
- $e'$ is the successor effectivity.

The successor effectivity may be narrower, broader or differently
partitioned.

### 4.2 Lineage identity

A lineage baseline may bind:

- common model or software artefacts;
- product-family hardware assumptions;
- shared CCI definitions;
- constitutional policies;
- shared invariants;
- standard interfaces;
- common validation suites;
- common recovery provisions;
- permitted situated-adaptation envelopes;
- permitted collective-coordination profiles.

The lineage defines what local and collective systems inherit.

### 4.3 Deployment pattern

Lineage evolution need not occur synchronously across every instance.

A common progression is:

```text
Development baseline
→ virtual validation
→ representative trial cohort
→ limited deployment cohort
→ jurisdictional or customer partition
→ wider lineage effectivity
```

The active fleet may therefore contain several simultaneously canonical
baselines under different effectivities.

### 4.4 Lineage rollback and recovery

A failed lineage release does not necessarily require a universal rollback.

Possible responses include:

- instance rollback;
- cohort rollback;
- effectivity contraction;
- suspension of one hardware revision;
- rollback in one jurisdiction;
- compensation for irreversible effects;
- recovery baseline for one subset;
- retention of the successor baseline for unaffected cohorts.

Use:

> **Fleet-wide rollback is one possible recovery policy, not the definition of
> lineage recovery.**

## 5. Evolutionary Scope II — Situated Evolution

### 5.1 Definition

**Situated Evolution** concerns adaptation associated with a specific
instance, interlocutor, operator, site, environment, task domain or persistent
context.

It addresses how a system may become locally more effective without silently
rewriting the common lineage baseline.

Examples include:

- operator-specific interaction preferences;
- user-specific accessibility settings;
- local vocabulary;
- site-specific workflow adaptation;
- local calibration;
- environmental tuning;
- persistent instance memory;
- local model adapters;
- task-specific parameter refinement;
- organisation-specific policy overlays.

Situated evolution is broader than federated learning.

Federated learning is one possible method for aggregating distributed
experience. It is not the definition of situated evolution.

### 5.2 Situated composition

A situated configuration may be represented conceptually as:

```math
B_{n,i,c}^{S}
=
B_n^L
\oplus
A_{i,c}
```

Where:

- $B_n^L$ is the inherited lineage baseline;
- $A_{i,c}$ is the governed adaptation associated with instance $i$ and
  context $c$;
- $\oplus$ denotes governed composition, not arithmetic addition.

The composition must preserve:

- lineage invariants;
- effectivity;
- authority boundaries;
- provenance;
- rollback or removal semantics;
- distinction between inherited and local state.

### 5.3 Situated state classes

Situated information may be classified as:

| Class | Meaning |
|---|---|
| Transient context | Short-lived runtime information |
| Operational preference | User or operator preference under the current baseline |
| Delegated adaptation | Bounded adaptation inside a pre-authorised envelope |
| Governed local overlay | Persistent local configuration under explicit effectivity |
| Instance baseline | Ratified canonical configuration for one instance |
| Lineage-promotion candidate | Local learning proposed for broader adoption |

Use the distinction:

```text
User preference
≠ transient context
≠ delegated adaptation
≠ local overlay
≠ instance baseline
≠ lineage baseline
```

### 5.4 Interlocutor and operator context

For assistants, robots and collaborative systems, situated evolution may be
conditioned by the interlocutor or operator.

Relevant dimensions may include:

- role;
- qualification;
- language;
- accessibility needs;
- preferred interaction style;
- task competence;
- work history;
- trust level;
- authorisation;
- risk exposure.

Personalisation must not silently change:

- constitutional safety rules;
- legal restrictions;
- root authority;
- lineage invariants;
- access beyond the operator’s mandate.

An inexperienced or malicious operator must not be able to alter protected
lineage CCIs through local interaction.

### 5.5 Privacy and local custody

Situated evolution may involve personal, sensitive or organisation-specific
data.

A situated profile should declare:

- data custodian;
- retention;
- portability;
- deletion rules;
- local versus central storage;
- aggregation permissions;
- privacy-preserving transformations;
- scope of model or memory reuse.

A locally successful adaptation must not automatically be exported.

## 6. Evolutionary Scope III — Collective Evolution

### 6.1 Definition

**Collective Evolution** concerns the identity, capability and governed
adaptation of a group of cooperating artificial systems.

The group may be:

- temporary;
- persistent;
- centrally coordinated;
- distributed;
- peer-to-peer;
- hierarchical;
- dynamically assembled.

Examples include:

- collaborative robot cells;
- robot–robot cooperation;
- drone swarms;
- autonomous vehicle platoons;
- AGV or AMR fleets;
- multi-agent software systems;
- distributed sensor networks;
- human–robot teams;
- federated service coalitions.

`Corobotic Evolution` may be defined as a robotics-specific profile of
Collective Evolution.

### 6.2 Collective identity

A collective may have a distinct governed identity:

```math
G_k
=
\left\langle
N_k,\;
T_k,\;
P_k,\;
A_k,\;
E_k,\;
B_k^G
\right\rangle
```

Where:

- $N_k$ is the set of participating nodes;
- $T_k$ is the network or interaction topology;
- $P_k$ is the cooperation protocol;
- $A_k$ is the collective or delegated authority structure;
- $E_k$ is collective effectivity;
- $B_k^G$ is the group baseline or group configuration.

The group identity may persist only for the duration of one task, or it may
become a long-lived coalition baseline.

### 6.3 Collective configuration

A collective configuration may include:

- member identities;
- member lineage baselines;
- member situated overlays;
- roles;
- task allocation;
- shared world model;
- communication protocol;
- consensus rules;
- leader or quorum rules;
- safety veto;
- resource reservations;
- failure-recovery rules;
- collective invariants;
- group effectivity;
- formation and dissolution conditions.

### 6.4 Operational coordination versus evolution

Dynamic cooperation does not automatically constitute evolution.

Examples of operational coordination include:

- assigning a task to another robot;
- changing formation;
- rerouting after one node fails;
- selecting a pre-authorised leader;
- redistributing workload;
- switching to a declared fallback protocol.

These may remain inside the active collective baseline.

Collective evolution occurs when the group modifies a baseline-controlled
property such as:

- the coordination protocol;
- the consensus method;
- admissible roles;
- authority structure;
- shared model;
- task-allocation policy;
- collision-avoidance policy;
- communication topology constraints;
- collective capability repertoire.

Use:

```text
Operational coalition state
≠ collective adaptation
≠ collective candidate change
≠ ratified collective baseline
```

### 6.5 Consensus and authority

Consensus establishes agreement among participants.

It does not automatically establish legitimate authority.

> **Consensus is a decision mechanism; authority is the governed competence to
> make the decision effective.**

A collective may use:

- leader authority;
- peer consensus;
- quorum;
- weighted voting;
- safety-node veto;
- external supervisor;
- human approval;
- jurisdictional authority;
- pre-authorised emergency delegation.

The authority constitution of the collective must define which decisions each
mechanism may make.

## 7. Scope is orthogonal to mutability

Evolutionary scope and CCI mutability are independent dimensions.

| Object | Evolutionary scope | Possible mutability |
|---|---|---|
| Foundation safety policy | Lineage | M0 — Constitutive |
| Common perception model | Lineage | M1 or M2 |
| Site calibration | Situated | M2 or M3 |
| Operator-specific adapter | Situated | M3 |
| Temporary conversation context | Situated | M4 |
| Shared swarm strategy | Collective | M2 or M3 |
| Current task assignment | Collective-operational | M4 |
| Collective authority constitution | Collective or Lineage | M0 or M1 |

No fixed mapping should be assumed.

A situated change may be high risk and constitutive.

A lineage change may be low risk and highly reversible.

A collective operational decision may be transient.

## 8. Scope is orthogonal to effectivity

Evolutionary scope identifies the identity domain.

Effectivity identifies the actual applicability.

For example:

```text
Scope:
Situated

Effectivity:
Robot R07
Operator O12
Site S4
Night shift
Inspection task class
Valid until 2026-12-31
```

Or:

```text
Scope:
Collective

Effectivity:
Coalition G17
Nodes R02, R03, R08
Warehouse zone Z2
Task class pallet-recovery
Duration of mission M44
```

A scope without effectivity is incomplete for execution.

## 9. Scope is orthogonal to authority

Different authorities may govern the same scope.

Lineage authority may be:

- manufacturer;
- programme office;
- central model authority;
- regulator;
- consortium;
- fleet operator.

Situated authority may be:

- local operator;
- site administrator;
- data subject;
- instance owner;
- delegated machine authority;
- local safety authority.

Collective authority may be:

- coalition leader;
- peer quorum;
- safety supervisor;
- mission authority;
- external control station;
- shared policy engine.

The competent authority must match both scope and effectivity.

## 10. Scope is orthogonal to time

Each scope may operate at several temporal rates.

A conceptual relation is:

```math
\tau_{\mathrm{control}}
\ll
\tau_{\mathrm{operation}}
\ll
\tau_{\mathrm{adaptation}}
\ll
\tau_{\mathrm{governance}}
```

However, the actual time scales vary by domain.

### Lineage temporal regime

Typical properties:

- low or moderate release frequency;
- long validation cycle;
- wide effectivity;
- high coordination cost;
- strong ratification requirements.

### Situated temporal regime

Typical properties:

- frequent adaptation;
- local evidence;
- narrow effectivity;
- privacy constraints;
- rapid rollback or overlay removal.

### Collective temporal regime

Typical properties:

- high-rate operational coordination;
- temporary authority;
- rapidly changing membership;
- distributed state;
- delayed central reconciliation.

The Evolution Control Plane should not necessarily enter every real-time
decision.

Pre-authorised envelopes allow operational immediacy while preserving prior
governance.

## 11. Multidimensional decision predicate

The SAI-AUT-OS decision predicate may be extended to include scope validity.

```math
\mathrm{Allow}(u)
:=
D(u)
\land
C(u)
\land
M(u)
\land
S(u)
\land
A(u)
\land
E(u)
\land
R(u)
\land
V(u)
```

Where:

- $D(u)$ means the candidate belongs to an allowed domain;
- $C(u)$ means context is valid;
- $M(u)$ means the target CCI is mutable;
- $S(u)$ means the declared evolutionary scope is valid;
- $A(u)$ means competent authority exists;
- $E(u)$ means evidence and effectivity are sufficient;
- $R(u)$ means risk and recovery requirements are satisfied;
- $V(u)$ means required validation has passed.

The scope predicate $S(u)$ may verify that:

- the change belongs to the declared scope;
- the authority is competent for that scope;
- the affected identity is correctly resolved;
- the change does not silently modify another scope;
- inter-scope propagation is authorised;
- inherited invariants are preserved;
- local or collective changes remain inside lineage limits.

## 12. Inter-scope propagation

Knowledge and candidate changes may propagate between scopes.

Propagation is not simple copying.

It is a governed transition that must preserve provenance, effectivity,
authority and compatibility.

### 12.1 Bottom-up propagation

#### Situated to Lineage

```text
Situated execution
→ local Action Closure Records
→ local Learning Packs
→ privacy and quality validation
→ cross-instance comparison
→ Learning Aggregate
→ lineage candidate
→ lineage validation and trial
→ lineage ratification
```

#### Collective to Lineage

```text
Collective execution
→ collective Learning Packs
→ coordination-strategy validation
→ reusable protocol candidate
→ lineage or fleet-level trial
→ lineage ratification
```

#### Situated to Collective

```text
Local capability or preference
→ collective compatibility check
→ bounded coalition profile
→ collective authorisation
```

### 12.2 Top-down propagation

#### Lineage to Situated

```text
Lineage baseline
→ effectivity partition
→ instance deployment
→ local adaptation envelope
→ situated operation
```

#### Lineage to Collective

```text
Lineage policy
→ collective constitution
→ delegated group authority
→ collective operation
```

#### Collective to Situated

```text
Collective decision
→ node-specific assignment
→ local operational execution
```

### 12.3 Lateral propagation

#### Situated to Situated

```text
Situated scope A
→ validated transferable Learning Pack
→ compatibility and privacy validation
→ situated scope B
```

#### Collective to Collective

```text
Collective group G1
→ validated coordination strategy
→ topology and authority compatibility
→ collective group G2
```

#### Lineage to Lineage

```text
Lineage L1
→ portable candidate or evidence
→ architecture and invariant mapping
→ lineage L2 candidate
```

Lateral propagation must not assume semantic equivalence.

## 13. Promotion, retention and suppression

A validated local or collective innovation may have several outcomes.

It may be:

- retained locally;
- retained collectively;
- promoted laterally;
- proposed for lineage adoption;
- rejected as non-representative;
- restricted to one environment;
- blocked for privacy reasons;
- suppressed because it violates lineage invariants;
- retained only as negative evidence.

The architecture should avoid a binary local-versus-global model.

## 14. Scope transition classes

A change may be classified by scope movement.

| Transition class | Meaning |
|---|---|
| Intra-lineage | Change remains within one lineage |
| Intra-situated | Change remains within one instance–context scope |
| Intra-collective | Change remains within one coalition |
| Situated-to-lineage promotion | Local learning becomes a lineage candidate |
| Collective-to-lineage promotion | Group learning becomes a lineage candidate |
| Lineage-to-situated deployment | Common baseline is instantiated locally |
| Lineage-to-collective delegation | Common policy creates a group constitution |
| Situated-to-collective contribution | Local capability joins collective operation |
| Collective-to-situated assignment | Group policy produces node-specific action |
| Lateral transfer | Learning moves between peer scopes |

Each transition class may require a different validation and authority
profile.

## 15. Learning Packs by scope

Learning Packs should declare their originating scope.

### Lineage Learning Pack

May aggregate:

- release validation;
- fleet performance;
- cross-cohort regressions;
- common failure modes;
- baseline-wide evidence.

### Situated Learning Pack

May include:

- local environment;
- operator interaction;
- instance calibration;
- site-specific deviation;
- privacy restrictions;
- local task performance.

### Collective Learning Pack

May include:

- participating nodes;
- topology;
- group policy;
- task allocation;
- consensus record;
- distributed evidence;
- membership changes;
- group recovery.

A pack generated in one scope is not automatically valid in another.

## 16. Scope-aware Learning Aggregate

A Learning Aggregate should preserve scope boundaries.

A conceptual aggregate may be:

```math
LA_j^{s,e}
=
\bigoplus_{k \in K_j^{s,e}}
LP_k
```

Where:

- $s$ is the originating scope;
- $e$ is effectivity;
- $K_j^{s,e}$ is the compatible pack set;
- $\bigoplus$ is a governed aggregation operator.

Aggregation should preserve:

- originating scope;
- pack identity;
- effectivity;
- adverse evidence;
- outliers;
- privacy restrictions;
- authority;
- uncertainty.

## 17. Scope-aware baseline identity

A system may have several related baseline identities.

A conceptual representation is:

```math
\mathcal{B}(t)
=
\left\langle
B^L_n,\;
\{B^S_{i,c}\},\;
\{B^G_k\}
\right\rangle
```

Where:

- $B^L_n$ is the active lineage baseline;
- $B^S_{i,c}$ are active situated baselines or overlays;
- $B^G_k$ are active collective baselines or constitutions.

This is exploratory.

Not every runtime context or coalition requires a ratified baseline.

Profiles should distinguish:

- transient operational state;
- delegated overlay;
- persistent local baseline;
- temporary collective constitution;
- ratified collective baseline.

## 18. Scope inheritance

A lower-scope configuration may inherit constraints from a broader scope.

A typical inheritance chain is:

```text
Lineage invariants
→ situated invariants
→ collective invariants
→ operational constraints
```

Inheritance should be monotonic for protected constraints unless competent
authority explicitly permits a governed exception.

A local or collective scope may add stricter constraints.

It should not silently weaken lineage constitutional invariants.

## 19. Scope conflicts

Conflicts may arise when:

- a situated preference contradicts a lineage policy;
- a collective strategy exceeds one node’s authority;
- two lineages participate in one coalition with incompatible invariants;
- local calibration invalidates shared assumptions;
- a collective decision conflicts with jurisdictional effectivity;
- a lineage update invalidates a local overlay;
- one node leaves a coalition during execution.

Conflict resolution may require:

- precedence rules;
- veto rights;
- effectivity partitioning;
- adaptation invalidation;
- coalition reformation;
- safe-state transition;
- escalation;
- revised candidate formation.

The default must be explicit.

Ambiguity must not be treated as permission.

## 20. Heterogeneous collectives

A collective may contain systems from different lineages.

A heterogeneous collective profile should resolve:

- identity;
- compatible interfaces;
- shared operation vocabulary;
- minimum common invariants;
- authority;
- evidence exchange;
- trust;
- time synchronisation;
- data ownership;
- recovery;
- dissolution.

The group baseline should not imply that all members share one internal
baseline.

It may instead bind compatible external references.

## 21. Disconnected operation

Situated and collective systems may operate without access to central
lineage governance.

A disconnected profile may use:

- cached authority;
- delegated effectivity;
- local ledgers;
- signed event chains;
- safe-state rules;
- bounded local adaptation;
- later reconciliation.

Local operation must distinguish:

- globally ratified state;
- locally authorised state;
- provisional state;
- disputed state;
- unverified state.

A disconnected node must not silently declare its local state globally
canonical.

## 22. Scope revocation

Authority or effectivity may be revoked at one scope without invalidating all
others.

Examples include:

- revoke one operator-specific overlay;
- suspend one site;
- remove one robot from a coalition;
- withdraw one lineage release from one cohort;
- dissolve one collective constitution;
- block lateral transfer of one Learning Pack.

Revocation should preserve historical provenance.

## 23. Scope-aware rollback and recovery

Recovery should identify the affected scope.

### Lineage recovery

May include:

- release rollback;
- effectivity contraction;
- cohort recovery baseline;
- policy supersession.

### Situated recovery

May include:

- remove local overlay;
- restore instance calibration;
- clear invalid persistent memory;
- revert operator-specific adapter.

### Collective recovery

May include:

- dissolve coalition;
- remove failed node;
- revert coordination policy;
- elect fallback leader;
- enter group safe state;
- ratify recovery constitution.

A recovery action in one scope should not silently restore or alter another
scope.

## 24. Scope-aware authority constitution

Each scope may have an authority constitution.

### Lineage authority constitution

Defines:

- release authority;
- common policy authority;
- fleet effectivity;
- ratification;
- regulatory interaction.

### Situated authority constitution

Defines:

- operator permissions;
- user consent;
- local administrator authority;
- data ownership;
- local adaptation limits;
- export permission.

### Collective authority constitution

Defines:

- membership;
- leader or quorum;
- veto;
- task-allocation authority;
- emergency authority;
- dissolution;
- conflict resolution.

The constitutions themselves may be baseline-controlled CCIs.

## 25. Application profiles

The evolutionary scopes should not be equated with specific technologies.

### Lineage profiles

- Foundation Model Evolution
- Fleet Evolution
- Product-Line Evolution
- Firmware-Line Evolution
- Certified Baseline Evolution

### Situated profiles

- Personalisation
- Operator Adaptation
- Site Adaptation
- Local Calibration
- Persistent Context
- Federated Learning Participant

### Collective profiles

- Corobotics
- Swarm Robotics
- Multi-Agent Systems
- Cooperative Vehicles
- Distributed Sensor Networks
- Human–Robot Teams

`Federated Learning`, `Personalisation`, `Corobotics`, `Swarm Systems` and
`Fleet Evolution` are therefore application profiles, not synonyms for the
three scopes.

## 26. Robotics example

A collaborative robot may have:

| Layer | Example |
|---|---|
| Lineage baseline | Common controller, perception model and safety policy |
| Situated overlay | Operator-specific interaction and site calibration |
| Collective constitution | Temporary work-cell coordination policy |
| Operational state | Current trajectory and task assignment |

A local operator preference may alter communication style but not force limits.

A collective task reallocation may remain operational.

A revised shared collision-avoidance protocol may require collective or
lineage evolution.

## 27. LLM example

An AI assistant may have:

| Layer | Example |
|---|---|
| Lineage baseline | Foundation model, root policy and tool interfaces |
| Situated overlay | User memory, preferences and organisation-specific adapter |
| Collective constitution | Multi-agent coordination policy |
| Operational state | Current conversation and tool sequence |

A user preference may remain situated.

A reusable adapter may become a lineage candidate after aggregation.

A temporary agent coalition may coordinate tasks without changing the
foundation baseline.

## 28. Fleet example

An autonomous fleet may contain:

- one common lineage baseline;
- several hardware-revision effectivity partitions;
- local environmental calibrations;
- customer-specific policies;
- temporary task coalitions;
- one recovery baseline for a degraded cohort.

The fleet is not required to have one globally homogeneous active
configuration.

It must instead preserve explicit compatibility and provenance.

## 29. AI-II interface implications

AI-II may define interfaces for:

- scope identity;
- scope membership;
- lineage inheritance;
- situated overlay binding;
- collective constitution;
- inter-scope promotion;
- Learning Pack export;
- authority delegation;
- effectivity negotiation;
- scope conflict;
- scope revocation;
- reconciliation.

A scope identifier may be included in:

- candidate changes;
- GTL action candidates;
- evidence packages;
- authority records;
- Learning Packs;
- deployment records;
- ratification records.

## 30. SAI-AUT-OS implications

SAI-AUT-OS should become scope-aware.

It may:

- classify candidate scope;
- identify affected scope identities;
- enforce scope-specific policy;
- resolve competent authority;
- prevent unauthorised cross-scope effects;
- validate promotion conditions;
- enforce lineage inheritance;
- catalogue scope-specific Learning Packs;
- authorise lateral transfer;
- manage scope-specific rollback;
- ratify lineage, situated or collective baselines.

The SAI-AUT-OS decision record should include:

```yaml
evolutionaryScope:
  type: lineage | situated | collective
  scopeId:
  parentScope:
  inheritedBaseline:
  affectedIdentities:
  propagationIntent:
  sourceScope:
  targetScope:
```

This example is exploratory and non-normative.

## 31. Minimum scope descriptor

```yaml
scopeId:
scopeType:
status:

identity:
  lineageId:
  instanceIds:
  contextIds:
  collectiveId:
  memberIds:

inheritance:
  parentBaseline:
  inheritedInvariants:
  inheritedPolicies:
  inheritedAuthorityLimits:

effectivity:
  organisations:
  instances:
  cohorts:
  environments:
  jurisdictions:
  taskClasses:
  validFrom:
  validUntil:

authority:
  constitutionId:
  competentRoles:
  delegation:
  veto:
  revocation:

learning:
  catalogueId:
  exportPermitted:
  aggregationPermitted:
  promotionTargets:

recovery:
  rollbackScope:
  compensation:
  safeState:
  dissolution:
```

This example is exploratory and non-normative.

## 32. Design principles

1. **Architectural planes and evolutionary scopes must remain distinct.**
2. **Scope identifies where system identity is changing.**
3. **Mutability, effectivity, authority and risk are orthogonal axes.**
4. **Local adaptation must not silently rewrite lineage identity.**
5. **Collective agreement must not be confused with legitimate authority.**
6. **Operational coordination must remain distinct from collective evolution.**
7. **Inter-scope propagation is a governed transition.**
8. **Learning must preserve its originating scope and effectivity.**
9. **Lineage invariants constrain situated and collective evolution.**
10. **A narrower scope may add stricter constraints.**
11. **Promotion requires new validation at the target scope.**
12. **Federated learning is a situated-to-lineage profile, not the definition
    of situated evolution.**
13. **Corobotics is a collective profile, not the definition of collective
    evolution.**
14. **Scope-aware rollback must not silently alter unaffected identities.**
15. **Disconnected operation may be provisional but must remain
    reconstructable.**
16. **No scope may silently expand its own authority or effectivity.**

## 33. Open questions

- Are Lineage, Situated and Collective scopes sufficient as the minimum core?
- Is an additional Ecosystem or Institutional scope required?
- When does a situated overlay become an instance baseline?
- When does a temporary coalition require a ratified collective baseline?
- Can one candidate belong to more than one scope?
- How should mixed-scope atomic transitions be represented?
- How should lineage updates invalidate or migrate situated overlays?
- Which collective decisions may be made through peer consensus?
- How should heterogeneous lineages negotiate common invariants?
- How should privacy-preserving Learning Packs be promoted?
- Which evidence supports cross-scope generalisation?
- How should lateral transfer compatibility be measured?
- Can a situated adaptation be constitutive for one individual?
- How should scope identities survive custodian transfer?
- How should scope-specific ages be represented?
- Can lineage, situated and collective ages overlap independently?
- How should scope revocation affect active execution?
- How should disconnected collective ratification be reconciled?
- Which scope boundaries require independent authority?
- How should collective dissolution preserve provenance?
- How should emergent group behaviour be distinguished from baseline change?

## 34. Unresolved issues

- minimum scope ontology;
- mixed-scope transitions;
- concurrent scope-specific ages;
- inter-scope inheritance;
- lineage-to-situated migration;
- collective authority constitution;
- heterogeneous collective compatibility;
- scope-aware Learning Pack aggregation;
- privacy-preserving promotion;
- lateral transfer assurance;
- disconnected reconciliation;
- scope-specific ratification;
- effectivity conflicts;
- cross-jurisdictional collectives;
- constitutive local identity;
- temporary versus persistent collective identity.

## Related

- [`01-architectural-planes.md`](01-architectural-planes.md)
- [`02-state-and-transition-model.md`](02-state-and-transition-model.md)
- [`03-evidence-and-authority.md`](03-evidence-and-authority.md)
- [`04-effectivity.md`](04-effectivity.md)
- [`05-identity-and-provenance.md`](05-identity-and-provenance.md)
- [`06-GENTILE.md`](06-GENTILE.md)
- [`07-GTL.md`](07-GTL.md)
- [`08-gentile-gtl-integration.md`](08-gentile-gtl-integration.md)
- [`09-learning-mechanics.md`](09-learning-mechanics.md)
- [`10-SAI-AUT-OS.md`](10-SAI-AUT-OS.md)
- [`AI-II.md`](AI-II.md)
- [`../theory/02-system-identity.md`](../theory/02-system-identity.md)
- [`../theory/04-evolution-transitions.md`](../theory/04-evolution-transitions.md)
- [`../theory/05-governed-continuity.md`](../theory/05-governed-continuity.md)
- [`../models/identity-continuity-model.md`](../models/identity-continuity-model.md)
- [`../research/open-questions.md`](../research/open-questions.md)
