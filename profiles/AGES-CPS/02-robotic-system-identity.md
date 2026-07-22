<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Robotic System Identity

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Conceptual expression

As an exploratory conceptual model — not a complete mathematical
theory — the governed identity of a robotic system at time $t$ may be
sketched as:

$$
\mathrm{RobotIdentity}(t)
=
\left\langle
B_n,\;
\mathcal{T}_{0:n},\;
\mathcal{I}_n,\;
E_f,\;
P_n
\right\rangle
$$

Where:

* $B_n$ is the active canonical baseline;
* $\mathcal{T}_{0:n}$ is the ratified transition history;
* $\mathcal{I}_n$ is the applicable invariant set;
* $E_f$ is active effectivity;
* $P_n$ is the relevant physical-state and provenance record.

## 2. Distinctions

Four notions must be kept distinct:

| Notion | Meaning |
|---|---|
| Configuration identity | The canonical, ratified baseline: what the machine is declared and governed to be |
| Operational state | The current runtime condition: pose, velocity, task progress, loaded plans |
| Physical world state | The condition of the environment and workpieces the machine interacts with |
| Evolutionary history | The ratified succession of baselines and transitions across the machine's life |

Configuration identity is governed by AGES objects. Operational state
changes continuously under the active baseline without creating new
ages. Physical world state is observed, recorded where relevant, and
never fully captured: a baseline does not attempt to include or hash
the complete physical world. Evolutionary history is what makes the
machine's identity reconstructable rather than merely current.

## 3. The physical-state and provenance record

$P_n$ records the *relevant* physical facts for governance —
installed hardware identities, calibration references, wear or
degradation indicators declared identity-relevant, and provenance of
physical interventions — not the full state of the machine or its
environment. Which physical properties belong to configuration
identity is an open research question
([`../../research/open-questions.md`](../../research/open-questions.md)).

## 4. Related material

[`../../models/robotic-identity-model.md`](../../models/robotic-identity-model.md) ·
[`../../theory/02-system-identity.md`](../../theory/02-system-identity.md) ·
[`03-hardware-software-co-baselines.md`](03-hardware-software-co-baselines.md).
