#!/usr/bin/env python3
"""Offline, reproducible triage against synthetic sample CSVs. No internet required."""
import csv
from pathlib import Path
from collections import Counter
root=Path(__file__).resolve().parents[1]/'data'
def load(name):
    with (root/name).open(newline='') as file: return list(csv.DictReader(file))
auth=load('authentication.csv'); processes=load('process_events.csv'); network=load('network_connections.csv'); dns=load('dns_events.csv')
fail=[r for r in auth if r['username']=='j.park' and r['source_ip']=='203.0.113.77' and r['result']=='Failure' and r['logon_type']=='VPN']
success=[r for r in auth if r['username']=='j.park' and r['source_ip']=='203.0.113.77' and r['result']=='Success' and r['logon_type']=='VPN']
print('VPN failures:',len(fail),'first:',min(r['timestamp_utc'] for r in fail),'last:',max(r['timestamp_utc'] for r in fail))
print('VPN successes:',[r['timestamp_utc'] for r in success])
print('WS-101 suspicious process events:')
for r in processes:
 if r['host']=='WS-101' and '2026-10-19T13:10'<=r['timestamp_utc']<='2026-10-19T13:20': print(r)
print('WS-101 destination network events:')
for r in network:
 if r['host']=='WS-101' and r['destination_ip']=='198.51.100.88': print(r)
print('WS-101 DNS events in 13:10-13:20:')
for r in dns:
 if r['host']=='WS-101' and '2026-10-19T13:10'<=r['timestamp_utc']<='2026-10-19T13:20': print(r)
print('NOTE: Network CSV has no PID; process-to-network attribution is a supplemental exercise scenario.')
