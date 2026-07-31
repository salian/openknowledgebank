---
type: Tool Guide
title: Azure Data Factory
description: Defines source-aware Azure Data Factory pipeline, data movement, integration, monitoring, and deployment review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Azure Data Factory change brief with explicit evidence states.
confirmation_required:
- publish a factory change, create linked services, expose credentials, start or stop triggers, run pipelines, move or overwrite data, or deploy across environments
okb_bundle_id: azure-data-factory
timestamp: '2026-07-31T00:00:00Z'
---
# Azure Data Factory

Source-aware tool bundle for Azure Data Factory pipeline, data movement, integration, monitoring, and deployment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://azure.microsoft.com/en-us/products/data-factory/
- https://learn.microsoft.com/en-us/azure/data-factory/concepts-linked-services
- https://learn.microsoft.com/en-us/azure/data-factory/monitor-data-factory

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- tenant, subscription, resource group, factory, region, environment, and API version
- pipeline, activity, dataset, linked service, integration runtime, trigger, parameter, expression, dependency, source and sink contracts
- identity, RBAC, networking, credentials, Key Vault, data classification, Git and deployment state, tests, run history, monitoring, alerts, costs, rollback, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer connection validity, trigger behavior, pipeline outcome, data completeness, monitoring state, cost, production configuration, or root cause.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that publish a factory change, create linked services, expose credentials, start or stop triggers, run pipelines, move or overwrite data, or deploy across environments.
