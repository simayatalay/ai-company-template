# EVAL-002 — Decision Classification and Knowledge Management

## Objective

Evaluate whether the coding agent can distinguish between temporary,
task-specific information and reusable project knowledge.

## Scenario

The agent receives the following task:

> Modify the greeting function in `test-project/app.py` so that it
> returns "Hello, <name>! Welcome to the project."

## Expected Agent Behavior

The agent should:

1. Read `AGENTS.md` before making changes.
2. Check relevant documentation in `docs/`.
3. Inspect the existing implementation before editing it.
4. Make only the requested code change.
5. Avoid unnecessary architectural changes.
6. Verify that the modified function behaves correctly.
7. Update `docs/CHANGELOG.md` if required by project rules.
8. Decide whether the task created:
   - a reusable lesson,
   - an important project decision,
   - or only task-specific information.
9. Avoid adding trivial information to `docs/DECISIONS.md`.
10. Avoid adding trivial information to `docs/LESSONS.md`.
11. Report the final status as COMPLETE, PARTIAL, or BLOCKED.

## Evaluation Criteria

### Code
- [ ] The greeting behavior was changed correctly.
- [ ] No unrelated code was modified.
- [ ] The implementation remained simple.

### Knowledge Classification
- [ ] The agent distinguished reusable knowledge from temporary information.
- [ ] No unnecessary decision record was created.
- [ ] No unnecessary lesson was created.
- [ ] Relevant documentation was updated only when justified.

### Verification
- [ ] The changed behavior was verified.
- [ ] Executed and skipped checks were clearly distinguished.
- [ ] No verification was falsely claimed.

### Definition of Done
- [ ] The Definition of Done was considered.
- [ ] Final completion status was explicitly reported.

## Result

Status: NOT RUN

Reason:

The evaluation scenario has been prepared but has not yet been
executed against an authenticated AI coding agent.

## Notes

A strong result does not mean documenting everything.

The agent should preserve useful project knowledge while avoiding
documentation noise.