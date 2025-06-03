from django.db import models

class TrainingPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=100)  # np. "Początkujący", "Zaawansowany"

# extend this