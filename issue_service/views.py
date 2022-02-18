import os
from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render,redirect
from issue_service.models import Issue
from calendar_service.models import Lesson


def add_issue(request) -> None:
    data = request.POST
    dist: str = ''
    if request.FILES.get('doc'):
        dist = ''.join([f'static/files/{request.user.id}/', request.FILES.get('doc').name])
        if not os.path.exists(f'static/files/{request.user.id}/'): os.makedirs(f'static/files/{request.user.id}/')
        with open(dist, 'wb+') as destination:
            for chunk in request.FILES.get('doc').chunks():
                destination.write(chunk)
    file = Issue(lesson=Lesson.objects.get(id=data.get('lesson')), user=request.user, title=data.get('title'),
                 issue=data.get('desc'), issueDoc=dist)
    file.save()  # Добавялем информацию по файлу в базу данных

    return redirect('issues')


def remove_issue(request):
    data = request.GET
    issue = Issue.objects.get(id=data.get('id'))
    if os.path.exists(str(issue.answerFile)): os.remove(str(issue.answerFile))
    if os.path.exists(str(issue.issueDoc)): os.remove(str(issue.issueDoc))
    issue.delete()
    return redirect('issues')


def change_issue(requset):
    data = requset.GET
    issue_id = data.get('id').split('_')[1]
    issue = Issue.objects.get(id=issue_id)
    if data.get('status', False):
        issue.status = True if data.get('status') == 'true' else False
    elif data.get('desc', False):
        issue.issue = data.get('desc')
    issue.save()
    return JsonResponse({'_status': 'OK'})


def issues(request):
    manager = connection.cursor()
    manager.execute(
        f'select lesson_id,status,count(issue) from issue_service_issue where user_id={request.user.id} group by lesson_id,status;')

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
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons,
        'issueData': dataDict
    }
    return render(request, 'issues/issues.html', context)


def lesson(request):
    data = request.GET
    issuesList = list(Issue.objects.filter(lesson_id=data.get('id'), user_id=request.user.id))
    context = {
        'issues': issuesList
    }
    return render(request, 'issues/lesson.html', context)
