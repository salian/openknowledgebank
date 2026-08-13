---
type: "Tool Guide"
title: "FloQast"
description: "Source-aware guidance for FloQast."
resource: "https://www.floqast.com/"
okb_bundle_id: floqast
timestamp: "2026-08-13T00:00:00Z"
tool_category: "AI-assisted accounting close, reconciliation, compliance, and record-to-report platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import ledgers, match transactions, prepare or post entries, reconcile accounts, collect evidence, test controls, close periods, generate reports, or represent financial accuracy"
---
# FloQast Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.floqast.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable FloQast configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import ledgers, match transactions, prepare or post entries, reconcile accounts, collect evidence, test controls, close periods, generate reports, or represent financial accuracy.

## Guardrails

- Do not invent account ownership, transaction match, reconciliation, journal validity, control effectiveness, close status, financial statement accuracy, audit readiness, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
