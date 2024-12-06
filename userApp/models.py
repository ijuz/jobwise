from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField()
    is_workker = models.BooleanField(default=False,blank=True,null=True)
    is_recruiter = models.BooleanField(default=False,blank=True,null=True)
    

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    age = models.IntegerField(default=18)
    full_name = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
