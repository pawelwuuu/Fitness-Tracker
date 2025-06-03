from django.db import models

class Advice(models.Model):
    CATEGORY_CHOICES = [('diet', 'Dieta'), ('training', 'Trening'), ('health', 'Zdrowie')]

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

class EducationFact(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_myth = models.BooleanField(default=False)  # True = mit do obalenia
