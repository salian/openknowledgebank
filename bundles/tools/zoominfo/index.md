---
type: Bundle Index
title: "ZoomInfo"
description: "Source-aware tool bundle for ZoomInfo company and contact research, filters, intent, lists, CRM evidence, enrichment, and controlled prospecting briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "zoominfo"
  - "sales-intelligence"
  - "business-data"
  - "tool"
aliases:
  - "ZoomInfo"
problems_solved:
  - "Prepare a zoominfo research and data-use brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Sales"
  - "Marketing"
  - "Business services"
tools:
  - "ZoomInfo"
frameworks:
  - "source-evidence matrix"
  - "business-data-and-sales-intelligence evidence matrix"
  - "qualified-review gate"
deliverables:
  - "ZoomInfo research and data-use brief"
commands: []
skills: []
evaluations:
  - "ZoomInfo source-awareness check"
okb_bundle_id: zoominfo
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "account-executive-closer"
  - "business-development-representative-bdr"
  - "sales-development-representative-sdr"
  - "sales-representative-of-services"
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
  - "Use official ZoomInfo sources for general context; local business data and sales intelligence, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for product edition, license, and data entitlement, company, contact, and search criteria, record source date and confidence evidence, intent, scoops, signals, and definition scope, lists, workflows, enrichment, and CRM mappings, suppression, privacy, and permitted-use requirements, and export, outreach, and approval evidence."
  - "Do not infer record accuracy, employment, contactability, intent, company fit, CRM state, consent, data entitlement."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before exporting or enriching records, syncing CRM data, launching outreach, changing workflows, or making unsupported personal claims."
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
  baseline_score: 16
  okb_score: 36
  absolute_lift: 20
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 1
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 10
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 5
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 16/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# ZoomInfo

Source-aware tool bundle for ZoomInfo company and contact research, filters, intent, lists, CRM evidence, enrichment, and controlled prospecting briefs.

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
- [deliverables/zoominfo-brief.md](deliverables/zoominfo-brief.md)
