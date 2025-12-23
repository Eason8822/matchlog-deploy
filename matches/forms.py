from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Match


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["date", "team", "opponent", "score_for", "score_against", "note"]
