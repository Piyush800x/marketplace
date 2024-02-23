from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Register(User):
    email = forms.EmailField(required=True)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password']
