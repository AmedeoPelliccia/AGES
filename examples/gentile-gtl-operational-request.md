<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — Operational Request through GENTILE and GTL (No Baseline Change)

**Status:** Exploratory · **Document class:** Example · **Repository:** AGES
A human asks an autonomous maintenance assistant to inspect a component.
This worked example shows an **operational** use of
[GENTILE](../architecture/06-GENTILE.md) and
[GTL](../architecture/07-GTL.md): the action is authorised, executed and
closed under the current ratified baseline, and **no new system baseline
is created**.

1. **Intent.** The operator states: "Have a look at the heat exchanger
   in unit 2 — I think the surface is corroding."
2. **GENTILE co-construction.** Through iterative exchange, GENTILE
   clarifies which component is meant (HX-204, not all exchangers in
   unit 2 — the broader interpretation is recorded as rejected), the
   inspection purpose (surface-condition assessment before overhaul),
   the limits (visual and ultrasonic only, no disassembly) and the
   acceptance criteria (a surface-condition report with photographic
   and thickness evidence).
3. **Classification.** The negotiated semantic artefact is classified
   as **operational intent** with no evolutionary or baseline impact
   ([`../schemas/examples/gentile-artefact.example.yaml`](../schemas/examples/gentile-artefact.example.yaml)).
4. **GTL grounding.** GTL generates an inspection **action candidate**
   binding the executor (an inspection crawler), the direct object
   (HX-204), the operational context, explicit preconditions
   (depressurised, lockout–tagout active), limits, abort conditions,
   a safe state and closure-evidence criteria
   ([`../schemas/examples/gtl-action-candidate.example.yaml`](../schemas/examples/gtl-action-candidate.example.yaml)).
5. **Validation and authorisation.** Validation execution checks the
   candidate against policy and the operational envelope; adjudication
   then confirms the delegated maintenance authority covers the
   operation, and the action is authorised. Authorisation precedes
   execution.
6. **Execution and closure evidence.** The crawler performs the
   inspection within its limits; closure evidence (report, coverage
   map, supervisor attestation) demonstrates the declared
   postconditions were achieved
   ([`../schemas/examples/closure-evidence.example.yaml`](../schemas/examples/closure-evidence.example.yaml)).
7. **No new baseline.** The system configuration is unchanged. No
   candidate change was formed, no ratification occurs, and the current
   age remains open.

**Related.**
[`../architecture/08-gentile-gtl-integration.md`](../architecture/08-gentile-gtl-integration.md)
