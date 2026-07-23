<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Effectivity

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Define where, when and to which parts of an artificial evolutive
system a candidate, authority, transition or baseline applies.

## Definition

**Effectivity** is the declared applicability of an AGES object.

It determines where, when and to which:

- organisations;
- programmes;
- products;
- system families;
- hardware revisions;
- software configurations;
- model variants;
- individual instances;
- fleets or cohorts;
- deployments;
- environments;
- jurisdictions;
- operating contexts;
- mission or task classes;
- lifecycle stages;
- authority domains;
- time intervals;

a candidate change, validation result, authorisation, transition, policy,
invariant or baseline applies.

A valid change is not necessarily valid everywhere.

A baseline may be canonical for one effectivity and inapplicable, prohibited
or superseded under another.

## Effectivity as a first-class object

Effectivity must not be treated as an informal deployment note.

An effectivity declaration should be:

- explicit;
- identifiable;
- versioned or otherwise provenance-controlled;
- linked to the governed object;
- bounded in scope;
- temporally qualified where required;
- adjudicated where it affects authority or safety;
- reconstructable from the ledger.

A conceptual effectivity object may include:

```text
Effectivity :=
    Subject
    + Scope dimensions
    + Inclusion rules
    + Exclusion rules
    + Validity interval
    + Preconditions
    + Authority
    + Provenance
```

This is a conceptual model, not a completed formal definition.

## Effectivity dimensions

Effectivity may be expressed across several dimensions.

### Organisational effectivity

Defines which organisations, operators, owners, authorities or business
entities may apply the governed object.

Examples:

- one operator;
- one customer;
- one maintenance organisation;
- one regulatory authority;
- one consortium;
- one programme office.

### Product and configuration effectivity

Defines which product families, hardware revisions, software configurations
or component combinations are covered.

Examples:

- one robot family;
- one aircraft variant;
- one hardware revision;
- one sensor configuration;
- one firmware branch;
- one model architecture.

### Instance and cohort effectivity

Defines whether applicability is:

- global;
- fleet-wide;
- cohort-specific;
- batch-specific;
- instance-specific;
- experimental;
- temporary.

A fleet-level candidate does not automatically have fleet-wide deployment
authority.

### Environmental effectivity

Defines the environments in which the object is valid.

Examples:

- simulation;
- sandbox;
- laboratory;
- staging;
- shadow mode;
- controlled physical cell;
- production;
- airborne operation;
- degraded mode;
- emergency operation.

### Jurisdictional effectivity

Defines applicability under legal, regulatory, contractual or institutional
boundaries.

A baseline or policy valid in one jurisdiction may not be valid in another.

### Operational-context effectivity

Defines applicable:

- tasks;
- missions;
- modes;
- geographic zones;
- human-supervision levels;
- autonomy levels;
- safety envelopes;
- external dependencies;
- environmental assumptions.

### Lifecycle effectivity

Defines the lifecycle stages in which the object applies.

Examples:

- concept;
- development;
- integration;
- validation;
- controlled trial;
- deployment;
- probation;
- operation;
- maintenance;
- recovery;
- retirement.

### Temporal effectivity

Defines when applicability begins and ends.

It may include:

- valid-from;
- valid-until;
- expiry;
- review date;
- activation event;
- suspension event;
- supersession event.

Temporal validity is distinct from baseline age.

An age describes how long a ratified baseline remains canonical under its
effectivity. Temporal effectivity defines where that canonicality is valid in
time.

## Effectivity across the lifecycle

Effectivity should be declared and progressively refined throughout the
transition lifecycle.

```mermaid
flowchart LR
    C["Candidate effectivity"]
    V["Validation effectivity"]
    T["Controlled-trial effectivity"]
    D["Operational deployment effectivity"]
    P["Probation effectivity"]
    B["Ratified baseline effectivity"]

    C --> V
    V --> T
    T --> D
    D --> P
    P --> B
```

Expansion from one stage to another is not automatic.

Each expansion may require new evidence, adjudication and authority.

## Candidate effectivity

Candidate effectivity defines the intended scope of the proposed change.

It should identify:

- the source baseline or baseline family;
- intended target systems;
- expected environments;
- proposed jurisdictions;
- affected lifecycle stages;
- known exclusions;
- assumed dependencies.

Candidate effectivity is a proposal, not permission to test or deploy.

## Validation effectivity

Validation evidence is valid only within the domain actually represented by
the test.

Validation effectivity may be limited by:

- simulated environment;
- dataset;
- hardware model;
- software configuration;
- model variant;
- operational assumptions;
- test conditions;
- failure modes;
- geographic or environmental conditions.

Evidence produced under one effectivity must not be silently generalised to
another.

For example:

```text
Evidence valid for simulation
≠ evidence valid for laboratory hardware
≠ evidence valid for operational deployment
```

## Controlled-trial effectivity

Controlled-trial effectivity defines the bounded scope in which experimental
execution is authorised.

It may restrict:

