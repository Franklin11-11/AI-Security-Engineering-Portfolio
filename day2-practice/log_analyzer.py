from collections import Counter
from datetime import datetime

log_file = "day2-practice/auth.log"
report_file = "day2-practice/security_report.txt"

failed_logins = []

with open(log_file, "r") as file:
    for line in file:
        if "FAILED" in line:
            ip_address = line.strip().split()[-1]
            failed_logins.append(ip_address)

login_counts = Counter(failed_logins)

threshold = 5
alert_ips = []

report = []

report.append("AI SECURITY LOG ANALYSIS REPORT")
report.append("=" * 35)
report.append(f"Report generated: {datetime.now()}")
report.append("")

for ip, count in login_counts.items():
    report.append(f"IP Address: {ip}")
    report.append(f"Failed Attempts: {count}")

    if count >= threshold:
        report.append("STATUS: ALERT - Suspicious activity")
        alert_ips.append(ip)
    else:
        report.append("STATUS: Below alert threshold")

    report.append("")

report.append("SECURITY SUMMARY")
report.append("-" * 20)
report.append(f"Total failed login attempts: {len(failed_logins)}")
report.append(f"Unique IP addresses: {len(login_counts)}")
report.append(f"IP addresses triggering alerts: {len(alert_ips)}")

with open(report_file, "w") as file:
    file.write("\n".join(report))

print("\n".join(report))
print(f"\nReport saved successfully to: {report_file}")
