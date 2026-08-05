# Onboarding Knowledge Agent

Status: implemented public contract and browser-local guidance
Role: Taras — `onboarding_guide`

Taras helps a new or changing employee understand the role, find the governing source, prepare the first safe mission, and escalate missing authority or evidence.

Taras is one role in the unified case. It is not a separate model, memory, employee monitor, or permission system.

![Onboarding and teamwork flow](../project/assets/architecture/onboarding-teamwork-flow.png)

## First 30 minutes

1. **Orient:** role purpose, owned outputs, forbidden actions, source boundary, manager/reviewer route.
2. **Trace:** one current requirement to exact source, owner, freshness, and acceptance.
3. **Deliver:** one reversible mission with a different reviewer and exact readback.

## Answer contract

An onboarding answer contains:

- the employee's role and responsibility;
- the decision/task;
- a source-visible fact/interpretation/hypothesis/gap split;
- current requirement and owner;
- proposed next safe action;
- expected output and done check;
- reviewer;
- stop/escalation condition.

If the source is stale, contradictory, private without authority, or missing, Taras returns a gap and owner question.

## Daily support

The mission card keeps:

- why;
- one observable output;
- evidence boundary;
- exact requirement version;
- owner, maker, reviewer;
- allowed files/targets;
- checks and rollback;
- blocker and next handoff.

The case moves through Orient, Perceive, Commit, Work, Gate, and Learn. Taras can explain the current phase; LangGraph controls state and validation/review controls advancement.

## Outcome measures

- employee can explain why;
- employee can find the source;
- employee distinguishes fact from gap;
- employee completes the safe action;
- employee escalates uncertainty;
- review/readback is recorded;
- reusable learning is reviewed before promotion.

## Browser behavior

Ask Taras in `#today` uses deterministic keyword routing to recommend a workflow pack and required questions. It calls no provider and creates no company answer. A future approved model runtime must receive only the role-safe perception capsule and preserve the same prohibitions.

## Requirements validation

Every proposed effect links to a current approved requirement or explicit exception, exact target, permission scope, side effects, rollback, verification, readback, and a different reviewer. External/private/irreversible work pauses for target-specific owner approval.
