---
type: Bundle Index
title: Sales Compensation / Incentive Analyst
description: Source-aware role bundle for sales incentive plan analysis, crediting, payout reconciliation, and governance, evidence reconciliation, reviewable recommendations, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- sales-compensation-incentive-analyst
- sales
- role
aliases:
- Sales Compensation / Incentive Analyst
problems_solved:
- Prepare a sales compensation analysis brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Sales
- Revenue operations
tools: []
frameworks:
- source-evidence matrix
- sales incentive plan analysis, crediting, payout reconciliation, and governance review matrix
- qualified-review gate
deliverables:
- sales compensation analysis brief
commands: []
skills: []
evaluations:
- Sales Compensation / Incentive Analyst source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- asc-606
- salesforce-service-cloud
- sox
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1141.00
  soc: []
  isco_08: []
  esco:
  - '2423'
limitations:
- Use the cited authoritative sources for general role, standards, or regulatory context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for plan, period, population, territory, quota, and eligibility; CRM, bookings, crediting, and source-system data; plan document and version; calculations, adjustments, disputes, protected employee data, pay-equity review, communication, and approvals.
- Do not infer eligibility, attainment, credit, payout, dispute outcome, fairness, or legal compliance.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, and other sensitive data.
- Require explicit confirmation before actions that change a plan, quota, credit, payout, or employee record, or communicate compensation decisions.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: sales-compensation-incentive-analyst
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 20
  okb_score: 36
  absolute_lift: 16
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 20/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Sales Compensation / Incentive Analyst

Source-aware role bundle for sales incentive plan analysis, crediting, payout reconciliation, and governance, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

Facts explicitly stated in the request belong under `Provided`, including the label `Prompt-provided request`. Do not move them to `Assumed`. Do not assign an owner, author, date, or version to a provided artifact unless the request states it. Mark each absent field `Needs verification`.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/sales-compensation-incentive-analyst-brief.md](deliverables/sales-compensation-incentive-analyst-brief.md)
