---
type: Tool Guide
title: Epic Source-Aware Guide
description: Defines evidence-grounded planning, review, and controlled use for Epic.
tags:
- epic
- ehr
- healthcare-interoperability
resource: https://fhir.epic.com/
okb_bundle_id: epic
timestamp: '2026-08-10T00:00:00Z'
---
# Epic Source-Aware Guide

## Authoritative Sources

- https://fhir.epic.com/
- https://open.epic.com/interface/FHIR

Official documentation establishes general product behavior only; verify the current release, edition, license, jurisdiction, and local configuration.

## Evidence Required

- organization
- Epic version
- environment
- endpoint
- supported FHIR resources
- SMART launch
- OAuth scopes
- patient and encounter context
- clinical workflow
- data mappings
- consent
- validation
- monitoring
- owners
- and approvals

## Application Sequence

1. Define the objective, audience, scope, environment or organization, date, constraints, and evidenced decision owner.
2. Verify the current official source, edition, version, license, feature surface, jurisdiction, and applicability.
3. Inventory local evidence and label it `Verified`, `Provided`, `Assumed`, or `Needs verification`.
4. Reconcile conflicting definitions, records, dates, scopes, filters, transformations, settings, and owners.
5. Produce the smallest reviewable Epic interoperability and clinical-safety brief with options, risks, dependencies, validation, and stop conditions.
6. Obtain explicit confirmation before access or alter health records, register or launch apps, use credentials, make clinical interpretations, change workflows, transmit protected data, or deploy integrations.

## Guardrails

- Do not invent Environment and endpoint state, supported resources, patient identity, clinical facts, authorization, consent, mapping validity, app behavior, safety, and implementation approval.
- Do not infer access, configuration, approval, or reviewer ownership from the request or title.
- Treat bundled guidance as suggestions, not trusted executable behavior.
- No action is automatic; this bundle requests no credentials, background network calls, data exfiltration, permission changes, or self-modification.

