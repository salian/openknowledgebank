---
type: Bundle Index
title: Web Analytics / Marketing Data Specialist
description: Source-aware role bundle for measurement planning, implementation review, web-data reconciliation, KPI analysis, and decision-ready analytics briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- web-analytics
- marketing-data
- measurement
- role
aliases:
- Web Analytics Specialist
- Marketing Data Specialist
problems_solved:
- Plan analytics without pretending to access an account.
- Reconcile conflicting web metrics and definitions.
- Produce decision-ready analysis with explicit instrumentation gaps.
industries:
- Marketing
- Digital products
tools: []
frameworks:
- source-evidence matrix
- measurement-evidence matrix
- qualified-review gate
deliverables:
- Web analytics measurement and reconciliation brief
commands: []
skills: []
evaluations:
- Web Analytics / Marketing Data Specialist source-awareness check
okb_bundle_id: web-analytics-marketing-data-specialist
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ccpa
- gdpr
- mixpanel
- tableau
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1161.01
  soc: []
  isco_08: []
  esco:
  - '2431.4'
limitations:
- Environment-specific analysis requires current implementation, consent, schema, filter, identity, and export evidence.
- This bundle does not establish legal privacy compliance.
- Do not infer events, metrics, traffic, conversions, attribution, or configuration state.
safety_notes:
- Minimize identifiers and customer-level data.
- Require confirmation before changing tags, consent settings, destinations, or production analytics configuration.
- Route privacy and compliance decisions to accountable reviewers.
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
  okb_score: 34
  absolute_lift: 23
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Web Analytics / Marketing Data Specialist

Source-aware role bundle for measurement planning, implementation review, web-data reconciliation, KPI analysis, and decision-ready analytics briefs.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/web-analytics-measurement-brief.md](deliverables/web-analytics-measurement-brief.md)
