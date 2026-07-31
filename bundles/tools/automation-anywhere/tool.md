---
type: Tool Guide
title: Automation Anywhere
description: Defines source-aware Control Room, bot, dependency, credential, schedule, workload, audit, and deployment review, evidence handling, and action boundaries.
resource: https://docs.automationanywhere.com/
okb_bundle_id: automation-anywhere
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a automation anywhere review brief with explicit evidence states.
confirmation_required:
- create, edit, deploy, schedule, or run bots; change queues or permissions; access credentials; process production data; or alter live systems
---
# Automation Anywhere Source-Aware Tool Guide

Source-aware tool bundle for Control Room, bot, dependency, credential, schedule, workload, audit, and deployment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://docs.automationanywhere.com/
- https://www.automationanywhere.com/

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- product and deployment version, Control Room tenant, bot package and dependencies, credential vault references, device pools, schedules, queues, permissions, input and output data, audit logs, tests, approvals, and rollback

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
- Do not infer bot behavior, credential access, schedule state, queue result, production readiness, execution result, or business outcome.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create, edit, deploy, schedule, or run bots; change queues or permissions; access credentials; process production data; or alter live systems.
