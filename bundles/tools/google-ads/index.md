---
type: Bundle Index
title: "Google Ads"
description: "Source-aware tool bundle for Google Ads campaign planning, conversion and attribution review, budget and bidding analysis, reporting reconciliation, and controlled change briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "google-ads"
  - "paid-search"
  - "advertising"
  - "tool"
aliases:
  - "Google Ads"
problems_solved:
  - "Prepare a google ads decision and change brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Marketing"
  - "Advertising"
  - "Commerce"
tools:
  - "Google Ads"
frameworks:
  - "source-evidence matrix"
  - "paid-advertising-planning-and-performance-review evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Google Ads decision and change brief"
commands: []
skills: []
evaluations:
  - "Google Ads source-awareness check"
okb_bundle_id: google-ads
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "advertising-promotions-manager"
  - "demand-generation-manager"
  - "digital-marketing-analyst"
  - "digital-marketing-manager"
  - "e-commerce-marketing-manager"
  - "growth-marketing-manager"
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
  - "Use official Google Ads sources for general context; local paid advertising planning and performance review, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for account and campaign scope, objectives and conversion-action definitions, targeting, keywords, audiences, and exclusions, ads, assets, landing pages, and approvals, budgets and bidding settings, date, attribution, currency, and reporting settings, and change history and experiment evidence."
  - "Do not infer campaign state, spend, bids, budgets, conversion definitions, targeting, performance, attribution."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before publishing ads, changing targeting, budgets, bids, conversion actions, experiments, billing, or account access."
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
  baseline_score: 18
  okb_score: 36
  absolute_lift: 18
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 3
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 9
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 18/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Google Ads

Source-aware tool bundle for Google Ads campaign planning, conversion and attribution review, budget and bidding analysis, reporting reconciliation, and controlled change briefs.

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
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/google-ads-brief.md](deliverables/google-ads-brief.md)
