---
type: "Tool Guide"
title: "Freshservice"
description: "Source-aware guidance for Freshservice."
resource: "https://www.freshworks.com/freshservice/features/"
okb_bundle_id: freshservice
timestamp: "2026-08-13T00:00:00Z"
tool_category: "AI-powered IT service, asset, operations, and enterprise service management platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or resolve tickets, approve or deploy changes, run discovery, alter assets or CMDB, automate access, deploy AI agents, trigger remediation, or represent service health or compliance"
---
# Freshservice Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.freshworks.com/freshservice/features/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Freshservice configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or resolve tickets, approve or deploy changes, run discovery, alter assets or CMDB, automate access, deploy AI agents, trigger remediation, or represent service health or compliance.

## Guardrails

- Do not invent requester identity, incident severity, root cause, change risk or success, asset ownership, CMDB accuracy, entitlement, AI action, SLA, service health, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
