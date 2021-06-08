from django.db import models
from django.db.models import CASCADE
from datetime import datetime


# get today's date as string
def getTodaysDate():
    return datetime.today().strftime('%Y-%m-%d')

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(default=getTodaysDate(), max_length=10)
    is_finished = models.BooleanField(default=False)
    winner = models.CharField(max_length=250, default='will not be concluded until midnight')

    def checkStatus(self):
        event_details = 'Lottery Event on ' + str(self.date) + ' ' + self.winner
        if self.is_finished is True:
            event_details = 'Lottery Event on ' + str(self.date) + ' is concluded. The winner ballot is ' + self.winner
        return event_details

    def __str__(self):
        return self.checkStatus()


class Participant(models.Model):
    id = models.CharField(primary_key=True, blank=False, null=False, unique=True, max_length=20)
    password = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=200)
    register_date = models.CharField(default=getTodaysDate(), max_length=10)
    lottery_event = models.ForeignKey(Event, on_delete=CASCADE)


    def __str__(self):
        return self.name + '. Event: ' + self.lottery_event.date



class Ballot(models.Model):
    id = models.AutoField(primary_key=True)
    numbers = models.CharField(max_length=17)
    participant = models.ForeignKey(Participant, on_delete=CASCADE)
    lottery_event = models.ForeignKey(Event, on_delete=CASCADE)
    submission_date = models.CharField(default=getTodaysDate(), max_length=10)
    status = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.numbers


