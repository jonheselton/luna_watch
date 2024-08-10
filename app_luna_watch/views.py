from django.db.models import F
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Schedule, Visit, Visitor, Pet
from .forms import PetSelection, PetForm, VisitorForm, ScheduleForm, VisitForm

def create_visits(schedule : Schedule) -> None:
    pass

def index(request):
    form = PetSelection()
    context = {'form' : form}
    return render(request, 'app_luna_watch/index.html', context)

def pets(request):
    form = PetSelection()
    context = {'form' : form}
    return render(request, 'app_luna_watch/index.html', context)

def pet_details(request, pet = None):
    if not pet:
        return HttpResponseRedirect(reverse('luna_watch:index'))
    pet = get_object_or_404(Pet, name = pet)
    return render(request, "app_luna_watch/pet_detail.html", {'pet': pet})

def add_pet(request):
    if request.POST.get('name', False):
        form = PetForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('luna_watch:pet_details', pet = request.POST.get('name', False)))
    elif request.POST.get('selected_pet', False) == "99" or  request.method == 'GET':
        form = PetForm()
        context = {'form' : form}
        return render(request, 'app_luna_watch/add_pet.html', context)
    else:
        pet = get_object_or_404(Pet, name = request.POST['selected_pet'])
        return pet_details(request, pet)

def add_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('luna_watch:index'))
    elif request.method == 'GET':
        form = VisitorForm()
        context = {'form' : form}
        return render(request, 'app_luna_watch/add_visitor.html', context)

def new_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        schedule = form.save()
        return HttpResponseRedirect(reverse('luna_watch:index'))
    else:
        form = ScheduleForm()
        return render(request, 'app_luna_watch/new_schedule.html', { 'form' : form})

def set_visits(request, schedule):
    formset = formset_factory(VisitForm, extra = (schedule.n_days() * schedule.visits_per_day) - 1)
    formset = formset(initial=[{'id': x.id} for x in some_objects])
