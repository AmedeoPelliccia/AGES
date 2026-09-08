<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GENIUSS — Contract

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** State the input/output contract that makes GENIUSS an
independent, composable functional engine.

## 1. Transformation

$$
F_G : (X_t,\ \Sigma_{t-1},\ C_t) \rightarrow \Sigma_t
$$

Where:

- $X_t$ — heterogeneous observations and input available at time $t$
  (**required**);
- $\Sigma_{t-1}$ — the prior semantic state (**optional**; enables recursive
  contextual interpretation);
- $C_t$ — current context (**optional**);
- $\Sigma_t$ — the updated semantic structure, emitted as a
  [`SemanticContext`](../../contracts/semantic-context.md).

In interface form:

```text
GENIUSS(
    observations,
    prior?: SemanticContext,
    context?
) -> SemanticContext
```

## 2. Input expectations

Consumed inputs may include natural-language statements, system state,
sensor readings, telemetry, events and logs, perceptual channels, history
and prior semantic structures. Every consumed input should carry, or be
resolvable to, provenance, timestamp and integrity status
([`../../contracts/provenance-envelope.md`](../../contracts/provenance-envelope.md)).

## 3. Output guarantees

The emitted `SemanticContext` preserves:

- explicit entities, relations, roles and attributes;
- confidence, competing hypotheses and declared ambiguity
  ([`../../contracts/confidence-model.md`](../../contracts/confidence-model.md));
- salience and temporal state;
- traceability of every assertion to its source observations.

## 4. Independence clauses

- GENIUSS **does not know that GENTILE or GTL exist.** It emits a conformant
  artefact for any conformant consumer.
- GENIUSS accepts no instruction from downstream engines about what its
  interpretation should be.
- Recursive conditioning on $\Sigma_{t-1}$ is an interpretive mechanism only;
  it does not authorise self-modification of the engine or of the system
  baseline.

## 5. Non-responsibilities

GENIUSS must not:

- negotiate or determine intent;
- produce action candidates;
- authorise or execute anything;
- decide policy;
- convert uncertain interpretation into false certainty;
- create a direct path to any actuator.

## Related

- [`semantic-model.md`](semantic-model.md)
- [`../../architecture/12-GENIUSS.md`](../../architecture/12-GENIUSS.md)
- [`../../toolchains/README.md`](../../toolchains/README.md)
