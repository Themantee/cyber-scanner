# import json
# from datetime import datetime
# from pathlib import Path

# def save_report(target, target_ip, open_ports, risk):
#     reports_dir = Path("reports")
#     reports_dir.mkdir(exist_ok=True)

#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     filename = reports_dir / f"scan_{target}_{timestamp}.json"

#     report_data = {
#         "target": target,
#         "ip_address": target_ip,
#         "scan_time": datetime.now().isoformat(),
#         "open_ports": open_ports,
#         "risk_level": risk
#     }

#     with open(filename, "w") as f:
#         json.dump(report_data, f, indent=4)

#     return filename








import json
from datetime import datetime
from pathlib import Path

def save_report(target, target_ip, open_ports, risk, password_audit=None):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = reports_dir / f"scan_{target}_{timestamp}.json"

    report_data = {
        "target": target,
        "ip_address": target_ip,
        "scan_time": datetime.now().isoformat(),
        "open_ports": open_ports,
        "risk_level": risk,
        "password_audit": password_audit or []
    }

    with open(filename, "w") as f:
        json.dump(report_data, f, indent=4)

    return filename
