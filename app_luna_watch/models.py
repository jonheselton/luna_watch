import datetime

from django.db import models
from django.utils import timezone

class Schedule(models.Model):
    pets_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('First day of the watch')
    end_date = models.DateField('Last day of the watch')


class Visit(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    visit_datetime = models.DateTimeField('Date and Time of this visit')
    needs_feeding = models.BooleanField('Serve food?')

class Visitor(models.Modl):
    visitor_name = models.CharField(max_length=200)
    visitor_email = models.EmailField('Email Address')
    pets_name = models.Fore
