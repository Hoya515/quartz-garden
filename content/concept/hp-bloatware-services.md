---

publish: true
title: "HP Bloatware Services"
type: concept
tags: [hp, windows, bloatware, services, telemetry, performance]
sources: [sources/conversation/pc-power-waste-analysis.md]
related: ["[[WSL2 vmmem Memory Leak]]", "[[Discord GPU Memory Issue]]"]
created: "2026-11-18"
updated: "2026-11-18"
---

# HP Bloatware Services

## Overview

HP pre-installs 7 telemetry/bloatware services on consumer laptops that run continuously in the background, consuming CPU, memory, and network resources with minimal user benefit.

## Details

### Services to Disable (Safe to Disable)
| Service Name | Display Name | Description |
|--------------|--------------|-------------|
| `HPCommRecovery` | HP Comm Recover | Firmware recovery communication |
| `HPAppHelperCap` | HP App Helper Cap | App telemetry collection |
| `HPDiagsCap` | HP Diagnostics Cap | Hardware diagnostics telemetry |
| `HPNetworkCap` | HP Network Cap | Network usage telemetry |
| `HPOmenCap` | HP Omen Cap | Gaming hub telemetry (even on non-Omen) |
| `HPSysInfoCap` | HP System Info Cap | System inventory collection |
| `HpTouchpointAnalyticsService` | HP Touchpoint Analytics | User behavior analytics |

### Disable Commands (Admin PowerShell)
```powershell
# Stop and disable all 7 services
$services = @(
    "HPCommRecovery",
    "HPAppHelperCap",
    "HPDiagsCap",
    "HPNetworkCap",
    "HPOmenCap",
    "HPSysInfoCap",
    "HpTouchpointAnalyticsService"
)

foreach ($svc in $services) {
    Stop-Service -Name $svc -Force -ErrorAction SilentlyContinue
    Set-Service -Name $svc -StartupType Disabled -ErrorAction SilentlyContinue
}
```

### Impact
- **RAM**: ~50-150 MB combined
- **CPU**: Periodic spikes during telemetry uploads
- **Network**: Background telemetry traffic
- **Battery**: Prevents proper idle states

### Safety
All 7 services are safe to disable. They provide no critical functionality â€” only telemetry and "value-add" features that most users never use. HP hardware functions normally without them.

## Connections

- [[WSL2 vmmem Memory Leak]] â€” another background resource consumer
- [[Discord GPU Memory Issue]] â€” application-level memory leak

## Sources

- Conversation transcript: PC power waste analysis (2026-11-18)


