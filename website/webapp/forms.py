from .models import Authentication, Question
from django import forms


class AuthenticationForm(forms.ModelForm):
    sessionID = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Authentication
        fields = ['sessionID']



class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['body']