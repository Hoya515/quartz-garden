---
publish: true
title: "Protein Dataset Curation Pipeline â€” Automated Bioinformatics Platform"
type: case-study
status: draft
project: "Protein Dataset Curation"
role: "ML Engineer / Research Engineer"
duration: "2024-06 â€” 2024-12 (7 months)"
tags: [portfolio, case-study, bioinformatics, ml, python, automation]
skills: ["Machine Learning", "Python", "Bioinformatics", "Data Engineering", "Automation", "Open Source", "Research"]
technologies: ["Python", "PyTorch", "BioPython", "RDKit", "Dask", "PostgreSQL", "S3", "Docker", "GitHub Actions"]
impact: "Automated protein structure dataset curation achieving 20x speedup, processing 187k structures, open-sourced as community tool"
metrics:
  - name: "Processing Speed"
    before: "~50 structures/hour (manual)"
    after: "~1,000 structures/hour (automated)"
    change: "20x"
  - name: "Structures Processed"
    before: "~5,000"
    after: "187,000+"
    change: "+182k"
  - name: "Data Quality"
    before: "~60% usable"
    after: "95%+ usable"
    change: "+35%"
  - name: "Community Adoption"
    before: "0"
    after: "200+ stars, 15 contributors"
    change: "200+"
adr-refs:
  - "ADR-020: Incremental Processing with Checkpointing"
  - "ADR-021: Quality Gates with Automated Validation"
  - "ADR-022: Open Source Licensing (MIT)"
related:
  - "wiki/20-evergreen/star-innovation.md"

created: "2026-11-18"
updated: "2026-11-18"
---

# Protein Dataset Curation Pipeline â€” Automated Bioinformatics Platform

> **One-line summary**: Automated protein structure dataset curation achieving 20x speedup, processing 187k structures, open-sourced as community tool.

## Problem

Structural biology researchers needed high-quality protein datasets for ML training, but existing pipelines were:
- Manual/semi-automated (PhD students spending weeks curating)
- Low quality (~60% usable structures after cleaning)
- Not reproducible (no versioning, inconsistent criteria)
- Not scalable to PDB-scale (180k+ structures)

## Role & Scope

- **Role**: ML Engineer / Research Engineer
- **Duration**: 7 months (2024-06 â€” 2024-12)
- **Team Size**: 2 engineers + 1 computational biologist
- **My Contribution**: Pipeline architecture, automation, quality gates, open-source release

## Solution

### Architecture Decision Records
- [[ADR-020: Incremental Processing with Checkpointing]]
- [[ADR-021: Quality Gates with Automated Validation]]
- [[ADR-022: Open Source Licensing (MIT)]]

### Technical Approach

**Pipeline Stages** (Python, Dask for parallelism):
1. **Fetch** â€” PDB/mmCIF download with resume, checksum validation
2. **Parse** â€” BioPython/RDKit for structure extraction, ligand identification
3. **Filter** â€” Resolution, R-free, completeness, ligand criteria
4. **Featurize** â€” Geometric features, physicochemical properties, embeddings
5. **Validate** â€” Clash scores, Ramachandran, ligand geometry, ML readiness
6. **Export** â€” ML-ready formats (PyTorch Geometric, DGL, NumPy)

**Quality Gates**:
- Automated validation at each stage
- Statistical quality reports per release
- Regression testing against known-good subsets
- Versioned datasets with reproducibility manifests

**Scalability**:
- Dask distributed processing (horizontal scaling)
- Incremental checkpointing (resume from failure)
- S3 + PostgreSQL for metadata/artifact storage
- 20x speedup vs manual: 187k structures in 48 hours

**Open Source Release**:
- MIT licensed, pip-installable (`pip install protcurate`)
- Comprehensive docs, tutorials, API reference
- 200+ GitHub stars, 15 external contributors
- Adopted by 3 research labs for publication datasets

### Technologies Used
- Python, Dask, BioPython, RDKit, PyTorch
- PostgreSQL, S3, Docker
- GitHub Actions (CI/CD, release automation)
- Sphinx (documentation), pytest (testing)

## Implementation Highlights

### Challenge 1: Handling Heterogeneous PDB Data
- **Problem**: PDB entries vary wildly in quality, format, completeness
- **Approach**: Multi-stage validation with configurable thresholds, per-entry quality scores
- **Result**: 95%+ usable rate, transparent quality metadata per structure

### Challenge 2: Reproducibility at Scale
- **Problem**: Need exact same results across runs, clusters, time
- **Approach**: Content-addressable storage, pinned dependencies, deterministic algorithms, manifest files
- **Result**: Bit-for-bit reproducible datasets across environments

### Challenge 3: Community Adoption
- **Problem**: Academic tools often abandoned after publication
- **Approach**: Treated as product: docs, tutorials, issue templates, semantic versioning, contributor guide
- **Result**: Active community, external PRs, cited in 5+ papers

## Impact & Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Processing Speed | ~50/hr | ~1,000/hr | 20x |
| Structures Processed | ~5,000 | 187,000+ | +182k |
| Data Quality | ~60% | 95%+ | +35% |
| Community Adoption | 0 | 200+ stars | 200+ |

## Skills Demonstrated

- **Machine Learning**: Dataset curation for GNNs, feature engineering, validation
- **Python**: High-performance data pipelines, Dask, scientific stack
- **Bioinformatics**: Protein structure analysis, PDB/mmCIF, quality metrics
- **Data Engineering**: Incremental processing, checkpointing, quality gates
- **Open Source**: Product thinking, documentation, community building
- **Research Engineering**: Reproducibility, collaboration with domain experts

## Reflection

### What Went Well
- 20x speedup exceeded 10x target
- Open source adoption validated utility
- Quality gates caught issues early
- Collaboration with biologist improved criteria

### What I'd Do Differently
- Invest in GPU-accelerated featurization earlier
- Build web UI for non-programmer biologists
- Design for multi-species from start (human-only initially)

### Key Learnings
- Treat research tools as products for adoption
- Quality metadata > binary pass/fail
- Incremental processing essential at scale
- Domain expert collaboration prevents blind spots

## Links

- **Repository**: [GitHub](https://github.com/username/protein-dataset-curator)
- **PyPI**: `pip install protcurate`
- **Documentation**: [ReadTheDocs](https://protcurate.readthedocs.io)
- **ADRs**: [[architecture-decision-records]]
- **Related**: [[wiki/20-evergreen/star-innovation.md]]

