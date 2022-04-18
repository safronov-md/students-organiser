from django.shortcuts import render
from .models import TimeTable
from todo.models import Events
from django.http import JsonResponse


def dashboard(request):
    return render(request, 'dashboard.html')


def init_dashboard(request):
    response: dict = dict()
    time_sheet = TimeTable.objects.filter(group=request.user.group).first()
    task_and_events_by_group = Events.objects.filter(assignee_type='group', assignee=request.user.group.id).first()
    task_and_events_by_user = Events.objects.filter(assignee_type='user', assignee=request.user.id).first()
    response['time_sheet'] = time_sheet.sheet_data if time_sheet else None
    response['task_events_by_group'] = task_and_events_by_group.event_data if task_and_events_by_group else None
    response['task_events_by_user'] = task_and_events_by_user.event_data if task_and_events_by_user else None
    return JsonResponse(response)
