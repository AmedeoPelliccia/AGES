<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Glossary

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

Controlled working vocabulary. Changes require an RFC once terms are
accepted ([`GOVERNANCE.md`](GOVERNANCE.md)).

| Term | Working definition |
|---|---|
| Artificial evolutive system | An engineered system whose evolution is representable as identifiable states connected by governed transitions. |
| System baseline | The complete, canonical, uniquely identifiable configuration of the system at a declared point of ratification — not merely a software version or model checkpoint. |
| Ratification | The lifecycle event by which a deployed candidate configuration becomes the canonical baseline. |
| Age | The validity interval during which a ratified baseline remains canonical: Age_n = [ratify(B_n), ratify(B_n+1)). |
| Candidate change | A proposed modification that may produce a successor baseline; it may be rejected, blocked, revised, withdrawn, validated but not authorised, authorised but not deployed, deployed but not ratified, or reverted before ratification. |
| Evolution transition | The completed and ratified event through which the canonical configuration changes from one baseline to another — distinct from the proposal, the evidence and the authorisation record. |
| Evolution evidence | Observations, test results, analyses, attestations and trace records used to establish whether a candidate satisfies declared requirements. |
| Evolution authority | Who or what is permitted to propose, validate, adjudicate, authorise, deploy, ratify, suspend or reverse a transition; may be human, organisational, procedural, delegated, automated under prior policy, or distributed. |
| Effectivity | Where, when and to which instances, products, deployments, jurisdictions, operating contexts or lifecycle stages a baseline or transition applies. |
| Evolutionary invariant | A property that must remain true across one or more classes of transition for declared continuity and identity to be preserved. |
| Governed continuity | The verifiable relation connecting two ratified baselines through an authorised, evidence-supported, reconstructable transition. |
| Probation window | The interval between deployment and ratification, during which monitoring informs the ratification decision. |
