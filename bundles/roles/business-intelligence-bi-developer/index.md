---
type: Bundle Index
title: Business Intelligence (BI) Developer
description: Source-aware role bundle for BI requirements, semantic-model planning, report reconciliation, data-quality review, and implementation-ready technical briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- business-intelligence
- semantic-model
- reporting
- role
aliases:
- BI Developer
- Business Intelligence Developer
problems_solved:
- Design BI work without fictional schemas.
- Reconcile dashboards using explicit metric and filter definitions.
- Produce implementation briefs with testable acceptance criteria.
industries:
- Data and analytics
tools: []
frameworks:
- source-evidence matrix
- metric-lineage matrix
- qualified-review gate
deliverables:
- BI semantic-model and report implementation brief
commands: []
skills: []
evaluations:
- Business Intelligence (BI) Developer source-awareness check
okb_bundle_id: business-intelligence-bi-developer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- gdpr
- hipaa
- microsoft-power-bi
- soc-2
- tableau
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 15-2051.01
  soc: []
  isco_08: []
  esco:
  - '2511.1'
limitations:
- Implementation requires current schemas, definitions, lineage, permissions, and platform evidence.
- This bundle does not validate production data or security controls.
- Do not infer tables, fields, relationships, refresh state, or report values.
safety_notes:
- Minimize sensitive and row-level data.
- Require confirmation before running costly queries, changing models, publishing reports, or altering access.
- Route governance, privacy, and security decisions to accountable owners.
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
  okb_score: 32
  absolute_lift: 24
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 10
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 3
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 8/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Business Intelligence (BI) Developer

Source-aware role bundle for BI requirements, semantic-model planning, report reconciliation, data-quality review, and implementation-ready technical briefs.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/bi-implementation-brief.md](deliverables/bi-implementation-brief.md)
