---
type: Bundle Index
title: Analytics Engineer
description: Source-aware role bundle for analytics engineering across warehouse modeling, transformation, testing, documentation, lineage, governance, deployment, and stakeholder-facing data products.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- analytics-engineer
- data-modeling
- dbt
- role
aliases:
- Analytics Engineer
problems_solved:
- Prepare a analytics engineering delivery brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Data and analytics
- Software
- Financial services
tools: []
frameworks:
- source-evidence matrix
- analytics engineering and governed data transformation review matrix
- qualified-review gate
deliverables:
- analytics engineering delivery brief
commands: []
skills: []
evaluations:
- Analytics Engineer source-awareness check
okb_bundle_id: analytics-engineer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- dbt
- google-bigquery
- snowflake
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 15-1243.01
  soc: []
  isco_08: []
  esco:
  - '2521.3'
limitations:
- Use the cited official, originator, standards, or professional sources for general analytics engineering and governed data transformation context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for business question, stakeholder, decision, and acceptance criteria, warehouse, platform, environment, repository, and tool versions, source data contracts, freshness, quality, ownership, and sensitivity, models, grain, keys, joins, transformations, tests, and lineage, metric and semantic definitions, dimensions, filters, and reconciliation, and review, CI, deployment, access, documentation, monitoring, and incident evidence.
- Do not infer source-data meaning, model grain, join behavior, metric definition, test result, and production state.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before querying or exposing sensitive data, changing production models or metrics, deploying transformations, changing access, or certifying data products without review.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 18
  okb_score: 36
  absolute_lift: 18
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 18/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Analytics Engineer

Source-aware role bundle for analytics engineering across warehouse modeling, transformation, testing, documentation, lineage, governance, deployment, and stakeholder-facing data products.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/analytics-engineer-brief.md](deliverables/analytics-engineer-brief.md)
