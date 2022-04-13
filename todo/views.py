from django.shortcuts import render


def create_task(request):
    return render(request, 'create_task.html')


def todo_list(request):
    return render(request, 'todo_list.html')


def task_view(request):
    return render(request, 'task_view.html')
