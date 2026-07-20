<div align="center">

# 🎯 AutoRecon-AI — Complete Command Reference

*Every command, flag, and one-liner for the full recon → vuln scan → AI analysis pipeline.*

</div>

---

## 📑 Table of Contents

- [⚡ Quick Start](#-quick-start)
- [🔍 Subdomain Enumeration](#-subdomain-enumeration)
- [🌐 Live Host Probing](#-live-host-probing)
- [🔒 Vulnerability Scanning](#-vulnerability-scanning)
- [📁 Directory & URL Discovery](#-directory--url-discovery)
- [🛠️ Port Scanning & OSINT](#️-port-scanning--osint)
- [📄 File Checks & Info Gathering](#-file-checks--information-gathering)
- [🧠 AI Assistant Commands](#-ai-assistant-commands)
- [📂 Output & Results](#-output--results)
- [🔧 Troubleshooting](#-troubleshooting)
- [🚀 One-Liner Power Scans](#-one-liner-power-scans)
- [📋 Multi-Target Workflow](#-multi-target-workflow)

---

## ⚡ Quick Start

The four commands you'll use 90% of the time:

```bash
hunt example.com                    # Quick subdomain scan
hunt example.com full               # Full scan with nuclei
ai-assistant analyze example.com    # AI analysis of results
ai-assistant payloads xss           # Generate XSS payloads
```

---

## 🔍 Subdomain Enumeration

### Subfinder

| Command | Description |
|---|---|
| `subfinder -d example.com` | Basic scan |
| `subfinder -d example.com -all` | Query all sources |
| `subfinder -d example.com -all -silent` | Silent mode (clean output) |
| `subfinder -d example.com -all -silent -o subdomains.txt` | Output to file |
| `subfinder -dL domains.txt -all -silent -o all_subdomains.txt` | Multiple domains from a list |
| `subfinder -d example.com -s crtsh,shodan` | Query specific sources only |
| `subfinder -d example.com -recursive` | Recursive subdomain discovery |

### Amass

| Command | Description |
|---|---|
| `amass enum -passive -d example.com` | Passive enumeration only |
| `amass enum -active -d example.com` | Active enumeration |
| `amass enum -brute -d example.com` | Brute-force subdomains |
| `amass enum -passive -active -brute -d example.com` | All techniques combined |
| `amass enum -passive -d example.com -o amass_results.txt` | Output to file |
| `amass enum -brute -w wordlist.txt -d example.com` | Custom wordlist |
| `amass enum -passive -df domains.txt` | Multiple domains from a file |

### Assetfinder

| Command | Description |
|---|---|
| `assetfinder example.com` | Basic scan |
| `assetfinder --subs-only example.com` | Subdomains only |
| `assetfinder --domains-only example.com` | Root domains only |
| `assetfinder --subs-only example.com > assetfinder_results.txt` | Output to file |

### DNSGen — Subdomain Permutations

| Command | Description |
|---|---|
| `dnsgen subdomains.txt` | Generate permutations from a subdomain list |
| `dnsgen -f subdomains.txt example.com` | Generate with target domain context |
| `dnsgen subdomains.txt > permutations.txt` | Output to file |
| `dnsgen -f subdomains.txt -w wordlist.txt example.com` | Custom wordlist |

### Shuffledns — DNS Validation

| Command | Description |
|---|---|
| `shuffledns -d example.com -list subdomains.txt` | Validate subdomains resolve |
| `shuffledns -d example.com -list subdomains.txt -r resolvers.txt` | Custom resolvers |
| `shuffledns -d example.com -list subdomains.txt -threads 100` | Concurrent threads |
| `shuffledns -d example.com -list subdomains.txt -o validated.txt` | Output to file |
| `shuffledns -d example.com -list subdomains.txt -silent` | Quiet mode |
| `shuffledns -d example.com -list subdomains.txt -rate 50` | Rate limiting |

---

## 🌐 Live Host Probing

### HTTPX

| Command | Description |
|---|---|
| `httpx -u https://example.com` | Basic liveness check |
| `httpx -l subdomains.txt` | Check multiple hosts |
| `httpx -l subdomains.txt -status-code` | Show HTTP status codes |
| `httpx -l subdomains.txt -title` | Show page titles |
| `httpx -l subdomains.txt -tech-detect` | Detect technologies in use |
| `httpx -l subdomains.txt -threads 50 -status-code -title -tech-detect -silent -o live_hosts.txt` | ⭐ Full combo (recommended default) |
| `httpx -l subdomains.txt -follow-redirects` | Follow redirects |
| `httpx -l subdomains.txt -timeout 10` | Custom timeout |
| `httpx -l subdomains.txt -method POST -body "test=1"` | Override HTTP method |
| `httpx -l subdomains.txt -header "User-Agent: CustomAgent"` | Custom header |
| `httpx -l subdomains.txt -match-status 200,301,302` | Match specific status codes |
| `httpx -l subdomains.txt -json -o results.json` | JSON output |
| `httpx -l subdomains.txt -ports 80,443,8080,8443` | Check multiple ports |

### Httprobe

| Command | Description |
|---|---|
| `httprobe -c 50 example.com` | Basic probe, 50 concurrent |
| `httprobe -c 50 < domains.txt` | Probe from a domain list |
| `httprobe -c 50 < domains.txt > live_hosts.txt` | Output to file |

---

## 🔒 Vulnerability Scanning

### Nuclei

| Command | Description |
|---|---|
| `nuclei -u https://example.com` | Basic scan against one target |
| `nuclei -l hosts.txt` | Scan a list of hosts |
| `nuclei -l hosts.txt -severity critical,high,medium` | Filter by severity |
| `nuclei -u https://example.com -t cves/ -t exposures/` | Use specific template categories |
| `nuclei -update-templates` | Update the template library |
| `nuclei -l hosts.txt -o results.txt` | Output to file |
| `nuclei -l hosts.txt -json -o results.json` | JSON output |
| `nuclei -l hosts.txt -c 50` | Concurrency |
| `nuclei -l hosts.txt -rl 10` | Rate limit (requests/sec) |
| `nuclei -l hosts.txt -exclude-tags dos` | Exclude noisy/risky template tags |
| `nuclei -u https://example.com -t /path/to/templates` | Custom template directory |
| `nuclei -u https://example.com -silent` | Silent mode |
| `nuclei -u https://example.com -match-only` | Show only matched findings |
| `nuclei -l hosts.txt -resume results.json` | Resume an interrupted scan |
| `nuclei -u https://example.com -v` | Verbose output |

> ⚠️ Always run `nuclei -update-templates` before a scan — stale templates miss recently disclosed CVEs.

### Dalfox — XSS Detection

| Command | Description |
|---|---|
| `dalfox url https://example.com` | Basic XSS scan |
| `dalfox file urls.txt` | Scan a list of URLs |
| `dalfox url https://example.com -o results.txt` | Output to file |
| `dalfox url https://example.com -p payloads.txt` | Custom payload list |
| `dalfox url https://example.com -b https://xss.ht` | Blind XSS callback |
| `dalfox file urls.txt -w 30` | Concurrency |
| `dalfox url https://example.com -silence` | Silent mode |
| `dalfox url https://example.com --only-poc` | Show only proof-of-concept results |
| `dalfox url https://example.com -v` | Verbose |

### SQLMap

| Command | Description |
|---|---|
| `sqlmap -u "https://example.com/page?id=1"` | Basic SQLi test |
| `sqlmap -u "https://example.com/page?id=1" --dbs` | Enumerate databases |
| `sqlmap -u "https://example.com/page?id=1" -D dbname --tables` | Enumerate tables |
| `sqlmap -u "https://example.com/page?id=1" -D dbname -T tablename --dump` | Dump table data |
| `sqlmap -u "https://example.com" --crawl=3` | Crawl site for injectable parameters |
| `sqlmap -u "https://example.com/login" --data="user=admin&pass=test"` | Test a POST request |
| `sqlmap -u "https://example.com/page?id=1" --cookie="session=abc123"` | Authenticated scan via cookie |
| `sqlmap -u "https://example.com/page?id=1" --random-agent` | Randomize user-agent |
| `sqlmap -u "https://example.com/page?id=1" --batch` | Non-interactive mode |
| `sqlmap -u "https://example.com/page?id=1" --threads=10` | Threads |
| `sqlmap -u "https://example.com/page?id=1" --timeout=30` | Timeout |
| `sqlmap -u "https://example.com/page?id=1" --output-dir=./sqlmap_results` | Custom output directory |
| `sqlmap -u "https://example.com/page?id=1" --resume` | Resume a previous scan |

---

## 📁 Directory & URL Discovery

### Ffuf — Directory/File Fuzzing

| Command | Description |
|---|---|
| `ffuf -u https://example.com/FUZZ -w wordlist.txt` | Basic fuzzing |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -e .php,.html,.txt` | Add file extensions |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -fc 404,403` | Filter out status codes |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -mc 200,301` | Match specific status codes |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -t 50` | Threads |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -d 0.1` | Delay between requests |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -H "User-Agent: Custom"` | Custom header |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -b "session=abc123"` | Cookie/session |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -o results.json -of json` | JSON output |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -recursion` | Recursive fuzzing |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -s` | Silent mode |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt -c` | Colorized output |

### GAU — Get All URLs

| Command | Description |
|---|---|
| `gau example.com` | Basic URL discovery |
| `gau example.com > urls.txt` | Output to file |
| `gau example.com test.com` | Multiple domains |
| `gau -f domains.txt` | Domains from a file |
| `gau example.com --silent` | Silent mode |
| `gau example.com --fc 404,403` | Filter by status code |
| `gau example.com --providers wayback,commoncrawl,alienvault` | Specific data sources |

### Hakrawler

| Command | Description |
|---|---|
| `hakrawler -url https://example.com` | Basic crawl |
| `hakrawler -url https://example.com -depth 3` | Set crawl depth |
| `hakrawler -url https://example.com -out urls.txt` | Output to file |
| `hakrawler -url https://example.com -threads 20` | Threads |
| `hakrawler -url https://example.com -follow` | Follow redirects |
| `echo "example.com" \| hakrawler -wayback` | Pull URLs from the Wayback Machine |

### Paramspider — Parameter Discovery

| Command | Description |
|---|---|
| `paramspider -d example.com` | Discover parameters |
| `paramspider -d example.com -o params.txt` | Output to file |
| `paramspider -d example.com -l domains.txt` | Multiple domains |
| `paramspider -d example.com -e json,xml` | Extract specific formats |

### Arjun — Parameter Discovery

| Command | Description |
|---|---|
| `arjun -u https://example.com` | Basic parameter discovery |
| `arjun -u https://example.com -t 50` | Threads |
| `arjun -u https://example.com -m GET` | HTTP method |
| `arjun -u https://example.com -w wordlist.txt` | Custom wordlist |
| `arjun -u https://example.com -o params.txt` | Output to file |

---

## 🛠️ Port Scanning & OSINT

### Nmap

| Command | Description |
|---|---|
| `nmap -sV example.com` | Quick service version scan |
| `nmap -sC -sV -p- example.com` | Full port range + default scripts |
| `nmap -sS -sV -p 80,443,8080 example.com` | Specific ports |
| `nmap -sV -Pn example.com` | Skip host discovery (treat as up) |
| `nmap -sV -T4 example.com` | Aggressive timing |
| `nmap -sV -oN scan.txt example.com` | Output to file |
| `nmap -sV -iL hosts.txt` | Multiple hosts from a list |

### Shodan

| Command | Description |
|---|---|
| `shodan search hostname:example.com` | Basic search |
| `shodan search "example.com" --limit 100` | Limit result count |
| `shodan host example.com` | Host details |
| `shodan domains example.com` | Domain details |

### Censys

| Command | Description |
|---|---|
| `censys search "example.com"` | Basic search |
| `censys view example.com` | Host details |
| `censys certificates example.com` | Certificate search |

---

## 📄 File Checks & Information Gathering

### Common Sensitive Files

```bash
curl -s https://example.com/robots.txt                # Robots.txt
curl -s https://example.com/.well-known/security.txt  # Security.txt
curl -s https://example.com/sitemap.xml               # Sitemap
curl -s https://example.com/.git/HEAD                 # Exposed Git repo
curl -s https://example.com/.env                      # Exposed environment file
curl -s https://example.com/.htaccess                 # HT Access file
curl -s https://example.com/.DS_Store                 # DS Store (macOS artifact)
curl -s https://example.com/backup.zip                # Backup archive
curl -s https://example.com/config.php                # Config file
```

### Certificate Transparency

```bash
curl -s "https://crt.sh/?q=%25.example.com&output=json" \
  | jq -r '.[].name_value' \
  | sed 's/\*\.//g' \
  | sort -u
```

### Wayback Machine

```bash
curl -s "http://web.archive.org/cdx/search/cdx?url=example.com/*&output=json&fl=original&collapse=urlkey" \
  | jq -r '.[1:][]'
```

---

## 🧠 AI Assistant Commands

### Analysis

| Command | Description |
|---|---|
| `ai-assistant analyze example.com` | Analyze results for a target |
| `ai-assistant analyze example.com /path/to/scan` | Analyze a specific scan directory |

### Payload Generation

| Command | Vulnerability Class |
|---|---|
| `ai-assistant payloads xss` | Cross-Site Scripting |
| `ai-assistant payloads sqli` | SQL Injection |
| `ai-assistant payloads ssti` | Server-Side Template Injection |
| `ai-assistant payloads ssrf` | Server-Side Request Forgery |
| `ai-assistant payloads idor` | Insecure Direct Object Reference |
| `ai-assistant payloads rce` | Remote Code Execution |
| `ai-assistant payloads lfi` | Local File Inclusion |
| `ai-assistant payloads xxe` | XML External Entity |

---

## 📂 Output & Results

### View Results

```bash
ls -la ~/bugbounty/                                  # List all scans
ls -la ~/bugbounty/example.com_*/                    # List a specific scan
cat ~/bugbounty/example.com_*/README.md              # View the report
cat ~/bugbounty/example.com_*/all_subdomains.txt     # View subdomains
cat ~/bugbounty/example.com_*/live_hosts.txt         # View live hosts
cat ~/bugbounty/example.com_*/vulnerabilities.txt    # View vulnerabilities
cat ~/bugbounty/example.com_*/ai_analysis.txt        # View AI analysis
```

### Open Results

```bash
open ~/bugbounty/example.com_*/            # Open scan folder in Finder
open ~/bugbounty/example.com_*/README.md   # Open the report
```

### Clean Up

```bash
rm -rf ~/bugbounty/example.com_*/                    # Delete a specific scan
rm -rf ~/bugbounty/*_$(date -v-30d +%Y%m%d)*        # Delete scans older than 30 days
```

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| Command not found after install | Fix `PATH` — see below |
| Permission denied running `hunt` / `ai-assistant` | Fix permissions — see below |
| Tool missing or broken | Reinstall — see below |
| Nuclei missing recent CVEs | `nuclei -update-templates` |

**Fix PATH issues:**
```bash
export PATH="$HOME/bin:$PATH"
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Fix permissions:**
```bash
chmod +x ~/bin/hunt
chmod +x ~/bin/ai-assistant
```

**Reinstall a single tool:**
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

**Reinstall all core tools:**
```bash
for tool in subfinder amass nuclei httpx assetfinder ffuf gau; do
    go install -v github.com/projectdiscovery/$tool/cmd/$tool@latest
done
```

**Update Nuclei templates:**
```bash
nuclei -update-templates
```

**Re-source your shell config:**
```bash
source ~/.zshrc
```

---

## 🚀 One-Liner Power Scans

**Complete recon in one command:**
```bash
subfinder -d example.com -all -silent | httpx -threads 50 -silent | nuclei -severity critical,high
```

**Find live hosts only:**
```bash
subfinder -d example.com -all -silent | httpx -threads 50 -silent -o live_hosts.txt
```

**Full pipeline with AI analysis:**
```bash
hunt example.com && ai-assistant analyze example.com
```

**Multi-target scan (sequential):**
```bash
for domain in $(cat targets.txt); do hunt $domain; done
```

**Multi-target scan (parallel, 10 at a time):**
```bash
cat targets.txt | parallel -j 10 "hunt {}"
```

---

## 📋 Multi-Target Workflow

**1. Create `targets.txt`:**
```text
example.com
test.com
demo.com
api.example.com
admin.example.com
```

**2. Run against all targets:**
```bash
while read domain; do hunt "$domain"; done < targets.txt
```

---

<div align="center">

*That's the full reference — bookmark this page.* 🎯

</div>
