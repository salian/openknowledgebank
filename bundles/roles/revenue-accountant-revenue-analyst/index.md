---
type: Bundle Index
title: "Revenue Accountant / Revenue Analyst"
description: "Source-aware role bundle for contract and order evidence, revenue schedules, close support, reconciliations, controls, and review-ready revenue accounting briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags:
  - "revenue-accounting"
  - "reconciliation"
  - "financial-close"
  - "role"
aliases:
  - "Revenue Accountant / Revenue Analyst"
problems_solved:
  - "Prepare a revenue accounting analysis brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Software"
  - "Professional services"
  - "Commerce"
tools: []
frameworks:
  - "source-evidence matrix"
  - "revenue-accounting-analysis-and-close-decisions evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Revenue accounting analysis brief"
commands: []
skills: []
evaluations:
  - "Revenue Accountant / Revenue Analyst source-awareness check"
okb_bundle_id: revenue-accountant-revenue-analyst
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "asc-606"
  - "frc-uk-gaap-standards"
  - "salesforce-service-cloud"
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
    - "13-2011.00"
  soc: []
  isco_08: []
  esco:
    - "2411"
limitations:
  - "Use official Revenue Accountant / Revenue Analyst sources for general context; local revenue accounting analysis and close decisions, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for executed contracts and amendments, orders, invoices, credits, and collections, applicable accounting policy, performance-obligation analysis, revenue schedules and subledger detail, general-ledger balances, and period and approval evidence."
  - "Do not infer contract terms, performance obligations, transaction price, allocation, recognition timing, journal entries, balances, close status."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before posting entries, changing schedules, closing periods, issuing financial statements, or making accounting-policy conclusions."
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
  baseline_score: 12
  okb_score: 36
  absolute_lift: 24
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 2
      okb_score: 12
      max_score: 12
    - task: "role-prioritization-review"
      baseline_score: 6
      okb_score: 12
      max_score: 12
    - task: "role-source-reconciliation"
      baseline_score: 4
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 12/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Revenue Accountant / Revenue Analyst

Source-aware role bundle for contract and order evidence, revenue schedules, close support, reconciliations, controls, and review-ready revenue accounting briefs.

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
- [deliverables/revenue-accountant-revenue-analyst-brief.md](deliverables/revenue-accountant-revenue-analyst-brief.md)
