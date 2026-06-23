# Bundle Creation Process

This is the public process for creating OpenKnowledgeBank bundles.

## 1. Choose a Bundle Topic or Role

Start with a specific bundle topic or agentic role.

Good bundle candidates have clear boundaries, repeatable workflows or checks, recognizable deliverables, and enough public source material to build from.

Bundles can represent roles, industries, capabilities, tools, frameworks, compliance regimes, jurisdictions, deliverables, or datasets.

Do not force a non-role topic into a role. For example, AVETMISS should usually be modeled as `compliance/avetmiss-compliance`, while `vet-compliance-officer` can be a separate role bundle that links to it.

## 2. Research the Bundle

Research how the bundle topic works in practice:

- responsibilities
- workflows
- tools
- frameworks
- metrics
- deliverables
- examples
- common mistakes
- references

Use public, reputable, and sourceable material. Do not copy proprietary content or private material into a bundle.

## 3. Design the Bundle

Every bundle should include:

- `index.md`
- `log.md`
- a category-specific core file, such as `role.md`, `overview.md`, `tool.md`, `framework.md`, `deliverable.md`, `jurisdiction.md`, or `dataset.md`

Useful folders include:

- `responsibilities/`
- `workflows/`
- `playbooks/`
- `metrics/`
- `tools/`
- `frameworks/`
- `deliverables/`
- `commands/`
- `examples/`
- `references/`
- `evaluations/`

## 4. Write Agent-Usable Content

Bundle content should help an LLM agent perform the role, apply the rule, use the tool, follow the framework, create the deliverable, or understand the dataset.

Prefer practical, specific, category-aware guidance over generic advice.

Every concept file should use markdown with YAML frontmatter and include a `type` field.

See `docs/BUNDLE_SCHEMA.md` for the current working canonical schema.

## 5. Add Safety Boundaries

Commands, tools, and workflows should not instruct agents to bypass policies, hide behavior, exfiltrate data, spam users, or modify live systems without confirmation.

Do not include secrets, credentials, private data, or source material that cannot be publicly redistributed.

## 6. Add Examples and Evaluations

Strong bundles include examples and checks that help users judge output quality.

Examples may include:

- sample briefs
- reports
- plans
- checklists
- quality rubrics
- before/after agent outputs

## 7. Update Metadata

Add or update the bundle entry in:

```text
registry/bundles.json
```

Include the bundle path, status, license, trust tier, version, and relevant metadata.

## 8. Submit

Open a pull request with:

- bundle files
- registry update
- source references
- explanation of what the bundle enables
- notes about safety or licensing concerns

Maintainers will review structure, usefulness, source quality, metadata, and safety.

## 9. Validate

Run the validator before submitting:

```bash
python tools/validate-bundle/validate.py --root .
```

The validator checks registry metadata, required bundle files, markdown frontmatter, internal links, and obvious public-safety issues such as secrets or private workspace paths.

Validation passing does not mean the bundle is expert-approved or suitable for every use case. It means the contribution passes the baseline repository quality gate.
