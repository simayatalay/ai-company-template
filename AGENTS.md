# Project Agent Instructions

## Purpose

This file defines the core rules that every AI coding agent must follow while working on this project.

The goal is to ensure that different developers and different AI tools produce consistent, simple, maintainable, and predictable results.

## Core Principles

1. Think Before Coding
2. Simplicity First
3. Surgical Changes
4. Goal-Driven Execution

## 1. Think Before Coding

Before writing or modifying code:

- Understand the user's actual goal.
- Inspect the relevant files before making changes.
- Identify the existing architecture and coding patterns.
- Identify assumptions, uncertainties, or missing information.
- Prefer existing project patterns over creating new ones.
- Do not start implementation until the required change is clear.

## 2. Simplicity First

When implementing a solution:

- Choose the simplest solution that satisfies the requirement.
- Do not introduce unnecessary abstractions.
- Do not add features that were not requested.
- Reuse existing functions, components, and patterns when possible.
- Prefer readable and explicit code over clever or overly complex code.
- Do not design for hypothetical future requirements unless explicitly requested.

## 3. Surgical Changes

When modifying an existing project:

- Change only the files and code required for the task.
- Do not refactor unrelated code.
- Do not rename unrelated variables, functions, files, or components.
- Do not reformat unrelated files.
- Preserve existing behavior unless the task explicitly requires changing it.
- Keep the code diff as small and focused as reasonably possible.
- If a larger change is necessary, explain why before making it.

## 5. Verification & Testing

After making code changes:

- Run the relevant existing tests when available.
- Add or update tests when the requested behavior requires it.
- Check for syntax, type, lint, or build errors when applicable.
- Verify the requested behavior whenever possible.
- Check that existing functionality has not been unintentionally broken.
- Never claim that a test passed unless it was actually executed.
- Never claim that the implementation works unless it was verified.
- Clearly report tests or checks that could not be performed.
- If verification fails, investigate the cause before considering the task complete.

## 6. Communication

When completing a task, communicate the result clearly and consistently.

The final response should include:

1. Summary
   - Briefly explain what was changed and why.

2. Files Changed
   - List the files that were created, modified, or deleted.
   - Briefly explain the purpose of each change.

3. Verification
   - Report the tests, checks, builds, or validations that were actually performed.
   - Clearly distinguish between passed, failed, and not executed checks.

4. Risks or Uncertainties
   - Report any known risks, assumptions, limitations, or unresolved issues.
   - Do not hide failed or incomplete verification.

5. Result
   - Clearly state whether the task is complete, partially complete, or blocked.

Keep responses concise, factual, and relevant to the requested task.
Do not claim work that was not actually performed.