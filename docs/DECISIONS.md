# Project Decision Log

This document records important technical, architectural, and process
decisions made during the project.

The purpose is to preserve not only what was decided, but also why the
decision was made.

Decisions should not disappear inside conversations with AI agents.

---

## Decision Format

Every important decision should use the following structure:

### DEC-XXX - Decision Title

**Date:**
YYYY-MM-DD

**Status:**
Proposed / Accepted / Rejected / Superseded

**Type:**
GENERAL / SPECIFIC

**Context:**
What problem or situation caused this decision?

**Decision:**
What was decided?

**Reason:**
Why was this option selected?

**Alternatives:**
What other approaches were considered?

**Consequences:**
What changes because of this decision?

**Related Files:**
Which project files are affected?

**Rule Candidate:**
YES / NO

---

# Decision Records

## DEC-001 - Use AGENTS.md as the Main AI Instruction File

**Status:**
Accepted

**Type:**
GENERAL

**Context:**
Different AI coding agents may behave differently when working on the
same codebase.

**Decision:**
Use `AGENTS.md` as the central file containing project-level instructions
for AI coding agents.

**Reason:**
A shared instruction file makes agent behavior easier to standardize,
compare, and evaluate.

**Alternatives:**
- Give instructions manually for every task.
- Maintain different instructions for every AI tool.

**Consequences:**
AI agents working on the repository should follow a common set of rules.

**Related Files:**
`AGENTS.md`

**Rule Candidate:**
YES

---

## DEC-002 - Keep AI Instructions Tool-Agnostic

**Status:**
Accepted

**Type:**
GENERAL

**Context:**
The project is intended to compare and potentially use multiple AI coding
agents.

**Decision:**
Core project rules should not depend on a single AI product.

**Reason:**
The same standards should be reusable with different AI coding agents.

**Alternatives:**
Create separate rule systems for each AI tool.

**Consequences:**
Rules should describe desired engineering behavior rather than
tool-specific behavior whenever possible.

**Related Files:**
`AGENTS.md`

**Rule Candidate:**
YES

---

## DEC-003 - Create a Dedicated Test Project

**Status:**
Accepted

**Type:**
SPECIFIC

**Context:**
AI coding behavior needs to be tested in a controlled environment.

**Decision:**
Create `test-project/app.py` as a small experimental codebase.

**Reason:**
A small project makes AI-generated changes easier to inspect and compare.

**Alternatives:**
Test agents directly on a large real-world project.

**Consequences:**
Experiments can be performed without risking a larger codebase.

**Related Files:**
`test-project/app.py`

**Rule Candidate:**
NO

---

## DEC-004 - Track Project History with Git

**Status:**
Accepted

**Type:**
GENERAL

**Context:**
AI agents will modify project files during experiments.

**Decision:**
Use Git to track changes to the project.

**Reason:**
Git allows modifications to be inspected, compared, and reversed.

**Alternatives:**
Manually save different copies of project files.

**Consequences:**
Important project states and AI-generated changes can be compared through
version history.

**Related Files:**
Entire repository

**Rule Candidate:**
YES

---

## DEC-005 - Create a Persistent Documentation System

**Status:**
Accepted

**Type:**
GENERAL

**Context:**
Important knowledge was being created during conversations but could be
lost after the conversation ended.

**Decision:**
Create a `docs` directory for persistent project knowledge.

**Reason:**
Project knowledge should live inside the repository rather than only
inside conversations.

**Alternatives:**
Keep project knowledge only in chat history or README.md.

**Consequences:**
Changes, decisions, terminology, research, lessons, and influences will
have dedicated documentation files.

**Related Files:**
`docs/`

**Rule Candidate:**
YES

---

## DEC-006 - Separate General Knowledge from Specific Knowledge

**Status:**
Accepted

**Type:**
GENERAL

**Context:**
The project may eventually contain many decisions and observations.
Not all of them should become permanent AI rules.

**Decision:**
Classify knowledge as GENERAL or SPECIFIC.

**Reason:**
This prevents one-time project decisions from unnecessarily expanding
the global AI instruction set.

**Alternatives:**
Store every observation directly inside `AGENTS.md`.

**Consequences:**
Reusable knowledge can be separated from task-specific knowledge.

**Related Files:**
`GLOSSARY.md`
`DECISIONS.md`
`LESSONS.md`
`AGENTS.md`

**Rule Candidate:**
YES

---

## DEC-007 - Promote Rules Only After Evaluation

**Status:**
Accepted

**Type:**
GENERAL

**Context:**
A useful observation from one experiment may not necessarily be a good
general engineering rule.

**Decision:**
New observations should first become CANDIDATE RULES before being promoted
to `AGENTS.md`.

**Reason:**
This keeps the main instruction file focused and prevents unnecessary or
poorly supported rules from accumulating.

**Alternatives:**
Immediately add every new lesson to `AGENTS.md`.

**Consequences:**
The project develops its AI coding standard gradually based on accumulated
evidence.

**Related Files:**
`LESSONS.md`
`DECISIONS.md`
`AGENTS.md`

**Rule Candidate:**
YES