---
type: "Bundle Index"
title: "Coupa"
description: "Source-aware guidance for procurement, sourcing, contracts, suppliers, expenses, invoicing, payments, treasury, and spend analytics. and controlled Coupa use."
category: tools
version: 0.1.0
tags:
- "coupa"
- "tool"
- "source-aware"
aliases:
- "Coupa BSM"
- "Coupa Business Spend Management"
problems_solved:
- "Review Coupa use from current official sources and inspected local evidence."
- "Prepare a controlled Coupa decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Coupa"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Coupa configuration and use review brief"
commands: []
skills: []
evaluations:
- "Coupa source-awareness check"
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
  - "accounting"
  - "privacy"
  - "security"
  - "legal"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, clinical, employment, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for subscription and modules, entities and currencies, users and roles, suppliers and bank details, catalogs and contracts, requisitions and purchase orders, invoices and expenses, approvals and policies, tax and accounting mappings, payment state, integrations, AI settings, audit logs, and controls."
- "This bundle does not grant authority to onboard suppliers, change bank details, create or approve requisitions, purchase orders, invoices or expenses, initiate payments, alter controls, export financial data, or represent settlement or compliance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before onboard suppliers, change bank details, create or approve requisitions, purchase orders, invoices or expenses, initiate payments, alter controls, export financial data, or represent settlement or compliance."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: coupa
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
# Coupa

Use this bundle to prepare a reviewable **Coupa configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent supplier identity, bank details, contract terms, account coding, invoice validity, approval authority, payment status, savings, compliance, reconciliation, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Coupa configuration and use review brief](deliverables/coupa-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
