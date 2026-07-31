---
type: Tool Guide
title: Rippling
description: Defines source-aware workforce records, payroll, identity, device, spend, integration, and workflow review, evidence handling, and action boundaries.
resource: https://developer.rippling.com/
okb_bundle_id: rippling
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a rippling review brief with explicit evidence states.
confirmation_required:
- create or change worker, payroll, identity, device, spend, integration, or workflow data; run automations; expose credentials; send employee data; or make tax or employment determinations
---
# Rippling Source-Aware Tool Guide

Source-aware tool bundle for workforce records, payroll, identity, device, spend, integration, and workflow review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://developer.rippling.com/
- https://www.rippling.com/

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- company and worker identifiers, enabled products, environment, API or workflow version, authorization scope, field mappings, payroll and identity sources of record, audit history, tests, approvals, and rollback

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
- Do not infer worker status, pay result, identity or device state, workflow execution, authorization, compliance, or source-of-record status.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create or change worker, payroll, identity, device, spend, integration, or workflow data; run automations; expose credentials; send employee data; or make tax or employment determinations.
