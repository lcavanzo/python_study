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


def mname(self):
    pass
