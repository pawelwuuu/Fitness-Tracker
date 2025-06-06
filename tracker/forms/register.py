from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from tracker.models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'border border-gray-300 rounded-md p-2 w-full',
        'placeholder': 'Email'
    }))
    height_cm = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'border border-gray-300 rounded-md p-2 w-full',
        'placeholder': 'Wzrost w cm'
    }))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'border border-gray-300 rounded-md p-2 w-full',
    }))
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES, widget=forms.Select(attrs={
        'class': 'border border-gray-300 rounded-md p-2 w-full',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'height_cm', 'birth_date', 'gender']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-md p-2 w-full',
            'placeholder': 'Nazwa użytkownika'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-md p-2 w-full',
            'placeholder': 'Hasło'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-md p-2 w-full',
            'placeholder': 'Powtórz hasło'
        })

    def save(self, commit=True):
        user = super().save(commit)
        UserProfile.objects.create(
            user=user,
            height_cm=self.cleaned_data['height_cm'],
            birth_date=self.cleaned_data['birth_date'],
            gender=self.cleaned_data['gender'],
        )
        return user
