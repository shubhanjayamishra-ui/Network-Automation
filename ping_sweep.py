# My First Network Automation Script
# Ping Sweep Tool
# Author: Subham

import subprocess

def ping_host(host):
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True
    )
    if result.returncode == 0:
        print(f"{host} is UP ✅")
    else:
        print(f"{host} is DOWN ❌")

# List of hosts to ping
hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

for host in hosts:
    ping_host(host)