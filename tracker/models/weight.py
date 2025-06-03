from django.db import models
from django.contrib.auth.models import User

class DailyWeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight_kg = models.FloatField()
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']