- environment;
- hardware;
- data;
- instances;
- cohort size;
- duration;
- task class;
- operator supervision;
- autonomy level;
- physical limits;
- geographic zone;
- permitted fallback actions.

Trial effectivity should normally be narrower than proposed operational
effectivity.

Approval for a controlled trial does not authorise deployment outside the
trial scope.

## Operational deployment effectivity

Operational deployment effectivity defines where the candidate may be
introduced into operational use.

It should identify:

- authorised systems or instances;
- configuration prerequisites;
- operational environment;
- jurisdiction;
- mission or task scope;
- authority duration;
- deployment sequence;
- fallback and rollback applicability;
- excluded configurations.

A deployment authority is invalid outside its declared effectivity.

## Probation effectivity

A deployed but unratified configuration may operate under a narrower
**probation effectivity**.

Probation effectivity may constrain:

- number of instances;
- operating duration;
- operating modes;
- permitted tasks;
- environmental conditions;
- monitoring intensity;
- human supervision;
- fallback requirements.

Probation authority ends when the configuration is:

- ratified;
- reverted;
- compensated;
- suspended;
- replaced by a recovery baseline;
- allowed to expire.

## Baseline effectivity

A ratified baseline is canonical only within its declared effectivity.

Baseline effectivity should bind:

- system identity;
- applicable instances or cohorts;
- environment;
- jurisdiction;
- lifecycle stage;
- applicable policies;
- invariant set;
- authority domain;
- validity interval.

The expression “current baseline” is incomplete unless the relevant
effectivity is known.

## Multiple canonical baselines

Multiple baselines may be simultaneously canonical under disjoint or
partially disjoint effectivities.

For example:

```text
Baseline B12
    effective for hardware revision R1
    in jurisdiction J1

Baseline B13
    effective for hardware revision R2
    in jurisdictions J1 and J2
```

This does not necessarily imply contradiction.

The system may be modelled as:

- one partitioned artificial system with several active baseline
  effectivities;
- several cohort identities under one system family;
- concurrent ages associated with different effectivity partitions.

AGES does not yet prescribe one universal interpretation.

The chosen model must make clear:

- what constitutes the identity of the whole system;
- whether ages are global or partition-specific;
- how transitions affect each partition;
- how shared components and policies are represented;
- whether one partition may supersede another.

See
[`../research/open-questions.md`](../research/open-questions.md).

## Effectivity overlap

Overlapping effectivities may be:

- compatible;
- hierarchical;
- conditional;
- conflicting;
- ambiguous.

An overlap analysis should determine:

- whether two objects apply to the same subject;
- whether one is more specific;
- whether one supersedes another;
- whether both may coexist;
- whether a conflict requires adjudication;
- which authority has precedence.

Use the principle:

> **Applicability must be resolved before execution; ambiguity must not be
> treated as permission.**

Where conflicting effectivities remain unresolved, the default response
should be explicit, such as:

- BLOCK;
- DEFER;
- ESCALATE;
- restrict to the safer or narrower effectivity;
- enter a safe state.

## Specificity and precedence

A profile or policy may define precedence rules such as:

```text
instance-specific
> cohort-specific
> product-specific
> family-wide
> global
```

However, specificity alone must not override:

- jurisdiction;
- safety policy;
- constitutional invariants;
- authority limits;
- explicit prohibitions.

Precedence rules must be declared, not inferred informally.

## Inclusion and exclusion

Effectivity should support both inclusion and exclusion rules.

Examples:

```text
Include:
- robot family R
- hardware revision 3
- laboratory environment

Exclude:
- units with sensor package S1
- jurisdiction J2
- degraded battery state
```

Exclusions are first-class constraints and must be preserved during
effectivity expansion.

## Effectivity expansion

Expanding effectivity is itself a governed change.

Examples include:

- one instance to one cohort;
- laboratory to production;
- one jurisdiction to several;
- one hardware revision to a product family;
- supervised to unsupervised operation;
- temporary to indefinite validity.

Expansion may require:

- additional evidence;
- new validation;
- new authority;
- revised invariants;
- revised rollback or recovery provisions;
- a new candidate change;
- a successor baseline.

Use:

> **Evidence for a narrow effectivity does not automatically justify broader
> applicability.**

## Effectivity contraction

Effectivity may be reduced because of:

- anomaly;
- new evidence;
- authority revocation;
- environmental change;
- hardware degradation;
- jurisdictional restriction;
- invalidated assumptions;
- safety concern.

Contraction may result in:

- suspension of affected instances;
- cohort partitioning;
- fallback to another baseline;
- restricted operation;
- recovery transition;
- withdrawal of deployment authority.

Effectivity contraction must not silently rewrite historical records.

## Effectivity and authority

Authority is itself effective only within declared boundaries.

An authority record should specify:

- subject;
- role;
- permitted decisions;
- organisations;
- systems;
- instances;
- environments;
- jurisdictions;
- lifecycle stages;
- valid-from;
- valid-until;
- delegation chain;
- revocation status.

A technically valid decision issued outside the authority's effectivity is
not an authorised AGES decision.

## Effectivity and evidence

