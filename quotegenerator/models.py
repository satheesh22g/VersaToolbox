from django.db import models

class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.content[:50]}... - {self.author}'
