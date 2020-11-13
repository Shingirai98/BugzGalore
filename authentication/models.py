# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=20)
    surname = models.TextField(max_length=20)
    emplID = models.TextField(max_length=10) #COMP###### - should be a primary key
    email = models.EmailField()

    address = models.TextField()
    phoneNumber = models.TextField(max_length=10) # all numbers are 10 digits long right?


    def __str__(self):
        return self.emplID

