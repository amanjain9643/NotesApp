from django.db import models
from django.contrib.auth.models import User
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    note=models.CharField(max_length=10000)
    time=models.TimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.date} {self.time} - {self.note[:50]}"  