from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Address(models.Model):
     name = models.CharField(max_length=255)
     address = models.CharField(max_length=255)
     
     def __str__(self):
          return self.name
