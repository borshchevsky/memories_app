from django.db import models


class Memory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lon = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
