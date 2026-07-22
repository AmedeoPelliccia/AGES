<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Evolution Transitions

**Status:** Exploratory · **Document class:** Foundational · **Repository:** AGES
**Purpose.** Distinguish candidates from transitions, and deployment
from ratification.

**Candidate change.** A proposed modification that may produce a
successor baseline. A candidate is not yet a transition: it may be
rejected, blocked, revised, withdrawn, validated but not authorised,
authorised but not deployed, deployed but not ratified, or reverted
before ratification.

**Evolution transition.** The completed and ratified event through which
the canonical configuration changes:

$$
B_n \xrightarrow{T_n} B_{n+1}
$$

The transition is the arrow — not the proposal, not the evidence
package, not the authorisation record.

**Deployment is not ratification.** A deployed configuration becomes
canonical only when ratified. A failed deployment must not create a new
baseline. Between deployment and ratification lies a probation window in
which monitoring informs the ratification decision
([`../models/transition-model.md`](../models/transition-model.md)).

**Key questions.** What evidence is sufficient to ratify? Who may
operate, and for how long, a deployed but unratified configuration?

**Unresolved issues.** Ratification of physically irreversible
transitions; atomicity of multi-component transitions.

**Related.** [`03-baselines-and-ages.md`](03-baselines-and-ages.md) ·
[`../architecture/02-state-and-transition-model.md`](../architecture/02-state-and-transition-model.md)
