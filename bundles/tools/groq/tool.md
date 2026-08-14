---
type: "Tool Guide"
title: "GroqCloud"
description: "Source-aware guidance for GroqCloud."
resource: "https://console.groq.com/docs"
okb_bundle_id: groq
timestamp: "2026-08-13T00:00:00Z"
tool_category: "High-speed generative AI inference and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "upload sensitive data, enable tools, call functions, fine-tune, publish generated output, deploy inference, incur spend, or represent factuality, safety, latency, or completion"
---
# GroqCloud Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://console.groq.com/docs

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current GroqCloud documentation for the selected model, endpoint, feature, and date.
- Organization, project, key scope, model, request, prompt, file, tool, output, usage, limit, retention, and log state.
- Data rights, security and safety review, evaluation, fallback, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable GroqCloud inference implementation and risk review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before upload sensitive data, enable tools, call functions, fine-tune, publish generated output, deploy inference, incur spend, or represent factuality, safety, latency, or completion.

## Guardrails

- Do not invent model availability, request execution, data retention, source authority, citation support, tool or function result, output accuracy, safety, latency, cost, deployment state, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
