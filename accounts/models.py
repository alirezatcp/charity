from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOISES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1 , choices=GENDER_CHOISES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
