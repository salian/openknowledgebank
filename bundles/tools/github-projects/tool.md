---
type: Tool Guide
title: GitHub Projects
description: Defines source-aware project, view, field, item, issue, pull request, iteration, workflow, chart, GraphQL, and status review, evidence handling, and action boundaries.
resource: https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
okb_bundle_id: github-projects
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a github projects review brief with explicit evidence states.
confirmation_required:
- add, edit, archive, or delete items; change fields, views, iterations, workflows, templates, permissions, or status updates; or trigger GitHub Actions
---
# GitHub Projects Source-Aware Tool Guide

Source-aware tool bundle for project, view, field, item, issue, pull request, iteration, workflow, chart, GraphQL, and status review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- owner and project number, repositories, views and filters, field definitions and option IDs, items and linked issues or pull requests, iterations, built-in workflows or Actions, GraphQL query, permissions, dates, metric definitions, and approvals

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
- Do not infer item state, field value, ownership, iteration, workflow effect, query result, chart meaning, or delivery status.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that add, edit, archive, or delete items; change fields, views, iterations, workflows, templates, permissions, or status updates; or trigger GitHub Actions.
