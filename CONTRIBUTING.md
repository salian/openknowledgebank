# Contributing

OpenKnowledgeBank accepts contributions that improve bundle quality, add useful role knowledge, or help validate and distribute bundles.

## Contribution Areas

- Improve existing bundle concepts.
- Add new role, industry, or capability bundles.
- Add references and examples.
- Improve registry metadata.
- Improve validation tooling.
- Submit external OpenKnowledge-style repositories for listing.

## Contributor Credit

OpenKnowledgeBank should give visible credit to contributors.

Future bundle metadata may include creators, maintainers, contributors, reviewers, source researchers, and editors. Contributor profile pages may be generated from public registry metadata.

Do not include private contact details or personal information that a contributor has not intentionally made public.

## Bundle Requirements

- Use markdown files with YAML frontmatter.
- Include a required `type` field in frontmatter.
- Include `index.md` as the bundle entry point.
- Include `log.md` for material changes.
- Credit sources where source material influenced the bundle.
- Keep content practical, role-specific, and agent-usable.
- Do not include secrets, credentials, private notes, personal data, or source material that cannot be publicly redistributed.

## Agent Affordances

Bundles may include optional directories for agent actions and outputs:

- `frameworks/`
- `tools/`
- `workflows/`
- `deliverables/`
- `commands/`
- `skills/`
- `evaluations/`

Tool guides and commands must include safety boundaries. They must not instruct agents to modify live systems, send messages, spend money, export data, or perform other risky actions without explicit user confirmation.

## Trust Tiers

OpenKnowledgeBank uses trust tiers for bundles and external resources:

- `trusted`: reviewed and maintained in this repository.
- `community`: external repository or contribution that has passed basic review.
- `unverified`: submitted or discovered resource that has not been reviewed.
- `rejected`: unsafe, spam, malicious, noncompliant, or unsuitable.

`trusted` does not mean guaranteed safe for every use case. It means reviewed and maintained by OpenKnowledgeBank.

## Safety Review

Do not submit bundles that include:

- hidden or deceptive instructions
- instructions to bypass system, developer, model, or application policies
- credential or secret exfiltration behavior
- phishing, spam, malware, fraud, or abuse workflows
- private or personal data
- copied copyrighted content without permission
- undisclosed external runtime dependencies
- unsafe regulated advice without careful scoping

## Improvement Contributions

If an agent or user identifies a bundle weakness, propose improvements through a reviewed contribution.

Do not submit private user context, secrets, credentials, personal data, or confidential examples. User corrections should be generalized and reviewed before becoming public bundle content.

Good improvement PRs explain:

- what failed or was missing
- why the improvement is generally useful
- what files changed
- what sources or rationale support the change
- any safety or licensing considerations

## Attribution

By contributing, you agree that non-code content is available under CC BY 4.0 and code/tooling is available under MIT.
