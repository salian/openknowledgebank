---
type: Bundle Index
title: "Kirkpatrick Model"
description: "Source-aware framework bundle for evaluating learning programs across reaction, learning, behavior, results, and the current model's performance-environment evidence."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: frameworks
tags:
  - "kirkpatrick-model"
  - "training-evaluation"
  - "learning-analytics"
  - "framework"
aliases:
  - "Kirkpatrick Model"
problems_solved:
  - "Prepare a kirkpatrick evaluation design brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Education"
  - "Training"
  - "Human resources"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "learning-program evaluation application matrix"
  - "qualified-review gate"
deliverables:
  - "Kirkpatrick evaluation design brief"
commands: []
skills: []
evaluations:
  - "Kirkpatrick Model source-awareness check"
okb_bundle_id: kirkpatrick-four-levels-of-evaluation
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
  - "Use the cited official or primary sources for general learning-program evaluation context; local facts, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for current model version and official definitions, target organizational results, critical behaviors and performance environment, learning outcomes and assessment evidence, reaction and engagement evidence, and baseline, timing, comparison, confounders, and data quality."
  - "Do not infer model version, target result, behavior change, learning gain, participant reaction, and attribution."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before claiming causality or return on investment, changing programs, monitoring employees, or making personnel decisions without appropriate evidence and review."
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

# Kirkpatrick Model

Source-aware framework bundle for evaluating learning programs across reaction, learning, behavior, results, and the current model's performance-environment evidence.

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
- [deliverables/kirkpatrick-four-levels-of-evaluation-brief.md](deliverables/kirkpatrick-four-levels-of-evaluation-brief.md)
