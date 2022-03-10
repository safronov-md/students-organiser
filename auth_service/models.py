from django.db import models
from django.contrib.auth.models import User


class Teams(models.Model):
    title = models.CharField(max_length=35)

    def __str__(self):
        return self.title


class ExtendedUser(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    team = models.ForeignKey(to=Teams, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username