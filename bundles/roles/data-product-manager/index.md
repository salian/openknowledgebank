---
type: Bundle Index
title: Data Product Manager
description: Entry point for the Data Product Manager OpenKnowledge bundle.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [data-product-management, data-products, product-management, analytics, data-governance, data-quality]
aliases: [DPM, data PM, data product owner, analytics product manager, data platform product manager]
problems_solved:
  - define data product opportunities
  - draft data product PRDs
  - review data contracts
  - reconcile metric definitions
  - plan data product roadmaps
  - evaluate data product trust and adoption
industries: [software, saas, digital-products, internal-tools, data-platforms, analytics, enterprise-data]
tools: [Jira, Linear, Confluence, Notion, dbt, Snowflake, BigQuery, Databricks, Looker, Tableau, Amplitude, Mixpanel, Monte Carlo, Collibra, Alation, Atlan, GitHub]
frameworks: [data-as-a-product, data contracts, data quality dimensions, Jobs-to-be-Done, OKRs, RICE prioritization, North Star metric, lineage, governance]
deliverables: [data product brief, data product PRD, data contract brief, metric definition review, data product roadmap note]
commands: [/draft-data-product-prd, /review-data-contract, /reconcile-metric-definition]
skills: []
evaluations: [data-product-management-quality-check]
okb_bundle_id: data-product-manager
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles: [agile, figma, gdpr, jira, okrs, product-manager, soc-2, technical-product-manager]
adjacent_bundles: [product-manager, technical-product-manager, ga4-analytics-specialist, stackoverflow-data-analyst]
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings:
  onet_soc: ["11-2011.00"]
  soc: []
  isco_08: ["1330"]
  esco: ["1330.6"]
limitations:
  - Data Product Manager responsibilities vary by organization; verify local ownership, decision rights, governance process, and product lifecycle.
  - The O*NET mapping comes from the reviewed generator candidate and points to Advertising and Promotions Managers; treat it as candidate taxonomy context, not a precise role standard.
  - The bundle does not include tool-specific API, workspace, schema, or admin procedures.
  - It does not replace legal, privacy, security, data governance, compliance, or data engineering review.
safety_notes:
  - Confirm before modifying live schemas, data contracts, semantic layers, dashboards, pipeline schedules, access grants, tickets, docs, or roadmap systems.
  - Treat customer data, personal data, restricted datasets, roadmap plans, data incidents, and governance records as confidential unless the user confirms they are safe to use.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 16
  okb_score: 25
  absolute_lift: 9
  task_scores:
    - task: customer-health-data-product-prd
      baseline_score: 9
      okb_score: 10
      max_score: 12
    - task: customer-events-contract-review
      baseline_score: 3
      okb_score: 9
      max_score: 12
    - task: active-customer-metric-reconciliation
      baseline_score: 4
      okb_score: 6
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 16/36 to 25/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
timestamp: 2026-07-09T00:00:00Z
---

# Data Product Manager

This bundle helps an agent support data-product-management work: defining useful data products, drafting data-product requirements, reviewing data contracts, reconciling metric definitions, planning data-product roadmaps, and evaluating whether data products are trustworthy enough for consumers.

## Core Concepts

- [Role](role.md)
- [Operating Principles](operating-principles.md)
- [Responsibilities](responsibilities/index.md)

## Workflows

- [Define Data Product Opportunity](workflows/define-data-product-opportunity.md)
- [Write Data Product PRD](workflows/write-data-product-prd.md)
- [Review Data Contract](workflows/review-data-contract.md)
- [Reconcile Metric Definition](workflows/reconcile-metric-definition.md)
- [Plan Data Product Roadmap](workflows/plan-data-product-roadmap.md)

## Deliverables and Commands

- [Data Product Brief](deliverables/data-product-brief.md)
- [Data Product PRD](deliverables/data-product-prd.md)
- [Data Contract Brief](deliverables/data-contract-brief.md)
- [Metric Definition Review](deliverables/metric-definition-review.md)
- [Data Product Roadmap Note](deliverables/data-product-roadmap-note.md)
- [/draft-data-product-prd](commands/draft-data-product-prd.md)
- [/review-data-contract](commands/review-data-contract.md)
- [/reconcile-metric-definition](commands/reconcile-metric-definition.md)

Use this bundle as decision support. It is not authority to inspect restricted data, change live systems, publish metric definitions, grant access, or make roadmap commitments without confirmation.
