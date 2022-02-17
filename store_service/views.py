from django.shortcuts import render,redirect
from .models import Storage
from django.forms.models import model_to_dict
from django.http import JsonResponse


def _upload_file(f, user):
    dist = ''.join(['static/files/', f.name])
    type: str = str()
    if 'pdf' in f.name:
        type = 'doc'
    file = Storage(destination=dist, user_id=user, type=type, name=f.name)
    file.save()  # Добавялем информацию по файлу в базу данных
    with open(dist, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return dist.replace('static/files/', '')


def querySet_to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]


def get_stored_files(request):
    data = request.GET
    files_type = data.get('type')
    files: list = querySet_to_list(Storage.objects.filter(user_id=request.user, type=files_type).values())
    return JsonResponse({'files': files})


def add_file(request):
    if request.FILES.get("add_file"):
        file = request.FILES.get('add_file')
        _upload_file(file, request.user)
    return redirect('calendar')


def remove_file(request):
    data = request.GET
    Storage.objects.filter(id=data['id']).delete()
    return redirect('calendar')


