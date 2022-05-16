class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Describe restaurant information"""
        print(f"{self.restaurant_name} offers {self.cuisine_type}")


    def open_restaurant(self):
        """prints restaurant opening"""
        print(f"The restaurant {self.restaurant_name} is now open")


restaurant = Restaurant("moe's bar", "fast food")
print(f"{restaurant.restaurant_name} offers {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

