---
type: Bundle Index
title: Kanban Pull System
description: Source-aware framework bundle for designing and reviewing pull-based flow using demand, replenishment, work-state, capacity, queue, signal, quality, and safety evidence.
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
- kanban
- pull-system
- flow
- framework
aliases:
- Kanban Pull System
problems_solved:
- Prepare a kanban pull-system design brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Manufacturing
- Software
- Operations
tools: []
frameworks:
- source-evidence matrix
- pull-based workflow and replenishment review matrix
- qualified-review gate
deliverables:
- Kanban pull-system design brief
commands: []
skills: []
evaluations:
- Kanban Pull System source-awareness check
okb_bundle_id: kanban-pull-system
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
- Use the cited official, originator, standards, or professional sources for general pull-based workflow and replenishment context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for customer demand and service expectations, workflow states, entry and exit policies, capacity, work-in-progress, queue, and lead-time evidence, replenishment point, quantity, signal, and ownership, blocked work, defects, dependencies, and exceptions, and experiment, safety, quality, and review evidence.
- Do not infer demand, capacity, work state, replenishment need, flow constraint, and change effect.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before changing production flow, inventory, work limits, staffing, service commitments, or safety and quality controls without accountable approval.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 22
  okb_score: 36
  absolute_lift: 14
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 6
    okb_score: 12
    max_score: 12
  - task: framework-application-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 22/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Kanban Pull System

Source-aware framework bundle for designing and reviewing pull-based flow using demand, replenishment, work-state, capacity, queue, signal, quality, and safety evidence.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

## Start Here

- [overview.md](overview.md)
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/kanban-pull-system-brief.md](deliverables/kanban-pull-system-brief.md)
