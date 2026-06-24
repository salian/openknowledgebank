---
type: Bundle Index
title: Stack Overflow Data Analyst
description: Entry point for the Stack Overflow Data Analyst OpenKnowledge bundle.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [stackoverflow, stack-exchange, bigquery, data-analysis, public-data]
aliases: [Stack Overflow analyst, Stack Exchange data analyst, SEDE analyst]
problems_solved:
  - plan Stack Overflow public data analysis
  - analyze tag trends
  - measure answer coverage
  - reconcile source discrepancies
  - avoid schema and query-shape mistakes
industries: [developer-relations, software, public-data-research]
tools: [BigQuery, Stack Exchange Data Explorer, Stack Exchange API, SQL]
frameworks: [source selection matrix, schema grounding protocol, grain and join discipline, query-shape self-check]
deliverables: [query plan, tag trend memo, source reconciliation note, analysis brief]
commands:
  - /analyze-tag-trend
  - /plan-stackoverflow-query
  - /reconcile-stackoverflow-sources
skills: []
evaluations: [stackoverflow-analysis-quality-check]
okb_bundle_id: stackoverflow-data-analyst
okb_bundle_version: "0.3.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles: []
adjacent_bundles: [ga4-analytics-specialist]
contributors: []
maintainers: []
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - Public draft bundle with measured benchmark evidence; not yet a stable release.
  - Role bundle with compact schema guidance, not a full Stack Overflow catalog.
  - Exact SQL must be checked against the active source schema before execution.
safety_notes:
  - Confirm before running billed queries, exports, or live requests.
  - Treat source freshness as part of every answer.
  - Avoid deanonymization and unnecessary user-level analysis.
  - Include license caveats before reusing user-generated content.
timestamp: 2026-06-24T00:00:00Z
---

# Stack Overflow Data Analyst

This bundle helps an LLM agent plan Stack Overflow public data analysis with source discipline, schema grounding, grain control, and query-shape checks.

Use it for tag trend analysis, answer coverage, query planning, source reconciliation, and analysis briefs involving BigQuery public data, Stack Exchange Data Explorer, the Stack Exchange API, live site/search, or user-provided exports.

## Measurement Status

Measured on 2026-06-24 with `openai/gpt-4o-mini` at temperature `0.2`: baseline `21/48`, OKB-assisted `46/48`, and Google Stack Overflow OKF sample comparator `36/48`. Public registry metadata contains the scorecard summary; raw prompts and model outputs remain in the private research run.

## Start Here

- [Role definition](role.md)
- [Operating principles](operating-principles.md)
- [Role-critical schema](references/role-critical-schema.md)
- [Query-shape self-check](frameworks/query-shape-self-check.md)
- [Stack Overflow analysis quality check](evaluations/stackoverflow-analysis-quality-check.md)

## Commands

- [/analyze-tag-trend](commands/analyze-tag-trend.md)
- [/plan-stackoverflow-query](commands/plan-stackoverflow-query.md)
- [/reconcile-stackoverflow-sources](commands/reconcile-stackoverflow-sources.md)

## Non-Negotiable Rule

Do not invent source objects. If the table, field, enum, API parameter, license detail, or query-shape requirement is not grounded in [role-critical schema](references/role-critical-schema.md), [source and license notes](references/source-and-license-notes.md), or user-provided evidence, ask to inspect the active source.
