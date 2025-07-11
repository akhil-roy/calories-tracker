from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    desc = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.calories} cal'