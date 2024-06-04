from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Schedule, Visit, Visitor

class IndexView(generic.ListView):
    template_name = "app_luna_watch/index.html"

    def get_queryset(self):
        """Return the list of visits"""
        return Visit

