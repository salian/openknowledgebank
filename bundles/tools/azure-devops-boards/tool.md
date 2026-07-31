---
type: Tool Guide
title: Azure DevOps Boards
description: Defines source-aware work item, backlog, board, iteration, area, query, WIQL, process, workflow, and reporting review, evidence handling, and action boundaries.
resource: https://learn.microsoft.com/en-us/azure/devops/boards/get-started/what-is-azure-boards
okb_bundle_id: azure-devops-boards
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a azure devops boards review brief with explicit evidence states.
confirmation_required:
- create, edit, move, link, bulk-update, or delete work items; change process, fields, states, areas, iterations, boards, queries, permissions, or notifications
---
# Azure DevOps Boards Source-Aware Tool Guide

Source-aware tool bundle for work item, backlog, board, iteration, area, query, WIQL, process, workflow, and reporting review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://learn.microsoft.com/en-us/azure/devops/boards/get-started/what-is-azure-boards
- https://learn.microsoft.com/en-us/azure/devops/boards/queries/wiql-syntax

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- organization and project, process model, work-item types and fields, area and iteration paths, board columns and states, query or WIQL, permissions, links, history, reporting definitions, dates, owners, and approvals

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
- Do not infer work-item state, owner, priority, estimate, query result, process behavior, delivery status, or metric meaning.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create, edit, move, link, bulk-update, or delete work items; change process, fields, states, areas, iterations, boards, queries, permissions, or notifications.
