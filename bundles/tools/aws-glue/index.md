---
type: Bundle Index
title: AWS Glue
description: Source-aware tool bundle for Data Catalog, crawler, classifier, connection, ETL job, trigger, schema, lineage, security, and run review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: tools
version: 0.1.0
tags:
- aws-glue
- tool
- source-aware
aliases:
- AWS Glue
problems_solved:
- Prepare a aws glue review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools:
- AWS Glue
frameworks:
- source-evidence matrix
- AWS Glue application matrix
- qualified-review gate
deliverables:
- AWS Glue review brief
commands: []
skills: []
evaluations:
- AWS Glue source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- data-warehousing-specialist
- apache-airflow
adjacent_bundles: []
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
- Use the listed authoritative or identified source surfaces for general AWS Glue guidance; local facts, configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for AWS account and region, Glue version, IAM role and Lake Formation policy, data locations, catalog database and tables, crawler classifiers and change policy, job code and arguments, connections, triggers, encryption, logs, costs, tests, and rollback.
- Do not infer schema, partition, permission, job result, data quality, lineage, cost, or production readiness.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that create or alter catalog objects, crawlers, jobs, triggers, connections, IAM or Lake Formation permissions; run workloads; read or write data; delete resources; or incur spend.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: aws-glue
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 14
  okb_score: 36
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: configuration-risk-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# AWS Glue

Source-aware tool bundle for Data Catalog, crawler, classifier, connection, ETL job, trigger, schema, lineage, security, and run review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and domain actions prohibited without explicit approval.
5. **Source note** - name authoritative source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role.

Facts explicitly stated in the request belong under `Provided` as `Prompt-provided request`; do not move them to `Assumed`. Do not assign an owner, author, date, or version unless the request states it.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/aws-glue-brief.md](deliverables/aws-glue-brief.md)
