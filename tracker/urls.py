from django.urls import path
from .views import home_view  # This should work now
from .views.calculator_views import calculate_bmi, calculate_bmr, calculate_tdee

urlpatterns = [
    path('', home_view, name='home'),
    path('bmi/', calculate_bmi, name='bmi_calculator'),
    path('bmr/', calculate_bmr, name='bmr_calculator'),
    path('tdee/', calculate_tdee, name='tdee_calculator'),
    path('', home_view, name='home'),
]
