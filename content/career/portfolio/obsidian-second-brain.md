---
publish: true
title: "Obsidian Second Brain â€” Personal Knowledge Management System"
type: case-study
status: published
project: "Obsidian Second Brain"
role: "Solo Developer / Architect"
duration: "2026-11 (ongoing)"
tags: [portfolio, case-study, knowledge-management, obsidian, automation]
skills: ["System Architecture", "TypeScript", "Node.js", "Dataview", "CI/CD", "MCP", "Spaced Repetition", "Knowledge Management"]
technologies: ["Obsidian", "TypeScript", "Node.js", "Dataview", "QuickAdd", "Templater", "Better Recall", "Quartz", "GitHub Actions", "MCP"]
impact: "Built a comprehensive three-layer second brain (sources/inbox/wiki) with 21-plugin automation pipeline, career workflows, and digital garden deployment"
metrics:
  - name: "Vault Pages"
    before: "0"
    after: "30+"
    change: "+30"
  - name: "Automation Macros"
    before: "0"
    after: "7"
    change: "+7"
  - name: "Spaced Repetition Decks"
    before: "0"
    after: "4 (21 cards)"
    change: "+21"
  - name: "CI/CD Pipeline Stages"
    before: "0"
    after: "6"
    change: "+6"
  - name: "STAR Stories"
    before: "0"
    after: "9"
    change: "+9"
  - name: "MCP Endpoints"
    before: "0"
    after: "7"
    change: "+7"
adr-refs:
  - "ADR-001: Three-Layer Architecture (Sources â†’ Inbox â†’ Wiki)"
  - "ADR-002: PARA via Frontmatter Properties"
  - "ADR-003: FSRS over SM-2 for Spaced Repetition"
  - "ADR-004: REST API over MCP stdio on Windows"
  - "ADR-005: Quartz for Digital Garden Publishing"
related:
  - "wiki/30-project/obsidian-second-brain-integration.md"
  - "wiki/10-concept/obsidian-second-brain-architecture.md"
  - "wiki/10-concept/obsidian-second-brain-enhanced.md"
created: "2026-11-18"
updated: "2026-11-18"
---

# Obsidian Second Brain â€” Personal Knowledge Management System

> **One-line summary**: Comprehensive three-layer second brain (sources â†’ inbox â†’ wiki) with 21-plugin automation pipeline, career transition workflows, and digital garden deployment.

## Problem

As a student transitioning to a software engineering career, I needed a system to:
- Capture and retain technical knowledge from courses, projects, and research
- Track job applications, interview prep, and networking systematically
- Build a portfolio demonstrating engineering skills
- Automate repetitive knowledge management tasks
- Enable spaced repetition for interview readiness

Existing tools (Notion, Roam, vanilla Obsidian) lacked the automation depth, career-specific workflows, or developer-centric architecture I needed.

## Role & Scope

- **Role**: Solo Developer / Architect
- **Duration**: 2026-11 (ongoing)
- **Team Size**: 1
- **My Contribution**: 100% â€” architecture, implementation, automation, documentation

## Solution

### Architecture Decision Records
- [[ADR-001: Three-Layer Architecture (Sources â†’ Inbox â†’ Wiki)]]
- [[ADR-002: PARA via Frontmatter Properties]]
- [[ADR-003: FSRS over SM-2 for Spaced Repetition]]
- [[ADR-004: REST API over MCP stdio on Windows]]
- [[ADR-005: Quartz for Digital Garden Publishing]]

### Technical Approach

Built on **Obsidian** as the local-first knowledge base with a **three-layer architecture** validated against Karpathy's LLM Wiki best practice:

