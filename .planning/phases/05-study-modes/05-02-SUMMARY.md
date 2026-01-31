---
phase: "05-study-modes"
plan: "02"
subsystem: "ui/study-modes"
tags: [weak-spots, flashcards, question-tracking, study-modes]

dependency-graph:
  requires:
    - "05-01"  # Home screen and mode infrastructure
  provides:
    - "weak-spots-mode"
    - "flashcard-mode"
    - "question-level-tracking"
  affects: []

tech-stack:
  added: []
  patterns:
    - "question-history-tracking"
    - "css-3d-flip-animation"
    - "keyboard-event-handling"
    - "touch-detection"

file-tracking:
  key-files:
    created: []
    modified:
      - web/index.html

decisions:
  - id: "MODE-03"
    choice: "Weak spots defined as never answered correctly OR never attempted"
    rationale: "Questions with 0 correct answers are problem areas regardless of attempt count"
  - id: "MODE-04"
    choice: "Flashcard shows only correct answer text, not full option"
    rationale: "Cleaner display - users don't need A/B/C/D prefix or explanation when studying"
  - id: "MODE-05"
    choice: "Keyboard support for flashcards (Space, Arrows, Escape)"
    rationale: "Power users on desktop benefit from keyboard navigation"

metrics:
  duration: "4 minutes"
  completed: "2026-01-31"
---

# Phase 5 Plan 02: Weak Spots & Flashcard Modes Summary

**One-liner:** Question-level tracking enables weak spots review mode with priority sorting; flashcard mode features 3D flip animation with keyboard/touch support.

## What Was Built

### Weak Spots Review Mode
- `questionHistory` added to gamificationState for per-question tracking
- Each question tracks: `{ attempts: N, correct: N }`
- `getWeakQuestions()` filters questions never answered correctly or never attempted
- Weak questions sorted by weakness (never attempted first, then by failure count)
- Session capped at 15 questions, shuffled for variety
- Home screen shows "X questions to review" or "All caught up!"
- Congratulations message when no weak spots exist
- Final score screen shows "Weak Spots Review Complete!" with appropriate messaging

### Flashcard Study Mode
- Full-screen flashcard interface with 3D flip animation
- Question displayed on front with topic and hint text
- Correct answer (text only, no "A) " prefix) on back
- CSS `transform: rotateY(180deg)` with `preserve-3d` for flip effect
- Touch detection: "Tap to reveal" vs "Press Space to reveal"
- Keyboard controls: Space (flip), Left/Right arrows (navigate), Escape (exit)
- Previous/Next buttons for mouse users
- Counter shows "Card X of Y"
- Mobile responsive styling

## Key Implementation Details

```javascript
// Question history tracking
gamificationState.questionHistory = {
  "q1": { attempts: 3, correct: 1 },
  "q2": { attempts: 2, correct: 0 }  // Never got it right - weak!
};

// Weak spot detection
function getWeakQuestions() {
  return questions.filter(q => {
    const qHistory = history[q.id];
    if (!qHistory) return true;           // Never attempted
    if (qHistory.correct === 0) return true; // Never correct
    return false;
  });
}

// Flashcard flip with 3D CSS
.flashcard.flipped {
  transform: rotateY(180deg);
}
```

## Verification Results

| Criteria | Status |
|----------|--------|
| Weak spots count on home screen | Pass |
| Weak mode filters by question history | Pass |
| Session capped at 15 questions | Pass |
| Congratulations when no weak spots | Pass |
| Flashcard flip animation works | Pass |
| Spacebar reveals answer (desktop) | Pass |
| Tap reveals answer (mobile) | Pass |
| Arrow key navigation | Pass |
| Previous/Next buttons | Pass |
| Exit returns to home | Pass |
| Mobile responsive | Pass |

## Commits

| Hash | Type | Description |
|------|------|-------------|
| b60b726 | feat | Implement weak spots review mode with question-level tracking |
| 54c4ea4 | feat | Implement flashcard study mode with tap-to-flip interaction |

## Deviations from Plan

None - plan executed exactly as written.

## Files Modified

- `web/index.html` - Added ~370 lines for CSS styles, HTML structure, and JavaScript functions

## Next Phase Readiness

**Phase 5 Complete:**
- All study modes implemented: Standard, Topic, Weak Spots, Flashcards
- Question-level tracking persists to localStorage
- Home screen provides mode selection
- All gamification features (XP, achievements) work with all modes
