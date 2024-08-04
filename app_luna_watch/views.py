from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Schedule, Visit, Visitor, Pet
from .forms import PetSelection, PetForm

def index(request):
    form = PetSelection()
    context = {'form' : form}
    return render(request, 'app_luna_watch/index.html', context)

def pets(request):
    form = PetSelection()
    context = {'form' : form}
    return render(request, 'app_luna_watch/index.html', context)

def pet_details(request, pet):
    pet = get_object_or_404(Pet, name = pet)
    return render(request, "app_luna_watch/pet_detail.html", {'pet': pet})

def add_pet(request):
    if request.POST.get('name', False):
        form = PetForm(request.POST)
        form.save()
        return pet_details(request, request.POST.get('name'))
#        return HttpResponseRedirect(reverse('luna_watch:pets'))
    elif request.POST.get('selected_pet', False) == "99" or  request.method == 'GET':
        form = PetForm()
        context = {'form' : form}
        return render(request, 'app_luna_watch/add_pet.html', context)
    else:
        pet = get_object_or_404(Pet, id = int(request.POST['selected_pet']))
        return pet_details(request, pet)

