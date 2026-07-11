---
type: "Bundle Index"
title: "Data Engineer"
description: "Source-aware role bundle for data pipeline planning, schema and warehouse design, ETL/ELT review, orchestration triage, and data quality handoff."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "roles"
tags:
  - "data-engineering"
  - "pipelines"
  - "etl"
  - "warehousing"
  - "role"
aliases:
  - "Data Engineer"
  - "Analytics Engineer"
  - "Data Platform Engineer"
problems_solved:
  - "Turn source-system context, schemas, transformation rules, and warehouse constraints into a reviewable data pipeline plan."
  - "Separate verified schema facts, user-provided assumptions, missing source evidence, and environment-specific configuration."
  - "Prepare data quality, lineage, orchestration, and validation guidance without inventing fields, tables, credentials, or platform behavior."
industries:
  - "General"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "schema-grounding protocol"
  - "data-quality validation gate"
deliverables:
  - "Source-aware data pipeline plan"
commands:
  []
skills:
  []
evaluations:
  - "Data engineering source-awareness check"
okb_bundle_id: data-engineer
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles:
  - "data-warehousing-specialist"
  - "gdpr"
  - "google-bigquery"
  - "hipaa"
  - "soc-2"
adjacent_bundles:
  []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    - "15-1243.00"
  soc:
    []
  isco_08:
    []
  esco:
    - "data scientist"
limitations:
  - "This bundle supports data engineering planning and review; it is not security, privacy, legal, audit, or production-change approval."
  - "Environment-specific recommendations require current schemas, data samples, access controls, contracts, platform configuration, and owner review."
  - "Do not invent table names, fields, metric definitions, pipeline behavior, credentials, costs, SLAs, lineage, or data quality results."
safety_notes:
  - "Minimize personal, customer, patient, employee, financial, credential, and regulated data in prompts and examples."
  - "Require explicit confirmation before modifying production pipelines, schemas, permissions, jobs, exports, retention settings, or infrastructure."
  - "Route privacy, security, compliance, and production-impacting changes to accountable reviewers."
timestamp: "2026-07-11T00:00:00Z"
evaluation_summary:
  status: "blocked"
  last_evaluated: "2026-07-11"
  method: "baseline-vs-okb-rubric"
  tasks_count: 0
  display_summary: "Evaluation blocked: measured baseline and OKB-assisted outputs plus reviewer-scored aggregate results are not available for this run."
  evidence_note: "No measured score is claimed; private run records the evaluation blocker."
---

# Data Engineer

Source-aware role bundle for data pipeline planning, schema and warehouse design, ETL/ELT review, orchestration triage, and data quality handoff.

## Required Answer Habit

Include a short **Source note** naming the schema/source evidence, environment context, user-provided assumptions, and missing verification still needed before implementation or production reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-pipeline-triage.md](workflows/source-aware-pipeline-triage.md)
- [deliverables/source-aware-data-pipeline-plan.md](deliverables/source-aware-data-pipeline-plan.md)
