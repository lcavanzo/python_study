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
