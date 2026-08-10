---
type: Bundle Index
title: ABC Inventory Analysis
description: Source-aware guidance for selecting value measures, ranking items, setting thresholds, testing sensitivity, and governing inventory policies.
category: frameworks
version: 0.1.0
tags:
- abc-analysis
- inventory
- pareto
aliases:
- ABC Classification
problems_solved:
- Apply ABC Inventory Analysis using inspectable evidence.
- Review assumptions, definitions, calculations, and decision boundaries.
- Prepare a controlled recommendation without inventing local facts or outcomes.
industries:
- Cross-industry
- Operations
- Professional services
tools:
[]
frameworks:
- ABC Inventory Analysis
deliverables:
- ABC inventory classification brief
commands: []
skills: []
evaluations:
- ABC Inventory Analysis source-awareness check
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
  - financial
  - safety
  professional_review:
    status: not_reviewed
    required_qualification: A qualified inventory, supply-chain, operations, finance, safety, or domain professional appropriate to the items and decision.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for inventory population, item identifiers, period, quantities, unit values, demand, margin or criticality measures, data quality, inclusion rules, ranking formula, cumulative values, thresholds, sensitivity, service and safety constraints, policies, owners, and approvals.
- This bundle does not grant authority to change stocking, service levels, counts, procurement, disposal, safety stock, or financial plans.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before change stocking, service levels, counts, procurement, disposal, safety stock, or financial plans.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: abc-analysis
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
# ABC Inventory Analysis

Use this bundle to prepare a reviewable **ABC inventory classification brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Population completeness, quantities, values, demand, criticality, ranking measure, thresholds, class membership, sensitivity, service or safety effect, savings, and authority.

## Start Here

- [Overview](overview.md)
- [ABC Inventory Analysis Source-Aware Guide](framework.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [ABC inventory classification brief](deliverables/abc-analysis-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

