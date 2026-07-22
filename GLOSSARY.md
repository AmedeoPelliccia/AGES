<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Glossary

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

Controlled working vocabulary. Changes require an RFC once terms are
accepted ([`GOVERNANCE.md`](GOVERNANCE.md)).

| Term | Working definition |
|---|---|
| Artificial evolutive system | An engineered system whose evolution is representable as identifiable states connected by governed transitions. |
| System baseline | The complete, canonical, uniquely identifiable configuration of the system at a declared point of ratification — not merely a software version or model checkpoint. |
| Whole-system baseline | A canonical, uniquely identifiable configuration that binds the identity-relevant physical, digital, cognitive, policy and authority state of the governed artificial system through immutable references and provenance records. Used interchangeably with *system baseline* when the whole-system scope is being emphasised. |
| Ratification | The lifecycle event through which a verified resulting configuration becomes the canonical successor baseline and opens a new age. |
| Age | The validity interval during which a ratified baseline remains canonical: Age_n = [ratify(B_n), ratify(B_n+1)). |
| Candidate change | A proposed modification that may produce a successor baseline; it may be rejected, blocked, revised, withdrawn, validated but not authorised, authorised but not deployed, deployed but not ratified, or reverted before ratification. |
| Evolution transition | The completed and ratified event through which the canonical configuration changes from one baseline to another — distinct from the proposal, the evidence and the authorisation record. |
| Evolution evidence | Observations, test results, analyses, attestations and trace records used to establish whether a candidate satisfies declared requirements. |
| Evolution authority | Who or what is permitted to propose, validate, adjudicate, authorise, deploy, ratify, suspend or reverse a transition; may be human, organisational, procedural, delegated, automated under prior policy, or distributed. |
| Effectivity | Where, when and to which instances, products, deployments, jurisdictions, operating contexts or lifecycle stages a baseline or transition applies. |
| Evolutionary invariant | A property that must remain true across one or more classes of transition for declared continuity and identity to be preserved. |
| Governed continuity | The verifiable relation connecting two ratified baselines through an authorised, evidence-supported, reconstructable transition. |
| Constitutional version control | An explanatory framing for the AGES model of whole-system identity, in which proposed changes are evaluated against declared authority, evidence, effectivity and invariants before a resulting configuration may be ratified as the successor baseline. An architectural analogy, not a source-control implementation ([`positioning/ages-vs-version-control.md`](positioning/ages-vs-version-control.md)). |
| Artefact revision | A change to one or more tracked digital artefacts, for example a repository commit. An artefact revision does not by itself constitute an AGES evolution transition. |
| Underlying record system | A repository, registry, database, ledger or configuration-management mechanism whose records may be referenced by an AGES baseline without being duplicated by AGES. |
| Probation window | The interval between deployment and ratification, during which monitoring informs the ratification decision. |
| GENTILE | **GENTILE — Generative Engine for Neural Transformation through Interactive Language Exchange.** An interactive and co-constructive transformation engine that converts human or system intent, contextual information and iterative language exchanges into negotiated, structured and machine-interpretable semantic artefacts. A GENTILE artefact may represent an operational request, evolutionary intent, requirement, evidentiary statement, governance request or another formally classified representation. |
| GTL | **GTL — Generative Transitive Language.** A formal or semi-formal language for representing grounded transitive action candidates. A GTL expression binds an identified executor and transitive operation to a direct object, operational context, explicit preconditions, execution limits, expected effects, failure behaviour, recovery provisions and closure-evidence criteria. |
| Semantic artefact | A structured and reviewable representation of intent, context, assumptions, constraints, objectives, unresolved ambiguity and acceptance criteria produced through a semantic transformation process. |
| Semantic closure | The condition in which an artefact is sufficiently explicit, structured and reviewed to support classification, validation or downstream operationalisation, while preserving declared uncertainty and unresolved issues. |
| Grounded action candidate | A bounded and inspectable specification of a proposed operation on an identified physical, computational, informational or organisational object. |
| Closure evidence | Evidence produced during or after execution demonstrating whether the declared postconditions, expected state and operational closure criteria were achieved. |
| Direct object | The identified entity upon which a transitive operation is intended to act. |
| Executor | The human, agent, service, controller, machine or composite system assigned to perform a grounded operation. |
| Operational envelope | The explicit set of contextual, temporal, physical, computational and authority limits within which an action candidate may be executed. |
| AGES-CPS | The proposed, exploratory application profile of AGES for cyber-physical and robotic systems ([`profiles/AGES-CPS/`](profiles/AGES-CPS/README.md)). It specialises AGES vocabulary and lifecycle to systems whose changes have physical consequences; it is not a middleware, controller, planner or safety standard. |
| Robotic baseline | A system baseline for a robotic or cyber-physical system, possibly realised as a hardware–software co-baseline; it records the identity-relevant configuration of the complete machine, not merely a software version or model checkpoint. |
| Hardware–software co-baseline | A single canonical baseline spanning the relevant physical configuration, electronic configuration, firmware, software, models, calibration, safety constraints, authority configuration and environmental assumptions of a machine. |
| Delegated operational envelope | The bounded set of actions, adaptations and runtime decisions that the Operational Plane may perform under prior authority without requesting a new evolutionary authorisation for every decision. Actions inside the envelope do not automatically create a new baseline; a change to the envelope itself may require evolution governance. |
| Physical invariant | An evolutionary invariant whose subject matter is a physical property, capability limit or safety boundary that must remain true across one or more classes of transition for declared identity and safety to be preserved. |
| Digital–physical closure evidence | Evidence connecting the authorised action specification, recorded execution and observed physical result of a cyber-physical action or transition. |
| Compensation | A recovery mode that mitigates or neutralises the effects of an action without recreating the exact prior state; distinct from rollback, safe-state transition and containment. |
| Recovery baseline | A stable configuration ratified after an abnormal or partially irreversible event, re-establishing a governed canonical identity; ratified only after evidence collection and closure verification. |
| Reversibility class | A declared classification of a candidate change or action stating the extent to which its effects can be reversed: for example reversible, partially irreversible or declared irreversible. |
| Fleet effectivity | Effectivity applied at fleet granularity: the scoping of candidates, baselines and transitions to individual robots, hardware revisions, batches, facilities, environments, jurisdictions, task classes, cohorts or complete fleets. |
