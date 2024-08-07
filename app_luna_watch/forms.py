from django import forms
from .models import Pet, Visitor, Schedule

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

# class NewSchedule(forms.Form):
#     pet = forms.ChoiceField(choices = pet_choices)
#     start_date = forms.DateField(label = 'First day of the watch')
#     end_date = forms.DateField(label = 'Last day of the watch')
#     visits_per_day = forms.IntegerField(label = 'visits_per_day', initial = 3)
#     visit_times = forms.CharField(label = 'visit_times', max_length = 64,
#         initial = '07:00 AM, 12:00 PM, 5:00 PM')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['pet', 'start_date', 'end_date', 'visits_per_day', 'visit_times']
