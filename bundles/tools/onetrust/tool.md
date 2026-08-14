---
type: "Tool Guide"
title: "OneTrust"
description: "Source-aware guidance for OneTrust."
resource: "https://www.onetrust.com/products/"
okb_bundle_id: onetrust
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Consent, privacy, data, AI, third-party risk, and compliance governance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "scan systems, collect or signal consent, block trackers, process rights requests, classify sensitive data, assess vendors or AI, change policies or controls, remediate findings, or represent legal compliance or certification"
---
# OneTrust Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.onetrust.com/products/
- https://www.onetrust.com/products/consent-management/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable OneTrust data, consent, and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before scan systems, collect or signal consent, block trackers, process rights requests, classify sensitive data, assess vendors or AI, change policies or controls, remediate findings, or represent legal compliance or certification.

## Guardrails

- Do not invent identity, consent, jurisdiction, tracker classification, data inventory, rights-request status, vendor or AI risk, control effectiveness, legal applicability, compliance, certification, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
