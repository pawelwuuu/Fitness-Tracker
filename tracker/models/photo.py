from django.db import models
from django.contrib.auth.models import User

class ProgressPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='progress_photos/')
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
