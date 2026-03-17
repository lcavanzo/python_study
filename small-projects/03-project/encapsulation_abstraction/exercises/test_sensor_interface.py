"""
Scenario: You are building a system for environmental monitoring. Different types of sensors (Temperature, Humidity, Pressure) will provide data. You need a common interface for them.

Task:

    Define an abstract base class Sensor with the following abstract methods:
        get_value(): Returns the current reading from the sensor.
        get_unit(): Returns the unit of measurement (e.g., "°C", "%", "hPa").
        calibrate(): Performs a calibration process for the sensor.

    Implement two concrete sensor classes: TemperatureSensor and HumiditySensor.
        TemperatureSensor should take an initial temperature value and a unit (e.g., "Celsius" or "Fahrenheit"). Its get_value should return the current temperature. calibrate could simulate a recalibration.
        HumiditySensor should take an initial humidity percentage. Its get_value should return the current humidity. calibrate could simulate a recalibration.

    Write pytest tests to:
        Verify that Sensor cannot be instantiated directly.
        Verify that TemperatureSensor and HumiditySensor can be instantiated and correctly implement all abstract methods.
        Test that calling get_value, get_unit, and calibrate on instances of TemperatureSensor and HumiditySensor behave as expected.
        Demonstrate how a class failing to implement an abstract method from Sensor would raise a TypeError upon instantiation.

"""

import pytest

from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, device_id):
        self._device_id = device_id

    @abstractmethod
    def get_device_id(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_unit(self) -> str:
        pass

    @abstractmethod
    def calibrate(self) -> str:
        pass


class TemperatureSensor(Sensor):
    def __init__(self, device_id, temp_value, unit):
        super().__init__(device_id)
        self._temp_value = temp_value
        self._unit = unit

    def get_device_id(self):
        return self._device_id

    def get_value(self):
        return self._temp_value

    def get_unit(self):
        return self._unit

    def calibrate(self):
        return "Calibrating Sensor ..."


class HumiditySensor(Sensor):
    def __init__(self, device_id, hum_percentage):
        super().__init__(device_id)
        self._hum_percentage = hum_percentage

    def get_device_id(self):
        return self._device_id

    def get_unit(self):
        return "%"

    def get_value(self):
        return self._hum_percentage

    def calibrate(self):
        return "Calibrating Sensor ..."


# testing
sensors = [
    TemperatureSensor("Temp-01", 20, "Celsius"),
    HumiditySensor("Humi-01", 50),
]
for sensor in sensors:
    print(f"{sensor.get_device_id()}: {sensor.get_value()} {sensor.get_unit()}")
    print(sensor.calibrate())
    print()


if __name__ == "__main__":
    pytest.main()
