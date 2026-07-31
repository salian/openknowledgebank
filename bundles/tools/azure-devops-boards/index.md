---
type: Bundle Index
title: Azure DevOps Boards
description: Source-aware tool bundle for work item, backlog, board, iteration, area, query, WIQL, process, workflow, and reporting review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: tools
version: 0.1.0
tags:
- azure-devops-boards
- tool
- source-aware
aliases:
- Azure DevOps Boards
problems_solved:
- Prepare a azure devops boards review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools:
- Azure DevOps Boards
frameworks:
- source-evidence matrix
- Azure DevOps Boards application matrix
- qualified-review gate
deliverables:
- Azure DevOps Boards review brief
commands: []
skills: []
evaluations:
- Azure DevOps Boards source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- jira
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
- Use the listed authoritative or identified source surfaces for general Azure DevOps Boards guidance; local facts, configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for organization and project, process model, work-item types and fields, area and iteration paths, board columns and states, query or WIQL, permissions, links, history, reporting definitions, dates, owners, and approvals.
- Do not infer work-item state, owner, priority, estimate, query result, process behavior, delivery status, or metric meaning.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that create, edit, move, link, bulk-update, or delete work items; change process, fields, states, areas, iterations, boards, queries, permissions, or notifications.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: azure-devops-boards
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 14
  okb_score: 34
  absolute_lift: 20
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: configuration-risk-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Azure DevOps Boards

Source-aware tool bundle for work item, backlog, board, iteration, area, query, WIQL, process, workflow, and reporting review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and domain actions prohibited without explicit approval.
5. **Source note** - name authoritative source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role.

Facts explicitly stated in the request belong under `Provided` as `Prompt-provided request`; do not move them to `Assumed`. Do not assign an owner, author, date, or version unless the request states it.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/azure-devops-boards-brief.md](deliverables/azure-devops-boards-brief.md)
