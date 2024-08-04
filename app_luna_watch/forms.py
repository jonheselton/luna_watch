from django import forms
from .models import Pet, Visitor

def pet_choices():
    pets =  list(enumerate(Pet.objects.all(), start = 1))
    pets.append((99, '<Add Pet>'))
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
