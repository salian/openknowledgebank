---
type: Tool Guide
title: Azure DevOps
description: Defines source-aware Repos, Pipelines, Boards, Artifacts, Test Plans, service connection, permission, and release review, evidence handling, and action boundaries.
resource: https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops
okb_bundle_id: azure-devops
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a azure devops review brief with explicit evidence states.
confirmation_required:
- push or merge code, run or approve pipelines, deploy releases, edit work items, change feeds, policies, permissions, agents, environments, service connections, variables, or secrets
---
# Azure DevOps Source-Aware Tool Guide

Source-aware tool bundle for Repos, Pipelines, Boards, Artifacts, Test Plans, service connection, permission, and release review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops
- https://learn.microsoft.com/en-us/rest/api/azure/devops/

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- organization, project, service and API version, repository and branch policy, pipeline YAML and variables, agent pools, environments, service connections, work-item process, artifact feeds, tests, permissions, audit logs, approvals, and rollback

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
- Do not infer repository state, pipeline result, work-item state, artifact provenance, permission, deployment readiness, or release outcome.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that push or merge code, run or approve pipelines, deploy releases, edit work items, change feeds, policies, permissions, agents, environments, service connections, variables, or secrets.
