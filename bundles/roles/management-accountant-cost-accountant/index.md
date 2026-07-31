---
type: Bundle Index
title: Management Accountant (Cost Accountant)
description: Source-aware role bundle for cost accounting, management reporting, budgeting, variance analysis, allocation review, and qualified-accountant-ready decision support.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- management-accounting
- cost-accounting
- variance-analysis
- role
aliases:
- Management Accountant
- Cost Accountant
problems_solved:
- Prepare cost and management accounting decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Accounting
- Finance
tools: []
frameworks:
- source-evidence matrix
- cost-evidence matrix
- qualified-review gate
deliverables:
- Cost and management accounting decision brief
commands: []
skills: []
evaluations:
- Management Accountant (Cost Accountant) source-awareness check
okb_bundle_id: management-accountant-cost-accountant
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- frc-uk-gaap-standards
- microsoft-power-bi
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
  - 13-2011.00
  soc: []
  isco_08: []
  esco:
  - '2411'
limitations:
- Use as occupational context; entities, periods, balances, cost objects, allocation methods, policies, controls, and approvals require current authoritative evidence.
- Task-specific work requires current evidence for entity, period, and currency, chart of accounts and cost objects, ledger and subledger evidence, approved costing and allocation policy, operational drivers, budget and actual definitions, controls and review authority.
- Do not infer balances, cost drivers, allocation rates, journal entries, materiality, control results, approval.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before journal posting, financial reporting, allocation policy, controls, tax, or management reliance.
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
  baseline_score: 10
  okb_score: 34
  absolute_lift: 24
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 10/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Management Accountant (Cost Accountant)

Source-aware role bundle for cost accounting, management reporting, budgeting, variance analysis, allocation review, and qualified-accountant-ready decision support.

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
- [deliverables/management-accounting-brief.md](deliverables/management-accounting-brief.md)
