from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField(verbose_name='Date of birth')
    phone_no_regex=RegexValidator(regex=r'^[7-9]\d{9}$',message='Phone number must be 10 digits')
    phone_number=models.CharField(validators=[phone_no_regex],max_length=10)
    password_regex=RegexValidator(regex=r'[a-zA-Z0-9]{8}$',message='Password must be of 8 characters(only alphabets and anumbers allowed)')
    password=models.CharField(validators=[password_regex],max_length=100)

    def __str__(self):
        return self.name