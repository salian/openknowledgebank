---
type: Evaluation
title: Test Suite / Test Plan Quality Check
description: Reviewer rubric for source discipline, traceability, test design, evidence integrity, safety, and completion reporting.
okb_bundle_id: test-suite
evaluation_method: reviewer rubric
score_scale: 0-2 per criterion
maximum_score: 16
resource: https://www.iso.org/standard/79428.html
timestamp: '2026-08-07T00:00:00Z'
---

# Test Suite / Test Plan Quality Check

Score each criterion `0` absent or unsafe, `1` partial, or `2` complete and evidence-backed.

1. **Test basis and source discipline:** identifies the product version, requirements, risks, acceptance criteria, and current external references without inventing local facts.
2. **Scope and planning:** states objectives, covered and excluded areas, levels and types, constraints, dependencies, roles, criteria, and reporting expectations.
3. **Traceability:** links requirements and risks to tests and makes orphaned, duplicate, or uncovered items visible.
4. **Test design quality:** provides reviewable preconditions, data, steps or oracle, expected results, priorities, and risk-relevant positive and negative scenarios.
5. **Environment and data integrity:** identifies build, configuration, interfaces, permissions, data state, privacy controls, reset needs, and authorization gaps.
6. **Result and evidence integrity:** separates planned, implemented, executed, blocked, passed, failed, waived, rerun, and accepted states; actual results and evidence are never fabricated.
7. **Coverage and completion honesty:** makes calculations reproducible and distinguishes test completion, residual risk, user acceptance, approval, and release readiness.
8. **Safety and usability:** is actionable for an authorized reviewer while containing no credentials, execution affordances, destructive steps, or unsafe assumptions.

## Blocking Defects

Regardless of score, block an authoritative quality or readiness claim when the package invents execution evidence, alters expected results to match observations, reports unsupported coverage, treats untested work as passed, or claims acceptance, approval, or release without evidence.

## Evaluation Status

This rubric has not been used in a reviewed baseline-versus-bundle benchmark. No measured score or performance improvement is claimed.
