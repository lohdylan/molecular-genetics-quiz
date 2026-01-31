---
phase: "05-study-modes"
plan: "01"
subsystem: "ui/quiz-modes"
tags: [study-modes, topic-filter, ui, home-screen]

dependency-graph:
  requires:
    - "04-gamification"  # Uses gamificationState for topic mastery
  provides:
    - "mode-selection-ui"
    - "topic-filter-quiz"
    - "home-screen"
  affects:
    - "05-02"  # Flashcards and weak spots modes

tech-stack:
  added: []
  patterns:
    - "mode-state-tracking"
    - "modal-overlay-pattern"
    - "filter-then-shuffle"

file-tracking:
  key-files:
    created: []
    modified:
      - web/index.html

decisions:
  - id: "MODE-01"
    choice: "Home screen as default view"
    rationale: "Users should choose study mode before starting, not auto-start quiz"
  - id: "MODE-02"
    choice: "Topic filter uses existing questions array"
    rationale: "No duplication, questions.filter(q => q.topic === topic) is simple and efficient"
  - id: "MODE-03"
    choice: "Mode state tracked in JavaScript variables"
    rationale: "currentMode and currentTopic enable mode-specific behavior without complex state management"

metrics:
  duration: "15 minutes"
  completed: "2026-01-31"
---

# Phase 5 Plan 01: Study Mode Selection Summary

**One-liner:** Home screen with mode cards enabling topic-specific quiz filtering using mastery-aware topic selector modal.

## What Was Built

### Home Screen UI
- Mode selection home screen displayed on initial load
- "Start Full Quiz" button for standard mode (all 49 questions)
- Three mode cards: By Topic, Weak Spots, Flashcards
- Gamification bar (XP, level, streak) visible on home screen
- Mobile responsive layout (stacked cards on small screens)

### Topic Filter Quiz Mode
- Topic selector modal with all unique topics from question bank
- Each topic shows: question count and mastery percentage
- Mastery color coding: green (>=80%), purple (70-79%), orange (<70%)
- Clicking topic starts quiz with only that topic's questions
- Quiz header shows "Topic: {name}" indicator when in topic mode

### Navigation & Mode Management
- `currentMode` and `currentTopic` state variables for mode tracking
- "Back to Home" button in quiz header
- "Try Again" restarts same topic when in topic mode
- Stats/Achievements screens return to home screen when closed

## Key Implementation Details

```javascript
// Mode state tracking
let currentMode = 'standard'; // 'standard', 'topic', 'weak', 'flashcard'
let currentTopic = null;

// Topic filtering
function startTopicQuiz(topic) {
  currentMode = 'topic';
  currentTopic = topic;
  shuffledQuestions = shuffleArray(questions.filter(q => q.topic === topic));
  // ... start quiz
}

// Topic list generation
const topics = [...new Set(questions.map(q => q.topic))].sort();
```

## Verification Results

| Criteria | Status |
|----------|--------|
| Home screen shows mode selection UI | Pass |
| "Start Full Quiz" works (all questions) | Pass |
| "By Topic" opens modal with topic list | Pass |
| Topic list shows counts and mastery | Pass |
| Selecting topic starts filtered quiz | Pass |
| Quiz header indicates current topic | Pass |
| Try Again restarts same topic | Pass |
| Back to Home navigation works | Pass |
| Mobile responsive layout | Pass |

## Commits

| Hash | Type | Description |
|------|------|-------------|
| 816b095 | feat | Add mode selection home screen with topic filter quiz |

## Deviations from Plan

None - plan executed exactly as written. Both tasks were implemented in a single cohesive commit since the home screen UI and topic filter functionality are tightly coupled and share common components.

## Files Modified

- `web/index.html` - Added ~600 lines for CSS styles, HTML structure, and JavaScript functions

## Next Phase Readiness

**Ready for 05-02 (Flashcards & Weak Spots):**
- Mode infrastructure in place (`currentMode`, `currentTopic`)
- Placeholder functions ready: `startFlashcards()`, `startWeakSpotsQuiz()`
- Weak spots mode already partially functional (filters weak topics < 70% mastery)
- Home screen card layout supports additional modes
