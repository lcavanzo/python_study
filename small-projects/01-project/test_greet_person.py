# test greet_person.py

import pytest
from greet_person import greet_person


def test_greet_person_default():
    assert greet_person("Luis") == "Hello, Luis"


def test_greet_person_custom():
    assert greet_person("Cavanzo", "Sir") == "Sir, Cavanzo"
