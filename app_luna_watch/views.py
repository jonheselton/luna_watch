from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Schedule, Visit, Visitor, Pet

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    template_name = 'app_luna_watch/index.html'

def pets(request):
    pet_list = Pet.objects.all()
    output = [p.name for p in pet_list]
    context = {'pet_list' : pet_list}
    return render(request, 'app_luna_watch/index.html', context)

def pet_details(request, pet):
    pet = get_object_or_404(Pet, name = pet)
    return render(request, "app_luna_watch/pet_detail.html", {'pet': pet})
