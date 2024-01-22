# users/urls.py

from django.urls import path
from . import views
from .views import ProfileView,admin_user_management,feedback,view_reports
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('admin-user_management/', admin_user_management, name='admin_user_management'),
    path('password-change/', views.password_change, name='password_change'),


    path('feedback/', feedback, name='feedback'),
    path('view-reports', view_reports, name='view_reports'),


]
