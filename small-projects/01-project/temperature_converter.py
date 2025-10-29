# temperature_converter.py
from typing import Union


def celsius_to_fahrenheit(celsius: Union[int, float]) -> float:
    """Converts Celsius to Fahrenheit."""
    # Implement this correctly after writing tests, or make it return 0 initially.
    if isinstance(celsius, str):
        raise TypeError("numeric value is needed")
    return celsius * 9 / 5 + 32
