---

publish: true
title: "Vault Mining Pattern"
type: concept
tags: [obsidian, subagent, mining, conversation-analysis, automation]
sources: []
related: ["[[Obsidian Second Brain Architecture]]", "[[Obsidian Second Brain Integration]]", "[[Obsidian Mine Chat Skill]]"]
created: "2026-11-17"
updated: "2026-11-17"
---

# Vault Mining Pattern

## Overview

A reusable workflow where a subagent analyzes conversation transcripts in the context of an Obsidian vault, then writes extracted insights directly to the vault's three-layer structure.

## Details

### Trigger
- Invoked via `/obsidian-mine-chat` slash command
- Can run periodically or on-demand after significant conversations

### Subagent Responsibilities
1. **Read vault context** â€” constitution, index, log, active projects, recent dailies, templates
2. **Analyze conversation** for six categories of insights:
   - **NEW SKILLS**: Reusable workflows/patterns mentioned 2+ times
   - **PROJECT UPDATES**: Status changes, decisions, blockers, priorities
   - **WIKI PAGES**: Concepts, people, synthesis worth atomic notes
   - **SOURCES**: URLs, references, articles mentioned â†’ ingest via `sources/`
   - **TASKS**: Action items, commitments, follow-ups â†’ add to today's daily
   - **DECISIONS**: Architectural choices, trade-offs â†’ log to `_log.md`
3. **Write to vault** using prescribed patterns:
   - Skills: Create `.claude/skills/new-skill/SKILL.md` + command file
   - Wiki: Create `wiki/{type}/page.md` with frontmatter + wikilinks
   - Sources: Create `sources/{type}/slug.md` with template
   - Dailies: Append to `inbox/YYYY-MM-DD.md` Open Loops/Work
   - Log: Append to `_log.md` with date + summary
   - Index: Update `_index.md` catalog

### Constraints
- Never hand-edit `wiki/` without frontmatter
- One idea per wiki page
- Sources are immutable
- Log every write to `_log.md`
- Use templates for all new files

## Connections

- [[Obsidian Second Brain Architecture]] â€” the vault structure this pattern operates on
- [[Obsidian Second Brain Integration]] â€” project that uses this pattern
- [[Obsidian Mine Chat Skill]] â€” the skill implementing this pattern

## Sources

- Conversation transcript: Obsidian second brain setup session (2026-11-17)


