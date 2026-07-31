---
type: Bundle Index
title: "Slack"
description: "Source-aware tool bundle for Slack workspace, channel, message, app, permission, retention, workflow, and controlled communication briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "slack"
  - "team-communication"
  - "collaboration"
  - "tool"
aliases:
  - "Slack"
problems_solved:
  - "Prepare a slack communication and governance brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Business services"
  - "Software"
  - "Education"
tools:
  - "Slack"
frameworks:
  - "source-evidence matrix"
  - "team-communication-and-collaboration evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Slack communication and governance brief"
commands: []
skills: []
evaluations:
  - "Slack source-awareness check"
okb_bundle_id: slack
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "account-manager-client-relationship-manager"
  - "customer-support-engineer-product-support-engineer"
  - "customer-support-team-lead-supervisor"
  - "technical-account-manager-tam"
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
  - "Use official Slack sources for general context; local team communication and collaboration, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for workspace, organization, channel, and thread scope, message content, timestamp, author, and edit state, membership, roles, and permissions, apps, scopes, tokens, workflows, and integrations, retention, legal hold, export, and administrator policy, notification and communication approvals, and audit and source-of-record evidence."
  - "Do not infer workspace state, channel membership, message content, permissions, app scopes, retention, export availability, approval."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before sending or editing messages, inviting users, changing channels, permissions, retention, apps, workflows, tokens, or exports."
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
      baseline_score: 1
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 9
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 5
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Slack

Source-aware tool bundle for Slack workspace, channel, message, app, permission, retention, workflow, and controlled communication briefs.

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
- [deliverables/slack-brief.md](deliverables/slack-brief.md)
