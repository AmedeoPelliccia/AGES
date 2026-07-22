<!-- ages:authored — informative. This document does not define conformance requirements. -->

# Example — Bounded Cyber-Physical Action and Safe-State Recovery

**Status:** Exploratory application profile · **Document class:** Example · **Repository:** AGES

A non-normative AGES-CPS example of a bounded cyber-physical action
whose execution deviates, triggering safe-state recovery, compensation
and a proposed recovery baseline
([`../profiles/AGES-CPS/08-irreversibility-and-recovery.md`](../profiles/AGES-CPS/08-irreversibility-and-recovery.md)).

**Bounded action.** A GTL candidate authorises `robot:amr-014` to
transport `asset:container-C-88` to a staging bay, with declared
limits, abort conditions, safe state, compensation strategy and
closure-evidence requirements
([`../schemas/examples/robotic-action-candidate.example.yaml`](../schemas/examples/robotic-action-candidate.example.yaml)).

**Deviation.** During transit, load-cell feedback indicates a payload
shift beyond the declared failure condition. The **independent runtime
safety function** — not the Evolution Control Plane — triggers the
declared safe state: controlled stop, load lowered, alarm raised.
Governance is never in the hard real-time reaction path.

**Evidence.** Digital–physical closure evidence is collected: force
traces, pose history, the deviation event, safe-state entry and the
condition of the container and contents.

**Irreversibility.** Exact physical rollback is impossible: the
container has been partially displaced and its contents disturbed. The
event is assessed as **partially irreversible**. **Compensation** is
applied instead: an operator reseats the contents, the container is
inspected, and the affected route segment is flagged for survey.

**Recovery baseline.** Because the event and its response alter
baseline-controlled configuration (a tightened payload-shift threshold
and a temporary envelope restriction), a **recovery baseline** is
proposed
([`../schemas/examples/recovery-baseline.example.yaml`](../schemas/examples/recovery-baseline.example.yaml)).
It is adjudicated under recovery authority and may be ratified only
after compensation is verified complete and invariants are confirmed to
have held.

**Distinctions exercised.** Rollback, compensation, safe-state
transition and recovery baseline are four different things here: the
safe state bounded the event; compensation mitigated effects that
rollback could not restore; and the recovery baseline re-establishes a
governed canonical identity after the event.

**Related.**
[`gentile-gtl-cyber-physical-action.md`](gentile-gtl-cyber-physical-action.md) ·
[`../schemas/examples/physical-closure-evidence.example.yaml`](../schemas/examples/physical-closure-evidence.example.yaml)
