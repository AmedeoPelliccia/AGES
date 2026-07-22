<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Baselines and Ages

**Status:** Exploratory · **Document class:** Foundational · **Repository:** AGES
**Purpose.** Define the paradigm's two temporal primitives.

**System baseline.** The complete, canonical and uniquely identifiable
configuration of the system at a declared point of ratification. It may
include executable components, models, parameters, memory, knowledge,
interfaces, tools, policies, permissions, infrastructure dependencies,
schemas, configuration data, safety constraints, authority assignments
and effectivity declarations. A baseline is not merely a software
version or model checkpoint: it is the configuration identity of the
whole governed system. Notation: B₀, B₁, …, Bₙ.

**Age.** The validity interval during which a ratified baseline remains
canonical:

$$
\text{Age}_n = [\, \mathrm{ratify}(B_n),\ \mathrm{ratify}(B_{n+1}) \,)
$$

The active age remains open until a successor is ratified. Baseline
(configuration identity), ratification (lifecycle event) and age
(validity interval) are three distinct concepts.

**Key questions.** When does an update create a new age rather than a
minor revision? Can multiple baselines coexist under different
effectivities?

**Unresolved issues.** Granularity thresholds; concurrent ages.

**Related.** [`04-evolution-transitions.md`](04-evolution-transitions.md)
· [`../models/temporal-model.md`](../models/temporal-model.md) ·
[`../positioning/ages-vs-version-control.md`](../positioning/ages-vs-version-control.md)
(how a whole-system baseline relates to commits and checkpoints)
