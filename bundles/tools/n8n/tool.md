---
type: "Tool Guide"
title: "n8n"
description: "Source-aware guidance for n8n."
resource: "https://docs.n8n.io/"
okb_bundle_id: n8n
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Workflow automation, integration, AI-agent, API, and self-hosted platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "store credentials, call external or production systems, execute code or AI tools, activate schedules or webhooks, process personal data, install community nodes, change access, deploy or upgrade instances, or represent execution, delivery, security, or business results"
---
# n8n Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.n8n.io/
- https://docs.n8n.io/api/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable n8n workflow, credential, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before store credentials, call external or production systems, execute code or AI tools, activate schedules or webhooks, process personal data, install community nodes, change access, deploy or upgrade instances, or represent execution, delivery, security, or business results.

## Guardrails

- Do not invent credential scope, node behavior, input or output data, workflow execution, AI tool action, human review, webhook exposure, community-node safety, API result, deployment, availability, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
