<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0012 — AGES-CPS: AGES Profile for Cyber-Physical and Robotic Systems

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes AGES-CPS as an exploratory application profile of
AGES for cyber-physical and robotic systems. AGES remains the general
engineering paradigm; AGES-CPS specialises its vocabulary, models and
lifecycle to systems whose changes have physical consequences.

## Motivation

Robotic systems combine hardware, firmware, software, models,
calibration, learned policies, safety envelopes and delegated
authority. No single artefact version captures the identity of the
complete machine, and updates may carry physical risk. A domain profile
is needed to state how baselines, transitions, evidence, effectivity
and authority apply to such systems without altering the AGES core.

## Proposal

Adopt the profile documented under
[`../profiles/AGES-CPS/`](../profiles/AGES-CPS/README.md), comprising:
scope and positioning, robotic system identity, hardware–software
co-baselines, multi-rate autonomy, delegated operational envelopes,
GENTILE and GTL for robotics, physical invariants, irreversibility and
recovery, digital–physical closure evidence, fleet effectivity and
middleware integration.

## Non-goals

AGES-CPS is not a robotics middleware, a real-time operating system, a
controller, a motion planner, a perception framework, a replacement for
ROS 2, or a safety or certification standard. It introduces no parent
paradigm above AGES, and robotics is not the exclusive AGES domain.

## Compatibility

The profile preserves all core AGES concepts and the lifecycle order
unchanged. Operational actions that do not change canonical
configuration identity do not create a new age.

## Open questions

See the AGES-CPS section of
[`../research/open-questions.md`](../research/open-questions.md).

## Status

Draft. Not accepted. Terminology and structure are expected to change
through the RFC process
([`0000-rfc-process.md`](0000-rfc-process.md)).
