---
type: Bundle Index
title: "Microsoft 365"
description: "Source-aware tool bundle for Microsoft 365 documents, collaboration, sharing, tenant controls, retention, automation, and review-ready work briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "microsoft-365"
  - "productivity"
  - "collaboration"
  - "tool"
aliases:
  - "Microsoft 365"
problems_solved:
  - "Prepare a microsoft 365 work and governance brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Business services"
  - "Education"
  - "Public sector"
tools:
  - "Microsoft 365"
frameworks:
  - "source-evidence matrix"
  - "office-productivity-and-collaboration evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Microsoft 365 work and governance brief"
commands: []
skills: []
evaluations:
  - "Microsoft 365 source-awareness check"
okb_bundle_id: microsoft-365
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "supply-chain-analyst"
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
  - "Use official Microsoft 365 sources for general context; local office productivity and collaboration, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for tenant, subscription, and application scope, file, site, mailbox, team, or workspace identity, document version and content evidence, sharing, membership, and permission state, retention, sensitivity, compliance, and administrator policy, automation and integration configuration, and audit, approval, and source-of-record evidence."
  - "Do not infer tenant configuration, license, file state, permissions, sharing, retention, sensitivity labels, automation."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before sending messages, sharing files, changing content, permissions, retention, labels, tenant settings, or automations."
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

# Microsoft 365

Source-aware tool bundle for Microsoft 365 documents, collaboration, sharing, tenant controls, retention, automation, and review-ready work briefs.

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
- [deliverables/microsoft-365-brief.md](deliverables/microsoft-365-brief.md)
