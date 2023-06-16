from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    img=models.ImageField(upload_to='myimages',null=True,blank=True)
    email=models.EmailField()
    Address=models.TextField(null=True,blank=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

 

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)




