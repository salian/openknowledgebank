---
type: Bundle Index
title: Financial Controller
description: Source-aware role bundle for financial close and reporting oversight, controls, cash and budget review, policy governance, and qualified-review-ready controller briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- financial-control
- controllership
- internal-controls
- role
aliases:
- Financial Controller
- Controller
problems_solved:
- Prepare controller close, reporting, and control brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Finance
- Accounting
tools: []
frameworks:
- source-evidence matrix
- controller-evidence matrix
- qualified-review gate
deliverables:
- Controller close, reporting, and control brief
commands: []
skills: []
evaluations:
- Financial Controller source-awareness check
okb_bundle_id: financial-controller
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- frc-uk-gaap-standards
- quickbooks-online
- sap-s4hana
- sox
- us-gaap
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-3031.01
  soc: []
  isco_08: []
  esco:
  - '1211'
limitations:
- Use as occupational context; entities, periods, ledgers, statements, policies, controls, cash, budgets, approvals, and filings require current authoritative evidence.
- Task-specific work requires current evidence for entity, period, currency, and framework, trial balance and subledger evidence, reconciliations and journal support, approved accounting policies, control design and execution evidence, cash, budget, and forecast definitions, review, payment, and filing authority.
- Do not infer balances, journal entries, financial statements, cash position, forecast, control results, approval, filing status.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before financial reporting, journals, payments, cash, controls, filings, tax, or management reliance.
- Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 12
  okb_score: 33
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 12/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Financial Controller

Source-aware role bundle for financial close and reporting oversight, controls, cash and budget review, policy governance, and qualified-review-ready controller briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts
and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/financial-controller-brief.md](deliverables/financial-controller-brief.md)
