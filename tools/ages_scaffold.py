#!/usr/bin/env python3
"""
ages_scaffold.py — deterministic repository generator for AGES.

    AGES — Artificial General Evolutive Systems
    An open engineering paradigm for artificial systems that evolve
    through governed, traceable and reconstructable states.

This generator is the single source of truth for the AGES repository
structure and its exploratory seed content. Same guarantees as the
SAI-AUT-OS scaffold: deterministic (no clocks, no randomness), idempotent,
non-destructive without --force, self-verifying via --check and --manifest.

Usage:
    python tools/ages_scaffold.py [--root PATH] [--force] [--check]
                                  [--verify] [--manifest PATH] [--list]

Exit codes: 0 = OK · 1 = check/verify failed · 2 = usage error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import textwrap
from pathlib import Path

AGES_VERSION = "0.2.0"
FILES: dict[str, str] = {}

SEED = "<!-- ages:seed v@V@ — exploratory scaffold; supersede through the RFC process. -->"
AUTHORED = "<!-- ages:authored — informative. This document does not define conformance requirements. -->"


def T(s: str) -> str:
    return textwrap.dedent(s).strip("\n") + "\n"


def add(rel: str, content: str) -> None:
    if rel in FILES:
        raise ValueError(f"duplicate path: {rel}")
    FILES[rel] = content.replace("@V@", AGES_VERSION)


def doc(rel: str, cls: str, title: str, body: str, authored: bool = False) -> None:
    head = AUTHORED if authored else SEED
    add(rel, T(f"""
        {head}

        # {title}

        **Status:** Exploratory · **Document class:** {cls} · **Repository:** AGES

        """) + T(body))


# ============================================================================
# Root
# ============================================================================

add("README.md", T("""
    """ + SEED + """

    # AGES — Artificial General Evolutive Systems

    > An open engineering paradigm for artificial systems that evolve through
    > governed, traceable and reconstructable states.

    **Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

    ## 1. Overview

    AGES studies artificial engineered systems whose identity extends across
    multiple governed configurations. Such a system is not defined by a single
    configuration: it is defined by the continuity that connects its ratified
    configurations across time — a continuity that is authorised, evidenced
    and reconstructable.

    ## 2. Why AGES

    Existing concepts are each insufficient to describe the complete lifecycle
    identity of a system that may modify its capabilities, knowledge, tools,
    policies and infrastructures. A *software version* captures code but not
    memory, knowledge or authority. A *model checkpoint* captures parameters
    but not the surrounding cognitive configuration. An *adaptive system*
    changes, but its changes need not be identifiable states. An *autonomous
    agent* acts, but action is not evolution. *Continuous deployment* moves
    artefacts without establishing configuration identity. A *self-learning
    system* accumulates change without necessarily preserving reconstructable
    continuity. AGES names what these concepts miss: the governed succession
    of complete system states.

    ## 3. Foundational proposition

    > An artificial evolutive system is not a photograph of one
    > configuration. It is the governed continuity of its ratified states.

    ## 4. What "General" means

    *General* qualifies the applicability of the evolutive paradigm across
    different classes of artificial systems. It does not claim human-level
    general intelligence, universal capability or AGI.

    ## 5. What "Artificial" means

    AGES concerns systems resulting from human design, engineering,
    manufacture, programming or institutional construction. Natural
    biological evolution is outside the project's primary scope.

    ## 6. What "Evolutive" means

    *Evolutive* is stronger than adaptive or changeable. Evolution, in this
    paradigm, must involve identifiable states and reconstructable
    transitions. A system does not qualify merely because it changes, learns,
    updates or adapts.

    ## 7. Core conceptual model

    | Object | Definition |
    |---|---|
    | Baseline | The complete, canonical, uniquely identifiable configuration of the system at a declared point of ratification. |
    | Age | The validity interval during which a ratified baseline remains the canonical identity of the system. |
    | Candidate change | A proposed modification that may — or may not — produce a successor baseline. |
    | Evolution transition | The completed, ratified event through which the canonical configuration changes from one baseline to another. |
    | Evidence | Observations, test results, analyses, attestations and trace records supporting or opposing a candidate. |
    | Authority | Who or what may propose, validate, adjudicate, authorise, deploy, ratify, suspend or reverse a transition. |
    | Effectivity | Where, when and to which instances, jurisdictions, contexts or lifecycle stages a baseline or transition applies. |
    | Invariant | A property that must remain true across one or more transition classes for identity to be preserved. |
    | Governed continuity | The verifiable relation connecting two ratified baselines through an authorised, evidence-supported, reconstructable transition. |

    Full definitions: [`GLOSSARY.md`](GLOSSARY.md) and
    [`theory/`](theory/README.md).

    ## 8. Baselines, ages and transitions

    ```mermaid
    flowchart LR
        B0[Baseline B0] -->|Transition T0| B1[Baseline B1]
        B1 -->|Transition T1| B2[Baseline B2]
    ```

    Each ratified baseline opens a new age and remains the canonical identity
    of the system until the next baseline is ratified:

    $$
    \\text{Age}_n = [\\, \\mathrm{ratify}(B_n),\\ \\mathrm{ratify}(B_{n+1}) \\,)
    $$

    The currently active age remains open until a successor is ratified.
    Baseline, ratification and age are distinct: configuration identity,
    lifecycle event, validity interval.

    ## 9. The three architectural planes

    | Plane | Function | Question |
    |---|---|---|
    | Operational Plane | Performs current authorised functions | What does the system do now? |
    | Evolution Plane | Produces and evaluates candidate configurations | What could the system become? |
    | Evolution Control Plane | Adjudicates and authorises transitions | What is the system permitted to become? |

    ```mermaid
    flowchart TB
        subgraph OP["Operational Plane"]
            RT[Runtime components, interfaces, memory, tools]
        end
        subgraph EP["Evolution Plane"]
            GEN[Candidate generation, validation execution, deployment mechanics, monitoring]
        end
        subgraph CP["Evolution Control Plane"]
            ADJ[Policy, authority, evidence adjudication, ratification, ledger, rollback control]
        end
        OP --> GEN
        GEN --> ADJ
        ADJ -->|authorised transitions| OP
    ```

    $$
    \\mathrm{AGES} := \\langle\\, O,\\ E,\\ C_E \\,\\rangle
    $$

    This tuple is an architectural decomposition — coordinated planes, not an
    arithmetic sum, and not a completed mathematical theory. The control
    plane is not part of the runtime datapath unless a specific
    implementation requires it.

    ## 10. Governed continuity

    System identity depends on the ability to reconstruct why and how each
    ratified state followed from the previous one: which candidate was
    proposed, what evidence supported it, who authorised it, under which
    effectivity, and what would restore the predecessor. Continuity that
    cannot be reconstructed is not governed; it is merely history.

    ## 11. AGES is not

    AGES is not a foundation model, an AGI claim, a machine-learning
    framework, an autonomous agent platform, a biological theory of
    evolution, a single implementation, a certification authority, or a claim
    that unrestricted autonomous self-modification is desirable.

    ## 12. AGES · AI-II · SAI-AUT-OS

    | Level | Role | Question |
    |---|---|---|
    | AGES | Theoretical and engineering paradigm | What is an artificial system that evolves through governed states? |
    | AI-II | Reference architecture | How are evolutionary states, interfaces and infrastructures represented and connected? |
    | SAI-AUT-OS | Operational method and open standard | How are AI evolution transitions governed, verified and controlled? |

    This stack is an ecosystem outlook, not a conformance dependency. Neither
    the AI-II reference architecture nor the SAI-AUT-OS open standard is
    required to study, implement or conform to AGES — and the converse holds
    equally. See [`positioning/`](positioning/README.md).

    ## 13. Repository map

    | Path | Contents |
    |---|---|
    | [`theory/`](theory/README.md) | Foundational theory: evolutive systems, identity, baselines, transitions, continuity, invariants |
    | [`architecture/`](architecture/README.md) | Architectural planes, state and transition model, evidence and authority, effectivity, provenance, AI-II sketch |
    | [`models/`](models/README.md) | Minimal conceptual, temporal, transition and identity-continuity models |
    | [`schemas/`](schemas/README.md) | Exploratory, non-normative YAML examples of core objects |
    | [`positioning/`](positioning/README.md) | Relationship of AI-II and SAI-AUT-OS to AGES |
    | [`research/`](research/README.md) | Open questions, terminological issues, bibliography |
    | [`rfcs/`](rfcs/README.md) | The RFC process governing changes to foundational definitions |
    | [`examples/`](examples/README.md) | Illustrative applications: AI-centred, aerospace, cyber-physical |
    | [`tools/`](tools/README.md) | Deterministic repository generator (single source of truth for structure) |

    ## 14. Current status

    ```text
    Status: Exploratory research and pre-specification
    ```

    Terminology, formal models and boundaries are expected to evolve through
    RFCs ([`rfcs/0000-rfc-process.md`](rfcs/0000-rfc-process.md)).

    ## 15. Open research questions

    See [`research/open-questions.md`](research/open-questions.md). Among
    them: what establishes system identity across substantial change; which
    invariants are constitutive; when an update creates a new age rather
    than a minor revision; whether multiple baselines may coexist under
    different effectivities; how branching and merging are represented; how
    rollback is modelled when a transition is physically irreversible; how
    human and delegated machine authority interact; what evidence suffices to
    ratify; how continuity is treated under progressive component
    replacement; whether one system may contain multiple asynchronous
    evolutionary timelines; and who authorises — and for how long — the
    operation of a deployed but not yet ratified configuration.

    ## 16. Contributing

    Contributions are invited from systems engineering, AI architecture,
    configuration management, safety engineering, formal methods, software
    architecture, cyber-physical systems, philosophy of technology,
    governance, certification and lifecycle management. See
    [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md).

    Licensing is under review and will be declared before the first formal
    release ([`LICENSE`](LICENSE)).

    ## 17. Closing statement

    > **AGES treats artificial evolution not as uncontrolled change, but as
    > an engineered continuity of governed states.**
    """))

add("MANIFESTO.md", T("""
    """ + SEED + """

    # The AGES Manifesto

    **Status:** Exploratory · **Document class:** Foundational · **Repository:** AGES

    Twelve working principles, stated in an engineering register.

    1. Artificial systems will increasingly evolve after initial deployment.
    2. Change without state identity is configuration loss.
    3. Adaptation without evidence is speculation.
    4. Transition without authority is uncontrolled mutation.
    5. Automation does not eliminate responsibility.
    6. Every significant state must be identifiable.
    7. Every governed transition must be reconstructable.
    8. System identity must survive legitimate change.
    9. Evolution must remain bounded by declared invariants.
    10. Irreversible transitions must be explicitly recognised as such.
    11. Governance must not be conflated with operational execution.
    12. Artificial evolution should be engineered before it is automated.

    These principles are commitments of method, not claims of achievement.
    Each is expected to be refined, contested and, where necessary,
    superseded through the RFC process.
    """))

add("GOVERNANCE.md", T("""
    """ + SEED + """

    # Governance

    **Status:** Exploratory · **Document class:** Process · **Repository:** AGES

    ## Material classes

    | Class | Meaning | Change path |
    |---|---|---|
    | Authored documents | Positioning and explanatory texts with named authorship | Editorial review |
    | Accepted conceptual definitions | Terms and models accepted through an RFC | RFC required |
    | Experimental models | Formal sketches under evaluation | Light review; promotion via RFC |
    | Proposed RFCs | Changes under discussion | RFC process |
    | Superseded material | Retained, never deleted; marked superseded | Supersession record |
    | Downstream implementation specifications | External to AGES (e.g. the SAI-AUT-OS open standard) | Governed in their own repositories |

    ## Decision classes

    `ACCEPT` · `REVISE` · `DEFER` · `REJECT` · `SUPERSEDE`

    ## Rules

    - Changes to foundational definitions require an RFC
      ([`rfcs/0000-rfc-process.md`](rfcs/0000-rfc-process.md)).
    - Editorial changes and examples use a lighter review process.
    - This repository makes no formal conformance claims, and no downstream
      standard's conformance language is treated as normative here.
    - Superseded material is never rewritten; it is superseded with a record.
    """))

add("CONTRIBUTING.md", T("""
    """ + SEED + """

    # Contributing

    **Status:** Exploratory · **Document class:** Process · **Repository:** AGES

    Contributions should declare which class of material they touch
    ([`GOVERNANCE.md`](GOVERNANCE.md)): foundational theory (RFC required),
    experimental models, examples, or editorial text.

    The repository structure is generated deterministically by
    [`tools/`](tools/README.md); structural changes are made in the generator
    first. Write in precise technical British English; keep claims
    restrained; separate normative, informative and exploratory material
    explicitly; never treat a model checkpoint as the complete system state.

    Issue templates for theory, architecture and terminology proposals are
    provided under `.github/ISSUE_TEMPLATE/`.
    """))

add("VERSIONING.md", T("""
    """ + SEED + """

    # Versioning

    **Status:** Exploratory · **Document class:** Process · **Repository:** AGES

    This repository is pre-specification: there are no formal releases and no
    conformance versions. Documents carry status headers; accepted conceptual
    definitions cite the RFC that accepted them; superseded documents remain
    in place with a supersession record. A formal versioning scheme will be
    proposed by RFC before any first release.
    """))

add("CHANGELOG.md", T("""
    """ + SEED + """

    # Changelog

    **Status:** Exploratory · **Document class:** Process · **Repository:** AGES

    ## Unreleased

    - Initial exploratory scaffold (generator v@V@): theory, architecture,
      models, schema examples, positioning, research, RFC process, examples.
    """))

add("LICENSE", T("""
    AGES — LICENCE DECISION NOTE (placeholder)

    No licence has been specified for this repository yet. Licensing is under
    review and will be declared before the first formal release. Until then,
    all rights are reserved by the author(s); do not assume any open-source
    licence applies.
    """))

add("GLOSSARY.md", T("""
    """ + SEED + """

    # Glossary

    **Status:** Exploratory · **Document class:** Informative · **Repository:** AGES

    Controlled working vocabulary. Changes require an RFC once terms are
    accepted ([`GOVERNANCE.md`](GOVERNANCE.md)).

    | Term | Working definition |
    |---|---|
    | Artificial evolutive system | An engineered system whose evolution is representable as identifiable states connected by governed transitions. |
    | System baseline | The complete, canonical, uniquely identifiable configuration of the system at a declared point of ratification — not merely a software version or model checkpoint. |
    | Ratification | The lifecycle event by which a deployed candidate configuration becomes the canonical baseline. |
    | Age | The validity interval during which a ratified baseline remains canonical: Age_n = [ratify(B_n), ratify(B_n+1)). |
    | Candidate change | A proposed modification that may produce a successor baseline; it may be rejected, blocked, revised, withdrawn, validated but not authorised, authorised but not deployed, deployed but not ratified, or reverted before ratification. |
    | Evolution transition | The completed and ratified event through which the canonical configuration changes from one baseline to another — distinct from the proposal, the evidence and the authorisation record. |
    | Evolution evidence | Observations, test results, analyses, attestations and trace records used to establish whether a candidate satisfies declared requirements. |
    | Evolution authority | Who or what is permitted to propose, validate, adjudicate, authorise, deploy, ratify, suspend or reverse a transition; may be human, organisational, procedural, delegated, automated under prior policy, or distributed. |
    | Effectivity | Where, when and to which instances, products, deployments, jurisdictions, operating contexts or lifecycle stages a baseline or transition applies. |
    | Evolutionary invariant | A property that must remain true across one or more classes of transition for declared continuity and identity to be preserved. |
    | Governed continuity | The verifiable relation connecting two ratified baselines through an authorised, evidence-supported, reconstructable transition. |
    | Probation window | The interval between deployment and ratification, during which monitoring informs the ratification decision. |
    """))


# ============================================================================
# theory/
# ============================================================================

doc("theory/README.md", "Foundational", "theory/ — Foundational Theory", """
    Purpose: hold the paradigm's foundational documents. Reading order:
    [01](01-artificial-evolutive-systems.md) →
    [02](02-system-identity.md) → [03](03-baselines-and-ages.md) →
    [04](04-evolution-transitions.md) → [05](05-governed-continuity.md) →
    [06](06-evolutionary-invariants.md). Changes here require an RFC
    ([`../GOVERNANCE.md`](../GOVERNANCE.md)).
    """)

doc("theory/01-artificial-evolutive-systems.md", "Foundational",
    "Artificial Evolutive Systems", """
    **Purpose.** Define the class of systems the paradigm studies.

    **Scope.** Artificial, human-designed and engineered systems only:
    AI systems, autonomous and robotic systems, cyber-physical systems,
    aerospace systems, digital twins, distributed computing systems,
    adaptive industrial systems, self-configuring infrastructures,
    human-machine systems. Biological organisms and unguided natural
    evolution are outside the primary scope.

    **Initial definition.** An artificial evolutive system is an engineered
    system whose structures, configurations, capabilities or behaviours may
    change through explicit evolution transitions while preserving
    operational coherence, declared identity invariants, configuration
    traceability, authorised continuity, reconstructability, bounded
    effectivity, evidence-based transition records, and recoverability or
    declared irreversibility.

    **Qualification criterion.** A system does not qualify merely because it
    changes, learns, updates or adapts. Its evolution must be representable
    as a sequence of identifiable states and governed transitions.

    **Key questions.** Where exactly is the boundary between adaptation and
    evolution? Which of the preserved properties are jointly necessary?

    **Unresolved issues.** Whether partially governed systems (some
    transitions governed, others not) form a meaningful intermediate class.

    **Related.** [`02-system-identity.md`](02-system-identity.md) ·
    [`../GLOSSARY.md`](../GLOSSARY.md)
    """)

doc("theory/02-system-identity.md", "Foundational", "System Identity", """
    **Purpose.** State what makes an evolving system *the same system*.

    **Position.** Identity is not material persistence and not configuration
    equality. It is established by the governed continuity connecting
    ratified configurations, together with the preservation of declared
    invariants. This is the engineered answer to the ship-of-Theseus
    problem: the ship's registry, not its planks.

    **Key questions.** What properties establish identity across substantial
    change? Can identity survive replacement of every component if
    continuity and invariants hold? What breaks identity — invariant
    violation, continuity gap, authority collapse?

    **Unresolved issues.** Identity under progressive component replacement;
    identity across forks (see branching, in
    [`../research/open-questions.md`](../research/open-questions.md)).

    **Related.** [`05-governed-continuity.md`](05-governed-continuity.md) ·
    [`06-evolutionary-invariants.md`](06-evolutionary-invariants.md) ·
    [`../models/identity-continuity-model.md`](../models/identity-continuity-model.md)
    """)

doc("theory/03-baselines-and-ages.md", "Foundational", "Baselines and Ages", """
    **Purpose.** Define the paradigm's two temporal primitives.

    **System baseline.** The complete, canonical and uniquely identifiable
    configuration of the system at a declared point of ratification. It may
    include executable components, models, parameters, memory, knowledge,
    interfaces, tools, policies, permissions, infrastructure dependencies,
    schemas, configuration data, safety constraints, authority assignments
    and effectivity declarations. A baseline is not merely a software
    version or model checkpoint: it is the configuration identity of the
    whole governed system. Notation: B₀, B₁, …, Bₙ.

    **Age.** The validity interval during which a ratified baseline remains
    canonical:

    $$
    \\text{Age}_n = [\\, \\mathrm{ratify}(B_n),\\ \\mathrm{ratify}(B_{n+1}) \\,)
    $$

    The active age remains open until a successor is ratified. Baseline
    (configuration identity), ratification (lifecycle event) and age
    (validity interval) are three distinct concepts.

    **Key questions.** When does an update create a new age rather than a
    minor revision? Can multiple baselines coexist under different
    effectivities?

    **Unresolved issues.** Granularity thresholds; concurrent ages.

    **Related.** [`04-evolution-transitions.md`](04-evolution-transitions.md)
    · [`../models/temporal-model.md`](../models/temporal-model.md)
    """)

doc("theory/04-evolution-transitions.md", "Foundational",
    "Evolution Transitions", """
    **Purpose.** Distinguish candidates from transitions, and deployment
    from ratification.

    **Candidate change.** A proposed modification that may produce a
    successor baseline. A candidate is not yet a transition: it may be
    rejected, blocked, revised, withdrawn, validated but not authorised,
    authorised but not deployed, deployed but not ratified, or reverted
    before ratification.

    **Evolution transition.** The completed and ratified event through which
    the canonical configuration changes:

    $$
    B_n \\xrightarrow{T_n} B_{n+1}
    $$

    The transition is the arrow — not the proposal, not the evidence
    package, not the authorisation record.

    **Deployment is not ratification.** A deployed configuration becomes
    canonical only when ratified. A failed deployment must not create a new
    baseline. Between deployment and ratification lies a probation window in
    which monitoring informs the ratification decision
    ([`../models/transition-model.md`](../models/transition-model.md)).

    **Key questions.** What evidence is sufficient to ratify? Who may
    operate, and for how long, a deployed but unratified configuration?

    **Unresolved issues.** Ratification of physically irreversible
    transitions; atomicity of multi-component transitions.

    **Related.** [`03-baselines-and-ages.md`](03-baselines-and-ages.md) ·
    [`../architecture/02-state-and-transition-model.md`](../architecture/02-state-and-transition-model.md)
    """)

doc("theory/05-governed-continuity.md", "Foundational", "Governed Continuity", """
    **Purpose.** Define the paradigm's central relation.

    **Definition.** Governed continuity is the verifiable relation connecting
    two ratified baselines through an authorised, evidence-supported and
    reconstructable transition. It is one of the defining properties of an
    artificial evolutive system: continuity that cannot be reconstructed is
    history, not governance.

    **Reconstructability.** For every transition it must be possible to
    recover: the candidate, the evidence, the adjudication, the authority,
    the effectivity, the deployment record, the ratification, and the
    recovery path (or the declared irreversibility).

    **Key questions.** Is continuity transitive across long chains with
    superseded invariants? How is continuity treated when components are
    replaced progressively?

    **Unresolved issues.** Continuity across repository or custodian
    changes; continuity under partial record loss.

    **Related.** [`02-system-identity.md`](02-system-identity.md) ·
    [`../models/identity-continuity-model.md`](../models/identity-continuity-model.md)
    """)

doc("theory/06-evolutionary-invariants.md", "Foundational",
    "Evolutionary Invariants", """
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
    """)


# ============================================================================
# architecture/
# ============================================================================

doc("architecture/README.md", "Informative", "architecture/ — Architecture", """
    Purpose: architectural documents realising the theory. Contents:
    [planes](01-architectural-planes.md) ·
    [state and transition model](02-state-and-transition-model.md) ·
    [evidence and authority](03-evidence-and-authority.md) ·
    [effectivity](04-effectivity.md) ·
    [identity and provenance](05-identity-and-provenance.md) ·
    [AI-II sketch](AI-II.md).
    """)

doc("architecture/01-architectural-planes.md", "Informative",
    "Architectural Planes", """
    **Purpose.** Decompose an artificial evolutive system into three
    coordinated planes.

    $$
    \\mathrm{AGES} := \\langle\\, O,\\ E,\\ C_E \\,\\rangle
    $$

    An architectural decomposition — coordinated planes, not an arithmetic
    sum, and not a completed mathematical theory.

    | Plane | Answers | Possible contents |
    |---|---|---|
    | Operational (O) | What does the system do under its current baseline? | Runtime components, models and agents, interfaces, memory and knowledge, tools, infrastructure, actuators, operational policies |
    | Evolution (E) | What could the system become? | Observation, candidate generation, training, tuning, assembly, simulation, validation execution, test execution, deployment mechanics, post-deployment monitoring |
    | Evolution Control (C_E) | What is the system permitted to become? | Configuration identification, scope and effectivity control, policy evaluation, authority evaluation, evidence adjudication, risk adjudication, transition authorisation, baseline ratification, ledger management, rollback control, conformance assessment |

    The control plane is not part of the runtime datapath unless a specific
    implementation requires it.

    **Execution versus adjudication.** The Evolution Plane may execute tests,
    run validation suites, collect measurements, produce reports and operate
    deployment infrastructure. The Evolution Control Plane must interpret the
    resulting evidence, compare it with declared policy, assess authority and
    effectivity, and issue or record the governance verdict.

    > The subsystem that executes validation does not automatically own the
    > authority to adjudicate its sufficiency.

    Rollback remains governed: monitoring signals may trigger a new
    adjudication, an emergency policy path, a rollback previously authorised
    by policy, suspension of the current baseline, or transition to a
    recovery baseline. An automatic rollback may be operationally immediate
    while still being constitutionally governed through prior authorisation.

    **Related.**
    [`02-state-and-transition-model.md`](02-state-and-transition-model.md) ·
    [`../models/minimal-conceptual-model.md`](../models/minimal-conceptual-model.md)
    """)

doc("architecture/02-state-and-transition-model.md", "Informative",
    "State and Transition Model", """
    **Purpose.** Fix the candidate-to-ratified-baseline lifecycle.

    ```mermaid
    flowchart TD
        O[Observe] --> P[Propose]
        P --> CE[Collect evidence]
        CE --> V[Validate — execution]
        V --> AJ[Adjudicate]
        AJ --> AU[Authorise]
        AU --> D[Deploy]
        D -->|deployment sound| R[Ratify baseline]
        D -->|deployment fails| RV[Revert — no new baseline]
        R --> M[Monitor]
        M -->|acceptable| K[Continue current age]
        M -->|anomaly| RB[Governed rollback or suspension]
    ```

    Ordering rules: validation execution precedes adjudication; deployment
    precedes baseline ratification; a failed deployment must not
    automatically create a new baseline. Monitoring also operates inside the
    probation window between deployment and ratification, where it informs
    the ratification decision
    ([`../models/transition-model.md`](../models/transition-model.md)).

    **Key questions.** Which states may be skipped, and under whose policy?
    How are multi-component transitions kept atomic?

    **Related.**
    [`../theory/04-evolution-transitions.md`](../theory/04-evolution-transitions.md)
    """)

doc("architecture/03-evidence-and-authority.md", "Informative",
    "Evidence and Authority", """
    **Purpose.** Characterise the two inputs to adjudication.

    **Evidence.** Observations, test results, analyses, attestations and
    trace records establishing whether a candidate satisfies declared
    requirements. Evidence carries integrity protection, scope and declared
    limitations (see
    [`../schemas/examples/evidence.example.yaml`](../schemas/examples/evidence.example.yaml)).

    **Authority.** Who or what may propose, validate, adjudicate, authorise,
    deploy, ratify, suspend or reverse a transition. Authority may be human,
    organisational, procedural, delegated, automated under prior policy, or
    distributed across roles. Automation does not eliminate responsibility.

    **Key questions.** How do human and delegated machine authority
    interact? What evidence is sufficient to ratify a transition?

    **Unresolved issues.** Authority revocation mid-transition; conflicting
    distributed authorities.

    **Related.**
    [`../theory/05-governed-continuity.md`](../theory/05-governed-continuity.md)
    """)

doc("architecture/04-effectivity.md", "Informative", "Effectivity", """
    **Purpose.** Bound where and when baselines and transitions apply.

    **Definition.** Effectivity defines where, when and to which system
    instances, products, deployments, jurisdictions, operating contexts or
    lifecycle stages a baseline or transition applies. A valid change is not
    necessarily valid everywhere.

    **Consequence.** Multiple baselines may be simultaneously canonical
    under disjoint effectivities — one of the open questions is whether this
    should be modelled as concurrent ages or as one partitioned system
    ([`../research/open-questions.md`](../research/open-questions.md)).

    **Related.**
    [`../schemas/examples/effectivity.example.yaml`](../schemas/examples/effectivity.example.yaml)
    """)

doc("architecture/05-identity-and-provenance.md", "Informative",
    "Identity and Provenance", """
    **Purpose.** Anchor baselines to verifiable identity.

    **Position.** Every baseline is uniquely identified (for example by a
    configuration hash over its canonical representation); every transition
    record carries provenance: who proposed, what evidence, who adjudicated,
    who authorised, who ratified. Identity anchors are candidate constitutive
    invariants ([`../theory/06-evolutionary-invariants.md`](../theory/06-evolutionary-invariants.md)).

    **Key questions.** Which identification scheme survives repository and
    custodian changes? What minimum provenance makes a transition
    reconstructable?

    **Related.**
    [`../schemas/examples/baseline.example.yaml`](../schemas/examples/baseline.example.yaml)
    """)

doc("architecture/AI-II.md", "Informative",
    "AI-II — Artificial Intelligence Interoperability and Infrastructure", """
    **Purpose.** Sketch AI-II as a proposed reference architecture for
    AI-centred evolutive systems.

    AI-II may define state representations, lifecycle semantics, interface
    contracts, interoperability rules, infrastructure boundaries, transition
    protocols, evidence exchange formats, identity and provenance
    mechanisms, effectivity semantics and governance interfaces. It is not
    itself an AI model, runtime or implementation: its intended role is
    analogous to a reference model, establishing shared architectural
    language and layer contracts while allowing different technical
    implementations.

    The comparison with the OSI model is an architectural aspiration and
    explanatory analogy only; no claim of equivalent maturity, adoption or
    industry status is made.

    **Related.** [`../positioning/AI-II-within-AGES.md`](../positioning/AI-II-within-AGES.md)
    """)


# ============================================================================
# models/
# ============================================================================

doc("models/README.md", "Experimental model", "models/ — Conceptual Models", """
    Purpose: minimal formal sketches. All content here is exploratory and is
    labelled as conceptual modelling, not completed mathematics. Contents:
    [minimal conceptual model](minimal-conceptual-model.md) ·
    [temporal model](temporal-model.md) ·
    [transition model](transition-model.md) ·
    [identity-continuity model](identity-continuity-model.md).
    """)

doc("models/minimal-conceptual-model.md", "Experimental model",
    "Minimal Conceptual Model", """
    **Purpose.** Relate the core objects in one picture.

    ```mermaid
    flowchart LR
        CAND[Candidate change] -->|evidence, adjudication, authority| TR[Evolution transition]
        TR -->|ratifies| BASE[Baseline]
        BASE -->|opens| AGE[Age]
        AGE -->|closed by next ratification| BASE2[Successor baseline]
        INV[Invariants] -.constrain.-> TR
        EFF[Effectivity] -.bound.-> BASE
    ```

    $$
    \\mathrm{AGES} := \\langle\\, O,\\ E,\\ C_E \\,\\rangle
    $$

    Plain-language reading: candidates become transitions only through
    evidence, adjudication and authority; transitions ratify baselines;
    baselines open ages; invariants constrain transitions; effectivity
    bounds where baselines apply. This is a minimal conceptual model, not a
    formal theory.
    """)

doc("models/temporal-model.md", "Experimental model", "Temporal Model", """
    **Purpose.** Model system time as a sequence of ages.

    $$
    \\text{Age}_n = [\\, \\mathrm{ratify}(B_n),\\ \\mathrm{ratify}(B_{n+1}) \\,)
    $$

    The timeline is a half-open partition: every instant after genesis
    belongs to exactly one age per effectivity scope; the current age is
    right-open. Ratification events are the only age boundaries — deployment
    events are not.

    **Unresolved issues.** Concurrent ages under disjoint effectivities;
    multiple asynchronous evolutionary timelines within one system
    ([`../research/open-questions.md`](../research/open-questions.md)).
    """)

doc("models/transition-model.md", "Experimental model", "Transition Model", """
    **Purpose.** Model the two monitoring windows around ratification.

    $$
    B_n \\xrightarrow{T_n} B_{n+1}
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
    """)

doc("models/identity-continuity-model.md", "Experimental model",
    "Identity-Continuity Model", """
    **Purpose.** Sketch identity as a chain property.

    Conceptual reading: the system's identity at baseline B_n holds if and
    only if there exists a chain of governed transitions from a declared
    identity origin to B_n in which every transition is authorised,
    evidence-supported and reconstructable, and every constitutive invariant
    is preserved. Replaceable invariants may change only through governed
    transitions of the invariant set itself.

    **Unresolved issues.** Chains across forks and merges; identity under
    partial record loss; progressive replacement of identity anchors.

    **Related.** [`../theory/02-system-identity.md`](../theory/02-system-identity.md)
    """)


# ============================================================================
# schemas/
# ============================================================================

doc("schemas/README.md", "Example", "schemas/ — Exploratory Examples", """
    Purpose: illustrative, non-normative YAML examples of the core objects.
    Nothing in this directory is a specification: field names, structures
    and values are exploratory and expected to change through RFCs.
    Contents: [`examples/`](examples/baseline.example.yaml) — baseline,
    transition, evidence, effectivity.
    """)

add("schemas/examples/baseline.example.yaml", T("""
    # ages:seed v@V@ — Exploratory example. Non-normative.
    baselineId: B-0003
    status: ratified
    ratifiedAt: 2026-05-11T09:30:00Z
    supersedes: B-0002
    systemIdentity: example-org/assistive-system
    configurationHash: "sha256:3f6a1c..."
    components:
      - componentId: core-model
        kind: foundation-model
        stateRef: "model-registry://example/base-7b@rev-41"
      - componentId: task-memory
        kind: memory
        stateRef: "memory-store://org-glossary@snapshot-19"
      - componentId: analysis-tools
        kind: tool-set
        stateRef: "tool-manifest://assistant@m-0007"
    policies:
      - policyId: change-policy-standard
        version: 0.3.0
    effectivity:
      environments: [production-eu]
    transitionRecord: T-0002
    provenance:
      ratifiedBy: change-board
      method: recorded-decision
    """))

add("schemas/examples/transition.example.yaml", T("""
    # ages:seed v@V@ — Exploratory example. Non-normative.
    transitionId: T-0002
    sourceBaseline: B-0002
    candidateBaseline: B-0003
    changeSet:
      - component: task-memory
        change: snapshot-18 -> snapshot-19
    evidenceReferences: [EV-0104, EV-0105]
    validationResults:
      regressionSuite: pass
      driftCheck: within-declared-bounds
    authority:
      adjudicatedBy: evolution-control-board
      authorisedBy: change-board
    decision: authorised
    deploymentStatus: deployed
    ratificationStatus: ratified
    rollbackTarget: B-0002
    effectivity:
      environments: [production-eu]
    """))

add("schemas/examples/evidence.example.yaml", T("""
    # ages:seed v@V@ — Exploratory example. Non-normative.
    evidenceId: EV-0104
    type: regression-suite
    source: validation-cluster-2
    collectedAt: 2026-05-10T16:00:00Z
    integrityHash: "sha256:9b41d0..."
    scope:
      components: [task-memory]
      environments: [staging-eu]
    results:
      passed: 412
      failed: 0
    limitations: >
      Staging traffic profile only; production load characteristics were
      not exercised.
    """))

add("schemas/examples/effectivity.example.yaml", T("""
    # ages:seed v@V@ — Exploratory example. Non-normative.
    effectivityId: EFF-0009
    organisations: [example-org]
    programmes: [assistive-systems]
    products: [assistive-system]
    instances: [prod-eu-01, prod-eu-02]
    jurisdictions: [EU]
    environments: [production-eu]
    lifecycleStages: [operation]
    validFrom: 2026-05-11T09:30:00Z
    validUntil: null
    """))


# ============================================================================
# positioning/
# ============================================================================

doc("positioning/README.md", "Informative", "positioning/ — Ecosystem Positioning", """
    Purpose: relate AGES to compatible downstream realisations. The stack
    AGES → AI-II → SAI-AUT-OS is an ecosystem outlook, not a conformance
    dependency: neither downstream layer is required to study, implement or
    conform to AGES, and each remains usable without the others. Contents:
    [`AI-II-within-AGES.md`](AI-II-within-AGES.md) ·
    [`SAI-AUT-OS-within-AGES.md`](SAI-AUT-OS-within-AGES.md).
    """, authored=True)

doc("positioning/AI-II-within-AGES.md", "Informative", "AI-II within AGES", """
    The AI-II reference architecture (Artificial Intelligence
    Interoperability and Infrastructure) is a possible architectural
    realisation of the AGES paradigm for AI-centred systems: it may specify
    how evolutionary states are represented, interconnected and made
    interoperable — state representations, lifecycle semantics, interface
    contracts, transition protocols, evidence exchange formats, identity and
    provenance mechanisms, effectivity semantics.

    ```mermaid
    flowchart TB
        AGES[AGES — paradigm] --> AIII[AI-II — reference architecture]
    ```

    AI-II is optional with respect to AGES, and AGES makes no claim about
    AI-II's maturity or adoption. See
    [`../architecture/AI-II.md`](../architecture/AI-II.md).
    """, authored=True)

doc("positioning/SAI-AUT-OS-within-AGES.md", "Informative",
    "SAI-AUT-OS within AGES", """
    The SAI-AUT-OS open standard (Selective AI for Autonomous Upgrade and
    Tuning — Open Standard) is an independent, specification-first open
    standard defining an Evolution Control Plane for governed AI evolution.
    Within the AGES vocabulary, it operationalises the Evolution Control
    Plane: selective mutability, cognitive configuration items, evidence
    packages, effectivity, authority, policy and validation adjudication,
    baselines, traceability, ledger management, deployment authorisation,
    rollback and conformance.

    ```mermaid
    flowchart TB
        AGES[AGES — paradigm] --> AIII[AI-II — reference architecture]
        AIII --> SAI[SAI-AUT-OS — Evolution Control Plane standard]
    ```

    This is one possible ecosystem stack, not a normative dependency chain:
    the SAI-AUT-OS open standard is governed in its own repository, remains
    usable without adopting AGES or AI-II, and its conformance language is
    not normative here.
    """, authored=True)


# ============================================================================
# research/
# ============================================================================

doc("research/README.md", "Informative", "research/ — Open Research", """
    Purpose: the honest ledger of what is unresolved. Contents:
    [`open-questions.md`](open-questions.md) ·
    [`terminology.md`](terminology.md) · [`bibliography.md`](bibliography.md).
    """)

doc("research/open-questions.md", "Informative", "Open Research Questions", """
    1. What properties establish system identity across substantial change?
    2. Which invariants are constitutive and which are replaceable?
    3. When does an update create a new age rather than a minor revision?
    4. Can multiple baselines coexist under different effectivities?
    5. How should branching and merging be represented?
    6. How can rollback be modelled when a transition is physically
       irreversible?
    7. How should human authority and delegated machine authority interact?
    8. What evidence is sufficient to ratify a transition?
    9. How should continuity be treated when components are replaced
       progressively?
    10. Can one artificial system contain multiple asynchronous evolutionary
        timelines?
    11. Who authorises — and for how long — the operation of a deployed but
        not yet ratified configuration (the probation window)?
    """)

doc("research/terminology.md", "Informative", "Terminological Issues", """
    Open terminological questions, tracked for RFC resolution:
    *evolutive* versus *evolutionary* (the former chosen to avoid biological
    connotations — is the distinction sustainable in English?); *ratification*
    versus *acceptance* versus *promotion*; whether *age* should admit
    synonyms (*era*, *epoch*) or remain exclusive; whether *canonical* is the
    right qualifier for the active baseline; how to name a deployed but
    unratified configuration (*probationary configuration* is the current
    working term).
    """)

doc("research/bibliography.md", "Informative", "Bibliography — Starting Points", """
    A deliberately short list of relevant, well-established starting points;
    to be extended through contributions.

    - Configuration management: ISO 10007 (quality management — guidelines
      for configuration management).
    - Systems and software engineering lifecycle: ISO/IEC/IEEE 15288.
    - Software evolution: M. M. Lehman's laws of software evolution;
      D. L. Parnas, "Software Aging" (ICSE 1994).
    - Reference-model precedent: ISO/IEC 7498-1 (the OSI basic reference
      model) — cited here as an architectural analogy only.
    - Identity through change: the ship-of-Theseus problem (Plutarch), as
      classical background to
      [`../theory/02-system-identity.md`](../theory/02-system-identity.md).
    """)


# ============================================================================
# rfcs/
# ============================================================================

doc("rfcs/README.md", "Process", "rfcs/ — RFC Process", """
    Purpose: govern changes to foundational definitions. Process:
    [`0000-rfc-process.md`](0000-rfc-process.md). Foundational changes
    require an RFC; editorial changes do not
    ([`../GOVERNANCE.md`](../GOVERNANCE.md)).
    """)

doc("rfcs/0000-rfc-process.md", "Process", "RFC-0000 — The RFC Process", """
    **RFC contents.** Title; status; authors; created date; abstract;
    motivation; terminology; proposed model; alternatives; compatibility
    impact; unresolved questions; decision record.

    **Statuses.** Draft · Under Review · Accepted · Rejected · Withdrawn ·
    Superseded.

    **Decision classes.** ACCEPT · REVISE · DEFER · REJECT · SUPERSEDE
    ([`../GOVERNANCE.md`](../GOVERNANCE.md)).

    **Suggested future RFCs** (titles reserved, content not yet written):

    ```text
    0001 — Core AGES terminology
    0002 — Baselines and ages
    0003 — Evolution transition semantics
    0004 — Governed continuity
    0005 — Evolutionary invariants
    0006 — Branching, merging and concurrent ages
    0007 — AI-II reference architecture
    0008 — Relationship with SAI-AUT-OS
    ```
    """)


# ============================================================================
# examples/
# ============================================================================

doc("examples/README.md", "Example", "examples/ — Illustrative Applications", """
    Purpose: show the paradigm applied to three different classes of
    engineered system. Contents:
    [`ai-centred-system.md`](ai-centred-system.md) ·
    [`aerospace-system.md`](aerospace-system.md) ·
    [`cyber-physical-system.md`](cyber-physical-system.md).
    """)

doc("examples/ai-centred-system.md", "Example", "Example — AI-Centred System", """
    For an AI-centred artificial evolutive system, the canonical baseline
    includes the entire cognitive configuration: foundation models,
    adapters, memory, retrieval systems, knowledge, agent tools, routing,
    permissions, policies, runtime infrastructure. "Model version" alone is
    explicitly rejected as a description of system identity: two deployments
    of the same model with different memory, tools and permissions are two
    different configurations — and, once ratified, two different baselines.

    A typical transition: a durable memory promotion is proposed, evidenced
    (provenance, integrity, drift checks), adjudicated against policy,
    authorised, deployed to a probationary scope, monitored, and ratified —
    opening a new age of the assistant.

    **Related.** [`../theory/03-baselines-and-ages.md`](../theory/03-baselines-and-ages.md)
    """)

doc("examples/aerospace-system.md", "Example", "Example — Aerospace System", """
    Aerospace engineering already practises much of the paradigm under other
    names: type-design configuration, modification approval, effectivity by
    serial number, service-bulletin incorporation, configuration baselines
    and airworthiness evidence. An aircraft fleet is an artificial evolutive
    system whose ages are opened by approved modifications: the ratification
    event is regulatory approval plus recorded incorporation, and
    effectivity (which airframes, which operators, which jurisdictions) is
    first-class — a modification valid for one serial range is not valid for
    another.

    The example illustrates two AGES claims: effectivity-bounded baselines
    can coexist, and irreversible physical transitions (structural
    modifications) require declared irreversibility rather than rollback.

    **Related.** [`../architecture/04-effectivity.md`](../architecture/04-effectivity.md)
    """)

doc("examples/cyber-physical-system.md", "Example",
    "Example — Cyber-Physical System", """
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
    """)


# ============================================================================
# profiles/ — application profiles (AGES-CPS)
# ============================================================================

doc("profiles/README.md", "Informative", "profiles/ — Application Profiles", """
    Purpose: exploratory application profiles that apply the AGES paradigm
    to specific engineering domains. A profile specialises AGES vocabulary,
    models and lifecycle to a domain; it does not replace AGES, introduce a
    parent paradigm, or claim that its domain is the exclusive AGES domain.
    Contents: [`AGES-CPS/`](AGES-CPS/README.md) — AGES Profile for
    Cyber-Physical and Robotic Systems.
    """)

doc("profiles/AGES-CPS/README.md", "Informative",
    "AGES-CPS — AGES Profile for Cyber-Physical and Robotic Systems", """
    An exploratory application profile of AGES for robotics and
    cyber-physical systems. AGES remains the general paradigm; AGES-CPS is
    not a middleware, controller, planner or safety standard. Contents:
    [scope and positioning](01-scope-and-positioning.md) ·
    [robotic system identity](02-robotic-system-identity.md) ·
    [hardware–software co-baselines](03-hardware-software-co-baselines.md) ·
    [multi-rate autonomy](04-multi-rate-autonomy.md) ·
    [delegated operational envelopes](05-delegated-operational-envelopes.md) ·
    [GENTILE and GTL for robotics](06-gentile-and-gtl-for-robotics.md) ·
    [physical invariants](07-physical-invariants.md) ·
    [irreversibility and recovery](08-irreversibility-and-recovery.md) ·
    [digital–physical closure evidence](09-digital-physical-closure-evidence.md) ·
    [fleet effectivity](10-fleet-effectivity.md) ·
    [middleware integration](11-middleware-integration.md).
    """)

_CPS_DOCS = [
    ("01-scope-and-positioning.md", "Scope and Positioning",
     "Thesis, preserved AGES core, motivation for a robotics profile and "
     "the relationship with robotics middleware."),
    ("02-robotic-system-identity.md", "Robotic System Identity",
     "Conceptual model of governed robotic identity: baseline, transition "
     "history, invariants, effectivity and physical-state record."),
    ("03-hardware-software-co-baselines.md", "Hardware–Software Co-Baselines",
     "The robotic baseline as a possible hardware–software co-baseline and "
     "the criteria that determine baseline impact."),
    ("04-multi-rate-autonomy.md", "Multi-Rate Autonomy",
     "Control, operation, adaptation and governance timescales; the "
     "Evolution Control Plane outside the hard real-time path."),
    ("05-delegated-operational-envelopes.md", "Delegated Operational Envelopes",
     "The bounded runtime authority delegated in advance to the "
     "Operational Plane."),
    ("06-gentile-and-gtl-for-robotics.md", "GENTILE and GTL for Robotics",
     "GENTILE and GTL applied to robotic intent negotiation and grounded "
     "robotic action candidates."),
    ("07-physical-invariants.md", "Physical Invariants",
     "Physical properties, capability limits and safety boundaries that "
     "must hold across transitions."),
    ("08-irreversibility-and-recovery.md", "Irreversibility and Recovery",
     "Rollback, compensation, safe-state transition, containment, recovery "
     "baseline and declared irreversibility."),
    ("09-digital-physical-closure-evidence.md",
     "Digital–Physical Closure Evidence",
     "Evidence connecting authorised action, recorded execution and "
     "observed physical result."),
    ("10-fleet-effectivity.md", "Fleet Effectivity",
     "Fleet, cohort and instance effectivity for robotic candidates and "
     "baselines."),
    ("11-middleware-integration.md", "Middleware Integration",
     "Relationship with ROS 2 and comparable middleware; adapters from GTL "
     "candidates to executable robotic forms."),
]
for _rel, _title, _summary in _CPS_DOCS:
    doc(f"profiles/AGES-CPS/{_rel}", "Informative", _title, f"""
        {_summary}
        Part of the AGES-CPS exploratory application profile
        ([`README.md`](README.md)).
        """)

doc("models/robotic-identity-model.md", "Experimental model",
    "Robotic Identity Model", """
    Exploratory conceptual model of governed robotic identity for the
    AGES-CPS profile
    ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)):
    active baseline, ratified transition history, invariant set, active
    effectivity and the relevant physical-state and provenance record.
    A conceptual expression, not a complete mathematical theory.
    """)

doc("models/hardware-software-co-baseline-model.md", "Experimental model",
    "Hardware–Software Co-Baseline Model", """
    Exploratory sketch of the robotic co-baseline for the AGES-CPS profile
    ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)):
    identity-relevant physical, electronic, firmware, software, model,
    calibration, safety, authority and environmental configuration groups.
    """)

doc("models/multi-rate-autonomy-model.md", "Experimental model",
    "Multi-Rate Autonomy Model", """
    Exploratory timescale model for the AGES-CPS profile
    ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)):
    control, operation, adaptation and governance rates, with the
    Evolution Control Plane outside the hard real-time control path.
    No universal timing values are prescribed.
    """)

add("schemas/examples/robotic-baseline.example.yaml", T("""
    # ages:seed v@V@ — exploratory, non-normative example.
    # Robotic hardware–software co-baseline; supersede with authored content.
    baselineId: RB-0000
    system: example-org/example-robot
    class: hardware-software-co-baseline
    status: seed
    """))

add("schemas/examples/delegated-operational-envelope.example.yaml", T("""
    # ages:seed v@V@ — exploratory, non-normative example.
    # Delegated operational envelope; supersede with authored content.
    envelopeId: DOE-0000
    baseline: RB-0000
    status: seed
    """))

add("schemas/examples/robotic-action-candidate.example.yaml", T("""
    # ages:seed v@V@ — exploratory, non-normative example.
    # Robotic GTL action candidate; supersede with authored content.
    actionCandidateId: RAC-0000
    status: seed
    """))

add("schemas/examples/physical-closure-evidence.example.yaml", T("""
    # ages:seed v@V@ — exploratory, non-normative example.
    # Digital–physical closure evidence; supersede with authored content.
    closureEvidenceId: PCE-0000
    status: seed
    """))

add("schemas/examples/recovery-baseline.example.yaml", T("""
    # ages:seed v@V@ — exploratory, non-normative example.
    # Recovery baseline; supersede with authored content.
    baselineId: RB-0000-R
    class: recovery-baseline
    status: seed
    """))

doc("examples/robotic-operational-inspection.md", "Example",
    "Example — Robotic Operational Inspection", """
    An operational AGES-CPS example: GENTILE clarifies an inspection
    request, GTL produces a bounded inspection action, execution produces
    closure evidence, and no baseline changes
    ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)).
    """)

doc("examples/robotic-calibration-evolution.md", "Example",
    "Example — Robotic Calibration Evolution", """
    An evolutionary AGES-CPS example: calibration drift creates a candidate
    change, evidence is collected, deployment is instance-specific, closure
    is verified and a successor baseline is ratified
    ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)).
    """)

doc("examples/bounded-cyber-physical-action.md", "Example",
    "Example — Bounded Cyber-Physical Action and Safe-State Recovery", """
    An AGES-CPS example: an execution deviation triggers an independent
    safe state, evidence is collected, exact physical rollback is
    impossible, compensation is applied and a recovery baseline is proposed
    ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)).
    """)

doc("examples/fleet-model-deployment.md", "Example",
    "Example — Fleet Model Deployment", """
    An AGES-CPS example: fleet evidence produces a perception-model
    candidate, shadow-mode validation is performed, effectivity is
    cohort-specific, rollback is declared and ratification is staged
    ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)).
    """)

_CPS_RFCS = [
    ("0012-ages-cps-profile.md",
     "RFC-0012 — AGES-CPS: AGES Profile for Cyber-Physical and Robotic Systems",
     "Proposes AGES-CPS as an exploratory application profile of AGES."),
    ("0013-robotic-baseline-semantics.md",
     "RFC-0013 — Robotic Baseline Semantics",
     "Proposes hardware–software co-baseline semantics for robotic systems."),
    ("0014-multi-rate-autonomy.md",
     "RFC-0014 — Multi-Rate Autonomy",
     "Proposes the multi-rate autonomy relation and envelope delegation."),
    ("0015-physical-irreversibility.md",
     "RFC-0015 — Physical Irreversibility",
     "Proposes recovery modes and reversibility declarations for "
     "cyber-physical transitions."),
    ("0016-digital-physical-closure-evidence.md",
     "RFC-0016 — Digital–Physical Closure Evidence",
     "Proposes evidence connecting authorised action, execution and "
     "physical result."),
    ("0017-fleet-effectivity.md",
     "RFC-0017 — Fleet Effectivity",
     "Proposes fleet, cohort and instance effectivity semantics."),
]
for _rel, _title, _summary in _CPS_RFCS:
    doc(f"rfcs/{_rel}", "RFC proposal", _title, f"""
        {_summary}
        Draft; not accepted. Part of the AGES-CPS exploratory application
        profile
        ([`../profiles/AGES-CPS/README.md`](../profiles/AGES-CPS/README.md)).
        Process: [`0000-rfc-process.md`](0000-rfc-process.md).
        """)


# ============================================================================
# tools/ and .github/
# ============================================================================

doc("tools/README.md", "Process", "tools/ — Deterministic Tooling", """
    Purpose: hold the deterministic repository generator,
    `ages_scaffold.py`, which is the single source of truth for this
    repository's structure and exploratory seed content. Structural changes
    are made in the generator first; `--check` verifies the tree and
    `--manifest` emits a SHA-256 record of the seed set. The generator is
    copied into this directory alongside this file.
    """)

add(".github/ISSUE_TEMPLATE/theory-proposal.yml", T("""
    # ages:seed v@V@
    name: Theory proposal
    description: Propose a change to AGES foundational theory (RFC candidate)
    labels: ["theory", "rfc-candidate"]
    body:
      - type: textarea
        id: summary
        attributes:
          label: Summary
          description: What conceptual change is proposed, in a few sentences?
        validations:
          required: true
      - type: textarea
        id: motivation
        attributes:
          label: Motivation
          description: Why the current formulation is insufficient.
        validations:
          required: true
      - type: textarea
        id: impact
        attributes:
          label: Affected documents and terms
          description: Which theory documents and glossary terms are affected?
    """))

add(".github/ISSUE_TEMPLATE/architecture-proposal.yml", T("""
    # ages:seed v@V@
    name: Architecture proposal
    description: Propose a change to AGES architectural documents
    labels: ["architecture"]
    body:
      - type: textarea
        id: summary
        attributes:
          label: Summary
        validations:
          required: true
      - type: textarea
        id: planes
        attributes:
          label: Affected planes and documents
          description: Operational, Evolution, Evolution Control; which files?
    """))

add(".github/ISSUE_TEMPLATE/terminology-proposal.yml", T("""
    # ages:seed v@V@
    name: Terminology proposal
    description: Propose, refine or contest a controlled term
    labels: ["terminology", "rfc-candidate"]
    body:
      - type: input
        id: term
        attributes:
          label: Term
        validations:
          required: true
      - type: textarea
        id: definition
        attributes:
          label: Proposed working definition
        validations:
          required: true
      - type: textarea
        id: conflicts
        attributes:
          label: Conflicts and overlaps
          description: Existing glossary terms this interacts with.
    """))

add(".github/pull_request_template.md", T("""
    <!-- ages:seed v@V@ -->
    ## Material class

    Which class does this change touch? (see GOVERNANCE.md)
    Foundational theory (RFC required) · Experimental model · Example ·
    Editorial · Structure (generator change required)

    ## Summary

    ## Affected documents

    ## RFC reference (if foundational)
    """))


# ----------------------------------------------------------------------------
# Engine
# ----------------------------------------------------------------------------

def emit(root: Path, force: bool) -> tuple[int, int, int]:
    created = skipped = overwritten = 0
    for rel, content in FILES.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        exists = path.exists()
        if exists and not force:
            skipped += 1
            continue
        with path.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        overwritten += int(exists)
        created += int(not exists)
    return created, skipped, overwritten


def check(root: Path) -> int:
    missing = [rel for rel in FILES if not (root / rel).exists()]
    if missing:
        print(f"[FAIL] structure: {len(missing)} controlled path(s) missing:")
        for rel in missing:
            print(f"       - {rel}")
        return 1
    seed = sum(1 for rel, c in FILES.items()
               if (root / rel).read_bytes() == c.encode("utf-8"))
    print(f"[OK]   structure: all {len(FILES)} controlled paths present.")
    print(f"[info] authoring progress: {len(FILES) - seed}/{len(FILES)} "
          f"authored, {seed}/{len(FILES)} still at seed state.")
    return 0


def verify(root: Path) -> int:
    """Content gate: the foundational checklist, executable forever.

    Checks (hard failures): no empty files; every relative Markdown link
    resolves; no 'General Evolutive System' superclass (the phrase is valid
    only inside 'Artificial General Evolutive System'); British English
    (no authorized/authorization/behavior/organization/modeling/
    standardization); no sai-aut-os identifiers; display maths uses $$ only;
    every substantive .md outside .github/ carries a Status header; YAML
    parses (skipped with a warning if PyYAML is unavailable)."""
    errors: list[str] = []
    md = sorted(root.rglob("*.md"))
    everything = sorted(p for p in root.rglob("*") if p.is_file())

    for p in everything:
        if p.stat().st_size == 0:
            errors.append(f"empty file: {p.relative_to(root)}")

    link_rx = re.compile(r"\]\(([^)#\s]+?)(?:#[^)\s]*)?\)")
    n_links = 0
    for p in md:
        for target in link_rx.findall(p.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            n_links += 1
            if not (p.parent / target).resolve().exists():
                errors.append(f"broken link in {p.relative_to(root)}: {target}")

    ges_rx = re.compile(r"(?<!Artificial )General Evolutive System")
    american = ("authorized", "authorization", "behavior", "organization",
                "modeling", "standardization")
    for p in md:
        text = p.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if ges_rx.search(line):
                errors.append(f"GES superclass in {p.relative_to(root)}:{i}")
        for w in american:
            if re.search(rf"\b{w}\b", text, re.I):
                errors.append(f"American spelling '{w}' in {p.relative_to(root)}")
        if re.search(r"^\\\[", text, re.M):
            errors.append(f"non-$$ display maths in {p.relative_to(root)}")
        if ".github" not in p.parts and "**Status:**" not in text:
            errors.append(f"missing status header: {p.relative_to(root)}")

    needle = "sai-aut-os" + ":"  # built at runtime: the scanner must not match its own source
    for p in everything:
        if needle in p.read_text(encoding="utf-8", errors="ignore"):
            errors.append(f"sai-aut-os identifier in {p.relative_to(root)}")

    yaml_note = ""
    try:
        import yaml  # type: ignore
        for p in sorted(root.rglob("*.yml")) + sorted(root.rglob("*.yaml")):
            try:
                yaml.safe_load(p.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid YAML {p.relative_to(root)}: {exc}")
    except ImportError:
        yaml_note = " (YAML checks skipped: PyYAML unavailable)"

    if errors:
        print(f"[FAIL] verify: {len(errors)} finding(s):")
        for e in errors:
            print(f"       - {e}")
        return 1
    print(f"[OK]   verify: {len(everything)} files, {n_links} links resolved, "
          f"content gates green{yaml_note}.")
    return 0


def manifest_json() -> str:
    return json.dumps({
        "repository": "AGES",
        "generator_version": AGES_VERSION,
        "file_count": len(FILES),
        "files": {rel: {"sha256": hashlib.sha256(c.encode()).hexdigest(),
                        "bytes": len(c.encode())}
                  for rel, c in FILES.items()},
    }, indent=2, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ages_scaffold.py",
        description=f"AGES deterministic repository generator v{AGES_VERSION}.")
    parser.add_argument("--root", default=".")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--manifest", metavar="PATH")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args(argv)

    if args.list:
        for rel in FILES:
            print(rel)
        return 0

    root = Path(args.root)
    if args.check or args.verify:
        rc = 0
        if args.check:
            rc = check(root)
        if args.verify and rc == 0:
            rc = verify(root)
    else:
        created, skipped, overwritten = emit(root, args.force)
        print(f"[OK]   AGES scaffold v{AGES_VERSION}")
        print(f"       root: {root.resolve()}")
        print(f"       created={created} skipped={skipped} "
              f"overwritten={overwritten} (controlled files: {len(FILES)})")
        rc = 0

    if args.manifest:
        out = Path(args.manifest)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write(manifest_json())
        print(f"[OK]   manifest: {len(FILES)} seed files -> {out}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
