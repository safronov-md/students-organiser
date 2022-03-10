from django.contrib.auth.models import User
from django.db import models
from calendar_service.models import Lesson
import datetime


class Issue(models.Model):
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=1, blank=False)
    title = models.CharField(max_length=70, default='Issue')
    issue = models.TextField(default="Issue description")
    issueDoc = models.FileField(default='', upload_to='static', blank=True)
    answerFile = models.FileField(default='', upload_to='static', blank=True)
    status = models.BooleanField(default=False)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.lesson} - {self.title}'
