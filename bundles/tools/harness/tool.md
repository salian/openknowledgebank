---
type: "Tool Guide"
title: "Harness"
description: "Source-aware guidance for Harness."
resource: "https://www.harness.io/products"
okb_bundle_id: harness
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Software delivery, feature management, cloud cost, security, and incident platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "run pipelines, deploy code, change infrastructure or feature flags, expose secrets, approve policies, remediate findings, alter budgets, manage incidents, or represent delivery or security state"
---
# Harness Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.harness.io/products
- https://developer.harness.io/docs/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Harness developer documentation for the account, modules, and deployment model.
- Account, org, project, connector, secret, service, environment, infrastructure, pipeline, artifact, flag, policy, approval, cost, finding, and audit state.
- Change and security owner, test evidence, rollback, incident plan, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Harness software delivery and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before run pipelines, deploy code, change infrastructure or feature flags, expose secrets, approve policies, remediate findings, alter budgets, manage incidents, or represent delivery or security state.

## Guardrails

- Do not invent source or artifact provenance, pipeline result, environment state, deployment, flag exposure, secret safety, policy approval, cost saving, vulnerability, incident resolution, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
