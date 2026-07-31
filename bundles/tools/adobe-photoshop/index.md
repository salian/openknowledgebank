---
type: Bundle Index
title: "Adobe Photoshop"
description: "Source-aware tool bundle for Adobe Photoshop document review, non-destructive editing plans, color and asset checks, export specifications, and production-ready creative briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "adobe-photoshop"
  - "image-editing"
  - "creative-production"
  - "tool"
aliases:
  - "Adobe Photoshop"
problems_solved:
  - "Prepare a photoshop production brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Design"
  - "Media"
  - "Marketing"
tools:
  - "Adobe Photoshop"
frameworks:
  - "source-evidence matrix"
  - "image-editing-and-creative-production evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Photoshop production brief"
commands: []
skills: []
evaluations:
  - "Adobe Photoshop source-awareness check"
okb_bundle_id: adobe-photoshop
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
  - "Use official Adobe Photoshop sources for general context; local image editing and creative production, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for source document and linked assets, document dimensions and resolution, layers, masks, smart objects, and text, color mode and profile, brand and accessibility requirements, target channels and export specifications, and review and usage-rights evidence."
  - "Do not infer document structure, asset rights, dimensions, resolution, color profile, fonts, edits, export settings."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before overwriting source files, flattening editable work, exporting or sharing assets, using restricted content, or publishing creative."
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

# Adobe Photoshop

Source-aware tool bundle for Adobe Photoshop document review, non-destructive editing plans, color and asset checks, export specifications, and production-ready creative briefs.

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
- [deliverables/adobe-photoshop-brief.md](deliverables/adobe-photoshop-brief.md)
