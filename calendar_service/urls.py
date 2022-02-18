from django.urls import path

from calendar_service import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('issues/', views.issues, name='issues'),
    path('edit_schedule/', views.edit_schedule, name='edit_schedule'),
]
