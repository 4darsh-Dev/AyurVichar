from django import forms
from .models import PrakrutiResult

class PrakrutiForm(forms.ModelForm):
    class Meta:
        model = PrakrutiResult
        fields = []  # Exclude fields not needed in the form
