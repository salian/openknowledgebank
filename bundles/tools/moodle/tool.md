---
type: Tool Guide
title: Moodle
description: Defines source-aware Moodle course, role, plugin, integration, assessment, and data administration review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Moodle change brief with explicit evidence states.
confirmation_required:
- enroll or message users, change grades or course content, enable web services, issue tokens, install plugins, run upgrades, restore backups, or expose learner data
okb_bundle_id: moodle
timestamp: '2026-07-31T00:00:00Z'
---
# Moodle

Source-aware tool bundle for Moodle course, role, plugin, integration, assessment, and data administration review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://moodledev.io/docs/5.1/apis
- https://docs.moodle.org/dev/Web_services

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- site and Moodle version, environment, course, category, cohort, user, role, and capability
- plugins, themes, dependencies, activities, resources, questions, grades, dates, enrollment, completion, web-service functions and tokens, privacy, retention, backup, restore, logs, tests, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer capability, enrollment, grade, completion, plugin compatibility, course visibility, integration behavior, or learner outcome.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that enroll or message users, change grades or course content, enable web services, issue tokens, install plugins, run upgrades, restore backups, or expose learner data.
