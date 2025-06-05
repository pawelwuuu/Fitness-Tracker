from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from tracker.calculators.bmi import BMICalculator
from tracker.calculators.bmr import BMRCalculator
from tracker.calculators.tdee import TDEECalculator

def calculate_bmi(request):
    if request.method == 'POST':
        print("Raw POST data:", request.POST)  # Debugowanie danych wejściowych
        
        try:
            weight = float(request.POST.get('weight', 0))
            height = float(request.POST.get('height', 0))
            
            print(f"Received weight: {weight}, height: {height}")  # Debugowanie
            
            if weight <= 0 or height <= 0:
                raise ValidationError("Waga i wzrost muszą być dodatnie")
            
            calculator = BMICalculator(weight, height)
            bmi = calculator.calculate()
            
            return JsonResponse({
                'status': 'success',
                'result': bmi,
                'interpretation': interpret_bmi(bmi)
            })
            
        except Exception as e:
            print("Error:", str(e))  # Logowanie błędów
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return render(request, 'tracker/bmi_calculator.html')

def calculate_bmr(request):
    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight', 0))
            height = float(request.POST.get('height', 0))
            age = int(request.POST.get('age', 0))
            gender = request.POST.get('gender', '').lower()
            
            if weight <= 0 or height <= 0 or age <= 0:
                raise ValidationError("Waga, wzrost i wiek muszą być dodatnie")
            
            if gender not in ['male', 'female']:
                raise ValidationError("Płeć musi być 'male' lub 'female'")
            
            calculator = BMRCalculator(weight, height, age, gender)
            bmr = calculator.calculate()
            
            return JsonResponse({
                'status': 'success',
                'result': bmr
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return render(request, 'tracker/bmr_calculator.html')

def calculate_tdee(request):
    if request.method == 'POST':
        try:
            bmr = float(request.POST.get('bmr', 0))
            activity_level = request.POST.get('activity_level', '').lower()
            
            if bmr <= 0:
                raise ValidationError("BMR musi być dodatni")
            
            calculator = TDEECalculator(bmr, activity_level)
            tdee = calculator.calculate()
            
            return JsonResponse({
                'status': 'success',
                'result': tdee
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return render(request, 'tracker/tdee_calculator.html')

# Funkcja pomocnicza do interpretacji BMI
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi < 25:
        return "Waga prawidłowa"
    elif 25 <= bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"