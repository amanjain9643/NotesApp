from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
from django.contrib.auth import get_user_model
from .utils import *

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    slug=models.CharField(unique=True,max_length=100)
    note=models.CharField(max_length=10000)
    time=models.TimeField(auto_now=True)

    def save(self,*args,**kwargs):
        self.slug=generate_slug(self.note)
        super(Notes,self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.date} {self.time} - {self.note[:50]}"  


class CustomUser(AbstractBaseUser):
    username=None
    phone_number=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    user_bio=models.CharField(max_length=50)

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]

    objects=UserManager()