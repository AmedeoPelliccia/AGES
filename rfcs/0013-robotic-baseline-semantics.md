<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0013 — Robotic Baseline Semantics

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes semantics for robotic baselines as hardware–software
co-baselines: canonical configurations spanning physical configuration,
electronic configuration, firmware, software, models, calibration,
safety constraints, authority configuration and environmental
assumptions.

## Motivation

A model checkpoint or software version alone is not the identity of a
complete machine. Robotic governance requires a baseline notion that
includes the identity-relevant physical and authority configuration
without attempting to capture the complete physical world.

## Proposal

* Define the co-baseline groups sketched in
  [`../models/hardware-software-co-baseline-model.md`](../models/hardware-software-co-baseline-model.md).
* Define baseline-impact criteria: identity relevance, safety
  relevance, invariant impact, effectivity, change classification and
  authority policy. Not every hardware replacement, parameter
  adjustment or calibration update creates a new age.
* Distinguish configuration identity, operational state, physical world
  state and evolutionary history
  ([`../profiles/AGES-CPS/02-robotic-system-identity.md`](../profiles/AGES-CPS/02-robotic-system-identity.md)).
* Provide the illustrative schema
  [`../schemas/examples/robotic-baseline.example.yaml`](../schemas/examples/robotic-baseline.example.yaml)
  as a non-normative starting point.

## Open questions

Which physical properties belong to configuration identity; how wear
and degradation are represented; how hardware replacement affects
identity; whether physically different robots may share a logical
baseline.

## Status

Draft. Not accepted.
