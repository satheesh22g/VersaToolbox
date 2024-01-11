# users/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user
        return super().authenticate(request, username, password, **kwargs)
