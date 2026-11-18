---
publish: true
title: "Networking CRM"
type: project
status: active
priority: medium
para: project
concept: "career-networking"
tags: [career, networking, crm, contacts, relationships]
sources: []
related:
  - [[Job Application Tracker]]
  - [[Interview Preparation]]
  - [[Portfolio Development]]
owner: "jmclo"
stakeholders: []
due: ""
created: "2026-11-18"
updated: "2026-11-18"
last_reviewed: "2026-11-18"
---

# Networking CRM

## Overview
Manage professional relationships: mentors, recruiters, alumni, peers, hiring managers. Visualize paths to decision-makers at target companies.

## Contact Dashboard
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

## Relationship Types
| Type | Count | Strategy |
|------|-------|----------|
| **Mentor** | | Monthly check-ins, seek guidance |
| **Recruiter** | | Quarterly updates, share wins |
| **Alumni** | | Semesterly catch-ups, referrals |
| **Peer** | | Casual, mutual support |
| **Hiring Manager** | | Targeted, value-first outreach |

## Person Network Visualization
*Use **Person Network** plugin for orbital/planetary layout*

- **Inner ring**: Strong ties (mentors, close peers)
- **Middle ring**: Active relationships (recruiters, alumni)
- **Outer ring**: Weak ties (LinkedIn connections, cold contacts)
- **Company clusters**: Group by organization

## Follow-Up System
1. **Every interaction** â†’ Log in contact note Interactions table
2. **Next action** â†’ Set `next_action` and `last_contact` date
3. **Weekly review** â†’ Run dashboard, complete overdue follow-ups
4. **Monthly** â†’ Reach out to 5+ dormant contacts

## Target Company Network Mapping
For each target company:
- Identify: Hiring managers, team leads, alumni, recruiters
- Map: Who knows whom (Person Network edges)
- Strategy: Warm intro path vs. cold outreach

## Templates
- New contact: `templates/person-contact.md`
- Outreach emails: QuickAdd macro with variables

## Next Actions
- [ ] Install Person Network + Contacts plugins
- [ ] Import LinkedIn contacts (CSV â†’ person notes)
- [ ] Create contact notes for 10 key relationships
- [ ] Set up weekly follow-up dashboard in daily note
- [ ] Map network for top 5 target companies

