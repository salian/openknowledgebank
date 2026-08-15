---
type: "Framework"
title: "dbt Staging, Intermediate, and Marts Layering source-aware framework guide"
description: "Evidence-grounded planning, review, and authority boundaries for dbt Staging, Intermediate, and Marts Layering."
tags:
- "framework"
- "source-aware"
resource: "https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview"
okb_bundle_id: dbt-layering-convention
timestamp: "2026-08-14T00:00:00Z"
---
# dbt Staging, Intermediate, and Marts Layering Source-Aware Framework Guide

## Authoritative Sources

- https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview

Framework sources describe generalized concepts and methods; they do not establish local applicability, inputs, decisions, authority, or outcomes.

## Evidence Required

- Current primary or originator source and the applicable edition, scope, definitions, and method.
- Inspected local inputs, constraints, assumptions, alternatives, calculations, and outcome evidence.
- Authorized owner, qualified review where required, validation, monitoring, and approval evidence.

## Application Sequence

1. Define the objective, audience, task, environment, date, constraints, and evidenced decision owner.
2. Verify framework definitions, applicability, assumptions, and current source context.
3. Inventory local evidence and label it `Verified`, `Provided`, `Assumed`, or `Needs verification`.
4. Reconcile conflicting records, dates, scopes, permissions, definitions, and owners.
5. Produce the smallest reviewable dbt layering and migration decision brief with options, risks, dependencies, validation, and stop conditions.
6. Obtain explicit confirmation before access production data, expose credentials, create or alter models and schemas, run jobs, deploy changes, or represent lineage, semantics, quality, performance, or approval.

## Guardrails

- Do not invent source schema, model grain or semantics, lineage, contract, test result, performance, compatibility, data quality, deployment state, or approval.
- Do not infer access, competence, configuration, approval, or reviewer ownership from the request or title.
- Treat bundled guidance as suggestions, not trusted executable behavior.
- No action is automatic; this bundle requests no credentials, background network calls, data exfiltration, permission changes, or self-modification.
