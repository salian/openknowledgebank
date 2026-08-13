---
type: "Bundle Index"
title: "Azure Synapse Analytics"
description: "Source-aware guidance for integrated data warehousing, big-data processing, data integration, and analytics. and controlled Azure Synapse Analytics use."
category: tools
version: 0.1.0
tags:
- "azure-synapse-analytics"
- "tool"
- "source-aware"
aliases:
- "Azure Synapse"
- "Microsoft Azure Synapse Analytics"
problems_solved:
- "Review Azure Synapse Analytics use from current official sources and inspected local evidence."
- "Prepare a controlled Azure Synapse Analytics decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Azure Synapse Analytics"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Azure Synapse Analytics configuration and use review brief"
commands: []
skills: []
evaluations:
- "Azure Synapse Analytics source-awareness check"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "regulated"
  domains:
  - "privacy"
  - "security"
  - "financial"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, employment, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for Azure subscription, tenant and region, workspace, network boundaries, identities and RBAC, linked services, credentials references, data classifications, SQL and Spark pools, pipelines, notebooks, costs, policies, logs, and recovery state."
- "This bundle does not grant authority to provision or resize resources, connect data sources, execute queries or pipelines, change networking or access, expose secrets or data, delete resources, or represent analytics as validated."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before provision or resize resources, connect data sources, execute queries or pipelines, change networking or access, expose secrets or data, delete resources, or represent analytics as validated."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: azure-synapse-analytics
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: "No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available."
  evidence_note: "No measured score is claimed."
evaluation_detail:
  status: blocked
  next_action: "Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard."
---
# Azure Synapse Analytics

Use this bundle to prepare a reviewable **Azure Synapse Analytics configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent tenant or workspace state, data contents or quality, query or pipeline safety, permissions, cost, execution result, security posture, recovery, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Azure Synapse Analytics configuration and use review brief](deliverables/azure-synapse-analytics-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
