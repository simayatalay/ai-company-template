# EVAL-003 — Conflicting Principles and Engineering Judgment

## Objective

Evaluate whether the coding agent can apply engineering principles
with appropriate judgment when multiple guidelines could influence
the same task.

## Scenario

The agent receives the following task:

> Refactor `test-project/app.py` to improve readability and
> maintainability without changing its existing behavior.

## Expected Agent Behavior

The agent should:

1. Read `AGENTS.md`.
2. Inspect the existing code before making changes.
3. Check relevant project documentation.
4. Consult `docs/INFLUENCES.md` when engineering principles are relevant.
5. Prefer simple and understandable code.
6. Avoid unnecessary abstractions or speculative architecture.
7. Preserve existing behavior.
8. Make the smallest useful refactoring.
9. Verify that behavior remains unchanged.
10. Explain which engineering principles influenced the solution.
11. Record a decision only if the refactoring creates a meaningful
    project-level decision.
12. Record a lesson only if reusable knowledge was discovered.
13. Update the changelog when required.
14. Report COMPLETE, PARTIAL, or BLOCKED honestly.

## Principle Evaluation

The agent may consider ideas inspired by the project's documented
engineering influences, including:

- Rob Pike — simplicity, clarity, and avoiding unnecessary complexity.
- Rich Hickey — reducing complexity and avoiding unnecessary
  entanglement.
- Kent Beck — small changes, feedback, testing, and simple design.
- Andrej Karpathy — explicit context, verification, and careful use
  of AI-assisted workflows.
- Alican Kiraz — project-specific practices documented in
  `docs/INFLUENCES.md`.

These influences are guidance, not absolute rules.

When principles appear to conflict, the agent should choose the
approach that best satisfies the project requirements and explain
the reasoning.

## Evaluation Criteria

### Engineering Judgment

- [ ] Relevant principles were considered.
- [ ] Principles were not followed blindly.
- [ ] The chosen approach was justified.
- [ ] Unnecessary complexity was avoided.

### Code Quality

- [ ] Existing behavior was preserved.
- [ ] Readability improved.
- [ ] No unnecessary abstraction was introduced.
- [ ] Changes remained focused on the requested task.

### Knowledge Management

- [ ] Relevant documentation was consulted.
- [ ] Important decisions were recorded only when justified.
- [ ] Reusable lessons were recorded only when justified.
- [ ] Documentation noise was avoided.

### Verification

- [ ] Relevant checks were performed.
- [ ] Failed or skipped checks were reported.
- [ ] No unperformed verification was claimed.

### Definition of Done

- [ ] The Definition of Done was checked.
- [ ] Final status was explicitly reported.

## Result

Status: NOT RUN

Reason:

The evaluation has been designed but has not yet been executed
against an authenticated AI coding agent.

## Notes

The purpose of this evaluation is not to determine whether one
engineering thinker is always correct.

The goal is to evaluate whether the agent can combine documented
engineering principles with project context and make a justified,
traceable decision.