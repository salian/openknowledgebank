---
type: Tool Guide
title: Canvas
description: Defines source-aware Canvas LMS course, content, assessment, integration, permission, and data review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Canvas LMS change brief with explicit evidence states.
confirmation_required:
- publish or change course content, enroll users, alter grades or dates, send messages, import SIS data, install an integration, or access student records
okb_bundle_id: canvas-instructure
timestamp: '2026-07-31T00:00:00Z'
---
# Canvas

Source-aware tool bundle for Canvas LMS course, content, assessment, integration, permission, and data review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://www.instructure.com/canvas
- https://canvas.instructure.com/doc/api/index.html

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- Canvas instance, environment, release, account, subaccount, course, term, section, and object IDs
- user, role, enrollment, permissions, OAuth scopes, developer key, LTI or SIS integration
- content, module, assignment, rubric, quiz, dates, gradebook, files, accessibility, privacy, audit, backup, test, and approval evidence

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer course state, permission, enrollment, grade, due date, content visibility, integration behavior, accessibility, or student outcome.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that publish or change course content, enroll users, alter grades or dates, send messages, import SIS data, install an integration, or access student records.
