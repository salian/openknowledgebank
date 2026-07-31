---
type: Tool Guide
title: "Visual Studio Code"
description: "Defines source-aware editor workspace and development configuration, evidence handling, and action boundaries."
tool_category: "editor workspace and development configuration"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review editor workspace and development configuration from supplied evidence."
  - "Draft a vs code workspace and configuration brief with explicit evidence states."
confirmation_required:
  - "opening an untrusted workspace, installing or enabling extensions, changing files or settings, running tasks or terminals, or syncing settings"
okb_bundle_id: vscode
timestamp: "2026-07-31T00:00:00Z"
---

# Visual Studio Code

Source-aware tool bundle for Visual Studio Code workspaces, settings, extensions, tasks, debugging, trust, and controlled configuration changes.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- VS Code version and build
- workspace files and folder scope
- user, remote, and workspace settings
- extensions and versions
- Workspace Trust state
- tasks, launch configurations, terminals, language tooling, and logs

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer effective setting precedence, extension behavior, workspace trust, task execution state, debug configuration, and local file contents.
- Require accountable confirmation before opening an untrusted workspace, installing or enabling extensions, changing files or settings, running tasks or terminals, or syncing settings.
