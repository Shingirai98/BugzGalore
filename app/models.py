# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from authentication.models import Employee
from django.utils import timezone

# Create your models here.
class HealthRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now)
    cough = models.BooleanField()
    sneeze = models.BooleanField()
    recentExposure = models.BooleanField()
    fever = models.BooleanField()

    def __str__(self):
        return self.employee

    def __repr__(self):
        return str(self.employee)