<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Multi-Rate Autonomy Model

**Status:** Exploratory application profile · **Document class:** Experimental model · **Repository:** AGES

An exploratory timescale model for the AGES-CPS profile
([`../profiles/AGES-CPS/04-multi-rate-autonomy.md`](../profiles/AGES-CPS/04-multi-rate-autonomy.md)).
Conceptual modelling: no universal timing values are prescribed.

$$
\tau_{\mathrm{control}}
\ll
\tau_{\mathrm{operation}}
\ll
\tau_{\mathrm{adaptation}}
\ll
\tau_{\mathrm{governance}}
$$

| Timescale | Activity | Governing structure |
|---|---|---|
| $\tau_{\mathrm{control}}$ | Real-time control, servo loops, reflexive safety | Runtime safety mechanisms; authorised envelope |
| $\tau_{\mathrm{operation}}$ | Task execution, planning, behaviour selection | Active baseline; delegated operational envelope |
| $\tau_{\mathrm{adaptation}}$ | Bounded adaptation, recalibration, learning | Delegated envelope; adaptation ranges |
| $\tau_{\mathrm{governance}}$ | Candidate evaluation, adjudication, ratification | Evolution Control Plane |

The ordering encodes the placement constraint: the Evolution Control
Plane must not normally be placed in the hard real-time control path.
Faster loops operate inside envelopes authorised by slower loops; a
faster loop cannot expand its own envelope — expansion is an
adjudicated change at the governance timescale.

Relation to the core models: this refines the temporal model
([`temporal-model.md`](temporal-model.md)) by distinguishing timescales
*within* a single age, whereas ages themselves succeed one another at
the governance timescale.
