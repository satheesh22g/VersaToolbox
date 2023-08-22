from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.dashboard),
    path('qr/',views.qr),
]