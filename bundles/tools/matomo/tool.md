---
type: "Tool Guide"
title: "Matomo"
description: "Source-aware guidance for Matomo."
resource: "https://matomo.org/guide/"
okb_bundle_id: matomo
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Privacy-focused web and app analytics platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "deploy tracking or tags, collect or identify visitors, change consent or privacy settings, import or delete data, grant access, install plugins, or represent compliance, attribution, conversion, or revenue"
---
# Matomo Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://matomo.org/guide/
- https://developer.matomo.org/guides/tracking-consent

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Matomo analytics, consent, and privacy review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before deploy tracking or tags, collect or identify visitors, change consent or privacy settings, import or delete data, grant access, install plugins, or represent compliance, attribution, conversion, or revenue.

## Guardrails

- Do not invent visitor identity, consent, cookie state, anonymization, data residency, tracking completeness, attribution, goal or conversion accuracy, revenue, legal compliance, deletion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
