---
type: "Tool Guide"
title: "Ollama"
description: "Source-aware guidance for Ollama."
resource: "https://docs.ollama.com/"
okb_bundle_id: ollama
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Local and cloud model runtime, management, and API platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "download or execute models, send data to cloud models, expose API endpoints, run model-requested tools, alter model files, delete models, consume GPU, memory or paid resources, or represent model identity, privacy, output accuracy, tool execution, or safety"
---
# Ollama Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.ollama.com/
- https://ollama.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Ollama model, API, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before download or execute models, send data to cloud models, expose API endpoints, run model-requested tools, alter model files, delete models, consume GPU, memory or paid resources, or represent model identity, privacy, output accuracy, tool execution, or safety.

## Guardrails

- Do not invent model availability, digest or provenance, local versus cloud execution, data retention, context, parameter support, structured-output validity, tool-call safety, output accuracy, resource use, performance, security, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
