# 🌐 Module 01: Network Port Scanner

A CLI-based port scanning utility written in Python that interfaces with Nmap to perform host discovery, port state analysis, and service detection.

## 🚀 Features
* **Firewall Bypass:** Uses the `-Pn` flag to skip ICMP ping checks[cite: 3].
* **Fast Discovery:** Scans common ports quickly using `-F`[cite: 3].
* **Service Detection:** Identifies running service versions via `-sV`[cite: 3].
* **Interactive UI:** Displays results in styled terminal tables powered by `rich`[cite: 3].

## 🛠️ Prerequisites
* **Python 3.x**
* **Nmap** installed on system PATH
* Python Libraries: `python-nmap`, `rich`[cite: 3]

## 💻 Usage
```bash
python network_scanner.py

## Output

<img width="506" height="302" alt="image" src="https://github.com/user-attachments/assets/4bc76e8f-0521-44c2-9a89-a72a99910114" />

