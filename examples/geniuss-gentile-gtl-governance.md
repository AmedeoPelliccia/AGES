<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — From Heterogeneous Input to Governance Decision (GENIUSS · GENTILE · GTL · AGES)

**Status:** Exploratory · **Document class:** Example · **Repository:** AGES
A neutral aerospace test-platform scenario showing four distinct
transformations: [GENIUSS](../architecture/12-GENIUSS.md) interprets,
[GENTILE](../architecture/06-GENTILE.md) negotiates intent,
[GTL](../architecture/07-GTL.md) grounds an action candidate, and AGES
adjudicates. Each engine performs a different transformation; none of
them may substitute for another.

1. **Heterogeneous input.** During a high-altitude test campaign, a
   thermocouple reports a bay-3 bearing temperature of 92 °C rising at
   0.8 °C/min, vibration telemetry remains nominal, the test conductor
   messages "Bay 3 feels hot again, same as last week", and a
   maintenance closure record shows the thermocouple was recalibrated
   the previous week.
2. **GENIUSS semantic integration — what does it mean in context?**
   GENIUSS integrates the four channels with the prior semantic state
   into a contextualised semantic structure: entities (bearing
   assembly, thermocouple), relations (the sensor measures the
   bearing), salience, temporal context and competing hypotheses —
   bearing overheating (0.71), thermocouple calibration anomaly (0.24),
   unknown (0.05) — with the phrase "same as last week" retained as an
   unresolved ambiguity
   ([`../schemas/examples/geniuss-semantic-structure.example.yaml`](../schemas/examples/geniuss-semantic-structure.example.yaml)).
   GENIUSS asserts no intent, proposes no operation and authorises
   nothing; the interpretation is an inference, not a fact.
3. **GENTILE intent formalisation — what is intended?** Using that
   structure as grounding context, GENTILE negotiates with the test
   conductor what outcome is desired: not "fix the bearing", but
   "establish whether the thermal reading is genuine before the next
   ascent, without aborting the campaign". The exchange resolves the
   ambiguity flagged by GENIUSS — the conductor confirms the reference
   to the earlier maintenance event — and records the rejected broader
   interpretation ("shut down bay 3"). The result is a negotiated
   semantic artefact classified as operational intent, carrying
   acceptance criteria, constraints, effectivity and authority claims
   ([`../schemas/examples/gentile-artefact.example.yaml`](../schemas/examples/gentile-artefact.example.yaml)).
4. **GTL grounding — what operation could realise it?** GTL produces
   grounded, not-yet-authorised action candidates: a cross-check of
   bay-3 temperature against redundant thermocouple TC-08 under the
   current baseline, and, as an alternative candidate, a reduced-power
   hold pending confirmation. Each candidate binds executor,
   transitive operation, direct object, preconditions, operational
   limits, expected effects, abort conditions, recovery provisions and
   closure-evidence criteria. Because the bearing-overheating
   precondition rests on a GENIUSS **hypothesis**, the candidate
   records that dependency, its confidence and the verification
   required before execution
   ([`../schemas/examples/gtl-action-candidate.example.yaml`](../schemas/examples/gtl-action-candidate.example.yaml)).
5. **AGES governance — may it proceed?** The Evolution Control Plane
   evaluates the candidates against policy, physical invariants,
   delegated operational envelope, effectivity and authority. The
   cross-check candidate falls inside the delegated maintenance
   envelope and is authorised; the reduced-power hold affects the
   campaign profile and is escalated to the campaign authority. Neither
   the interpretation nor the negotiated intent conferred any
   authority: technical executability is not permission to execute.
6. **Closure and traceability.** Execution produces closure evidence,
   and the chain remains reconstructable end to end: source
   observations → semantic assertion → negotiated intent → action
   candidate → governance decision → closure evidence. A reviewer can
   ask why the system believed the bay was overheating and reach the
   original thermocouple reading, its confidence and the competing
   calibration hypothesis
   ([`../schemas/examples/closure-evidence.example.yaml`](../schemas/examples/closure-evidence.example.yaml)).
7. **No new baseline.** The cross-check runs under the current ratified
   baseline; no candidate change is formed and no age is opened. Had
   the calibration hypothesis been confirmed and a recalibration
   procedure changed, the resulting configuration change would have
   entered the evolutionary lifecycle instead.

**Related.**
[`../architecture/12-GENIUSS.md`](../architecture/12-GENIUSS.md) ·
[`../architecture/08-gentile-gtl-integration.md`](../architecture/08-gentile-gtl-integration.md)
