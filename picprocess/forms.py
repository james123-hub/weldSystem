from django import forms
from .models import Data

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['data']