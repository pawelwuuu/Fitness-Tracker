from django.shortcuts import render
from tracker.models.exercise_tips import ExerciseTip
import random

def home_view(request):
    # Pobieramy tylko aktywne porady
    active_tips = ExerciseTip.objects.filter(is_active=True)
    
    if active_tips.exists():
        random_tip = random.choice(active_tips)
    else:
        random_tip = None
    
    context = {
        'random_tip': random_tip
    }
    return render(request, 'tracker/home.html', context)