from django.db import models


class Events(models.Model):
    event_data = models.JSONField(null=False)
    type = models.CharField(max_length=10)
    assignee_type = models.CharField(max_length=15)
    assignee = models.IntegerField()
    category = models.IntegerField()
    attachments = models.FileField(null=True, blank=True)
