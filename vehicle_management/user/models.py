from django.db import models
from django.contrib.auth.models import AbstractUser
from vehicles.models import Vehicle
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    # Add any additional fields or methods here
    user_access = models.CharField(_('User Access'), max_length=10, choices=Vehicle.ACCESS_CHOICES)