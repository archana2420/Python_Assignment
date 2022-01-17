from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=200,label="Name")
    email = forms.EmailField(label="Email ")
    dob = forms.DateField(label="Date of Birth ")
    phone_number = forms.CharField(max_length=255,label="Phone no ")
    password=forms.CharField(max_length=100, widget=forms.PasswordInput, label="Password ")



