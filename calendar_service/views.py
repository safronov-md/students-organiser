from django.shortcuts import render
from .models import Schedule, Lesson, Issue


def calendar(request):
    schedule: list = list(Schedule.objects.all().order_by('order'))
    context = {
        'lessons': schedule,
    }
    return render(request, 'calendar/calendar.html', context)


def issues(request):
    issues: list = list(Issue.objects.all())
    context = {
        'issues': issues
    }
    return render(request, 'calendar/issues.html', context)
