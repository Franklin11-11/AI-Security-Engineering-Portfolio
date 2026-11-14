# Python-Based Security Log Analyser

## Project Overview
This project demonstrates basic security log analysis and automated detection of repeated failed login attempts using Python.

It was developed as part of my AI Security Engineering learning journey.

## Objectives
- Read and analyse authentication log files.
- Identify failed login attempts.
- Extract source IP addresses.
- Count failed login attempts per IP address.
- Detect suspicious login patterns using a configurable threshold.
- Generate and save an automated security report.

## Technologies Used
- Kali Linux
- Python 3
- Python Collections Module
- Nano Text Editor

## Project Structure

```text
day2-practice/
├── auth.log
├── login_monitor.py
├── log_analyzer.py
├── security_report.txt
└── README.md
```

## How It Works

1. The script reads the authentication log file.
2. It searches for entries marked `FAILED`.
3. It extracts the source IP address.
4. It counts failed attempts associated with each IP.
5. It flags IP addresses with five or more failed attempts.
6. It generates a timestamped report and saves it as `security_report.txt`.

## Detection Threshold

The current alert threshold is five failed login attempts.

## Sample Results

| IP Address | Failed Attempts | Result |
|---|---:|---|
| 192.168.1.25 | 4 | Below threshold |
| 10.0.0.8 | 5 | Suspicious activity alert |

Summary:
- Total failed login attempts: 9
- Unique IP addresses: 2
- IP addresses triggering alerts: 1

## How to Run

From the main project directory:

```bash
python day2-practice/log_analyzer.py
```

The generated report will be saved to:

```text
day2-practice/security_report.txt
```

## Security Relevance

Repeated failed login attempts can indicate brute-force activity or unauthorised access attempts.

This project demonstrates foundational SOC automation concepts, including log parsing, event counting, threshold-based detection and security reporting.

## Limitations

- Uses fictional sample authentication logs.
- Applies a simple threshold-based detection method.
- Does not perform real-time monitoring.
- Does not establish whether an IP address is malicious.

## Future Improvements

- Add real-time log monitoring.
- Support multiple log formats.
- Add configurable alert thresholds.
- Export reports in CSV or JSON.
- Integrate with a SIEM platform.

## Author
Franklin Chukwuemeka

AI Security Engineering Learning Portfolio
