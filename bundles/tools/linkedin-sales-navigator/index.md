---
type: Bundle Index
title: "LinkedIn Sales Navigator"
description: "Source-aware tool bundle for LinkedIn Sales Navigator account and lead research, lists, CRM evidence, outreach preparation, and controlled sales briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "linkedin-sales-navigator"
  - "sales-intelligence"
  - "prospecting"
  - "tool"
aliases:
  - "LinkedIn Sales Navigator"
problems_solved:
  - "Prepare a sales navigator research brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Sales"
  - "Business services"
  - "Technology"
tools:
  - "LinkedIn Sales Navigator"
frameworks:
  - "source-evidence matrix"
  - "sales-research-and-prospecting evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Sales Navigator research brief"
commands: []
skills: []
evaluations:
  - "LinkedIn Sales Navigator source-awareness check"
okb_bundle_id: linkedin-sales-navigator
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "account-executive-closer"
  - "business-development-representative-bdr"
  - "key-account-manager-account-manager"
  - "sales-development-representative-sdr"
  - "sales-representative-of-services"
  - "technical-sales-representative-technical-and-scientific-products"
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
  - "Use official LinkedIn Sales Navigator sources for general context; local sales research and prospecting, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for seat, edition, and permission scope, search criteria and saved-search settings, lead, account, and list evidence, profile and company source dates, CRM mappings and synchronization state, message, InMail, and outreach approvals, and privacy, suppression, and data-use requirements."
  - "Do not infer profile accuracy, employment, account fit, intent, relationships, CRM state, message eligibility, contact permission."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before saving or changing lists, syncing CRM data, sending messages or InMail, exporting data, or making unsupported personal claims."
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
      baseline_score: 9
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 16/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# LinkedIn Sales Navigator

Source-aware tool bundle for LinkedIn Sales Navigator account and lead research, lists, CRM evidence, outreach preparation, and controlled sales briefs.

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
- [deliverables/linkedin-sales-navigator-brief.md](deliverables/linkedin-sales-navigator-brief.md)
