import datetime

from django.db import models
from django.utils import timezone

class Pet(models.Model):
    name = models.CharField(max_length = 64, null = True)

    def __str__(self):
        return f'{self.name}'

class Visitor(models.Model):
    visitor_name = models.CharField(max_length=200)
    visitor_email = models.EmailField('Email Address')

    def __str__(self):
        return self.visitor_name

class Schedule(models.Model):
    pet_name = models.ForeignKey(Pet, on_delete=models.CASCADE)
    schedule_name = models.CharField(max_length=200)
    start_date = models.DateField('First day of the watch')
    end_date = models.DateField('Last day of the watch')

    def __str__(self):
        return self.pets_name
    
class Visit(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)
    visit_date = models.DateField('Date of this visit')
    visit_time = models.TimeField('Time of the visit')
    needs_feeding = models.BooleanField('Serve food?', default = True)

    def __str__(self):
        return f'{self.visit_date}, {self.visit_time}'
    
