# ReconPulse 🔍

**ReconPulse** is a lightweight, modular command-line reconnaissance utility built in Python. Designed for security professionals and administrators, it automates the initial phases of target assessment by combining DNS resolution, HTTP security header auditing, and structured Nmap service fingerprinting into a single workflow.

---

## 💻 Development Environment
Built with a clean, object-oriented script structure inside a modern text editor environment:

![VS Code Development Setup](path/to/your/vscode-screenshot.png)

---

## ⚡ Execution & Sample Output
Running the utility against an authorized target automatically validates the host, tests HTTPS/HTTP fallback headers, and invokes optimized Nmap service scans:

![Terminal Execution Output](path/to/your/terminal-screenshot.png)

```text
$ python3 recon.py -t scanme.nmap.org

    ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝
    ██████╔╝█████╗  ██║     ██║   ██║██████╔╝██║   ██║██║     ███████╗
    ██╔══██╗██╔══╝  ██║     ██║   ██║██╔═══╝ ██║   ██║██║     ╚╚══██║
    ██║  ██║███████╗╚██████╗╚██████╔╝██║     ╚██████╔╝███████╗███████║

[-] Automated Recon & Footprinting Utility v1.0

[+] Target Resolved: target-host -> [IP_ADDRESS]

--- [ HTTP Headers & Security Audit ] ---
[!] HTTPS connection failed or timed out. Trying HTTP...
[+] HTTP Status Code: 200

--- [ Nmap Port Scan & Service Detection ] ---
[*] Running quick service scan on top common ports...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH
80/tcp open  http    Apache httpd

[+] Recon completed successfully.
