---
type: Tool Guide
title: Eclipse IDE
description: Defines source-aware workspace, project, build path, launch configuration, plugin, secure storage, build, test, and diagnostic review, evidence handling, and action boundaries.
resource: https://help.eclipse.org/latest/
okb_bundle_id: eclipse
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a eclipse ide review brief with explicit evidence states.
confirmation_required:
- edit project or workspace metadata, install or update plugins, change build paths or launch settings, run code or tests, access secure storage, expose credentials, or publish artifacts
---
# Eclipse IDE Source-Aware Tool Guide

Source-aware tool bundle for workspace, project, build path, launch configuration, plugin, secure storage, build, test, and diagnostic review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://help.eclipse.org/latest/
- https://eclipseide.org/

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- Eclipse package and version, Java and toolchain versions, workspace and project metadata, build system and dependencies, target platform, launch configuration, installed plugins, secure-storage use, compiler settings, logs, tests, approvals, and rollback

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
- Do not infer workspace state, resolved dependency, build result, launch behavior, plugin compatibility, secure-storage content, or deployment readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that edit project or workspace metadata, install or update plugins, change build paths or launch settings, run code or tests, access secure storage, expose credentials, or publish artifacts.
