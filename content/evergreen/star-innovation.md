---
publish: true
title: "STAR: Innovation"
type: evergreen
concept: "interview-star-story"
category: "innovation"
status: budding
confidence: 0.8
tags: [interview, star, behavioral, innovation, problem-solving]
source: self
related: ["[[STAR: Proudest Project]]", "[[STAR: Learn Quickly]]"]
company_target: []
last_reviewed: "2026-11-18"
created: "2026-11-18"
updated: "2026-11-18"
para: project
---

# STAR: Innovation

## Situation
During my summer research internship at a computational biology lab, the team spent 4+ hours daily manually curating protein structure datasets from PDB (Protein Data Bank) for ML training. The pipeline involved: search PDB â†’ download CIF files â†’ parse metadata â†’ filter by resolution/chain length â†’ convert to numpy arrays â†’ validate. Errors were frequent and the process couldn't scale to the 200k+ structures needed.

## Task
Automate the protein dataset curation pipeline to reduce manual time from 4 hours to <30 minutes, handle 200k+ structures, and produce reproducible, versioned datasets.

## Action
1. **Analyzed the workflow**: Mapped each manual step, identified decision points (resolution < 2.5Ã…, single chain, length 50-500 residues), and failure modes (missing coordinates, alt loci, heteroatoms)
2. **Designed a declarative config**: YAML schema defining filters, transformations, and validation rules â€” enabling non-coders to modify criteria
3. **Built the pipeline in Python**: 
   - Async PDB REST API client with rate limiting and exponential backoff
   - Streaming CIF parser using `biotite` (memory-efficient for large files)
   - Parallel processing with `ray` for distributed computation across 16 cores
   - Checkpointing every 10k structures for fault tolerance
   - Output: Parquet files with embedded schema + metadata JSON
4. **Added CI/CD**: GitHub Actions workflow that runs nightly, publishes versioned datasets to S3, notifies team via Slack
5. **Created a web UI**: Simple React dashboard for browsing dataset versions, viewing stats (resolution distribution, chain length histograms), and triggering reprocessing

## Result
- Reduced curation time from 4 hours â†’ 12 minutes (20x speedup)
- Processed 187k structures in first run (vs. ~2k manually curated)
- Zero manual intervention needed for 6 months of nightly runs
- Enabled 3 new ML experiments that were previously infeasible due to data constraints
- Pipeline adopted by 2 other labs; open-sourced as `proteindata-curator` (147 GitHub stars)

## Skills Demonstrated
- End-to-end pipeline automation
- Domain-specific problem modeling (biology + ML)
- Scalable systems design (async, parallel, fault-tolerant)
- Developer experience (config-driven, UI, observability)
- Open-source contribution

## Variations for Different Roles
- **ML Engineer**: Emphasize data quality, versioning, reproducibility, scale
- **Backend Engineer**: Focus on async architecture, fault tolerance, API design
- **Research Engineer**: Highlight domain modeling, scientist collaboration, open science

