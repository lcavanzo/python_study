import re

# re.search
print("---TESTING re.search()---")
log_entry = "ERROR: [2023-10-27 11:30:05] Failed to connect to DB on 10.0.0.5."
pattern = (
    r"DB on (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # Pattern to capture an IP address
)

match = re.search(pattern, log_entry)

if match:
    print(f"Full match: {match.group(0)}")  # The entire matched string
    print(f"Captured IP address: {match.group(1)}")  # The first captured group (the IP)
else:
    print("No database connection error found.")

# SRE example: Identifying specific error patterns
critical_log = "CRITICAL: Service unavailable. Code: 503."
warning_log = "WARNING: Disk usage 90% on /dev/sda1."

# Pattern to find 'CRITICAL' followed by an error code
critical_pattern = r"CRITICAL: .*?Code: (\d{3})"
critical_match = re.search(critical_pattern, critical_log)

if critical_match:
    print(f"Critical error code: {critical_match.group(1)}")
else:
    print("No critical error code found.")

# re.match()
print("---Testing re.match()---")

# Matching the beginning of a log entry
log_start_pattern = r"^(INFO|ERROR|WARNING):"

info_log = "INFO: Application started."
error_log = "ERROR: Network unreachable."
# This won't match because the pattern doesn't start at the beginning
middle_match_log = "Some event occurred. INFO: Detailed message."

print(f"'{info_log}' matches start? {bool(re.match(log_start_pattern, info_log))}")
# Output: 'INFO: Application started.' matches start? True
print(f"'{error_log}' matches start? {bool(re.match(log_start_pattern, error_log))}")
# Output: 'ERROR: Network unreachable.' matches start? True
print(
    f"'{middle_match_log}' matches start? {bool(re.match(log_start_pattern, middle_match_log))}"
)
# Output: 'Some event occurred. INFO: Detailed message.' matches start? False

print("---Testing re.findall()---")
# Extracting all IP addresses from a text block
network_config = """
Server_A IP: 192.168.1.10
Server_B IP: 10.0.0.25
Router IP: 172.16.0.1
Invalid IP: 999.999.999.999
"""
ip_pattern = (
    r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"  # Word boundary \b ensures whole IPs
)

ip_addresses = re.findall(ip_pattern, network_config)
print(f"Found IP addresses: {ip_addresses}")
# Output: ['192.168.1.10', '10.0.0.25', '172.16.0.1', '999.999.999.999']
# Note: Regex validates format, not IP validity (e.g., 999.999.999.999 matches the pattern)

# Extracting all error codes and messages from multiple log lines
multi_error_logs = """
ERR: [1] Critical failure.
WARN: [2] Disk space low.
ERR: [10] Another critical error.
INFO: [0] No issues.
"""
error_pattern = r"ERR: \[(\d+)\] (.*)"  # Capture error code and message

all_errors = re.findall(error_pattern, multi_error_logs)
print(f"Found errors: {all_errors}")
# Output: [('1', 'Critical failure.'), ('10', 'Another critical error.')]

# Anonymizing sensitive data in logs
access_log = "User 'johndoe' logged in from IP 192.168.1.5. Session ID: abc123def."
# Replace username and IP with placeholders
anonymized_log = re.sub(r"User '\w+'", "User '[ANONYMIZED_USER]'", access_log)
anonymized_log = re.sub(
    r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "[ANONYMIZED_IP]", anonymized_log
)
print(f"Anonymized log: {anonymized_log}")
# Output: Anonymized log: User '[ANONYMIZED_USER]' logged in from IP [ANONYMIZED_IP]. Session ID: abc123def.

## re.sub()
print("TESTING re.sub()")
# Using a function as replacement (e.g., incrementing a version number)
version_string = "Service v1.2.3 released."


def increment_minor_version(match):
    major, minor, patch = map(int, match.groups())
    return f"v{major}.{minor + 1}.0"


new_version_string = re.sub(
    r"v(\d+)\.(\d+)\.(\d+)", increment_minor_version, version_string
)
print(f"New version string: {new_version_string}")
# Output: New version string: Service v1.3.0 released.

print("TESTING re.split()")
# Splitting log entries based on multiple delimiters
complex_log_line = "2023-10-27 | INFO | web-01: Operation_X completed (took 150ms)."
# Split by '|' or ':' or ' '
parts = re.split(
    r"\||\s*:\s*|\s+", complex_log_line
)  # Split by |, or ' : ', or whitespace
# Filter out empty strings that might result from multiple delimiters or leading/trailing spaces
filtered_parts = [part for part in parts if part]
print(f"Split parts: {filtered_parts}")
# Output: ['2023-10-27', 'INFO', 'web-01', 'Operation_X', 'completed', '(took', '150ms).']

print("TESTING re.compile()")
# Compiling a pattern for efficiency
ip_address_pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")

logs = [
    "Connection from 192.168.1.10 established.",
    "Data received from 10.0.0.5.",
    "Failed attempt from 172.16.0.200.",
]

for log in logs:
    match = ip_address_pattern.search(log)
    if match:
        print(f"Found IP in '{log}': {match.group(0)}")
# Output:
# Found IP in 'Connection from 192.168.1.10 established.': 192.168.1.10
# Found IP in 'Data received from 10.0.0.5.': 10.0.0.5
# Found IP in 'Failed attempt from 172.16.0.200.': 172.16.0.200
