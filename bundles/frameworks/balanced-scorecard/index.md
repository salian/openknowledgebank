---
type: Bundle Index
title: "Balanced Scorecard"
description: "Source-aware framework bundle for translating strategy into balanced objectives, causal hypotheses, measures, targets, initiatives, ownership, and reviewable decisions."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: frameworks
tags:
  - "balanced-scorecard"
  - "strategy"
  - "performance-management"
  - "framework"
aliases:
  - "Balanced Scorecard"
problems_solved:
  - "Prepare a balanced scorecard design and review brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Business services"
  - "Government"
  - "Healthcare"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "strategy execution and performance measurement application matrix"
  - "qualified-review gate"
deliverables:
  - "balanced scorecard design and review brief"
commands: []
skills: []
evaluations:
  - "Balanced Scorecard source-awareness check"
okb_bundle_id: balanced-scorecard
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
  - "Use the cited official or primary sources for general strategy execution and performance measurement context; local facts, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for strategy, scope, and framework interpretation, objectives and perspective assignment, causal hypotheses and dependencies, measure definitions, formulas, sources, baselines, and targets, initiatives, owners, resources, and timing, and review cadence, decisions, and observed results."
  - "Do not infer strategic objective, causal relationship, metric definition, baseline, target feasibility, and initiative effect."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before committing targets or resources, publishing performance claims, changing strategy, or making personnel decisions without accountable review."
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
  baseline_score: 18
  okb_score: 36
  absolute_lift: 18
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: framework-application-review
    baseline_score: 8
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 18/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Balanced Scorecard

Source-aware framework bundle for translating strategy into balanced objectives, causal hypotheses, measures, targets, initiatives, ownership, and reviewable decisions.

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
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/balanced-scorecard-brief.md](deliverables/balanced-scorecard-brief.md)
