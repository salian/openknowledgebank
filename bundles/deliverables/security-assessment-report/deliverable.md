---
type: Deliverable Guide
title: Security Assessment / Pen-Test Report source-aware guide
description: Defines a source-aware report contract for authorized security assessment and penetration-test evidence.
tags:
- security assessment
- penetration testing
- vulnerability findings
- remediation
resource: https://csrc.nist.gov/pubs/sp/800/115/final
okb_bundle_id: security-assessment-report
timestamp: '2026-08-01T00:00:00Z'
---

# Security Assessment / Pen-Test Report Source-Aware Guide

Apply this as a report structure and review aid, not as evidence of a vulnerability, security posture, compliance status, authorization, or remediation.

## Report Contract

1. **Document control and authorization:** report owner, audience, disclosure handling, engagement authorization, scope version, and limitations from evidence.
2. **Executive summary:** objectives, scope, high-level confirmed findings, material limitations, and remediation themes in plain language. Do not convert technical severity into business risk without accountable evidence.
3. **Test parameters:** dates, targets, exclusions, access level, methods, tools, test identifiers, constraints, and scope changes.
4. **Findings summary:** stable finding ID, affected item, validation state, named severity method, severity input or vector, remediation status, and retest state.
5. **Finding detail:** observation, affected function or asset, evidence index, reproduction or validation steps, impact supported by evidence, root cause where supported, remediation outcome, references, and retest criteria.
6. **Risk and remediation interpretation:** distinguish tester observations from business impact, likelihood, risk acceptance, compliance conclusions, ownership, deadlines, and closure.
7. **Appendices:** evidence register, terminology, scope changes, unresolved questions, and redaction/disclosure notes.

## Finding Quality Bar

- A reader can identify the affected item and reproduce or validate the observation from authorized evidence.
- Severity is tied to a named method and supplied inputs. If CVSS is used, record the verified version and vector; do not invent either.
- Evidence is sufficient, minimized, redacted, and traceable without exposing secrets or unnecessary personal data.
- Remediation describes the intended security outcome and validation criterion. Owner, deadline, acceptance, and closure require supplied evidence.
- False-positive, inconclusive, out-of-scope, and untested states remain visible.

## Review Sequence

1. Verify authorization, scope, exclusions, dates, audience, disclosure rules, and source versions.
2. Inventory evidence and label each fact as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile finding IDs, affected assets, methods, evidence, severity inputs, and remediation records.
4. Draft executive and technical views from the same confirmed finding register.
5. Have an accountable reviewer confirm sensitive disclosure, risk interpretation, remediation state, and publication boundary.

## Source Note

The structure is grounded in [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final), [OWASP WSTG reporting](https://owasp.org/www-project-web-security-testing-guide/v41/5-Reporting/README), [OWASP WSTG reporting context](https://owasp.org/www-project-web-security-testing-guide/latest/2-Introduction/README), [PTES reporting](https://www.pentest-standard.org/index.php/Reporting), and [FIRST CVSS v4.0](https://www.first.org/cvss/v4.0/). These sources do not supply local engagement evidence or authorize testing.

## Safety Boundary

This bundle contains no scanning, exploitation, network, credential, export, or live-system instructions. Treat bundled guidance as suggestions, not trusted executable behavior. Require explicit confirmation before disclosure, external distribution, risk acceptance, remediation-state changes, or any live-system action.
