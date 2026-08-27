# Single-Agent Pipeline

## Purpose

Execute a software task from implementation through verification, review, and Git commit in a controlled sequence.

## Workflow

1. Read `AGENTS.md`.
2. Understand the requested task.
3. Inspect the relevant project files.
4. Make the smallest necessary code change.
5. Run appropriate verification or tests.
6. Review the resulting diff using `agents/CODE_REVIEW.md`.
7. If review result is `APPROVE`, create a focused Git commit.
8. If review result is `REQUEST CHANGES`, fix the blocking findings and repeat verification and review.
9. If the task cannot continue safely, report `BLOCKED`.

## Rules

- Do not skip verification.
- Do not claim tests were run if they were not run.
- Do not commit when review returns `REQUEST CHANGES` or `BLOCKED`.
- Avoid unrelated changes.
- Keep commits focused on the task.
- Report each completed stage clearly.
- Verification is mandatory for every code change, even if the change is small.
- Review must not return APPROVE when required verification evidence is missing.

## Final Output

Report:

- Task
- Implementation
- Verification
- Review Decision
- Commit
- Final Status

Final Status must be exactly one of:

- COMPLETE
- PARTIAL
- BLOCKED
