from datetime import date, datetime, timedelta

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
    
    def visit_list(self) -> list:
        visits = []
        for i in range(self.n_days()):
            visits += [datetime.strptime(f'{self.start_date} {x} +0500', '%Y-%m-%d %I:%M %p %z') + timedelta(days = i) for x in self.visit_times.split(', ')]
        return visits
    
    def n_days(self):
        days = self.end_date - self.start_date
        return days.days + 1

    def __str__(self):
        print_string = f"{self.start_date.strftime('%d %B')} to {self.end_date.strftime('%d %B %Y')}"
        return print_string

class Visit(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, null = True, on_delete=models.SET_NULL)
    visit_datetime = models.DateTimeField('Date and Time of the visit')
    needs_feeding = models.BooleanField('Serve food?', default = True)
    
    def __str__(self):
        return f'{self.visit_datetime}'
    

