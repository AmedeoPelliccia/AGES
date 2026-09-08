<!-- ages:authored — informative. This document does not define conformance requirements. -->

# GENTILE — Intent Model

**Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

**Purpose.** Summarise the model of the negotiated-intent artefact that
GENTILE produces. The full treatment is
[`../../architecture/06-GENTILE.md`](../../architecture/06-GENTILE.md); the
handoff contract is
[`../../contracts/intent-artefact.md`](../../contracts/intent-artefact.md).

## 1. Co-constructive cycle

The artefact is the outcome of an iterative exchange:

```text
declared intent
→ elicitation and clarification
→ proposal of structure
→ review and correction
→ negotiated agreement or declared disagreement
→ structured artefact with semantic closure
```

Semantic closure means the artefact is sufficiently explicit, structured and
reviewed to support classification, validation or downstream
operationalisation — while preserving declared uncertainty and unresolved
issues.

## 2. Artefact classes

An `IntentArtefact` declares its class, for example:

- operational request;
- evolutionary intent;
- requirement;
- evidentiary statement;
- governance request.

Classification is what routes the artefact: operational uses need not create
a baseline change, while an evolutionary artefact may — after governance
classification and registration — become a candidate change
([`../../architecture/02-state-and-transition-model.md`](../../architecture/02-state-and-transition-model.md)).

## 3. Content model

The artefact should carry: the intended state or objective; participants;
context and assumptions; constraints; acceptance criteria; unresolved
ambiguity; rejected interpretations; confidence where agreement is partial;
and the provenance of the exchange
([`../../contracts/provenance-envelope.md`](../../contracts/provenance-envelope.md)).

## 4. Illustrative rendering

A non-normative YAML rendering is provided in
[`../../schemas/examples/gentile-artefact.example.yaml`](../../schemas/examples/gentile-artefact.example.yaml).
