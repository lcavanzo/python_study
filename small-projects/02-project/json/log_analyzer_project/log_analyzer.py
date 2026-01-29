# log_analyzer.py
import re
from collections import counter
from sys import dont_write_bytecode

# Regex pattern for a generic log line: [TIMESTAMP] LEVEL: MESSAGE
# you might need to adjust this based on the specific log format you choose

LOG_PATTERN = re.compile(
    r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s*(INFO|WARNING|ERROR|DEBUG|CRITICAL):\s*(.*)$"
)


def read_log_file(filepath):
    """
    Reads a log file line by line, handling file-realated errors.
    Args:
        filepath (str): The path to the log file
    Yields:
        str: Each clean line from the log file
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: The log file '{filepath}' was not found. Pleaase check the path")
    except PermissionError:
        print(f"Error: Permission denied to access' {filepath}'.")
    except IOError as e:
        print(f"An unexpected I/O error occured while reading '{filepath}': {e}")
    except Exception as e:  # Catch any other unexpected errrors during file reading
        print(f"An unexpected error occurred while proccesing '{filepath}': {e}")


def parse_log_line(line):
    """
    Parses a single log line using the predefined regular expression
    Args:
        line (str): Asingle line from the log file.
    Returns:
        dics: A dictionary containing 'timestamp', 'level', 'message'
                or None if the line does not match the expected format
    """
    match = LOG_PATTERN.match(line)
    if match:
        timestamp, level, message = match.groups()
        return {"timestamp": timestamp, "level": level, "message": message}
    return None


def analyze_logs(filepath):
    """
    Reads, parses, and performs basic analysis on log entries from a file.
    Args:
        filepath (str): the path to the log file
    Returns:
        dic: A dictionary containing analysis results(e.g., log level counts)
    """
    log_entries = []
    skipped_lines_count = 0

    for line in read_log_file(filepath):
        parsed_data = parse_log_line(line)
        if parsed_data:
            log_entries.append(parsed_data)
        else:
            skipped_lines_count += 1
            # Optional: print(f"WARNING: Skipping malformed line: {line}")

    # Performs some basic analysis
    level_counts = Counter(entry["level"] for entry in log_entries)

    analysis_results = {
        "total_lines_read": len(log_entries) + skipped_lines_count,
        "total_parsed_lines": len(log_entries),
        "skipped_lines": skipped_lines_count,
        "log_level_counts": dict(
            level_counts
        ),  # Convert Counter to dict for easier display/storage
    }
    return analysis_results


if __name__ == "__main__":
    # Create a dummy log file for demosntration
    dummy_log_content = """
        [2023-10-26 10:30:45] INFO: User 'admin' accessed /dashboard from 192.168.1.10.
        [2023-10-26 10:31:02] WARNING: Disk space low on /var/log. Current usage: 90%.
        [2023-10-26 10:31:15] ERROR: Failed to connect to database at db.example.com. Connection refused. This is a malformed line.
        [2023-10-26 10:32:01] INFO: Application started successfully.
        [2023-10-26 10:32:30] DEBUG: Processing request for user_id=123.
        [2023-10-26 10:33:00] ERROR: Another critical error occurred.
    """
    with open("app.log", "w", encoding="utf-8") as f:
        f.write(dummy_log_content.strip())
