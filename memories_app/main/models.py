from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('memory-detail', args=[str(self.id)])
