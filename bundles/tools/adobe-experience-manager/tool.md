---
type: "Tool Guide"
title: "Adobe Experience Manager"
description: "Source-aware guidance for Adobe Experience Manager."
resource: "https://business.adobe.com/products/experience-manager/adobe-experience-manager.html"
okb_bundle_id: adobe-experience-manager
timestamp: "2026-08-12T00:00:00Z"
tool_category: "Content management platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "edit or publish content, change workflows or permissions, deploy code, move assets, collect form data, or represent release approval"
---
# Adobe Experience Manager Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://business.adobe.com/products/experience-manager/adobe-experience-manager.html

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Adobe Experience Manager configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before edit or publish content, change workflows or permissions, deploy code, move assets, collect form data, or represent release approval.

## Guardrails

- Do not invent repository state, content rights, asset metadata, permission, deployment state, publication, form-data basis, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
