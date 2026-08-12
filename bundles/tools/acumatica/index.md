---
type: "Bundle Index"
title: "Acumatica"
description: "Source-aware guidance for cloud ERP configuration, customization, integrations, data, and controlled business-process changes."
category: tools
version: 0.1.0
tags:
- "acumatica"
- "tool"
- "source-aware"
aliases:
- "Acumatica Cloud ERP"

problems_solved:
- "Review Acumatica use from current official sources and inspected local evidence."
- "Prepare a controlled Acumatica decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Acumatica"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Acumatica configuration and use review brief"
commands: []
skills: []
evaluations:
- "Acumatica source-awareness check"
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
  - "financial"
  - "security"
  - "privacy"
  - "accounting"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, marketing, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for edition and build, tenant, companies and branches, modules, roles, workflows, customizations, endpoints, records, integrations, logs, and approvals."
- "This bundle does not grant authority to change ERP configuration or records, deploy customizations, call production APIs, post transactions, expose credentials, or represent financial approval."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before change ERP configuration or records, deploy customizations, call production APIs, post transactions, expose credentials, or represent financial approval."
timestamp: "2026-08-12T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: acumatica
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
# Acumatica

Use this bundle to prepare a reviewable **Acumatica configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent tenant state, ledger or operational record, permission, customization compatibility, transaction result, control status, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Acumatica configuration and use review brief](deliverables/acumatica-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
