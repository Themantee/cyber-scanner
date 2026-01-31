def calculate_risk(open_ports):
    if not open_ports:
        return "NONE"

    if len(open_ports) <= 2:
        return "LOW"

    if len(open_ports) <= 5:
        return "MEDIUM"

    return "HIGH"
