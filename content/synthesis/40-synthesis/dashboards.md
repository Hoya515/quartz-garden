---
publish: true
title: "Dashboards"
type: synthesis
status: evergreen
concept: "dashboard-collection"
tags: [dashboard, dataview, para, review]
sources: []
related: []
para: area
created: "2026-11-18"
updated: "2026-11-18"
---

# Dataview Dashboards

Central collection of all dashboard queries for the second brain.

---

## ðŸ“‹ PARA Project Dashboard

**Active projects with priority, due dates, and progress**

```dataview
TABLE WITHOUT ID
  file.link as Project,
  priority as Priority,
  due as Due,
  status as Status,
  round(length(filter(file.tasks, (t) => t.status = "done")) / length(file.tasks) * 100) as Progress
FROM "wiki"
WHERE para = "project" AND status = "active"
SORT priority DESC, due ASC
```

---

## ðŸŽ¯ Skill Progress Dashboard

**Confidence and review status per skill domain**

```dataview
TABLE WITHOUT ID
  concept as Skill,
  length(rows) as Notes,
  round(average(confidence) * 100) / 100 as AvgConfidence,
  min(last_reviewed) as LastReviewed
FROM "wiki"
WHERE type = "evergreen" AND contains(tags, "skill")
GROUP BY concept
SORT AvgConfidence ASC
```

---

## â­ STAR Stories Review Queue

**Interview stories needing review (oldest first)**

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

---

## ðŸ’¼ Job Application Pipeline

**Kanban-style application tracking**

```dataview
TABLE WITHOUT ID
  file.link as Application,
  company as Company,
  role as Role,
  status as Status,
  applied_date as Applied,
  salary_range as Salary,
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

---

## ðŸ¤ Networking CRM - Follow-ups Due

**Contacts not contacted in 30+ days**

```dataview
TABLE WITHOUT ID
  file.link as Contact,
  role as Role,
  company as Company,
  relationship as Relationship,
  strength as Strength,
  last_contact as LastContact,
  next_action as NextAction
FROM "wiki"
WHERE type = "person"
AND last_contact < date(today) - dur(30 days)
SORT last_contact ASC
```

---

## ðŸŒ± Orphaned Wiki Notes

**Notes with no incoming links (need connections)**

```dataview
LIST FROM "wiki"
WHERE !contains(file.inlinks, file.link)
AND type != "daily"
```

---

## ðŸŒ± Seedling Notes Needing Review (>30 days)

**Early-stage notes stale for review**

```dataview
TABLE WITHOUT ID
  file.link as Note,
  status as Status,
  confidence as Confidence,
  last_reviewed as LastReviewed,
  concept as Concept
FROM "wiki"
WHERE status = "seedling" 
AND last_reviewed < date(today) - dur(30 days)
SORT last_reviewed ASC
```

---

## ðŸ“š Certification Progress

**Active certification projects**

```dataview
TABLE WITHOUT ID
  file.link as Certification,
  status as Status,
  due as Due,
  length(rows) as StudyNotes
FROM "wiki"
WHERE para = "project" AND contains(tags, "certification")
GROUP BY file.link, status, due
```

---

## ðŸ“Š Weekly Review Metrics

**Auto-computed weekly metrics**

```dataview
TABLE WITHOUT ID
  "Tasks Completed" as Metric,
  length(filter(rows, (r) => r.status = "done" AND r.completed >= date(today) - dur(7 days))) as Value
FROM #task
GROUP BY "Week"

UNION

TABLE WITHOUT ID
  "New Permanent Notes" as Metric,
  length(filter(rows, (r) => r.created >= date(today) - dur(7 days) AND r.type = "evergreen")) as Value
FROM "wiki"
GROUP BY "Week"

UNION

TABLE WITHOUT ID
  "SR Cards Reviewed" as Metric,
  length(filter(rows, (r) => r.reviewed >= date(today) - dur(7 days))) as Value
FROM #flashcard
GROUP BY "Week"
```

---

## ðŸ”— Knowledge Graph Bridge Nodes

**High-centrality notes connecting clusters**

```dataview
TABLE WITHOUT ID
  file.link as Note,
  length(file.outlinks) as Outgoing,
  length(file.inlinks) as Incoming,
  round((length(file.outlinks) + length(file.inlinks)) / 2) as Centrality
FROM "wiki"
WHERE type = "evergreen"
SORT Centrality DESC
LIMIT 20
```

---

## ðŸš€ Active Projects with Task Velocity

**Project health with completion rate**

```dataview
TABLE WITHOUT ID
  file.link as Project,
  priority as Priority,
  length(filter(file.tasks, (t) => t.status = "done")) as Done,
  length(filter(file.tasks, (t) => t.status != "done")) as Open,
  round(length(filter(file.tasks, (t) => t.status = "done")) / length(file.tasks) * 100) as Progress
FROM "wiki"
WHERE para = "project" AND status = "active"
SORT Progress ASC
```

---

## ðŸ“ Portfolio Case Studies Index

**Published case studies with ADRs and skills**

```dataview
TABLE WITHOUT ID
  file.link as CaseStudy,
  file.name as Title,
  length(rows.adr) as ADRs,
  skills_demonstrated as Skills
FROM "wiki"
WHERE contains(tags, "case-study") OR contains(tags, "portfolio")
FLATTEN related as adr
WHERE contains(adr, "ADR")
GROUP BY file.link, file.name, skills_demonstrated
```

---

## ðŸ“¥ Learning Queue (Sources to Process)

**Sources ingested but not yet synthesized**

```dataview
TABLE WITHOUT ID
  file.link as Source,
  source_type as Type,
  date_ingested as Ingested,
  tags as Topics
FROM "sources"
WHERE !contains(file.path, "processed")
SORT date_ingested ASC
```

---

## Usage

### As Bases (Editable Tables)
Create a note with:
```yaml
---
type: base
query: |
  TABLE ... FROM "wiki" WHERE ...
---
```

### In Periodic Notes
Embed in weekly/monthly review templates for live metrics.

### With Buttons Plugin
Add button to run Templater script that regenerates dashboards.

---

*Last updated: {{date}}*
*Auto-maintained â€” do not hand-edit query logic*

