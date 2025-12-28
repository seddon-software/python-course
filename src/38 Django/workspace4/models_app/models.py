from django.db import models

class Match(models.Model):
    homeTeam = models.CharField(max_length=20)
    homeScore = models.IntegerField(default=0)
    awayTeam = models.CharField(max_length=20)
    awayScore = models.IntegerField(default=0)

    def create(self, home, score1, away, score2):
        self.homeTeam = home
        self.homeScore = score1
        self.awayTeam = away
        self.awayScore = score2
        
    def __str__(self):
        return f"{self.homeTeam} {self.homeScore}-{self.awayScore} {self.awayTeam}"
