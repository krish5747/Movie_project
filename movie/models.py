from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class moviedatabase(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    rating=models.FloatField()
    image=models.ImageField(upload_to="images/")

class user (models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    rating=models.FloatField()
    date=models.DateField(default=timezone.now())
    




    
