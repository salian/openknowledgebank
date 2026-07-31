---
type: Bundle Index
title: "Google Docs / Google Workspace"
description: "Source-aware tool bundle for Google Docs and Workspace document collaboration, review, sharing, version, automation, and governance evidence."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "google-workspace"
  - "google-docs"
  - "document-collaboration"
  - "tool"
aliases:
  - "Google Docs / Google Workspace"
problems_solved:
  - "Prepare a google workspace document brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Business services"
  - "Education"
  - "Nonprofit"
tools:
  - "Google Docs / Google Workspace"
frameworks:
  - "source-evidence matrix"
  - "collaborative-document-creation-and-review evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Google Workspace document brief"
commands: []
skills: []
evaluations:
  - "Google Docs / Google Workspace source-awareness check"
okb_bundle_id: google-workspace-docs
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "copywriter-content-writer"
  - "editor"
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
  - "Use official Google Docs / Google Workspace sources for general context; local collaborative document creation and review, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for document identity, owner, and version, content, comments, suggestions, and approvals, sharing, access, and link settings, workspace and administrator policy, templates, add-ons, scripts, and integrations, retention, classification, and export requirements, and source-of-record and publication destination."
  - "Do not infer document content, version, owner, permissions, comments, suggestions, admin policy, publication status."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before editing documents, accepting suggestions, resolving comments, sharing, changing ownership, exporting, sending, or publishing."
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
      baseline_score: 9
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

# Google Docs / Google Workspace

Source-aware tool bundle for Google Docs and Workspace document collaboration, review, sharing, version, automation, and governance evidence.

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
- [deliverables/google-docs-google-workspace-brief.md](deliverables/google-docs-google-workspace-brief.md)
