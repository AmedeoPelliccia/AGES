<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Evidence and Authority

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Characterise the evidentiary and authority structures used to
adjudicate candidate changes, controlled trials, operational deployments,
ratification decisions and recovery actions.

Evidence and authority are distinct inputs to governance.

Evidence addresses:

> **What is known, how was it established, and within which limits does it
> support the candidate?**

Authority addresses:

> **Who or what is permitted to decide, act, delegate, ratify, suspend or
> reverse the transition?**

Neither evidence nor authority is sufficient alone. Strong evidence does not
create authority, and authority does not make weak evidence sufficient.

## Evidence

Evidence consists of observations, test results, analyses, attestations,
measurements and trace records used to determine whether a candidate,
execution or resulting state satisfies declared requirements.

Evidence should carry:

- a unique identifier;
- source and provenance;
- collection time;
- integrity protection;
- scope;
- applicable baseline and candidate references;
- effectivity;
- method;
- assumptions;
- limitations;
- uncertainty;
- result;
- responsible producer or attestor;
- links to the requirement, invariant or closure criterion it supports.

See
[`../schemas/examples/evidence.example.yaml`](../schemas/examples/evidence.example.yaml).

## Evidence classes

AGES may distinguish several evidence classes.

### Observational evidence

Evidence derived from operation, monitoring or inspection, including:

- anomaly reports;
- performance trends;
- incident records;
- degradation observations;
- operator reports;
- telemetry;
- sensor data;
- field experience.

Observational evidence may motivate a candidate change, but raw observation
alone may not establish that the candidate is safe or effective.

### Analytical evidence

Evidence produced through structured reasoning or computation, including:

- static analysis;
- interface analysis;
- hazard analysis;
- dependency analysis;
- compatibility analysis;
- formal proof;
- model checking;
- resource analysis;
- risk assessment.

### Virtual-validation evidence

Evidence produced without modifying the current operational baseline,
including:

- model-in-the-loop testing;
- software-in-the-loop testing;
- simulation;
- digital-twin evaluation;
- synthetic-data testing;
- regression suites;
- fault injection in a virtual environment.

Virtual evidence must state the validity domain of the model or simulation.
Correspondence with the physical or operational system must not be assumed
without justification.

### Controlled-trial evidence

Evidence produced under bounded experimental authority, including:

- sandbox execution;
- hardware-in-the-loop testing;
- laboratory trials;
- staging;
- shadow mode;
- canary deployment;
- limited-instance or limited-cohort trials.

Trial evidence must identify:

- the authorised test scope;
- the test environment;
- applicable safety limits;
- effectivity;
- duration;
- abort conditions;
- deviations;
- restoration or compensation status.

### Deployment evidence

Evidence establishing whether the authorised change was installed, activated
or executed as intended.

It may include:

- deployed artefact identifiers;
- configuration hashes;
- installation records;
- activation records;
- migration results;
- hardware identity;
- calibration confirmation;
- execution logs;
- authority and effectivity checks.

### Closure evidence

Evidence establishing whether the resulting state satisfies the declared
postconditions and may be considered operationally closed.

Closure evidence should address:

- whether the authorised action occurred;
- whether execution remained inside its authorised envelope;
- whether the expected target state was achieved;
- whether applicable invariants remained true;
- whether deviations occurred;
- whether fallback, rollback or compensation was used;
- whether the resulting configuration corresponds to the candidate baseline;
- whether the result is eligible for ratification.

Closure evidence may be digital, physical, organisational or mixed.

### Monitoring evidence

Evidence produced after deployment or ratification.

Two contexts must be distinguished:

- **probation monitoring**, which informs whether a deployed candidate may be
  ratified;
- **active-baseline monitoring**, which evaluates the continued validity of an
  already ratified baseline.

An anomaly after ratification may justify suspension or a new transition, but
does not erase the historical ratification record.

## Evidence quality

Evidence quality is not determined by volume alone.

