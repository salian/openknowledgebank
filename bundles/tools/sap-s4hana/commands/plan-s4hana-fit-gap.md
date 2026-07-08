---
type: Slash Command
command: /plan-s4hana-fit-gap
title: Plan SAP S/4HANA Fit-Gap
description: "Create a source-scoped SAP S/4HANA fit-gap plan without inventing tenant scope, configuration, roles, data, or integrations."
okb_bundle_id: sap-s4hana
inputs:
  - business process or decision question
  - S/4HANA edition, release, and activated scope evidence
  - current process, configuration, role, data, integration, and reporting evidence
  - target outcome and constraints
outputs:
  - SAP S/4HANA fit-gap plan
  - missing local evidence
  - source and tenant verification checklist
  - confirmation boundaries for risky actions
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-s4hana-fit-gap

Purpose: produce an SAP S/4HANA fit-gap plan that is ready for human review, not an unsafely executed implementation instruction.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business process, report, integration, migration, or configuration question.
- S/4HANA deployment model, edition, release, localization, licensed capability, and activated scope evidence, if available.
- Current process evidence, configuration screenshots/exports, app and role evidence, master-data examples, integration contracts, report definitions, or issue logs.
- Target outcome, business constraints, controls, cutover timing, and reviewer/owner.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to make a fit-gap recommendation now.
2. Required local evidence: missing edition, release, scope, configuration, role, data, integration, report, or approval inputs.
3. Source scope: official SAP source categories checked and the user-provided tenant evidence used.
4. Fit-gap table: requirement, current evidence, SAP-standard option, customer-specific gap, risk, owner, and next validation step.
5. Action boundary: changes, postings, approvals, migrations, integrations, exports, and security decisions that require explicit confirmation and authorized access.
6. Source note: official SAP source categories, local evidence, assumptions, and missing verification.

## Confirmation Boundary

Do not change SAP configuration, roles, transports, master data, workflows, integrations, APIs, extensions, reports, postings, approvals, exports, uploads, migrations, or production schedules without explicit user confirmation and authorized tool access.
