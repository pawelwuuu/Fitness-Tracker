from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class DailyWeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight_kg = models.FloatField()
    date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']
    
    
