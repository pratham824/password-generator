import subprocess
import sys
import os

# Subdomain Enumeration with Subfinder (Install: go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest)
def subdomain_enumeration(target):
    print(f"\n[+] Performing Subdomain Enumeration on {target}...")
    result = subprocess.run(['subfinder', '-d', target, '-silent'], capture_output=True, text=True)
    subdomains = result.stdout.splitlines()
    if subdomains:
        print(f"[+] Subdomains Found: {len(subdomains)}")
        for subdomain in subdomains:
            print(subdomain)
        return subdomains
    else:
        print("[-] No Subdomains Found.")
    return []

# Port Scanning with Nmap (Install: sudo apt install nmap)
def port_scanning(target):
    print(f"\n[+] Performing Port Scanning on {target}...")
    result = subprocess.run(['nmap', '-sS', '-T4', '-p-', target], capture_output=True, text=True)
    print(result.stdout)

# HTTP Status Code Checker using httpx (Install: go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest)
def check_http_status(subdomains):
    print("\n[+] Checking HTTP Status Codes for Subdomains...")
    for subdomain in subdomains:
        result = subprocess.run(['httpx', '-silent', '-status-code', '-title', subdomain], capture_output=True, text=True)
        if result.stdout:
            print(result.stdout.strip())

# Main function for target input and tool selection
def main():
    if len(sys.argv) != 2:
        print("Usage: python recon_tool.py <target>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    # Step 1: Subdomain Enumeration
    subdomains = subdomain_enumeration(target)
    
    # Step 2: HTTP Status Code Checking
    if subdomains:
        check_http_status(subdomains)
    
    # Step 3: Port Scanning (can be optional or run separately)
    port_scanning(target)

if __name__ == "__main__":
    main()
