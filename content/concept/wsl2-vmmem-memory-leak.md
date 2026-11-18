---

publish: true
title: "WSL2 vmmem Memory Leak"
type: concept
tags: [wsl2, windows, memory, vmmem, troubleshooting]
sources: [sources/conversation/pc-power-waste-analysis.md]
related: ["[[Discord GPU Memory Issue]]", "[[HP Bloatware Services]]"]
created: "2026-11-18"
updated: "2026-11-18"
---

# WSL2 vmmem Memory Leak

## Overview

WSL2's `vmmem` process can consume 1+ GB of RAM even when all Linux distributions are reported as "Stopped" by `wsl --list --verbose`. This is a known memory leak where the VM doesn't properly release memory after distro shutdown.

## Details

### Symptoms
- `vmmem` process shows 1+ GB RAM usage in Task Manager
- `wsl --list --verbose` shows all distros as "Stopped"
- Memory not reclaimed until explicit shutdown

### Fix
```powershell
wsl --shutdown
```
This terminates the WSL2 lightweight utility VM completely, reclaiming ~1 GB RAM immediately.

### Root Cause
WSL2 runs a real Linux kernel in a lightweight VM. The VM's memory management doesn't always release pages back to Windows when distros stop, especially after intensive workloads (compilation, databases, containers).

### Prevention
- Run `wsl --shutdown` before sleep/hibernate
- Consider setting `autoMemoryReclaim=gradual` in `.wslconfig` (experimental)
- Monitor with `wsl --list --running` to confirm distros actually stopped

## Connections

- [[Discord GPU Memory Issue]] â€” another Windows memory leak pattern
- [[HP Bloatware Services]] â€” background services consuming resources

## Sources

- Conversation transcript: PC power waste analysis (2026-11-18)


