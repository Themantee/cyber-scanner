



# import sys
# import socket
# from datetime import datetime
# from core.port_scanner import scan_ports
# from core.risk_engine import calculate_risk
# from core.reporter import save_report
# from core.password_audit import audit_passwords

# COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python main.py <target> [password_file]")
#         sys.exit(1)

#     target = sys.argv[1]
#     password_file = sys.argv[2] if len(sys.argv) == 3 else None

#     try:
#         target_ip = socket.gethostbyname(target)
#     except socket.gaierror:
#         print("❌ Unable to resolve target")
#         sys.exit(1)

#     print(f"\nTarget: {target} ({target_ip})")
#     print(f"Scan started at: {datetime.now()}\n")

#     open_ports = scan_ports(
#         target_ip=target_ip,
#         ports=COMMON_PORTS,
#         threads=50
#     )

#     risk = calculate_risk(open_ports)

#     password_results = []
#     if password_file:
#         print("\n🔐 Running password security audit...")
#         password_results = audit_passwords(password_file)

#     report_file = save_report(
#         target=target,
#         target_ip=target_ip,
#         open_ports=open_ports,
#         risk=risk,
#         password_audit=password_results
#     )

#     print("\n===== SCAN SUMMARY =====")
#     print(f"Open Ports: {open_ports}")
#     print(f"Risk Level: {risk}")

#     if password_results:
#         weak = sum(1 for p in password_results if p["issues"] != ["OK"])
#         print(f"Weak Passwords Found: {weak}")

#     print(f"Report saved to: {report_file}")
#     print(f"Scan completed at: {datetime.now()}\n")

# if __name__ == "__main__":
#     main()









import sys
import socket
from datetime import datetime
from core.port_scanner import scan_ports
from core.risk_engine import calculate_risk
from core.reporter import save_report
from core.password_audit import audit_passwords

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

def show_help():
    print("""
Cyber Scanner — Modular Security Toolkit

Usage:
  python main.py <target>
  python main.py <target> <password_file>
  python main.py --help

Examples:
  python main.py testphp.vulnweb.com
  python main.py testphp.vulnweb.com passwords.txt

Features:
  - Multithreaded port scanning
  - Banner grabbing
  - Risk analysis
  - JSON reporting
  - Password security audit
""")
    sys.exit(0)

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()

    if len(sys.argv) < 2:
        show_help()

    target = sys.argv[1]
    password_file = sys.argv[2] if len(sys.argv) == 3 else None

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Unable to resolve target")
        sys.exit(1)

    print(f"\nTarget: {target} ({target_ip})")
    print(f"Scan started at: {datetime.now()}\n")

    open_ports = scan_ports(
        target_ip=target_ip,
        ports=COMMON_PORTS,
        threads=50
    )

    risk = calculate_risk(open_ports)

    password_results = []
    if password_file:
        print("\n🔐 Running password security audit...")
        password_results = audit_passwords(password_file)

    report_file = save_report(
        target=target,
        target_ip=target_ip,
        open_ports=open_ports,
        risk=risk,
        password_audit=password_results
    )

    print("\n===== SCAN SUMMARY =====")
    print(f"Open Ports: {open_ports}")
    print(f"Risk Level: {risk}")

    if password_results:
        weak = sum(1 for p in password_results if p["issues"] != ["OK"])
        print(f"Weak Passwords Found: {weak}")

    print(f"Report saved to: {report_file}")
    print(f"Scan completed at: {datetime.now()}\n")

if __name__ == "__main__":
    main()
