<div align="center">
  <h1>AgentTeacher — Senior C++ & Systems Edition</h1>
  <p><b>Rigorous Mentorship, Hardware-Grounded Theory & Code Review for Systems & Embedded Engineers</b></p>
  <p><a href="README.vi.md"><b>Tiếng Việt (Khuyên Dùng)</b></a> · <a href="README.md"><b>English</b></a></p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/skill-agent--teacher-orange.svg?style=flat-square" alt="Skill"></a>
</div>

---

## Why AgentTeacher C++ & Systems?

When learning Modern C++, Bare-metal Embedded, and Computer Architecture, **dictionary definitions don't teach — physical hardware constraints, memory layouts, and compiler codegen do**.

AgentTeacher transforms the learning experience into a complete 6-phase engineering mentorship loop:
`Ingestion (YouTube / Docs / Concepts) → 6-Layer Hardware Theory Spine → 3-Level Progressive Exercises → Student Implementation → Senior Code Review & Multi-Pillar Deep Assessment → Learning Report & Knowledge Graph Persistence`.

---

## The 6-Phase Engineering Loop

```
┌─────────────────────────────────────────────────────────────┐
│ 1. INGESTION & CONCEPT EXTRACTION                           │
│    Input: YouTube Video, Transcript, Datasheet, Topic       │
│    Action: Extract concepts & audit prerequisites           │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. THEORY SYNTHESIS (THE 6-LAYER HARDWARE SPINE)            │
│    Intuition → Memory Layout & Stack Frame → Code & ASM     │
│    → Purpose Walkthrough → Hardware Traps & UB → Pointers   │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. 3-LEVEL PROGRESSIVE EXERCISES                            │
│    Level 1: Host Simulation in standard C++20 on PC         │
│    Level 2: Target & Register Mapping on MCU (CMSIS/Bitwise)│
│    Level 3: Zero-HAL / Bare-Metal (No vendor SDK/headers)   │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. STUDENT IMPLEMENTATION                                   │
│    You write the code and submit snippets or git repo       │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. SENIOR CODE REVIEW & DEEP ASSESSMENT BATTERY             │
│    Scored across 4 Pillars: Understanding / Impl / Debug /  │
│    Mental Model + 3-Tier Questions (Concept, Mutation, Bug) │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. LEARNING REPORT & KNOWLEDGE GRAPH TRACKING               │
│    Updates learning_profile.json & unlocks next milestones  │
└─────────────────────────────────────────────────────────────┘
```

---

## Repository Map

- [SKILL.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/SKILL.md) — Skill entrypoint: 6-phase lifecycle and contracts.
- [README.vi.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/README.vi.md) — Comprehensive user-facing documentation in Vietnamese.
- [AGENTS.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/AGENTS.md) / [CLAUDE.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/CLAUDE.md) — Working rules and operational guidelines.
- `references/`:
  - [knowledge-graph.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/knowledge-graph.md) — 24-node C++ & Systems competency DAG and prerequisites matrix.
  - [teaching-method.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/teaching-method.md) — 6-layer teaching playbook grounded in hardware physics.
  - [exercise-generator.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/exercise-generator.md) — 3-level progressive exercise rubric.
  - [code-review-rubric.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/code-review-rubric.md) — Senior Code Review standards and 3-tier deep assessment battery.
  - [youtube-ingestion.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/youtube-ingestion.md) — Pipeline for parsing YouTube transcripts and technical documentation.
  - [concept-to-language.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/concept-to-language.md) — Domain to language & assembly mapping.
- `scripts/`:
  - [tracker.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/tracker.py) — CLI tracking engine managing `learning_profile.json`.
  - [lab_manager.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/lab_manager.py) — Lab scaffolding and session snapshots manager.
  - [package_skill.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/package_skill.py) & [package-skill.sh](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/package-skill.sh) — Skill release packaging tools.
- `labs/` — Hands-on student workspace (`lab01_boot`, `lab02_mmio`...).
- `sessions/` — Student session assessment snapshots.
- `assets/examples/`:
  - [interrupt-nvic-cortex-m.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/assets/examples/interrupt-nvic-cortex-m.md) & [interrupt-sim.cpp](file:///c:/Users/Phucx/Desktop/Agent_Teacher/assets/examples/interrupt-sim.cpp) — Worked Interrupt & NVIC example.
  - [lockfree-spsc-queue.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/assets/examples/lockfree-spsc-queue.md) & [lockfree-spsc-queue.hpp](file:///c:/Users/Phucx/Desktop/Agent_Teacher/assets/examples/lockfree-spsc-queue.hpp) — Worked Lock-Free SPSC Ring Buffer example.

---

## Quick CLI Commands

```bash
# View Knowledge Graph mastery tree
python scripts/tracker.py --status

# Audit prerequisites before diving into an advanced concept
python scripts/tracker.py --check rtos-context-switch

# Update student score after deep assessment
python scripts/tracker.py --update "embed-nvic-interrupt" --state MASTERED --score 90

# List active labs or scaffold a new one
python scripts/lab_manager.py --list
python scripts/lab_manager.py --create lab02_mmio --name "Lab 02: Peripheral MMIO"
```
