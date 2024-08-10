from django import forms
from .models import Pet, Visitor, Schedule, Visit

def pet_choices():
    pets =  [(x.name, x.name) for x in Pet.objects.all()]
    return pets

class PetSelection(forms.Form):
    selected_pet = forms.ChoiceField(label="Pet's Name", choices = pet_choices)

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name']

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['visitor_name', 'visitor_email']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['pet', 'start_date', 'end_date', 'visits_per_day', 'visit_times']

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['schedule', 'visitor', 'visit_datetime', 'needs_feeding']
