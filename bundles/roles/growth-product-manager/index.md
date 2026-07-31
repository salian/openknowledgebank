---
type: Bundle Index
title: Growth Product Manager
description: Source-aware role bundle for product-growth opportunity analysis, experiment prioritization, instrumentation review, rollout planning, and decision-ready product briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- growth-product
- product-experiments
- product-analytics
- role
aliases:
- Growth Product Manager
- Product Growth Manager
problems_solved:
- Prepare product growth experiment and rollout brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Digital products
- Software
tools: []
frameworks:
- source-evidence matrix
- product-growth evidence matrix
- qualified-review gate
deliverables:
- Product growth experiment and rollout brief
commands: []
skills: []
evaluations:
- Growth Product Manager source-awareness check
okb_bundle_id: growth-product-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- amplitude
- figma
- jira
- jobs-to-be-done
- mixpanel
- okrs
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
- Treat the occupational mapping as approximate; product goals, user evidence, event schemas, experiment state, technical constraints, and outcomes require local evidence.
- Task-specific work requires current evidence for product outcome and strategy, user research, event and identity schema, baseline and segment definitions, experiment design and guardrails, technical constraints, rollout and rollback controls.
- Do not infer user needs, event names, baseline metrics, experiment results, technical feasibility, feature state, roadmap commitment.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before feature, experiment, tracking, customer, data, or production rollout changes.
- Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 6
  okb_score: 35
  absolute_lift: 29
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 3
    okb_score: 12
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 2
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 6/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Growth Product Manager

Source-aware role bundle for product-growth opportunity analysis, experiment prioritization, instrumentation review, rollout planning, and decision-ready product briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts
and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/product-growth-brief.md](deliverables/product-growth-brief.md)
