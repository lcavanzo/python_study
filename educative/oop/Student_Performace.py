class Student:
    """docstring for student"""

    def __init__(self, name, phy, chem, bio) -> None:
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        total = self.phy + self.chem + self.bio
        return total

    def percentage(self):
        obtained = self.totalObtained()
        return (obtained / 300) * 100


Mark = Student("Mark", 80, 90, 40)
print(Mark.totalObtained())
print(Mark.percentage())
