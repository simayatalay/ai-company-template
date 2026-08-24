# Research Log

This document stores research that may influence the project's
AI engineering standards.

Research is not automatically treated as a project rule.

Every important idea should move through an evaluation process before
being promoted into the permanent AI instruction system.

---

# Research Process

SOURCE
  ↓
OBSERVATION
  ↓
INTERPRETATION
  ↓
CANDIDATE RULE
  ↓
EXPERIMENT
  ↓
LESSON
  ↓
DECISION
  ↓
PROMOTION or REJECTION

---

# Research Entry Format

## RES-XXX - Research Title

**Status:**
TO RESEARCH / RESEARCHING / EVALUATED / REJECTED

**Category:**
AI / Software Engineering / Testing / Architecture / Workflow / Tooling

**Source:**

**Person / Author:**

**Main Idea:**

**Project Interpretation:**

**Candidate Rule:**

**Experiment Idea:**

**Result:**

**Related Decisions:**

---

# Research Entries

## RES-001 - Context Before Coding

**Status:**
RESEARCHING

**Category:**
AI / Workflow

**Person / Author:**
Andrej Karpathy

**Main Idea:**
AI-assisted coding benefits from giving the model sufficient context
and defining the task clearly before implementation.

**Project Interpretation:**
The coding agent should understand the relevant project context before
making changes.

**Candidate Rule:**
Inspect relevant files and understand the requested outcome before
implementation.

**Experiment Idea:**
Give the same coding task with and without the Think Before Coding rule
and compare the resulting changes.

**Result:**
NOT TESTED

---

## RES-002 - Simplicity and Measurement

**Status:**
RESEARCHING

**Category:**
Software Engineering

**Person / Author:**
Rob Pike

**Main Idea:**
Avoid unnecessary complexity and premature optimization.
Prefer simple algorithms and data structures and measure before
optimizing.

**Project Interpretation:**
AI coding agents should not introduce complex solutions or performance
optimizations without evidence that they are necessary.

**Candidate Rule:**
Do not optimize or introduce additional complexity without a demonstrated
requirement.

**Experiment Idea:**
Give an AI agent a simple performance-related task and observe whether
it introduces unnecessary abstractions or optimization.

**Result:**
NOT TESTED

---

## RES-003 - Simple Is Not the Same as Easy

**Status:**
RESEARCHING

**Category:**
Architecture / Software Engineering

**Person / Author:**
Rich Hickey

**Main Idea:**
A solution being familiar or easy to implement does not necessarily make
it structurally simple.

Complexity can arise when independent concepts become unnecessarily
intertwined.

**Project Interpretation:**
AI agents should evaluate whether their solution couples responsibilities
that could remain independent.

**Candidate Rule:**
Avoid unnecessarily coupling independent concepts or responsibilities.

**Experiment Idea:**
Give an agent a task that can be solved either by modifying an existing
independent function or by coupling multiple components.

Compare the resulting architecture.

**Result:**
NOT TESTED

---

## RES-004 - Small Verified Changes

**Status:**
RESEARCHING

**Category:**
Testing / Workflow

**Person / Author:**
Kent Beck

**Main Idea:**
Software development benefits from short feedback loops, small changes,
and verification through tests.

**Project Interpretation:**
AI-generated changes should preferably be small enough to understand,
test, and review independently.

**Candidate Rule:**
Prefer small independently verifiable changes.

**Experiment Idea:**
Compare an unrestricted AI implementation with an implementation
explicitly instructed to work in small verified steps.

**Result:**
NOT TESTED

---

## RES-005 - Practical Agentic Coding Workflows

**Status:**
TO RESEARCH

**Category:**
AI / Tooling / Workflow

**Person / Author:**
Alican Kiraz

**Main Idea:**
To be determined through source-based research.

Areas of interest include:

- AI coding agents
- Claude Code
- local LLM workflows
- MCP
- agent skills
- development automation

**Project Interpretation:**
Practical AI-assisted development workflows may reveal patterns that can
be tested within this project's agent architecture.

**Candidate Rule:**
NONE YET

**Experiment Idea:**
Study documented workflows first, then reproduce relevant patterns in a
controlled environment.

**Result:**
NOT TESTED

---

# Research Backlog

Topics that should be investigated later:

- Prompt Engineering 101 / 102
- Claude Code best practices
- CLAUDE.md
- AGENTS.md conventions
- Claude Skills
- Superpowers
- MCP
- Context engineering
- Local LLM coding models
- Ollama
- Automated code review
- Structured AI output
- GitHub Actions
- Self-hosted runners
- Agent evaluation
- Multi-agent consistency
- Design systems for AI-generated UI

---

# Research Rules

1. Do not treat an idea as true only because a respected person said it.

2. Prefer original or reliable sources when possible.

3. Separate the original author's idea from our interpretation.

4. Do not attribute a rule to someone without sufficient evidence.

5. Store uncertain information as research rather than as a permanent rule.

6. Test candidate rules when practical.

7. Record failed experiments as well as successful experiments.

8. Promote rules based on usefulness and evidence, not popularity.