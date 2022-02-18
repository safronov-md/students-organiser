from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calendar_service.urls')),
    path('auth/', include('auth_service.urls')),
    path('issues/', include('issue_service.urls')),
    path('store/', include('store_service.urls'))
]
