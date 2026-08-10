---
type: Bundle Index
title: Kimball Dimensional Modeling
description: Source-aware guidance for business processes, grain, facts, dimensions, conformance, history, quality, and controlled warehouse design.
category: frameworks
version: 0.1.0
tags:
- kimball
- dimensional-modeling
- data-warehouse
aliases:
- Business Dimensional Lifecycle
problems_solved:
- Apply Kimball Dimensional Modeling using inspectable evidence.
- Review assumptions, definitions, calculations, and decision boundaries.
- Prepare a controlled recommendation without inventing local facts or outcomes.
industries:
- Cross-industry
- Operations
- Professional services
tools:
[]
frameworks:
- Kimball Dimensional Modeling
deliverables:
- Kimball dimensional model design brief
commands: []
skills: []
evaluations:
- Kimball Dimensional Modeling source-awareness check
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
    required_qualification: A qualified dimensional-modeling, analytics engineering, data governance, security, privacy, finance, or domain professional appropriate to the warehouse.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for business requirements, processes, source systems, records, grain, facts, dimensions, keys, hierarchies, slowly changing behavior, conformance, bus matrix, transformations, quality rules, security classifications, query patterns, tests, owners, and approvals.
- This bundle does not grant authority to change schemas or pipelines, expose data, redefine metrics, backfill history, alter access, migrate reports, or deploy production models.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before change schemas or pipelines, expose data, redefine metrics, backfill history, alter access, migrate reports, or deploy production models.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: kimball-dimensional-modeling
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
# Kimball Dimensional Modeling

Use this bundle to prepare a reviewable **Kimball dimensional model design brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Business process, source semantics, grain, fact additivity, dimension meaning, key behavior, history, conformance, transformation result, quality, effective access, query result, and migration impact.

## Start Here

- [Overview](overview.md)
- [Kimball Dimensional Modeling Source-Aware Guide](framework.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Kimball dimensional model design brief](deliverables/kimball-dimensional-modeling-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

