from django.contrib.auth.models import User
from django.db import models


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'memories'

    def __str__(self):
        return f'{self.user} {self.title}'
