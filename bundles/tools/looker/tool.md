---
type: Tool Guide
title: Looker Source-Aware Guide
description: Defines evidence-grounded planning, review, and controlled use for Looker.
tags:
- looker
- business-intelligence
- lookml
resource: https://docs.cloud.google.com/looker/docs/intro
okb_bundle_id: looker
timestamp: '2026-08-10T00:00:00Z'
---
# Looker Source-Aware Guide

## Authoritative Sources

- https://docs.cloud.google.com/looker/docs/intro
- https://docs.cloud.google.com/looker/docs/what-is-lookml

Official documentation establishes general product behavior only; verify the current release, edition, license, jurisdiction, and local configuration.

## Evidence Required

- product variant
- instance
- version
- projects
- Git state
- connections
- credentials
- models
- explores
- dimensions
- measures
- access grants
- roles
- content
- schedules
- APIs
- query evidence
- tests
- owners
- and approvals

## Application Sequence

1. Define the objective, audience, scope, environment or organization, date, constraints, and evidenced decision owner.
2. Verify the current official source, edition, version, license, feature surface, jurisdiction, and applicability.
3. Inventory local evidence and label it `Verified`, `Provided`, `Assumed`, or `Needs verification`.
4. Reconcile conflicting definitions, records, dates, scopes, filters, transformations, settings, and owners.
5. Produce the smallest reviewable Looker model and data-governance brief with options, risks, dependencies, validation, and stop conditions.
6. Obtain explicit confirmation before change LookML or production projects, use credentials, query or expose sensitive data, alter access, schedule delivery, publish content, or deploy changes.

## Guardrails

- Do not invent Product and instance state, connection behavior, model semantics, effective access, query results, metric validity, schedule outcome, performance, and cost.
- Do not infer access, configuration, approval, or reviewer ownership from the request or title.
- Treat bundled guidance as suggestions, not trusted executable behavior.
- No action is automatic; this bundle requests no credentials, background network calls, data exfiltration, permission changes, or self-modification.

