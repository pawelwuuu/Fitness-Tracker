from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ProgressPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='progress_photos/')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']