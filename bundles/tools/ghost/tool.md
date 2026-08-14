---
type: "Tool Guide"
title: "Ghost"
description: "Source-aware guidance for Ghost."
resource: "https://ghost.org/docs/"
okb_bundle_id: ghost
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Publishing, membership, subscription, and newsletter platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "publish or delete content, change themes or code, import or export members, charge subscribers, send newsletters, connect services, or represent delivery or revenue"
---
# Ghost Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://ghost.org/docs/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Ghost documentation and product lifecycle information.
- Site, plan, theme, members, Stripe, email, integration, permission, and analytics configuration.
- Content rights, audience consent, test results, change owner, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Ghost configuration and publishing review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before publish or delete content, change themes or code, import or export members, charge subscribers, send newsletters, connect services, or represent delivery or revenue.

## Guardrails

- Do not invent content ownership, publication state, member consent, subscription or payment status, email delivery, analytics result, integration state, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
