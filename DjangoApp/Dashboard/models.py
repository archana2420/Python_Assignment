from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField(verbose_name='Date of birth')
    phone_number=models.CharField(max_length=255)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name