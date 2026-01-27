# test_log_anayzer.py
import pytest
from unittest.mock import mock_open, patch
from log_analyzer import read_log_file
from parse_log_line import parse_log_line


def test_read_log_file_success():
    """
    Test that read_log_file correctly reads all lines from a valid file.
    """
    mock_file_content = "line 1\nline 2\nline 3"
    # patch 'builtins.open' replaces the global open() function during the test
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        lines = list(read_log_file("dummy.log"))
        assert lines == ["line 1", "line 2", "line 3"]
        # Ensure open was called correct arguments
        mock_file.assert_called_once_with("dummy.log", "r")


def test_read_log_file_not_found():
    """
    Test that read_log_file handles FileNotFoundError
    """
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        # We expect it to print an error and return an emptry generator
        # Capturing stdout is one way to test print statements, or check specific return values
        # For no, we'll assert taht no lines are yielded
        lines = list(read_log_file("non_existent.log"))
        assert lines == []  # should yield no lines


def test_read_log_file_permissions_denied():
    """
    Test that read_log_file handles PermissionError
    """
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = PermissionError
        lines = list(read_log_file("protected.log"))
        assert lines == []


def test_parse_log_line_valid_info():
    """
    Test parsing a valid INFO log line
    """
    line = "[2023-10-26 10:30:45] INFO: User 'admin' accessed /dashboard from 192.168.1.10."
    expected = {
        "timestamp": "2023-10-26 10:30:45",
        "level": "INFO",
        "message": "User 'admin' accessed /dashboard from 192.168.1.10.",
    }
    assert parse_log_line(line) == expected


def test_parse_log_line_valid_error():
    """
    Test parsing a valid Error log line
    """
    line = "[2023-10-26 10:31:15] ERROR: Failed to connect to database."
    expected = {
        "timestamp": "2023-10-26 10:31:15",
        "level": "ERROR",
        "message": "Failed to connect to database.",
    }
    assert parse_log_line(line) == expected


def test_parse_log_line_malformed():
    """
    Test parsing a malformed log line
    """
    line = "This is a completely malformed line without a proper log format."
    assert parse_log_line(line) is None


def test_parse_log_line_empty():
    """
    Test parsing an empty line
    """
    line = ""
    assert parse_log_line(line) is None


def test_parse_log_line_different_level():
    """
    Test parsing a log line with a different log leve
    """
    line = "[2023-10-27 11:00:00] DEBUG: Debug message here."
    expected = {
        "timestamp": "2023-10-27 11:00:00",
        "level": "DEBUG",
        "message": "Debug message here.",
    }
    assert parse_log_line(line) == expected
