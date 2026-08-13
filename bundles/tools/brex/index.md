---
type: "Bundle Index"
title: "Brex"
description: "Source-aware guidance for cards, expenses, travel, reimbursements, budgets, vendors, payments, accounts, and financial workflows. and controlled Brex use."
category: tools
version: 0.1.0
tags:
- "brex"
- "tool"
- "source-aware"
aliases:
- "Brex platform"
- "Brex API"
problems_solved:
- "Review Brex use from current official sources and inspected local evidence."
- "Prepare a controlled Brex decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Brex"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Brex configuration and use review brief"
commands: []
skills: []
evaluations:
- "Brex source-awareness check"
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
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, employment, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for Brex product and API version, organization, users and roles, departments and locations, cards and limits, budgets, policies, expenses and receipts, vendors, bank details, payments, accounts, transactions, statements, credentials, webhooks, integrations, and audit logs."
- "This bundle does not grant authority to create users or cards, change limits or budgets, submit or approve expenses, add vendors or bank details, initiate payments, move funds, use credentials, or represent settlement."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before create users or cards, change limits or budgets, submit or approve expenses, add vendors or bank details, initiate payments, move funds, use credentials, or represent settlement."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: brex
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
# Brex

Use this bundle to prepare a reviewable **Brex configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent user or vendor identity, card or account state, policy compliance, receipt validity, budget availability, approval authority, transaction classification, payment status, settlement, or accounting approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Brex configuration and use review brief](deliverables/brex-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
