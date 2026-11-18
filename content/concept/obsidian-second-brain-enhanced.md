---

publish: true
title: "Obsidian Second Brain â€” Enhanced Architecture"
type: concept
status: evergreen
concept: "obsidian-second-brain-enhanced"
tags: [obsidian, second-brain, architecture, automation, career]
sources:
  - [[Obsidian Second Brain Architecture]]
  - [[Vault Mining Pattern]]
  - [[Dashboards]]
related:
  - [[Obsidian Second Brain Integration]]
  - [[Job Application Tracker]]
  - [[Interview Preparation]]
  - [[Portfolio Development]]
para: area
created: "2026-11-18"
updated: "2026-11-18"
last_reviewed: "2026-11-18"
confidence: 0.9
---

# Obsidian Second Brain â€” Enhanced Architecture

## Overview
Enhanced three-layer vault with career-focused automation, spaced repetition, and publishing pipeline.

## Architecture Layers

### Layer 1: Sources (Immutable)
```
sources/
â”œâ”€â”€ articles/          # Web articles, blog posts
â”œâ”€â”€ youtube/           # Video transcripts, timestamps
â”œâ”€â”€ x/                 # Twitter threads, X posts
â”œâ”€â”€ podcasts/          # Episode notes, highlights
â”œâ”€â”€ papers/            # Academic papers, PDFs
â””â”€â”€ books/             # Book notes, highlights (Readwise sync)
```

### Layer 2: Inbox (Human-Only Capture)
```
inbox/
â”œâ”€â”€ YYYY-MM-DD.md      # Daily notes (Periodic Notes)
â”œâ”€â”€ fleeting/          # Quick captures (QuickAdd)
â”œâ”€â”€ literature/        # Synthesized source notes
â””â”€â”€ meeting/           # Meeting notes
```

### Layer 3: Wiki (LLM-Written Only)
```
wiki/
â”œâ”€â”€ concepts/          # Atomic evergreen notes
â”œâ”€â”€ projects/          # Active projects (PARA: project)
â”œâ”€â”€ people/            # CRM contacts (PARA: resource)
â”œâ”€â”€ synthesis/         # Dashboards, MOCs, reviews (PARA: area)
â””â”€â”€ career/            # Career-specific subfolder
    â”œâ”€â”€ star-stories/  # STAR method interview stories
    â”œâ”€â”€ company-research/
    â”œâ”€â”€ certifications/
    â””â”€â”€ portfolio/     # Case studies, ADRs
```

## Enhanced Frontmatter Schema

Every wiki note has:
```yaml
type: concept|project|person|synthesis|adr|evergreen
status: seedling|budding|evergreen|active|inactive|done|proposed|accepted|superseded|deprecated
para: project|area|resource|archive
concept: ""              # Atomic concept identifier
confidence: 0.8          # 0-1 for knowledge notes
tags: []
sources: []              # Wikilinks to sources/
related: []              # Wikilinks to other wiki pages
created: YYYY-MM-DD
updated: YYYY-MM-DD
last_reviewed: ""
```

## Automation Pipeline

| Trigger | Tool | Action |
|---------|------|--------|
| New source URL | QuickAdd + Web Clipper | Save to sources/, create literature note |
| Daily note created | Periodic Notes + Templater | Roll up tasks, metrics, priorities |
| New `#skill` tag | QuickAdd + Better Recall | Create SR deck for skill |
| Task completed | Tasks Plugin | Update project progress, skill metrics |
| Weekly review | Periodic Notes + Dataview | Auto-generate metrics dashboard |
| Graph analysis run | Knowledge Graph Analysis | Flag orphans, find bridge nodes |

## Plugin Stack (21 Plugins)

### Core (Week 1)
1. Periodic Notes (core)
2. Tasks
3. Dataview
4. QuickAdd
5. Templater

### Intelligence (Week 1-2)
6. Better Recall (FSRS/SM-2)
7. Knowledge Graph Analysis
8. Tasks Kanban

### Infrastructure (Week 2)
9. Obsidian Git
10. Digital Garden / Quartz Syncer

### Advanced (Week 2-3)
11. obsidian-local-rest-api (MCP)
12. ShellCommands
13. Semantic Auto-Linker
14. Excalidraw
15. Person Network
16. Contacts
17. Job Application Tracker
18. MADR Author
19. Project Tracker
20. Vault Linker Auto
21. Multi Backup

## Career Integration

### Job Hunt Pipeline
```
Wishlist â†’ Applied â†’ Screening â†’ Interviewing â†’ Offer â†’ Accepted
```
Tracked via **Job Application Tracker** plugin + Dataview dashboards.

### Interview Prep
- **6 STAR stories** as evergreen notes with `#flashcards/interview/behavioral`
- **Technical decks** in Better Recall: `#flashcards/cs/algorithms`, `#flashcards/cs/system-design`
- **Company research** notes per target

### Portfolio
- **Case studies** from projects with ADRs
- **Skill trees** visualization in garden

### Networking CRM
- **Person Network** plugin for visual relationship mapping
- **Contacts** plugin for sidebar quick access
- **Dataview** dashboards for follow-ups

## Key Dataview Dashboards
(See `wiki/synthesis/dashboards.md` for 15 queries)

1. PARA Projects â€” Active projects with progress
2. Skill Progress â€” Confidence + review status
3. STAR Stories â€” Review queue (spaced repetition)
4. Job Pipeline â€” Kanban + metrics
5. Network CRM â€” Contacts needing follow-up
6. Orphans/Seedlings â€” Wiki health
7. Weekly Metrics â€” Tasks, notes, SR cards

## Review Cadence

| Cadence | Trigger | Duration | Focus |
|---------|---------|----------|-------|
| Daily | `/today` | 10 min | Tasks, priorities, capture |
| Weekly | `/weekly-review` | 30 min | Metrics, STAR review, graph health |
| Monthly | Periodic Note | 60 min | Project retros, skill gaps, network |
| Quarterly | Periodic Note | 2 hr | Career trajectory, portfolio, strategy |

## Next Evolution (Month 2+)
- [ ] MCP server for external agent access
- [ ] LLM synthesis (Ollama + ShellCommands)
- [ ] Semantic auto-linking
- [ ] Team collaboration (LiveSync/Git)
- [ ] Advanced Excalidraw diagrams for architecture


