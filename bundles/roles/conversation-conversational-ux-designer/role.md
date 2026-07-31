---
type: Role
title: Conversation / Conversational UX Designer Source-Aware Guide
description: Defines source-aware conversation design, intent coverage, safety, and
  experience validation, evidence handling, and action boundaries.
tags:
- conversation-conversational-ux-designer
- conversation
- role
resource: https://www.onetonline.org/link/summary/15-1255.00
okb_bundle_id: conversation-conversational-ux-designer
timestamp: '2026-07-31T00:00:00Z'
---
# Conversation / Conversational UX Designer Source-Aware Guide

Source-aware role bundle for conversation design, intent coverage, safety, and experience validation, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative Sources

- https://www.onetonline.org/link/summary/15-1255.00

Use the occupation source to ground role scope. For standards or regulated decisions, name the applicable primary standards or regulator source in the response, then verify its current version, effective date, jurisdiction, and applicability. A generic phrase such as `regulatory guidelines` is not a sufficient source note when a specific source is listed here.

## Evidence Required

- users, channel, use cases, intents, entities, taxonomy, dialog states, prompts, fallback, and escalation
- model or NLU version and data
- privacy, consent, safety, accessibility, language, transcript, test, and metric evidence

## Application Sequence

1. Define the decision, scope, accountable reviewer, date, jurisdiction, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, methods, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming a state or result.
- Distinguish verified source facts from prompt-provided evidence, assumptions, and missing evidence.
- Do not infer intent coverage, model behavior, user comprehension, safety, accessibility, or measured performance.
- Do not invent an artifact owner, author, date, version, approval, or reviewer.
- Require accountable confirmation before actions that deploy prompts or a model, collect user data, send outbound messages, or claim safety, usability, or accessibility.
