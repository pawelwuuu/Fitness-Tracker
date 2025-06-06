from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from tracker.models import DailyWeightEntry, UserProfile
from tracker.calculators import BMRCalculator

class GoalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['goal', 'weekly_goal_kg']
        widgets = {
            'goal': forms.NumberInput(attrs={'step': '0.1'}),
            'weekly_goal_kg': forms.NumberInput(attrs={'step': '0.01'}),
        }

@login_required
def user_weight_view(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        if 'weight_kg' in request.POST:
            weight_raw = request.POST.get('weight_kg')
            try:
                weight = float(weight_raw)
                note = request.POST.get('note', '')
                today = timezone.now().date()

                entry, created = DailyWeightEntry.objects.update_or_create(
                    user=request.user,
                    date=today,
                    defaults={'weight_kg': weight, 'note': note}
                )

                if created:
                    messages.success(request, 'Weight added.')
                else:
                    messages.success(request, 'Weight updated.')
            except (ValueError, TypeError):
                messages.error(request, 'Invalid weight value.')
            return redirect('user_weight')

        elif 'goal' in request.POST or 'weekly_goal_kg' in request.POST:
            form = GoalForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Goals updated.')
                return redirect('user_weight')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = GoalForm(instance=profile)

    entries = DailyWeightEntry.objects.filter(user=request.user).order_by('date')
    weight_data = []

    previous_weight = None
    for entry in entries:
        change = None
        direction = None
        if previous_weight is not None:
            diff = round(entry.weight_kg - previous_weight, 2)
            if diff > 0:
                change = f"+{diff} kg"
                direction = "↑"
            elif diff < 0:
                change = f"{diff} kg"
                direction = "↓"
            else:
                change = "0 kg"
                direction = "→"
        weight_data.append({
            'date': entry.date,
            'weight_kg': entry.weight_kg,
            'note': entry.note,
            'change': change,
            'direction': direction
        })
        previous_weight = entry.weight_kg

    calorie_info = None
    if profile.goal is not None and profile.weekly_goal_kg is not None and entries.exists():
        current_weight = entries.last().weight_kg
        age = (timezone.now().date() - profile.birth_date).days // 365
        gender_map = {'M': 'male', 'F': 'female', 'O': 'female'}  # możesz zmienić obsługę 'O'
        gender = gender_map.get(profile.gender, 'female')
        bmr_calc = BMRCalculator(weight=current_weight, height=profile.height_cm, age=age, gender=gender)
        bmr = bmr_calc.calculate()
        
        weekly_goal = profile.weekly_goal_kg
        surplus = (7700 * abs(weekly_goal)) / 7
        if weekly_goal > 0:
            calories_needed = bmr + surplus
        else:
            calories_needed = bmr - surplus
        
        calorie_info = {
            'calories_needed': round(calories_needed),
            'weekly_goal': weekly_goal,
            'current_weight': current_weight,
            'bmr': bmr,
            'age': age,
        }

    return render(request, 'tracker/user_weight.html', {
        'weight_data': weight_data,
        'entries': entries,
        'form': GoalForm(instance=profile),
        'calorie_info': calorie_info,
    })