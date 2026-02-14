from unittest.mock import Mock


# Scenario: we have a function that processes sensor data
# This function depends on a Sensor object
def process_sensor_reading(sensor_object):
    """
    Processes a sensor reading, classifying it as 'normal' or 'high'
    """
    reading = sensor_object.read_value()
    if reading > 30.0:
        return "HIGH_ALERT"
    return "NORMAL"


# Create a mock sensor object
mock_sensor = Mock()

# Configure the mock sensor's read_value method to return a specific value
mock_sensor.read_value.return_value = 28.5

# Now, when process_sensor_reading calls read_value on the mock_sensor,
# it will receive 28.5, not intereact with any real hardware
result_normal = process_sensor_reading(mock_sensor)
print(f"Result for normal reading: {result_normal}")

# Configre for a high value
mock_sensor.read_value.return_value = 35.0
result_high = process_sensor_reading(mock_sensor)
print(f"Result for high reading: {result_high}")

# we can also assert that methods were called
# mock_sensor.read_value.assert_called_once()  # This will fail if called multiple times or not at all in the test scope
# To reset call count for next test scenario:
mock_sensor.read_value.reset_mock()
mock_sensor.read_value.assert_not_called()
