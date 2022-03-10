import json
import os
from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render, redirect
from issue_service.models import Issue
from calendar_service.models import Lesson
from datetime import datetime


def upload_file(user_id, file):
    dist = ''.join([f'static/files/{user_id}/', file.name])
    if not os.path.exists(f'static/files/{user_id}/'):
        os.makedirs(f'static/files/{user_id}/')
    with open(dist, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return dist


def add_issue(request) -> None:
    data = request.POST
    deadline = None
    if data.get('deadline'):
        deadline = datetime.strptime(data['deadline'], '%Y-%m-%dT%H:%M')
    dist: str = ''
    if request.FILES.get('doc'):
        dist = upload_file(request.user.id, request.FILES.get('doc'))
    file = Issue(lesson=Lesson.objects.get(id=data.get('lesson')),
                 user=request.user, title=data.get('title'),
                 issue=data.get('desc'), issueDoc=dist,
                 end_date=deadline)
    file.save()  # Добавялем информацию по файлу в базу данных

    return redirect('issues')


def upload_issue_answer(request):
    data = request.POST
    dist: str = ''
    doc_name = f"doc_{data.get('id').split('_')[1]}"
    if request.FILES.get(doc_name):
        dist = upload_file(request.user.id, request.FILES.get(doc_name))
    file = Issue.objects.get(id=data.get('id').split('_')[1])
    if data.get('type') == 'answer':
        if os.path.exists(str(file.answerFile)): os.remove(str(file.answerFile))
        file.answerFile = dist
    elif data.get('type') == 'issue':
        if os.path.exists(str(file.issueDoc)): os.remove(str(file.issueDoc))
        file.issueDoc = dist
    file.save()

    return redirect(request.META['HTTP_REFERER'])


def remove_issue(request):
    data = request.GET
    issue = Issue.objects.get(id=data.get('id'))
    if os.path.exists(str(issue.answerFile)): os.remove(str(issue.answerFile))
    if os.path.exists(str(issue.issueDoc)): os.remove(str(issue.issueDoc))
    issue.delete()
    return redirect(request.META['HTTP_REFERER'])


def change_issue(request):
    data = request.GET if request.method == 'GET' else json.loads(request.body)
    deadline = datetime.strptime(data['deadline'], '%Y-%m-%dT%H:%M') if data.get('deadline') else None
    issue_id = data.get('id')
    issue = Issue.objects.get(id=issue_id)
    if data.get('status', False):
        issue.status = True if data.get('status') == 'true' else False
    if 'desc' in data.keys():
        issue.issue = data.get('desc')
        issue.end_date = deadline
    issue.save()
    deadline = issue.end_date.strftime("%b. %d, %Y, %I:%M %p") if deadline else None
    return JsonResponse({'_status': 'OK',
                         'date': deadline})


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
    issuesList = list(Issue.objects.filter(lesson_id=data.get('id'), user_id=request.user.id).order_by('id'))
    issuesList.reverse()
    context = {
        'issues': issuesList
    }
    return render(request, 'issues/lesson.html', context)
