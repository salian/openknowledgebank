---
type: Workflow
title: AWS Glue Source-Aware Triage
description: Inspect-first workflow for Data Catalog, crawler, classifier, connection, ETL job, trigger, schema, lineage, security, and run review.
okb_bundle_id: aws-glue
---
# AWS Glue Source-Aware Triage

1. State the decision and direct answer possible now.
2. Record Verified, Provided, Assumed, and Needs verification separately.
3. Inspect the current source version and exact local evidence for AWS account and region, Glue version, IAM role and Lake Formation policy, data locations, catalog database and tables, crawler classifiers and change policy, job code and arguments, connections, triggers, encryption, logs, costs, tests, and rollback.
4. Reconcile definitions, identifiers, dates, scope, permissions, processing, and ownership.
5. Record alternatives, stop conditions, and an independent cross-check.
6. Require explicit approval before actions that create or alter catalog objects, crawlers, jobs, triggers, connections, IAM or Lake Formation permissions; run workloads; read or write data; delete resources; or incur spend.
7. End with a Source Note naming source URLs, user evidence, and missing sources.
