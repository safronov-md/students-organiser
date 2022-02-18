from django.shortcuts import render, redirect
from .models import Schedule, Lesson, Issue
from django.db import connection


def calendar(request):
    schedule: list = list(Schedule.objects.all().order_by('order'))
    context = {
        'lessons': schedule,
    }
    return render(request, 'calendar/calendar.html', context)


def issues(request):
    manager = connection.cursor()
    manager.execute('select lesson_id,status,count(issue) from calendar_service_issue group by lesson_id,status;')

    dataDict: dict = dict()
    for data in manager.fetchall():
        lesson_id, status, count = data

        if lesson_id in dataDict.keys():
            dataDict[lesson_id]['Done'] = count if status is True else dataDict[lesson_id]['Done']
            dataDict[lesson_id]['New'] = count if status is False else dataDict[lesson_id]['New']
        else:
            dataDict[lesson_id] = {
                'Done': count if status is True else 0,
                'New': count if status is False else 0,
            }
    lessons = Lesson.objects.filter(id__in=dataDict.keys())
    context = {
        'lessons': lessons,
        'issueData': dataDict
    }
    return render(request, 'calendar/issues.html', context)


def edit_schedule(request):
    data = request.POST
    for key in data.keys():
        if key != 'csrfmiddlewaretoken':
            lesson = Lesson.objects.get(id=int(key))
            lesson.meet_link = data.get(key)
            lesson.save()
    return redirect('calendar')
