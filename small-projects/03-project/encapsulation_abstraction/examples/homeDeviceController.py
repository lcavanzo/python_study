from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, device_id, name):
        self._device_id = device_id
        self.name = name
        self._is_on = False

    @abstractmethod
    def turn_on(self):
        """
        Turns the device on
        """
        pass

    @abstractmethod
    def turn_off(self):
        """
        Turns the device off.
        """
        pass

    @abstractmethod
    def get_status(self) -> str:
        """
        Returns the current status of the device
        """
        pass

    def is_powered_on(self):
        return self._is_on


class SmartLight(SmartDevice):
    def __init__(self, device_id, name, brightness=0):
        super().__init__(device_id, name)
        self._brightness = brightness  # Protected internal state for light

    def turn_on(self):
        self._is_on = True
        self._brightness = 50  # Default brightness on turn on
        print(f"{self.name} (Light) turned ON with brightness {self._brightness}%")

    def turn_off(self):
        self._is_on = False
        self._brightness = 0
        print(f"{self.name} (light) turned OFF.")

    def set_brightness(self, level):
        if self._is_on and 0 <= level <= 100:
            self._brightness = level
            print(f"{self.name} brightness set to {self._brightness}%.")
        elif not self._is_on:
            print(f"{self.name} is off, cannot set brightness")
        else:
            print("Brightness level must be between 0 and 100.")

    def get_status(self):
        return f"{self.name} (Light) - ID: {self._device_id}, Power: {'On' if self._is_on else 'Off'}, Brightness: {self._brightness}%"


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, name, target_temp=20):
        super().__init__(device_id, name)
        self._target_temp = target_temp  # Protected internal state for thermostat

    def turn_on(self):
        self._is_on = True
        print(
            f"{self.name} (Thermostat) turned ON. Current target: {self._target_temp}C"
        )

    def turn_off(self):
        self._is_on = False
        print(f"{self.name} (Thermostat) turned OFF")

    def set_temperature(self, temp):
        if self._is_on and 15 <= temp <= 30:  # example of valid range
            self._target_temp = temp
            print(f"{self.name} target temperature to {self._target_temp}C")
        elif not self._is_on:
            print(f"{self.name} is off, cannot set temperature")
        else:
            print("Temperature must get between 15 and 30 C.")

    def get_status(self):
        return f"{self.name} (Thermostat) - ID: {self._device_id}, Power: {'On' if self._is_on else 'Off'}, Target Temp: {self._target_temp}°C"


# Using the abstract interface
devices = [
    SmartLight("L001", "Living Room Light"),
    SmartThermostat("T001", "Main Thermostat"),
]

for device in devices:
    device.turn_on()
    print(device.get_status())

    if isinstance(device, SmartLight):
        device.set_brightness(75)
    elif isinstance(device, SmartThermostat):
        device.set_temperature(22)
    print(device.get_status())
    device.turn_off()
    print("-" * 30)

# Attempt to set brightness on a thermostat (will fail gracefully due to abstraction)
if isinstance(
    devices[1], SmartLight
):  # This check prevents calling set_brightness on a thermostat
    devices[1].set_brightness(90)
else:
    print(
        f"Cannot set brightness on a {type(devices[1]).__name__} as it's not a SmartLight."
    )
