---
type: "Tool Guide"
title: "eClinicalWorks"
description: "Source-aware guidance for eClinicalWorks."
resource: "https://www.eclinicalworks.com/products-services/interoperability/"
okb_bundle_id: eclinicalworks
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Electronic health record and practice management platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change patient records, place or sign orders, prescribe, release results, exchange health data, submit claims, schedule care, change permissions or interfaces, or represent clinical or payment outcomes"
---
# eClinicalWorks Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.eclinicalworks.com/products-services/interoperability/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable eClinicalWorks configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change patient records, place or sign orders, prescribe, release results, exchange health data, submit claims, schedule care, change permissions or interfaces, or represent clinical or payment outcomes.

## Guardrails

- Do not invent patient identity, consent, diagnosis, medication or allergy status, order or result validity, clinician authority, interoperability state, coding or claim accuracy, payment, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