Evidence must declare the scope within which it is relevant.

Evidence adjudication should assess:

- whether the evidence subject matches the candidate subject;
- whether configuration and environment match;
- whether the dataset or simulation is representative;
- whether the evidence remains temporally valid;
- whether jurisdictional or operational assumptions differ;
- whether extrapolation is being requested;
- whether uncertainty increases under expanded scope.

Evidence may support:

- all proposed effectivity;
- only a subset;
- a conditional subset;
- no applicable scope.

## Effectivity and invariants

Invariant applicability may vary by effectivity.

Examples:

- a human-separation invariant applies only during collaborative operation;
- an emissions invariant applies only in a declared jurisdiction;
- a thermal invariant applies only in a high-temperature environment;
- a policy invariant applies only to one organisational domain.

Effectivity must identify which invariants govern the candidate and resulting
baseline.

A transition cannot preserve an invariant that was never correctly selected.

## Effectivity and rollback

Rollback, compensation and recovery provisions also have effectivity.

A rollback target may be valid only for:

- specific hardware;
- specific data migrations;
- specific environments;
- a limited time;
- instances that have not crossed an irreversible step.

Before deployment, governance should verify that the declared recovery path is
effective for the same scope as the deployment.

Use:

```text
Deployment effectivity
must be compatible with
recovery effectivity
```

Where exact rollback is unavailable, compensation or recovery-baseline
effectivity must be declared.

## Effectivity and GENTILE

GENTILE may help identify and negotiate:

- intended scope;
- target subjects;
- exclusions;
- environmental assumptions;
- jurisdiction;
- lifecycle stage;
- temporal validity;
- unresolved ambiguity.

A semantic artefact should preserve uncertainty about effectivity rather than
silently selecting an overly broad scope.

GENTILE does not authorise the resulting effectivity.

## Effectivity and GTL

A GTL action candidate should bind its operation to explicit effectivity.

It should identify:

- which executor may act;
- on which direct object;
- in which environment;
- under which operating mode;
- during which validity interval;
- for which instance or cohort;
- under which authority;
- with which limits and fallback actions.

A technically executable action outside its effectivity is not an authorised
operation.

## Minimal conceptual checks

Before adjudication or execution, an AGES implementation should be able to
answer:

1. What object is being governed?
2. To which systems or instances does it apply?
3. Under which configurations?
4. In which environments and operating contexts?
5. Under which jurisdiction?
6. During which lifecycle stage?
7. From when until when?
8. Which authority is effective?
9. Which invariants are applicable?
10. Which evidence supports this exact scope?
11. Which exclusions apply?
12. Is the rollback, compensation or recovery path effective for the same
    scope?
13. Does the proposed scope overlap or conflict with another canonical
    baseline?

## Example lifecycle constraint

```text
Candidate effectivity
⊇ validation effectivity
⊇ controlled-trial effectivity

Operational deployment effectivity
must be supported by applicable evidence

Probation effectivity
⊆ operational deployment effectivity

Ratified baseline effectivity
must not exceed adjudicated and authorised effectivity
```

These relations are conceptual. Profiles may define different relationships
where justified, but any expansion must remain explicit and governed.

## Key questions

- Can one AGES contain several simultaneously canonical baselines?
- Are concurrent effectivity partitions separate ages or one partitioned age?
- Which dimensions are mandatory for a minimal effectivity declaration?
- How should effectivity inheritance work?
- How should conflicting effectivities be resolved?
- When does effectivity expansion require a new baseline?
- Can evidence be safely extrapolated from one cohort to another?
- How should temporary experimental effectivity expire?
- How should jurisdictional and technical authority interact?
- Can one component have a different baseline effectivity from the system that
  contains it?
- How should shared services be represented across several baseline
  partitions?
- How is rollback effectivity validated?
- What happens when effectivity becomes ambiguous during execution?
- How should effectivity be represented for mobile or dynamically
  reconfigurable systems?
- How are effectivity changes reconstructed over long system lifecycles?

## Unresolved issues

- concurrent ages versus partitioned system identity;
- precedence across overlapping effectivities;
- effectivity inheritance;
- cross-jurisdictional conflicts;
- temporary and conditional canonicality;
- effectivity of shared infrastructure;
- effectivity drift caused by environmental or hardware change;
- effectivity reconciliation after fleet divergence;
- rollback applicability after irreversible transitions.

## Related

- [`01-architectural-planes.md`](01-architectural-planes.md)
- [`02-state-and-transition-model.md`](02-state-and-transition-model.md)
- [`03-evidence-and-authority.md`](03-evidence-and-authority.md)
- [`06-GENTILE.md`](06-GENTILE.md)
- [`07-GTL.md`](07-GTL.md)
- [`08-gentile-gtl-integration.md`](08-gentile-gtl-integration.md)
- [`../schemas/examples/effectivity.example.yaml`](../schemas/examples/effectivity.example.yaml)
- [`../models/transition-model.md`](../models/transition-model.md)
- [`../research/open-questions.md`](../research/open-questions.md)
