<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GTL — Action-Candidate Model

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Summarise the model of the grounded action candidate that GTL
produces. The full treatment is
[`../../architecture/07-GTL.md`](../../architecture/07-GTL.md); the handoff
contract is
[`../../contracts/action-candidate.md`](../../contracts/action-candidate.md).

## 1. Core binding structure

A candidate binds, at minimum:

```text
executor
    performs transitive operation
        upon direct object
            within operational context
                under preconditions · limits · invariants
                    with expected effects · failure semantics ·
                         recovery provisions · closure-evidence criteria
```

Transitivity is the load-bearing property: an operation without an identified
direct object is not groundable, and therefore not a candidate.

## 2. Candidate, not command

A candidate is technically executable and deliberately unauthorised:

```text
ActionCandidate
≠ validated candidate
≠ trial-authorised action
≠ operationally authorised action
≠ completed deployment
≠ ratified baseline
```

Candidate sets are legitimate: GTL may emit alternatives with different
trade-offs, and adjudication — not the engine — selects among them.

## 3. Operational and evolutionary effects

The model carries enough information for the governance boundary to classify
the candidate's effect:

- **operational** — acts within the active baseline and delegated envelope;
- **evolutionary** — would modify baseline-controlled configuration, and so
  proceeds as a candidate change through the evolutionary lifecycle
  ([`../../toolchains/cognitive-action-chain.md`](../../toolchains/cognitive-action-chain.md)).

The classification itself is a governance act, made against the active
baseline and declared policy.

## 4. Illustrative rendering

A non-normative YAML rendering is provided in
[`../../schemas/examples/gtl-action-candidate.example.yaml`](../../schemas/examples/gtl-action-candidate.example.yaml);
a robotic variant is
[`../../schemas/examples/robotic-action-candidate.example.yaml`](../../schemas/examples/robotic-action-candidate.example.yaml).
