from django.db import models
from django.conf import settings


class Incident(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    resolution = models.TextField(null=True, blank=True)
    resolved = models.BooleanField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
