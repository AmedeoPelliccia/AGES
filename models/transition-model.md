<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Transition Model

**Status:** Exploratory · **Document class:** Experimental model · **Repository:** AGES
**Purpose.** Model the two monitoring windows around ratification.

$$
B_n \xrightarrow{T_n} B_{n+1}
$$

A transition passes through a **probation window** — the interval between
deployment and ratification — in which monitoring evidence informs the
ratification decision, and reversal produces no new baseline. After
ratification, **operational monitoring** continues under the new age;
anomalies there trigger governed rollback or suspension, which are
themselves transitions (or policy-authorised recovery actions), never
silent reversions.

Two windows, two consequences: reversal before ratification erases a
candidate; rollback after ratification opens a new age.

**Key question.** Who authorises, and for how long, the operation of a
deployed but unratified configuration?
