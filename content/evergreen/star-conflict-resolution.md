---
publish: true
title: "STAR: Conflict Resolution"
type: evergreen
concept: "interview-star-story"
category: "conflict-resolution"
status: budding
confidence: 0.8
tags: [interview, star, behavioral, conflict, teamwork]
source: self
related: ["[[STAR: Team Under Pressure]]", "[[STAR: Leadership]]"]
company_target: []
last_reviewed: "2026-11-18"
created: "2026-11-18"
updated: "2026-11-18"
para: project
---

# STAR: Conflict Resolution

## Situation
During my capstone project in senior year, our 4-person team had a fundamental disagreement on the architecture for our distributed task scheduling system. Two members wanted to use a message queue (RabbitMQ) for inter-service communication, while the other two (including me) advocated for gRPC with protobuf for lower latency and stronger contracts. The disagreement stalled our progress for a week as neither side would compromise.

## Task
As the team's technical lead, I needed to resolve the architectural deadlock so we could meet our project deadline while maintaining team cohesion and choosing the technically sound approach.

## Action
1. **Structured the debate**: Called a dedicated architecture decision meeting with a clear agenda: present trade-offs, define evaluation criteria, decide.
2. **Created a decision matrix**: Listed criteria (latency, operational complexity, team familiarity, debugging ease, scalability) and had each person score both approaches.
3. **Proposed a hybrid**: For core scheduling logic (latency-critical), use gRPC. For async event propagation (notifications, metrics), use RabbitMQ.
4. **Ran a spike**: Each sub-team built a minimal prototype in 4 hours to validate their approach's feasibility.
5. **Facilitated consensus**: Presented results objectively. The data showed gRPC was 3x faster for our critical path but RabbitMQ was simpler for event fan-out. The hybrid won unanimous agreement.

## Result
- Delivered the project on time with the hybrid architecture
- System handled 10k tasks/minute with <50ms p99 latency
- Team collaboration improved â€” we established a formal ADR process for future decisions
- Professor cited our architecture decision process as a model for future cohorts

## Skills Demonstrated
- Technical leadership
- Conflict mediation
- Data-driven decision making
- Architecture trade-off analysis
- Team facilitation

## Variations for Different Roles
- **Backend Engineer**: Emphasize the gRPC vs message queue trade-offs and latency requirements
- **Tech Lead**: Focus on the decision-making process and team alignment
- **Project Manager**: Highlight the timeline impact and stakeholder management

