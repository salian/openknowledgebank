---
type: "Tool Guide"
title: "osTicket"
description: "Source-aware guidance for osTicket."
resource: "https://docs.osticket.com/"
okb_bundle_id: osticket
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source support ticket, help desk, and self-hosted workflow system"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create, assign, close or delete tickets, expose customer messages or attachments, send replies, change SLA or routing, install plugins, expose API keys, upgrade systems, or represent response, resolution, security, or availability"
---
# osTicket Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.osticket.com/
- https://osticket.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable osTicket workflow, integration, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create, assign, close or delete tickets, expose customer messages or attachments, send replies, change SLA or routing, install plugins, expose API keys, upgrade systems, or represent response, resolution, security, or availability.

## Guardrails

- Do not invent ticket or user identity, confidentiality, assignment, SLA calculation, reply delivery, resolution, plugin safety, API result, backup validity, security, uptime, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
