from django.urls import path

from issue_service import views

urlpatterns = [
    path('', views.issues, name='issues'),
    path('add_issue/', views.add_issue, name='add_issue'),
    path('lesson/', views.lesson, name='lesson'),
    path('remove_issue/', views.remove_issue, name='remove_issue'),
    path('change_issue/', views.change_issue, name='change_issue'),
]
