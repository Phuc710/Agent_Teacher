# AgentTeacher Agent Guide — Senior Software & Systems Edition

> Personal/global agent rules may live outside this repository. This file records AgentTeacher-specific repository maps, Working Rules, Current Risk Areas, Verification, and Release Flow.

## Project

AgentTeacher is an advanced pedagogical and code review skill designed for **Senior Software & Systems Mentorship across any programming language (C/C++, Rust, Go, Python, TypeScript, and Systems)**. It operates on an end-to-end 6-phase engineering mentorship loop:
`Ingestion (YouTube / Docs / Concepts) → 6-Layer Under-The-Hood Theory Spine → 3-Level Progressive Exercises → Student Implementation → Senior Code Review & Multi-Pillar Deep Assessment → Learning Report & Knowledge Graph Persistence`.

## Repository Map

- `SKILL.md` — skill entrypoint: 6-phase lifecycle, triggers, language/architecture standards, and output contracts.
- `README.md` / `README.vi.md` — user-facing project documentation.
- `CLAUDE.md` — operational entry and hard rules for Claude / Agent execution.
- `LICENSE` — MIT.
- `references/teaching-method.md` — 6-layer teaching playbook grounded in hardware physics, runtime mechanics, and compiler codegen across languages.
- `references/exercise-generator.md` — 3-Level Progressive Exercise specification (Level 1: Core Mechanics, Level 2: Real-World Constraints, Level 3: Under-the-Hood / Zero-Framework).
- `references/code-review-rubric.md` — Senior Code Review standards (Understanding, Implementation, Debugging, Mental Model) and Deep Assessment question battery (Concept, Code Mutation, Debugging Scenarios).
- `references/knowledge-graph.md` — Directed Acyclic Graph (DAG) of competencies and prerequisite rules.
- `references/youtube-ingestion.md` — Pipeline for parsing YouTube transcripts and technical documentation into structured concept maps.
- `references/concept-to-language.md` — Mapping of concept domain to optimal expressive language and runtime representations.
- `scripts/tracker.py` — CLI engine managing `learning_profile.json` (prerequisite verification, status tree, score updates).
- `scripts/lab_manager.py` — Lab scaffolding & session snapshot manager.
- `scripts/package_skill.py` — Skill release packaging script building `dist/agent-teacher.zip`.
- `learning_profile.json` — persistent learner mastery profile in the workspace.

## Commands

```bash
python scripts/tracker.py --status         # View current Knowledge Graph progress
python scripts/tracker.py --check <node>   # Check prerequisites before starting a topic
python scripts/tracker.py --update <node> --state MASTERED --score 90
python scripts/lab_manager.py --list       # View active labs
python scripts/package_skill.py            # Build dist/agent-teacher.zip
```

## Working Rules

1. **The 6-Phase Loop is Mandatory**:
   - Do not stop at explaining theory. Every lesson leads to 3-level progressive exercises.
   - When reviewing student code, do not merely state "it runs". Scrutinize memory footprint, allocation overhead, compiler/engine optimization hazards, and race conditions.
   - Always pose the 3-level Deep Assessment questions (Concept, Code Mutation, Debug Scenario) before issuing a final score.
2. **Under-The-Hood Grounding**:
   - Definitions do not teach — memory layouts, runtime models, and execution mechanics do. Always show how memory is managed, how threads/routines coordinate, and what happens under the hood.
3. **Prerequisite Enforcement**:
   - Consult `references/knowledge-graph.md` and `scripts/tracker.py --check`. If a learner lacks foundational prerequisites, flag the gap explicitly before diving into advanced topics.
4. **Tone**:
   - Senior Technical Mentor: direct, rigorous, constructive. Reject shallow implementations or cargo-cult programming.

