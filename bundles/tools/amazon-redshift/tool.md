---
type: Tool Guide
title: Amazon Redshift
description: Defines source-aware Amazon Redshift data warehouse, query, workload, security, and recovery review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Amazon Redshift change brief with explicit evidence states.
confirmation_required:
- run write queries or DDL, load or unload data, grant access, expose credentials, resize or pause resources, restore snapshots, or change production configuration
okb_bundle_id: amazon-redshift
timestamp: '2026-07-31T00:00:00Z'
---
# Amazon Redshift

Source-aware tool bundle for Amazon Redshift data warehouse, query, workload, security, and recovery review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://aws.amazon.com/redshift/
- https://docs.aws.amazon.com/redshift/
- https://docs.aws.amazon.com/redshift/latest/mgmt/security-incident-response.html

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- AWS account, region, cluster or serverless namespace, engine and client versions
- database, schema, table, view, owner, data contracts, lineage, load and transformation logic
- IAM, database roles, network, encryption, secrets, workload management, SQL, query plans, statistics, monitoring, audit logs, snapshots, recovery tests, costs, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer data completeness, query result, performance, permission, encryption, backup coverage, recovery point, cost, or production state.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that run write queries or DDL, load or unload data, grant access, expose credentials, resize or pause resources, restore snapshots, or change production configuration.
