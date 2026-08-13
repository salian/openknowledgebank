---
type: "Tool Guide"
title: "Cloudflare Web Analytics"
description: "Source-aware guidance for Cloudflare Web Analytics."
resource: "https://developers.cloudflare.com/web-analytics/"
okb_bundle_id: cloudflare-web-analytics
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Privacy-oriented web analytics service"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "enable or disable collection, add or change beacon code, rules or filters, expose visitor data, change site configuration, export reports, or represent traffic, performance, privacy, or conversion outcomes"
---
# Cloudflare Web Analytics Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developers.cloudflare.com/web-analytics/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Cloudflare Web Analytics configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before enable or disable collection, add or change beacon code, rules or filters, expose visitor data, change site configuration, export reports, or represent traffic, performance, privacy, or conversion outcomes.

## Guardrails

- Do not invent site ownership, collection state, visitor identity, consent applicability, metric definition, data completeness, bot treatment, Core Web Vital result, attribution, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
