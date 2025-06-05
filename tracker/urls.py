from django.urls import path
from .views import home_view, calculate_bmi, calculate_bmr, calculate_tdee, register


urlpatterns = [
    path('', home_view, name='home'),
    path('bmi/', calculate_bmi, name='bmi_calculator'),
    path('bmr/', calculate_bmr, name='bmr_calculator'),
    path('tdee/', calculate_tdee, name='tdee_calculator'),
    path('register/', register, name="register")
]
