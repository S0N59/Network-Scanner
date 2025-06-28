import os
import platform
import concurrent.futures
from datetime import datetime

# Determine ping command options based on the operating system
PING_COUNT_PARAM = "-n" if platform.system().lower() == "windows" else "-c"
PING_TIMEOUT_PARAM = "-w" if platform.system().lower() == "windows" else "-W"

# Scan configuration
SUBNET = "192.168.10"
MAX_WORKERS = 100
TIMEOUT = 1  # seconds per ping

# Log file for results
LOG_FILE = "scan_results.txt"

def ping(ip: str) -> tuple[str, bool]:
    """Pings an IP address and returns a tuple (IP, is_reachable)."""
    command = f"ping {PING_COUNT_PARAM} 1 {PING_TIMEOUT_PARAM} {TIMEOUT} {ip} > /dev/null 2>&1"
    response = os.system(command)
    return ip, response == 0

def scan_network():
    """Scans the subnet and prints lists of active and inactive IP addresses."""
    active_ips = []
    inactive_ips = []

    print(f"\nScanning subnet {SUBNET}.0/24...\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(ping, f"{SUBNET}.{i}") for i in range(1, 255)]

        for future in concurrent.futures.as_completed(futures):
            ip, is_active = future.result()
            if is_active:
                active_ips.append(ip)
                print(f"{ip} is reachable")
            else:
                inactive_ips.append(ip)

    print("\nScan results:")
    print("\nActive IP addresses:")
    for ip in sorted(active_ips):
        print(f"  {ip}")

    print("\nInactive or unreachable IP addresses:")
    for ip in sorted(inactive_ips):
        print(f"  {ip}")

    save_results(active_ips, inactive_ips)

def save_results(active_ips: list[str], inactive_ips: list[str]):
    """Saves scan results to a log file."""
    with open(LOG_FILE, "w") as log:
        log.write(f"Scan results for {SUBNET}.0/24 - {datetime.now()}\n\n")

        log.write("Active IP addresses:\n")
        for ip in sorted(active_ips):
            log.write(f"{ip}\n")

        log.write("\nInactive or unreachable IP addresses:\n")
        for ip in sorted(inactive_ips):
            log.write(f"{ip}\n")

    print(f"\nResults saved to {LOG_FILE}")

if __name__ == "__main__":
    scan_network()