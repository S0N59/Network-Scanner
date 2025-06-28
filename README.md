# Network Scanner

A simple multithreaded Python script for scanning a local network to identify active and inactive IP addresses within a given subnet.

## Features
- Detects operating system to use correct ping command.
- Scans a configurable subnet (default: `192.168.10.0/24`).
- Utilizes multithreading for fast scanning.
- Prints and saves lists of reachable and unreachable IP addresses.

## Requirements
- Python 3.x
- Works on Windows, macOS, and Linux

## Usage
1. Edit the `SUBNET` variable in `find_ips.py` to match your network.
2. Run the script:

```bash
python3 find_ips.py
```

3. Results will be printed to the console and saved to `scan_results.txt`.

## Notes
- The script uses the system `ping` command, so it may require administrative privileges or firewall adjustments.
- Inactive IP addresses may simply be devices that block ping, not necessarily free IPs.

## License
This project is provided for educational purposes only.
