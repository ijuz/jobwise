from django.db import models
from userApp.models import CustomUser

class JobPosting(models.Model):  
    user = models.ForeignKey(CustomUser, models.CASCADE)
    job_title = models.CharField(max_length=100) 
    description = models.TextField()
    job_type = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    place = models.CharField(max_length=200)
    

    def __str__(self):
        return self.job_title


