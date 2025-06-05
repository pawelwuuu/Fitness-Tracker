from django.db import models
from django.core.validators import MinLengthValidator

class ExerciseTip(models.Model):
    CATEGORY_CHOICES = [
        ('STRENGTH', 'Trening siłowy'),
        ('CARDIO', 'Cardio'),
        ('FLEXIBILITY', 'Rozciąganie'),
        ('NUTRITION', 'Odżywianie'),
        ('RECOVERY', 'Regeneracja'),
    ]
    
    title = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    content = models.TextField(validators=[MinLengthValidator(20)])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"