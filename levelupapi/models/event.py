from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    address = models.CharField(max_length=100)
    organizer = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    attendee = models.ManyToManyField("Player", related_name='attending', through='AttendingPlayer')