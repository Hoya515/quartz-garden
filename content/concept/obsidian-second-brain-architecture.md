---

publish: true
title: "Obsidian Second Brain Architecture"
type: concept
tags: [obsidian, second-brain, architecture, vault]
sources: []
related: ["[[Vault Mining Pattern]]", "[[Obsidian Second Brain Integration]]"]
created: "2026-11-17"
updated: "2026-11-17"
---

# Obsidian Second Brain Architecture

## Overview

A three-layer vault architecture designed for LLM-augmented knowledge management. Raw inputs flow through immutable sources into synthesized wiki pages, with an inbox for fleeting capture.

## Details

### Layer 1: Sources (`sources/`)
- **Immutable inputs** â€” articles, YouTube videos, X/Twitter threads, podcasts
- Never modified after creation
- Organized by source type: `article/`, `youtube/`, `x/`, `podcast/`
- Template: `templates/source.md`

### Layer 2: Inbox (`inbox/`)
- **Fleeting capture** â€” daily notes, quick ideas, meeting notes
- Temporary holding zone
- Processed weekly to `sources/` or `wiki/`
- Daily notes use `templates/daily.md`

### Layer 3: Wiki (`wiki/`)
- **LLM-written only** â€” never hand-edit files in `wiki/`
- Atomic notes: one idea per page
- Types: `concept/`, `project/`, `person/`, `synthesis/`
- Frontmatter required (see `templates/wiki-note.md`)
- Generous `[[wikilinks]]` for connection density
- Auto-maintained index at `_index.md`

## Connections

- [[Vault Mining Pattern]] â€” subagent pattern for extracting insights from conversations
- [[Obsidian Second Brain Integration]] â€” active project implementing this architecture

## Sources

- Conversation transcript: Obsidian second brain setup session (2026-11-17)


