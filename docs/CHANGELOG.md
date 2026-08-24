# Project Changelog

This document records the important changes made throughout the project.

---

## Phase 1 - Project Initialization

### Created Project Structure
- Created the main project folder: `ai-company-template`.
- Created `AGENTS.md`.
- Created `README.md`.
- Created the `test-project` directory.
- Created `test-project/app.py`.

### Purpose
The initial structure was created to build a reusable AI coding standards template.

---

## Phase 2 - Agent Rules

### Created AGENTS.md

The `AGENTS.md` file was created to define how AI coding agents should behave while working on the project.

The following core principles were added:

- Think Before Coding
- Simplicity First
- Surgical Changes
- Goal-Driven Execution

Additional rules were added for:

- planning
- code changes
- verification
- testing
- communication
- reporting risks and uncertainties

### Purpose
The goal is to make AI-generated changes predictable, controlled, testable, and easy to review.

---

## Phase 3 - Test Project

Created:

`test-project/app.py`

A small Python program was added to provide a controlled environment for testing AI coding agents.

The program currently contains:

- a `greet_user()` function
- a `calculate_total()` function
- user input
- basic output

### Purpose
This test project will allow different AI coding agents to receive the same task so their behavior can be compared.

---

## Phase 4 - Git Setup

Git was initialized for the project.

The first project commit was created:

`Initial AI company template`

### Purpose
Git allows every modification made by humans or AI agents to be tracked and compared.

---

## Phase 5 - Claude Code Installation

Claude Code was installed and verified successfully.

### Purpose
Claude Code will be one of the AI coding agents used to test whether the rules defined in `AGENTS.md` influence AI behavior.

---

## Phase 6 - Documentation System

A `docs` directory was introduced.

The documentation system will contain:

- `CHANGELOG.md`
- `GLOSSARY.md`
- `DECISIONS.md`
- `RESEARCH.md`
- `LESSONS.md`
- `INFLUENCES.md`

### Purpose
Important project knowledge should not remain only inside AI conversations.

Changes, decisions, terminology, experiments, research, and lessons should be stored permanently inside the repository.

---

## Current Status

Project foundation: COMPLETE

AGENTS.md initial rules: COMPLETE

Git initialization: COMPLETE

Claude Code installation: COMPLETE

Documentation system: IN PROGRESS

AI agent comparison experiments: NOT STARTED
---

## Phase 7 - Agent Evaluation System

### Added Evaluation Framework

Created the `evals/` directory to measure whether AI coding agents
follow the project's engineering standards.

Added:

- `evals/README.md`
- `evals/EVAL-001.md`
- `evals/EVAL-002.md`
- `evals/EVAL-003.md`
- `evals/SCORING.md`

### Evaluation Areas

The evaluation system measures:

- task correctness,
- scope discipline,
- simplicity and code quality,
- verification and testing,
- documentation and knowledge management,
- communication,
- Definition of Done compliance.

### Scoring

A common 100-point scoring system was introduced so that different
AI coding agents can be evaluated using the same criteria.

### Purpose

The project should not assume that written AI rules are effective.

Agent behavior must be tested, observed, and measured before rules
are considered successful.

### Current Status

Evaluation framework: COMPLETE

Evaluation scenarios designed: COMPLETE

Live agent evaluations: NOT RUN