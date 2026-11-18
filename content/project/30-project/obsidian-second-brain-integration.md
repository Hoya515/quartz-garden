---
publish: true
title: "Obsidian Second Brain Integration"
type: project
tags: [obsidian, second-brain, integration, claude-code, active]
sources: []
related: ["[[Obsidian Second Brain Architecture]]", "[[Vault Mining Pattern]]", "[[Obsidian Mine Chat Skill]]"]
created: "2026-11-17"
updated: "2026-11-17"
---

# Obsidian Second Brain Integration

## Overview

Active project to connect Obsidian as a "second brain" with Claude Code, enabling seamless knowledge capture, synthesis, and retrieval through a three-layer vault architecture.

## Status

**Active** â€” Vault initialized, core skills deployed, first daily note created, mining skill implemented.

## Decisions

- **2026-11-17**: Adopted three-layer architecture (sources/, inbox/, wiki/)
- **2026-11-17**: Wiki is LLM-written only â€” no hand-editing
- **2026-11-17**: One idea per wiki page with generous wikilinks
- **2026-11-17**: Frontmatter required on all wiki pages
- **2026-11-17**: Sources are immutable
- **2026-11-17**: Inbox processed weekly
- **2026-11-17**: All changes logged to `_log.md`

## Milestones

- [x] **2026-11-17**: Vault structure created (sources/, inbox/, wiki/)
- [x] **2026-11-17**: Governance files created (_CLAUDE.md, _index.md, _log.md)
- [x] **2026-11-17**: Templates created (wiki-note.md, daily.md, source.md)
- [x] **2026-11-17**: Core skills deployed (today, weekly-review, obsidian-ingest, obsidian-find, lint, recall)
- [x] **2026-11-17**: Slash commands created for all skills
- [x] **2026-11-17**: First daily note created (inbox/2026-11-17.md)
- [x] **2026-11-17**: obsidian-mine-chat skill created and command registered
- [ ] **Next**: Ingest first source to populate wiki
- [ ] **Next**: Test /obsidian-find and /obsidian-ingest workflows
- [ ] **Next**: Set up automated daily/weekly review cadence

## Blockers

None currently.

## Connections

- [[Obsidian Second Brain Architecture]] â€” the architecture this project implements
- [[Vault Mining Pattern]] â€” the conversation mining pattern used by this project
- [[Obsidian Mine Chat Skill]] â€” the skill enabling automated vault updates

## Sources

- Conversation transcript: Obsidian second brain setup session (2026-11-17)
- Reference: "twitter obsidian second brain" agent (source to be ingested)