Evidence should be evaluated for:

- relevance;
- validity;
- integrity;
- provenance;
- independence;
- repeatability;
- representativeness;
- uncertainty;
- completeness;
- timeliness;
- consistency;
- domain applicability;
- resistance to manipulation;
- traceability to requirements and invariants.

A large quantity of telemetry may still be insufficient if it does not
support the declared decision criteria.

## Evidence sufficiency

Evidence is sufficient only relative to a declared decision.

The evidence required to permit a virtual simulation may differ from the
evidence required to:

- authorise a controlled physical trial;
- authorise operational deployment;
- extend effectivity;
- ratify a successor baseline;
- waive a non-constitutive requirement;
- suspend an active baseline;
- initiate rollback or compensation;
- establish a recovery baseline.

Therefore:

```text
Evidence sufficiency
= evidence quality
+ decision context
+ applicable risk
+ effectivity
+ authority policy
+ declared acceptance criteria
```

Evidence adjudication should record not only whether the evidence passed, but
why it was considered sufficient for the specific decision.

## Negative, conflicting and inconclusive evidence

AGES must preserve evidence that:

- opposes the candidate;
- reveals uncertainty;
- conflicts with other evidence;
- remains inconclusive;
- invalidates an assumption;
- indicates a failed trial;
- demonstrates effectivity limitations.

Evidence must not be discarded merely because it does not support the desired
outcome.

Where evidence conflicts, adjudication should record:

- the conflict;
- the relative credibility and applicability of each source;
- any unresolved uncertainty;
- the authority responsible for accepting residual risk;
- whether the decision is deferred, restricted or escalated.

## Authority

Authority defines who or what may:

- observe and report;
- propose a candidate change;
- generate or collect evidence;
- execute validation;
- adjudicate evidence;
- authorise a controlled trial;
- execute a controlled trial;
- authorise operational deployment;
- deploy;
- verify closure;
- ratify a baseline;
- suspend a baseline;
- initiate rollback, compensation or safe-state action;
- establish a recovery baseline;
- revoke or delegate authority.

Authority may be:

- human;
- organisational;
- procedural;
- role-based;
- policy-based;
- delegated;
- automated under prior policy;
- distributed across multiple roles;
- time-limited;
- effectivity-limited;
- conditional.

Automation does not eliminate responsibility.

## Authority is not capability

A subsystem may be technically capable of performing an action without being
authorised to perform it.

Use the distinctions:

```text
Capability ≠ authority
Semantic agreement ≠ authorisation
Technical executability ≠ permission to execute
Evidence production ≠ evidence adjudication
Deployment completion ≠ baseline ratification
```

GENTILE may structure an authority request but does not acquire authority by
doing so.

GTL may produce a technically executable action candidate but does not
authorise its execution.

A validator may establish that a test passed but does not automatically own
the authority to judge whether the test set was sufficient.

## Authority roles

A concrete AGES implementation may define roles such as:

| Role | Typical responsibility |
|---|---|
| Proposer | Defines or submits the candidate change |
| Evidence producer | Generates tests, measurements, analyses or attestations |
| Validator | Executes declared validation activities |
| Evidence adjudicator | Judges evidence relevance, quality and sufficiency |
| Trial authority | Permits bounded experimentation |
| Deployment authority | Permits operational deployment |
| Executor | Performs the authorised trial, deployment or recovery action |
| Closure verifier | Determines whether postconditions and invariants were satisfied |
| Ratification authority | Establishes the resulting configuration as the canonical successor baseline |
| Suspension authority | Restricts or suspends use of an active baseline |
| Recovery authority | Approves rollback, compensation, containment or a recovery baseline |
| Ledger custodian | Preserves decision, authority and provenance records |

One actor may hold multiple roles in a low-risk implementation, but role
combination must remain explicit.

Higher-risk profiles may require organisational or technical separation of
duties.

## Two authorisation gates

