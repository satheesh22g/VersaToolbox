# users/urls.py

from django.urls import path
from . import views
from .views import ProfileView,admin_user_management,password_change

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('admin_user_management/', admin_user_management, name='admin_user_management'),
    path('password_change/', views.password_change, name='password_change'),

    # Add other URL patterns as needed
]
