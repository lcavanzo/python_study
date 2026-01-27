import re
from log_analyzer import read_log_file


def parse_log_line(line):
    """
    Parses a single log line using regular expressions.
    Expected format: [YYYY-MM-DD HH:MM:SS] LEVEL: MESSAGE
    Args:
        line (str): A single line from the log file.
    Returns:
        dict: A dictionary containing 'timestamp', 'level', 'message',
              or None if the line does not match the expected format.
    """
    # Regex breakdown:
    # ^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]   -> Captures timestamp (YYYY-MM-DD HH:MM:SS)
    # \s*                                          -> Matches zero or more whitespace characters
    # (INFO|WARNING|ERROR|DEBUG|CRITICAL)          -> Captures log level
    # :                                            -> Matches the colon separator
    # \s*                                          -> Matches zero or more whitespace characters
    # (.*)                                         -> Captures the rest of the line as the message
    # $                                            -> Matches the end of the line
    log_pattern = re.compile(
        r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s*(INFO|WARNING|ERROR|DEBUG|CRITICAL):\s*(.*)$"
    )
    match = log_pattern.match(line)
    if match:
        timestamp, level, message = match.groups()
        return {"timestamp": timestamp, "level": level, "message": message}
    return None


# Example of usage with sample.log file
if __name__ == "__main__":
    # Assuming the sample.log exists
    print("\nParsing log Entries:")
    parsed_logs = []
    for log_entry in read_log_file("sample.log"):
        parsed_data = parse_log_line(log_entry)
        if parsed_data:
            parsed_logs.append(parsed_data)
            print(f"Parsed: {parsed_data}")
        else:
            print(f"Skipped malformed line: {log_entry}")

    # we have structured data in parsed_logs
    print("\nCollected parsed logs:")
    for log in parsed_logs:
        print(log)
