# test_temperature_converter.py

import pytest
from temperature_converter import celsius_to_fahrenheit


def test_temperature_converter_0():
    assert celsius_to_fahrenheit(0) == 32


def test_temperature_converter_100():
    assert celsius_to_fahrenheit(100) == 212


def test_temperature_converter_minus10():
    assert celsius_to_fahrenheit(-10) == 14


def test_temperature_converter_approx():
    assert celsius_to_fahrenheit(25.5) == pytest.approx(77.9)


def test_temperature_converter_string():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("abc")
