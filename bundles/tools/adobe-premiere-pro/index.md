---
type: Bundle Index
title: "Adobe Premiere Pro"
description: "Source-aware tool bundle for Adobe Premiere Pro media, sequence, edit, audio, color, caption, review, and export evidence with production-ready briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "adobe-premiere-pro"
  - "video-editing"
  - "media-production"
  - "tool"
aliases:
  - "Adobe Premiere Pro"
problems_solved:
  - "Prepare a premiere pro production brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Media"
  - "Marketing"
  - "Entertainment"
tools:
  - "Adobe Premiere Pro"
frameworks:
  - "source-evidence matrix"
  - "video-editing-and-delivery evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Premiere Pro production brief"
commands: []
skills: []
evaluations:
  - "Adobe Premiere Pro source-awareness check"
okb_bundle_id: adobe-premiere-pro
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "social-media-manager-specialist"
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
  - "Use official Adobe Premiere Pro sources for general context; local video editing and delivery, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for project and source media, sequence settings, frame rate, and timebase, edit decisions and version history, audio, color, graphics, and caption requirements, linked assets, fonts, and plugins, review notes and approvals, and delivery codec, container, dimensions, loudness, and destination requirements."
  - "Do not infer media availability, sequence settings, frame rate, edit status, rights, captions, color, export preset."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before relinking or deleting media, overwriting projects, exporting restricted footage, publishing, or replacing approved masters."
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
      baseline_score: 2
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 8
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

# Adobe Premiere Pro

Source-aware tool bundle for Adobe Premiere Pro media, sequence, edit, audio, color, caption, review, and export evidence with production-ready briefs.

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
- [deliverables/adobe-premiere-pro-brief.md](deliverables/adobe-premiere-pro-brief.md)
