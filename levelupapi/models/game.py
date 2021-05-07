from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()