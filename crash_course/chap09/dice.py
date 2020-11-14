"""A class that represent a dice"""
from random import randint

class Dice:
    """A simple attempt to represent a dice"""
    def __init__(self, sides=6):
        """Initialize the dice's attributes"""
        self.sides = sides

    def roll_dice(self):
        """Roll the dice"""
        result = randint(1, self.sides)
        print(f"\t{result} ")


my_dice = Dice(20)

for attempt in range(10):
    print(f"Rolling the dice, attempt #{attempt + 1}: ")
    my_dice.roll_dice()

