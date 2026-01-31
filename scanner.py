import socket
import argparse
import sys
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

def banner_grab(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore")
        sock.close()
        return banner.strip()
    except:
        return None

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def risk_level(open_ports):
    risk = "LOW"
    if any(p in open_ports for p in [21, 23, 3306]):
        risk = "HIGH"
    elif len(open_ports) >= 3:
        risk = "MEDIUM"
    return risk

def run_scan(target):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(Fore.RED + "[-] Invalid target")
        sys.exit(1)

    print(Fore.CYAN + f"\nTarget: {target} ({ip})")
    print(Fore.CYAN + f"Scan started at: {datetime.now()}\n")

    open_ports = []

    for port, service in COMMON_PORTS.items():
        if scan_port(ip, port):
            print(Fore.GREEN + f"[OPEN] Port {port} ({service})")
            open_ports.append(port)

            banner = banner_grab(ip, port)
            if banner:
                print(Fore.YELLOW + f"       Banner: {banner.splitlines()[0]}")

        else:
            print(Fore.RED + f"[CLOSED] Port {port}")

    risk = risk_level(open_ports)

    print("\n" + Fore.MAGENTA + "===== SCAN SUMMARY =====")
    print(Fore.MAGENTA + f"Open Ports: {open_ports}")
    print(Fore.MAGENTA + f"Risk Level: {risk}")
    print(Fore.CYAN + f"Scan completed at: {datetime.now()}")

def main():
    parser = argparse.ArgumentParser(description="Python Network Security Scanner")
    parser.add_argument("target", help="Target domain or IP")
    args = parser.parse_args()
    run_scan(args.target)

if __name__ == "__main__":
    main()
