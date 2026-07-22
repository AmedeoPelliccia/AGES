<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Hardware–Software Co-Baseline Model

**Status:** Exploratory application profile · **Document class:** Experimental model · **Repository:** AGES

An exploratory sketch of the robotic co-baseline for the AGES-CPS
profile
([`../profiles/AGES-CPS/03-hardware-software-co-baselines.md`](../profiles/AGES-CPS/03-hardware-software-co-baselines.md)).
Conceptual modelling, not completed mathematics.

A robotic baseline $B_n$ may be sketched as a tuple of
identity-relevant configuration groups:

$$
B_n
=
\left\langle
H,\; F,\; S,\; M,\; K,\; \Sigma,\; A,\; W
\right\rangle
$$

Where, illustratively: $H$ is the physical and electronic
configuration (assemblies, sensors, actuators, computing modules); $F$
is firmware; $S$ is software packages and runtime topology; $M$ is
perception, planning and learned models; $K$ is calibration and
control parameters; $\Sigma$ is safety constraints and envelopes; $A$
is authority configuration, permissions and delegated envelopes; and
$W$ is declared environmental assumptions, maps and world models.

Membership is governed by identity relevance, safety relevance,
invariant impact, effectivity, change classification and authority
policy. Not every hardware replacement, parameter adjustment or
calibration update creates a new age; the model records what the
governing authority declares baseline-controlled.

Illustrative schema:
[`../schemas/examples/robotic-baseline.example.yaml`](../schemas/examples/robotic-baseline.example.yaml).
