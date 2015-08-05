from django.forms import ModelForm
from django import forms
from UserAuthentication.models import UserModel
from django.contrib.auth.models import User

class SignUpForm(ModelForm):
    """
    This form will be used in the sign up page.
    """

    password = forms.CharField(max_length = 100, widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class LoginForm(ModelForm):

    password = forms.CharField(max_length = 100, widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')
