# Detection content

- `encoded_powershell_sigma.yml` is a draft Sigma-style rule and **was not tested against a production EDR/SIEM**. The sample CSV uses `process_name` / `command_line`, not native Sigma `Image` / `CommandLine` fields. Field mapping is required.
- `vpn_failures_followed_by_success.spl` is illustrative SPL for a CSV lookup, **not run in Splunk**, and does not yet enforce failure-before-success ordering in a bounded window. Do not deploy as a production alert without additional logic and tuning.
