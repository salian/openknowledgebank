---
type: Workflow
title: ChatGPT / OpenAI API source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: product surface, organization, project, account, environment, API and SDK versions; model ID or snapshot, inputs, outputs, prompts, tools, function schemas, files, vector stores, external services, authentication, permissions, retention and data controls, regional requirements, safety policy, eval data and results, latency, usage, cost, monitoring, fallback, and approvals.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable OpenAI implementation and risk brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
