from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home_view, calculate_bmi, calculate_bmr, calculate_tdee, register, user_weight_view, settings_view, custom_login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('bmi/', calculate_bmi, name='bmi_calculator'),
    path('bmr/', calculate_bmr, name='bmr_calculator'),
    path('tdee/', calculate_tdee, name='tdee_calculator'),
    path('register/', register, name="register"),
    path('weight/', user_weight_view, name='user_weight'),
    path('weight/add/', user_weight_view, name='user_weight_post'),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('settings/', settings_view, name='user_settings'),
    path('login/', custom_login_view, name='login'),
]
