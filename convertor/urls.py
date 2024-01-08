from django.urls import path
from . import views

urlpatterns = [
    path('convertor/', views.convert_home),
    path('jpgtopdf/', views.jpgToPdf),
    path('pdftojpg/', views.pdftojpg),
]
