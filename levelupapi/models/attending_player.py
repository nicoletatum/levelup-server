from django.db import models

class AttendingPlayer(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)