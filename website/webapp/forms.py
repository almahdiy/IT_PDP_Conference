from .models import Authentication
from django import forms


class AuthenticationForm(forms.ModelForm):
    sessionID = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Authentication
        fields = ['sessionID']