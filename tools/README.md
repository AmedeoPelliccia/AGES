<!-- ages:seed v0.2.0 — exploratory scaffold; supersede through the RFC process. -->

# tools/ — Deterministic Tooling

**Status:** Exploratory · **Document class:** Process · **Repository:** AGES
Purpose: hold the deterministic repository generator,
`ages_scaffold.py`, which is the single source of truth for this
repository's structure and exploratory seed content. Structural changes
are made in the generator first; `--check` verifies the tree and
`--manifest` emits a SHA-256 record of the seed set. The generator is
copied into this directory alongside this file.