Where a controlled trial is applicable, AGES distinguishes at least two
authority gates.

### Controlled-trial authorisation

This authority permits bounded evidence generation.

It should specify:

- candidate identifier;
- source baseline;
- authorised environment;
- permitted systems, instances or cohorts;
- trial duration;
- operational limits;
- applicable invariants;
- required monitoring;
- abort conditions;
- restoration, compensation or safe-state provisions;
- evidence to be collected;
- responsible executor;
- authority expiry.

Approval for a controlled trial does not authorise operational deployment.

### Operational deployment authorisation

This authority permits the candidate to enter its declared operational
effectivity.

It should specify:

- approved candidate or bounded candidate set;
- operational effectivity;
- deployment method;
- delegated selection policy, if alternatives exist;
- residual risk;
- required rollback, compensation or recovery provisions;
- probation conditions;
- closure criteria;
- authority expiry or review conditions.

Operational authorisation does not itself ratify the successor baseline.

## Ratification authority

Ratification authority determines whether the verified resulting
configuration becomes canonical.

Ratification should consider:

- the authorised candidate;
- actual deployment outcome;
- closure evidence;
- resulting configuration identity;
- invariant results;
- deviations;
- effectivity;
- unresolved risk;
- rollback or compensation status;
- probation evidence;
- ledger completeness.

Ratification closes the preceding age and opens the next.

A deployed but unratified configuration may operate only under an explicit,
bounded probation authority.

## Delegated machine authority

Machine authority must derive from explicit prior delegation.

A delegated machine may be authorised to:

- reject structurally incomplete input;
- request clarification;
- select among pre-authorised alternatives;
- abort execution;
- activate an independently authorised safe state;
- collect evidence;
- initiate an emergency containment path;
- execute a rollback already authorised by policy.

Delegation should define:

- delegating authority;
- delegated subject;
- permitted decisions or actions;
- prohibited actions;
- effectivity;
- validity period;
- decision thresholds;
- required evidence;
- escalation conditions;
- revocation mechanism;
- audit requirements.

A delegated component should not implicitly be permitted to:

- expand its own authority;
- expand effectivity;
- waive constitutional invariants;
- authorise an unapproved candidate;
- suppress adverse evidence;
- ratify its own resulting baseline;
- rewrite the policy governing its delegation.

## Prior authority and emergency action

Some actions must be operationally immediate, including:

- emergency stop;
- safe-state activation;
- containment;
- abort;
- rollback under pre-approved conditions.

Such action may occur without waiting for a new human decision while still
remaining governed through prior authority.

Use:

> **Operational immediacy does not imply absence of governance; it may reflect
> governance established in advance.**

Emergency action should produce an authority and evidence record after
execution where pre-execution recording is impossible.

## Authority revocation

Authority may be revoked because of:

- expiry;
- role change;
- policy change;
- loss of qualification;
- conflict of interest;
- evidence of compromise;
- effectivity change;
- anomaly;
- invalidated assumptions;
- superseding authority.

Revocation must define its impact on transitions already in progress.

Possible responses include:

- allow the current bounded step to complete;
- pause before the next irreversible step;
- abort immediately;
- enter safe state;
- transfer control to another authority;
- invalidate unexecuted authorisations;
- require re-adjudication;
- prevent ratification pending review.

Revocation must not silently rewrite historical authority records.

## Conflicting and distributed authority

Distributed systems may contain multiple competent authorities.

Conflicts may occur across:

- organisations;
- jurisdictions;
- safety and mission authorities;
- system and component owners;
- fleet and local operators;
- human and delegated machine roles;
- technical and legal authority.

A distributed authority model should define:

- precedence;
- quorum;
- veto rights;
- escalation;
- conflict resolution;
- jurisdiction;
- effectivity;
- emergency override;
- deadlock handling;
- record ownership.

Where conflict remains unresolved, the default outcome should be explicit,
such as block, defer, restrict effectivity or enter safe state.

