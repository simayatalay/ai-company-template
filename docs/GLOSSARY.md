# Project Glossary

This document defines the shared terminology used between the developer
and AI coding agents working on this project.

The purpose of this glossary is to reduce ambiguity and create a consistent
communication language between humans and AI agents.

---

## Core Commands

### PLAN

Meaning:
Analyze the requested task before making any code changes.

Expected AI behavior:
- Understand the goal.
- Inspect the relevant files.
- Identify possible risks.
- Explain the intended approach.
- Do not modify code yet.

---

### IMPLEMENT

Meaning:
Execute an already understood or approved task.

Expected AI behavior:
- Make only the necessary changes.
- Follow the rules in `AGENTS.md`.
- Avoid unrelated modifications.
- Keep the implementation simple.

---

### VERIFY

Meaning:
Check whether the implementation works correctly.

Expected AI behavior:
- Run relevant tests or checks.
- Inspect the changed behavior.
- Report what was actually verified.
- Do not claim tests were performed if they were not run.

---

### DOCUMENT

Meaning:
Record important information produced during the task.

Expected AI behavior:
Determine where the information belongs.

Examples:

- Project changes -> `CHANGELOG.md`
- Important decisions -> `DECISIONS.md`
- New terminology -> `GLOSSARY.md`
- Research findings -> `RESEARCH.md`
- Lessons learned -> `LESSONS.md`
- External engineering influences -> `INFLUENCES.md`

---

### DECISION

Meaning:
A meaningful technical or project decision has been made.

Expected AI behavior:
Record the decision in `DECISIONS.md`.

The record should explain:

- What was decided?
- Why was it decided?
- What alternatives existed?
- What are the consequences?

---

### DONE

Meaning:
The requested task has been completed and verified.

A task should only be marked DONE when:

- the requested change is implemented,
- relevant verification has been performed,
- important changes are documented,
- unresolved problems are reported.

If these conditions are not satisfied, the AI should not report the task
as DONE.

---

## Knowledge Classification

### GENERAL

A rule, lesson, or decision that is useful across many projects.

General knowledge should be considered for inclusion in the reusable
AI coding standard.

---

### SPECIFIC

A decision or piece of information that only applies to a particular
task, feature, experiment, or project.

Specific knowledge should remain documented but should not automatically
become a general rule.

---

### CANDIDATE RULE

A repeated lesson or observation that may eventually become a permanent
rule in `AGENTS.md`.

Before promotion, the rule should have sufficient evidence or repeated
usefulness.

---

### PROMOTED RULE

A candidate rule that has been reviewed and accepted as a general
AI coding rule.

Promoted rules may be added to `AGENTS.md`.

---

## Task Status

### NOT STARTED
The task has not been worked on yet.

### IN PROGRESS
Work on the task has started but is not complete.

### BLOCKED
The task cannot continue because of a known dependency or problem.

### NEEDS VERIFICATION
Implementation exists but has not been sufficiently tested or checked.

### COMPLETE
Implementation, verification, and required documentation are finished.

---

## Example Communication

Human:

PLAN: Improve the calculate_total function.

AI should first analyze the task without modifying code.

Human:

IMPLEMENT.

AI may now make the necessary code changes.

Human:

VERIFY.

AI should test or inspect the implementation.

Human:

DOCUMENT.

AI should record relevant changes, decisions, or lessons.

Human:

DONE?

AI should only answer COMPLETE if implementation, verification,
and documentation requirements have been satisfied.