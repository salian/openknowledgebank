---
type: Tool Guide
title: AWS Glue
description: Defines source-aware Data Catalog, crawler, classifier, connection, ETL job, trigger, schema, lineage, security, and run review, evidence handling, and action boundaries.
resource: https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
okb_bundle_id: aws-glue
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a aws glue review brief with explicit evidence states.
confirmation_required:
- create or alter catalog objects, crawlers, jobs, triggers, connections, IAM or Lake Formation permissions; run workloads; read or write data; delete resources; or incur spend
---
# AWS Glue Source-Aware Tool Guide

Source-aware tool bundle for Data Catalog, crawler, classifier, connection, ETL job, trigger, schema, lineage, security, and run review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
- https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html
- https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- AWS account and region, Glue version, IAM role and Lake Formation policy, data locations, catalog database and tables, crawler classifiers and change policy, job code and arguments, connections, triggers, encryption, logs, costs, tests, and rollback

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory evidence and label it as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, identifiers, versions, periods, scope, permissions, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer schema, partition, permission, job result, data quality, lineage, cost, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create or alter catalog objects, crawlers, jobs, triggers, connections, IAM or Lake Formation permissions; run workloads; read or write data; delete resources; or incur spend.
