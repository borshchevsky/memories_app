from django.contrib.auth.models import User
from django.db import models


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    lon = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
