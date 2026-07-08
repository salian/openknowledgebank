---
type: Workflow
title: Review Sales Automation and Outreach
description: "Review HubSpot Sales Hub sequences, workflows, tasks, playbooks, and outreach automation before changing live behavior."
okb_bundle_id: hubspot-sales-hub
timestamp: "2026-07-09T00:00:00Z"
---

# Review Sales Automation and Outreach

## Purpose

Evaluate a proposed sequence, workflow, task automation, playbook, lead rotation, meeting, notification, integration, quote/payment, or API-connected action before it affects contacts, customers, reps, CRM data, or external systems.

## Evidence to Inspect First

- Current official HubSpot source category for the feature being changed.
- Existing active and draft sequence, workflow, playbook, report, integration, and permission definitions from the user's portal.
- Enrollment criteria, suppression/exclusion logic, object/property dependencies, owner/team context, permissions, email/domain settings, consent status, unsubscribe behavior, and downstream side effects.
- Test records, sandbox or limited rollout evidence, owner approvals, deployment plan, and rollback plan.
- Privacy, consent, deliverability, security, compliance, retention, and customer communication policy where personal data or outreach is involved.

## Output Shape

1. Source note.
2. Readiness answer: ready, ready with gaps, or not ready.
3. Dependency map: objects, properties, owners, teams, lists, records, permissions, reports, integrations, and automations touched.
4. Risk review: accidental outreach, duplicate automation, conflicting workflow/sequence behavior, bulk updates, data exposure, deliverability, unsubscribe/consent, customer impact, reporting impact, and integration side effects.
5. Test plan: sample records, expected outcomes, negative cases, suppression checks, report checks, permission checks, and monitoring.
6. Deployment plan: approver, change window, limited rollout, communication plan, backup/export evidence, activation steps, and rollback steps.
7. Confirmation boundary: actions that require explicit approval before execution.

## Safety Boundary

Sales automation and outreach changes are risky. Treat recommendations as review material until an authorized HubSpot owner confirms the change, verifies the source evidence, completes consent/deliverability review where needed, and approves execution.
