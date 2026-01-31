import re
import math

COMMON_PATTERNS = [
    r"password",
    r"1234",
    r"admin",
    r"qwerty",
    r"letmein"
]

def password_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)

def audit_passwords(password_file):
    results = []

    try:
        with open(password_file, "r") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

    for pwd in passwords:
        issues = []

        if len(pwd) < 8:
            issues.append("Too short")

        for pattern in COMMON_PATTERNS:
            if re.search(pattern, pwd.lower()):
                issues.append("Common pattern")

        entropy = password_entropy(pwd)

        if entropy < 40:
            issues.append("Low entropy")

        results.append({
            "password": "*" * len(pwd),
            "length": len(pwd),
            "entropy": entropy,
            "issues": issues if issues else ["OK"]
        })

    return results
