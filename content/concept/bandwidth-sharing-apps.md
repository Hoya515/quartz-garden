---

publish: true
title: "Bandwidth Sharing Apps (Honeygain, Salad)"
type: concept
tags: [honeygain, salad, bandwidth, passive-income, windows, resource-usage]
sources: [sources/conversation/pc-power-waste-analysis.md]
related: ["[[Overwolf SteelSeries Logitech Bloatware]]", "[[HP Bloatware Services]]"]
created: "2026-11-18"
updated: "2026-11-18"
---

# Bandwidth Sharing Apps (Honeygain, Salad)

## Overview

Apps like Honeygain and Salad run background processes that share your internet bandwidth and compute resources for minimal financial return, often consuming disproportionate system resources.

## Details

### Honeygain
- **Process**: `Honeygain.exe` + helper processes
- **Resource Usage**: Constant network traffic, ~50-100 MB RAM, periodic CPU
- **Earnings**: ~$1-5/month for typical residential connection
- **Privacy**: Routes unknown third-party traffic through your IP

### Salad
- **Process**: `Salad.exe` + `Salad.Kitchen.exe` + container runtime
- **Resource Usage**: High CPU (compute workloads), GPU (if enabled), significant RAM
- **Earnings**: Variable, depends on workload availability
- **Mechanism**: Runs containerized workloads (AI inference, rendering, etc.)

### Cost-Benefit Analysis
| App | Monthly Earnings | Electricity Cost | Hardware Wear | Privacy Risk |
|-----|------------------|------------------|---------------|--------------|
| Honeygain | $1-5 | $2-10 | Low | High (IP exposure) |
| Salad | $5-50 | $10-50 | High (GPU/CPU) | Medium |

### Recommendation
**Uninstall both** unless:
- You have unlimited unmetered bandwidth
- Electricity is free/very cheap
- You accept IP reputation risks (Honeygain)
- You have spare GPU compute capacity (Salad)

### Removal
```powershell
# Honeygain
winget uninstall Honeygain.Honeygain

# Salad
winget uninstall SaladTechnologies.Salad
```

## Connections

- [[Overwolf SteelSeries Logitech Bloatware]] â€” similar background resource consumers
- [[HP Bloatware Services]] â€” telemetry/services with poor value proposition

## Sources

- Conversation transcript: PC power waste analysis (2026-11-18)


