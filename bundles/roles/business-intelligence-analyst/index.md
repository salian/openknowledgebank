---
type: Bundle Index
title: Business Intelligence Analyst
description: Source-aware role bundle for business-question framing, metric definition, data reconciliation, trend analysis, dashboard review, and decision-ready BI briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- business-intelligence
- analytics
- decision-support
- role
aliases:
- Business Intelligence Analyst
- BI Analyst
problems_solved:
- Prepare business intelligence analysis and reconciliation brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Data and analytics
tools: []
frameworks:
- source-evidence matrix
- metric-lineage matrix
- qualified-review gate
deliverables:
- Business intelligence analysis and reconciliation brief
commands: []
skills: []
evaluations:
- Business Intelligence Analyst source-awareness check
okb_bundle_id: business-intelligence-analyst
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- gdpr
- google-bigquery
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
  - 2511.1 (ICT business analyst / data analyst family)
limitations:
- Use as occupational context; schemas, metrics, grain, lineage, refresh, permissions, report state, and values require inspected local evidence.
- Task-specific work requires current evidence for business question and decision, metric and dimension definitions, source schemas and grain, keys, lineage, and refresh state, filters and access rules, query or export evidence, validation and owner approvals.
- Do not infer tables, fields, joins, metric values, dashboard state, data freshness, access, causal claims.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before data access, production queries, dashboard changes, sensitive data, or consequential business reliance.
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
  baseline_score: 14
  okb_score: 35
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 7
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Business Intelligence Analyst

Source-aware role bundle for business-question framing, metric definition, data reconciliation, trend analysis, dashboard review, and decision-ready BI briefs.

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
- [deliverables/bi-analysis-brief.md](deliverables/bi-analysis-brief.md)
