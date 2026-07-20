<div align="center">

# 🎯 AutoRecon-AI

### Native macOS Bug Bounty Automation with AI-Powered Analysis

*One command. Full recon. AI-prioritized findings.*

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![macOS](https://img.shields.io/badge/platform-macOS-black.svg?logo=apple)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](#license)
[![Claude AI](https://img.shields.io/badge/AI-Claude%20Integrated-purple.svg?logo=anthropic)](#)
[![Go](https://img.shields.io/badge/Go-1.21+-00ADD8.svg?logo=go)](#)

</div>

---

## ⚠️ Disclaimer — Authorized Use Only

This tool is built **exclusively** for authorized security testing: bug bounty programs you are enrolled in, penetration tests covered by a signed Statement of Work, or infrastructure you own or have explicit written permission to test.

Running this toolkit against any system without explicit authorization is illegal in most jurisdictions. The author accepts no liability for misuse. **You are solely responsible for ensuring you have permission before pointing this at a target.**

---

## 📖 Overview

**AutoRecon-AI** is a native macOS reconnaissance and testing orchestrator that wraps industry-standard security tools behind a single command, then uses Claude AI to triage results, flag high-value targets, and suggest next testing steps mapped to the OWASP Web Security Testing Guide (WSTG).

Instead of manually chaining `subfinder` → `amass` → `httpx` → `nuclei` and cross-referencing output by hand, AutoRecon-AI runs the entire pipeline, normalizes the output, and asks Claude to reason over it — surfacing what's actually worth a human's time.

```mermaid
flowchart LR
    A[🎯 Target Input] --> B[🔍 AutoRecon-AI]
    B --> C[subfinder<br/>Subdomain Discovery]
    B --> D[amass<br/>Advanced Recon]
    B --> E[assetfinder<br/>Additional Enumeration]
    C --> F[📊 Combined Subdomains]
    D --> F
    E --> F
    F --> G[🌐 httpx<br/>Live Host Probing]
    G --> H[🔒 nuclei<br/>Vulnerability Scanning]
    H --> I[🧠 Claude AI Analysis]
    I --> J[📊 Prioritized Findings]
    I --> K[🧭 OWASP WSTG Mapping]
    I --> L[💡 Custom Payloads]
    J --> M[📄 Final Report]
    K --> M
    L --> M