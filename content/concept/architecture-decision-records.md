---

publish: true
title: "Architecture Decision Records (ADRs)"
type: concept
status: evergreen
tags: [architecture, adr, decision-making, documentation]
sources: []
related:
  - "wiki/50-career/portfolio/obsidian-second-brain.md"
  - "wiki/50-career/portfolio/distributed-task-scheduler.md"
  - "wiki/50-career/portfolio/protein-dataset-curation.md"
concept: "architecture-decision-record"
confidence: 0.95
created: "2026-11-18"
updated: "2026-11-18"
---

# Architecture Decision Records (ADRs)

> **One-line summary**: Lightweight documentation of significant architectural decisions using MADR format, enabling future understanding, reversal, and onboarding.

## What is an ADR?

An **Architecture Decision Record (ADR)** captures a significant architectural decision along with its context, consequences, and rationale. Based on [Michael Nygard's ADR format](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) and the [MADR (Markdown ADR)](https://adr.github.io/madr/) specification.

## MADR Format

```markdown
---
title: "ADR-XXX: Short Title"
status: proposed | accepted | superseded | deprecated
number: "XXX"
concept: "architecture-decision"
tags: [adr]
supersedes: "ADR-YYY"
deciders: ["Name"]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
---

# Title

## Status
[Proposed | Accepted | Superseded | Deprecated]

## Context
[Problem statement, constraints, assumptions, forces at play]

## Decision
[What we decided, in active voice â€” "We will..."]

## Consequences

### Positive
- [Benefits]

### Negative
- [Trade-offs]

### Risks
- [Mitigations]

## Related
- [[ADR-YYY]]
- [[wiki/page]]
```

## ADR Index

| ID | Title | Status | Date | Supersedes |
|----|-------|--------|------|------------|
| ADR-001 | Three-Layer Architecture (Sources â†’ Inbox â†’ Wiki) | accepted | 2026-11-17 | â€” |
| ADR-002 | PARA via Frontmatter Properties | accepted | 2026-11-17 | â€” |
| ADR-003 | FSRS over SM-2 for Spaced Repetition | accepted | 2026-11-18 | â€” |
| ADR-004 | REST API over MCP stdio on Windows | accepted | 2026-11-18 | â€” |
| ADR-005 | Quartz for Digital Garden Publishing | accepted | 2026-11-18 | â€” |
| ADR-010 | Leader Election via etcd | accepted | 2025-01-15 | â€” |
| ADR-011 | Exactly-Once Semantics with Idempotency Keys | accepted | 2025-02-01 | â€” |
| ADR-012 | Horizontal Scaling with Partitioned Queues | accepted | 2025-02-15 | â€” |
| ADR-020 | Incremental Processing with Checkpointing | accepted | 2024-06-20 | â€” |
| ADR-021 | Quality Gates with Automated Validation | accepted | 2024-07-01 | â€” |
| ADR-022 | Open Source Licensing (MIT) | accepted | 2024-08-01 | â€” |

## When to Create an ADR

Create an ADR when making a decision that:
- **Affects multiple components** or teams
- **Is difficult to reverse** (database choice, framework, protocol)
- **Has significant trade-offs** (performance vs consistency, build vs buy)
- **Impacts long-term maintenance** (tech debt, migration path)
- **Requires future justification** (why did we choose X?)

## ADR Lifecycle

1. **Proposed** â€” Draft circulating for feedback
2. **Accepted** â€” Approved, implementation proceeds
3. **Superseded** â€” Replaced by newer ADR (link to replacement)
4. **Deprecated** â€” No longer relevant (link to why)

## Best Practices

- **One decision per ADR** â€” keep focused
- **Write in active voice** â€” "We will use PostgreSQL" not "PostgreSQL should be used"
- **Include rejected alternatives** â€” shows due diligence
- **Link related ADRs** â€” creates decision graph
- **Store in version control** â€” alongside code
- **Review periodically** â€” quarterly architecture review

## Tools

- **Template**: `templates/adr.md`
- **CLI**: `adr-tools` (npx adr-tools)
- **Viewer**: VS Code ADR extension, `adr-log` generator
- **This vault**: `wiki/10-concept/architecture-decision-records.md` (this file)

## Related

- [[Obsidian Second Brain Architecture]]
- [[Obsidian Second Brain Enhanced]]
- [[Portfolio: Obsidian Second Brain]]
- [[Portfolio: Distributed Task Scheduler]]
- [[Portfolio: Protein Dataset Curation]]


