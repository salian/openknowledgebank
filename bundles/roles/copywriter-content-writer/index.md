---
type: Bundle Index
title: Copywriter / Content Writer
description: Source-aware role bundle for audience research, evidence-bounded copy drafting, brand-voice alignment, editorial review, and publication-ready handoff.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- copywriting
- content-writing
- editorial
- role
aliases:
- Copywriter
- Content Writer
problems_solved:
- Draft persuasive copy without fabricated proof.
- Align copy to evidence, audience, and brand constraints.
- Prepare publication-ready handoffs with claim review.
industries:
- Marketing
- Media
tools: []
frameworks:
- source-evidence matrix
- claim-evidence matrix
- qualified-review gate
deliverables:
- Source-aware copy and editorial brief
commands: []
skills: []
evaluations:
- Copywriter / Content Writer source-awareness check
okb_bundle_id: copywriter-content-writer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ftc-endorsement-and-review-integrity-rules
- gdpr
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 27-3043.00
  soc: []
  isco_08: []
  esco:
  - '2641.2'
limitations:
- Draft quality depends on current audience, product, brand, channel, and source evidence.
- This bundle is not legal, regulatory, medical, or financial review.
- Do not invent claims, quotations, citations, results, awards, or permissions.
safety_notes:
- Minimize personal and customer information.
- Require confirmation before publishing, sending, or changing live content.
- Route regulated, comparative, endorsement, privacy, and rights-sensitive claims to qualified review.
timestamp: '2026-07-29T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-29'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 11
  okb_score: 31
  absolute_lift: 20
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 10
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 3
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 5
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Copywriter / Content Writer

Source-aware role bundle for audience research, evidence-bounded copy drafting, brand-voice alignment, editorial review, and publication-ready handoff.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-copy-brief.md](deliverables/source-aware-copy-brief.md)
