# Requirements: Molecular Genetics Study Tool (Web App)

**Defined:** 2026-01-31
**Core Value:** Engaging gamified testing for active recall

## v1 Requirements

### Core Quiz (Web)

- [ ] **WEB-01**: Single-page web app loads in browser
- [ ] **WEB-02**: Questions load from JSON data file
- [ ] **WEB-03**: Display question with multiple choice options
- [ ] **WEB-04**: User clicks option to answer
- [ ] **WEB-05**: Show correct/incorrect feedback with explanation
- [ ] **WEB-06**: Progress bar shows quiz completion
- [ ] **WEB-07**: Final score screen at end of quiz

### Gamification

- [x] **GAME-01**: Earn XP points for correct answers (10 XP each)
- [x] **GAME-02**: Bonus XP for streaks (consecutive correct)
- [x] **GAME-03**: Display current level based on total XP
- [x] **GAME-04**: Daily streak counter (days studied in a row)
- [x] **GAME-05**: Visual level-up animation/notification

### Achievements

- [x] **ACH-01**: Achievement badges for milestones
- [x] **ACH-02**: "First Quiz" badge - complete first quiz
- [x] **ACH-03**: "Perfect Score" badge - 100% on a quiz
- [x] **ACH-04**: "Hot Streak" badge - 10 correct in a row
- [x] **ACH-05**: "Topic Master" badge - 100% on a topic
- [x] **ACH-06**: Achievement gallery/display screen

### Progress Tracking

- [x] **PROG-01**: Track correct/incorrect per question
- [x] **PROG-02**: Show mastery % per topic (DNA Structure, PCR, etc.)
- [x] **PROG-03**: Visual progress bars for each topic
- [x] **PROG-04**: Identify weak topics (< 70% correct)
- [x] **PROG-05**: History of quiz scores over time

### Data Persistence

- [ ] **DATA-01**: Save all progress to localStorage
- [ ] **DATA-02**: Load saved progress on page load
- [ ] **DATA-03**: Reset progress option

### Study Modes

- [ ] **MODE-01**: Full quiz mode (all questions, randomized)
- [ ] **MODE-02**: Topic-specific quiz (filter by topic)
- [ ] **MODE-03**: Weak spots review (prioritize missed questions)
- [ ] **MODE-04**: Flashcard mode (reveal answer on click)

### UI/UX

- [ ] **UI-01**: Clean, modern design with good typography
- [ ] **UI-02**: Mobile-responsive layout
- [ ] **UI-03**: Smooth animations for feedback/transitions
- [ ] **UI-04**: Color scheme (green=correct, red=incorrect)
- [ ] **UI-05**: Dashboard/home screen with stats

## v2 Requirements (Future)

- Timed quiz mode
- Compete with friends (shareable scores)
- Sound effects
- Dark mode toggle
- More question banks

## Out of Scope

| Feature | Reason |
|---------|--------|
| User accounts | localStorage sufficient, no server |
| Backend/database | Fully client-side app |
| Native mobile app | Responsive web works on mobile |
| Content editor | Questions in JSON file |
| Complex algorithms | Simple tracking works |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| WEB-01 to WEB-07 | Phase 3 | Complete |
| GAME-01 to GAME-05 | Phase 4 | Complete |
| ACH-01 to ACH-06 | Phase 4 | Complete |
| PROG-01 to PROG-05 | Phase 4 | Complete |
| DATA-01 to DATA-03 | Phase 3 | Complete |
| MODE-01 to MODE-04 | Phase 5 | Pending |
| UI-01 to UI-05 | Phase 3 | Complete |

**Coverage:**
- v1 requirements: 32 total
- Mapped to phases: 32
- Unmapped: 0

---
*Requirements defined: 2026-01-31*
