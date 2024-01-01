from django.urls import path
from . import views

urlpatterns = [
    path('display-messages/', views.display_contact_messages, name='display_messages'),
]
