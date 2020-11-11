from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """
    Adds on additional functionality to existing Django UserCreationForm
    (ie Email)
    """
    email = forms.EmailField()

    class Meta:
        """
        Nested namespace for configuration on User model
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
