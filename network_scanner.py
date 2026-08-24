#================================
#---------> ifconfig

import subprocess
import re

command_ifconfig = ["ifconfig"]

output = subprocess.run(command_ifconfig, capture_output=True,text=True)

match_eth0= re.search(r"eth0:.*\n\s+inet\s+(\d+\.\d+\.\d+\.\d+)", output.stdout)

match_Subnetmask= re.search(r"netmask\s(\d+\.\d+\.\d+\.\d+)", output.stdout)

IP_Address = match_eth0.group(1)
Subnet_Mask = match_Subnetmask.group(1)

print(f"IP Address : {IP_Address}")

print(f"Subnet Mask: {Subnet_Mask}")

#====================================
#-----------------> ipcalce

ipcalc = ["ipcalc", f"{IP_Address}/{Subnet_Mask}"]

Result = subprocess.run(ipcalc, capture_output=True, text=True)

match_network= re.search(r"Network:\s+(\d+\.\d+\.\d+\.\d+)/(\d+)", Result.stdout)

#                        r"Network:\s+(\d+\.\d+\.\d+\.\d+)/(\d+)"

Network = match_network.group(1)
prefix = match_network.group(2)

print(f"Network Address: {Network}/{prefix}\n\n")

#====================================t
#-----------------> Nmap

nmap = ["nmap", "-sn", f"{Network}/{prefix}"]

nmap_output = subprocess.run(nmap, capture_output=True, text=True)

#nmap_match = re.search()

print("\n------------------------Nmap Output---------------------\n")

print(f"Network Scaning Result{nmap_output.stdout}")

#====================================t
#-----------------> Active Host Show

host_ips = re.findall(r"Nmap scan report for\s+(\d+\.\d+\.\d+\.\d+)",nmap_output.stdout)

print("\n---------------- Active Hosts ----------------\n")

for Host in host_ips:
    print(f"Active Host: {Host}")

    #====================================
    #-----------------> Hosts Port Scan

    Port_scan = ["nmap", "-sT", Host]

    result = subprocess.run(
        Port_scan,
        capture_output=True,
        text=True
    )

    print("\n------------------------Port Scan---------------------\n")

    print(f"Output:\n\n{result.stdout}")







