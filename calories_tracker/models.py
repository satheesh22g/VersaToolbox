from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    
class Consume(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1.0)
    date = models.DateField(auto_now_add=True)  # Add this line for tracking date

    def __str__(self):
        return f"{self.user.username} consumed {self.food_consumed.name} on {self.date}"
