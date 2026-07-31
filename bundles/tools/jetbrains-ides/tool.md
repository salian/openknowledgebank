---
type: Tool Guide
title: JetBrains IDEs
description: Defines source-aware JetBrains IDE project trust, build, plugin, run configuration, and team settings review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a JetBrains IDE configuration brief with explicit evidence states.
confirmation_required:
- trust a project, resolve dependencies, execute code or scripts, install or update plugins, expose environment variables, change shared settings, or commit and push code
okb_bundle_id: jetbrains-ides
timestamp: '2026-07-31T00:00:00Z'
---
# JetBrains IDEs

Source-aware tool bundle for JetBrains IDE project trust, build, plugin, run configuration, and team settings review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://www.jetbrains.com/ides/
- https://www.jetbrains.com/help/idea/project-security.html
- https://www.jetbrains.com/help/idea/managing-plugins.html

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- JetBrains product, edition, version, license, project source and trust status
- language, SDK, build tool, dependencies, indexes, plugins, versions, project and user settings
- run and debug configurations, arguments, environment variables, secrets, VCS state, inspections, tests, build outputs, remote development, team settings, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer project safety, dependency resolution, plugin trust, build or test result, runtime behavior, configuration parity, or code correctness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that trust a project, resolve dependencies, execute code or scripts, install or update plugins, expose environment variables, change shared settings, or commit and push code.
