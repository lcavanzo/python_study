"""
Temperature Conversion: Write a function that converts Celsius to Fahrenheit.
Test it with the freezing point (0°C) and boiling point (100°C) of water.
Also, consider absolute zero (-273.15°C).
"""


def cel2fah(temp: float) -> float:
    if temp >= -273.15:
        fahrenheit = temp * (9 / 5) + 32
        return round(fahrenheit, 2)
    else:
        raise ValueError("Invalid temperature")


# print(cel2fah(0)
# print(cel2fah(100))
# print(cel2fah(-273.15))
# print(cel2fah(-273.15))

assert cel2fah(0) == 32.0
assert cel2fah(100) == 212.0
assert cel2fah(-273.15) == -459.67
