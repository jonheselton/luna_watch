from django.urls import path

from . import views

app_name = 'app_luna_watch'
urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name = 'pets'),
    path('<pet>/pet_details', views.pet_details, name = 'pet_details')
]
