---
type: "Tool Guide"
title: "Insomnia"
description: "Source-aware guidance for Insomnia."
resource: "https://developer.konghq.com/index/insomnia/"
okb_bundle_id: insomnia
timestamp: "2026-08-14T00:00:00Z"
tool_category: "API design, debugging, testing, mocking, and automation client"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "send requests to live systems, expose credentials, run scripts or tests, create public mocks, synchronize repositories, export data, change API specifications, or represent test or service results"
---
# Insomnia Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developer.konghq.com/index/insomnia/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Insomnia API workflow and security review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before send requests to live systems, expose credentials, run scripts or tests, create public mocks, synchronize repositories, export data, change API specifications, or represent test or service results.

## Guardrails

- Do not invent endpoint safety, credential scope, request execution, response authenticity, test coverage, mock trust, specification validity, Git state, API behavior, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
