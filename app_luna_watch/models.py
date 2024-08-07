from datetime import date

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
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_date = models.DateField('First day of the watch')
    end_date = models.DateField('Last day of the watch')
    visits_per_day = models.IntegerField(name = 'visits_per_day', default = 3)
    visit_times = models.CharField(name = 'visit_times', max_length = 64,
        default = '07:00 AM, 12:00 PM, 5:00 PM')
    
    def n_days(self) -> int:
        return (self.end_date - self.start_date).days + 1
    
    def __str__(self):
        print_string = f"{self.start_date.strftime('%d %B')} to {self.end_date.strftime('%d %B %Y')}"
        return print_string

class Visit(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)
    visit_date = models.DateField('Date of this visit')
    visit_time = models.TimeField('Time of the visit')
    needs_feeding = models.BooleanField('Serve food?', default = True)
    scheduled = models.BooleanField('Visit Scheduled', default = False)
    def __str__(self):
        return f'{self.visit_date}, {self.visit_time}'
    

