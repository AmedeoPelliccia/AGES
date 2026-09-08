<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GENIUSS — Semantic Model

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Summarise the model of the semantic structure that GENIUSS
produces. The full treatment is
[`../../architecture/12-GENIUSS.md`](../../architecture/12-GENIUSS.md); the
handoff contract is
[`../../contracts/semantic-context.md`](../../contracts/semantic-context.md).

## 1. Abstract structure

$$
\Sigma(t) = \langle V,\ E,\ R,\ A,\ C,\ H,\ T \rangle
$$

Where:

- $V$ — entities, events and concepts;
- $E$ — relations between them;
- $R$ — semantic or functional roles;
- $A$ — attributes and properties;
- $C$ — confidence and uncertainty;
- $H$ — contextual hypotheses;
- $T$ — temporal and state information.

This is a conceptual contract, not a mandatory implementation schema. *Graph*
names the architectural shape of the output, not a storage technology,
query language or ontology.

## 2. Recursive interpretation

Interpretation at $t$ may be conditioned by the semantic state at $t-1$:

$$
\Sigma(t) = F_G\big(X(t),\ \Sigma(t-1),\ C(t)\big)
$$

Prior semantic state may condition interpretation — never governance.

## 3. Semantic levels

Elements of the structure are labelled by level, and levels must not
collapse:

```text
observation ≠ inference ≠ hypothesis ≠ assertion
```

Competing hypotheses, including an explicit *unknown*, remain representable
and inspectable downstream
([`../../contracts/confidence-model.md`](../../contracts/confidence-model.md)).

## 4. Illustrative rendering

A non-normative YAML rendering is provided in
[`../../schemas/examples/geniuss-semantic-structure.example.yaml`](../../schemas/examples/geniuss-semantic-structure.example.yaml).
Where a semantic representation already exists in a profile or deployment,
GENIUSS should extend or map to it rather than introduce a competing model.
