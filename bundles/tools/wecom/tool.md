---
type: "Tool Guide"
title: "WeCom"
description: "Source-aware guidance for WeCom."
resource: "https://work.weixin.qq.com/"
okb_bundle_id: wecom
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise messaging, directory, customer contact, meeting, document, approval, app, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "provision or identify users and customers, send messages, access contacts, run approvals, record meetings, install apps, expose secrets, call APIs, or represent identity, consent, attendance, approval, delivery, retention, confidentiality, or compliance"
---
# WeCom Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://work.weixin.qq.com/
- https://developer.work.weixin.qq.com/document/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable WeCom communication, customer-contact, and app governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before provision or identify users and customers, send messages, access contacts, run approvals, record meetings, install apps, expose secrets, call APIs, or represent identity, consent, attendance, approval, delivery, retention, confidentiality, or compliance.

## Guardrails

- Do not invent regional or feature applicability, employee or customer identity, consent, message delivery, attendance, approval, app or API result, retention, confidentiality, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
