---
type: "Tool Guide"
title: "SystmOne"
description: "Source-aware guidance for SystmOne."
resource: "https://tpp-uk.com/products/"
okb_bundle_id: systmone
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Electronic health record, clinical workflow, prescribing, interoperability, reporting, and governance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change health records, document clinical care, prescribe or administer medicines, book appointments, refer patients, share data, configure decision support, or make diagnosis, treatment, eligibility, safeguarding, or clinical-safety decisions"
---
# SystmOne Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://tpp-uk.com/products/
- https://tpp-uk.com/systmone/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SystmOne clinical workflow and information-governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change health records, document clinical care, prescribe or administer medicines, book appointments, refer patients, share data, configure decision support, or make diagnosis, treatment, eligibility, safeguarding, or clinical-safety decisions.

## Guardrails

- Do not invent patient identity, record completeness, diagnosis, medication or allergy state, prescription, result interpretation, referral, consent, capacity, eligibility, safeguarding, clinical outcome, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
