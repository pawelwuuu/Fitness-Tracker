from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from tracker.forms.user_settings import UserProfileForm, UserForm
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def settings_view(request):
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)
    password_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        password_form = PasswordChangeForm(request.user, request.POST)

        if 'update_profile' in request.POST:
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect('user_settings')

        elif 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password changed successfully.")
                return redirect('user_settings')
            else:
                messages.error(request, "Please correct the errors in the password form.")

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form
    }
    return render(request, 'account/settings.html', context)
