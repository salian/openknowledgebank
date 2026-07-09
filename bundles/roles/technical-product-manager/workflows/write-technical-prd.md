---
type: Workflow
title: Write Technical PRD
description: Turns product and engineering evidence into a technical product requirements document.
tags: [prd, requirements, feasibility]
okb_bundle_id: technical-product-manager
timestamp: 2026-07-09T00:00:00Z
---

# Write Technical PRD

Use this workflow when the user needs a technical PRD or a review of whether a feature request is ready for engineering.

## Inputs

- User/business problem and target users.
- Customer evidence, support examples, research notes, or analytics context.
- Product scope, non-goals, constraints, and decision owner.
- Technical source evidence: architecture notes, API specs, data contracts, tickets, designs, repos, logs, incidents, service owners, or engineering notes.
- Measurement source evidence: metric definitions, dashboards, queries, time windows, filters, identity logic, and refresh cadence.

## Steps

1. State the product decision being supported.
2. Classify evidence as verified source fact, user-provided evidence, assumption for this draft, or missing verification.
3. Define product scope, non-goals, user impact, and business goal.
4. Identify technical surfaces affected: APIs, services, data, permissions, integrations, UI states, observability, migration, support, and rollout.
5. Convert requirements into acceptance criteria that can be verified.
6. Add dependency, risk, privacy/security/accessibility/compliance, support, and launch-readiness questions.
7. End with a source note and the next evidence needed before implementation commitment.

## Output Contract

- Direct recommendation or readiness status.
- Source note.
- Problem, users, goal, scope, and non-goals.
- Verified facts, user-provided evidence, assumptions, and missing verification.
- Requirements and acceptance criteria.
- Technical surfaces and dependencies.
- Risks, mitigations, rollout, observability, and rollback questions.
- Decision points and required owner confirmations.

Do not invent local endpoints, fields, services, event names, effort estimates, roadmap dates, or approvals. Ask for source evidence instead.
