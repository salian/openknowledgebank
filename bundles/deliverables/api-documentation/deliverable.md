---
type: Deliverable Guide
title: API Documentation and Integration Guide Source-Aware Guide
description: Defines source-aware API contract and integration documentation, evidence handling, and action boundaries.
tags:
- api-documentation
- openapi
- integration-guide
- deliverable
resource: https://spec.openapis.org/oas/
okb_bundle_id: api-documentation
timestamp: '2026-07-31T00:00:00Z'
---

# API Documentation and Integration Guide Source-Aware Guide

Source-aware deliverable bundle for API references and integration guides covering versioned contracts, authentication, operations, schemas, errors, examples, limits, security, and change history.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- API owner, audience, use cases, environment, and version
- authoritative specification, code, routes, operations, and lifecycle
- authentication, authorization, scopes, credentials, and security requirements
- parameters, headers, schemas, examples, validation, and content types
- responses, errors, retries, idempotency, pagination, limits, and webhooks
- SDKs, testing, support, deprecation, changelog, and publication approval

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer endpoint behavior, schema, authentication, error response, rate limit, and version support.
- Require accountable confirmation before publishing secrets or undocumented endpoints, changing API contracts, promising compatibility, or releasing documentation without technical and security review.
