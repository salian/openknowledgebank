---
type: Bundle Index
title: Customer Experience (CX) Manager
description: Source-aware role bundle for voice-of-customer synthesis, journey evidence review, experience measurement, improvement planning, and owner-ready recommendations.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- customer-experience
- voice-of-customer
- journey
- role
aliases:
- Customer Experience Manager
- CX Manager
problems_solved:
- Synthesize feedback without fabricated customer evidence.
- Separate journey observations from causal hypotheses.
- Prioritize improvements with measurement and ownership gates.
industries:
- Customer experience
- Services
tools: []
frameworks:
- source-evidence matrix
- experience-evidence matrix
- qualified-review gate
deliverables:
- Voice-of-customer and experience improvement brief
commands: []
skills: []
evaluations:
- Customer Experience (CX) Manager source-awareness check
okb_bundle_id: customer-experience-cx-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ccpa
- gdpr
- salesforce-service-cloud
- tableau
- zendesk
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
  - '1221'
limitations:
- Recommendations require current feedback, survey, journey, service, metric, and ownership evidence.
- The taxonomy mapping is approximate, not an exact title match.
- Do not infer scores, samples, quotations, behavior, causes, or improvement impact.
safety_notes:
- Minimize personal, customer, and verbatim feedback data.
- Require confirmation before contacting customers, publishing findings, or changing workflows.
- Route privacy, accessibility, regulated-service, and high-impact decisions to qualified review.
timestamp: '2026-07-29T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-29'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 13
  okb_score: 32
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 9
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 13/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Customer Experience (CX) Manager

Source-aware role bundle for voice-of-customer synthesis, journey evidence review, experience measurement, improvement planning, and owner-ready recommendations.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/cx-improvement-brief.md](deliverables/cx-improvement-brief.md)
