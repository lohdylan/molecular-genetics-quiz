# Phase 4: Gamification - Context

**Gathered:** 2026-01-31
**Status:** Ready for planning

<domain>
## Phase Boundary

User earns XP, levels up, maintains streaks, and unlocks achievements. Includes progress visualization with topic mastery tracking. Study modes (topic filtering, weak spot focus, flashcards) are a separate phase.

</domain>

<decisions>
## Implementation Decisions

### XP & Leveling
- +10 XP base for each correct answer
- Streak bonus: +5 XP per consecutive correct answer (3-streak = +15 bonus, 5-streak = +25 bonus)
- Linear level progression: 100 XP per level (Level 1 = 100 XP, Level 10 = 1000 XP total)
- Display: Top bar with level + XP progress bar always visible during quiz

### Streaks & Daily Engagement
- Streak requirement: Answer at least 10 questions per day to maintain streak
- Streak break: Reset to 0, start fresh (no freezes or decay)
- Visual: Fire icon with number (e.g., "7 day streak") — Duolingo-style
- Day reset: Midnight local time (browser timezone)

### Achievements & Unlocks
- Achievement types: Milestones + topic mastery badges
  - Milestones: First quiz, 100 questions, 7-day streak, etc.
  - Mastery: Topic-specific badges ("DNA Expert", "Protein Pro")
- Notification: Toast popup that auto-dismisses after 3-4 seconds
- Display: Dedicated achievements page showing all badges (earned and locked)
- Locked achievements: Show requirements ("Complete 50 questions") — clear goals to chase

### Progress Visualization
- Topic mastery: Progress bars per topic (no percentages shown)
- Weak topic highlighting: Red/orange color coding for topics < 70%
- Stats dashboard: Dedicated stats page with total questions, accuracy %, time studied
- Time range: All-time stats only (lifetime, always growing)

### Claude's Discretion
- Exact toast animation timing and style
- Specific milestone thresholds (which numbers trigger achievements)
- Progress bar colors and styling
- Stats page layout and chart types

</decisions>

<specifics>
## Specific Ideas

- Fire icon for streaks — Duolingo-inspired visual language
- Clear achievement requirements visible for locked badges — gives users goals to chase

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 04-gamification*
*Context gathered: 2026-01-31*
