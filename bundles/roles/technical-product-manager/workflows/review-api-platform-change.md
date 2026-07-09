---
type: Workflow
title: Review API or Platform Change
description: Reviews API, integration, or platform changes for product value, compatibility, migration, and launch risk.
tags: [api, platform, compatibility, migration]
okb_bundle_id: technical-product-manager
timestamp: 2026-07-09T00:00:00Z
---

# Review API or Platform Change

Use this workflow when the user asks whether an API, integration, SDK, platform, or developer-experience change is product-ready.

## Inputs

- Proposed change and product rationale.
- Source-of-record interface evidence such as an OpenAPI spec, docs, schema, contract, code excerpt, or owner-provided description.
- Consumer segments, affected clients, compatibility expectations, versioning policy, support burden, and migration path.
- Observability, error behavior, security/privacy/accessibility/compliance constraints, and rollout/rollback plan.

## Review Pattern

- State whether the change is ready, conditionally ready, or not ready for commitment.
- Define what the change does and does not change.
- Identify affected consumers and compatibility risk.
- List migration, documentation, support, observability, and incident-readiness requirements.
- Separate product value, technical feasibility, operational risk, and unresolved evidence gaps.

## Output Contract

- Direct readiness answer.
- Source note naming the interface evidence used and missing evidence.
- Consumer and compatibility impact.
- Required docs, examples, migration notes, tests, telemetry, support readiness, and rollback.
- Open questions for engineering, security/privacy, legal/compliance, support, and go-to-market owners.

Never fabricate endpoint names, request/response fields, status codes, rate limits, version policies, consumers, or compatibility guarantees.
