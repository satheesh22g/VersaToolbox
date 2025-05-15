from zoneinfo import ZoneInfo

from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.sent_at:
            self.sent_at = timezone.now().astimezone(ZoneInfo("Asia/Kolkata"))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.subject}"
