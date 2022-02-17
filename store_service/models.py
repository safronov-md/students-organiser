from django.db import models
from django.contrib.auth.models import User


class Storage(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=10, null=False, default='undefined')
    name = models.CharField(max_length=30, null=False, default='undefined')
