# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('display-messages/', views.display_contact_messages, name='display_messages'),
    path('mark-as-read/<int:message_id>/', views.mark_as_read, name='mark_as_read'),
]
