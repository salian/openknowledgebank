---
type: Bundle Index
title: SAP S/4HANA
description: "Tool bundle for source-aware SAP S/4HANA fit-gap, process, integration, reporting, and migration support."
schema_version: 0.1.0
bundle_format: okf-compatible
category: tools
tags:
  - sap-s4hana
  - sap
  - erp
  - finance
  - supply-chain
  - procurement
  - manufacturing
aliases:
  - SAP S/4HANA
  - S/4HANA
  - SAP S/4HANA Cloud
problems_solved:
  - Plan SAP S/4HANA analysis without inventing tenant configuration, master data, roles, APIs, or process scope.
  - Separate official SAP product documentation from customer-specific implementation evidence.
  - Draft fit-gap, process, integration, and reporting plans with inspect-first evidence requirements.
industries:
  - cross-industry
tools:
  - SAP S/4HANA
  - SAP S/4HANA Cloud Public Edition
  - SAP S/4HANA Cloud Private Edition
  - SAP Help Portal
  - SAP Business Accelerator Hub
frameworks:
  - source-aware ERP fit-gap
  - process-scope evidence review
  - integration evidence matrix
deliverables:
  - SAP S/4HANA fit-gap brief
commands:
  - /plan-s4hana-fit-gap
skills: []
evaluations:
  - SAP S/4HANA source-awareness check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: blocked
license: CC-BY-4.0
related_bundles: []
adjacent_bundles:
  - google-bigquery
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Not a complete SAP implementation, configuration, authorization, extensibility, migration, API, or module reference."
  - "Requires user-provided tenant, edition, release, scope item, process, master data, authorization, integration, and reporting evidence for final recommendations."
  - "Does not replace SAP partner, implementation, architecture, security, data migration, audit, legal, or compliance review."
safety_notes:
  - "Require confirmation before changing configuration, transporting changes, posting transactions, exporting data, modifying roles, calling APIs, or changing integrations."
  - "Do not claim access to SAP tenants, Fiori apps, configuration, CDS views, APIs, tables, roles, logs, or data unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: "measured"
  last_evaluated: "2026-07-09"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 48
  baseline_score: 23
  okb_score: 42
  absolute_lift: 19
  display_summary: "Improved measured rubric score from 23/48 to 42/48 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts, raw outputs, and provider response artifacts. Private artifacts are retained in the evaluation run folder."
okb_bundle_id: sap-s4hana
timestamp: "2026-07-09T00:00:00Z"
---

# SAP S/4HANA

This bundle helps an agent support SAP S/4HANA work without pretending to know a customer's tenant, configuration, master data, authorizations, APIs, reports, or implementation history.

Use it for source-aware fit-gap, process-scope, integration, reporting, and migration planning. Treat it as a companion tool bundle for finance, procurement, supply-chain, manufacturing, operations, audit, and IT role bundles.

## Required Answer Habit

For source-sensitive SAP S/4HANA work, include a short **Source note** naming the official SAP source category, the user-provided local evidence used, and missing evidence required before treating a plan, configuration recommendation, integration design, or report answer as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-s4hana-fit-gap.md](commands/plan-s4hana-fit-gap.md)
- [workflows/plan-s4hana-fit-gap.md](workflows/plan-s4hana-fit-gap.md)
- [workflows/reconcile-s4hana-reporting.md](workflows/reconcile-s4hana-reporting.md)
- [deliverables/s4hana-fit-gap-brief.md](deliverables/s4hana-fit-gap-brief.md)
- [evaluations/s4hana-source-awareness-check.md](evaluations/s4hana-source-awareness-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use SAP product pages, SAP Help Portal documentation for the specific S/4HANA edition and release, SAP Business Accelerator Hub for API and integration assets, SAP Activate or implementation guidance when relevant, and user-provided local tenant evidence. Do not invent scope items, app names, tables, CDS views, APIs, business roles, configuration activities, migration objects, report definitions, postings, or process status.
