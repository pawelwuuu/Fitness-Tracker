
from django import forms
from tracker.models import ProgressPhoto

class ProgressPhotoForm(forms.ModelForm):
    class Meta:
        model = ProgressPhoto
        fields = ['photo']
