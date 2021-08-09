from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date




class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)




