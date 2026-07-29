---
type: Bundle Index
title: Demand Generation Manager
description: Source-aware role bundle for demand strategy, campaign planning, funnel-evidence review, nurture design, and budget-owner-ready recommendations.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- demand-generation
- campaigns
- funnel
- role
aliases:
- Demand Generation Manager
- Demand Gen Manager
problems_solved:
- Plan demand programs without invented funnel performance.
- Separate campaign hypotheses from measured results.
- Prepare launch recommendations with consent and budget gates.
industries:
- Marketing
- B2B
tools: []
frameworks:
- source-evidence matrix
- funnel-evidence matrix
- qualified-review gate
deliverables:
- Demand generation campaign and evidence brief
commands: []
skills: []
evaluations:
- Demand Generation Manager source-awareness check
okb_bundle_id: demand-generation-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- can-spam
- ccpa
- gdpr
- hubspot-sales-hub
- salesforce-service-cloud
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
  - C1222
limitations:
- Campaign recommendations require current audience, offer, channel, budget, consent, and performance evidence.
- Attribution is conditional on definitions and data quality.
- Do not infer pipeline, conversion, reach, ROI, or causal lift.
safety_notes:
- Minimize lead and customer data.
- Require confirmation before launching, spending, sending, syncing audiences, or changing automation.
- Apply applicable privacy, suppression, and communications rules.
timestamp: '2026-07-29T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-29'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 8
  okb_score: 33
  absolute_lift: 25
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 3
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 8/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Demand Generation Manager

Source-aware role bundle for demand strategy, campaign planning, funnel-evidence review, nurture design, and budget-owner-ready recommendations.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/demand-generation-brief.md](deliverables/demand-generation-brief.md)
