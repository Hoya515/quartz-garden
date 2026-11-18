---

publish: true
title: "MuMuPlayer Android Emulator Service"
type: concept
tags: [mumuplayer, android, emulator, windows, service, bloatware]
sources: [sources/conversation/pc-power-waste-analysis.md]
related: ["[[HP Bloatware Services]]", "[[Discord GPU Memory Issue]]"]
created: "2026-11-18"
updated: "2026-11-18"
---

# MuMuPlayer Android Emulator Service

## Overview

MuMuPlayer (NetEase Android emulator) installs a Windows service `MuMuPlayerRemoteService` that runs automatically at boot, consuming resources even when the emulator is never used.

## Details

### Service
- **Name**: `MuMuPlayerRemoteService`
- **Display Name**: MuMu Player Remote Service
- **Behavior**: Auto-start at boot, runs in background

### Impact
- **RAM**: ~50-100 MB
- **CPU**: Idle polling
- **Network**: Checks for updates/phone-home

### Disable Commands (Admin PowerShell)
```powershell
Stop-Service -Name "MuMuPlayerRemoteService" -Force -ErrorAction SilentlyContinue
Set-Service -Name "MuMuPlayerRemoteService" -StartupType Disabled -ErrorAction SilentlyContinue
```

### When to Keep Enabled
Only if you use MuMuPlayer regularly for Android app testing/gaming. The service handles ADB bridging and clipboard sync between Windows and the emulator.

### Alternative Emulators
- **BlueStacks** â€” Similar background services
- **LDPlayer** â€” Similar background services
- **Google Android Emulator (SDK)** â€” No background service, manual launch only
- **Waydroid (WSL2)** â€” Runs in Linux VM, no Windows service

## Connections

- [[HP Bloatware Services]] â€” similar auto-start service pattern
- [[WSL2 vmmem Memory Leak]] â€” WSL-based Android alternative

## Sources

- Conversation transcript: PC power waste analysis (2026-11-18)


