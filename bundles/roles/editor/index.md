---
type: Bundle Index
title: Editor
description: Source-aware role bundle for editorial review, revision planning, style
  consistency, fact-check triage, and publication-readiness review.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- editing
- editorial
- writing
- review
- role
aliases:
- Editor
- Content Editor
- Editorial Reviewer
problems_solved:
- Turn draft text, source material, style guidance, and publication goals into a reviewable
  editorial plan.
- Separate verified source facts, author-provided claims, assumptions, and missing
  evidence before revising or approving copy.
- Improve clarity, consistency, structure, and publication readiness without inventing
  facts or silently changing meaning.
industries:
- General
tools: []
frameworks:
- source-evidence matrix
- meaning-preservation review
- publication-readiness gate
deliverables:
- Source-aware editorial review
commands: []
skills: []
evaluations:
- Editorial source-awareness check
okb_bundle_id: editor
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- content-marketing-manager-content-strategist
- can-spam
- ftc-endorsement-and-review-integrity-rules
- gdpr
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 27-3041.00
  soc: []
  isco_08: []
  esco:
  - '2642.2'
limitations:
- This bundle supports editorial review and revision planning; it is not legal, medical,
  financial, scientific, compliance, or publication approval.
- Fact-sensitive edits require current source material, author intent, citation evidence,
  rights/licensing review, and accountable publication review.
- Do not invent facts, citations, quotations, permissions, claims, endorsements, or
  publication approvals.
safety_notes:
- Minimize personal, customer, confidential, unpublished, and rights-restricted material
  in prompts and examples.
- Require explicit confirmation before publishing, submitting, sending, licensing,
  attributing, or materially changing author meaning.
- Route legal, compliance, medical, scientific, brand, rights, and reputational issues
  to accountable reviewers.
timestamp: '2026-07-11T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-11'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 1
  max_score: 12
  baseline_score: 4
  okb_score: 9
  absolute_lift: 5
  task_scores:
  - task: source-aware-edit-review
    baseline_score: 4
    okb_score: 9
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 4/12 to 9/12 across 1 benchmark
    tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Editor

Source-aware role bundle for editorial review, revision planning, style consistency, fact-check triage, and publication-readiness review.

## Required Answer Habit

Include a short **Source note** naming the draft/source evidence, style or publication guidance, author-provided context, assumptions, and missing verification still needed before publication reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-edit-review.md](workflows/source-aware-edit-review.md)
- [deliverables/source-aware-editorial-review.md](deliverables/source-aware-editorial-review.md)
