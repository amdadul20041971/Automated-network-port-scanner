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




Requirements

Make sure the following tools are installed:

Python 3
Nmap
ipcalc
ifconfig
Install Nmap
sudo apt update
sudo apt install nmap
Install ipcalc
sudo apt install ipcalc
Usage

Clone the repository:

git clone https://github.com/amdadul20041971/Automated-network-port-scanner.git

Navigate to the project directory:

cd Automated-network-port-scanner

Run the script:

python3 network_scanner.py
Disclaimer

This project is created for educational purposes and authorized security testing only. Do not scan networks or systems without proper permission.

Author

Amdadul Huq Emon

Cybersecurity Enthusiast | Python | Network Security
