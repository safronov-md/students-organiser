from django.urls import path

from todo import views as todo_views


urlpatterns = [
    path('new_task', todo_views.create_task, name='create_task_view'),
    path('', todo_views.todo_list, name='todo_list_view'),
    path('task_view', todo_views.task_view, name='task_view'),
]