---
type: Bundle Index
title: Payroll Specialist / Administrator
description: Source-aware role bundle for payroll input review, gross-to-net reconciliation, exception handling, period close, employee inquiry support, and approval-ready payroll briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- payroll
- timekeeping
- payroll-reconciliation
- role
aliases:
- Payroll Specialist
- Payroll Administrator
problems_solved:
- Prepare payroll reconciliation and exception brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Payroll
- Human resources
tools: []
frameworks:
- source-evidence matrix
- payroll-evidence matrix
- qualified-review gate
deliverables:
- Payroll reconciliation and exception brief
commands: []
skills: []
evaluations:
- Payroll Specialist / Administrator source-awareness check
okb_bundle_id: payroll-specialist-administrator
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- flsa-minimum-wage-overtime
- quickbooks-online
- sox
- us-gaap
- workday-hcm
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 43-3051.00
  soc: []
  isco_08: []
  esco:
  - '4313'
limitations:
- Use as occupational context; jurisdiction, pay period, employee records, time, earnings, deductions, tax settings, bank files, and approvals require current protected evidence.
- Task-specific work requires current evidence for jurisdiction and pay period, authorized employee master data, approved time and leave, earnings and deduction rules, tax and benefit configuration, prior-period and bank reconciliation, payroll approval and filing authority.
- Do not infer employee data, hours, wages, deductions, tax settings, bank details, payment or filing status.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before personal data, payroll changes, bank files, payments, tax filings, or employee communications.
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
  baseline_score: 15
  okb_score: 32
  absolute_lift: 17
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 8
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Payroll Specialist / Administrator

Source-aware role bundle for payroll input review, gross-to-net reconciliation, exception handling, period close, employee inquiry support, and approval-ready payroll briefs.

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
- [deliverables/payroll-reconciliation-brief.md](deliverables/payroll-reconciliation-brief.md)
