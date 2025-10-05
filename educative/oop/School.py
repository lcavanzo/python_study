class Player:
    def __init__(self, ID, teamName, name):
        self.ID = ID
        self.teamName = teamName
        self.name = name


class Team:
    def __init__(self, players, name) -> None:
        self.players = players
        self.name = name

    def addPlayers(self, player):
        self.players.append(player)

    def getPlayers(self):
        return len(self.players)


class School:
    def __init__(self, teams, schoolName) -> None:
        self.teams = teams
        self.schoolName = schoolName

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersIn(self):
        print(f"PlayerID - Player Name - Teams")
        for t in teams:
            for p in t.players:
                print(p.ID, p.name, p.teamName)


p1 = Player(1, "Red", "harris")
p2 = Player(2, "Red", "Carol")
p3 = Player(1, "Blue", "Johnny")
p4 = Player(2, "Blue", "Sarah")
p5 = Player(5, "Blue", "Luis")
p6 = Player(6, "Blue", "Diana")
p7 = Player(7, "Red", "Mariana")
playersRed = [p1, p2]
playersBlue = [p3, p4]

red = Team(playersRed, "Red")
blue = Team(playersBlue, "Blue")

print("Red Team")
print(red.getPlayers())
print("Adding a new member to red team")
red.addPlayers(p7)
print(red.getPlayers())
print("Blue Team")
print(blue.getPlayers())
print("Adding a new member to blue team")
blue.addPlayers(p5)
blue.addPlayers(p6)
print(blue.getPlayers())

teams = [red, blue]
itver = School(teams, "ITVER")
print("School")
itver.getTotalPlayersIn()
