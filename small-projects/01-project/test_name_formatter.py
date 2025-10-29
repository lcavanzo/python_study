# test_name_formatter.py

import pytest
from name_formatter import format_name


def test_name_formatter():
    assert format_name("John", "Doe") == "John Doe"


def test_name_formatter_last_name_empty():
    assert format_name("Jane", "") == "Jane"


def test_name_formatter_first_name_empty():
    assert format_name("", "Smith") == "Smith"


def test_name_formatter_spaces():
    assert format_name("Alice ", " Wonderland") == "Alice Wonderland"


def test_name_formatter_symbols():
    assert format_name("Alice!", " Wonderland-") == "Alice Wonderland"


def test_name_formatter_invalid_first_name():
    with pytest.raises(ValueError):
        format_name(None, "Doe")


def test_name_formatter_invalid_last_name():
    with pytest.raises(ValueError):
        format_name("Doe", None)
