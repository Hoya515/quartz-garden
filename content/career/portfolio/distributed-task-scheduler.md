---
publish: true
title: "Distributed Task Scheduler â€” High-Throughput Job Processing System"
type: case-study
status: draft
project: "Distributed Task Scheduler"
role: "Backend Engineer / Tech Lead"
duration: "2025-01 â€” 2025-06 (6 months)"
tags: [portfolio, case-study, distributed-systems, go, kubernetes]
skills: ["Distributed Systems", "Go", "Kubernetes", "gRPC", "PostgreSQL", "Redis", "Observability", "System Design"]
technologies: ["Go", "Kubernetes", "gRPC", "PostgreSQL", "Redis", "Prometheus", "Grafana", "Jaeger", "Docker"]
impact: "Designed and built a distributed task scheduler processing 10k tasks/minute with <50ms p99 latency, supporting 50+ microservices"
metrics:
  - name: "Throughput"
    before: "0 tasks/min"
    after: "10,000 tasks/min"
    change: "+10k"
  - name: "P99 Latency"
    before: "N/A"
    after: "<50ms"
    change: "<50ms"
  - name: "Service Adoption"
    before: "0"
    after: "50+"
    change: "+50"
  - name: "Uptime"
    before: "N/A"
    after: "99.99%"
    change: "99.99%"
adr-refs:
  - "ADR-010: Leader Election via etcd"
  - "ADR-011: Exactly-Once Semantics with Idempotency Keys"
  - "ADR-012: Horizontal Scaling with Partitioned Queues"
related:
  - "wiki/20-evergreen/star-proudest-project.md"

created: "2026-11-18"
updated: "2026-11-18"
---

# Distributed Task Scheduler â€” High-Throughput Job Processing System

> **One-line summary**: Distributed task scheduler processing 10k tasks/minute with <50ms p99 latency, supporting 50+ microservices across the organization.

## Problem

The organization had no centralized task scheduling system. Teams built ad-hoc cron jobs, leading to:
- Duplicate infrastructure across 20+ services
- No visibility into job execution, failures, or SLAs
- Inability to handle burst workloads or priority queuing
- Manual intervention required for retries, dead letter handling

## Role & Scope

- **Role**: Backend Engineer / Tech Lead
- **Duration**: 6 months (2025-01 â€” 2025-06)
- **Team Size**: 4 engineers
- **My Contribution**: Architecture, core scheduler, leader election, partitioning, observability

## Solution

### Architecture Decision Records
- [[ADR-010: Leader Election via etcd]]
- [[ADR-011: Exactly-Once Semantics with Idempotency Keys]]
- [[ADR-012: Horizontal Scaling with Partitioned Queues]]

### Technical Approach

**Core Scheduler** (Go, gRPC):
- Leader election via etcd for HA (single active scheduler)
- Partitioned priority queues (Redis sorted sets) for horizontal scaling
- Exactly-once execution via idempotency keys + PostgreSQL transactions
- Pluggable executor interface (HTTP, gRPC, message queue, shell)

**Scalability**:
- 10k tasks/minute sustained, burst to 50k
- <50ms p99 scheduling latency
- Horizontal scaling: add scheduler replicas + queue partitions
- Kubernetes HPA based on queue depth

**Reliability**:
- Dead letter queue with exponential backoff retry
- Circuit breaker for downstream protection
- Comprehensive observability: Prometheus metrics, Grafana dashboards, Jaeger tracing
- 99.99% uptime over 6 months

**Developer Experience**:
- CRD for Kubernetes-native job definitions
- CLI for local testing and debugging
- Web UI for monitoring, manual triggers, replay
- Self-serve onboarding for new teams

### Technologies Used
- Go, gRPC, Protocol Buffers
- Kubernetes (CRD, Operator pattern)
- etcd (leader election, config)
- Redis (partitioned priority queues)
- PostgreSQL (job metadata, idempotency)
- Prometheus, Grafana, Jaeger

## Implementation Highlights

### Challenge 1: Exactly-Once at Scale
- **Problem**: Duplicate task execution causing downstream side effects
- **Approach**: Idempotency keys + PostgreSQL advisory locks + deterministic execution IDs
- **Result**: Zero duplicate executions in 6 months production

### Challenge 2: Leader Election Without Single Point of Failure
- **Problem**: Scheduler must be HA but only one active leader
- **Approach**: etcd lease-based election with graceful handoff, health checks
- **Result**: Sub-second failover, zero scheduling gaps during deployments

### Challenge 3: Multi-Tenant Fair Queuing
- **Problem**: Noisy neighbors starving other teams' jobs
- **Approach**: Token bucket per tenant + weighted fair queuing across partitions
- **Result**: Guaranteed minimum throughput per team

## Impact & Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Throughput | 0 tasks/min | 10,000 tasks/min | +10k |
| P99 Latency | N/A | <50ms | <50ms |
| Service Adoption | 0 | 50+ | +50 |
| Uptime | N/A | 99.99% | 99.99% |
| Manual Interventions | Daily | <1/week | -95% |

## Skills Demonstrated

- **Distributed Systems**: Leader election, consensus, exactly-once, partitioning
- **Go**: High-performance scheduler, gRPC services, Kubernetes operator
- **Kubernetes**: CRDs, controllers, HPA, operator pattern
- **Observability**: Metrics, tracing, dashboards, alerting
- **System Design**: Trade-off analysis, capacity planning, failure modes
- **Technical Leadership**: Architecture decisions, code review, mentoring

## Reflection

### What Went Well
- Clean architecture with clear separation of concerns
- Comprehensive observability from day one
- Team adoption exceeded expectations (50+ services)
- Zero data loss or duplicate execution incidents

### What I'd Do Differently
- Invest in integration test framework earlier
- Build chaos engineering tests for leader failover
- Design multi-region from start (single region initially)

### Key Learnings
- Idempotency keys > distributed transactions for exactly-once
- etcd leases simpler than Raft for leader election
- Developer experience drives adoption more than features

## Links

- **Repository**: [Internal GitHub](https://github.com/org/task-scheduler)
- **Documentation**: [Internal Wiki](https://wiki.org/task-scheduler)
- **ADRs**: [[architecture-decision-records]]
- **Related**: [[wiki/20-evergreen/star-proudest-project.md]]

