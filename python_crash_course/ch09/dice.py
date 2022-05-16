from random import randint

class Dice:
    """ Attempt to model a Dice"""

    def __init__(self):
        """Initialize attributes to describe a dice"""
        self.sides = 6


    def roll_die(self):
        """Return the dice result"""
        result = randint(1,self.sides)
        print(f"Dice result: {result}")


my_dice = Dice()
for time in range(1,10):
    my_dice.roll_die()
