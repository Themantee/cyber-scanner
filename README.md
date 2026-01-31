# 🔐 Cyber Scanner

A modular, Python-based cybersecurity toolkit designed for **defensive security analysis** and **educational use**.

This project demonstrates real-world security engineering concepts, including
network scanning, multithreading, banner analysis, risk assessment, structured reporting,
and password hygiene auditing — all built without external scanning tools.

---

## 📌 Why This Project Exists

Many security students rely heavily on tools without understanding how they work.
This project was built to demonstrate **how core security tools are implemented internally**
using Python and networking fundamentals.

It is designed to be:
- Educational
- Ethical
- Interview-ready
- Extensible

---

## 🚀 Features

- 🔍 **Multithreaded TCP Port Scanning**
- 🧾 **Service Banner Grabbing**
- ⚠️ **Risk Level Assessment**
- 📊 **Structured JSON Reporting**
- 🔐 **Password Security Audit**
  - Length checks
  - Common pattern detection
  - Entropy analysis
- 🧱 **Clean Modular Architecture**
- 🖥️ **Command-Line Interface with Help Mode**

---

## 🧠 Technical Highlights

- Built using **Python standard libraries**
- Uses `socket` programming for low-level networking
- Optimized using `ThreadPoolExecutor`
- Designed for **defensive security and auditing**
- Outputs reports suitable for SOC / SIEM pipelines

---

## 🛠️ Installation

### Requirements
- Python 3.9+
- macOS / Linux / Windows

### Setup
```bash
git clone https://github.com/YOUR_USERNAME/cyber-scanner.git
cd cyber-scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
