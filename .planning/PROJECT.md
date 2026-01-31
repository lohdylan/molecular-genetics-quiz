# Molecular Genetics Study Tool

## What This Is

A gamified web-based study tool for molecular genetics exam preparation. Features Duolingo-style points, streaks, achievements, and progress tracking. Quizzes users on concepts with immediate feedback and focuses on weak areas.

## Core Value

Help the user actively recall and retain molecular genetics concepts through engaging, gamified testing — not passive review.

## Requirements

### Validated

- Quiz system that asks questions and checks answers (CLI version complete)
- Question bank loaded from provided quiz content (49 questions)
- Immediate feedback with explanations
- Color-coded feedback (correct/incorrect)
- Progress bar during quiz
- History tracking with score trends

### Active

- [ ] Web-based interface (browser app)
- [ ] Gamified UI (points, XP, levels)
- [ ] Daily streaks tracking
- [ ] Achievement badges system
- [ ] Visual progress per topic
- [ ] Mastery levels for each category
- [ ] Browser localStorage for persistence
- [ ] Weak spot prioritization in review mode
- [ ] Flashcard study mode

### Out of Scope

- User accounts / authentication — localStorage is sufficient
- Mobile app — responsive web works on mobile
- Backend server — fully client-side
- Content creation UI — questions in JSON
- Complex spaced repetition algorithms — simple tracking sufficient

## Context

**Exam Details:**
- 36 multiple choice questions
- Covers Unit 1: DNA structure, replication, transcription, translation, gene regulation
- Monday exam

**Content Sources:**
- Quiz 1: 16 questions
- Quiz 2: 17 questions
- Practice Problems: 16 questions
- Total: 49 questions across 15 topics

**Topics Covered:**
DNA Structure, DNA Replication, Chromatin Structure, PCR, Sanger Sequencing, Transcription, Translation, Gene Expression, Gene Regulation, Gene Structure, Lac Operon, Mutations, RNA Interference

**Current State:**
- CLI quiz tool working with color output, progress bar, history tracking
- All 49 questions in JSON format with explanations
- Ready to transform into web app

## Constraints

- **Tech stack**: HTML/CSS/JavaScript (vanilla or lightweight framework) — keep it simple
- **No backend**: Everything runs in browser, data in localStorage
- **Mobile-friendly**: Responsive design that works on phone
- **Build on existing**: Reuse questions.json data structure

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| CLI-based quiz tool | Fastest initial build | ✓ Good (working) |
| Web app upgrade | Cleaner UX, gamification possible | — Pending |
| localStorage | No server needed, persists data, simple | — Pending |
| Vanilla JS or lightweight | Fast to build, no complex tooling | — Pending |

---
*Last updated: 2026-01-31 after web app pivot*
