<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GTL — Contract

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** State the input/output contract that makes GTL an independent,
composable functional engine.

## 1. Transformation

$$
F_T : (S,\ \Sigma_t,\ K) \rightarrow \{A_1, \ldots, A_n\}
$$

Where:

- $S$ — a structured semantic or intent artefact (**required**), typically an
  [`IntentArtefact`](../../contracts/intent-artefact.md) or a sufficiently
  grounded [`SemanticContext`](../../contracts/semantic-context.md);
- $\Sigma_t$ — additional grounded context (**optional**);
- $K$ — capability and tool grounding, for example a capability registry of
  executors, operations and limits (**optional**);
- $\{A_1, \ldots, A_n\}$ — a set of grounded
  [`ActionCandidate`](../../contracts/action-candidate.md) artefacts;
  alternatives are legitimate and adjudication chooses among them.

In interface form:

```text
GTL(
    semantic_artefact,
    context?: SemanticContext,
    capability_registry?
) -> ActionCandidate[]
```

## 2. Grounding expectations

Each emitted candidate binds an identified executor and transitive operation
to a direct object, operational context, preconditions, limits, expected
effects, invariants, failure and abort behaviour, recovery provisions,
closure-evidence criteria, effectivity and required authority
([`action-candidate-model.md`](action-candidate-model.md)).

> **No transitive operation without an identified direct object; no grounded
> operation without context, bounds, authority reference and closure
> evidence.**

## 3. Hypotheses are not preconditions

GTL must not treat a hypothesis contained in a consumed artefact as an
established precondition. Where a precondition rests on an inference, the
candidate records the dependency, its confidence and the verification
required before execution
([`../../contracts/confidence-model.md`](../../contracts/confidence-model.md)).

## 4. Independence clauses

- GTL **does not require GENTILE or GENIUSS** and does not know their
  implementations; it consumes conformant artefacts from any producer.
- GTL **is not an executor** and defines no direct path to any actuator;
  execution happens, if at all, through adapters after authorisation.
- The near-invariant of the engine is:

$$
\mathrm{ActionCandidate} \neq \mathrm{AuthorisedAction}
$$

## 5. Non-responsibilities

GTL must not:

- interpret raw heterogeneous input;
- negotiate intent;
- authorise, schedule or execute actions;
- classify its own output as operational or evolutionary for governance
  purposes — that classification belongs to the governance boundary
  ([`../../toolchains/cognitive-action-chain.md`](../../toolchains/cognitive-action-chain.md)).

## Related

- [`action-candidate-model.md`](action-candidate-model.md)
- [`../../architecture/07-GTL.md`](../../architecture/07-GTL.md)
- [`../../toolchains/README.md`](../../toolchains/README.md)
