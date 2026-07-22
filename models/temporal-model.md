<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Temporal Model

**Status:** Exploratory · **Document class:** Experimental model · **Repository:** AGES
**Purpose.** Model system time as a sequence of ages.

$$
\text{Age}_n = [\, \mathrm{ratify}(B_n),\ \mathrm{ratify}(B_{n+1}) \,)
$$

The timeline is a half-open partition: every instant after genesis
belongs to exactly one age per effectivity scope; the current age is
right-open. Ratification events are the only age boundaries — deployment
events are not.

**Unresolved issues.** Concurrent ages under disjoint effectivities;
multiple asynchronous evolutionary timelines within one system
([`../research/open-questions.md`](../research/open-questions.md)).
