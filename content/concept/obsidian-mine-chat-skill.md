---

publish: true
title: "Obsidian Mine Chat Skill"
type: concept
tags: [obsidian, skill, subagent, mining, automation, claude-code]
sources: []
related: ["[[Vault Mining Pattern]]", "[[Obsidian Second Brain Integration]]"]
created: "2026-11-17"
updated: "2026-11-17"
---

# Obsidian Mine Chat Skill

## Overview

A Claude Code slash command (`/obsidian-mine-chat`) that spawns a subagent to analyze conversation transcripts and write extracted insights directly to the Obsidian vault.

## Details

### Command Syntax
```
/obsidian-mine-chat [--since <turns>] [--focus <skills|projects|wiki|tasks|all>]
```

### Flags
- `--since <turns>` â€” How many conversation turns to analyze (default: full conversation)
- `--focus <category>` â€” Limit extraction to specific category:
  - `skills` â€” New skill patterns
  - `projects` â€” Project status updates
  - `wiki` â€” Concept/wiki page candidates
  - `tasks` â€” Action items for daily notes
  - `all` â€” All categories (default)

### Implementation
- Located at `.claude/skills/obsidian-mine-chat/SKILL.md`
- Command file at `.claude/commands/obsidian-mine-chat.md`
- Invokes Agent tool with vault mining prompt template
- Subagent reads: `_CLAUDE.md`, `_index.md`, `_log.md`, active projects, recent dailies, templates
- Subagent writes: wiki pages, source files, daily note updates, log entries, index updates

### Extraction Categories
1. **NEW SKILLS** â€” Reusable workflows/patterns mentioned 2+ times
2. **PROJECT UPDATES** â€” Status changes, decisions, blockers, priorities
3. **WIKI PAGES** â€” Concepts, people, synthesis worth atomic notes
4. **SOURCES** â€” URLs, references, articles â†’ `sources/{type}/`
5. **TASKS** â€” Action items â†’ today's daily note Open Loops/Work
6. **DECISIONS** â€” Architectural choices â†’ `_log.md`

## Connections

- [[Vault Mining Pattern]] â€” the pattern this skill implements
- [[Obsidian Second Brain Integration]] â€” the project this skill serves

## Sources

- Conversation transcript: Obsidian second brain setup session (2026-11-17)


