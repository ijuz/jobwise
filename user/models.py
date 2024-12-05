from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumber



class CustomeUser(AbstractUser):
    is_rekcruter = models.BooleanField(default=False)
    is_worker = models.CharField(default=False)
    phone_number = models.CharField(unique=True)
    
    
    def __str__(self):
        return self.username

class Signup(models.Model):
    user = models.OneToOneField(CustomeUser,on_delete=models.CASCADE)
    age = models.IntegerField(default=14)
    
    
    