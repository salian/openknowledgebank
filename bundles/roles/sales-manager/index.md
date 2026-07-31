---
type: Bundle Index
title: Sales Manager
description: Source-aware role bundle for sales planning, territory and pipeline review, forecast governance, coaching decisions, and approval-ready commercial briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- sales-management
- pipeline
- forecasting
- role
aliases:
- Sales Manager
problems_solved:
- Prepare sales pipeline and forecast decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Sales
- Business services
tools: []
frameworks:
- source-evidence matrix
- sales-governance matrix
- qualified-review gate
deliverables:
- Sales pipeline and forecast decision brief
commands: []
skills: []
evaluations:
- Sales Manager source-awareness check
okb_bundle_id: sales-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- hubspot-sales-hub
- salesforce-service-cloud
- tableau
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-2022.00
  soc: []
  isco_08: []
  esco:
  - sales manager
limitations:
- Use as occupational context; territories, quotas, pipeline, CRM state, forecasts, pricing, compensation, customer facts, and commitments require current evidence.
- Task-specific work requires current evidence for approved sales goals and definitions, territory and quota rules, CRM opportunity evidence, stage and forecast criteria, pricing and discount authority, activity and outcome definitions, compensation and approval policy.
- Do not infer pipeline value, forecast, customer intent, stage, quota attainment, pricing authority, CRM state.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before customer communication, pricing, terms, compensation, forecasts, or CRM changes.
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
  baseline_score: 10
  okb_score: 34
  absolute_lift: 24
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 12
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
  display_summary: Improved measured rubric score from 10/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Sales Manager

Source-aware role bundle for sales planning, territory and pipeline review, forecast governance, coaching decisions, and approval-ready commercial briefs.

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
- [deliverables/sales-management-brief.md](deliverables/sales-management-brief.md)
