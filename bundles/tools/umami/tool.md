---
type: "Tool Guide"
title: "Umami"
description: "Source-aware guidance for Umami."
resource: "https://umami.is/docs"
okb_bundle_id: umami
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Privacy-focused web analytics, event, funnel, journey, cloud, self-hosted, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "deploy tracking, collect identifiers or event properties, change retention or sharing, expose tokens, call APIs, import or export data, upgrade deployments, or represent consent, visitor identity, metric, attribution, privacy, availability, or business results"
---
# Umami Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://umami.is/docs
- https://umami.is/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Umami tracking, privacy, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before deploy tracking, collect identifiers or event properties, change retention or sharing, expose tokens, call APIs, import or export data, upgrade deployments, or represent consent, visitor identity, metric, attribution, privacy, availability, or business results.

## Guardrails

- Do not invent deployment or version applicability, visitor identity, consent requirement, event semantics, metric definition, data completeness or freshness, attribution, API result, privacy compliance, availability, or business conclusion.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
