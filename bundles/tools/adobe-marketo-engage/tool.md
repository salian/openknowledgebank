---
type: "Tool Guide"
title: "Adobe Marketo Engage"
description: "Source-aware guidance for Adobe Marketo Engage."
resource: "https://business.adobe.com/products/marketo.html"
okb_bundle_id: adobe-marketo-engage
timestamp: "2026-08-12T00:00:00Z"
tool_category: "Marketing automation platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or update people, change scoring, activate campaigns, send communications, sync CRM data, export records, or represent consent or attribution"
---
# Adobe Marketo Engage Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://business.adobe.com/products/marketo.html

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Adobe Marketo Engage configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or update people, change scoring, activate campaigns, send communications, sync CRM data, export records, or represent consent or attribution.

## Guardrails

- Do not invent person identity, consent, field semantics, score, membership, campaign state, delivery, attribution, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
