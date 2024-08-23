"""
Problem statement
The code below has:

A parent class named Animal.

Inside it, define:
name
sound
__init__()
Animal_details() function
It prints the name and sound of the Animal.
Then there are two derived classes*

Dog class
Has a property family
Has an initializer that calls the parent class initializer in it through super()
Has an overridden method named Animal_details() which prints detail of the dog.
Sheep class
Has a property color
Has an initializer that calls the parent class initializer in it through super()
Has an overridden method named Animal_details(), which prints detail of the sheep
The derived classes should override the Animal_details() method defined in the Animal class.

The overridden method in Dog class should print the value of family as well as the name and sound.
The overridden method in Sheep class should print the value of color as well as the name and sound
Input
name of Dog is set to Pongo, sound is set to Woof Woof, and family is set to Carnivore in the initializer of Dog object.

name of Sheep is set to Billy, sound is set to Baaa Baaa, and color is set to White in the initializer of Sheep object.

Now, call Animal_details() from their respective objects.

Sample input
d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print(" ")
s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()

Sample output
Name: Pongo
Sound: Woof Woof
Family: Husky

Name: Billy
Sound: Baa Baa
Color: White

"""


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print("Name:", self.name)
        print("Sound:", self.sound)


class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def Animal_details(self):
        super().Animal_details()
        print("Family:", self.family)


class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        print("Color:", self.color)


d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print("")
s = Sheep("Billy", "Baa Baa", "White")
s.Animal_details()

print()

demo2 = Animal("Cat", "mia")
demo2.Animal_details()
