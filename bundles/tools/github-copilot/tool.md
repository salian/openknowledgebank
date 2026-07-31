---
type: Tool Guide
title: GitHub Copilot
description: Defines source-aware IDE or GitHub surface, context, suggestion, chat, coding agent, policy, code review, privacy, and change review, evidence handling, and action boundaries.
resource: https://docs.github.com/en/copilot
okb_bundle_id: github-copilot
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a github copilot review brief with explicit evidence states.
confirmation_required:
- apply edits, run commands or tests, delegate coding-agent work, create commits or pull requests, change Copilot policies, send private code, expose credentials, or deploy changes
---
# GitHub Copilot Source-Aware Tool Guide

Source-aware tool bundle for IDE or GitHub surface, context, suggestion, chat, coding agent, policy, code review, privacy, and change review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://docs.github.com/en/copilot
- https://docs.github.com/en/copilot/responsible-use/chat-in-github

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- Copilot plan and surface, IDE and extension version, repository and branch, selected context, organization and enterprise policies, model or agent mode, diffs, commands, tests, code-review evidence, data controls, approvals, and rollback

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
- Do not infer context used, suggestion correctness, security, license suitability, command result, policy effect, agent state, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that apply edits, run commands or tests, delegate coding-agent work, create commits or pull requests, change Copilot policies, send private code, expose credentials, or deploy changes.
