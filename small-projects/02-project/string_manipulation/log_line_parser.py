import re

# Regex to parse a log line like: "[TIMESTAMP] [SEVERITY] <ID> Message content"
# Example: "[2023-10-27T12:00:00] [ERROR] <ABC-123> Failed to process request."
log_pattern = re.compile(
    r"^\[(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\]\s+"
    r"\[(?P<severity>(INFO|WARNING|ERROR|CRITICAL))\]\s+"
    r"<(?P<id>[A-Z]{3}-\d{3})>\s+"
    r"(?P<message>.*)$"
)


# Function to extract log details
def parse_log_entry(log_entry: str) -> dict | None:
    match = log_pattern.match(log_entry)
    if match:
        return match.groupdict()
    return None