1. **Sources/** â€” Immutable raw inputs (articles, conversations, papers, videos)
2. **Inbox/** â€” Daily notes, fleeting captures, temporal workspace
3. **Wiki/** â€” Atomic evergreen notes organized by Johnny Decimal (10-concept, 20-evergreen, 30-project, 40-synthesis, 50-career, 60-people)

**Automation Pipeline** (7 QuickAdd macros):
- `capture-source` â€” Web/article/video â†’ sources/ with metadata
- `capture-fleeting` â€” Quick thought â†’ inbox/fleeting/
- `create-wiki-concept` â€” Structured concept note with PARA frontmatter
- `create-star-story` â€” Behavioral interview story with SR integration
- `create-job-application` â€” Kanban-ready application tracker
- `create-person-contact` â€” CRM contact with follow-up scheduling
- `create-adr` â€” Architecture decision record
- `daily-review` â€” End-of-day synthesis

**Spaced Repetition** (Better Recall + FSRS):
- 4 decks: Behavioral (6 STAR), Algorithms (5), System Design (5), Career Skills (5), Company Research (2)
- 21 cards total, algorithmically scheduled

**Digital Garden** (Quartz):
- Selective publishing via `publish: true` frontmatter
- 25 pages deployed to GitHub Pages
- Custom components for dashboards, graph view

**CI/CD Pipeline** (GitHub Actions):
- Lint (frontmatter, links, orphans, stale)
- Frontmatter validation (JSON Schema)
- Dataview query syntax testing
- Quartz build
- Deploy to GitHub Pages

**MCP Integration**:
- `obsidian-local-rest-api` on port 27123 (7 endpoints)
- Vault read/write/search/graph/commands via HTTP
- Alternative to stdio MCP (Windows spawn issues)

### Technologies Used
- Obsidian (core)
- TypeScript / Node.js (plugins, REST API)
- Dataview (15 live dashboard queries)
- QuickAdd + Templater (capture automation)
- Better Recall (FSRS spaced repetition)
- Quartz (static site generation)
- GitHub Actions (CI/CD)
- MCP (Model Context Protocol)

## Implementation Highlights

### Challenge 1: Three-Layer Architecture Validation
- **Problem**: Needed confidence the architecture follows best practices
- **Approach**: Researched Karpathy's LLM Wiki, mapped to PARA, validated with community patterns
- **Result**: Architecture recognized as best practice; documented in `wiki/10-concept/obsidian-second-brain-architecture.md`

### Challenge 2: Windows MCP stdio Spawn Failure
- **Problem**: `obsidian-mcp` works manually but fails when spawned by Claude Code child process
- **Approach**: Debugged PATH, npx.cmd, entry points; built REST API alternative
- **Result**: REST API fully operational (7 endpoints); documented ADR-004; MCP config fixed for future

### Challenge 3: Quartz YAML Frontmatter Compatibility
- **Problem**: Bare wikilink arrays `[[A], [B]]` fail Quartz build
- **Approach**: Converted to quoted strings `["[[A]]", "[[B]]"]` across 10 concept files
- **Result**: Clean Quartz build; 25 pages published

### Challenge 4: Career Workflow Integration
- **Problem**: Generic PKM doesn't serve studentâ†’career transition needs
- **Approach**: Designed 4 career projects + 9 STAR stories + company research CRM + portfolio from ADRs
- **Result**: Unified system serving both learning and job search

## Impact & Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Vault Pages | 0 | 30+ | +30 |
| Automation Macros | 0 | 7 | +7 |
| Spaced Repetition Cards | 0 | 21 | +21 |
| CI/CD Pipeline Stages | 0 | 6 | +6 |
| STAR Stories | 0 | 9 | +9 |
| MCP Endpoints | 0 | 7 | +7 |
| Company Research Notes | 0 | 10 | +10 |
| Templates Created | 0 | 12 | +12 |

## Skills Demonstrated

- **System Architecture**: Three-layer design, ADR documentation, technology selection
- **TypeScript/Node.js**: REST API server, plugin configs, automation scripts
- **Automation**: QuickAdd macros, Templater scripts, GitHub Actions CI/CD
- **Knowledge Management**: PARA, Johnny Decimal, atomic notes, spaced repetition (FSRS)
- **DevOps**: GitHub Actions, Quartz deployment, Git workflow, linting
- **AI Integration**: MCP server, REST API, subagent workflows
- **Career Engineering**: STAR stories, interview prep system, company CRM, portfolio
- **Documentation**: Technical specs, user guides, architecture decisions

## Reflection

### What Went Well
- Three-layer architecture validated externally (Karpathy's LLM Wiki)
- Automation pipeline eliminates manual friction
- REST API more reliable than MCP stdio on Windows
- Career workflows directly serve immediate job search needs
- Digital garden provides public portfolio artifact

### What I'd Do Differently
- Start with REST API instead of debugging MCP stdio
- Use JSON Schema for frontmatter from day one
- Build weekly review automation earlier
- Create Excalidraw templates before case studies

### Key Learnings
- Local-first tools (Obsidian) + automation > cloud-only for developer PKM
- FSRS significantly outperforms SM-2 for retention
- Career transition benefits from structured CRM + SR integration
- Digital garden forces clarity in thinking (writing for audience)

## Links

- **Repository**: [GitHub](https://github.com/username/claude-brain)
- **Live Demo**: [Digital Garden](https://username.github.io/quartz-garden)
- **Documentation**: [[wiki/10-concept/obsidian-second-brain-enhanced.md]]
- **ADRs**: [[architecture-decision-records]]
- **Related Projects**: [[wiki/30-project/obsidian-second-brain-integration.md]]

