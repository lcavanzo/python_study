# test_word_counter.py

import pytest
from word_counter import count_words


def test_count_words_empty():
    assert count_words("") == {}


def test_count_words_single_word():
    assert count_words("hello") == {"hello": 1}


def test_count_words_multiple_words():
    assert count_words("hello world hello") == {"hello": 2, "world": 1}


def test_count_words_multiple_words_insensitive():
    assert count_words("Hello world hello") == {"hello": 2, "world": 1}


def test_count_words_multiple_words_punctuaction():
    assert count_words("Hello, world! hello.") == {"hello": 2, "world": 1}
