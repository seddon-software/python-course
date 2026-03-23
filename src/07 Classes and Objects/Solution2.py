'''
Add methods to the two classes below such that the remaining code executes successfully.
Note some of the methods should be static (class methods).

The expected output from your program is:
            John     has 33 points from 3 games
            Peter    has 19 points from 4 games
            Alfred   has 18 points from 2 games
            Alice    has 11 points from 1 games
'''

class Player:
    players = []
    def print():
        for player in Player.players:
            print(player)
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.games = 0
        Player.players.append(self)
    def score(self, points):
        self.points += int(points)
        self.games += 1
    def __str__(self):
        return f"{self.name:8s} has {self.points:2} points from {self.games} games"

class Match:
    def result(player1, player2, scores):
        score1, score2 = scores.split('-')
        player1.score(score1)
        player2.score(score2)
 
john = Player("John")
peter = Player("Peter")
alfred = Player("Alfred")
alice = Player("Alice")
Match.result(john, peter, "11-3")
Match.result(john, alfred, "11-7")
Match.result(alfred, peter, "11-9")
Match.result(john, peter, "11-5")
Match.result(alice, peter, "11-2")
Player.print()
