<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# Evolutionary Invariants

**Status:** Exploratory · **Document class:** Foundational · **Repository:** AGES
**Purpose.** Define what must not change for identity to survive change.

**Definition.** An evolutionary invariant is a property that must remain
true across one or more classes of transition for the system to preserve
declared continuity and identity. Examples: identity anchors, safety
constraints, constitutional policies, interface contracts, data-integrity
requirements, authority boundaries, rollback guarantees, traceability
requirements.

**Classes.** Constitutive invariants (their violation breaks identity)
versus replaceable invariants (they may be superseded by governed
transition of the invariant set itself).

**Key questions.** Which invariants are constitutive and which are
replaceable? Who governs changes to the invariant set?

**Unresolved issues.** Invariants across branches; meta-invariants
(invariants about how invariants change).

**Related.** [`02-system-identity.md`](02-system-identity.md) ·
[`../architecture/03-evidence-and-authority.md`](../architecture/03-evidence-and-authority.md)
