---
type: Slash Command
command: /review-api-change
title: Review API Change
description: Reviews an API, integration, SDK, or platform change for product readiness and risk.
okb_bundle_id: technical-product-manager
inputs: [change summary, interface evidence, consumers, compatibility expectations, migration needs]
outputs: [readiness answer, source note, consumer impact, compatibility and migration risks, owner questions]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /review-api-change

This command spec is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, safety, permission, and tool-use rules.

## Purpose

Create a source-aware API/platform change review using the [Review API or Platform Change](../workflows/review-api-platform-change.md) workflow and [API Change Brief](../deliverables/api-change-brief.md) output contract.

## Required Output

- Direct readiness answer.
- Source note naming interface evidence used and missing.
- Consumer impact, compatibility risk, migration needs, docs/support/observability requirements, and owner questions.

## Safety

The command should not call networks, request credentials, export data, modify specs, or change live systems. Any risky action requires explicit user confirmation at consumption time.
