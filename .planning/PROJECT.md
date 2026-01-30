# Molecular Genetics Study Tool

## What This Is

An active recall study tool for molecular genetics exam preparation. Quizzes the user on concepts, tracks weak spots, and uses spaced repetition to reinforce learning. Built for a student with an exam in 2 days.

## Core Value

Help the user actively recall and retain molecular genetics concepts through testing, not passive review.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Quiz system that asks questions and checks answers
- [ ] Flashcard system for concept review
- [ ] Weak spot tracking to identify struggling areas
- [ ] Question bank loaded from provided quiz content
- [ ] Immediate feedback with explanations

### Out of Scope

- User accounts / authentication — single user, local tool
- Mobile app — CLI/web is sufficient for 2 days
- Spaced repetition algorithm complexity — simple "seen/correct/incorrect" tracking is enough
- Content creation UI — questions loaded from data files

## Context

**Exam Details:**
- 36 multiple choice questions
- Covers Unit 1: DNA structure, replication, transcription, translation, gene regulation
- Monday exam (2 days away)

**Content Sources:**
- Quiz 1: 16 questions (DNA structure, replication, PCR, Sanger sequencing)
- Quiz 2: 17 questions (transcription, translation, gene regulation, lac operon, mutations, RNAi)
- Practice Problems PDF: conceptual questions with diagrams
- Lecture transcript: professor's explanations and emphasis points

**Key Topics:**
1. DNA structure (bases, backbone, 5'/3' ends, major/minor grooves, chromatin)
2. DNA replication (enzymes, leading/lagging, Okazaki fragments, proofreading, telomerase)
3. PCR (primer design, exponential amplification, Taq polymerase)
4. Sanger sequencing (ddNTPs, chain termination, gel electrophoresis)
5. Transcription vs replication (similarities/differences)
6. Translation (start/stop codons, reading frames, codon table usage)
7. Gene regulation (cis/trans elements, transcription factors)
8. Lac operon (CAP, repressor, glucose/lactose conditions)
9. Mutations (silent, missense, nonsense)
10. RNA types and RNAi

**Common Mistakes (from professor):**
- PCR: primers on same strand, wrong direction analysis
- Translation: starting at beginning instead of AUG, taking complement of codons
- Mixing up introns/exons

## Constraints

- **Timeline**: Must be usable within hours, not days
- **Tech stack**: Simple — Python or web-based, no complex setup
- **Data**: Questions stored in JSON or similar for easy addition

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| CLI-based quiz tool | Fastest to build, user is technical | — Pending |

---
*Last updated: 2026-01-30 after initialization*
