from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    types = (
        ('LAB', 'LAB'),
        ('CURS', 'CURS')
    )
    title = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=4, choices=types, null=False, default='CURS')
    meet_link = models.CharField(max_length=255, default='https://google.com/')

    def __str__(self):
        return f'[{self.type}] {self.title}'


class Schedule(models.Model):
    DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    TIME = (
        ('08:00 - 09:30', '08:00 - 09:30'),
        ('09:45 - 11:15', '09:45 - 11:15'),
        ('11:30 - 13:00', '11:30 - 13:00'),
        ('13:30 - 15:00', '13:30 - 15:00'),
        ('15:15 - 16:45', '15:15 - 16:45'),
        ('17:00 - 18:30', '17:00 - 18:30')
    )

    day = models.CharField(max_length=3, null=False, choices=DAYS)
    order = models.IntegerField(null=False, default=0)
    time = models.CharField(max_length=25, null=False, choices=TIME, default='UnTimed')
    title = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day} - {self.title}'


class Issue(models.Model):
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=70, default='Issue')
    issue = models.TextField(default="Issue description")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title