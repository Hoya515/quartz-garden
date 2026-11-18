---

publish: true
title: "Portfolio Development"
type: project
status: active
priority: medium
para: project
concept: "career-portfolio"
tags: [career, portfolio, case-study, adr, digital-garden]
sources: []
related:
  - [[Job Application Tracker]]
  - [[Interview Preparation]]
  - [[Dashboards]]
owner: "jmclo"
stakeholders: []
due: ""
created: "2026-11-18"
updated: "2026-11-18"
last_reviewed: "2026-11-18"
---

# Portfolio Development

## Overview
Build a public portfolio from vault content: case studies, ADRs, published digital garden.

## Case Studies to Create
| Project | Status | ADRs | Skills | Target Publish Date |
|---------|--------|------|--------|---------------------|
| Obsidian Second Brain | ðŸ”„ In Progress | 0 | Python, Obsidian, MCP, Automation | 2026-12-01 |
| [Project 2] | | | | |
| [Project 3] | | | | |

## Case Study Template
Use `templates/adr.md` for Architecture Decision Records within each case study.

## Portfolio Case Studies Index
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

## Digital Garden Publishing (Quartz)
1. Fork `sosiristseng/template-quartz` or `jackyzha0/quartz`
2. Configure `quartz.config.ts`:
   - Enable graph view, backlinks, tag pages
   - Add custom components for skill trees
3. Sync via **Quartz Syncer** plugin (one-click publish) or GitHub Actions
4. Customize: Add skill progression visualization component

## Publish Criteria
- [ ] Case study has problem statement, architecture, challenges, metrics
- [ ] At least 2 ADRs documenting key decisions
- [ ] Skills demonstrated tags match resume keywords
- [ ] Reflection section with "what I'd change"

## Next Actions
- [ ] Complete Obsidian Second Brain case study
- [ ] Set up Quartz digital garden
- [ ] Configure Quartz Syncer plugin
- [ ] Create 2 more case studies from past projects
- [ ] Add portfolio link to resume and LinkedIn

