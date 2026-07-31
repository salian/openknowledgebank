---
type: Bundle Index
title: "Snowflake"
description: "Source-aware tool bundle for Snowflake data, SQL, warehouse, access, performance, cost, governance, and review-ready analysis or change briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "snowflake"
  - "data-platform"
  - "analytics"
  - "tool"
aliases:
  - "Snowflake"
problems_solved:
  - "Prepare a snowflake analysis and change brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Data and analytics"
  - "Software"
  - "Financial services"
tools:
  - "Snowflake"
frameworks:
  - "source-evidence matrix"
  - "cloud-data-platform-analysis-and-administration evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Snowflake analysis and change brief"
commands: []
skills: []
evaluations:
  - "Snowflake source-awareness check"
okb_bundle_id: snowflake
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "ai-data-platform-engineer"
  - "business-intelligence-analyst"
  - "business-intelligence-bi-developer"
  - "data-architect"
  - "data-engineer"
  - "data-product-manager"
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Use official Snowflake sources for general context; local cloud data platform analysis and administration, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for account, region, edition, and version context, database, schema, object, and ownership metadata, warehouse and resource-monitor configuration, roles, grants, policies, and data classification, SQL text, parameters, query profile, and history, freshness, lineage, quality, and source-of-record checks, and cost, change, and approval evidence."
  - "Do not infer objects, columns, data, roles, grants, warehouse state, query results, cost."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before running state-changing SQL, changing objects, warehouses, roles, grants, policies, integrations, shares, or production data."
  - "Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: "2026-07-31"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 1
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 10
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Snowflake

Source-aware tool bundle for Snowflake data, SQL, warehouse, access, performance, cost, governance, and review-ready analysis or change briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/snowflake-brief.md](deliverables/snowflake-brief.md)
