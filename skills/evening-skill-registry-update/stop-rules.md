# Evening Skill Update Stop Rules

These rules apply to the post-execution skill update review inside the existing evening skill and hook lane.

## Loop Control

- Maximum 3 repair attempts per task.
- Stop if the same error appears twice.
- Stop if the next step is not justified by evidence.
- Stop if required credentials, production permissions, or owner decisions are missing.
- Stop when acceptance criteria are met.
- Do not continue simply because more improvement is possible.
- Do not change unrelated architecture during repair.
- Do not mutate controlling prompts without evidence.

## Skill Update Control

- Choose `NO_UPDATE` when evidence is ordinary, one-off, private-source-dependent, weakly validated, or not reusable.
- Choose `APPEND_PATTERN` only when a completed run proves a reusable method, failure pattern, or efficient sequence.
- Choose `PATCH_EXISTING_SKILL` only when the run proves a clear improvement to an existing skill, subprompt, task template, stop rule, verification rule, or repair rule.
- Do not create a new skill automatically.
- If no matching skill exists, store candidate material here under `candidate-patterns.md` for later review.
- Keep every update append-only unless a human explicitly asks for a targeted rewrite.

## Evidence Requirement

Every update must cite at least one concrete evidence type:

- test, build, lint, parse, smoke, or safety output;
- changed file list;
- diff summary;
- failed command or repeated error;
- successful command;
- before or after behavior from the run note;
- public-safe execution log excerpt.
