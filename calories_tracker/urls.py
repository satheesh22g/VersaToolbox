
# calorie_tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('calories/', views.c_index, name="c_index"),
        path('delete/<int:id>/', views.delete_consume, name="delete"),
]