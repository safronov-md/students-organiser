from django.urls import path

from auth_service import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
