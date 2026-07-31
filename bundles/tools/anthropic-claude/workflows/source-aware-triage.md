---
type: Workflow
title: Claude and Anthropic API Source-Aware Triage
description: Inspect-first workflow for model, Messages API, prompt, tool use, caching, token, safety, privacy, evaluation, and production review.
okb_bundle_id: anthropic-claude
---
# Claude and Anthropic API Source-Aware Triage

1. State the decision and direct answer possible now.
2. Record Verified, Provided, Assumed, and Needs verification separately.
3. Inspect the current source version and exact local evidence for account and workspace, current model ID and date, API and SDK version, system and user prompts, tool schemas and permission model, data classification, retention controls, token and cache behavior, rate and spend limits, evaluations, logs, approvals, and rollback.
4. Reconcile definitions, identifiers, dates, scope, permissions, processing, and ownership.
5. Record alternatives, stop conditions, and an independent cross-check.
6. Require explicit approval before actions that send sensitive data, expose API keys, invoke tools with side effects, execute model-suggested actions, change retention or safety controls, deploy integrations, or incur spend.
7. End with a Source Note naming source URLs, user evidence, and missing sources.
