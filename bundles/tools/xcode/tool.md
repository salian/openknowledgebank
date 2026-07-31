---
type: Tool Guide
title: Xcode
description: Defines source-aware project, target, scheme, build setting, test, signing, archive, and diagnostic review, evidence handling, and action boundaries.
resource: https://developer.apple.com/xcode/
okb_bundle_id: xcode
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a xcode review brief with explicit evidence states.
confirmation_required:
- edit project or workspace files, change signing or entitlements, install packages, run scripts or tests, archive or upload builds, expose credentials, or modify release settings
---
# Xcode Source-Aware Tool Guide

Source-aware tool bundle for project, target, scheme, build setting, test, signing, archive, and diagnostic review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://developer.apple.com/xcode/
- https://developer.apple.com/documentation/xcode/build-system
- https://developer.apple.com/documentation/xcode/customizing-the-build-schemes-for-a-project

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- Xcode and SDK versions, project or workspace, targets, schemes, configurations, resolved build settings, package state, signing identities and entitlements, test plan, logs, CI environment, and release destination

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
- Do not infer resolved build setting, signing validity, test result, archive readiness, App Store acceptance, or local project state.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that edit project or workspace files, change signing or entitlements, install packages, run scripts or tests, archive or upload builds, expose credentials, or modify release settings.
