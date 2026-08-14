---
type: "Tool Guide"
title: "Plausible Analytics"
description: "Source-aware guidance for Plausible Analytics."
resource: "https://plausible.io/docs"
okb_bundle_id: plausible-analytics
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Privacy-focused web analytics, conversion, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "install tracking, send events or revenue, import or delete data, expose dashboards or API keys, change goals or access, query or export analytics, or represent anonymity, consent requirements, attribution, conversion, or revenue"
---
# Plausible Analytics Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://plausible.io/docs
- https://plausible.io/docs/stats-api

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Plausible analytics and privacy review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before install tracking, send events or revenue, import or delete data, expose dashboards or API keys, change goals or access, query or export analytics, or represent anonymity, consent requirements, attribution, conversion, or revenue.

## Guardrails

- Do not invent site ownership, visitor identity, personal-data status, consent applicability, event completeness, metric definition, API result, attribution, conversion, revenue, legal compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
