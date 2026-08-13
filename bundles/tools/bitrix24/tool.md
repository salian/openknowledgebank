---
type: "Tool Guide"
title: "Bitrix24"
description: "Source-aware guidance for Bitrix24."
resource: "https://apidocs.bitrix24.com/"
okb_bundle_id: bitrix24
timestamp: "2026-08-13T00:00:00Z"
tool_category: "CRM and workplace platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or update CRM or workplace records, send messages, change users or permissions, upload files, alter catalog or stock data, install apps, invoke webhooks, or represent completion"
---
# Bitrix24 Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://apidocs.bitrix24.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Bitrix24 configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or update CRM or workplace records, send messages, change users or permissions, upload files, alter catalog or stock data, install apps, invoke webhooks, or represent completion.

## Guardrails

- Do not invent portal state, person or company identity, CRM stage, task state, message delivery, stock balance, permission, API result, workflow outcome, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
