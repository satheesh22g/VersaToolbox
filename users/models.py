from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(default=0)  # Add a field for rating
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f'{self.name} - {self.created_at}'

class ErrorReport(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    error_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    screenshot = models.ImageField(upload_to='error_screenshots/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.created_at}'

    def __str__(self):
        return f'{self.name} - {self.created_at}'
