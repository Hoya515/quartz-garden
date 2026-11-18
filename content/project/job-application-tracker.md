---
publish: true
title: "Job Application Tracker"
type: project
status: active
priority: high
para: project
concept: "career-job-tracking"
tags: [career, job-hunt, tracking, kanban]
sources: []
related:
  - [[Interview Preparation]]
  - [[Portfolio Development]]
  - [[Networking CRM]]
owner: "jmclo"
stakeholders: []
due: ""
created: "2026-11-18"
updated: "2026-11-18"
last_reviewed: "2026-11-18"
---

# Job Application Tracker

## Overview
Track all job applications through the pipeline: Wishlist â†’ Applied â†’ Screening â†’ Interviewing â†’ Offer â†’ Accepted/Rejected.

## Kanban Board
```dataview
TABLE WITHOUT ID
  file.link as Application,
  company as Company,
  role as Role,
  status as Status,
  applied_date as Applied,
  next_action as NextAction
FROM "wiki"
WHERE type = "project" AND contains(tags, "job-application")
SORT 
  CASE status
    WHEN "interviewing" THEN 1
    WHEN "screening" THEN 2
    WHEN "applied" THEN 3
    WHEN "offer" THEN 4
    WHEN "wishlist" THEN 5
    ELSE 6 END,
  applied_date ASC
```

## Sankey Pipeline (Visual)
*Use Job Application Tracker plugin for native Sankey diagram*

## Metrics
- **Total Applications**: 
- **Response Rate**: 
- **Interview Rate**: 
- **Offer Rate**: 
- **Avg Time to Offer**: 

## Pipeline Stages

### ðŸŽ¯ Wishlist
Target companies/roles not yet applied to.

### ðŸ“ Applied
Submitted applications awaiting response.

### ðŸ” Screening
Phone screens, recruiter calls, take-home assessments.

### ðŸŽ¤ Interviewing
Technical interviews, system design, behavioral rounds.

### ðŸ’° Offer
Negotiation, decision, acceptance.

### âœ… Accepted / âŒ Rejected / ðŸ‘» Ghosted / â†©ï¸ Withdrawn
Final outcomes.

## Related
- [[Interview Preparation]] â€” STAR stories, technical prep per application
- [[Portfolio Development]] â€” Case studies to reference in interviews
- [[Networking CRM]] â€” Recruiter contacts per application

## Next Actions
- [ ] Install Job Application Tracker plugin
- [ ] Create application notes for target companies
- [ ] Set up Kanban board in Tasks Kanban
- [ ] Add salary ranges and target compensation per role

