import socket
import subprocess
import platform
from datetime import datetime

def scan_network(network="192.168.1"):
    print(f"\nScanning network: {network}.0/24")
    print(f"Started at: {datetime.now()}\n")
    
    active_hosts = []
    
    for i in range(1, 255):
        ip = f"{network}.{i}"
        # Ping the IP
        param = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.run(
            ["ping", param, "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown"
            
            print(f"[+] Active: {ip} — {hostname}")
            active_hosts.append({"ip": ip, "hostname": hostname})
    
    print(f"\nTotal active hosts found: {len(active_hosts)}")
    return active_hosts

if __name__ == "__main__":
    scan_network()
