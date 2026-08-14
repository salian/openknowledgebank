---
type: "Tool Guide"
title: "Redmine"
description: "Source-aware guidance for Redmine."
resource: "https://www.redmine.org/guide"
okb_bundle_id: redmine
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source project, issue, time, wiki, API, and self-hosted platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter issues, projects, time entries, workflows or permissions, send email, install plugins, expose API keys, change repositories, upgrade systems, restore backups, or represent status, effort, delivery, security, or availability"
---
# Redmine Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.redmine.org/guide
- https://www.redmine.org/projects/redmine/wiki/Rest_api

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Redmine workflow, API, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter issues, projects, time entries, workflows or permissions, send email, install plugins, expose API keys, change repositories, upgrade systems, restore backups, or represent status, effort, delivery, security, or availability.

## Guardrails

- Do not invent version or plugin compatibility, project or issue state, workflow transition, time accuracy, repository state, permission, API result, plugin safety, backup validity, migration, uptime, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
