"""
Problem statement
You have to implement 3 classes, School, Team, and Player, such that an instance of a School should contain instances of Team objects. Similarly, a Team object can contain instances of Player class.

Consider this diagram for clarification:



School, Team, Player: Class Representation
You have to implement a School class containing a list of Team objects and a Team class comprising a list of Player objects.

Task 1
The Player class should have three properties that will be set using an initializer:

ID
name
teamName
Task 2
The Team class will have two properties that will be set using an initializer:

name
players: a list with player class objects in it
It will have two methods:

addPlayer(), which will add new player objects in the players list

getNumberOfPlayers(), which will return the total number of players in the players list

Task 3
The School class will contain two properties that will be set using an initializer:

teams, a list of team class objects
name
It will have two methods:

addTeam, which will add new team objects in the teams list
getTotalPlayersInSchool(), which will count the total players in all of the teams in the School and return the count
So, your school should have these players in their respective teams:

Player ID’s	Player Names	Teams
1	            Harris  	Red
2	            Carol   	Red
1	            Johnny	    Blue
2	            Sarah   	Blue
"""


class Player:
    """docstring for Player."""

    def __init__(self, ID="", teamName="", name=""):
        self.ID = ID
        self.teamName = teamName
        self.name = name


class Team:
    """docstring for ClassName."""

    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayers(self, player):
        self.players.append(player)

    def getPlayers(self):
        print(len(self.players))


class School:
    """docstring for School."""

    def __init__(self, name):
        self.teams = []
        self.name = name

    def getTotalPlayersInSchool(self):
        print(len(name))

    def addTeam(self, team):
        print(self.teams.append(team))


p1 = Player("1", "Red", "Harris")
p2 = Player("2", "Red", "Carol")
p3 = Player("3", "Blue", "Johny")
p4 = Player("4", "Blue", "Sarah")

red = Team("red")
red.getPlayers()
red.addPlayers(p1)
red.addPlayers(p2)
red.getPlayers()
blue = Team("blue")
blue.getPlayers()
blue.addPlayers(p3)
blue.addPlayers(p4)
blue.getPlayers()
