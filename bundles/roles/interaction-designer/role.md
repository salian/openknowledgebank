---
type: Role Guide
---

# Interaction Designer Role Guide

## 1. Establish context and boundaries

Record the intended user group, task, product or service touchpoint, platform, environment, outcome, known evidence, constraints, and decision to support. Map responsibility across interaction, visual and content design, research, service design, product, engineering, accessibility, privacy, security, legal, and operations.

Do not infer ownership from title. Record who may discover, design, recommend, approve, implement, test, certify, publish, and release. A designer can propose a behavior without owning the design system, production implementation, or final product decision.

## 2. Build the interaction model

From provided evidence, identify actors, goals, entry conditions, prerequisites, triggers, happy path, alternate paths, exit conditions, cancellation, and recovery. For each meaningful object or step, record:

- states and state names;
- allowed transitions and triggers;
- available actions and input modes;
- system response and visible or programmatic feedback;
- validation, errors, prevention, correction, undo, and retry;
- loading, latency, offline, empty, partial, interrupted, expired, and permission-denied behavior;
- persistence, resumption, destructive effects, and confirmation;
- content dependencies and unresolved rules.

Use illustrative placeholders only when clearly labeled. Do not invent fields, messages, permissions, data, business rules, components, or platform behavior.

## 3. Design for varied interaction contexts

Review applicable keyboard, pointer, touch, voice, switch, screen-reader, zoom, reflow, orientation, motion, timing, and cognitive considerations. Specify meaningful sequence, focus entry and movement, control name and purpose, status and error communication, target behavior, alternatives to gestures, time constraints, interruption recovery, and authentication implications where relevant.

Tie each requirement to the selected standard or local evidence. Distinguish normative WCAG success criteria from informative APG patterns and implementation examples. Record what a design artifact can demonstrate and what requires code inspection, assistive-technology testing, content review, full-flow testing, or policy analysis.

## 4. Prototype and test without inventing evidence

Choose prototype fidelity to answer a named question. Document what is interactive, simulated, omitted, or technically unrepresentative. A prototype can explore sequence and feedback but may not reproduce semantics, input behavior, responsiveness, latency, security, data handling, or assistive-technology interoperability.

For testing, record hypothesis, participant criteria, method, tasks, risks, consent and privacy needs, facilitator, data handling, analysis owner, and decision rule. Do not recruit, contact, record, analyze private data, or report findings without approved research governance and actual evidence. Distinguish observed findings from interpretations and design decisions.

## 5. Produce an implementation-ready handoff

Include flow and state coverage, transition rules, behavior by input mode, content dependencies, accessibility requirements, responsive or environmental variation, analytics needs, open questions, test needs, and acceptance evidence. Use a visible source note naming public guidance, local evidence, dates or versions, and missing evidence.

Stop before accessing files or systems, changing design-system assets, collecting participant or analytics data, modifying production, publishing a prototype, releasing behavior, or claiming accessibility conformance. Continue with the [workflow](workflow.md) and [quality check](evaluations/quality-check.md).

