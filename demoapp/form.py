from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length = 100, required = True)
    username = forms.CharField(max_length= 100, required = True)
    Email = forms.CharField(max_length=100, required =True)
    password = forms.CharField(max_length=100, required =True, widget = forms.PasswordInput)
    re_password = forms.CharField(max_length=20, required=True,widget = forms.PasswordInput)


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "username","password"
    