---
type: Bundle Index
title: "Zapier"
description: "Source-aware tool bundle for Zapier triggers, actions, data mappings, filters, paths, connections, task history, testing, and controlled automation briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "zapier"
  - "workflow-automation"
  - "integrations"
  - "tool"
aliases:
  - "Zapier"
problems_solved:
  - "Prepare a zapier automation brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Business operations"
  - "Marketing"
  - "Sales"
tools:
  - "Zapier"
frameworks:
  - "source-evidence matrix"
  - "workflow-automation-planning-and-review evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Zapier automation brief"
commands: []
skills: []
evaluations:
  - "Zapier source-awareness check"
okb_bundle_id: zapier
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "customer-success-operations-manager-cs-ops"
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
  - "Use official Zapier sources for general context; local workflow automation planning and review, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for account, plan, workspace, and ownership scope, trigger and action app versions, connection and permission boundaries, field schemas, sample data, mappings, filters, paths, and delays, test records, task history, errors, and replay evidence, privacy, retention, rate, and usage requirements, and publish, rollback, and approval evidence."
  - "Do not infer trigger behavior, action behavior, field mappings, connections, sample data, task history, usage, published state."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before testing with live data, turning automations on, replaying tasks, changing connections, sending messages, modifying records, or incurring usage."
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
      baseline_score: 2
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 8
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

# Zapier

Source-aware tool bundle for Zapier triggers, actions, data mappings, filters, paths, connections, task history, testing, and controlled automation briefs.

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
- [deliverables/zapier-brief.md](deliverables/zapier-brief.md)
