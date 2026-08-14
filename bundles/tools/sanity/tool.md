---
type: "Tool Guide"
title: "Sanity"
description: "Source-aware guidance for Sanity."
resource: "https://www.sanity.io/docs"
okb_bundle_id: sanity
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Structured content, Studio, API, real-time, release, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "change schemas or documents, publish releases, upload protected assets, mutate or delete data, deploy Studio or Functions, enable AI actions, expose tokens, trigger webhooks, or represent content, translation, query, publication, rights, or availability"
---
# Sanity Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.sanity.io/docs
- https://www.sanity.io/products

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Sanity content-model, API, and AI governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before change schemas or documents, publish releases, upload protected assets, mutate or delete data, deploy Studio or Functions, enable AI actions, expose tokens, trigger webhooks, or represent content, translation, query, publication, rights, or availability.

## Guardrails

- Do not invent project or dataset state, schema or field identity, content rights, query or mutation result, reference integrity, translation, release or publication state, AI action, token scope, webhook, usage, uptime, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
