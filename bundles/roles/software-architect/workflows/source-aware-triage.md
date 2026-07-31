---
type: Workflow
title: Software Architect source-aware triage
---

# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: stakeholders, business requirements, constraints, and quality attributes; system context, components, interfaces, data, and deployment topology; current technology versions, dependencies, and operational evidence; threat model, privacy, reliability, capacity, cost, and compliance requirements; alternatives, tradeoffs, ADRs, validation, ownership, and approval.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, and owners.
5. Produce the smallest reviewable architecture decision brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification`, and prohibited actions
- **Source note** with sources and limitations
