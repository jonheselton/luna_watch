from django.urls import path

from . import views

app_name = 'luna_watch'
urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name = 'pets'),
    path('add_pet/', views.add_pet, name = 'add_pet'),
    path('pet_details/', views.pet_details, name = 'pet_details')
]
