from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    organizer = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    attendee = models.ManyToManyField("Player", related_name='attending', through='AttendingPlayer')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value