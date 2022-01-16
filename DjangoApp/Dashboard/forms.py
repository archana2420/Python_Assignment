from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserInfo

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=200,label="Name")
    email = forms.EmailField(label="Email ")
    dob = forms.DateField(label="Date of Birth ")
    phone_number = forms.CharField(max_length=255,label="Phone no ")
    password=forms.CharField(max_length=100,widget=forms.PasswordInput,label="Password ")

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['first_name','email','dob','phone_number','password']



class LoginForm(forms.Form):
    email = forms.EmailField(label="Email ")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)