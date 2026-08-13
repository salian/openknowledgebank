---
type: "Tool Guide"
title: "Lark / Feishu"
description: "Source-aware guidance for Lark / Feishu."
resource: "https://www.larksuite.com/"
okb_bundle_id: feishu-lark
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Regional collaboration suite for messaging, documents, meetings, workflow, and structured data"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or share content, message users, schedule meetings, record or transcribe, run approvals, alter Base records, connect apps, or change access"
---
# Lark / Feishu Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.larksuite.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Lark / Feishu configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or share content, message users, schedule meetings, record or transcribe, run approvals, alter Base records, connect apps, or change access.

## Guardrails

- Do not invent regional product equivalence, user identity, message delivery, content ownership, meeting consent, transcript accuracy, approval state, record accuracy, access, or compliance.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
