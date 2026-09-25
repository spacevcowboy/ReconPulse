#!/usr/bin/env python3
import argparse
import socket
import subprocess
import sys
import requests
from datetime import datetime

def banner():
    print(r"""
    ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝
    ██████╔╝█████╗  ██║     ██║   ██║██████╔╝██║   ██║██║     ███████╗
    ██╔══██╗██╔══╝  ██║     ██║   ██║██╔═══╝ ██║   ██║██║     ╚════██║
    ██║  ██║███████╗╚██████╗╚██████╔╝██║     ╚██████╔╝███████╗███████║
    """)
    print("[-] Automated Recon & Footprinting Utility v1.0\n")

def check_target(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Target Resolved: {target} -> {ip}")
        return ip
    except socket.gaierror:
        print(f"[!] Error: Unable to resolve target {target}")
        sys.exit(1)

def http_recon(target):
    print("\n--- [ HTTP Headers & Security Audit ] ---")
    url = f"https://{target}"
    try:
        response = requests.get(url, timeout=5)
        print(f"[+] Status Code: {response.status_code}")
        print("[+] Key Security Headers Found:")
        headers_to_check = ['Server', 'Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options']
        for h in headers_to_check:
            val = response.headers.get(h, "Not Present")
            print(f"    - {h}: {val}")
    except requests.exceptions.RequestException:
        print(f"[!] HTTPS connection failed or timed out for {url}. Trying HTTP...")
        try:
            response = requests.get(f"http://{target}", timeout=5)
            print(f"[+] HTTP Status Code: {response.status_code}")
        except Exception:
            print("[!] HTTP/HTTPS requests failed entirely.")

def run_nmap(target_ip):
    print("\n--- [ Nmap Port Scan & Service Detection ] ---")
    print("[*] Running quick service scan on top common ports...")
    # Using safe, standard flags: -T4 for speed, -F for fast (top 100 ports), -sV for service version
    command = ["nmap", "-T4", "-F", "-sV", target_ip]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except FileNotFoundError:
        print("[!] Error: Nmap is not installed or not found in system PATH.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Nmap scan failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Automated Reconnaissance Tool")
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP address (e.g., scanme.nmap.org)")
    args = parser.parse_args()

    banner()
    start_time = datetime.now()
    
    ip = check_target(args.target)
    http_recon(args.target)
    run_nmap(ip)
    
    end_time = datetime.now()
    print(f"\n[+] Recon completed in {end_time - start_time}")

if __name__ == "__main__":
    main()