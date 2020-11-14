from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Employee


@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    print("Saved and employee")
    if created:
        print("Created employee")
        Employee.objects.create(employee=instance, company="", phone="", address="")
