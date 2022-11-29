from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender = (
        ('male','male'),
        ('female','female'),
    )
    nickname = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=32,choices=gender,default='male')

 
    class Meta(AbstractUser.Meta):
        pass

