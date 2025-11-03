import pytest
from temperature_converter import celsius_to_fahrenheit


@pytest.mark.parametrize(
    "celsius, expected_fahrenheit",
    [
        (0, 32),
        (100, 212),
        (-10, 14),
    ],
)
def test_temperature_converter_fixed_values(celsius, expected_fahrenheit):
    assert celsius_to_fahrenheit(celsius) == expected_fahrenheit


def test_temperature_converter_approx():
    assert celsius_to_fahrenheit(25.5) == pytest.approx(77.9)


def test_temperature_converter_string():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("abc")
