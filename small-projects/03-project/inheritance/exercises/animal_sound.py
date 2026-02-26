"""
Practice from Scratch 1: Animal Sound System

Objective: Design a system where different animals make their unique sounds using polymorphism.

    Design a base class Animal with a make_sound() method.

    Create at least three subclasses of Animal (e.g., Dog, Cat, Cow).

    Each subclass should override the make_sound() method to return its specific sound.

    Implement a function that takes a list of Animal objects and calls make_sound() on each, then prints the result.

    Write pytest tests to ensure each animal's make_sound() method returns the correct string and that the function handling the list of animals correctly invokes the polymorphic behavior.

"""


class Animal:
    """
    Base Class that models an animal
    """

    def make_sound(self):
        raise NotImplementedError


class Dog(Animal):
    """
    Child class that represents a dog
    """

    def make_sound(self):
        return "Wof"


class Cat(Animal):
    """
    Child class that represents a cat
    """

    def make_sound(self):
        return "Miau"


class Cow(Animal):
    """
    Child class that represents a cow
    """

    def make_sound(self):
        return "Muu"


def animals_sounds(animal_list):
    return [animal.make_sound() for animal in animal_list]


animals = [Dog(), Cat(), Cow()]
print(animals_sounds(animals))
