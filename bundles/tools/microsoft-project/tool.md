---
type: Tool Guide
title: Microsoft Project
description: Defines source-aware Microsoft Project schedule, dependency, resource, baseline, and variance review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Microsoft Project schedule brief with explicit evidence states.
confirmation_required:
- overwrite the schedule, set or clear a baseline, change assignments or calendars, publish the plan, notify resources, or commit dates or costs
okb_bundle_id: microsoft-project
timestamp: '2026-07-31T00:00:00Z'
---
# Microsoft Project

Source-aware tool bundle for Microsoft Project schedule, dependency, resource, baseline, and variance review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://www.microsoft.com/en-us/microsoft-365/project/project-management-software
- https://support.microsoft.com/en-us/project/set-and-save-a-baseline
- https://support.microsoft.com/en-us/project/how-project-schedules-tasks-behind-the-scenes

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- Project product, edition, version, file, owner, status date, calendar, work breakdown, tasks, milestones, durations, dependencies, constraints, deadlines, resources, rates, assignments, availability, costs, baseline identity and date, actuals, progress method, critical-path settings, external links, reports, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer finish date, critical path, resource availability, variance, cost, progress, baseline meaning, or schedule feasibility.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that overwrite the schedule, set or clear a baseline, change assignments or calendars, publish the plan, notify resources, or commit dates or costs.
