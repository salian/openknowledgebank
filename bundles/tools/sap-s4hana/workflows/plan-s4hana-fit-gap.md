---
type: Workflow
title: Plan SAP S/4HANA Fit-Gap
description: "Evidence-first workflow for translating a business requirement into SAP S/4HANA fit-gap analysis."
okb_bundle_id: sap-s4hana
timestamp: "2026-07-09T00:00:00Z"
---

# Plan SAP S/4HANA Fit-Gap

## When To Use

Use this workflow when a user asks whether SAP S/4HANA can support a business process, report, integration, migration, or configuration need.

## Steps

1. Identify the target process and decision: line of business, legal entity, geography, process owner, deadline, and desired output.
2. Establish source scope: deployment model, edition, release, localization, activated scope, licensed capabilities, and official SAP source categories to inspect.
3. Collect local evidence: process maps, configuration evidence, Fiori app/role evidence, master data, transactional examples, integration contracts, reports, and known customizations.
4. Separate facts: verified official SAP facts, verified customer evidence, assumptions for this draft, and missing evidence.
5. Draft the fit-gap table: requirement, standard SAP option, customer-specific gap, dependency, risk, owner, validation action, and decision status.
6. Add action controls: list any live-system, data, security, finance, statutory, or production action that requires explicit confirmation and authorized access.

## Output Requirements

The final answer should include a direct recommendation only when official source scope and local customer evidence are sufficient. Otherwise, state the provisional path and the exact evidence needed next.

Include a **Source note** naming official SAP source categories, user-provided tenant evidence, assumptions, and missing verification.
