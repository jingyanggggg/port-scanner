# Multi-Threaded Python Port Scanner

Continuing my hands-on journey into cybersecurity, I built this simple TCP port scanner in Python. I started this project because I wanted to dive deeper into how network communication and services work at a fundamental level. This project helped me better understand TCP/IP, and how to utilize Python's `socket` and `threading` libraries to speed up network tasks.

## Features

* **Multi-threaded:** Uses Python's `threading` and `queue` modules to scan multiple ports concurrently, making it significantly faster than sequential scanning.
* **TCP Connect Scan:** Attempts a full TCP connection to determine if a port is open.
* **No External Dependencies:** Built entirely using Python's standard libraries (`socket`, `threading`, `queue`).

## Prerequisites

* Python 3.x installed on your machine.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/jingyanggggg/port-scanner.git
   cd port-scanner
   ```
2. Open `port-scanner.py` in your preferred text editor and update the configuration section:
   ```python
   # configuration
   target = "127.0.0.1" # <-- Replace with your target IP address
   ```

3. Run the script:
   ```bash
   python3 port-scanner.py
   ```
