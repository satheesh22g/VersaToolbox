# quotegenerator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('quote-generate/', views.generate_quote, name='generate_quote'),
]
