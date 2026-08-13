---
type: "Tool Guide"
title: "Connecteam"
description: "Source-aware guidance for Connecteam."
resource: "https://developer.connecteam.com/docs/introduction-1"
okb_bundle_id: connecteam
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Workforce management and employee operations platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or change employee records, schedules, shifts, time or attendance, send communications, assign tasks or training, publish documents, change permissions, export personal data, or represent payroll or employment outcomes"
---
# Connecteam Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developer.connecteam.com/docs/introduction-1

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Connecteam configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or change employee records, schedules, shifts, time or attendance, send communications, assign tasks or training, publish documents, change permissions, export personal data, or represent payroll or employment outcomes.

## Guardrails

- Do not invent employee identity or status, availability, shift assignment, hours or break compliance, pay calculation, task or training completion, message delivery, employment decision, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
