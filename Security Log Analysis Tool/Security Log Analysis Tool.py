import re
from collections import defaultdict

class SecurityLogAnalyzer:
    def __init__(self, log_file, output_file):
        self.log_file = log_file
        self.output_file = output_file
        self.failed_logins = defaultdict(int)
        self.suspicious_ips = defaultdict(int)
        self.threshold_failed_logins = 5  # Threshold for failed login attempts
        self.suspicious_ip_patterns = [r"192\.168\.1\.\d+", r"10\.0\.0\.\d+"]  # Example suspicious IP patterns

    def analyze_logs(self):
        """Analyze the security logs for potential threats."""
        try:
            with open(self.log_file, 'r') as file:
                for line in file:
                    self._check_failed_logins(line)
                    self._check_suspicious_ips(line)
            print("Log analysis completed.")
        except Exception as e:
            print(f"Error reading log file: {e}")

    def _check_failed_logins(self, line):
        """Check for failed login attempts."""
        if "Failed login" in line:
            ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if ip_match:
                ip = ip_match.group()
                self.failed_logins[ip] += 1

    def _check_suspicious_ips(self, line):
        """Check for suspicious IP addresses."""
        for pattern in self.suspicious_ip_patterns:
            ip_match = re.search(pattern, line)
            if ip_match:
                ip = ip_match.group()
                self.suspicious_ips[ip] += 1

    def generate_report(self):
        """Generate a report of potential threats."""
        try:
            with open(self.output_file, 'w') as file:
                file.write("Security Log Analysis Report\n")
                file.write("==========================\n\n")

                # Report failed login attempts
                file.write("Failed Login Attempts:\n")
                for ip, count in self.failed_logins.items():
                    if count >= self.threshold_failed_logins:
                        file.write(f"IP: {ip}, Attempts: {count}\n")
                file.write("\n")

                # Report suspicious IP addresses
                file.write("Suspicious IP Addresses:\n")
                for ip, count in self.suspicious_ips.items():
                    file.write(f"IP: {ip}, Occurrences: {count}\n")
                file.write("\n")

            print(f"Report generated and saved to {self.output_file}")
        except Exception as e:
            print(f"Error generating report: {e}")

    def run(self):
        """Run the log analysis and generate a report."""
        self.analyze_logs()
        self.generate_report()

if __name__ == "__main__":
    # Specify log file and output report file paths
    log_file = "C:security.log"  # Replace with your log file path
    output_file = "C:security_report.txt"  # Replace with your output file path

    # Create an instance of SecurityLogAnalyzer and run the analysis
    analyzer = SecurityLogAnalyzer(log_file, output_file)
    analyzer.run()