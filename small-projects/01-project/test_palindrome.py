"""
Testing: Create a test file (test_string_utils.py) and write comprehensive unit tests for this function. Include tests for:

    Actual palindromes (e.g., "madam", "racecar").
    Non-palindromes (e.g., "hello", "python").
    Palindromes with mixed casing (e.g., "Madam").
    Palindromes with spaces and punctuation (e.g., "A man, a plan, a canal: Panama").
    Empty strings.
    Single-character strings.
    Strings with only non-alphanumeric characters.
    Non-string inputs (should raise a TypeError).
"""

import pytest
from palindrome import is_palindrome


def test_is_palindrome_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True


def test_is_palindrome_non_palindrome():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False


def test_is_palindrome_insensitive_palindrome():
    assert is_palindrome("Madam") == True


def test_is_palindrome_symbols_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True


def test_is_palindrome_empty():
    assert is_palindrome("") == True


def test_is_palindrome_single_char():
    assert is_palindrome("a") == True


def test_is_palindrome_non_alphanumerics_characters():
    # all the chars are removed, so the string is empty
    assert is_palindrome("!@#$") == True


def test_is_palindrome_numbers():
    with pytest.raises(TypeError):
        is_palindrome(12345)
