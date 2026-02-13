import pytest
from log_line_parser import parse_log_entry


def test_parse_log_entry():
    # positive test cases
    valid_log_1 = "[2023-10-27T12:00:00] [ERROR] <ABC-123> Failed to process request."
    expected_1 = {
        "timestamp": "2023-10-27T12:00:00",
        "severity": "ERROR",
        "id": "ABC-123",
        "message": "Failed to process request.",
    }
    assert parse_log_entry(valid_log_1) == expected_1

    valid_log_2 = (
        "[2023-10-27T12:01:05] [INFO] <XYZ-987> User logged in from 192.168.1.1."
    )
    expected_2 = {
        "timestamp": "2023-10-27T12:01:05",
        "severity": "INFO",
        "id": "XYZ-987",
        "message": "User logged in from 192.168.1.1.",
    }
    assert parse_log_entry(valid_log_2) == expected_2

    # Edge case: minimal message
    valid_log_3 = "[2023-10-27T12:02:10] [WARNING] <DEF-456> OK."
    expected_3 = {
        "timestamp": "2023-10-27T12:02:10",
        "severity": "WARNING",
        "id": "DEF-456",
        "message": "OK.",
    }
    assert parse_log_entry(valid_log_3) == expected_3

    # Negative test cases (should not match, or return None)
    invalid_log_1 = "Malformed log entry."  # Missing all parts
    assert parse_log_entry(invalid_log_1) is None

    invalid_log_2 = "[2023-10-27T12:00:00] [DEBUG] <ABC-123> Unknown severity level."  # Invalid severity
    assert parse_log_entry(invalid_log_2) is None

    invalid_log_3 = "[2023-10-27T12:00:00] [ERROR] <123-ABC> Invalid ID format."  # ID format incorrect
    assert parse_log_entry(invalid_log_3) is None

    invalid_log_4 = (
        " [2023-10-27T12:00:00] [ERROR] <ABC-123> Leading space."  # Leading space
    )
    assert parse_log_entry(invalid_log_4) is None

    print("\nAll log parsing tests passed!")
