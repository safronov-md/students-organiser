from django.urls import path

from dashboard import views as dashboard_views


urlpatterns = [
    path('', dashboard_views.dashboard, name='dashboard_view'),
    path('init', dashboard_views.init_dashboard, name='init_dashboard'),
]

