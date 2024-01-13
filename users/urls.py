# users/urls.py

from django.urls import path
from . import views
from .views import ProfileView

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # Add other URL patterns as needed
]
