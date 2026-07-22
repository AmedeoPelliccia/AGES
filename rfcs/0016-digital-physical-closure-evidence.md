<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0016 — Digital–Physical Closure Evidence

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes digital–physical closure evidence: evidence
connecting the authorised action specification, recorded execution and
observed physical result of a cyber-physical action or transition.

## Motivation

Logs and telemetry demonstrate that a system produced data, not that an
authorised action achieved its declared physical outcome inside its
envelope. Ratification of cyber-physical transitions requires evidence
that bridges the digital record and the physical world.

## Proposal

* Adopt the definition and the eight questions that closure evidence
  should establish, as documented in
  [`../profiles/AGES-CPS/09-digital-physical-closure-evidence.md`](../profiles/AGES-CPS/09-digital-physical-closure-evidence.md).
* Recognise evidence sources including actuator feedback, sensor
  measurements, pose estimates, force and torque data, energy
  measurements, deployed artefact identifiers, hardware identity,
  calibration verification, inspection records, safety-zone history,
  operator attestation, digital-twin comparison and post-action tests.
* State explicitly that telemetry volume alone is not evidentiary
  sufficiency.
* Provide the illustrative schema
  [`../schemas/examples/physical-closure-evidence.example.yaml`](../schemas/examples/physical-closure-evidence.example.yaml).

## Open questions

What constitutes sufficient physical closure evidence; what qualifies
digital-twin evidence.

## Status

Draft. Not accepted.
