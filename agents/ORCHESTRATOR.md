# Orchestrator

## Purpose

Coordinate the software task across specialized agents in a controlled sequence.

## Workflow

1. Read `AGENTS.md`.
2. Read the task description and relevant project context.
3. Create or link the task to an issue or ticket when required.
4. Start the Coding Agent.
5. If coding status is `IMPLEMENTED`, run required verification and testing.
6. If testing status is `PASS`, start the Code Review Agent.
7. If review decision is `APPROVE`, start the Git Agent.
8. Update the issue or ticket with progress and evidence.
9. Close the issue only when all required stages are complete.
10. If any stage returns `FAIL`, `BLOCKED`, or `REQUEST CHANGES`, stop or route the task back to the appropriate previous stage.

## Routing Rules

### Coding Agent

Expected result:

- IMPLEMENTED
- BLOCKED

If `BLOCKED`:
- Stop the workflow.
- Record the blocker.

### Test Agent

Expected result:

- PASS
- FAIL
- BLOCKED

If `FAIL`:
- Return the task to the Coding Agent.

If `BLOCKED`:
- Stop the workflow.

### Code Review Agent

Expected result:

- APPROVE
- REQUEST CHANGES
- BLOCKED

If `REQUEST CHANGES`:
- Return the task to the Coding Agent.
- Run testing again after the new implementation.

If `BLOCKED`:
- Stop the workflow.

### Git Agent

Run only when:

- Coding is complete.
- Tests passed.
- Code review returned `APPROVE`.

Expected result:

- COMPLETE
- FAILED
- BLOCKED

## Safety Rules

- Never skip testing.
- Never skip code review.
- Never allow Git operations before approval.
- Never close an issue when the workflow is incomplete.
- Preserve the output of each stage for traceability.
- Re-run relevant verification after implementation changes.
- Do not assume one testing method is sufficient for every project; use the verification methods required by the target environment.

## Final Status

The orchestrator must finish with exactly one of:

- COMPLETE
- FAILED
- BLOCKED