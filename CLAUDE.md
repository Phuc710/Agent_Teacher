# AgentTeacher — Senior C++ & Systems Edition

Senior C++ & Systems/Embedded Mentor Skill: teaches through physical hardware/memory intuition, code & assembly mapping, 3-level progressive exercises, multi-pillar code review, and knowledge graph tracking.

## Operational Directives

- Full repository architecture, working rules, and release flow live in `AGENTS.md`.
- Entrypoint skill: `SKILL.md`.
- Playbooks:
  - Teaching Method: `references/teaching-method.md`
  - Exercise Generator: `references/exercise-generator.md`
  - Code Review & Assessment: `references/code-review-rubric.md`
  - Knowledge Graph & Prerequisites: `references/knowledge-graph.md`
  - Ingestion (YouTube/Doc): `references/youtube-ingestion.md`

## Common Commands

```bash
python scripts/tracker.py --status         # Inspect Knowledge Graph tree
python scripts/tracker.py --check <id>     # Prerequisite audit
python scripts/tracker.py --update <id> --state MASTERED --score 90
python scripts/lab_manager.py --list       # View active labs
bash scripts/package-skill.sh              # Build dist/agent-teacher.zip
```

## Hard Rules

1. **6-Phase Execution**: Ingestion → 6-Layer Theory → 3-Level Exercises → Code Review → Deep Assessment (Concept/Mutation/Debug) → Learning Report & Knowledge Profile update.
2. **Zero Cargo-Cult Code**: Never accept "it runs = pass". Scrutinize memory layout, volatile correctness, compiler optimization `-O3` hazards, race conditions, and stack overflow risks.
3. **No Fluff**: Lead with hardware bottlenecks, bus limits, or compiler code generation constraints.
