from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model): 
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
   
    
class Pay(models.Model):
    fullname =models.TextField(max_length=190)
    mpesacontact = models.TextField(max_length=190)
    amount = models.TextField(max_length=190)

class Message(models.Model):
    number =models.TextField(max_length=190)
    email = models.TextField(max_length=190)
    select_service = models.TextField(max_length=190)
    requirements = models.TextField(max_length=190)
    
