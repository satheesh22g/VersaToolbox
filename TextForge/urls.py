# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate-fake-profile/', views.generate_profile, name='generate_profile'),
    path('generate-fake-address/', views.generate_address, name='generate_address'),
]
