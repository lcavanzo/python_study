import unittest
from unittest.mock import patch, Mock


# Assume this is the module containing the Sensor class and the function
# we want to test. In a real project, this would be in a separate file
# For demonstration, we'll define it here
class Sensor:
    def __init__(self, sensor_id, min_value, max_value):
        self.sensor_id = sensor_id
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = 0

    def read_value(self):
        """
        This would normally interact with external systems
        """
        print(f"Reading actual sensor {self.sensor_id}...")
        self.current_value = 10
        return self.current_value

    def update_value(self, new_value):
        """
        Verify new value is within the sensor range
        """
        if new_value > self.max_value or new_value < self.min_value:
            print(f"Error: Sensor Value {new_value} is out of range")
        else:
            self.current_value = new_value
            return f"Sensor: {self.sensor_id} - {self.current_value}"


def set_sensor_value(sensor):
    """
    Validates new sensor value is within the range
    """
    sensor.update_value()


def get_alert_status(sensor_id):
    """
    creates a Sensor object and gets its reading to determine alert status
    """
    sensor = Sensor(sensor_id, -20, 100)
    value = sensor.read_value()
    if value > 20.0:
        return "CRITICAL"
    return "OK"


sensor1 = Sensor("bd01", -20, 100)
print(f"Sensor: {sensor1.sensor_id} - tmp:{sensor1.read_value()}")
sensor1.update_value(-30)
sensor1.update_value(110)


# Unit test class
class TestSensorAlerts(unittest.TestCase):
    # Use @patch as a decorator to mock the Sensor class
    # The string 'Sensor' refers to the class defined in the current module.
    # If Sensor was in a module like 'my_module.sensors', the path would be 'my_module.sensors.Sensor'.
    @patch("__main__.Sensor")  # Mocking the Sensor class in the current scope
    def test_alert_status_critical(self, MockSensor):
        # Configure the mock Sensor Class
        # When Sensor() is called in get_alert_status, MockSensor will be returned
        # we then configurethe instance of the mock Sensor
        mock_instance = MockSensor.return_value
        mock_instance.read_value.return_value = (
            25  # Set the return value for read_value()
        )

        # Call the function under test
        status = get_alert_status("SERVER-TEMP-01")

        # Assertions
        self.assertEqual(status, "CRITICAL")
        MockSensor.assert_called_once_with(
            "SERVER-TEMP-01", -20, 100
        )  # Check the sensor was instantiated
        mock_instance.read_value.assert_called_once()  # check read_value was called

    @patch("__main__.Sensor")
    def test_alert_status_ok(self, MockSensor):
        mock_instance = MockSensor.return_value
        mock_instance.read_value.return_value = (
            15  # Set the return value for read_value()
        )

        status = get_alert_status("DB-CPU-01")

        self.assertEqual(status, "OK")
        MockSensor.assert_called_once_with("DB-CPU-01", -20, 100)
        mock_instance.read_value.assert_called_once()

    def test_sensor_update_value_ok_real_object(self):
        sensor = Sensor("SRV-01", -20, 100)
        result = sensor.update_value(24)
        self.assertEqual(sensor.current_value, 24)
        self.assertEqual(result, "Sensor: SRV-01 - 24")

    def test_sensor_update_value_failed_real_object(self):
        sensor = Sensor("SRV-01", -20, 100)
        result_low = sensor.update_value(-30)
        self.assertIsNone(result_low)  # update_value returns None on error
        self.assertEqual(sensor.current_value, 0)  # Value should not change

        result_high = sensor.update_value(110)
        self.assertIsNone(result_high)  # update_value returns None on error
        self.assertEqual(sensor.current_value, 0)  # Value should not change


# To run the test if this script is executed directly
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
