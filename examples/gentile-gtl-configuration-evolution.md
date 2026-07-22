<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — AI Configuration Evolution through GENTILE and GTL

**Status:** Exploratory · **Document class:** Example · **Repository:** AGES
A human or system proposes improving the robustness of an AI-centred
assistant in a declared operational context. This worked example shows
the **evolutionary** case: the sequence ends in the ratification of a
successor baseline and the opening of a new age
([`../theory/03-baselines-and-ages.md`](../theory/03-baselines-and-ages.md)).

1. **Intent.** "The assistant misclassifies noisy sensor summaries in
   the offshore deployment; make it more robust there."
2. **GENTILE co-construction.** GENTILE converts the broad objective
   into a negotiated semantic artefact: the affected components are
   identified (the summarisation adapter and its retrieval index), the
   invariants are declared (no change to permissions, tools or safety
   policies), the evaluation criteria are agreed (misclassification
   rate below a stated threshold on a declared benchmark, no regression
   on the reference suite), and unresolved ambiguity is recorded.
3. **Classification.** The artefact is classified as **evolutionary
   intent** with potential baseline impact.
4. **Candidate change.** A candidate change is formed from the
   artefact, carrying its rationale, declared invariants and
   acceptance criteria ([`../GLOSSARY.md`](../GLOSSARY.md)).
5. **GTL grounding.** GTL generates one or more deployment **action
   candidates**: for example, deploy the retuned adapter to the
   offshore probationary scope, with executor (deployment service),
   direct object (the adapter configuration of the named instance),
   preconditions, limits, abort conditions, rollback target (the
   current baseline `B_n`) and closure-evidence criteria.
6. **Validation execution.** The Evolution Plane runs the declared
   validation suites and produces the validation record. Validation
   execution precedes adjudication.
7. **Governance adjudication.** The Evolution Control Plane receives
   both the semantic artefact and the executable action candidate with
   its validation record, adjudicates evidence, authority, policy and
   effectivity, and issues ALLOW.
8. **Authorised deployment.** The deployment executes within the
   authorised envelope and probationary scope. Authorisation precedes
   execution; deployment precedes ratification.
9. **Closure evidence.** Monitoring during the probation window
   produces closure evidence demonstrating the acceptance criteria and
   invariants hold.
10. **Ratification of the successor baseline.** Only after successful
    execution and closure verification is the successor baseline
    ratified, opening a new age of the assistant:

$$
B_n
\xrightarrow{A_c,\;V,\;D,\;E_c}
B_{n+1}
$$

**Related.**
[`ai-centred-system.md`](ai-centred-system.md) ·
[`../architecture/08-gentile-gtl-integration.md`](../architecture/08-gentile-gtl-integration.md)
