---
publish: true
title: "Career Dashboards"
type: synthesis
status: evergreen
concept: "career-dashboards"
tags: [career, dashboard, dataview, job-hunt]
sources: []
related:
  - [[Dashboards]]
  - [[Job Application Tracker]]
  - [[Interview Preparation]]
  - [[Portfolio Development]]
  - [[Networking CRM]]
created: "2026-11-18"
updated: "2026-11-18"
last_reviewed: ""
---

# Career Dashboards

Central collection of all career-focused Dataview queries.

## Job Application Pipeline (Kanban)

```dataview
TABLE WITHOUT ID
  file.link as Application,
  company as Company,
  role as Role,
  status as Status,
  applied_date as Applied,
  next_action as NextAction
FROM "wiki/30-project"
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

## STAR Stories Review Queue

```dataview
TABLE WITHOUT ID
  file.link as Story,
  category as Category,
  status as Status,
  last_reviewed as LastReviewed,
  company_target as TargetCompany,
  role_target as TargetRole
FROM "wiki/20-evergreen"
WHERE type = "evergreen" AND concept = "interview-star-story"
SORT last_reviewed ASC
```

## Company Research Status

```dataview
TABLE WITHOUT ID
  file.link as Company,
  priority as Priority,
  status as Status,
  salary-range as SalaryRange,
  length(roles-of-interest) as RolesTracked
FROM "wiki/50-career/company-research"
WHERE type = "company-research"
SORT priority DESC, company ASC
```

## Contacts Needing Follow-Up (30+ Days)

```dataview
TABLE WITHOUT ID
  file.link as Contact,
  role as Role,
  company as Company,
  relationship as Relationship,
  strength as Strength,
  last_contact as LastContact,
  next_action as NextAction
FROM "wiki/60-people"
WHERE type = "person"
AND last_contact < date(today) - dur(30 days)
SORT last_contact ASC
```

## Contacts by Relationship Strength

```dataview
TABLE WITHOUT ID
  file.link as Contact,
  company as Company,
  role as Role,
  relationship as Relationship,
  strength as Strength,
  last_contact as LastContact,
  next_followup as NextFollowup
FROM "wiki/60-people"
WHERE type = "person"
SORT 
  CASE strength
    WHEN "strong" THEN 1
    WHEN "medium" THEN 2
    WHEN "weak" THEN 3
    ELSE 4 END,
  last_contact ASC
```

## Target Company Network Map

```dataview
TABLE WITHOUT ID
  file.link as Contact,
  company as Company,
  relationship as Relationship,
  strength as Strength,
  "ðŸ”— " + join(map(related, (r) => "[[" + r + "]]"), ", ") as Connections
FROM "wiki/60-people"
WHERE type = "person"
AND contains(company, "Google") OR contains(company, "Microsoft") OR contains(company, "Amazon") OR contains(company, "Meta") OR contains(company, "Anthropic") OR contains(company, "Stripe") OR contains(company, "Vercel") OR contains(company, "Linear") OR contains(company, "Databricks") OR contains(company, "Snowflake")
SORT company ASC, strength DESC
```

## Application Metrics Summary

```dataview
TABLE WITHOUT ID
  length(rows) as TotalApplications,
  length(filter(rows, (r) => r.status = "interviewing")) as Interviewing,
  length(filter(rows, (r) => r.status = "screening")) as Screening,
  length(filter(rows, (r) => r.status = "applied")) as Applied,
  length(filter(rows, (r) => r.status = "offer")) as Offers,
  length(filter(rows, (r) => r.status = "accepted")) as Accepted,
  length(filter(rows, (r) => r.status = "rejected")) as Rejected,
  length(filter(rows, (r) => r.status = "wishlist")) as Wishlist
FROM "wiki/30-project"
WHERE type = "project" AND contains(tags, "job-application")
GROUP BY true
```

## Interview Prep Progress

```dataview
TABLE WITHOUT ID
  file.link as Area,
  length(rows) as Items,
  length(filter(rows, (r) => contains(r, "[x]"))) as Completed,
  round(length(filter(rows, (r) => contains(r, "[x]"))) / length(rows) * 100) + "%" as Progress
FROM "wiki/30-project/interview-preparation.md"
WHERE file.name = "interview-preparation"
FLATTEN list("DSA", "System Design", "Domain-Specific", "Company Research") as Area
GROUP BY Area
```

## Portfolio Case Studies Status

```dataview
TABLE WITHOUT ID
  file.link as CaseStudy,
  status as Status,
  skills_demonstrated as Skills,
  target_publish_date as TargetDate
FROM "wiki/30-project"
WHERE type = "project" AND contains(tags, "case-study")
SORT target_publish_date ASC
```

## Weekly Career Metrics

```dataview
TABLE WITHOUT ID
  "This Week" as Period,
  length(filter(rows, (r) => r.applied_date >= date(today) - dur(7 days))) as ApplicationsThisWeek,
  length(filter(rows, (r) => r.last_contact >= date(today) - dur(7 days))) as ContactsThisWeek,
  length(filter(rows, (r) => r.last_reviewed >= date(today) - dur(7 days))) as STARReviewedThisWeek
FROM "wiki/30-project"
WHERE type = "project" AND contains(tags, "job-application")
GROUP BY true
```

