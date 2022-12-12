from django.db import models
from django.conf import  settings 
# Create your models here.
from django.contrib.auth.models import AbstractUser

import uuid

class User(AbstractUser):
    gender = (
        ('male','male'),
        ('female','female'),
    )
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # nickname = models.CharField(max_length=50, blank=True)
    # sex = models.CharField(max_length=32,choices=gender,default='male')
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
 
    class Meta(AbstractUser.Meta):
        pass

