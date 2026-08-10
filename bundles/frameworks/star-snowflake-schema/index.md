---
type: Bundle Index
title: Star and Snowflake Schema Design
description: Source-aware guidance for grain, facts, dimensions, normalization choices, conformance, performance, and governed schema design.
category: frameworks
version: 0.1.0
tags:
- star-schema
- snowflake-schema
- dimensional-modeling
aliases:
- Star Schema
- Snowflake Schema
problems_solved:
- Apply Star and Snowflake Schema Design using inspectable evidence.
- Review assumptions, definitions, calculations, and decision boundaries.
- Prepare a controlled recommendation without inventing local facts or outcomes.
industries:
- Cross-industry
- Operations
- Professional services
tools:
[]
frameworks:
- Star and Snowflake Schema Design
deliverables:
- Star-versus-snowflake design brief
commands: []
skills: []
evaluations:
- Star and Snowflake Schema Design source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles:
[]
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc:
  []
  isco_08:
  []
  esco: []
content_risk:
  classification: ymyl
  domains:
  - privacy
  - security
  - financial
  professional_review:
    status: not_reviewed
    required_qualification: A qualified data architecture, dimensional-modeling, analytics engineering, security, privacy, finance, or domain professional appropriate to the system.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for business process, query use cases, source schemas, grain, facts, dimensions, hierarchies, keys, cardinalities, history, conformance, platform behavior, data volumes, security classifications, performance evidence, tests, owners, and approvals.
- This bundle does not grant authority to change schemas, redefine grain or metrics, expose data, alter history, migrate queries, drop objects, or deploy production changes.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before change schemas, redefine grain or metrics, expose data, alter history, migrate queries, drop objects, or deploy production changes.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: star-snowflake-schema
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard.
---
# Star and Snowflake Schema Design

Use this bundle to prepare a reviewable **Star-versus-snowflake design brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Source semantics, grain, fact additivity, dimension meaning, hierarchy validity, key behavior, history, conformance, effective access, query correctness, performance, and migration impact.

## Start Here

- [Overview](overview.md)
- [Star and Snowflake Schema Design Source-Aware Guide](framework.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Star-versus-snowflake design brief](deliverables/star-snowflake-schema-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

