"""Starter script for simulated Northstar SOC lab: no external dependencies."""
import csv
from collections import Counter
from pathlib import Path
DATA=Path(__file__).resolve().parents[1]/"data"
with (DATA/"authentication.csv").open(newline="") as f:
    rows=list(csv.DictReader(f))
failures=Counter((r["username"],r["source_ip"]) for r in rows if r["result"]=="Failure")
print("Highest failed-authentication counts by account/source IP:")
for (user,ip),count in failures.most_common(8):
    print(f"{user:12} {ip:18} {count:3}")
print("\nNext: inspect authentication.csv for successes from the same account/IP.")
