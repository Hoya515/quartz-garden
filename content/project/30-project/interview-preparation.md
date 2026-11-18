---
publish: true
title: "Interview Preparation"
type: project
status: active
priority: high
para: project
concept: "career-interview-prep"
tags: [career, interview, star, technical, behavioral]
sources: []
related:
  - [[Job Application Tracker]]
  - [[Portfolio Development]]
  - [[STAR Story: Failure]]
  - [[STAR Story: Learn Quickly]]
  - [[STAR Story: Team Pressure]]
  - [[STAR Story: Deadlines]]
  - [[STAR Story: Proudest Project]]
  - [[STAR Story: Weakness]]
owner: "jmclo"
stakeholders: []
due: ""
created: "2026-11-18"
updated: "2026-11-18"
last_reviewed: "2026-11-18"
---

# Interview Preparation

## Overview
Comprehensive interview preparation: STAR behavioral stories, technical questions, system design, company research.

## 6 Core STAR Stories (Behavioral)

| Category | Story | Status | Last Reviewed | Target Companies |
|----------|-------|--------|---------------|------------------|
| **Failure/Mistake** | [[STAR Story: Failure]] | seedling | | |
| **Learn Quickly** | [[STAR Story: Learn Quickly]] | seedling | | |
| **Team Under Pressure** | [[STAR Story: Team Pressure]] | seedling | | |
| **Pressure/Deadlines** | [[STAR Story: Deadlines]] | seedling | | |
| **Proudest Project** | [[STAR Story: Proudest Project]] | seedling | | |
| **Biggest Weakness** | [[STAR Story: Weakness]] | seedling | | |

## STAR Stories Review Queue
```dataview
TABLE WITHOUT ID
  file.link as Story,
  category as Category,
  status as Status,
  last_reviewed as LastReviewed,
  company_target as TargetCompany
FROM "wiki"
WHERE type = "evergreen" AND concept = "interview-star-story"
SORT last_reviewed ASC
```

## Technical Preparation

### Data Structures & Algorithms
- [ ] Arrays & Strings
- [ ] Linked Lists
- [ ] Trees & Graphs
- [ ] Dynamic Programming
- [ ] Sorting & Searching
- [ ] Heaps & Priority Queues

### System Design
- [ ] Scalability Patterns
- [ ] Database Design (SQL/NoSQL)
- [ ] Caching Strategies
- [ ] Message Queues
- [ ] API Design (REST/GraphQL)
- [ ] Microservices vs Monolith

### Domain-Specific
- [ ] Frontend Architecture
- [ ] Backend Services
- [ ] DevOps/Infrastructure
- [ ] Security Fundamentals

## Company Research Template
Per target company, create `wiki/career/company-{name}.md`:
- Mission, values, recent news
- Tech stack, architecture blog posts
- Interview process (levels, rounds, focus)
- Compensation bands (levels.fyi, Glassdoor)
- Team structure, hiring manager background
- Questions for interviewers

## Spaced Repetition Integration
- **Better Recall** decks: `#flashcards/interview/behavioral`, `#flashcards/interview/technical`
- Review daily: 15 min behavioral, 15 min technical
- FSRS algorithm optimizes intervals

## Next Actions
- [ ] Create 6 STAR story notes from template
- [ ] Set up Better Recall with interview decks
- [ ] Create company research notes for top 10 targets
- [ ] Schedule mock interviews
- [ ] Build technical flashcard deck

