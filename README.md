# SOC Incident Response & Threat Hunting Lab

**Portfolio case:** NS-SOC-001 | **Environment:** Northstar Technologies (entirely fictional) | **Data:** 100% synthetic | **Date of simulated event:** 2026-10-19 UTC

An evidence-driven junior SOC investigation of repeated VPN authentication failures, a subsequent successful login, encoded PowerShell execution, and outbound connections. This case demonstrates log triage, correlation, evidence handling, uncertainty management, and incident response recommendations.

> **Important:** This is an educational simulation, not a production security incident, real customer engagement, confirmed malware analysis, or demonstration of actual endpoint containment. Scenario-added evidence is separated from CSV-supported observations.

## Start here

1. Read [`reports/Final_Incident_Report.pdf`](reports/Final_Incident_Report.pdf) for the assessed case.
2. Open [`evidence/incident_timeline.csv`](evidence/incident_timeline.csv) to see timestamps and original CSV row numbers.
3. Inspect the synthetic source logs in [`data/`](data/).
4. Reproduce the investigation locally: `python scripts/analyze_case.py` (Python standard library only).
5. Review draft [`detections/`](detections/) and the caveats in the detection README.

## Case highlights

- 18 failed VPN authentications from `203.0.113.77` for `j.park` between 13:00 and 13:08 UTC, followed by a successful VPN authentication at 13:10 UTC.
- At 13:14 UTC, `WS-101` recorded `powershell.exe -NoProfile -EncodedCommand [REDACTED_SIMULATED]`; at 13:16 UTC, `cmd.exe /c whoami` was launched with `powershell.exe` listed as its parent.
- At 13:15 and 13:17 UTC, `WS-101` recorded TCP connections to `198.51.100.88:443`, with 32,541 and 52,802 recorded outbound bytes.
- The original network CSV **does not contain PID/process ownership**; a later **supplemental classroom scenario** associates the connections with PowerShell PID 4820 and includes employee denial of the VPN activity. Those supplements do not independently verify actual compromise.
- The final disposition is **high-priority suspected unauthorized activity; unresolved**. There is **no proof of C2 or exfiltration** in this dataset, and containment is recommended, not recorded as executed.

## Files

| File | Purpose |
|---|---|
| `data/*.csv` | Original synthetic VPN, DNS, process, and network records |
| `data/soc_events.sqlite` | Original synthetic SQLite event database |
| `scripts/analyze_case.py` | Reproducible local case queries |
| `evidence/incident_timeline.csv` | Events with original CSV row references |
| `evidence/scenario_supplements.csv` | Later exercise assumptions distinctly marked |
| `detections/encoded_powershell_sigma.yml` | Draft Sigma detection (not production validated) |
| `detections/vpn_failures_followed_by_success.spl` | Illustrative Splunk query (not executed in Splunk) |
| `reports/Final_Incident_Report.pdf` | Final assessment and response plan |

## Skills demonstrated

Security log analysis, basic DFIR chronology, endpoint-to-network correlation, threat hunting hypotheses, incident escalation, and defensible executive reporting. No real IP enrichment is attempted: the public-range sample addresses are reserved for documentation.

## Open questions

MFA result and legitimacy of the VPN session; complete decoded PowerShell content; genuine DNS answer mapping; trustworthy EDR PID-to-network evidence; lateral movement; actual file access; any data transfer contents; containment and recovery verification.