## Authority provenance

Every governance decision should preserve:

- decision identifier;
- authority identity;
- role;
- mandate;
- delegation chain;
- applicable policy;
- effectivity;
- time of decision;
- evidence considered;
- declared conflicts of interest;
- dissent or minority position;
- expiry;
- revocation status;
- signature or integrity protection.

Authority provenance is part of governed continuity.

## Evidence–authority interaction

Evidence and authority interact at adjudication.

A conceptual decision record may bind:

```text
Candidate
+ source baseline
+ evidence package
+ applicable invariants
+ effectivity
+ risk assessment
+ competent authority
+ decision
+ conditions
```

The decision may be:

- ALLOW;
- BLOCK;
- WARN;
- ESCALATE;
- DEFER;
- REVISE;
- SUSPEND;
- AUTHORISE TRIAL;
- AUTHORISE DEPLOYMENT;
- RATIFY;
- DECLINE RATIFICATION;
- AUTHORISE RECOVERY.

The exact vocabulary may be defined by profile or policy.

## Independence and separation of duties

AGES does not require universal organisational independence among all roles.

However, implementations should identify where independence is needed to
avoid:

- self-approval;
- evidence manipulation;
- hidden conflicts of interest;
- circular authority;
- unreviewable autonomous escalation;
- ratification by the same component whose change is being assessed.

Higher-risk profiles may require independent:

- evidence generation;
- validation;
- adjudication;
- deployment;
- closure verification;
- ratification.

The required level of independence should be proportional to risk and
declared by policy.

## Minimal ordering constraints

Evidence and authority must preserve these constraints:

1. Candidate-specific evidence precedes candidate adjudication.
2. Pre-deployment validation evidence precedes controlled-trial
   authorisation.
3. Controlled-trial authority precedes any governed physical or operational
   trial.
4. Trial evidence precedes operational deployment adjudication where a trial
   is required.
5. Operational deployment authority precedes deployment.
6. Deployment evidence and closure evidence precede ratification.
7. A failed or inconclusive deployment does not create a successor baseline.
8. Post-ratification evidence may trigger suspension or a new transition but
   does not erase the prior decision record.

## Key questions

- How should evidence sufficiency vary by risk and effectivity?
- What degree of evidence independence is required?
- When may simulation substitute for a controlled trial?
- How should uncertainty propagate into authorisation conditions?
- What evidence is sufficient to ratify a transition?
- How long may a deployed but unratified configuration remain in probation?
- How do human and delegated machine authority interact?
- Which decisions may be delegated to machines?
- How is authority revoked during an irreversible step?
- How are conflicting distributed authorities resolved?
- May the same actor validate, adjudicate and ratify?
- How should dissenting evidence be preserved?
- How should emergency authority be bounded and reviewed?
- Which authority may approve compensation or a recovery baseline?
- How are expired or superseded authorisations represented?

## Unresolved issues

- Authority revocation during an active or irreversible transition;
- conflicting distributed authorities;
- quorum and veto semantics;
- evidentiary thresholds across heterogeneous domains;
- independence requirements for low-risk and high-risk profiles;
- long-running probation authority;
- machine-generated evidence evaluated by machine authority;
- treatment of compromised evidence sources;
- cross-jurisdictional authority;
- post-event reconstruction when emergency action precedes complete
  recording.

## Related

- [`01-architectural-planes.md`](01-architectural-planes.md)
- [`02-state-and-transition-model.md`](02-state-and-transition-model.md)
- [`04-effectivity.md`](04-effectivity.md)
- [`06-GENTILE.md`](06-GENTILE.md)
- [`07-GTL.md`](07-GTL.md)
- [`08-gentile-gtl-integration.md`](08-gentile-gtl-integration.md)
- [`../theory/05-governed-continuity.md`](../theory/05-governed-continuity.md)
- [`../models/transition-model.md`](../models/transition-model.md)
