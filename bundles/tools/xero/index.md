---
type: Bundle Index
title: "Xero"
description: "Source-aware tool bundle for Xero organizations, ledgers, invoices, bills, payments, bank reconciliation, reports, tax settings, integrations, and controlled accounting actions."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "xero"
  - "accounting"
  - "reconciliation"
  - "tool"
aliases:
  - "Xero"
problems_solved:
  - "Prepare a xero accounting and reconciliation brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Accounting"
  - "Small business"
  - "Financial services"
tools:
  - "Xero"
frameworks:
  - "source-evidence matrix"
  - "cloud accounting records and reporting evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Xero accounting and reconciliation brief"
commands: []
skills: []
evaluations:
  - "Xero source-awareness check"
okb_bundle_id: xero
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Use the cited official or primary sources for general cloud accounting records and reporting context; local facts, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for organization, tenant, region, and accounting period, chart of accounts and tax rates, contacts, invoices, bills, payments, bank transactions, and journals, report definition, filters, and as-of date, lock dates and approval workflow, and API connection and granted scopes."
  - "Do not infer ledger accuracy, payment status, bank match, tax treatment, report completeness, and scope authorization."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before posting or updating transactions, recording payments, reconciling bank items, changing tax or lock dates, changing scopes, or exporting financial data."
  - "Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: configuration-risk-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Xero

Source-aware tool bundle for Xero organizations, ledgers, invoices, bills, payments, bank reconciliation, reports, tax settings, integrations, and controlled accounting actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

For an empty-evidence request, set the accountable reviewer to `Needs verification`. Do not nominate, designate, or invent a reviewer role.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/xero-brief.md](deliverables/xero-brief.md)
