---
type: "Tool Guide"
title: "SoapUI Open Source"
description: "Source-aware guidance for SoapUI Open Source."
resource: "https://www.soapui.org/docs/"
okb_bundle_id: soapui
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source SOAP and REST functional, regression, mock, load, and automation testing tool"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "send requests to systems, include credentials or production data, execute scripts, run load or security tests, expose project secrets, modify endpoints, or represent coverage, correctness, performance, vulnerability, or production readiness"
---
# SoapUI Open Source Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.soapui.org/docs/
- https://www.soapui.org/docs/open-source/features/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SoapUI API test design and execution review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before send requests to systems, include credentials or production data, execute scripts, run load or security tests, expose project secrets, modify endpoints, or represent coverage, correctness, performance, vulnerability, or production readiness.

## Guardrails

- Do not invent endpoint or schema applicability, authorization, test-data safety, request delivery, response meaning, assertion validity, coverage, performance, vulnerability, compatibility, or production readiness.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
