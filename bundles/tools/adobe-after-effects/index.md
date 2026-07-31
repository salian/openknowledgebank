---
type: Bundle Index
title: "Adobe After Effects"
description: "Source-aware tool bundle for Adobe After Effects composition, asset, animation, expression, render, review, and delivery evidence with production briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "adobe-after-effects"
  - "motion-graphics"
  - "visual-effects"
  - "tool"
aliases:
  - "Adobe After Effects"
problems_solved:
  - "Prepare a after effects production brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Media"
  - "Design"
  - "Entertainment"
tools:
  - "Adobe After Effects"
frameworks:
  - "source-evidence matrix"
  - "motion-graphics-and-visual-effects-production evidence matrix"
  - "qualified-review gate"
deliverables:
  - "After Effects production brief"
commands: []
skills: []
evaluations:
  - "Adobe After Effects source-awareness check"
okb_bundle_id: adobe-after-effects
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
  - "Use official Adobe After Effects sources for general context; local motion graphics and visual effects production, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for project, compositions, and render scope, dimensions, frame rate, duration, and color settings, footage, fonts, plugins, expressions, and linked assets, animation and effect requirements, review notes and approved versions, render settings, output module, codec, and destination, and usage rights and delivery approvals."
  - "Do not infer composition settings, assets, fonts, plugins, expressions, render settings, rights, approval state."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before replacing assets, changing approved compositions, overwriting projects, rendering restricted content, or publishing deliverables."
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
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
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
      baseline_score: 7
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Adobe After Effects

Source-aware tool bundle for Adobe After Effects composition, asset, animation, expression, render, review, and delivery evidence with production briefs.

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
- [deliverables/adobe-after-effects-brief.md](deliverables/adobe-after-effects-brief.md)
