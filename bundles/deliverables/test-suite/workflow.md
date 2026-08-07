---
type: Workflow
title: Test Planning and Review Workflow
description: A source-aware sequence for turning requirements and risks into traceable testware and evidence-backed status reporting.
okb_bundle_id: test-suite
inputs:
- test basis and change scope
- product and quality risks
- environment, data, and authorization constraints
- execution and defect evidence when reporting results
outputs:
- reviewed test plan
- traceable test suite
- evidence-backed test status and completion assessment
resource: https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf
timestamp: '2026-08-07T00:00:00Z'
---

# Test Planning and Review Workflow

1. **Inspect the test basis.** Identify the product and version, requirements, designs, interfaces, changes, risks, acceptance criteria, applicable policies, and evidence gaps. Do not infer absent requirements.
2. **Set objectives and scope.** Define test levels and types, covered and excluded areas, assumptions, constraints, dependencies, and explicit authorization boundaries.
3. **Plan the approach.** Record roles, environments, data, sequencing, priorities, entry and exit criteria, suspension and resumption criteria, evidence expectations, defect handling, and reporting cadence.
4. **Build traceability.** Map requirements and risks to planned tests. Review orphan requirements, unmitigated risks, duplicate cases, and tests with no justified source.
5. **Design test cases.** Specify preconditions, data, steps or test oracle, expected results, priorities, and rationale. Include negative, boundary, state, permission, failure, recovery, and change-focused scenarios when supported by risk.
6. **Implement testware.** Organize cases into suites, establish required data and environment states, and identify automation candidates. Keep implementation readiness separate from execution status.
7. **Verify readiness.** Confirm the version, configuration, interfaces, accounts, permissions, data handling, reset path, observability, evidence capture, and authorization before any execution by an accountable operator.
8. **Capture execution evidence.** When supplied, record actual results, status, evidence, defects, blockers, timestamps, and reruns without altering the pre-established expected result to force agreement.
9. **Review coverage and defects.** Reconcile tests against requirements and risks, distinguish untested from passed, and make coverage calculations reproducible.
10. **Assess completion.** Compare evidence with stated criteria, report open defects and residual risk, and keep test completion, user acceptance, approval, and release decisions distinct.

## Review Questions

- Is the exact product version and test basis known?
- Does every material test have a requirement, risk, criterion, change, or justified exploratory objective?
- Are expected and actual results independently visible?
- Are environment, data, authorization, evidence, and reset requirements complete?
- Can every coverage number be reproduced from defined inputs?
- Are blocked, waived, failed, untested, accepted, approved, and released states kept distinct?

## Source Discipline

Verify current source editions before relying on exact process or terminology claims. The workflow is an original synthesis informed by ISO/IEC/IEEE 29119 and ISTQB; it is not a reproduction of a standard, certification syllabus, or organization-specific procedure.
