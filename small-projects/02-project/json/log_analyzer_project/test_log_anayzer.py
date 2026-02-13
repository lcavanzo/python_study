# test_log_analyzer.py

import pytest
from unittest.mock import mock_open, patch
from log_analyzer import read_log_file, parse_log_line, analyze_logs


# --- Test for read_log_file ---
def test_read_log_file_success():
    """
    Verifies that read_log_file correctly reaads all lines and strips whitespaces
    """
    mock_file_content = "line 1\nline 2\n line 3"
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        lines = list(read_log_file("dummy.log"))
        assert lines == ["line 1", "line 2", "line 3"]
        mock_file.assert_called_once_with("dummy.log", "r", encoding="utf-8")


def test_read_log_file_not_found_returns_empty():
    """
    Ensuress read_log_file handles FilesNotFoundErrors gracefully
    """
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        lines = list(read_log_file("non_existent.log"))
        assert lines == []  # Should yield no lines


def test_read_log_file_permissions_denied_returns_empty():
    """
    Entures read_log_file handles PermissionError gracefully
    """
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = PermissionError
        lines = list(read_log_file("protected.log"))
        assert lines == []


# --- Test for parse_log_line ---
def test_parse_log_line_valid_info():
    """
    Tests parsing a standard INFO log line
    """
    line = (
        "[2023-10-26 10:30:45] INFO: User 'admin' accessed /dashboard from 192.168.1.10"
    )
    expected = {
        "timestamp": "2023-10-26 10:30:45",
        "level": "INFO",
        "message": "User 'admin' accessed /dashboard from",
        "ip": "192.168.1.10",
    }
    assert parse_log_line(line) == expected


def test_parse_log_line_valid_warning_with_spaces():
    """
    Tests parsing a WARNING log line with extra spaces
    """
    line = "[2023-10-26 10:31:02]  WARNING:   Disk space low"
    expected = {
        "timestamp": "2023-10-26 10:31:02",
        "level": "WARNING",
        "message": "Disk space low",
        "ip": None,
    }
    assert parse_log_line(line) == expected


def test_parse_log_line_malformed_returns_none():
    """
    Test that malformed lines return None
    """
    assert parse_log_line("This is not a log line.") is None
    assert parse_log_line("[2023-10-26] INFO: incomplete.") is None  # Missing time
    assert parse_log_line("INFO: No timestamp.") is None


def test_parse_log_line_empty_returns_none():
    """
    Tests handling of emtpy string
    """
    assert parse_log_line("") is None


# --- Test for analyze_logs ---
def test_analyze_logs_basic_funcionality():
    """
    Test basic log analysis results
    """
    mock_log_content = """ [2023-10-26 10:30:45] INFO: Log entry 1\n[2023-10-26 10:31:00] ERROR: Log entry 2\n[2023-10-26 10:31:15] INFO: Log entry 3\nMalformed line here.\n[2023-10-26 10:32:00] WARNING: Log entry 4"""
    with patch("builtins.open", mock_open(read_data=mock_log_content)) as mock_file:
        results = analyze_logs("test.logs")
        # 4 valid + 1 malformed 'total_parsed_lines': 4,
        expected_results = {
            "total_lines_read": 5,
            "total_parsed_lines": 4,
            "skipped_lines": 1,
            "log_level_counts": {"INFO": 2, "ERROR": 1, "WARNING": 1},
            "message_level_counts": {
                "Log entry 1": 1,
                "Log entry 2": 1,
                "Log entry 3": 1,
                "Log entry 4": 1,
            },
            "ip_addresses": {},
        }
        assert results == expected_results


def test_analyze_logs_empty_file():
    """Tests analysis of an empty log file."""
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        results = analyze_logs("empty.log")
        expected_results = {
            "total_lines_read": 0,
            "total_parsed_lines": 0,
            "skipped_lines": 0,
            "log_level_counts": {},
            "message_level_counts": {},
            "ip_addresses": {},
        }
        assert results == expected_results


def test_analyze_logs_file_not_found():
    """Tests analyze_logs when the file does not exist."""
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        results = analyze_logs("non_existent.log")
        assert (
            results
            == {  # Expect default/empty results or none, depending on how `analyze_logs` handles it
                "total_lines_read": 0,
                "total_parsed_lines": 0,
                "skipped_lines": 0,
                "log_level_counts": {},
                "message_level_counts": {},
                "ip_addresses": {},
            }
        )
