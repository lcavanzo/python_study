import re

# Flags example
multi_line_log = """
Line 1: error occurred
Line 2: Warning here
Line 3: Error critical
"""

# Case-insensitive search for 'error'
print(re.findall(r"error", multi_line_log, re.IGNORECASE))
# Output: ['error', 'ERROR']

# Multiline match for lines starting with 'Warning'
print(re.findall(r"Warning", multi_line_log, re.MULTILINE))
# Output: ['Warning']

# Verbose regex for readability (IP address validation)
# This is a basic IP pattern for demonstration, full validation is more complex.
verbose_ip_pattern = re.compile(
    r"""
    ^                           # Start of the string/line
    (\d{1,3})                   # First octet (1-3 digits)
    \.                          # Dot literal
    (\d{1,3})                   # Second octet
    \.
    (\d{1,3})                   # Third octet
    \.
    (\d{1,3})                   # Fourth octet
    $                           # End of the string/line
""",
    re.VERBOSE,
)

ip_address_test = "192.168.1.1"
match = verbose_ip_pattern.match(ip_address_test)
if match:
    print(f"Valid IP format: {match.groups()}")
else:
    print("Invalid IP format.")
# Output: Valid IP format: ('192', '168', '1', '1')
