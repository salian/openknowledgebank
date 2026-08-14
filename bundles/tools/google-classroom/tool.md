---
type: "Tool Guide"
title: "Google Classroom"
description: "Source-aware guidance for Google Classroom."
resource: "https://edu.google.com/workspace-for-education/products/classroom/"
okb_bundle_id: google-classroom
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Learning, classwork, assessment, and education administration platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create classes, enroll or remove users, publish assignments, return submissions, change grades, contact guardians, run originality checks, connect an SIS, export student data, or represent learning outcomes"
---
# Google Classroom Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://edu.google.com/workspace-for-education/products/classroom/
- https://developers.google.com/workspace/classroom

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Google for Education and Classroom developer documentation for the tenant and edition.
- Class, roster, role, assignment, submission, rubric, grade, guardian, originality, integration, and audit state.
- Student privacy, content rights, accessibility, assessment policy, validation, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Google Classroom configuration and learning workflow review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create classes, enroll or remove users, publish assignments, return submissions, change grades, contact guardians, run originality checks, connect an SIS, export student data, or represent learning outcomes.

## Guardrails

- Do not invent student identity, enrollment, authorship, submission state, grade, feedback delivery, originality finding, accessibility, completion, qualification, consent, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
