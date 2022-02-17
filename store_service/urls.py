from django.urls import path

from store_service import views

urlpatterns = [
    path('add/', views.add_file, name='add_file'),
    path('get_files/', views.get_stored_files, name='get_files'),
    path('remove_file/', views.remove_file, name='remove_file'),
]
