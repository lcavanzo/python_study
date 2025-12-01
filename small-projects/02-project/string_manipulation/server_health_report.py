"""
You have the following server monitoring data.
Create a formatted string for a health report that looks professional and readable.

Input Data
```python
server_name = "database-prod-01"
cpu_percent = 15.789
memory_gb_used = 12.5
total_memory_gb = 16.0
disk_usage_percent = 82.1
last_check_time = "2023-10-27 15:30:00"
```

Desired output formatted
```python
--- Server Health Report: database-prod-01 ---
CPU Usage:           15.79%
Memory Used:         12.50 GB / 16.00 GB
Disk Usage:          82.10%
Last Check:          2023-10-27 15:30:00
---------------------------------------------
```
"""

import re
import os

# Define constants at the module level for better visibility and potential reuse
LABEL_WIDTH = 15
VALUE_WIDTH = 10


def report_format(filename):
    """
    Reads server monitoring data from a file, parses it using regular expressions,
    and returns a professionally formatted health report string.

    Args:
        filename (str): Path to the file containing the server monitoring data.

    Returns:
        str: A professionally formatted server health report string, or None if an error occurs.
    """
    content = _read_file(filename)
    if not content:  # Check if file reading failed
        return None

    # Regex patterns - improved for robustness and focused capturing
    # Using non-capturing groups (?:...) for parts we don't need to extract
    pattern_server_name = re.compile(
        r"server_name = '([\w-]+)'"
    )  # More general for server names
    pattern_cpu = re.compile(r"cpu_percent = (\d+\.?\d*)")  # More specific for floats
    pattern_gb_used = re.compile(r"memory_gb_used = (\d+\.?\d*)")
    pattern_total_gb = re.compile(r"total_memory_gb = (\d+\.?\d*)")
    pattern_disk_usage = re.compile(r"disk_usage_percent = (\d+\.?\d*)")
    pattern_check_time = re.compile(
        r"last_check_time = '(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'"
    )

    # Store extracted data in a dictionary for clarity
    data = {}
    errors = []

    # Attempt to search and extract data for each pattern
    matches = {
        "server_name": pattern_server_name.search(content),
        "cpu_percent": pattern_cpu.search(content),
        "memory_gb_used": pattern_gb_used.search(content),
        "total_memory_gb": pattern_total_gb.search(content),
        "disk_usage_percent": pattern_disk_usage.search(content),
        "last_check_time": pattern_check_time.search(content),
    }

    for key, match in matches.items():
        if match:
            # For numerical values, convert immediately to float
            if key in [
                "cpu_percent",
                "memory_gb_used",
                "total_memory_gb",
                "disk_usage_percent",
            ]:
                data[key] = float(match.group(1))
            else:
                data[key] = match.group(1)  # For server_name and last_check_time
        else:
            errors.append(f"Could not find '{key}' in the report file.")

    if errors:
        print("Error(s) during data extraction:")
        for error in errors:
            print(f"- {error}")
        return None  # Return None if essential data is missing

    # Format the report string
    report_lines = []
    report_lines.append(f"--- Server Health Report: {data['server_name']} ---")
    report_lines.append(
        f"{'CPU Usage:':<{LABEL_WIDTH}} {data['cpu_percent']:>{VALUE_WIDTH}.2f}%"
    )
    report_lines.append(
        f"{'Memory Used:':<{LABEL_WIDTH}} {data['memory_gb_used']:>{VALUE_WIDTH}.2f} GB / {data['total_memory_gb']:.2f} GB"
    )
    report_lines.append(
        f"{'Disk Usage:':<{LABEL_WIDTH}} {data['disk_usage_percent']:>{VALUE_WIDTH}.2f}%"
    )
    report_lines.append(
        f"{'Last Check:':<{LABEL_WIDTH}} {data['last_check_time']:>{24}}"
    )
    report_lines.append("-" * 45)

    return "\n".join(report_lines)  # Return the formatted string


def _read_file(filename):
    """
    Reads the entire content of a specified file.
    Args:
        filename (str): The path to the file to read.
    Returns:
        str: The content of the file, or an empty string if an error occurs.
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File not found at '{filename}'.")
        return ""
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return ""


def _create_input_file(filename):
    """
    Creates a file with predefined server monitoring data.
    Args:
        filename (str): The path where the input file will be created.
    """
    try:
        with open(filename, "w") as f:
            f.write("server_name = 'database-prod-01'\n")
            f.write("cpu_percent = 15.789\n")
            f.write("memory_gb_used = 12.5\n")
            f.write("total_memory_gb = 16.0\n")
            f.write("disk_usage_percent = 82.1\n")
            f.write("last_check_time = '2023-10-27 15:30:00'\n")
    except Exception as e:
        print(f"Error creating file '{filename}': {e}")


# Demonstration
if __name__ == "__main__":
    report_file = "file-report.txt"
    _create_input_file(report_file)

    health_report = report_format(report_file)
    if health_report:
        print(health_report)
    else:
        print("Failed to generate server health report.")

    # Clean up the created file (optional, but good for demos)
    if os.path.exists(report_file):
        os.remove(report_file)
