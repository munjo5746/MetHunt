from django.forms import ModelForm
from django import forms
from UserAuthentication.models import UserModel
class SignUpForm(ModelForm):
    """
    This form will be used in the sign up page.
    """

    Password = forms.CharField(max_length = 100, widget = forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ('UserName', 'Password', 'Email', 'FirstName', 'LastName')

class LoginForm(ModelForm):

    Password = forms.CharField(max_length = 100, widget = forms.PasswordInput())
    class Meta:
        model = UserModel
        fields = ('UserName', 'Password')
