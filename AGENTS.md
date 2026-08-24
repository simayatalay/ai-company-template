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

## 7. Documentation & Knowledge Protocol

Project knowledge must be stored inside the repository and must not exist
only inside conversations with AI agents.

Before starting a task:

- Read `AGENTS.md`.
- Check `docs/GLOSSARY.md` for project-specific terminology.
- Check `docs/DECISIONS.md` for relevant existing decisions.
- Check other documentation when it is relevant to the task.

During a task:

- Follow existing project decisions and terminology.
- Do not create a new rule if an existing rule already covers the situation.
- Identify important new decisions, observations, and lessons.

After completing a task:

- Update `docs/CHANGELOG.md` when the project has meaningfully changed.
- Update `docs/DECISIONS.md` when an important technical or process decision was made.
- Update `docs/GLOSSARY.md` when new shared terminology is introduced.
- Update `docs/LESSONS.md` when an experiment produces a useful observation.
- Update `docs/RESEARCH.md` when new external research is introduced.
- Update `docs/INFLUENCES.md` when an external engineering influence is added or changed.

Do not update documentation unnecessarily.

Documentation changes must reflect actual work, decisions, research,
or observations.
## 8. Knowledge Classification & Rule Promotion

Not every observation or decision should become a permanent project rule.

Classify new knowledge as:

- SPECIFIC
- GENERAL
- CANDIDATE RULE
- PROMOTED RULE

SPECIFIC knowledge should remain in the relevant documentation.

GENERAL knowledge may be considered for reuse across tasks or projects.

A CANDIDATE RULE must be evaluated before becoming a permanent rule.

A rule should be promoted into `AGENTS.md` only when there is sufficient
evidence that it is broadly useful.

The preferred knowledge lifecycle is:

Research or Experiment
→ Observation
→ Lesson
→ Candidate Rule
→ Evaluation
→ Decision
→ Promoted Rule

Do not promote rules only because an expert, AI model, or external source
suggested them.

Prefer evidence from repeated experiments and practical usefulness.
## 9. Definition of Done

A task is not DONE only because code was written.

Before reporting a task as COMPLETE, confirm:

- The requested goal has been implemented.
- The change remains within the intended scope.
- Relevant verification has been performed.
- Failed or unavailable verification has been reported.
- Relevant documentation has been updated.
- Important decisions have been recorded.
- Important lessons or observations have been recorded when applicable.
- No known unresolved blocker is being hidden.

If these conditions are not satisfied, report the task as:

- IN PROGRESS
- NEEDS VERIFICATION
- PARTIALLY COMPLETE
- BLOCKED

Do not report COMPLETE unless the Definition of Done is satisfied.