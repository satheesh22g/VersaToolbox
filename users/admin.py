# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    
    # Customize the display fields, list filters, fieldsets, etc., as needed

admin.site.register(CustomUser, CustomUserAdmin)

