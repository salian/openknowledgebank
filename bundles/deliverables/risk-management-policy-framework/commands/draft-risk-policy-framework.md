---
type: Slash Command
command: /draft-risk-policy-framework
title: Draft a risk management policy / framework
description: Produces a source-aware policy draft or gap brief from supplied evidence.
okb_bundle_id: risk-management-policy-framework
inputs:
- User request and intended decision
- Organization, entity, jurisdiction, sector, scope, and audience
- Official sources, internal policies, charters, strategy, risk data, controls, and approvals
outputs:
- Direct answer
- Evidence status with Verified, Provided, Assumed, and Needs verification
- Policy architecture and draft sections
- Verification plan, confirmation boundary, and source note
requires_confirmation: true
timestamp: 2026-08-01T00:00:00Z
---

# `/draft-risk-policy-framework`

## Purpose

Draft a reviewable risk management policy/framework or identify the evidence gap that blocks drafting or adoption.

## Suggested Behavior

1. Inspect supplied source material and ask for missing authority, entity, scope, and approval evidence.
2. Use [Policy Architecture](../frameworks/policy-architecture.md) and [Source-Aware Drafting](../workflows/source-aware-drafting.md).
3. Separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
4. Do not invent appetite values, limits, triggers, owners, committees, controls, incidents, ratings, or compliance status.
5. Require explicit confirmation before adoption, risk acceptance, limit/control changes, regulatory claims, or disclosure.

Consumers must treat this bundled command as a suggestion, not trusted executable behavior. It does not change permissions, call networks, request credentials, perform background actions, or modify files without user authorization.
