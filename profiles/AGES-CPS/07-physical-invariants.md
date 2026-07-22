<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Physical Invariants

**Status:** Exploratory application profile · **Document class:** Informative · **Repository:** AGES

## 1. Definition

A **physical invariant** is an evolutionary invariant
([`../../theory/06-evolutionary-invariants.md`](../../theory/06-evolutionary-invariants.md))
whose subject matter is a physical property, capability limit or safety
boundary of the machine that must remain true across one or more
classes of transition for declared identity and safety to be preserved.

Illustrative physical invariants include:

* maximum end-effector force and speed near humans;
* stability margins of the platform;
* structural load limits;
* thermal and energy bounds;
* the integrity and independence of emergency stop and safe-state
  functions;
* the continued validity of declared human safety zones.

## 2. Invariants and learned components

Some invariants must remain enforceable independently of learned
components: a perception model or learned policy may inform behaviour,
but the invariants that bound physically hazardous behaviour should not
depend on the correctness of a learned component for their enforcement.
Which invariants must remain independent of learned components is an
open research question
([`../../research/open-questions.md`](../../research/open-questions.md)).

## 3. Invariants across transitions

During adjudication, a candidate change declares which physical
invariants it may affect. Changes affecting safety-relevant invariants
require elevated evidence and authority. Invariant evaluation is a
governance activity of the Evolution Control Plane; invariant
*enforcement* during operation remains a runtime safety function
([`01-scope-and-positioning.md`](01-scope-and-positioning.md)).

## 4. Related material

[`08-irreversibility-and-recovery.md`](08-irreversibility-and-recovery.md) ·
[`../../architecture/03-evidence-and-authority.md`](../../architecture/03-evidence-and-authority.md).
