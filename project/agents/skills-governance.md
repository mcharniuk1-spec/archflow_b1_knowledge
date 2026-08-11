# Skills Governance

The public tool admits ten portable packages. Each package is a reusable instruction contract under `skills/`; it is not a running agent, provider, credential, permission grant, or proof of execution.

## Admitted packages

`arcagcom`, `archflow-agent-control`, `archflow-architecture-operator`, `archflow-e1-runtime-guard`, `archflow-knowledge-service`, `archflow-task-breakdown`, `humanize-writing`, `outquestions`, `priority-task-operator`, and `task-handout`.

The canonical role-to-package allowlist lives in `project/system/contracts/role-catalog.json`. `agent-roster.yaml` and `skills-by-agent.md` are projections and must match it exactly.

## Package admission

A package is admitted only when all of these are true:

1. Its folder name and frontmatter `name` are identical, lowercase, and unique.
2. Frontmatter contains only `name` and a trigger-oriented `description`.
3. The body accepts caller-supplied approved inputs and names its source boundary.
4. Local files go only to an ignored `project/local/` path, or the result is returned through the dashboard Communication Center.
5. Forbidden effects, stop conditions, evidence requirements, and reviewer route are explicit.
6. It has no credential value, provider or external-action activation, independent authority, hidden personal context, or dependency on excluded workspace archives.
7. Bundled scripts and references are required for the skill's work and pass focused validation.

## Methods versus packages

A plain capability phrase is a method unless it resolves to one of the ten admitted package IDs. Methods can describe techniques such as source verification, contradiction checks, task splitting, accessibility inspection, rollback design, or claim calibration. Listing a method does not claim installation, execution, or new authority.

Do not create a package because a method appears once. Add one only when repeated tasks show a reusable gap, no admitted package covers it, its smallest permission set is known, and an independent reviewer can validate the behavior. Update the canonical role catalog and both projections in the same bounded change.

## Runtime and authority boundary

- The case supplies the goal, approved inputs, source boundary, exact targets, approvals, budget, and stop conditions.
- A role receives only the packages listed in its canonical contract.
- Provider calls are disabled unless a separate server-side provider gate is approved and proved.
- External writes, publication, deployment, Git actions, and durable knowledge promotion require their own exact approval and post-action readback.
- A maker never approves its own high-risk output. Reviewers inspect a frozen candidate and do not silently repair it.
- Secrets and personal inputs stay outside the repository and outside exported packets.

## Output and deactivation

Portable skills return a reviewable artifact, not a completion claim. Store optional local artifacts under `project/local/<case-id>/` or pass the packet through the Communication Center. Record source paths, assumptions, checks, gaps, reviewer, and next safe action.

Deactivate a package for a case when its input boundary is unclear, required evidence is missing, its assigned role is outside the allowlist, it requests a forbidden effect, or the same failed repair repeats twice. Keep the case blocked until the caller narrows the input or grants the separate authority explicitly.

## Validation

After a package or mapping change, parse every skill frontmatter block, validate every `agents/openai.yaml`, resolve all relative links, compare the ten package IDs with the local skill folders, and compare role IDs, titles, lanes, and package lists with the canonical role catalog. Then run the public safety scan before release.
