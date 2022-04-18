from django.db import models

from auth_service.models import Group


class TimeTable(models.Model):
    sheet_data = models.JSONField(null=False)
    group = models.OneToOneField(to=Group, on_delete=models.DO_NOTHING, null=True, blank=True, unique=True)


class Categories(models.Model):
    categories_list = models.JSONField(null=False)
    group = models.OneToOneField(to=Group, on_delete=models.DO_NOTHING, null=True, blank=True, unique=True)
