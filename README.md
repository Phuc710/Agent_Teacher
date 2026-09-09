<div align="center">
  <h1>AgentTeacher — Senior Software & Systems Edition</h1>
  <p><b>Rigorous Mentorship, Under-The-Hood Architecture & Deep Code Review for Any Language</b></p>
  <p><a href="README.vi.md"><b>Tiếng Việt (Khuyên Dùng)</b></a> · <a href="README.md"><b>English</b></a></p>
  <p>
    <img src="https://img.shields.io/badge/Languages-C%2B%2B%20%7C%20Rust%20%7C%20Go%20%7C%20Python%20%7C%20TS-00599C?style=flat-square" alt="Languages">
    <img src="https://img.shields.io/badge/Focus-Under--the--Hood%20%7C%20Systems-0091BD?style=flat-square" alt="Focus">
    <img src="https://img.shields.io/badge/Doctrine-Build%20Small.%20Understand%20Deep.-E95420?style=flat-square" alt="Doctrine">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
    <img src="https://img.shields.io/badge/Skill-AgentTeacher-blueviolet?style=flat-square" alt="Skill">
  </p>
</div>

---

## Why AgentTeacher?

Whether you are writing Modern C++, safe Rust, concurrent Go, Python, or TypeScript, **dictionary definitions don't teach — physical runtime mechanics, memory layouts, and compiler codegen do**.

Never learn by shallow feature-assembling (copy-pasting libraries to build a flashy UI without understanding what runs underneath).
AgentTeacher transforms your journey with the **"Build small. Understand deep."** doctrine across a complete 6-phase engineering mentorship loop:
`Ingestion (YouTube / Docs / Concepts) → 6-Layer Under-The-Hood Theory Spine → 3-Level Progressive Exercises → Student Implementation → Senior Code Review & Multi-Pillar Deep Assessment → Learning Report & Knowledge Graph Persistence`.

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
│    Level 1: Core Mechanics (Grammar & fundamental logic)    │
│    Level 2: Real-World & Constraints (Resource & efficiency)│
│    Level 3: Under-the-Hood / Zero-Framework (Build from scratch)│
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. STUDENT IMPLEMENTATION                                   │
│    Write code directly in labs/<lab_id>/ or submit snippets │
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
  - [knowledge-graph.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/knowledge-graph.md) — Competency DAG and prerequisites matrix.
  - [teaching-method.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/teaching-method.md) — 6-layer teaching playbook grounded in hardware physics and runtime models.
  - [exercise-generator.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/exercise-generator.md) — 3-level progressive exercise rubric.
  - [code-review-rubric.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/code-review-rubric.md) — Senior Code Review standards and 3-tier deep assessment battery.
  - [youtube-ingestion.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/youtube-ingestion.md) — Pipeline for parsing YouTube transcripts and technical documentation.
  - [concept-to-language.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/concept-to-language.md) — Domain to language & runtime mapping.
- `scripts/`:
  - [tracker.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/tracker.py) — CLI tracking engine managing `learning_profile.json`.
  - [lab_manager.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/lab_manager.py) — Lab scaffolding and session snapshots manager.
  - [package_skill.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/package_skill.py) — Skill release packaging tool.
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

---

## Keywords & Topics for Discovery

`programming` · `software-engineering` · `systems-programming` · `c++` · `rust` · `golang` · `python` · `typescript` · `embedded-systems` · `bare-metal` · `concurrency` · `memory-management` · `compilers` · `code-review` · `architecture` · `under-the-hood` · `learning-mentor`


