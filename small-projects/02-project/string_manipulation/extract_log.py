"""
From the given log entries, extract the timestamp, log level, and the main message.

Input Data:

log_entry_1 = "2023-10-27T16:05:30Z [INFO] User 'admin' logged in successfully."
log_entry_2 = "2023-10-27T16:06:15Z [ERROR] Failed to connect to service 'auth-api': Connection refused."
log_entry_3 = "2023-10-27T16:07:00Z [WARNING] Disk space low on /var/log."

Desired Output: For each entry, print: Timestamp: <extracted_timestamp> Level: <extracted_level> Message: <extracted_message>

Example for log_entry_1:

Timestamp: 2023-10-27T16:05:30Z
Level: INFO
Message: User 'admin' logged in successfully.
"""

import os
import re

pattern = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)"  # Group 1: Time
    r"\s+"  # Separator
    r"\[(?P<severity>INFO|WARNING|ERROR|CRITICAL)\]"  # Group 2: Severity
    r"\s+"  # Separator
    r"(?P<message>.+)"  # Group 3: Message
)


def extract_data(filename):
    """
    extract logs data
    """
    content = _read_file(filename)
    if not content:  # Check if file reading failed
        return None

    data = []
    # Attempt to search and extract data for all patterns
    matches = pattern.finditer(content)
    for match in matches:
        for key, value in match.groupdict().items():
            data.append(f"{key.capitalize()}: {value}")
            # print(f"{key.capitalize()}: {value}")
        data.append("\n")
    return "\n".join(data)  # Return the formatted string


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
    Creates a file with predefined server logging data.
    Args:
        filename (str): The path where the input file will be created.
    """
    try:
        with open(filename, "w") as f:
            f.write(
                "2023-10-27T16:05:30Z [INFO] User 'admin' logged in successfully.\n"
            )
            f.write(
                "2023-10-27T16:06:15Z [ERROR] Failed to connect to service 'auth-api': Connection refused.\n"
            )
            f.write("2023-10-27T16:07:00Z [WARNING] Disk space low on /var/log.\n")
    except Exception as e:
        print(f"Error creating file '{filename}': {e}")


if __name__ == "__main__":
    logging_file = "log_entries.txt"
    _create_input_file(logging_file)
    extracted_info = extract_data(logging_file)
    if extracted_info:
        print(extracted_info)
    else:
        print("Failed to generate report.")

    # Clean up the created file (optional, but good for demos)
    if os.path.exists(logging_file):
        os.remove(logging_file)
