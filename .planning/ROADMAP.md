# Roadmap: Molecular Genetics Study Tool

**Created:** 2026-01-31
**Milestone:** v2.0 — Gamified Web App

## Overview

| Phase | Name | Goal | Requirements |
|-------|------|------|--------------|
| 1 | Core Quiz (CLI) | Working CLI quiz | QUIZ-01 to QUIZ-03 |
| 2 | CLI Polish | Color, progress, history | Complete |
| 3 | Web Foundation | Basic web quiz working | WEB-01 to WEB-07, DATA-01 to DATA-03, UI-01 to UI-05 |
| 4 | Gamification | XP, levels, streaks, achievements, progress | GAME-01 to GAME-05, ACH-01 to ACH-06, PROG-01 to PROG-05 |
| 5 | Study Modes | Topic filter, weak spots, flashcards | MODE-01 to MODE-04 |

---

## Phase 1: Core Quiz (CLI) ✓

**Status:** Complete

Built CLI quiz tool with 49 questions.

---

## Phase 2: CLI Polish ✓

**Status:** Complete

Added color output (colorama), progress bar, history tracking.

---

## Phase 3: Web Foundation ✓

**Status:** Complete

Browser-based quiz with localStorage persistence, responsive design, and polished animations.

Plans:
- [x] 03-01-PLAN.md — Core web quiz (questions, answers, feedback, progress, final score)
- [x] 03-02-PLAN.md — Data persistence (localStorage) and responsive polish

---

## Phase 4: Gamification ✓

**Status:** Complete

**Goal:** User earns XP, levels up, maintains streaks, and unlocks achievements

**Requirements:** GAME-01 to GAME-05, ACH-01 to ACH-06, PROG-01 to PROG-05

**Plans:** 3 plans

Plans:
- [x] 04-01-PLAN.md — XP, levels, and daily streak system
- [x] 04-02-PLAN.md — Achievements with badges, toasts, and gallery
- [x] 04-03-PLAN.md — Progress tracking and stats dashboard

**Delivered:**
1. XP awarded for correct answers (+10 base, +5 per streak bonus)
2. Level displayed based on total XP (100 XP per level)
3. Daily streak counter with 10-question minimum
4. 15 milestone + dynamic topic mastery achievements
5. Topic mastery progress bars on stats dashboard
6. Weak topics highlighted in orange (< 70%)

---

## Phase 5: Study Modes

**Goal:** User can study specific topics, focus on weak areas, and use flashcards

**Requirements:** MODE-01 to MODE-04

**Success Criteria:**
1. Topic filter lets user quiz on specific subject
2. "Weak spots" mode prioritizes missed questions
3. Flashcard mode shows question, reveals answer on click
4. Mode selection on home screen

---

## Coverage

All 32 v1 requirements mapped to phases.

| Category | Count | Phase |
|----------|-------|-------|
| Core Quiz Web | 7 | Phase 3 |
| Gamification | 5 | Phase 4 |
| Achievements | 6 | Phase 4 |
| Progress Tracking | 5 | Phase 4 |
| Data Persistence | 3 | Phase 3 |
| Study Modes | 4 | Phase 5 |
| UI/UX | 5 | Phase 3 |

---
*Roadmap updated: 2026-01-31*
