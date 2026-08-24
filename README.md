# Automated Network & Port Scanner

A Python-based automated network reconnaissance tool that discovers active hosts and performs TCP port scanning using Nmap.

## Features

- Detects the local IP address
- Identifies the subnet mask
- Calculates the network address
- Performs network host discovery
- Identifies active hosts
- Performs TCP port scanning on discovered hosts

## Technologies Used

- Python
- Nmap
- ipcalc
- subprocess
- Regular Expressions (re)

## Workflow

```text
Get Local IP Address
        ↓
Get Subnet Mask
        ↓
Calculate Network Address
        ↓
Nmap Host Discovery
        ↓
Identify Active Hosts
        ↓
TCP Port Scan
