import re

# Regex pattern for a basic IPv4 address (does not validate octet ranges beyond 0-999)
# A more robust pattern would validate each octet to be 0-255.
ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

# --- Test Cases ---
valid_ips = [
    "192.168.1.1",
    "0.0.0.0",
    "255.255.255.255",
    "10.1.2.3",
]

# Negative test cases (should not match)
invalid_ips = [
    "255.255.255",  # Too few octets
    "192.168.1.1.1",  # Too many octets
    "abc.def.ghi.jkl",  # Non-numeric
    "192.168.1",  # Missing octet
    ".1.2.3.4",  # Leading dot
    "1.2.3.4.",  # Trailing dot
    "192.168.1.256",  # Invalid octet value (format-wise it matches, content-wise it's invalid)
    " 1.2.3.4",  # Leading space
    "1.2.3.4 ",  # Trailing space
]

print("--- Running IP Address Regex Test ---")

# test positive cases
for ip in valid_ips:
    match = ip_pattern.match(ip)
    assert match is not None, f"FAIL: Expected '{ip}' to match, but it didn't."
    assert match.group(0) == ip, (
        f"Fail: Matched '{match.group(0)}' for '{ip}', expected '{ip}'"
    )
    print(f"PASS: '{ip}' matched as expected")

# Test negative cases
for ip in invalid_ips:
    match = ip_pattern.match(ip)
    assert match is None, (
        f"FAIL: Expected '{ip}' NOT to match, but it did. Matched: '{match.group(0)}'"
    )
    print(f"PASS: '{ip}' matched as expected")


print("--- All IP Address Regex Test Passed ---")
