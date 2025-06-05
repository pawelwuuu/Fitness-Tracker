from django.urls import path
from . import views
from .views.calculator_views import calculate_bmi, calculate_bmr, calculate_tdee

urlpatterns = [
    path('', views.home, name='home'),
    path('bmi/', calculate_bmi, name='bmi_calculator'),
    path('bmr/', calculate_bmr, name='bmr_calculator'),
    path('tdee/', calculate_tdee, name='tdee_calculator'),
]
