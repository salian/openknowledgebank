---
type: Bundle Index
title: Content Marketing Manager / Content Strategist
description: Source-aware role bundle for content strategy, editorial planning, SEO-informed
  briefs, governance, and performance review.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- content
- marketing
- strategy
- editorial
- role
aliases:
- Content Marketing Manager
- Content Strategist
- Editorial Strategy Lead
problems_solved:
- Turn business goals, audience evidence, channel constraints, and source material
  into a reviewable content strategy.
- Create briefs and editorial plans that separate verified facts, assumptions, user-provided
  claims, and missing evidence.
- Review content performance without confusing channel metrics, attribution limits,
  or compliance review needs.
industries:
- General
tools: []
frameworks:
- source-evidence matrix
- audience-intent map
- editorial governance gate
deliverables:
- Source-aware content strategy brief
commands: []
skills: []
evaluations:
- Content strategy source-awareness check
okb_bundle_id: content-marketing-manager-content-strategist
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- can-spam
- ftc-endorsement-and-review-integrity-rules
- gdpr
- hubspot-sales-hub
- seo-specialist-consultant
- performance-marketing-manager
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-2021.00
  soc: []
  isco_08: []
  esco:
  - http://data.europa.eu/esco/occupation/6fcf4638-e7c7-4978-9302-9a7b63a3d57c
limitations:
- This bundle supports content strategy and planning; it is not legal, advertising,
  privacy, financial, medical, or professional advice.
- Campaign-specific recommendations require current audience data, product facts,
  brand guidance, channel rules, and qualified review.
- Do not invent customer claims, product capabilities, regulatory statements, performance
  results, citations, or endorsement disclosures.
safety_notes:
- Minimize customer, lead, employee, and account data in prompts and examples.
- Require explicit confirmation before publishing content, changing campaigns, sending
  messages, exporting lists, or spending budget.
- Route regulated claims, endorsements, privacy statements, and legal/compliance-sensitive
  copy to the accountable reviewer.
timestamp: '2026-07-11T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-11'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 19
  okb_score: 32
  absolute_lift: 13
  task_scores:
  - task: empty-evidence-content-brief
    baseline_score: 2
    okb_score: 9
    max_score: 12
  - task: evidence-classification-content-brief
    baseline_score: 9
    okb_score: 11
    max_score: 12
  - task: content-metric-reconciliation
    baseline_score: 8
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 19/36 to 32/36 across 3 benchmark
    tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Content Marketing Manager / Content Strategist

Source-aware role bundle for content strategy, editorial planning, SEO-informed briefs, governance, and performance review.

## Required Answer Habit

Include a short **Source note** naming the authoritative source category, user-provided evidence used, assumptions, and missing facts still needed before publication or strategic reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-content-strategy-brief.md](deliverables/source-aware-content-strategy-brief.md)
