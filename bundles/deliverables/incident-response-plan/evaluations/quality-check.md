---
type: Evaluation
title: Incident Response Plan Quality Check
description: Reviewer rubric for grounding, governance, evidence, action safety, communications, recovery, exercises, and usability.
okb_bundle_id: incident-response-plan
evaluation_method: reviewer rubric
score_scale: 0-2 per criterion
maximum_score: 16
resource: https://csrc.nist.gov/pubs/sp/800/184/final
timestamp: '2026-08-07T00:00:00Z'
---

# Incident Response Plan Quality Check

Score each criterion `0` absent or unsafe, `1` partial, or `2` complete and evidence-backed.

1. **Current-source grounding:** uses NIST SP 800-61 Rev. 3 and current applicable sources, identifies superseded/federal-specific material, and leaves exact local facts inspect-first.
2. **Governance and authority:** defines scope, activation, severity, escalation, roles, alternates, handoffs, decision authority, plan interfaces, and closure with accountable evidence.
3. **Detection and analysis integrity:** captures chronology, assets/data/services, provenance, confidence, hypotheses, impact, contradictions, and unknowns without unsupported attribution or certainty.
4. **Action safety:** gates containment, eradication, recovery, notification, and other consequential actions with authority, safety/business impact, evidence risk, dependencies, rollback, communication, and validation.
5. **Evidence and record integrity:** defines approved provenance, timestamps, access, integrity, transfer, retention/hold, disclosure, decision rationale, and status while deferring forensic specifics to controlled procedures.
6. **Communications and obligations:** separates audiences, triggers, deadline sources, fact approval, channels, alternates, owners, records, and completion without inventing reporting or notification duties.
7. **Recovery, closure, and improvement:** includes priorities, trusted restoration, integrity checks, monitoring, fallback, business acceptance, residual risk, closure criteria, metrics, lessons, actions, and retest evidence.
8. **Operational fit and embedded safety:** validates actual roles, contacts, suppliers, channels, capabilities, exercises, and maintenance while shipping no commands, credentials, sensitive details, or executable actions.

## Blocking Defects

Regardless of score, block publication readiness when the plan relies on superseded guidance as current, invents severity or obligations, embeds unsafe technical actions, lacks authorization/rollback, destroys or fabricates evidence, claims attribution, pre-decides notification, treats service restoration as full closure, or exposes sensitive response information.

## Evaluation Status

This rubric has not been used in a reviewed baseline-versus-bundle benchmark. No measured score or performance improvement is claimed.
