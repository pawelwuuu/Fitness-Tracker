from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = [('M', 'Mężczyzna'), ('F', 'Kobieta')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height_cm = models.PositiveIntegerField()
    current_weight_kg = models.FloatField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    goal = models.CharField(max_length=255)  # np. "schudnąć", "utrzymać", "zbudować masę"

    def __str__(self):
        return self.user.username
