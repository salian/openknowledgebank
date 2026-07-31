---
type: Bundle Index
title: "Visual Studio Code"
description: "Source-aware tool bundle for Visual Studio Code workspaces, settings, extensions, tasks, debugging, trust, and controlled configuration changes."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "vscode"
  - "developer-tools"
  - "configuration"
  - "tool"
aliases:
  - "Visual Studio Code"
problems_solved:
  - "Prepare a vs code workspace and configuration brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Software"
  - "Information technology"
  - "Education"
tools:
  - "Visual Studio Code"
frameworks:
  - "source-evidence matrix"
  - "editor workspace and development configuration evidence matrix"
  - "qualified-review gate"
deliverables:
  - "VS Code workspace and configuration brief"
commands: []
skills: []
evaluations:
  - "Visual Studio Code source-awareness check"
okb_bundle_id: vscode
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
  - "Use the cited official or primary sources for general editor workspace and development configuration context; local facts, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for VS Code version and build, workspace files and folder scope, user, remote, and workspace settings, extensions and versions, Workspace Trust state, and tasks, launch configurations, terminals, language tooling, and logs."
  - "Do not infer effective setting precedence, extension behavior, workspace trust, task execution state, debug configuration, and local file contents."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before opening an untrusted workspace, installing or enabling extensions, changing files or settings, running tasks or terminals, or syncing settings."
  - "Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 36
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: configuration-risk-review
    baseline_score: 8
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Visual Studio Code

Source-aware tool bundle for Visual Studio Code workspaces, settings, extensions, tasks, debugging, trust, and controlled configuration changes.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

For an empty-evidence request, set the accountable reviewer to `Needs verification`. Do not nominate, designate, or invent a reviewer role.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/vscode-brief.md](deliverables/vscode-brief.md)
