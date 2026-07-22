<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Example — Cyber-Physical System

**Status:** Exploratory · **Document class:** Example · **Repository:** AGES
An industrial plant controller evolves through firmware, control-logic
and safety-parameter changes. Governed continuity requires that every
ratified controller configuration be identifiable and reconstructable,
that safety constraints act as constitutive invariants, and that
rollback targets remain executable while a configuration is live —
with physically irreversible actions (for example, recalibration that
consumes a reference standard) explicitly declared as such.

The probation window is natural here: a new control configuration runs
under supervision before ratification, and reversal during probation
produces no new baseline.

**Related.** [`../models/transition-model.md`](../models/transition-model.md)
