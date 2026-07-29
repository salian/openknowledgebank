---
type: Bundle Index
title: Paralegal / Legal Assistant
description: Source-aware role bundle for legal research, record review, document preparation, matter organization, and attorney-review-ready support.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- paralegal
- legal-research
- legal-documents
- role
aliases:
- Paralegal
- Legal Assistant
problems_solved:
- Organize legal research without fabricating authorities.
- Separate matter facts from assumptions and missing records.
- Prepare attorney-review-ready drafts with visible limitations.
industries:
- Legal services
tools: []
frameworks:
- source-evidence matrix
- matter-evidence matrix
- qualified-review gate
deliverables:
- Source-aware legal research and document-preparation brief
commands: []
skills: []
evaluations:
- Paralegal / Legal Assistant source-awareness check
okb_bundle_id: paralegal-legal-assistant
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- hipaa
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 23-2011.00
  soc: []
  isco_08: []
  esco:
  - '3411'
limitations:
- This bundle supports legal work under qualified supervision; it is not legal advice or representation.
- Matter-specific work requires current jurisdiction, authorities, records, deadlines, and attorney instructions.
- Do not infer citations, holdings, client facts, filing status, or legal conclusions.
safety_notes:
- Minimize privileged, confidential, personal, and regulated information.
- Require attorney confirmation before filing, sending, signing, or relying on legal work.
- Verify citations and source versions against authoritative legal sources.
timestamp: '2026-07-29T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-29'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 29
  absolute_lift: 14
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 9
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 7
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 29/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Paralegal / Legal Assistant

Source-aware role bundle for legal research, record review, document preparation, matter organization, and attorney-review-ready support.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-legal-support-brief.md](deliverables/source-aware-legal-support-brief.md)
