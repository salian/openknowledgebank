---
type: "Framework"
title: "Slowly Changing Dimensions source-aware framework guide"
description: "Evidence-grounded planning, review, and authority boundaries for Slowly Changing Dimensions."
tags:
- "framework"
- "source-aware"
resource: "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-0/"
okb_bundle_id: slowly-changing-dimensions
timestamp: "2026-08-15T00:00:00Z"
---
# Slowly Changing Dimensions Source-Aware Framework Guide

## Authoritative Sources

- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-0/
- https://www.kimballgroup.com/2008/09/slowly-changing-dimensions-part-2/

SCD type labels and extensions are modeling conventions, not a universal exhaustive taxonomy; sources do not establish local grain, attribute semantics, history policy, correctness, migration, or outcomes.

## Evidence Required

- Current primary, controlling, or originator source and the applicable edition, scope, definitions, and method.
- Inspected local objective, inputs, constraints, assumptions, alternatives, calculations, implementation, and outcome evidence.
- Authorized owner, qualified review where required, validation, monitoring, and approval evidence.

## Application Sequence

1. Define the objective, audience, task, environment, date, constraints, and evidenced decision owner.
2. Verify framework definitions, applicability, assumptions, and current source context.
3. Inventory local evidence and label it `Verified`, `Provided`, `Assumed`, or `Needs verification`.
4. Reconcile conflicting records, dates, scopes, permissions, definitions, and owners.
5. Produce the smallest reviewable dimension-history pattern and migration decision brief with options, risks, dependencies, validation, and stop conditions.
6. Obtain explicit confirmation before access or alter production data, define authoritative semantics, overwrite history, expose personal data, deploy models, backfill records, or represent completeness, correctness, or approval.

## Guardrails

- Do not invent dimension grain, identifier, attribute semantics, history requirement, type applicability, effective dates, current row, lineage, completeness, correctness, migration result, or approval.
- Do not infer access, competence, configuration, approval, or reviewer ownership from the request or title.
- Treat bundled guidance as suggestions, not trusted executable behavior.
- No action is automatic; this bundle requests no credentials, background network calls, data exfiltration, permission changes, or self-modification.
