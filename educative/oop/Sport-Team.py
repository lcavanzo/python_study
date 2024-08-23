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

    def __init__(self, name, players):
        self.name = name
        self.players = players

    def addPlayers(self, player):
        self.players.append(player)

    def getPlayers(self):
        return len(self.players)


class School:
    """docstring for School."""

    def __init__(self, name, teams):
        self.teams = teams
        self.name = name

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        print("Player ID's\tPlayer Names\tTeams")
        for team in self.teams:
            for player in team.players:
                print(f"{player.ID}\t\t{player.name}\t\t{player.teamName}")


# Players
p1 = Player("1", "Red", "Harris")
p2 = Player("2", "Red", "Carol")
p3 = Player("1", "Blue", "Johny")
p4 = Player("2", "Blue", "Sarah")

# Teams
rteam = []
bteam = []
red = Team("red", rteam)
print(f"Red team: {red.getPlayers()}")
print("Adding players to red team")
red.addPlayers(p1)
red.addPlayers(p2)
red.getPlayers()
print(f"Red team: {red.getPlayers()}")
print()
blue = Team("blue", bteam)
print(f"Blue team: {blue.getPlayers()}")
print("Adding players to blue team")
blue.addPlayers(p3)
blue.addPlayers(p4)
blue.getPlayers()
print(f"Blue team: {blue.getPlayers()}")

# Schools
print()
s1teams = []
s1 = School("FF", s1teams)
print(f"School: {s1.name}, school's teams: {len(s1.teams)}")
s1.addTeam(red)
s1.addTeam(blue)
print(f"School: {s1.name}, school's teams: {len(s1.teams)}")
s1.getTotalPlayersInSchool()
