---
type: Bundle Index
title: Logistics Analyst
description: Source-aware guidance for logistics evidence, network analysis, service and cost tradeoffs, disruption scenarios, and reviewable recommendations.
category: roles
version: 0.1.0
tags:
- logistics
- supply-chain-analysis
- operations
aliases:
- Logistics Planning Analyst
- Distribution Analyst
problems_solved:
- Reconcile logistics records and definitions.
- Prepare evidenced network and service analyses.
- Keep recommendations within purchasing, safety, trade, and operational authority.
industries:
- Logistics
- Manufacturing
- Retail
tools:
[]
frameworks:
- logistics source-evidence matrix
deliverables:
- logistics analysis brief
commands: []
skills: []
evaluations:
- Logistics Analyst source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- supply-chain-manager
- logistician
- production-planning-and-expediting-clerk
adjacent_bundles:
- microsoft-power-bi
- sap-s4hana
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1081.02
  soc:
  - 13-1081
  isco_08:
  - '2421'
  esco: []
content_risk:
  classification: ymyl
  domains:
  - financial
  - safety
  - security
  - legal
  professional_review:
    status: not_reviewed
    required_qualification: A qualified logistics, supply-chain, procurement, finance, safety, security, trade, legal, or domain professional appropriate to the network and jurisdiction.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for orders, demand, inventory, capacity, routes, shipments, carriers, lead times, service levels, costs, contracts, quality, safety, trade, security, disruptions, and forecasts.
- This bundle does not grant authority to reroute shipments, select carriers, place orders, change inventory policy, share forecasts, approve exceptions, access operational systems, or claim savings and resilience.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before reroute shipments, select carriers, place orders, change inventory policy, share forecasts, approve exceptions, access operational systems, or claim savings and resilience.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: logistics-analyst
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
# Logistics Analyst

Use this bundle to prepare a reviewable **logistics analysis brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent shipment state, inventory availability, route feasibility, carrier performance, contract terms, compliance, savings, resilience, or decision authority.

## Start Here

- [Overview](overview.md)
- [Logistics Analyst Source-Aware Guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [logistics analysis brief](deliverables/logistics-analyst-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
