---
type: Tool Guide
title: ChatGPT / OpenAI API
description: Defines source-aware ChatGPT and OpenAI API use-case, model, tool, data, evaluation, and deployment review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a OpenAI implementation and risk brief with explicit evidence states.
confirmation_required:
- send sensitive data, call external tools, upload files, create or delete resources, change retention controls, expose credentials, deploy, or incur usage charges
okb_bundle_id: openai-chatgpt
timestamp: '2026-07-31T00:00:00Z'
---
# ChatGPT / OpenAI API

Source-aware tool bundle for ChatGPT and OpenAI API use-case, model, tool, data, evaluation, and deployment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://openai.com/api/
- https://developers.openai.com/api/docs/guides/tools
- https://developers.openai.com/api/docs/guides/your-data

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- product surface, organization, project, account, environment, API and SDK versions
- model ID or snapshot, inputs, outputs, prompts, tools, function schemas, files, vector stores, external services, authentication, permissions, retention and data controls, regional requirements, safety policy, eval data and results, latency, usage, cost, monitoring, fallback, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer current capability, model behavior, output accuracy, safety, retention setting, regional eligibility, cost, tool result, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that send sensitive data, call external tools, upload files, create or delete resources, change retention controls, expose credentials, deploy, or incur usage charges.
