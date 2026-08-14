---
type: "Tool Guide"
title: "Zammad"
description: "Source-aware guidance for Zammad."
resource: "https://admin-docs.zammad.org/"
okb_bundle_id: zammad
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source and hosted helpdesk, ticket, channel, SLA, automation, knowledge, API, and deployment platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change customer data, send messages, route or close tickets, alter SLAs or automations, grant access, expose tokens, call APIs, upgrade or restore systems, or represent identity, priority, SLA, delivery, resolution, security, or compliance"
---
# Zammad Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://admin-docs.zammad.org/
- https://docs.zammad.org/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Zammad helpdesk, automation, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change customer data, send messages, route or close tickets, alter SLAs or automations, grant access, expose tokens, call APIs, upgrade or restore systems, or represent identity, priority, SLA, delivery, resolution, security, or compliance.

## Guardrails

- Do not invent hosting or version applicability, customer identity, ticket or SLA state, message delivery, automation or API result, resolution, migration, backup or restore, security, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
