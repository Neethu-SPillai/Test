from django.db import models

#Create your models here.

class Vehicle(models.Model):
    ACCESS_CHOICES = (
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()
    user_access = models.CharField(max_length=10, choices=ACCESS_CHOICES)