---
type: Tool Guide
title: Jira Service Management
description: Defines source-aware Jira Service Management request, workflow, SLA, queue, automation, and permission review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Jira Service Management change brief with explicit evidence states.
confirmation_required:
- edit requests, send comments or notifications, add customers, change workflows, permissions, SLAs, queues, or automations, expose attachments, or transition incidents
okb_bundle_id: jira-service-management
timestamp: '2026-07-31T00:00:00Z'
---
# Jira Service Management

Source-aware tool bundle for Jira Service Management request, workflow, SLA, queue, automation, and permission review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://www.atlassian.com/software/jira/service-management
- https://support.atlassian.com/jira-service-management-cloud/docs/what-users-and-roles-are-there-in-jira-service-management/

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- site, product plan, project or space, environment, issue and request types, fields, forms, workflow, statuses, queues, SLA goals, calendars, roles, permissions, customers, organizations, knowledge base, automation, integrations, notifications, audit logs, sample issues, privacy, tests, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer request state, permission, SLA result, queue membership, automation behavior, customer visibility, incident state, or service performance.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that edit requests, send comments or notifications, add customers, change workflows, permissions, SLAs, queues, or automations, expose attachments, or transition incidents.
