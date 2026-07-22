<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Hardware–Software Co-Baselines

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Definition

A robotic baseline is a possible **hardware–software co-baseline**: a
single canonical configuration identity spanning the relevant physical
configuration, electronic configuration, firmware, software, models,
calibration, safety constraints, authority configuration and
environmental assumptions of the machine.

The co-baseline records what is *identity-relevant*, not everything
that is physically true of the machine. An illustrative, non-normative
schema is provided in
[`../../schemas/examples/robotic-baseline.example.yaml`](../../schemas/examples/robotic-baseline.example.yaml).

## 2. Baseline impact

Not every hardware replacement, parameter adjustment or calibration
update necessarily creates a new age. Whether a change is
baseline-relevant depends on:

* **identity relevance** — does the change alter what the machine is
  declared to be?
* **safety relevance** — does the change affect safety-relevant
  configuration?
* **invariant impact** — could the change violate or redefine a
  declared invariant?
* **effectivity** — to which instances, contexts or lifecycle stages
  does the change apply?
* **change classification** — the class assigned to the candidate
  change during intent classification;
* **authority policy** — what the governing authority has declared to
  require evolution governance.

A like-for-like replacement of a worn part with an identical, qualified
part under an authorised maintenance policy may remain an operational
action; the substitution of a sensor with a different model, a change
to a safety envelope, or the replacement of a perception model are
candidates for evolution governance.

## 3. Related material

[`../../models/hardware-software-co-baseline-model.md`](../../models/hardware-software-co-baseline-model.md) ·
[`../../theory/03-baselines-and-ages.md`](../../theory/03-baselines-and-ages.md) ·
[`../../rfcs/0013-robotic-baseline-semantics.md`](../../rfcs/0013-robotic-baseline-semantics.md).
