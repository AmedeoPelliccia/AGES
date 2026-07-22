<!-- ages:authored — informative. This document does not define conformance requirements. -->

# RFC-0017 — Fleet Effectivity

**Status:** Draft · **Document class:** RFC proposal · **Repository:** AGES
**Authors:** AGES contributors · **Created:** 2026-07-22

## Abstract

This RFC proposes fleet and instance effectivity semantics for
AGES-CPS: candidates and baselines scoped to individual robots,
hardware revisions, production batches, facilities, environments,
customers, jurisdictions, task classes, fleet cohorts or complete
fleets.

## Motivation

Robotic fleets mix hardware revisions, calibrations, environments and
regulatory contexts. A single canonical baseline for a whole fleet is
often neither achievable nor desirable, and fleet learning must not be
conflated with fleet-wide deployment authority.

## Proposal

* Distinguish global candidate, fleet candidate, cohort baseline,
  instance baseline and temporary experimental effectivity
  ([`../profiles/AGES-CPS/10-fleet-effectivity.md`](../profiles/AGES-CPS/10-fleet-effectivity.md)).
* Require evidence to account for differences in hardware, sensors,
  calibration, environment, local regulation, degradation and
  operational context across effectivity scopes.
* Support staged ratification with probation windows per cohort, as
  illustrated in
  [`../examples/fleet-model-deployment.md`](../examples/fleet-model-deployment.md).

## Open questions

Whether fleets may maintain multiple valid baselines concurrently; how
cohort membership itself is governed.

## Status

Draft. Not accepted.
