# AgentTeacher Agent Guide — Senior C++ & Systems/Embedded Edition

> Personal/global agent rules may live outside this repository. This file records AgentTeacher-specific repository maps, Working Rules, Current Risk Areas, Verification, and Release Flow.

## Project

AgentTeacher is an advanced pedagogical and code review skill specialized for **Modern C++, Embedded Bare-Metal, Computer Architecture, and RTOS**. It operates on an end-to-end 6-phase engineering mentorship loop:
`Ingestion (YouTube / Docs / Concepts) → 6-Layer Hardware/Memory Theory Spine → 3-Level Progressive Exercises → Student Implementation → Senior Code Review & Multi-Pillar Deep Assessment → Learning Report & Knowledge Graph Persistence`.

## Repository Map

- `SKILL.md` — skill entrypoint: 6-phase lifecycle, triggers, language/architecture standards, and output contracts.
- `README.md` / `README.vi.md` — user-facing project documentation.
- `CLAUDE.md` — operational entry and hard rules for Claude / Agent execution.
- `LICENSE` — MIT.
- `references/teaching-method.md` — Senior C++ & Systems 6-layer teaching playbook (Intuition from physical/hardware constraints, Mental Model & Memory layout, Code & ASM mapping, Purpose walkthrough, Traps & UB, Pointers).
- `references/exercise-generator.md` — 3-Level Progressive Exercise specification (Level 1: Host Simulation, Level 2: Target Registers/CMSIS, Level 3: Zero-HAL Bare-metal).
- `references/code-review-rubric.md` — Senior Code Review standards (Understanding, Implementation, Debugging, Mental Model) and Deep Assessment question battery (Concept, Code Mutation, Debugging Scenarios).
- `references/knowledge-graph.md` — Directed Acyclic Graph (DAG) of C++ and Embedded competencies and prerequisite rules.
- `references/youtube-ingestion.md` — Pipeline for parsing YouTube transcripts and technical documentation into structured concept maps.
- `references/concept-to-language.md` — mapping of concept domain to optimal expressive language and assembly/register representations.
- `scripts/tracker.py` — CLI engine managing `learning_profile.json` (prerequisite verification, status tree, score updates).
- `scripts/lab_manager.py` — Lab scaffolding & session snapshot manager.
- `learning_profile.json` — persistent learner mastery profile in the workspace.
- `evals/evals.json` — evaluation battery testing both CS theory and practical C++ / Systems scenarios.
- `scripts/package-skill.sh` — packaging script building `dist/agent-teacher.zip`.

## Commands

```bash
python scripts/tracker.py --status         # View current Knowledge Graph progress
python scripts/tracker.py --check <node>   # Check prerequisites before starting a topic
python scripts/tracker.py --update <node> --state MASTERED --score 90
python scripts/lab_manager.py --list       # View active labs
bash scripts/package-skill.sh              # Build dist/agent-teacher.zip
```

## Working Rules

1. **The 6-Phase Loop is Mandatory**:
   - Do not stop at explaining theory. Every lesson leads to 3-level progressive exercises.
   - When reviewing student code, do not merely state "it runs". Review for memory footprint, cache alignment, volatile correctness, atomic operations, and compiler optimization effects.
   - Always pose the 3-level Deep Assessment questions (Concept, Code Mutation, Debug Scenario) before issuing a final score.
2. **Hardware & Memory Grounding**:
   - In C++ and Embedded, definitions do not teach — memory layouts and hardware mechanics do. Always show Stack vs Heap vs Flash vs RAM, CPU register context, and compiler codegen.
3. **Prerequisite Enforcement**:
   - Consult `references/knowledge-graph.md` and `scripts/tracker.py --check`. If a learner lacks foundational prerequisites, flag the gap explicitly before diving into advanced topics.
4. **Tone**:
   - Senior Technical Mentor: direct, rigorous, constructive. Reject shallow implementations or cargo-cult programming.
