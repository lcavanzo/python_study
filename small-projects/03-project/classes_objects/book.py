class Book:
    """
    A class to represent a book
    """

    def __init__(self, title, author, publication_year):
        """
        The constructor method for the Book class.
        It initializes the title, author and publication_year
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        """
        Displays the details of the book
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.publication_year}")


# another example: A sensor class for SRE context
class Sensor:
    """
    A class to represent a basic sensor, e.g., for monitoring temperature
    """

    def __init__(self, sensor_id, sensor_type, location, current_value=0.0):
        """
        initializes a sensor with an ID, type, locaiton and an optional initial value
        """
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.location = location
        self.current_value = current_value

    def read_values(self):
        """
        Simulates reading a value from the sensor. In a real scenario, this
        would interact with hardware or an API
        """
        # For simplicity, we'll just return the current value
        # In a real SRE context, this might query a monitoring system
        return self.current_value

    def update_value(self, new_value):
        """
        Updates the sensor's current value
        """
        if isinstance(new_value, (int, float)):
            self.current_value = new_value
        else:
            print("Error: New value must be a number")

    def get_status(self):
        """
        Returns a string indicating the sensor's current status
        """
        return f"Sensor ID:{self.sensor_id}, Type:{self.sensor_type}, Location:{self.location}, Value: {self.current_value}"


# Instantiating objects from the Book class
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
book2 = Book("Python Crash Course", "Eric Matthes", 2015)

# Instantiating objects from the Sensor class
temperature_sensor = Sensor("TEMP-001", "Temperature", "Server Rack A", 25.5)
humidity_sensor = Sensor("HUM-002", "Humidity", "Data Center Floor")

# Accessing attributes and calling methods for Book objects
print(book1.title)
book2.display_details()

print()
# Accessing attributes and calling methods for Sensor objects
print(f"Initial Temperature: {temperature_sensor.read_values()}C")
temperature_sensor.update_value(26.1)
print(f"Updated Temperature: {temperature_sensor.read_values()}C")
print(humidity_sensor.get_status())
