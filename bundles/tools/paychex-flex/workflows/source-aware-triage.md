---
type: Workflow
title: Paychex Flex source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: company and worker identifiers, Paychex product, environment, API version, application, client-credential scope, and authorization; worker demographics, employment, compensation, pay period, checks, earnings, deductions, taxes, benefits, time, source-of-record and reconciliation rules; webhook domains, endpoint authentication, audit history, privacy, tests, payroll approvals, and rollback.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable Paychex Flex integration and payroll brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
