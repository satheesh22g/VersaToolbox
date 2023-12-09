from django.urls import path
from . import views

urlpatterns = [
    path('plagiarism/', views.plagiarism_check, name='plagiarism_check'),
    path('marks_calculation/', views.marks_calculation, name='marks_calculation'),
]
