---
type: Bundle Index
title: "Adobe Acrobat / Adobe Document Cloud"
description: "Source-aware tool bundle for Adobe Acrobat and Document Cloud PDF creation, review, forms, signatures, OCR, accessibility, redaction, and controlled delivery."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "adobe-acrobat"
  - "pdf"
  - "document-workflows"
  - "tool"
aliases:
  - "Adobe Acrobat / Adobe Document Cloud"
problems_solved:
  - "Prepare a acrobat document workflow brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Business services"
  - "Legal services"
  - "Public sector"
tools:
  - "Adobe Acrobat / Adobe Document Cloud"
frameworks:
  - "source-evidence matrix"
  - "pdf-document-workflows evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Acrobat document workflow brief"
commands: []
skills: []
evaluations:
  - "Adobe Acrobat / Adobe Document Cloud source-awareness check"
okb_bundle_id: adobe-acrobat-document-cloud
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
  - "Use official Adobe Acrobat / Adobe Document Cloud sources for general context; local PDF document workflows, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for source document and authoritative version, PDF structure, metadata, forms, and attachments, signature and certificate requirements, OCR, accessibility, and reading-order evidence, redaction and sensitive-data requirements, permissions, sharing, and review state, and export, retention, and delivery specifications."
  - "Do not infer document version, form fields, signatures, OCR quality, accessibility, redactions, permissions, delivery state."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before signing, sending, sharing, redacting, certifying, changing permissions, overwriting originals, or publishing documents."
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

# Adobe Acrobat / Adobe Document Cloud

Source-aware tool bundle for Adobe Acrobat and Document Cloud PDF creation, review, forms, signatures, OCR, accessibility, redaction, and controlled delivery.

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
- [deliverables/adobe-acrobat-adobe-document-cloud-brief.md](deliverables/adobe-acrobat-adobe-document-cloud-brief.md)
