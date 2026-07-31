---
type: Tool Guide
title: Hugging Face
description: Defines source-aware Hugging Face Hub and inference model selection, provenance, security, evaluation, and deployment review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Hugging Face model use brief with explicit evidence states.
confirmation_required:
- download or execute untrusted model code, accept gated terms, send sensitive data, expose tokens, deploy endpoints or Spaces, publish artifacts, or incur inference charges
okb_bundle_id: hugging-face
timestamp: '2026-07-31T00:00:00Z'
---
# Hugging Face

Source-aware tool bundle for Hugging Face Hub and inference model selection, provenance, security, evaluation, and deployment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://huggingface.co/docs/inference-providers/en/index
- https://huggingface.co/docs/inference-providers/security
- https://huggingface.co/docs/hub/security-tokens

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- Hugging Face surface, account, organization, repository, model, dataset, Space, provider, endpoint, and exact revision
- model and dataset cards, license, files, provenance, gated access, token scope, remote-code and artifact scans
- input data, privacy, provider routing and data policy, evaluation methods and results, hardware, latency, cost, monitoring, rollback, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer license compatibility, model safety, quality, provider selection, data handling, scan result, inference output, cost, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that download or execute untrusted model code, accept gated terms, send sensitive data, expose tokens, deploy endpoints or Spaces, publish artifacts, or incur inference charges.
