---
type: Bundle Index
title: "Accounts Payable / Accounts Receivable Specialist"
description: "Source-aware role bundle for invoice and payment processing, receivables, aging, reconciliations, exception handling, controls, and review-ready AP/AR briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags:
  - "accounts-payable"
  - "accounts-receivable"
  - "financial-operations"
  - "role"
aliases:
  - "Accounts Payable / Accounts Receivable Specialist"
problems_solved:
  - "Prepare a ap/ar operations brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Financial operations"
  - "Commerce"
  - "Professional services"
tools: []
frameworks:
  - "source-evidence matrix"
  - "accounts-payable-and-receivable-operations evidence matrix"
  - "qualified-review gate"
deliverables:
  - "AP/AR operations brief"
commands: []
skills: []
evaluations:
  - "Accounts Payable / Accounts Receivable Specialist source-awareness check"
okb_bundle_id: accounts-payable-accounts-receivable-specialist
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "frc-uk-gaap-standards"
  - "quickbooks-online"
  - "sap-s4hana"
  - "sox"
  - "us-gaap"
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    - "43-3031.00"
  soc: []
  isco_08: []
  esco:
    - "4311"
limitations:
  - "Use official Accounts Payable / Accounts Receivable Specialist sources for general context; local accounts payable and receivable operations, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for approved vendor and customer master data, invoices, bills, credit notes, and purchase orders, receipts and acceptance evidence, payments, remittances, and bank evidence, aging and subledger reports, general-ledger balances, and approval and segregation-of-duties evidence."
  - "Do not infer vendor identity, customer balance, invoice validity, payment status, bank details, aging, tax treatment, approval status."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before creating or changing master data, releasing payments, applying cash, issuing credits, contacting counterparties, or posting entries."
  - "Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: "2026-07-31"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 36
  absolute_lift: 21
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 4
      okb_score: 12
      max_score: 12
    - task: "role-prioritization-review"
      baseline_score: 5
      okb_score: 12
      max_score: 12
    - task: "role-source-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Accounts Payable / Accounts Receivable Specialist

Source-aware role bundle for invoice and payment processing, receivables, aging, reconciliations, exception handling, controls, and review-ready AP/AR briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/accounts-payable-accounts-receivable-specialist-brief.md](deliverables/accounts-payable-accounts-receivable-specialist-brief.md)
