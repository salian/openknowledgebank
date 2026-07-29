---
type: Bundle Index
title: Business Development Representative (BDR)
description: Source-aware role bundle for account research, qualification planning, approved-claim outreach drafts, objection preparation, and CRM-review-ready handoff.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- business-development
- sales-development
- qualification
- role
aliases:
- Business Development Representative
- BDR
problems_solved:
- Research accounts without fabricating buying signals.
- Draft outreach using only approved claims.
- Prepare qualification handoffs with visible uncertainty.
industries:
- Sales
- Business services
tools: []
frameworks:
- source-evidence matrix
- account-evidence matrix
- qualified-review gate
deliverables:
- Source-aware account research and outreach brief
commands: []
skills: []
evaluations:
- Business Development Representative (BDR) source-awareness check
okb_bundle_id: business-development-representative-bdr
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- can-spam
- gdpr
- hubspot-sales-hub
- salesforce-service-cloud
- tcpa
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 41-3091.00
  soc: []
  isco_08: []
  esco:
  - 516627bd-f335-4f5a-8a06-b59a16f23c81
limitations:
- This bundle supports research and drafting, not autonomous outreach or sales commitments.
- Account-specific work requires current sources, CRM evidence, contact permissions, and approved claims.
- Do not infer customer intent, authority, budget, timing, or product fit.
safety_notes:
- Minimize personal and customer data.
- Require confirmation before sending messages, enrolling contacts, exporting data, or changing CRM records.
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
  baseline_score: 7
  okb_score: 29
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 8
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 2
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 7/36 to 29/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Business Development Representative (BDR)

Source-aware role bundle for account research, qualification planning, approved-claim outreach drafts, objection preparation, and CRM-review-ready handoff.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/account-research-outreach-brief.md](deliverables/account-research-outreach-brief.md)
