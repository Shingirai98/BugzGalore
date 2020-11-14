# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    emplID = models.AutoField(max_length=10, primary_key=True, editable=False, unique=True) #COMP###### - should be a
    # primary key
    company = models.TextField(max_length=20)


    address = models.TextField()
    phone = models.TextField(max_length=10) # all numbers are 10 digits long right?


    def __str__(self):
        return str(self.emplID)

