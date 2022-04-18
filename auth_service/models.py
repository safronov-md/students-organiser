from django.contrib.auth.models import AbstractUser
from django.db import models


class Group(models.Model):
    tag = models.CharField(max_length=10, null=False)


class Account(AbstractUser):
    group = models.OneToOneField(to=Group, on_delete=models.DO_NOTHING, null=True, blank=True)
    profile_image = models.CharField(max_length=255, default="static/img/undraw_profile.svg")

    def __str__(self):
        return self.username
