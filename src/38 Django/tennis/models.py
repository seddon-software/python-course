from django.db import models

class Match(models.Model):
    homeTeam = models.CharField(max_length=20)
    homeScore = models.IntegerField(default=0)
    awayTeam = models.CharField(max_length=20)
    awayScore = models.IntegerField(default=0)

    def play(self, home, score1, away, score2):
        self.homeTeam = home
        self.homeScore = score1
        self.awayTeam = away
        self.awayScore = score2
